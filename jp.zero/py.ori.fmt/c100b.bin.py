from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ツァイト",               # 1
        "受付ミシェル",           # 2
        "SE制御",                 # 3
        "中央広場",               # 4
        "西通り",                 # 5
        "行政区",                 # 6
        "住宅街",                 # 7
        "歓楽街",                 # 8
        "東通り",                 # 9
        "旧市街",                 # 10
        "港湾区",                 # 11
        "ＩＢＣ",                 # 12
        "駅前通り",               # 13
        "裏通り",                 # 14
        "ウルスラ間道",           # 15
        "東クロスベル街道",       # 16
        "西クロスベル街道",       # 17
        "マインツ山道",           # 18
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

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

    ScpFunction((
        "Function_0_35C",          # 00, 0
        "Function_1_378",          # 01, 1
        "Function_2_388",          # 02, 2
        "Function_3_3A9",          # 03, 3
        "Function_4_9E6",          # 04, 4
        "Function_5_A2A",          # 05, 5
        "Function_6_A6E",          # 06, 6
        "Function_7_AB2",          # 07, 7
        "Function_8_AF6",          # 08, 8
        "Function_9_B8A",          # 09, 9
        "Function_10_BB0",         # 0A, 10
        "Function_11_C00",         # 0B, 11
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
        "#0108F#6Pこれは……\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x104,
        "#6P#0301F襲撃された後か……\x02",
    )

    CloseMessageWindow()

    #N0003
    NpcTalk(
        0x104,
        "シズク",
        "#5P#6008F……お、お父さん……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x2)

    def lambda_644():
        OP_96(0xFE, 0xFFFFDF30, 0xFFFFFF6A, 0x3390, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_644)

    def lambda_65E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_65E)
    WaitChrThread(0x9, 1)

    #C0004
    ChrTalk(
        0x9,
        "#11Pあら、あなたたち！？\x02",
    )

    CloseMessageWindow()

    #N0005
    NpcTalk(
        0x104,
        "シズク",
        "#5P#6005Fミシェルさん……！？\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#6P#0002Fよかった……\x01",
            "無事だったんですね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x9,
        (
            "#11Pええ、あの後、\x01",
            "何とか切り抜けて脱出したの。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        (
            "#11P連中が居なくなってから\x01",
            "こっそり戻ってきたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x9,
        "#11Pまだ連中、市内にいるみたいね？\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#6P#0013Fええ、行政区を中心に\x01",
            "市内に展開しているみたいです。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ミシェルに今までの経緯を手短に説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0012
    ChrTalk(
        0x9,
        "#11P……なるほど。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x9,
        (
            "#11P市外にいた遊撃士たちも\x01",
            "そろそろ戻ってくる頃合いよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        (
            "#11P戻り次第、フォローを回すから\x01",
            "このまま街道に逃げなさい！\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x9,
        (
            "#11Pあと、シズクちゃんは\x01",
            "このまま頼んだわよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        "#6P#0300F合点承知だ！\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        "#6P#0000F任せてください！\x02",
    )

    CloseMessageWindow()

    #N0018
    NpcTalk(
        0x104,
        "シズク",
        (
            "#5P#6010Fミシェルさん……\x01",
            "どうかお気をつけて……！\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x9,
        "#11Pええ、そっちもね！\x02",
    )

    CloseMessageWindow()
    OP_68(-7600, 700, 10000, 3000)
    SetCameraDistance(18000, 3000)

    def lambda_97A():

        label("loc_97A")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_97A")

    QueueWorkItem2(0x9, 2, lambda_97A)
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

    def Function_4_9E6(): pass

    label("Function_4_9E6")


    def lambda_9EB():
        OP_95(0xFE, -14700, -300, 13700, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9EB)
    WaitChrThread(0x101, 1)

    def lambda_A09():
        OP_95(0xFE, -10300, -300, 9300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A09)
    WaitChrThread(0x101, 1)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_4_9E6 end

    def Function_5_A2A(): pass

    label("Function_5_A2A")


    def lambda_A2F():
        OP_95(0xFE, -15900, -300, 13300, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A2F)
    WaitChrThread(0x104, 1)

    def lambda_A4D():
        OP_95(0xFE, -11500, -300, 9900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A4D)
    WaitChrThread(0x104, 1)
    OP_93(0x104, 0x2D, 0x1F4)
    Return()

    # Function_5_A2A end

    def Function_6_A6E(): pass

    label("Function_6_A6E")


    def lambda_A73():
        OP_95(0xFE, -16700, -300, 14800, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A73)
    WaitChrThread(0x102, 1)

    def lambda_A91():
        OP_95(0xFE, -12300, -300, 11400, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A91)
    WaitChrThread(0x102, 1)
    OP_93(0x102, 0x5A, 0x1F4)
    Return()

    # Function_6_A6E end

    def Function_7_AB2(): pass

    label("Function_7_AB2")


    def lambda_AB7():
        OP_95(0xFE, -15900, -300, 15900, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AB7)
    WaitChrThread(0x103, 1)

    def lambda_AD5():
        OP_95(0xFE, -11500, -300, 12500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AD5)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x5A, 0x1F4)
    Return()

    # Function_7_AB2 end

    def Function_8_AF6(): pass

    label("Function_8_AF6")

    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0xA, 1, 0, 11)

    def lambda_B25():
        OP_95(0xFE, -18000, -300, 14200, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B25)
    WaitChrThread(0x8, 1)

    def lambda_B43():
        OP_95(0xFE, -13600, -300, 10800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B43)
    WaitChrThread(0x8, 1)
    EndChrThread(0x8, 0x0)
    EndChrThread(0xA, 0x1)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_93(0x8, 0x5A, 0x1F4)
    Return()

    # Function_8_AF6 end

    def Function_9_B8A(): pass

    label("Function_9_B8A")

    OP_93(0xFE, 0x87, 0x1F4)

    def lambda_B96():
        OP_97(0xFE, 0x2EE0, 0x0, 0xFFFFD120, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B96)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_9_B8A end

    def Function_10_BB0(): pass

    label("Function_10_BB0")

    OP_93(0xFE, 0x87, 0x1F4)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0xA, 1, 0, 11)

    def lambda_BE6():
        OP_97(0xFE, 0x2EE0, 0x0, 0xFFFFD120, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BE6)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_10_BB0 end

    def Function_11_C00(): pass

    label("Function_11_C00")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C19")
    Sound(925, 0, 100, 0)
    Sleep(500)
    Jump("Function_11_C00")

    label("loc_C19")

    Return()

    # Function_11_C00 end

    SaveToFile()

Try(main)
