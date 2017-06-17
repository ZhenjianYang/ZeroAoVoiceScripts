from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c100b.bin",                # FileName
        "c100b",                    # MapName
        "c100b",                    # Location
        0x0010,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 16, 0, 1, 0, 2],
    )

    BuildStringList((
        "c100b",                  # 0
        "蔡特",                   # 1
        "接待员米歇尔",           # 2
        "SE控制",                 # 3
        "中央广场",               # 4
        "西街",                   # 5
        "行政区",                 # 6
        "住宅街",                 # 7
        "欢乐街",                 # 8
        "东街",                   # 9
        "旧城区",                 # 10
        "港湾区",                 # 11
        "ＩＢＣ",                 # 12
        "站前街道",               # 13
        "后巷",                   # 14
        "乌尔斯拉间道",           # 15
        "东克洛斯贝尔街道",       # 16
        "西克洛斯贝尔街道",       # 17
        "玛因兹山道",             # 18
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    PlaceName(-111.26000213623047, 0.0, 15.239999771118164, 0x0000, 0x0000, "中央广场")
    PlaceName(-186.8800048828125, 0.0, 20.40999984741211, 0x0000, 0x0000, "西街")
    PlaceName(-80.20999908447266, 0.0, 117.58999633789062, 0x0000, 0x0000, "行政区")
    PlaceName(-257.0299987792969, 0.0, 106.08999633789062, 0x0000, 0x0000, "住宅街")
    PlaceName(-173.0800018310547, 0.0, 96.88999938964844, 0x0000, 0x0000, "欢乐街")
    PlaceName(-17.829999923706055, 0.0, -11.210000038146973, 0x0000, 0x0000, "东街")
    PlaceName(23.0, 0.0, -74.45999908447266, 0x0000, 0x0000, "旧城区")
    PlaceName(14.380000114440918, 0.0, 64.69000244140625, 0x0000, 0x0000, "港湾区")
    PlaceName(-15.529999732971191, 0.0, 172.7899932861328, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-98.33000183105469, 0.0, -64.11000061035156, 0x0000, 0x0000, "站前街道")
    PlaceName(-152.3800048828125, 0.0, 55.4900016784668, 0x0000, 0x0000, "后巷")
    PlaceName(-101.77999877929688, 0.0, -99.76000213623047, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(44.279998779296875, 0.0, 4.889999866485596, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-245.52999877929688, 0.0, 18.690000534057617, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-238.6300048828125, 0.0, 133.69000244140625, 0x0000, 0x0000, "玛因兹山道")
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
        "Function_0_35C",          # 00, 0
        "Function_1_378",          # 01, 1
        "Function_2_388",          # 02, 2
        "Function_3_3A9",          # 03, 3
        "Function_4_98E",          # 04, 4
        "Function_5_9D2",          # 05, 5
        "Function_6_A16",          # 06, 6
        "Function_7_A5A",          # 07, 7
        "Function_8_A9E",          # 08, 8
        "Function_9_B32",          # 09, 9
        "Function_10_B58",         # 0A, 10
        "Function_11_BA8",         # 0B, 11
    ))


    def Function_0_35C(): pass

    label("Function_0_35C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_377")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_35C")

    label("loc_377")

    Return()

    # Function_0_35C end

    def Function_1_378(): pass

    label("Function_1_378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_387")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 3)

    label("loc_387")

    Return()

    # Function_1_378 end

    def Function_2_388(): pass

    label("Function_2_388")

    SetMapObjFrame(0xFF, "guild02a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "guild02b", 0x0, 0x1)
    Return()

    # Function_2_388 end

    def Function_3_3A9(): pass

    label("Function_3_3A9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02750.itc", 0x1E)
    LoadChrToIndex("chr/ch02751.itc", 0x1F)
    LoadChrToIndex("chr/ch02702.itc", 0x20)
    LoadChrToIndex("chr/ch09100.itc", 0x21)
    LoadChrToIndex("chr/ch00150.itc", 0x22)
    LoadChrToIndex("chr/ch00151.itc", 0x23)
    LoadChrToIndex("chr/ch00250.itc", 0x24)
    LoadChrToIndex("chr/ch00251.itc", 0x25)
    OP_68(-18700, 700, 13700, 0)
    MoveCamera(55, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(23000, 0)
    OP_90(0x101, -29700, -300, 13700, 90)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    OP_90(0x102, -31700, -300, 14800, 90)
    SetChrChipByIndex(0x103, 0x24)
    SetChrSubChip(0x103, 0x0)
    OP_90(0x103, -30900, -300, 15900, 90)
    OP_90(0x104, -30900, -300, 13300, 90)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x20)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0x8, -33000, -300, 15200, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    SetChrPos(0x9, -7600, 330, 14000, 225)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFrame(0xFF, "guild02a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "guild02b", 0x1, 0x1)
    SetMapObjFrame(0xFF, "guild01a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "guild01b", 0x0, 0x1)
    BeginChrThread(0x101, 3, 0, 4)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 7)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 5)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 6)
    Sleep(50)
    BeginChrThread(0x8, 3, 0, 8)
    SetCameraDistance(20000, 3000)
    FadeToBright(2000, 0)
    OP_6F(0x10)
    Fade(500)
    OP_68(-9600, 2700, 12000, 0)
    MoveCamera(15, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_68(-9600, 700, 12000, 3000)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x8, 3)
    OP_6F(0x1)

    #C0001
    ChrTalk(
        0x102,
        "#0108F#6P这是……\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x104,
        "#6P#0301F被袭击后的惨状吗……\x02",
    )

    CloseMessageWindow()

    #N0003
    NpcTalk(
        0x104,
        "滴",
        "#5P#6008F……爸、爸爸……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x2)

    def lambda_63C():
        OP_96(0xFE, 0xFFFFDF30, 0xFFFFFF6A, 0x3390, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_63C)

    def lambda_656():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_656)
    WaitChrThread(0x9, 1)

    #C0004
    ChrTalk(
        0x9,
        "#11P哎呀，是你们！？\x02",
    )

    CloseMessageWindow()

    #N0005
    NpcTalk(
        0x104,
        "滴",
        "#5P#6005F米歇尔先生……！？\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#6P#0002F太好了……\x01",
            "您没事吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x9,
        (
            "#11P嗯，在那之后，\x01",
            "总算是想方设法逃了出去。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        (
            "#11P后来，因为那些家伙已经离开了，\x01",
            "我就偷偷跑了回来……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x9,
        "#11P不过，他们好像仍在市区内吧？\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#6P#0013F嗯，他们似乎是以行政区为中心，\x01",
            "在市区内展开行动的。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "向米歇尔简单说明了至今为止的事情经过。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0012
    ChrTalk(
        0x9,
        "#11P……原来如此。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x9,
        (
            "#11P在市区外的游击士们\x01",
            "差不多也该回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        (
            "#11P等他们回来以后，我会组织他们去帮忙的，\x01",
            "你们就赶快逃到市外吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x9,
        (
            "#11P还有，小滴就\x01",
            "拜托你们了！\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        "#6P#0300F明白！\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        "#6P#0000F交给我们吧！\x02",
    )

    CloseMessageWindow()

    #N0018
    NpcTalk(
        0x104,
        "滴",
        (
            "#5P#6010F米歇尔先生……\x01",
            "请一定要小心……！\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x9,
        "#11P嗯，你们也一样！\x02",
    )

    CloseMessageWindow()
    OP_68(-7600, 700, 10000, 3000)
    SetCameraDistance(18000, 3000)

    def lambda_922():

        label("loc_922")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_922")

    QueueWorkItem2(0x9, 2, lambda_922)
    BeginChrThread(0x101, 3, 0, 9)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 9)
    Sleep(150)
    BeginChrThread(0x103, 3, 0, 9)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 9)
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 10)
    Sleep(500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x11)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0xA, 0x1)
    SetScenarioFlags(0x5C, 0)
    NewScene("r000B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_3A9 end

    def Function_4_98E(): pass

    label("Function_4_98E")


    def lambda_993():
        OP_95(0xFE, -14700, -300, 13700, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_993)
    WaitChrThread(0x101, 1)

    def lambda_9B1():
        OP_95(0xFE, -10300, -300, 9300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9B1)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_4_98E end

    def Function_5_9D2(): pass

    label("Function_5_9D2")


    def lambda_9D7():
        OP_95(0xFE, -15900, -300, 13300, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9D7)
    WaitChrThread(0x104, 1)

    def lambda_9F5():
        OP_95(0xFE, -11500, -300, 9900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9F5)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x2D, 0x1F4)
    Return()

    # Function_5_9D2 end

    def Function_6_A16(): pass

    label("Function_6_A16")


    def lambda_A1B():
        OP_95(0xFE, -16700, -300, 14800, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A1B)
    WaitChrThread(0x102, 1)

    def lambda_A39():
        OP_95(0xFE, -12300, -300, 11400, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A39)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_6_A16 end

    def Function_7_A5A(): pass

    label("Function_7_A5A")


    def lambda_A5F():
        OP_95(0xFE, -15900, -300, 15900, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A5F)
    WaitChrThread(0x103, 1)

    def lambda_A7D():
        OP_95(0xFE, -11500, -300, 12500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A7D)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x5A, 0x1F4)
    Return()

    # Function_7_A5A end

    def Function_8_A9E(): pass

    label("Function_8_A9E")

    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0xA, 1, 0, 11)

    def lambda_ACD():
        OP_95(0xFE, -18000, -300, 14200, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_ACD)
    WaitChrThread(0x8, 1)

    def lambda_AEB():
        OP_95(0xFE, -13600, -300, 10800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AEB)
    WaitChrThread(0x8, 1)
    EndChrThread(0x8, 0x0)
    EndChrThread(0xA, 0x1)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0x8, 0x5A, 0x1F4)
    Return()

    # Function_8_A9E end

    def Function_9_B32(): pass

    label("Function_9_B32")

    OP_93(0xFE, 0x87, 0x1F4)

    def lambda_B3E():
        OP_97(0xFE, 0x2EE0, 0x0, 0xFFFFD120, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B3E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_9_B32 end

    def Function_10_B58(): pass

    label("Function_10_B58")

    OP_93(0xFE, 0x87, 0x1F4)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0xA, 1, 0, 11)

    def lambda_B8E():
        OP_97(0xFE, 0x2EE0, 0x0, 0xFFFFD120, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B8E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_10_B58 end

    def Function_11_BA8(): pass

    label("Function_11_BA8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BC1")
    Sound(925, 0, 100, 0)
    Sleep(500)
    Jump("Function_11_BA8")

    label("loc_BC1")

    Return()

    # Function_11_BA8 end

    SaveToFile()

Try(main)
