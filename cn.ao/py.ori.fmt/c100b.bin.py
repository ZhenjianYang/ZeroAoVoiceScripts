from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c100b.bin",                # FileName
        "c100b",                    # MapName
        "c100b",                    # Location
        0x0010,                     # MapIndex
        "ed7513",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 16, 0, 1, 0, 2],
    )

    BuildStringList((
        "c100b",                  # 0
        "琪雅",                   # 1
        "蔡特",                   # 2
        "滴",                     # 3
        "亚里欧斯",               # 4
        "接待员米歇尔",           # 5
        "车",                     # 6
        "路人",                   # 7
        "路人",                   # 8
        "中央广场",               # 9
        "西街",                   # 10
        "行政区",                 # 11
        "住宅街",                 # 12
        "欢乐街",                 # 13
        "东街",                   # 14
        "旧城区",                 # 15
        "港湾区",                 # 16
        "ＩＢＣ",                 # 17
        "站前街道",               # 18
        "后巷",                   # 19
        "乌尔斯拉间道",           # 20
        "东克洛斯贝尔街道",       # 21
        "西克洛斯贝尔街道",       # 22
        "玛因兹山道",             # 23
        "兰花塔",                 # 24
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-30000,  -5500,   4000,    1200,    -30000,  -4500,   4000,    0x007C, 0,  3,  0x0000)
    DeclActor(-23010,  -14900,  -4830,   1200,    -23010,  -13900,  -4830,   0x007C, 0,  4,  0x0000)

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
    PlaceName(-88.0, 0.0, 269.0, 0x0000, 0x0000, "兰花塔")
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

    ChipFrameInfo(1084, 0)                                       # 0

    ScpFunction((
        "Function_0_43C",          # 00, 0
        "Function_1_4EC",          # 01, 1
        "Function_2_510",          # 02, 2
        "Function_3_53F",          # 03, 3
        "Function_4_67A",          # 04, 4
        "Function_5_7B5",          # 05, 5
        "Function_6_913",          # 06, 6
        "Function_7_95C",          # 07, 7
        "Function_8_98A",          # 08, 8
        "Function_9_C49",          # 09, 9
    ))


    def Function_0_43C(): pass

    label("Function_0_43C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_474"),
        (1, "loc_480"),
        (2, "loc_48C"),
        (3, "loc_498"),
        (4, "loc_4A4"),
        (5, "loc_4B0"),
        (6, "loc_4BC"),
        (SWITCH_DEFAULT, "loc_4C8"),
    )


    label("loc_474")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_4D4")

    label("loc_480")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_4D4")

    label("loc_48C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_4D4")

    label("loc_498")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_4D4")

    label("loc_4A4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_4D4")

    label("loc_4B0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_4D4")

    label("loc_4BC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4D4")

    label("loc_4C8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4D4")

    label("loc_4D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4EB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_4D4")

    label("loc_4EB")

    Return()

    # Function_0_43C end

    def Function_1_4EC(): pass

    label("Function_1_4EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_500")
    ClearScenarioFlags(0x22, 0)
    Event(0, 5)
    Jump("loc_50F")

    label("loc_500")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_50F")
    ClearScenarioFlags(0x22, 1)
    Event(0, 8)

    label("loc_50F")

    Return()

    # Function_1_4EC end

    def Function_2_510(): pass

    label("Function_2_510")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_523")
    OP_70(0xA, 0x0)
    Jump("loc_527")

    label("loc_523")

    OP_70(0xA, 0x1E)

    label("loc_527")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53A")
    OP_70(0xB, 0x0)
    Jump("loc_53E")

    label("loc_53A")

    OP_70(0xB, 0x1E)

    label("loc_53E")

    Return()

    # Function_2_510 end

    def Function_3_53F(): pass

    label("Function_3_53F")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_631")
    Sound(14, 0, 100, 0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('Ｕ材料', 1)"), scpexpr(EXPR_END)), "loc_5C2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_62C")

    label("loc_5C2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 'Ｕ材料'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xA, 0x1E, 0x0, 0x0, 0x0)

    label("loc_62C")

    Jump("loc_66E")

    label("loc_631")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_66E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_53F end

    def Function_4_67A(): pass

    label("Function_4_67A")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76C")
    Sound(14, 0, 100, 0)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('封魔之刃', 1)"), scpexpr(EXPR_END)), "loc_6FD")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '封魔之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_767")

    label("loc_6FD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '封魔之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, '封魔之刃'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xB, 0x1E, 0x0, 0x0, 0x0)

    label("loc_767")

    Jump("loc_7A9")

    label("loc_76C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_7A9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_67A end

    def Function_5_7B5(): pass

    label("Function_5_7B5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrFlags(0x153, 0x8)
    ClearChrFlags(0xD, 0x80)
    OP_78(0xC, 0xD)
    OP_49()
    SetChrPos(0xD, -21000, -350, 28700, 180)
    OP_D5(0xD, 0x0, 0x2BF20, 0x0, 0x0)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x1000)
    OP_74(0xC, 0x1E)
    OP_71(0xC, 0x79, 0xB4, 0x1, 0x20)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_892")
    ClearChrFlags(0xE, 0x80)
    LoadChrToIndex("chr/ch24000.itc", 0x1E)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x4)
    SetChrPos(0xE, -18150, -3000, 4000, 0)
    BeginChrThread(0xE, 3, 0, 7)
    ClearChrFlags(0xF, 0x80)
    LoadChrToIndex("chr/ch21200.itc", 0x1F)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -14050, -300, 16200, 180)

    label("loc_892")

    FadeToBright(1000, 0)
    Sound(458, 0, 100, 0)
    BeginChrThread(0xD, 3, 0, 6)
    OP_68(-24300, 3850, 15000, 0)
    MoveCamera(30, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26850, 0)
    OP_68(-20200, 1850, 15850, 5000)
    MoveCamera(65, 5, 0, 5000)
    Sleep(4500)
    OP_0D()
    StopSound(458, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c020B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_7B5 end

    def Function_6_913(): pass

    label("Function_6_913")

    SetChrPos(0xFE, -21000, -300, 28700, 180)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -21000, -300, 19000)
    OP_9F(0x1, -25350, -300, 14100)
    OP_9F(0x1, -40900, -300, 13900)
    OP_9F(0x2, 0xFE, 5000, 0x6)
    Return()

    # Function_6_913 end

    def Function_7_95C(): pass

    label("Function_7_95C")

    OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
    OP_9B(0x0, 0xFE, 0x5A, 0xBB8, 0x7D0, 0x0)
    OP_9B(0x0, 0xFE, 0x2D, 0x3A98, 0x7D0, 0x0)
    Return()

    # Function_7_95C end

    def Function_8_98A(): pass

    label("Function_8_98A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02710.itc", 0x1E)
    LoadChrToIndex("chr/ch08200.itc", 0x1F)
    LoadChrToIndex("chr/ch08700.itc", 0x20)
    LoadChrToIndex("chr/ch02400.itc", 0x21)
    LoadChrToIndex("chr/ch09100.itc", 0x22)
    SetChrPos(0x101, -13750, -300, 13300, 125)
    SetChrPos(0x102, -15150, -300, 12300, 125)
    SetChrPos(0x104, -14900, -300, 13900, 125)
    SetChrPos(0x109, -12050, -300, 14900, 170)
    SetChrPos(0x105, -13400, -300, 15000, 170)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x5)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -15650, -300, 11300, 125)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -13750, -300, 12300, 125)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -11100, -300, 10500, 305)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -11100, -300, 9700, 305)
    SetChrChipByIndex(0xC, 0x22)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -9800, -300, 11600, 305)

    def lambda_AC7():

        label("loc_AC7")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_AC7")

    QueueWorkItem2(0xA, 2, lambda_AC7)

    def lambda_AD9():

        label("loc_AD9")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_AD9")

    QueueWorkItem2(0xB, 2, lambda_AD9)

    def lambda_AEB():

        label("loc_AEB")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_AEB")

    QueueWorkItem2(0xC, 2, lambda_AEB)
    SetMapObjFrame(0xFF, "turi00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "turi01", 0x0, 0x1)
    OP_68(-12700, 900, 11600, 0)
    MoveCamera(71, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0xA, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 500)
    TurnDirection(0x8, 0x101, 500)

    def lambda_B92():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B92)
    Sleep(50)

    def lambda_BA2():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_BA2)
    Sleep(50)

    def lambda_BB2():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_BB2)
    Sleep(1000)
    OP_93(0x8, 0x131, 0x1F4)
    OP_68(-20000, 900, 11600, 9000)
    MoveCamera(53, 17, 0, 9000)
    SetCameraDistance(23000, 9000)
    BeginChrThread(0x9, 3, 0, 9)
    Sleep(400)
    BeginChrThread(0x104, 3, 0, 9)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 9)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 9)
    Sleep(450)
    BeginChrThread(0x102, 3, 0, 9)
    Sleep(50)
    BeginChrThread(0x101, 3, 0, 9)
    BeginChrThread(0x8, 3, 0, 9)
    Sleep(6000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0xA, 0x2)
    EndChrThread(0xB, 0x2)
    EndChrThread(0xC, 0x2)
    SetScenarioFlags(0x22, 0)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_98A end

    def Function_9_C49(): pass

    label("Function_9_C49")

    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_C55():
        OP_97(0xFE, 0xFFFF9E58, 0x0, 0x0, 0x6A4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C55)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_9_C49 end

    SaveToFile()

Try(main)
