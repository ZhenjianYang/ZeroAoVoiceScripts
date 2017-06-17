from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t5000.bin",                # FileName
        "t5000",                    # MapName
        "t5000",                    # Location
        0x0000,                     # MapIndex
        "ed7102",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x27,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "t5000",                  # 0
        "凯文神父",               # 1
        "穿修女服的少女",         # 2
        "达德利的车",             # 3
        "车",                     # 4
        "车",                     # 5
        "市民",                   # 6
        "市民",                   # 7
        "市民",                   # 8
        "市民",                   # 9
        "市民",                   # 10
        "市民",                   # 11
        "市民",                   # 12
        "市民",                   # 13
        "市民",                   # 14
        "共和国巴士",             # 15
        "护送车",                 # 16
        "假货商",                 # 17
        "共和国军人",             # 18
        "共和国军人",             # 19
        "黑月成员",               # 20
        "黑月成员",               # 21
        "SE控制",                 # 22
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(836, 0)                                        # 0

    ScpFunction((
        "Function_0_344",          # 00, 0
        "Function_1_3F4",          # 01, 1
        "Function_2_418",          # 02, 2
        "Function_3_419",          # 03, 3
        "Function_4_23AB",         # 04, 4
        "Function_5_243B",         # 05, 5
        "Function_6_246F",         # 06, 6
        "Function_7_24C7",         # 07, 7
        "Function_8_2547",         # 08, 8
        "Function_9_2581",         # 09, 9
        "Function_10_25C8",        # 0A, 10
        "Function_11_2623",        # 0B, 11
        "Function_12_2684",        # 0C, 12
        "Function_13_26A0",        # 0D, 13
        "Function_14_35A8",        # 0E, 14
        "Function_15_36C1",        # 0F, 15
        "Function_16_36EE",        # 10, 16
        "Function_17_3728",        # 11, 17
    ))


    def Function_0_344(): pass

    label("Function_0_344")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_37C"),
        (1, "loc_388"),
        (2, "loc_394"),
        (3, "loc_3A0"),
        (4, "loc_3AC"),
        (5, "loc_3B8"),
        (6, "loc_3C4"),
        (SWITCH_DEFAULT, "loc_3D0"),
    )


    label("loc_37C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_388")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_394")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3A0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3AC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3B8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3DC")

    label("loc_3F3")

    Return()

    # Function_0_344 end

    def Function_1_3F4(): pass

    label("Function_1_3F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_408")
    ClearScenarioFlags(0x22, 0)
    Event(0, 3)
    Jump("loc_417")

    label("loc_408")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_417")
    ClearScenarioFlags(0x22, 1)
    Event(0, 13)

    label("loc_417")

    Return()

    # Function_1_3F4 end

    def Function_2_418(): pass

    label("Function_2_418")

    Return()

    # Function_2_418 end

    def Function_3_419(): pass

    label("Function_3_419")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11400.itc", 0x1E)
    LoadChrToIndex("apl/ch51026.itc", 0x1F)
    LoadChrToIndex("chr/ch25600.itc", 0x20)
    LoadChrToIndex("chr/ch21102.itc", 0x21)
    LoadChrToIndex("chr/ch21302.itc", 0x22)
    LoadChrToIndex("chr/ch26000.itc", 0x23)
    LoadChrToIndex("chr/ch25000.itc", 0x24)
    LoadChrToIndex("chr/ch44200.itc", 0x25)
    LoadChrToIndex("chr/ch44100.itc", 0x26)
    LoadChrToIndex("chr/ch44000.itc", 0x27)
    LoadChrToIndex("chr/ch44400.itc", 0x28)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13800.itp")
    SetChrPos(0x101, 0, 0, 8400, 0)
    SetChrPos(0x109, -1300, 0, 8200, 0)
    SetChrPos(0x10A, -700, 0, 10900, 180)
    SetChrPos(0x108, 700, 0, 11200, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 1500, 0, 8200, 315)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x2)
    ClearChrFlags(0xA, 0x80)
    OP_78(0xA, 0xA)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xA, 0, 0, 13500, 0)
    OP_D5(0xA, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0xA, 0x1000)
    OP_74(0xA, 0x1E)
    OP_70(0xA, 0x0)
    ClearChrFlags(0xB, 0x80)
    OP_78(0x6, 0xB)
    OP_49()
    SetChrPos(0xB, 5000, 0, -3500, 0)
    OP_D5(0xB, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x6, 0x1000)
    ClearChrFlags(0xC, 0x80)
    OP_78(0x7, 0xC)
    OP_49()
    SetChrPos(0xC, -19000, 0, 2200, 0)
    OP_D5(0xC, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x7, 0x1000)
    ClearChrFlags(0x16, 0x80)
    OP_78(0x9, 0x16)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x16, -35000, 0, 17500, 0)
    OP_D5(0x16, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x9, 0x1000)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x0)
    OP_71(0x9, 0x79, 0xB4, 0x0, 0x20)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x20)
    SetChrPos(0xD, 5800, 0, -5400, 225)
    BeginChrThread(0xD, 0, 0, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x21)
    SetChrSubChip(0xE, 0x2)
    SetChrPos(0xE, -2300, 50, -2750, 225)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xF, 0x1)
    SetChrPos(0xF, -2950, 50, -2200, 225)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x23)
    SetChrPos(0x10, 14700, 0, -6400, 270)
    BeginChrThread(0x10, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x24)
    SetChrPos(0x11, -22200, 0, 900, 270)
    BeginChrThread(0x11, 0, 0, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x25)
    SetChrPos(0x12, 0, 0, -23000, 0)
    BeginChrThread(0x12, 1, 0, 6)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x26)
    SetChrPos(0x13, 21500, 180, 6000, 270)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x27)
    SetChrPos(0x14, 12000, 0, 9000, 0)
    BeginChrThread(0x14, 0, 0, 8)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x15, 0x28)
    SetChrPos(0x15, -23500, 0, 900, 90)
    BeginChrThread(0x15, 0, 0, 0)
    OP_68(0, 1900, -21500, 0)
    MoveCamera(45, 35, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(18000, 0)
    OP_68(0, 2000, 0, 8000)
    MoveCamera(30, 17, 0, 8000)
    SetCameraDistance(41000, 8000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    PlaceName2(100, 200, "c_plac35", 0x0, 0)
    Sleep(500)
    Sleep(1000)
    BeginChrThread(0x16, 0, 0, 4)
    BeginChrThread(0x16, 1, 0, 5)
    BeginChrThread(0x1D, 1, 0, 12)
    Sleep(2000)
    BeginChrThread(0x13, 0, 0, 7)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-11500, 1900, 7700, 0)
    MoveCamera(23, 27, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    WaitChrThread(0x16, 1)
    Sleep(1000)
    Fade(500)
    OP_68(0, 11000, 17800, 0)
    MoveCamera(31, -15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(26000, 0)
    OP_68(0, 5000, 17800, 7000)
    MoveCamera(39, 10, 0, 7000)
    SetCameraDistance(29000, 7000)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(0, 1100, 9600, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    #C0001
    ChrTalk(
        0x101,
        (
            "#12P#00004F那么，达德利警官，\x01",
            "押送他们两人的工作就拜托了。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x10A,
        "#00600F#5P嗯，放心吧。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x8, 500)
    Sleep(300)

    #C0003
    ChrTalk(
        0x10A,
        (
            "#00603F#5P凯文神父，\x01",
            "我要向你表示感谢。\x02\x03",

            "#00600F但说实话，要是能事先\x01",
            "联络警方就更好了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_98B():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_98B)
    Sleep(50)

    def lambda_99B():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_99B)
    Sleep(100)

    #C0004
    ChrTalk(
        0x8,
        (
            "#04306F#11P哈哈～其实我也\x01",
            "很想那样做。\x02\x03",

            "#04300F但对我们骑士团来说，克洛斯贝尔\x01",
            "实在是一处禁地……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x10A,
        (
            "#00606F#5P是因为克洛斯贝尔教区的负责人\x01",
            "艾拉尔达大主教吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#6P#00005F哦，原来玛布尔老师以前说过的\x01",
            "法术专家就是……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(150)

    #C0007
    ChrTalk(
        0x8,
        (
            "#04303F#11P嗯，指的应该就是我们。\x02\x03",

            "#04300F总之，出于各种原因，\x01",
            "大主教阁下非常讨厌我们。\x02\x03",

            "他禁止星杯骑士团\x01",
            "在克洛斯贝尔进行\x01",
            "任何活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x109,
        (
            "#6P#10108F艾拉尔达大主教吗……\x02\x03",

            "#10106F我以前也见过他，\x01",
            "看起来似乎是位很严厉的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "#04306F#11P严厉倒是无所谓，\x01",
            "但我从来没见过那么固执的人。\x02\x03",

            "#04308F当然，我们确实做过\x01",
            "不少见不得光的事情，\x01",
            "他那种正派人士恐怕很难接受吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        "#6P#00011F见、见不得光的事情是指……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x108,
        (
            "#5P#01403F牵扯到『古代遗物』的事件，\x01",
            "光靠正当手段是很难处理的。\x02\x03",

            "#01402F总而言之，凯文神父，\x01",
            "这次多亏有你相助。\x02\x03",

            "请容我再次表示感谢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x0, 0x1F4)
    Sleep(150)

    #C0012
    ChrTalk(
        0x8,
        (
            "#04302F#12P哈哈，不必客气，\x01",
            "我上次也欠您一个很大的人情啊。\x02\x03",

            "#04304F老实说，此事牵扯到了教团事件，\x01",
            "我本想继续参与。\x02\x03",

            "#04311F但我不想刺激到大主教，\x01",
            "你们要是掌握到了什么新消息，就通知我一声吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x108,
        (
            "#5P#01404F好，我会通过协会\x01",
            "和你联络的。\x02\x03",

            "#01402F罗伊德，诺艾尔上士，\x01",
            "你们这次的表现很不错。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DEB():
        TurnDirection(0xFE, 0x108, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DEB)
    Sleep(50)

    def lambda_DFB():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_DFB)
    Sleep(50)
    TurnDirection(0x109, 0x10A, 500)
    Sleep(200)

    #C0014
    ChrTalk(
        0x109,
        (
            "#6P#10112F啊哈哈，说实话，\x01",
            "我并没发挥什么作用。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#12P#00002F不，上士发挥了\x01",
            "很重要的作用。\x02\x03",

            "#00006F……倒是我，\x01",
            "仍然还不够成熟啊。\x02\x03",

            "#00008F按理说，本应由我\x01",
            "带领大家逮捕犯人的，\x01",
            "结果却……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x108,
        "#5P#01405F唔……\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x10A,
        (
            "#00606F#5P哼，别自我陶醉了。\x02\x03",

            "#00601F『由支援科负责此次逮捕行动』\x01",
            "只不过是名义上的说法而已，\x01",
            "你应该也明白这一点。\x02\x03",

            "以此为前提，你真的认为\x01",
            "自己没有派上用场吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#12P#00005F这、这个……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x10A,
        (
            "#00603F#5P严格要求自己自然是好事，但身为高级搜查官，\x01",
            "也必须要具备判断状况，客观评价自己的能力。\x02\x03",

            "#00600F虽说只是研修，但你既然身在一科，\x01",
            "就要把这些话牢记于心。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#12P#00002F达德利警官……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x109,
        (
            "#6P#10112F呵呵……\x01",
            "您真是不坦率呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x108,
        (
            "#5P#01404F呵，直率地赞一句\x01",
            "『干得好』也无妨吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x10A,
        (
            "#00610F#5P哼，不用你们多嘴。\x02\x03",

            "#00606F总之，班宁斯，\x01",
            "你在一科的研修到此结束。\x02\x03",

            "#00602F连同在此次事件中学到的东西，\x01",
            "希望你把这段时间的研修成果活用于新起点上。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#12P#00002F是……\x01",
            "多谢您的指导！\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x108,
        (
            "#5P#01404F那我们就\x01",
            "先走一步了。\x02\x03",

            "#01402F如果以后有需要，\x01",
            "还请你们多帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        "#12P#00000F好的，彼此彼此！\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x109,
        "#6P#10109F辛苦了！\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        "#04309F#12P请多保重～！\x02",
    )

    CloseMessageWindow()
    OP_71(0xA, 0x12D, 0x14A, 0x0, 0x0)
    Sound(462, 0, 100, 0)
    OP_79(0xA)
    BeginChrThread(0x10A, 3, 0, 9)
    Sleep(1000)
    BeginChrThread(0x108, 3, 0, 9)
    WaitChrThread(0x108, 3)

    def lambda_1267():

        label("loc_1267")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_1267")

    QueueWorkItem2(0x101, 2, lambda_1267)

    def lambda_1279():

        label("loc_1279")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_1279")

    QueueWorkItem2(0x109, 2, lambda_1279)

    def lambda_128B():

        label("loc_128B")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_128B")

    QueueWorkItem2(0x8, 2, lambda_128B)
    OP_71(0xA, 0x14B, 0x168, 0x0, 0x0)
    Sound(461, 0, 100, 0)
    OP_79(0xA)
    Sound(470, 0, 80, 0)
    OP_71(0xA, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0xA)
    Sound(494, 0, 90, 0)
    OP_71(0xA, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-2000, 1100, 9600, 2000)

    def lambda_12EA():
        OP_96(0xFE, 0xFFFFD6FC, 0x0, 0x34BC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_12EA)
    Sleep(2000)
    Sound(457, 0, 100, 0)
    Fade(500)
    EndChrThread(0xA, 0x1)
    SetChrPos(0xA, -15000, 0, 18000, 0)

    def lambda_1327():
        OP_96(0xFE, 0xFFFF3CB0, 0x0, 0x4650, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1327)
    OP_68(-18000, 900, 18000, 0)
    MoveCamera(60, 27, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16500, 0)
    OP_68(-30000, 900, 18000, 4000)
    MoveCamera(60, 21, 0, 4000)
    SetCameraDistance(23500, 4000)
    OP_6F(0x79)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x8, 0x2)
    Fade(500)
    StopSound(457, 500, 90)
    OP_68(500, 1000, 8500, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, -800, 0, 8900, 270)
    SetChrPos(0x109, -900, 0, 7600, 270)
    SetChrPos(0x8, 1500, 0, 8500, 270)
    OP_0D()

    #C0029
    ChrTalk(
        0x8,
        (
            "#04309F#11P哎呀～你们真是很幸运。\x02\x03",

            "#04311F虽然不在同一职场，\x01",
            "但遇到了很好的前辈呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1468():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1468)
    Sleep(50)
    TurnDirection(0x109, 0x8, 500)

    #C0030
    ChrTalk(
        0x101,
        "#00002F#6P嗯，我也这样想。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x109,
        (
            "#6P#10104F是啊……\x01",
            "其中也包括赛尔盖科长。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "#04300F#11P你们接下来有何打算？\x02\x03",

            "直接乘列车\x01",
            "回克洛斯贝尔吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#00004F#6P是的，正是这样计划的。\x02\x03",

            "#00005F对了……\x01",
            "凯文神父，您还有其它安排吗？\x02\x03",

            "#00000F这里离克洛斯贝尔只有一站……\x01",
            "如果时间方便，希望您去我们\x01",
            "那里做客，让我们略表谢意。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "#04306F#11P啊～感谢你们的好意，\x01",
            "不过我已经约了人。\x02\x03",

            "#04308F其实我很想向你们了解一下\x01",
            "那个教团的详细情况……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0035
    ChrTalk(
        0x101,
        "#00013F#6PＤ∴Ｇ教团吗……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x109,
        (
            "#6P#10101F教会自然也掌握到了\x01",
            "一些信息吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#04306F#11P啊～完全没有。\x02\x03",

            "#04300F我们最后一次接触教团，\x01",
            "还是在四年前的某起事件中。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x109,
        "#6P#10105F四年前……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#00005F#6P在各国军队与游击士协会\x01",
            "联手发起的那场镇压作战之后吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "#04303F#11P嗯，在那场作战结束之后，\x01",
            "我们击溃了漏网的教团据点之一。\x02\x03",

            "#04308F……这话只能在这里说，那个据点\x01",
            "在教团之中都称得上是最恶劣的地方。\x02\x03",

            "#04301F老实说，和那些家伙举行的恐怖仪式相比，\x01",
            "连各种人体实验都算是小巫见大巫了。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        "#00006F#6P……是吗。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x109,
        (
            "#6P#10106F实在是……\x01",
            "最可恨的败类啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "#04304F#11P嗯，就在那个时候，\x01",
            "亚里欧斯先生帮了我们很大的忙。\x02\x03",

            "#04311F当时欠他的大人情一直没有还，\x01",
            "这次能帮上他的忙，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#00002F#6P原来是这样啊……\x02\x03",

            "#00004F不管怎么说，多亏有您协助，\x01",
            "我们才能活捉犯人。\x02\x03",

            "#00000F非常感谢，\x01",
            "您真是帮了大忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "#04304F#11P哪里哪里。\x02\x03",

            "#04302F正如刚才那个戴眼镜的人所说，\x01",
            "起到关键作用的人其实是你。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0046
    ChrTalk(
        0x101,
        "#00005F#6P我吗？\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "#04304F#11P嗯，正是由于听到了\x01",
            "你的鼓舞，那位老兄才能在\x01",
            "危险时刻勉强撑住。\x02\x03",

            "#04300F否则的话，就算我赶来处理，\x01",
            "恐怕也救不了他了。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        "#00002F#6P是这样吗……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(200)

    #C0049
    ChrTalk(
        0x109,
        (
            "#12P#10109F嗯，肯定是这样的！\x02\x03",

            "#10102F正是因为罗伊德警官拼命劝慰他，\x01",
            "他才能恢复自我！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(150)

    #C0050
    ChrTalk(
        0x101,
        "#00005F#5P上士……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "#04309F#11P哈哈……\x01",
            "你们是叫『特别任务支援科』吧？\x02\x03",

            "#04302F以后要是有机会，\x01",
            "就把当时的详细情况讲给我听吧。\x02\x03",

            "虽然教团事件至此应该\x01",
            "已经算是彻底结束了，\x01",
            "但以后说不定还会发生什么情况呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1BF3():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1BF3)
    Sleep(50)
    TurnDirection(0x109, 0x8, 500)

    #C0052
    ChrTalk(
        0x101,
        (
            "#00004F#6P哈哈，我明白了。\x02\x03",

            "#00000F……那我们\x01",
            "这就告辞了。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x109,
        "#6P#10109F您辛苦了！\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "#04311F#11P嗯！\x01",
            "你们也辛苦了！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(500, 1000, 11400, 4000)

    def lambda_1C99():

        label("loc_1C99")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1C99")

    QueueWorkItem2(0x8, 2, lambda_1C99)
    BeginChrThread(0x101, 3, 0, 10)
    BeginChrThread(0x109, 3, 0, 11)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x109, 3)
    EndChrThread(0x8, 0x2)
    Sleep(500)

    #C0055
    ChrTalk(
        0x8,
        (
            "#04300F#11P罗伊德吗……\x01",
            "真是个很有前途的年轻人啊。\x02\x03",

            "#04304F听说之前还帮了\x01",
            "艾丝蒂尔他们的忙。\x02\x03",

            "#04308F不过……这次的事情\x01",
            "恐怕还是过于严峻了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x9, 7100, 0, 2300, 315)
    ClearChrFlags(0x9, 0x80)

    #N0056
    NpcTalk(
        0x9,
        "年轻女孩的声音",
        "凯文。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(5300, 1000, 3800, 0)
    MoveCamera(83, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_68(2300, 1000, 7800, 3500)
    SetCameraDistance(16500, 3500)

    def lambda_1DEB():
        OP_95(0xFE, 3100, 0, 7300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1DEB)
    OP_0D()
    TurnDirection(0x8, 0x9, 500)
    WaitChrThread(0x9, 1)
    TurnDirection(0x9, 0x8, 500)
    EndChrThread(0x8, 0x2)
    OP_6F(0x79)

    #C0057
    ChrTalk(
        0x8,
        (
            "#6P#04302F哦，你好慢啊。\x02\x03",

            "#04305F……嗯？那个纸袋是……？\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0058
    AnonymousTalk(
        0x9,
        (
            "在那边的路边摊买的\x01",
            "阿尔泰尔特产──炒栗子。\x02\x03",

            "又热又香甜，\x01",
            "味道绝妙呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0059
    ChrTalk(
        0x8,
        (
            "#6P#04306F那也不用买\x01",
            "这么一大袋吧……\x02\x03",

            "#04301F真是的，照你这种状态，\x01",
            "今后真的没问题吗？\x02\x03",

            "不然还是让我跟你……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "#13806F#11P……不行，\x01",
            "凯文早就臭名昭著了。\x02\x03",

            "#13811F要是被艾拉尔达大主教发现了，\x01",
            "他说不定会当场把你绑起来处以火刑。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "#6P#04305F再、再怎么说，\x01",
            "也不至于那么恐怖吧！？\x02\x03",

            "#04308F不对，毕竟之前有\x01",
            "典礼省的奥恩事件……\x02\x03",

            "#04306F那件事使大主教对封圣省的\x01",
            "态度越发强硬了。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        (
            "#13803F#11P所以说，要想掩人耳目，\x01",
            "就只能让我一个人去。\x02\x03",

            "#13801F凯文，你应该\x01",
            "也明白吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "#6P#04306F唉，真是的……我知道啦！\x02\x03",

            "#04308F总长也真是的，\x01",
            "为什么偏偏选你这家伙……\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x9,
        (
            "#13804F#11P因为我是最合适的人选。\x02\x03",

            "#13802F凯文，我不在的时候，\x01",
            "你可不要鲁莽行事。\x02\x03",

            "别让塞萨尔和玛卡斯\x01",
            "太操心。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "#6P#04303F好好好，我知道了。\x02\x03",

            "#04301F……莉丝，\x01",
            "你一定要多加小心啊。\x02\x03",

            "老实说，你要去的那个地方，\x01",
            "今后无论发生什么情况都不足为奇。\x02\x03",

            "遇到紧急情况时要立刻找我，\x01",
            "或祭出王牌哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "#13805F#11P我明白……\x02\x03",

            "#13801F……但情况真的有那么糟糕吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "#6P#04306F是的……\x01",
            "对圣俗双方而言，都是如此。\x02\x03",

            "#04301F而且『那些家伙』\x01",
            "好像也开始在暗中行动了。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    SetCameraDistance(17000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0068
    AnonymousTalk(
        0x8,
        (
            "#30W魔都克洛斯贝尔……\x01",
            "说不定要变成真正意义上的魔都了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CC(0x1, 0xFF, 0x0)
    RemoveParty(0x9, 0xFF)
    RemoveParty(0x7, 0xFF)
    SetScenarioFlags(0x25, 2)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x235), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(1500)
    SetScenarioFlags(0x22, 2)
    NewScene("e4800", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_419 end

    def Function_4_23AB(): pass

    label("Function_4_23AB")

    OP_96(0x16, 0xFFFFBF8C, 0x0, 0x445C, 0x1770, 0x0)
    OP_9E(0x16, 0xFFFFBF8C, 0x30D4, 0x15F90, 0x1388, 0x1)
    OP_96(0x16, 0xFFFFD314, 0x0, 0x5DC, 0x1770, 0x0)
    OP_9E(0x16, 0xFFFFBBA4, 0x5DC, 0x15F90, 0x1388, 0x1)
    OP_96(0x16, 0xFFFF9A70, 0x0, 0xFFFFEE6C, 0x1770, 0x0)
    OP_9E(0x16, 0xFFFF9A70, 0xFFFFDAE4, 0xFFFEA070, 0x1388, 0x1)
    OP_96(0x16, 0xFFFF86E8, 0x0, 0xFFFF88DC, 0x1770, 0x0)
    Return()

    # Function_4_23AB end

    def Function_5_243B(): pass

    label("Function_5_243B")

    Sleep(5500)
    OP_68(-24960, 1900, -3590, 6000)
    MoveCamera(24, 19, 0, 6000)
    OP_6E(700, 6000)
    SetCameraDistance(24000, 6000)
    OP_6F(0x79)
    Return()

    # Function_5_243B end

    def Function_6_246F(): pass

    label("Function_6_246F")

    OP_95(0x12, 0, 0, -10500, 2000, 0x0)
    OP_95(0x12, 4700, 0, -5400, 2000, 0x0)

    def lambda_249C():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_249C)
    TurnDirection(0x12, 0xD, 500)
    BeginChrThread(0x12, 0, 0, 0)
    Sleep(1000)
    OP_63(0x12, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    Return()

    # Function_6_246F end

    def Function_7_24C7(): pass

    label("Function_7_24C7")

    ClearMapObjFlags(0x0, 0x10)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)

    def lambda_24E5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_24E5)
    OP_95(0x13, 10500, 0, 6000, 2000, 0x0)
    OP_95(0x13, 10500, 0, -5000, 2000, 0x0)
    OP_9E(0x13, 0x7D0, 0xFFFFEC78, 0x15F90, 0x7D0, 0x1)
    OP_95(0x13, 2000, 0, -30000, 2000, 0x0)
    OP_70(0x0, 0x0)
    Return()

    # Function_7_24C7 end

    def Function_8_2547(): pass

    label("Function_8_2547")

    OP_95(0x14, 12000, 0, 15500, 2000, 0x0)
    OP_95(0x14, 30000, 0, 15500, 2000, 0x0)

    def lambda_2574():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_2574)
    Return()

    # Function_8_2547 end

    def Function_9_2581(): pass

    label("Function_9_2581")

    OP_92(0xFE, 0xFFFFFE70, 0x2EE0, 0x1F4)
    OP_95(0xFE, -400, 0, 12000, 2000, 0x0)

    def lambda_25A7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_25A7)
    OP_95(0xFE, -400, 150, 13500, 1500, 0x0)
    Return()

    # Function_9_2581 end

    def Function_10_25C8(): pass

    label("Function_10_25C8")

    OP_92(0xFE, 0xFFFFFE70, 0x4074, 0x1F4)
    OP_95(0xFE, -400, 0, 16500, 2500, 0x0)
    OP_95(0xFE, -400, 1100, 20500, 2500, 0x0)

    def lambda_2602():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2602)
    OP_95(0xFE, -400, 1100, 22500, 2500, 0x0)
    Return()

    # Function_10_25C8 end

    def Function_11_2623(): pass

    label("Function_11_2623")

    Sleep(100)
    OP_92(0xFE, 0xFFFFFDA8, 0x4074, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -600, 0, 16500, 2500, 0x0)
    OP_95(0xFE, -600, 1100, 20500, 2500, 0x0)

    def lambda_2663():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2663)
    OP_95(0xFE, -600, 1100, 22500, 2500, 0x0)
    Return()

    # Function_11_2623 end

    def Function_12_2684(): pass

    label("Function_12_2684")

    Sleep(2000)
    Sound(467, 0, 80, 0)
    Sleep(200)
    Sound(465, 0, 100, 0)
    Sleep(5300)
    Sound(471, 0, 100, 0)
    Return()

    # Function_12_2684 end

    def Function_13_26A0(): pass

    label("Function_13_26A0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-1960, 5600, 11900, 0)
    MoveCamera(40, 14, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(13600, 0)
    SetChrPos(0x101, 80, 0, 15350, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2711")
    SetChrPos(0x102, -1100, 0, 15350, 180)
    Jump("loc_27A4")

    label("loc_2711")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2737")
    SetChrPos(0x103, -1100, 0, 15350, 180)
    Jump("loc_27A4")

    label("loc_2737")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_275D")
    SetChrPos(0x104, -1100, 0, 15350, 180)
    Jump("loc_27A4")

    label("loc_275D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2783")
    SetChrPos(0x109, -1100, 0, 15350, 180)
    Jump("loc_27A4")

    label("loc_2783")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_27A4")
    SetChrPos(0x105, -1100, 0, 15350, 180)

    label("loc_27A4")

    SetChrPos(0x1A1, 1150, 0, 15350, 180)
    LoadChrToIndex("chr/ch24100.itc", 0x1E)
    LoadChrToIndex("chr/ch41200.itc", 0x1F)
    LoadChrToIndex("chr/ch31400.itc", 0x20)
    LoadChrToIndex("chr/ch31500.itc", 0x21)
    SetChrChipByIndex(0x18, 0x1E)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, -50, 0, 11950, 0)
    SetChrChipByIndex(0x19, 0x1F)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, -840, 0, 11950, 0)
    SetChrChipByIndex(0x1A, 0x1F)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 720, 0, 11950, 0)
    SetChrChipByIndex(0x1B, 0x20)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, -20430, 0, 2990, 45)
    SetChrChipByIndex(0x1C, 0x21)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, -21600, 0, 2950, 45)
    ClearChrFlags(0x17, 0x80)
    OP_78(0xA, 0x17)
    OP_49()
    SetChrPos(0x17, -500, 0, 8940, 0)
    OP_D5(0x17, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    OP_74(0xA, 0x1E)
    OP_70(0xA, 0x0)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    OP_68(-1960, 1900, 11900, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0069
    ChrTalk(
        0x19,
        (
            "克洛斯贝尔警察局的各位，\x01",
            "你们辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x19,
        (
            "这些人就由\x01",
            "我们带走。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        "#00000F非常感谢。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x1A1,
        "拜、拜托你们了～\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x1A,
        "喂，快走快走。\x02",
    )

    CloseMessageWindow()

    def lambda_2971():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2971)

    def lambda_297E():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_297E)
    Sleep(300)
    OP_93(0x18, 0xB4, 0x1F4)

    def lambda_2995():
        OP_95(0xFE, -840, 0, 10950, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_2995)

    def lambda_29AF():
        OP_95(0xFE, 720, 0, 10950, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_29AF)

    def lambda_29C9():
        OP_95(0xFE, -50, 0, 10950, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_29C9)
    WaitChrThread(0x18, 1)
    Sleep(500)
    OP_93(0x18, 0x0, 0x1F4)

    #C0074
    ChrTalk(
        0x18,
        "你、你们几个……\x02",
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0075
    ChrTalk(
        0x18,
        (
            "#5S此仇我一定会报的，\x01",
            "你们给我等着瞧吧！#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1A1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_93(0x1A, 0x10E, 0x1F4)

    #C0076
    ChrTalk(
        0x1A,
        "喂，不要随便讲话！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x1A, 500)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0077
    ChrTalk(
        0x18,
        (
            "#5S真啰嗦！\x01",
            "你们这些废物军人！#3S\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0078
    ChrTalk(
        0x18,
        (
            "#5S对待女士\x01",
            "要有礼貌啊！#3S\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x1A,
        "废、废物军人！？\x02",
    )

    CloseMessageWindow()
    OP_93(0x19, 0x5A, 0x1F4)

    #C0080
    ChrTalk(
        0x19,
        "……好了，赶快带走。\x02",
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Sound(462, 0, 100, 0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x169, 0x186, 0x1, 0x8)
    Sleep(1500)
    SetChrFlags(0x18, 0x40)
    SetChrFlags(0x18, 0x4)
    SetChrFlags(0x1A, 0x40)
    SetChrFlags(0x1A, 0x4)
    BeginChrThread(0x18, 1, 0, 15)
    BeginChrThread(0x1A, 1, 0, 16)
    WaitChrThread(0x1A, 1)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x1A, 0x80)
    Sound(461, 0, 100, 0)
    OP_71(0xA, 0x187, 0x1A4, 0x1, 0x8)
    Sleep(1500)

    #C0081
    ChrTalk(
        0x101,
        (
            "#00006F该、该怎么说呢……\x01",
            "总觉得她今后真的会再次出现。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C39")

    #C0082
    ChrTalk(
        0x102,
        "#00106F我也有同感……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CE8")

    label("loc_2C39")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C61")

    #C0083
    ChrTalk(
        0x103,
        "#00206F同感。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CE8")

    label("loc_2C61")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C8B")

    #C0084
    ChrTalk(
        0x104,
        "#00306F同感啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CE8")

    label("loc_2C8B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CB9")

    #C0085
    ChrTalk(
        0x109,
        "#10106F我有同感……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2CE8")

    label("loc_2CB9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CE8")

    #C0086
    ChrTalk(
        0x105,
        "#10302F呵呵，我也有同感。\x02",
    )

    CloseMessageWindow()

    label("loc_2CE8")

    OP_93(0x19, 0x0, 0x1F4)

    #C0087
    ChrTalk(
        0x19,
        (
            "……我们一定妥善处理，\x01",
            "不会让这种事情发生的。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x19,
        (
            "总之，你们辛苦了，\x01",
            "回去的路上多加小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        "#00000F啊……好的，您辛苦了。\x02",
    )

    CloseMessageWindow()
    OP_93(0x19, 0xB4, 0x1F4)
    Sound(462, 0, 100, 0)
    OP_71(0xA, 0xF1, 0x10E, 0x1, 0x8)
    Sleep(1500)
    SetChrFlags(0x19, 0x40)
    SetChrFlags(0x19, 0x4)

    def lambda_2D9D():
        OP_95(0xFE, -840, 150, 9610, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_2D9D)
    OP_A7(0x19, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Sound(461, 0, 100, 0)
    OP_71(0xA, 0x10F, 0x12C, 0x1, 0x8)
    Sleep(1500)
    Sound(470, 0, 50, 0)
    OP_71(0xA, 0x3C, 0x5A, 0x1, 0x8)
    Sleep(1000)
    Sound(457, 0, 100, 0)
    OP_71(0xA, 0x79, 0xB4, 0x1, 0x20)
    OP_68(-8150, 1900, 6710, 2500)
    MoveCamera(35, 31, 0, 2500)
    OP_6E(580, 2500)
    SetCameraDistance(18500, 2500)
    BeginChrThread(0x17, 1, 0, 17)
    OP_6F(0x79)
    Sleep(2000)
    StopSound(457, 1000, 90)
    Fade(500)
    EndChrThread(0x17, 0x1)
    SetMapObjFlags(0xA, 0x4)
    OP_68(-810, 1900, 13320, 0)
    MoveCamera(27, 23, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(13600, 0)
    SetChrPos(0x101, -200, 0, 15570, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2EAC")
    SetChrPos(0x102, -1040, 0, 14270, 45)
    Jump("loc_2F3F")

    label("loc_2EAC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2ED2")
    SetChrPos(0x103, -1040, 0, 14270, 45)
    Jump("loc_2F3F")

    label("loc_2ED2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2EF8")
    SetChrPos(0x104, -1040, 0, 14270, 45)
    Jump("loc_2F3F")

    label("loc_2EF8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F1E")
    SetChrPos(0x109, -1040, 0, 14270, 45)
    Jump("loc_2F3F")

    label("loc_2F1E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F3F")
    SetChrPos(0x105, -1040, 0, 14270, 45)

    label("loc_2F3F")

    SetChrPos(0x1A1, 750, 0, 14180, 315)
    OP_0D()

    #C0090
    ChrTalk(
        0x101,
        (
            "#00003F呼……\x01",
            "结果也只能这样了。\x02\x03",

            "#00001F其实我很想\x01",
            "亲手逮捕她……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FFE")

    #C0091
    ChrTalk(
        0x102,
        (
            "#00100F嗯，但是……\x01",
            "这也没办法呢。\x02\x03",

            "#00104F没有让她逃掉，\x01",
            "就已经很不错了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31BD")

    label("loc_2FFE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_306B")

    #C0092
    ChrTalk(
        0x103,
        (
            "#00200F我明白你的心情……\x01",
            "但这也没办法呢。\x02\x03",

            "#00204F没有让她逃掉，\x01",
            "就已经很不错了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31BD")

    label("loc_306B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30D4")

    #C0093
    ChrTalk(
        0x104,
        (
            "#00306F听你这么一说，\x01",
            "确实啊……\x02\x03",

            "#00300F算啦，没有让她逃掉，\x01",
            "就已经很不错了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31BD")

    label("loc_30D4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3146")

    #C0094
    ChrTalk(
        0x109,
        (
            "#10106F是啊……\x01",
            "感觉有点不甘心。\x02\x03",

            "#10100F……不过，\x01",
            "没有让她逃掉，\x01",
            "就算是不错的结果了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31BD")

    label("loc_3146")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31BD")

    #C0095
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，反正已经\x01",
            "把她抓住了，\x01",
            "那种事情就不要在意啦。\x02\x03",

            "#10304F没有让她逃掉，\x01",
            "就已经很不错了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31BD")


    #C0096
    ChrTalk(
        0x1A1,
        (
            "是啊是啊！\x01",
            "你们真是帮了我的大忙！\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x1A1,
        (
            "哎呀～太好了，太好了。\x01",
            "这样就能向多诺邦警督\x01",
            "交上一份圆满的报告了～\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#00000F哈哈……\x01",
            "也是呢。\x02\x03",

            "好了……\x01",
            "那我们这就回\x01",
            "克洛斯贝尔市吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32B0")

    #C0099
    ChrTalk(
        0x102,
        (
            "#00100F嗯，\x01",
            "一直留在这里\x01",
            "也不太好。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33A5")

    label("loc_32B0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32EC")

    #C0100
    ChrTalk(
        0x103,
        (
            "#00200F嗯，\x01",
            "总不能一直\x01",
            "留在这里。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33A5")

    label("loc_32EC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_332C")

    #C0101
    ChrTalk(
        0x104,
        (
            "#00300F嗯，\x01",
            "我们也没时间\x01",
            "在这里久留。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33A5")

    label("loc_332C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_336C")

    #C0102
    ChrTalk(
        0x109,
        (
            "#10100F嗯，\x01",
            "我们也没时间\x01",
            "在这里久留。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33A5")

    label("loc_336C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33A5")

    #C0103
    ChrTalk(
        0x105,
        (
            "#10300F嗯，\x01",
            "一直留在这里\x01",
            "也不太好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33A5")


    #C0104
    ChrTalk(
        0x1A1,
        (
            "唔～但难得\x01",
            "来一趟共和国……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x1A1,
        (
            "真想顺便去一些\x01",
            "旅游景点观光啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        "#00006F还、还是下次再说吧……\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x0, 1, 0, 14)
    Sleep(50)
    BeginChrThread(0x1, 1, 0, 14)
    Sleep(50)
    BeginChrThread(0x1A1, 1, 0, 14)
    Sleep(1000)
    OP_68(-18880, 1900, 2270, 5000)
    MoveCamera(41, 24, 0, 5000)
    OP_6E(700, 5000)
    SetCameraDistance(15100, 5000)
    OP_6F(0x79)

    #C0107
    ChrTalk(
        0x1B,
        (
            "没想到最后\x01",
            "会如此收场……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x1C,
        (
            "……算了，\x01",
            "反正完成了最低目标，\x01",
            "没有让那些余党跑掉。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x1C,
        (
            "回去向曹先生\x01",
            "报告吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x1B,
        "嗯，走吧……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x1A1, 0x1)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x1A1)
    SetChrName("")

    #A0111
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德一行人等来了\x01",
            "驶往克洛斯贝尔的列车……\x02\x03",

            "连说带劝地拉着对土特产商店恋恋不舍的\x01",
            "雷蒙德离开了共和国。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    SetScenarioFlags(0x22, 6)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    EventEnd(0x5)
    Return()

    # Function_13_26A0 end

    def Function_14_35A8(): pass

    label("Function_14_35A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_36C0")
    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_35EB"),
        (1, "loc_3605"),
        (2, "loc_361F"),
        (3, "loc_3639"),
        (4, "loc_3653"),
        (5, "loc_366D"),
        (6, "loc_3687"),
        (SWITCH_DEFAULT, "loc_36A1"),
    )


    label("loc_35EB")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_36BB")

    label("loc_3605")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(2000)
    Jump("loc_36BB")

    label("loc_361F")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(3000)
    Jump("loc_36BB")

    label("loc_3639")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_36BB")

    label("loc_3653")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1800)
    Jump("loc_36BB")

    label("loc_366D")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jump("loc_36BB")

    label("loc_3687")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_36BB")

    label("loc_36A1")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("loc_36BB")

    label("loc_36BB")

    Jump("Function_14_35A8")

    label("loc_36C0")

    Return()

    # Function_14_35A8 end

    def Function_15_36C1(): pass

    label("Function_15_36C1")

    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_36CD():
        OP_96(0xFE, 0xFFFFFFCE, 0x96, 0x258A, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_36CD)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_15_36C1 end

    def Function_16_36EE(): pass

    label("Function_16_36EE")

    OP_95(0xFE, -50, 0, 10950, 1000, 0x0)

    def lambda_3707():
        OP_95(0xFE, -50, 150, 9610, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3707)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    Return()

    # Function_16_36EE end

    def Function_17_3728(): pass

    label("Function_17_3728")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -500, 0, 8940)
    OP_9F(0x1, -6550, 0, 8940)
    OP_9F(0x1, -7500, 0, 8400)
    OP_9F(0x1, -8100, 0, 7000)
    OP_9F(0x1, -8200, 0, 4200)
    OP_9F(0x1, -8360, 0, -4860)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    Return()

    # Function_17_3728 end

    SaveToFile()

Try(main)
