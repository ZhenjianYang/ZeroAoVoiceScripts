from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c000b.bin",                # FileName
        "c000b",                    # MapName
        "c000b",                    # Location
        0x0002,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 2, 0, 2, 0, 3],
    )

    BuildStringList((
        "c000b",                  # 0
        "瓦吉",                   # 1
        "瓦鲁多",                 # 2
        "列车",                   # 3
        "SE控制",                 # 4
        "中央广场",               # 5
        "西街",                   # 6
        "行政区",                 # 7
        "住宅街",                 # 8
        "欢乐街",                 # 9
        "东街",                   # 10
        "旧城区",                 # 11
        "港湾区",                 # 12
        "ＩＢＣ",                 # 13
        "站前街道",               # 14
        "后巷",                   # 15
        "乌尔斯拉间道",           # 16
        "东克洛斯贝尔街道",       # 17
        "西克洛斯贝尔街道",       # 18
        "玛因兹山道",             # 19
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    PlaceName(-9.25, 0.0, 67.0, 0x0000, 0x0000, "中央广场")
    PlaceName(-75.0, 0.0, 71.5, 0x0000, 0x0000, "西街")
    PlaceName(17.75, 0.0, 156.0, 0x0000, 0x0000, "行政区")
    PlaceName(-136.0, 0.0, 146.0, 0x0000, 0x0000, "住宅街")
    PlaceName(-63.0, 0.0, 138.0, 0x0000, 0x0000, "欢乐街")
    PlaceName(72.0, 0.0, 44.0, 0x0000, 0x0000, "东街")
    PlaceName(107.5, 0.0, -11.0, 0x0000, 0x0000, "旧城区")
    PlaceName(100.0, 0.0, 110.0, 0x0000, 0x0000, "港湾区")
    PlaceName(74.0, 0.0, 204.0, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(2.0, 0.0, -2.0, 0x0000, 0x0000, "站前街道")
    PlaceName(-45.0, 0.0, 102.0, 0x0000, 0x0000, "后巷")
    PlaceName(-1.0, 0.0, -33.0, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(126.0, 0.0, 58.0, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-126.0, 0.0, 70.0, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-120.0, 0.0, 170.0, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(-31.25, 0.0, 53.0, 0x0000, 0x0051, "")
    PlaceName(22.5, 0.0, 79.0, 0x0000, 0x0054, "")
    PlaceName(-6.75, 0.0, 45.0, 0x0000, 0x0057, "")
    PlaceName(-32.0, 0.0, 82.0, 0x0000, 0x0053, "")
    PlaceName(-11.5, 0.0, 106.0, 0x0000, 0x0053, "")
    PlaceName(-62.25, 0.0, 77.0, 0x0000, 0x0053, "")
    PlaceName(-72.0, 0.0, 98.0, 0x0000, 0x0053, "")
    PlaceName(-48.0, 0.0, 130.0, 0x0000, 0x0052, "")
    PlaceName(-43.25, 0.0, 117.0, 0x0000, 0x0053, "")
    PlaceName(-34.5, 0.0, 108.5, 0x0000, 0x0053, "")
    PlaceName(-6.0, 0.0, 179.5, 0x0000, 0x0051, "")
    PlaceName(106.0, 0.0, 44.0, 0x0000, 0x0052, "")
    PlaceName(89.0, 0.0, -46.5, 0x0000, 0x0053, "")
    PlaceName(76.0, 0.0, -28.0, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_3EC",          # 00, 0
        "Function_1_4A4",          # 01, 1
        "Function_2_4DD",          # 02, 2
        "Function_3_4ED",          # 03, 3
        "Function_4_4FA",          # 04, 4
        "Function_5_2037",         # 05, 5
        "Function_6_2067",         # 06, 6
        "Function_7_20A4",         # 07, 7
        "Function_8_20E1",         # 08, 8
        "Function_9_211E",         # 09, 9
        "Function_10_215B",        # 0A, 10
    ))


    def Function_0_3EC(): pass

    label("Function_0_3EC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_42C"),
        (1, "loc_438"),
        (2, "loc_444"),
        (3, "loc_450"),
        (4, "loc_45C"),
        (5, "loc_468"),
        (6, "loc_474"),
        (SWITCH_DEFAULT, "loc_480"),
    )


    label("loc_42C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_438")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_444")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_450")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_45C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_468")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_474")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_480")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_48C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4A3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_48C")

    label("loc_4A3")

    Return()

    # Function_0_3EC end

    def Function_1_4A4(): pass

    label("Function_1_4A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4DC")
    OP_95(0xFE, -1830, 0, -23430, 2000, 0x0)
    Sleep(800)
    SetChrPos(0xFE, -1830, 0, 25870, 180)
    Jump("Function_1_4A4")

    label("loc_4DC")

    Return()

    # Function_1_4A4 end

    def Function_2_4DD(): pass

    label("Function_2_4DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_4EC")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 4)

    label("loc_4EC")

    Return()

    # Function_2_4DD end

    def Function_3_4ED(): pass

    label("Function_3_4ED")

    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    Return()

    # Function_3_4ED end

    def Function_4_4FA(): pass

    label("Function_4_4FA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00400.itc", 0x1E)
    LoadChrToIndex("chr/ch02100.itc", 0x1F)
    LoadChrToIndex("chr/ch02150.itc", 0x20)
    OP_68(-500, 1300, 16500, 0)
    MoveCamera(36, 12, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(18500, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -500, 0, 23500, 180)
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x8, -20800, -5000, 17000, 90)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8)
    OP_90(0x101, -11600, -4800, 17000, 270)
    OP_90(0x102, -10200, -3800, 17000, 270)
    OP_90(0x103, -8800, -2800, 17000, 270)
    OP_90(0x104, -7400, -1800, 17000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xA, 0x80)
    OP_78(0xB, 0xA)
    OP_49()
    SetChrPos(0xA, -50000, -11500, 7500, 0)
    OP_D3(0xA, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0xB, 0x1000)
    OP_7D(0xB4, 0xC8, 0xDC, 0x0, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01600.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00400.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00000.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    SetCameraDistance(15500, 3500)

    def lambda_6FE():
        OP_95(0xFE, -500, 0, 16500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6FE)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x9, 1)
    OP_6F(0x10)
    Sleep(300)
    OP_93(0x9, 0x10E, 0x1F4)
    Sound(1805, 255, 90, 0)    #voice#Wald
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0001
    AnonymousTalk(
        0x9,
        (
            "是站前街道角落\x01",
            "放建材的地方吗……\x02\x03",

            "话说回来，居然大半夜把人叫到\x01",
            "这种地方，而且还要求一个人前来……\x02\x03",

            "警察局的那群小鬼……\x01",
            "到底以为自己是谁啊……！？\x02",
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
    OP_68(-14500, -4200, 16500, 7000)
    MoveCamera(45, 16, 0, 7000)

    def lambda_851():
        OP_95(0xFE, -14500, -5000, 16500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_851)
    WaitChrThread(0x9, 1)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x9, 0xB4, 0x1F4)
    OP_6F(0x41)
    Fade(500)
    OP_68(-39500, -8000, 6500, 0)
    MoveCamera(65, 24, 0, 0)
    OP_6E(720, 0)
    SetCameraDistance(23000, 0)
    OP_11(0x34, 0x21, 0x49, 0x28, 0xFA, 0x0)
    ClearMapObjFlags(0xB, 0x4)
    BeginChrThread(0xA, 3, 0, 5)
    BeginChrThread(0xB, 1, 0, 10)
    OP_68(-21500, -8000, 6500, 5000)
    MoveCamera(45, 4, 0, 5000)
    SetCameraDistance(20000, 5000)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 1)
    OP_6F(0x79)
    Fade(500)
    OP_68(-14500, -4200, 16500, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(660, 0)
    SetCameraDistance(15500, 0)
    OP_11(0x34, 0x21, 0x49, 0x28, 0x78, 0x0)
    SetMapObjFlags(0xB, 0x4)
    OP_0D()

    #C0002
    ChrTalk(
        0x9,
        "#1605F刚才那是……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)

    #N0003
    NpcTalk(
        0x8,
        "少年的声音",
        (
            "#2P大概是开往共和国\x01",
            "方向的末班列车吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x9, 0x8, 500)
    Fade(1000)
    SetChrPos(0x9, -16000, -5000, 17000, 270)
    SetChrPos(0x8, -24400, -5000, 17000, 90)
    ClearChrFlags(0x8, 0x8)
    OP_68(-18040, -4000, 17740, 0)
    MoveCamera(325, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    Sleep(1)
    OP_68(-21120, -4000, 17740, 1600)
    OP_6F(0x1)

    #C0004
    ChrTalk(
        0x9,
        "#11P#1601F瓦吉……！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1435, 255, 90, 0)    #voice#Lazy
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0005
    AnonymousTalk(
        0x8,
        (
            "晚上好啊，瓦鲁多。\x02\x03",

            "真是个美好的夜晚呢，\x01",
            "月光如此皎洁而朦胧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    #C0006
    ChrTalk(
        0x9,
        (
            "#11P#1601F你这家伙……\x02\x03",

            "#1604F……哼哼，是吗，\x01",
            "原来是这么回事啊……\x02\x03",

            "#1602F你冒充警察局的那群小鬼，把我\x01",
            "骗到这里，是想来个瓮中捉鳖吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-22590, -4000, 17740, 2000)

    def lambda_BBA():
        OP_95(0xFE, -20400, -5000, 17000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_BBA)
    WaitChrThread(0x9, 1)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    Sound(808, 0, 100, 0)
    SetCameraDistance(18500, 0)
    OP_0D()
    Sleep(500)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)

    #C0007
    ChrTalk(
        0x9,
        (
            "#1607F#4S既然如此，那就不用再废话了！\x02\x03",

            "#3S想单挑的话，正合我意啊！\x01",
            "咱们就在这里做个了断吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "#0404F呵呵，我对此倒也\x01",
            "没什么异议，不过呢……\x02\x03",

            "#0400F巧得很，我和你一样，\x01",
            "也是被人邀请到这个地方的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x9,
        "#1601F什么……？\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        "#0402F看，人好像来了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(-16500, -4000, 17000, 0)
    MoveCamera(33, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x9, -22000, -5000, 17500, 270)
    SetChrPos(0x8, -25000, -5000, 17000, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(-20500, -4000, 17000, 5500)
    BeginChrThread(0x101, 3, 0, 6)
    BeginChrThread(0x102, 3, 0, 7)
    BeginChrThread(0x103, 3, 0, 8)
    BeginChrThread(0x104, 3, 0, 9)
    OP_0D()
    Sleep(500)
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(1000)

    def lambda_DC6():
        OP_95(0xFE, -23900, -5000, 17000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_DC6)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)

    #C0011
    ChrTalk(
        0x9,
        "#1600F那些家伙……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0012
    AnonymousTalk(
        0x101,
        (
            "不好意思啊，两位。\x01",
            "似乎让你们久等了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)

    #C0013
    ChrTalk(
        0x8,
        (
            "#3P#0404F承蒙邀请，荣幸之至──\x02\x03",

            "#0402F那么就按照约定，把你们调查到的\x01",
            "有趣消息告诉我们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#0004F#11P是否有趣还不敢肯定，\x01",
            "不过，我想你应该会很感兴趣的。\x02\x03",

            "#0000F那我开始说了？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2300, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    #C0015
    ChrTalk(
        0x9,
        (
            "#1607F慢、慢着！给我等一下。\x02\x03",

            "有趣的事情……！？\x01",
            "你到底要说什么啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        "#3P#0406F你可真是够迟钝啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 600)

    #C0017
    ChrTalk(
        0x9,
        "#11P#1605F什么……！\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "#3P#0404F五天前的夜晚，在旧城区\x01",
            "发生的那两起伤害事件……\x02\x03",

            "#0402F他们显然是查到了一些重要的线索，\x01",
            "要把真正的犯人告诉我们啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
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

    #C0019
    ChrTalk(
        0x9,
        "#11P#1605F什、什么……！？\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x102,
        "#11P#0105F真让人吃惊……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x103,
        (
            "#11P#0200F……看起来，你好像也\x01",
            "一直心存疑虑啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "#3P#0403F呵呵，可以这么说吧。\x01",
            "一开始，我也以为是我们的成员\x01",
            "一时头脑发热而做出那种事情……\x02\x03",

            "#0401F但在仔细分析了具体状况之后，\x01",
            "不管怎么想，都觉得有些不自然。\x02\x03",

            "『剑蛇帮』那边也是一样……\x02\x03",

            "#0406F呼，不过我的推理\x01",
            "也就到此为止啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#0003F#11P是吗……\x01",
            "既然如此，我解释起来也就轻松多了。\x02\x03",

            "#0001F──瓦鲁多·瓦雷斯。\x02\x03",

            "虽然还有不少地方残留着疑问，\x01",
            "需要继续进行推敲……\x02\x03",

            "不过，能不能先听我\x01",
            "把话说完呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x9,
        "#11P#1603F……嘁……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    OP_0D()
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(300)

    #C0025
    ChrTalk(
        0x9,
        (
            "#1601F──那就长话短说吧。\x02\x03",

            "如果都是些无聊的废话，\x01",
            "小心我把你的脑袋拧下来。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    OP_68(-20500, -4000, 17000, 0)
    MoveCamera(33, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    Sleep(1000)
    SetChrPos(0x9, -22000, -5000, 18000, 90)
    SetChrPos(0x8, -22200, -5000, 16500, 90)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    SetCameraDistance(17500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_64(0x8)
    OP_64(0x9)
    OP_6F(0x10)

    #C0026
    ChrTalk(
        0x101,
        (
            "#0003F#11P──这只是根据目前现有的情报\x01",
            "而做出的推理。\x02\x03",

            "#0001F希望能听听你们的真实感想。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        "#1605F#3P………………………………\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "#6P#0406F……哎呀呀，真是没想到啊。\x02\x03",

            "我们居然会被那些黑手党\x01",
            "耍得团团转。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        "#0000F#11P那么，言下之意就是……\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x102,
        (
            "#11P#0101F刚才罗伊德说的那些想法……\x01",
            "你算是表示认同了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "#6P#0402F呵呵，那是自然……\x02\x03",

            "因为，鲁巴彻商会之前\x01",
            "确实派人来找过我们。\x02\x03",

            "说会给我们很多好处，\x01",
            "招揽我们去他们的手下做事。\x02\x03",

            "#0404F当然，我不屑一顾地\x01",
            "拒绝了他们的要求。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        "#0001F#11P是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x104,
        "#11P#0303F……那就可以断定了吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)
    Sleep(300)

    #C0034
    ChrTalk(
        0x8,
        (
            "#12P#0400F瓦鲁多，\x01",
            "你那边的情况如何？\x02\x03",

            "是不是也曾受到过\x01",
            "黑手党的劝诱？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        (
            "#1603F……嗯，大概是在一个月之前吧……\x02\x03",

            "不过，那些家伙未免也太看不起人了，\x01",
            "于是我就连打带吓地把他们赶跑了……\x02\x03",

            "#1602F……但是没想到，那群混蛋居然真的敢\x01",
            "做出这种事，看来是相当不把我们放在眼里啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Sound(1808, 255, 90, 0)    #voice#Wald
    Sleep(800)
    Fade(250)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()
    TurnDirection(0x9, 0x8, 500)
    Sleep(300)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)

    #C0036
    ChrTalk(
        0x9,
        (
            "#1607F#5P瓦吉！\x01",
            "和你的决斗就先延期吧！\x02\x03",

            "管他什么黑手党！\x01",
            "一定要把那群混蛋统统干掉！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0037
    ChrTalk(
        0x102,
        "#11P#0101F等、等一下！\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x103,
        "#11P#0203F真是一点就爆的脾气……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#0013F#11P喂，先冷静一点啊！\x01",
            "如此冲动行事的话，一不小心就会——\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        "#12P#0406F呼，你可真是个笨蛋啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0041
    ChrTalk(
        0x9,
        "#1601F#5P你说什么……！？\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "#12P#0400F和黑手党的人开战，\x01",
            "根本就没有任何胜算可言吧？\x02\x03",

            "如果贸然行事，正面冲上去挑战的话，\x01",
            "下场也只会是被人打成蜂窝而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        (
            "#1607F少啰嗦！吵死人了！\x01",
            "能不能打赢，不试试看怎么会知道！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "#12P#0406F我说……就算你不怕死。\x02\x03",

            "#0401F但总要替手下们想想吧，你难道想把\x01",
            "那些可爱的小弟们也给卷进来吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0045
    ChrTalk(
        0x9,
        (
            "#1601F#5P…………唔………………\x02\x03",

            "#1607F那你说，该怎么办才好！？\x02\x03",

            "都已经被人欺负到这种地步了……\x01",
            "连同伴都惨遭他们的毒手，\x01",
            "难道还要继续忍气吞声吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "#12P#0409F哈……\x01",
            "那当然不可能啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0047
    ChrTalk(
        0x8,
        (
            "#12P#0404F不过，牵扯到此次事件的人，\x01",
            "应该只是黑手党组织中的一小部分成员而已。\x02\x03",

            "既然如此，只要让这些人\x01",
            "受到应得的教训就可以了。\x02\x03",

            "#0402F而且，必须是非常彻底的教训，\x01",
            "要达到让他们再也无法进行报复的程度。\x02\x03",

            "#0409F──瓦鲁多，\x01",
            "这也需要你的协助哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x9,
        "#1605F#5P……你………\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#0011F#11P等、等一下。\x02\x03",

            "#0013F你打算做什么？\x01",
            "如果是太乱来的违法行为——\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)

    #C0050
    ChrTalk(
        0x8,
        (
            "#6P#0409F哦，不必担心。\x01",
            "因为也需要你们来帮忙呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        "#0005F#11P什么……\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(1430, 255, 90, 0)    #voice#Lazy
    Sleep(300)
    OP_68(-19110, -4000, 16930, 1800)

    def lambda_1DC1():

        label("loc_1DC1")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1DC1")

    QueueWorkItem2(0x9, 2, lambda_1DC1)

    def lambda_1DD3():

        label("loc_1DD3")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1DD3")

    QueueWorkItem2(0x102, 2, lambda_1DD3)

    def lambda_1DE5():

        label("loc_1DE5")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1DE5")

    QueueWorkItem2(0x104, 2, lambda_1DE5)

    def lambda_1DF7():
        OP_95(0xFE, -19700, -5000, 16500, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1DF7)
    WaitChrThread(0x8, 1)
    Sleep(500)

    #C0052
    ChrTalk(
        0x8,
        (
            "#6P#0404F#30W──你们的任务是\x01",
            "解决旧城区的事件。\x02\x03",

            "因此，你们有义务进行『耐心劝解』，\x01",
            "让那群黑手党从今以后\x01",
            "不会再来找我们的麻烦……\x02\x03",

            "#20W#0402F如何——我说得没错吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        "#0011F#11P这、这个……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x102,
        "#5P#0105F（这是什么意思呢……？）\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        "#11P#0202F（……不太明白，不过……）\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        (
            "#11P#0309F（看样子，罗伊德这家伙，\x01",
            "  这次是被人吃定了呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "#6P#0402F呵呵，你都特意来告诉我们\x01",
            "如此有趣的推理了。\x02\x03",

            "#0409F自然就要负起责任……\x01",
            "陪我们到最后哦。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    EndChrThread(0x9, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    Sleep(2000)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c140B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_4FA end

    def Function_5_2037(): pass

    label("Function_5_2037")

    OP_82(0x64, 0x0, 0xBB8, 0x1B58)

    def lambda_204D():
        OP_96(0xFE, 0xEA60, 0xFFFFD314, 0x1D4C, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_204D)
    WaitChrThread(0xA, 1)
    Return()

    # Function_5_2037 end

    def Function_6_2067(): pass

    label("Function_6_2067")


    def lambda_206C():
        OP_95(0xFE, -13500, -5000, 17000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_206C)
    WaitChrThread(0xFE, 1)

    def lambda_208A():
        OP_96(0xFE, 0xFFFFB5C8, 0xFFFFEC78, 0x413C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_208A)
    WaitChrThread(0x101, 1)
    Return()

    # Function_6_2067 end

    def Function_7_20A4(): pass

    label("Function_7_20A4")


    def lambda_20A9():
        OP_95(0xFE, -13500, -5000, 17000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_20A9)
    WaitChrThread(0xFE, 1)

    def lambda_20C7():
        OP_96(0xFE, 0xFFFFB5C8, 0xFFFFEC78, 0x4588, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_20C7)
    WaitChrThread(0x102, 1)
    Return()

    # Function_7_20A4 end

    def Function_8_20E1(): pass

    label("Function_8_20E1")


    def lambda_20E6():
        OP_95(0xFE, -13500, -5000, 17000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_20E6)
    WaitChrThread(0xFE, 1)

    def lambda_2104():
        OP_96(0xFE, 0xFFFFBB40, 0xFFFFEC78, 0x4010, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2104)
    WaitChrThread(0x103, 1)
    Return()

    # Function_8_20E1 end

    def Function_9_211E(): pass

    label("Function_9_211E")


    def lambda_2123():
        OP_95(0xFE, -13500, -5000, 17000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2123)
    WaitChrThread(0xFE, 1)

    def lambda_2141():
        OP_96(0xFE, 0xFFFFBB40, 0xFFFFEC78, 0x445C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2141)
    WaitChrThread(0x104, 1)
    Return()

    # Function_9_211E end

    def Function_10_215B(): pass

    label("Function_10_215B")

    Sound(455, 0, 100, 0)
    Return()

    # Function_10_215B end

    SaveToFile()

Try(main)
