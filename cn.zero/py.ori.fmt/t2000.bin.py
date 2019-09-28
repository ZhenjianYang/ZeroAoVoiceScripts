from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t2000.bin",                # FileName
        "t2000",                    # MapName
        "t2000",                    # Location
        0x0059,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 24450, 0, -890, 0, 0, 1, 89, 0, 2, 0, 4],
    )

    BuildStringList((
        "t2000",                  # 0
        "卡塔队员",               # 1
        "罗金斯队员",             # 2
        "比利",                   # 3
        "游客",                   # 4
        "游客",                   # 5
        "游客",                   # 6
        "游客",                   # 7
        "游客",                   # 8
        "游客",                   # 9
        "游客",                   # 10
        "游客库露露",             # 11
        "巴士",                   # 12
        "米蕾优准尉",             # 13
        "西克洛斯贝尔街道",       # 14
    ))

    AddCharChip((
        "chr/ch31200.itc",                   # 00
        "chr/ch31300.itc",                   # 01
        "chr/ch32300.itc",                   # 02
        "chr/ch22100.itc",                   # 03
        "chr/ch22200.itc",                   # 04
        "chr/ch21900.itc",                   # 05
        "chr/ch20400.itc",                   # 06
        "chr/ch20000.itc",                   # 07
        "chr/ch20100.itc",                   # 08
        "chr/ch23600.itc",                   # 09
        "chr/ch34400.itc",                   # 0A
    ))

    DeclNpc(22430,   0,       4730,    90,   257,  0x0, 0,   0,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(22239,   0,       -5489,   90,   257,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(19319,   0,       13449,   270,  385,  0x0, 0,   9,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(13500,   0,       26299,   270,  385,  0x0, 0,   2,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(21540,   200,     -11369,  270,  385,  0x0, 0,   3,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(38529,   0,       -3880,   85,   385,  0x0, 0,   2,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(19920,   200,     -11939,  270,  385,  0x0, 0,   3,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(31100,   200,     -16420,  90,   385,  0x0, 0,   6,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(30870,   0,       22549,   270,  385,  0x0, 0,   7,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(30870,   0,       23530,   270,  385,  0x0, 0,   8,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(26700,   200,     -16879,  135,  385,  0x0, 0,   10,  0,   0,   1,   0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(31260,   0,       27730,   1200,    31260,   1000,    27730,   0x007C, 0,  23, 0x0000)
    DeclActor(18980,   200,     -11720,  1200,    18980,   1700,    -11720,  0x007C, 0,  26, 0x0000)
    DeclActor(39780,   0,       1010,    1200,    39780,   2000,    1010,    0x007C, 0,  11, 0x0000)
    DeclActor(1500,    5050,    -20000,  1200,    1500,    6050,    -20000,  0x007C, 0,  5,  0x0000)

    PlaceName(73.0, 0.0, -4.0, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(5.0, 0.0, -0.800000011920929, 0x0000, 0x0052, "")
    PlaceName(30.850000381469727, 0.0, 27.90999984741211, 0x0000, 0x0055, "")
    PlaceName(39.75, 0.0, 2.5999999046325684, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_378",          # 00, 0
        "Function_1_430",          # 01, 1
        "Function_2_45B",          # 02, 2
        "Function_3_4B8",          # 03, 3
        "Function_4_56D",          # 04, 4
        "Function_5_666",          # 05, 5
        "Function_6_79C",          # 06, 6
        "Function_7_857",          # 07, 7
        "Function_8_973",          # 08, 8
        "Function_9_A08",          # 09, 9
        "Function_10_FA0",         # 0A, 10
        "Function_11_108F",        # 0B, 11
        "Function_12_109D",        # 0C, 12
        "Function_13_18F0",        # 0D, 13
        "Function_14_21A4",        # 0E, 14
        "Function_15_2217",        # 0F, 15
        "Function_16_2282",        # 10, 16
        "Function_17_2311",        # 11, 17
        "Function_18_238F",        # 12, 18
        "Function_19_23D3",        # 13, 19
        "Function_20_2452",        # 14, 20
        "Function_21_24BA",        # 15, 21
        "Function_22_252D",        # 16, 22
        "Function_23_2645",        # 17, 23
        "Function_24_26EC",        # 18, 24
        "Function_25_2C14",        # 19, 25
        "Function_26_3477",        # 1A, 26
    ))


    def Function_0_378(): pass

    label("Function_0_378")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_3B8"),
        (1, "loc_3C4"),
        (2, "loc_3D0"),
        (3, "loc_3DC"),
        (4, "loc_3E8"),
        (5, "loc_3F4"),
        (6, "loc_400"),
        (SWITCH_DEFAULT, "loc_40C"),
    )


    label("loc_3B8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_418")

    label("loc_3C4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_418")

    label("loc_3D0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_418")

    label("loc_3DC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_418")

    label("loc_3E8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_418")

    label("loc_3F4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_418")

    label("loc_400")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_418")

    label("loc_40C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_418")

    label("loc_418")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_42F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_418")

    label("loc_42F")

    Return()

    # Function_0_378 end

    def Function_1_430(): pass

    label("Function_1_430")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_45A")
    OP_94(0xFE, 0x60D6, 0xFFFFB442, 0x7346, 0xFFFFC888, 0x3E8)
    Sleep(400)
    Jump("Function_1_430")

    label("loc_45A")

    Return()

    # Function_1_430 end

    def Function_2_45B(): pass

    label("Function_2_45B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 1)), scpexpr(EXPR_END)), "loc_467")
    Call(0, 3)

    label("loc_467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_476")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 25)

    label("loc_476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x88, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_490")
    SetMapFlags(0x10000000)
    Event(0, 24)
    SetScenarioFlags(0x88, 1)
    Jump("loc_4B7")

    label("loc_490")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_49F")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 8)

    label("loc_49F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_4B7")
    ClearScenarioFlags(0x7E, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 10)

    label("loc_4B7")

    Return()

    # Function_2_45B end

    def Function_3_4B8(): pass

    label("Function_3_4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4D0")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_559")

    label("loc_4D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4E3")
    ClearChrFlags(0xF, 0x80)
    Jump("loc_559")

    label("loc_4E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4F1")
    Jump("loc_559")

    label("loc_4F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4FF")
    Jump("loc_559")

    label("loc_4FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_50D")
    Jump("loc_559")

    label("loc_50D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_520")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_559")

    label("loc_520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_533")
    ClearChrFlags(0xD, 0x80)
    Jump("loc_559")

    label("loc_533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_54B")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_559")

    label("loc_54B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_559")
    ClearChrFlags(0xB, 0x80)

    label("loc_559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56C")
    ClearChrFlags(0x12, 0x80)

    label("loc_56C")

    Return()

    # Function_3_4B8 end

    def Function_4_56D(): pass

    label("Function_4_56D")

    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x5, 0x4)
    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5CA")
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    ClearMapObjFlags(0x5, 0x4)
    OP_66(0x2, 0x1)
    Jump("loc_5CF")

    label("loc_5CA")

    OP_16(0x3, 0x3, 0x1, 0x0)

    label("loc_5CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5DD")
    Jump("loc_64E")

    label("loc_5DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_5EB")
    Jump("loc_64E")

    label("loc_5EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_5F9")
    Jump("loc_64E")

    label("loc_5F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_607")
    Jump("loc_64E")

    label("loc_607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_615")
    Jump("loc_64E")

    label("loc_615")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_623")
    Jump("loc_64E")

    label("loc_623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_631")
    Jump("loc_64E")

    label("loc_631")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_645")
    ClearMapObjFlags(0x3, 0x4)
    Jump("loc_64E")

    label("loc_645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_64E")

    label("loc_64E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_661")
    OP_70(0x6, 0x0)
    Jump("loc_665")

    label("loc_661")

    OP_70(0x6, 0x1E)

    label("loc_665")

    Return()

    # Function_4_56D end

    def Function_5_666(): pass

    label("Function_5_666")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_753")
    Sound(14, 0, 100, 0)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('弹簧跑鞋', 1)"), scpexpr(EXPR_END)), "loc_6E5")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x646),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x113, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_74E")

    label("loc_6E5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x646),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x646),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x6, 0x1E, 0x0, 0x0, 0x0)

    label("loc_74E")

    Jump("loc_790")

    label("loc_753")

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

    label("loc_790")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_666 end

    def Function_6_79C(): pass

    label("Function_6_79C")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士车站。\x01",
            "要乘坐巴士吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "克洛斯贝尔市西出口\x01",          # 0
            "停靠站（警察学校附近）\x01",      # 1
            "放弃\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_82F")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_84F")

    label("loc_82F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84F")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1030", 0, 0, 0)
    IdleLoop()

    label("loc_84F")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_79C end

    def Function_7_857(): pass

    label("Function_7_857")

    Fade(1000)
    OP_68(27670, 1000, 21230, 0)
    MoveCamera(319, 34, 0, 0)
    OP_6E(590, 0)
    SetCameraDistance(23500, 0)
    OP_E0(0x1)
    SetChrPos(0x0, 32119, 0, 25500, 270)
    SetChrPos(0x1, 32119, 0, 24000, 270)
    SetChrPos(0x2, 32119, 0, 22500, 270)
    SetChrPos(0x3, 32119, 0, 21000, 270)
    ClearChrFlags(0x13, 0x80)
    ClearMapObjFlags(0x4, 0x4)
    OP_78(0x4, 0x13)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x13, 27000, 0, 4810, 0)
    OP_D3(0x13, 0x0, 0x1F4, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_0D()
    OP_71(0x4, 0x79, 0xB4, 0x0, 0x20)

    def lambda_92D():
        OP_95(0xFE, 27000, 0, 23850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_92D)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x13, 1)
    OP_71(0x4, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x4)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_7_857 end

    def Function_8_973(): pass

    label("Function_8_973")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, 31190, 0, 26620, 265)
    SetChrPos(0x1, 31190, 0, 26620, 265)
    SetChrPos(0x2, 31190, 0, 26620, 265)
    SetChrPos(0x3, 31190, 0, 26620, 265)
    OP_68(31190, 1000, 26620, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_8_973 end

    def Function_9_A08(): pass

    label("Function_9_A08")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)    #voice#Noel
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A22")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F98")

    Menu(
        0,
        32,
        26,
        1,
        (
            "使用警备队车辆进行移动\x01",      # 0
            "在此处休息\x01",                  # 1
            "放弃\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F35")
    Sound(1500, 255, 100, 0)    #voice#Noel
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AB0")
    MenuCmd(1, 1, "★克洛斯贝尔市·中央广场")
    MenuCmd(3, 1, 0x0)
    Jump("loc_ACC")

    label("loc_AB0")

    MenuCmd(1, 1, "　克洛斯贝尔市·中央广场")

    label("loc_ACC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AFE")
    MenuCmd(1, 1, "★克洛斯贝尔市·东出口")
    MenuCmd(3, 1, 0x1)
    Jump("loc_B18")

    label("loc_AFE")

    MenuCmd(1, 1, "  克洛斯贝尔市·东出口")

    label("loc_B18")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B4A")
    MenuCmd(1, 1, "★克洛斯贝尔市·西出口")
    MenuCmd(3, 1, 0x2)
    Jump("loc_B64")

    label("loc_B4A")

    MenuCmd(1, 1, "　克洛斯贝尔市·西出口")

    label("loc_B64")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B96")
    MenuCmd(1, 1, "★克洛斯贝尔市·南出口")
    MenuCmd(3, 1, 0x3)
    Jump("loc_BB0")

    label("loc_B96")

    MenuCmd(1, 1, "　克洛斯贝尔市·南出口")

    label("loc_BB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE2")
    MenuCmd(1, 1, "★克洛斯贝尔市·北出口")
    MenuCmd(3, 1, 0x4)
    Jump("loc_BFC")

    label("loc_BE2")

    MenuCmd(1, 1, "　克洛斯贝尔市·北出口")

    label("loc_BFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C24")
    MenuCmd(1, 1, "★唐古拉姆门")
    MenuCmd(3, 1, 0x5)
    Jump("loc_C34")

    label("loc_C24")

    MenuCmd(1, 1, "　唐古拉姆门")

    label("loc_C34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C5C")
    MenuCmd(1, 1, "★贝尔加德门")
    MenuCmd(3, 1, 0x6)
    Jump("loc_C6C")

    label("loc_C5C")

    MenuCmd(1, 1, "　贝尔加德门")

    label("loc_C6C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C9A")
    MenuCmd(1, 1, "★乌尔斯拉医科大学")
    MenuCmd(3, 1, 0x7)
    Jump("loc_CB0")

    label("loc_C9A")

    MenuCmd(1, 1, "　乌尔斯拉医科大学")

    label("loc_CB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDA")
    MenuCmd(1, 1, "★阿尔摩利卡村")
    MenuCmd(3, 1, 0x8)
    Jump("loc_CEC")

    label("loc_CDA")

    MenuCmd(1, 1, "　阿尔摩利卡村")

    label("loc_CEC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D16")
    MenuCmd(1, 1, "★矿山镇玛因兹")
    MenuCmd(3, 1, 0x9)
    Jump("loc_D28")

    label("loc_D16")

    MenuCmd(1, 1, "　矿山镇玛因兹")

    label("loc_D28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D58")
    MenuCmd(1, 1, "★玛因兹山道·隧道内")
    MenuCmd(3, 1, 0xA)
    Jump("loc_D70")

    label("loc_D58")

    MenuCmd(1, 1, "　玛因兹山道·隧道内")

    label("loc_D70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D96")
    MenuCmd(1, 1, "★星见之塔")
    MenuCmd(3, 1, 0xB)
    Jump("loc_DA4")

    label("loc_D96")

    MenuCmd(1, 1, "　星见之塔")

    label("loc_DA4")

    MenuCmd(1, 1, "　放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F26")
    OP_60(0x0)
    Sleep(500)
    Sound(1501, 255, 100, 0)    #voice#Noel
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xF1, 0x10E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x5)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    Sleep(500)
    OP_0D()
    Sound(488, 0, 100, 0)
    Sleep(2500)
    SetScenarioFlags(0x7E, 1)
    SetScenarioFlags(0x7F, 6)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E79"),
        (1, "loc_E87"),
        (2, "loc_E95"),
        (3, "loc_EA3"),
        (4, "loc_EB1"),
        (5, "loc_EBF"),
        (6, "loc_ECD"),
        (7, "loc_EDB"),
        (8, "loc_EE9"),
        (9, "loc_EF7"),
        (10, "loc_F05"),
        (11, "loc_F13"),
        (SWITCH_DEFAULT, "loc_F21"),
    )


    label("loc_E79")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_F21")

    label("loc_E87")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_F21")

    label("loc_E95")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_F21")

    label("loc_EA3")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_F21")

    label("loc_EB1")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_F21")

    label("loc_EBF")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_F21")

    label("loc_ECD")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_F21")

    label("loc_EDB")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_F21")

    label("loc_EE9")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_F21")

    label("loc_EF7")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_F21")

    label("loc_F05")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_F21")

    label("loc_F13")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_F21")

    label("loc_F21")

    Jump("loc_F30")

    label("loc_F26")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F30")

    Jump("loc_F93")

    label("loc_F35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F80")
    OP_60(0x0)
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    Jump("loc_F93")

    label("loc_F80")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F93")

    Jump("loc_A22")

    label("loc_F98")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_A08 end

    def Function_10_FA0(): pass

    label("Function_10_FA0")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, 39720, 0, -990, 175)
    SetChrPos(0x1, 39720, 0, -990, 175)
    SetChrPos(0x2, 39720, 0, -990, 175)
    SetChrPos(0x3, 39720, 0, -990, 175)
    SetChrPos(0x4, 39720, 0, -990, 175)
    SetChrPos(0x5, 39720, 0, -990, 175)
    Sleep(1)
    OP_68(39720, 1000, -990, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    Sound(489, 0, 100, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1074")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_107A")

    label("loc_1074")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_107A")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_FA0 end

    def Function_11_108F(): pass

    label("Function_11_108F")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)
    Return()

    # Function_11_108F end

    def Function_12_109D(): pass

    label("Function_12_109D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A4")

    #C0005
    ChrTalk(
        0xFE,
        (
            "这贝尔加德门可是\x01",
            "守卫帝国方向国境的要塞哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x104, 300)

    #C0006
    ChrTalk(
        0xFE,
        (
            "哎呀……？\x01",
            "你、你不是兰迪吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        "#0300F……哟，好久不见啊。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "哈哈……你能再来，我很高兴。\x01",
            "还以为你再也不会\x01",
            "出现在这边了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        "总之，你就随便转转吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8C, 0)
    Jump("loc_18EC")

    label("loc_11A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_120B")

    #C0010
    ChrTalk(
        0xFE,
        "今晚计划举行夜间演习呢。\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "我们平时也积攒了不少郁愤，\x01",
            "要借这次机会好好消解一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18EC")

    label("loc_120B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1280")

    #C0012
    ChrTalk(
        0xFE,
        (
            "昨天，好像从\x01",
            "唐古拉姆门那边送来了\x01",
            "那个遗迹的调查报告书。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "但司令那家伙\x01",
            "似乎根本就不想理会呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18EC")

    label("loc_1280")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1449")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C7")
    TurnDirection(0x8, 0x104, 0)

    #C0014
    ChrTalk(
        0xFE,
        "兰迪，今天到底有什么事情啊？\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x104,
        (
            "#0300F哦，你们放弃的那个\x01",
            "遗迹的调查，\x01",
            "现在由我们接手了。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        "你、你说什么……？\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x104,
        (
            "#0300F从听来的流言判断，\x01",
            "似乎是司令大人硬推给\x01",
            "唐古拉姆门那边的啊。\x02\x03",

            "#0309F哈哈，功劳就由我们领受了，\x01",
            "你活该。\x02\x03",

            "#0300F……麻烦你这样转告给司令。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        "……你自己去说吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1444")

    label("loc_13C7")


    #C0019
    ChrTalk(
        0xFE,
        (
            "不过……有你们和\x01",
            "唐古拉姆门的队员\x01",
            "一起调查的话，我也就放心了。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "拜托了，我们半途丢下的烂摊子，\x01",
            "就请你们帮忙收拾吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1444")

    Jump("loc_18EC")

    label("loc_1449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1480")

    #C0021
    ChrTalk(
        0xFE,
        (
            "但愿这种忙碌的状态\x01",
            "只到今天为止……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18EC")

    label("loc_1480")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1597")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1552")
    TurnDirection(0x8, 0x104, 0)

    #C0022
    ChrTalk(
        0xFE,
        "兰迪，在纪念庆典玩得尽兴吗？\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x104,
        "#0306F什么话，我可是也在工作呢。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "哎呀……但你们能自由地到处跑，\x01",
            "光是这一点，我就很羡慕了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "光是在这里站着，\x01",
            "其实也很辛苦呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1592")

    label("loc_1552")


    #C0026
    ChrTalk(
        0xFE,
        (
            "你们虽说也在工作，\x01",
            "但是可以到处转，真好呢。\x01",
            "好羡慕你们啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1592")

    Jump("loc_18EC")

    label("loc_1597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1618")

    #C0027
    ChrTalk(
        0xFE,
        (
            "哎呀，司令那家伙，\x01",
            "现在不知正在哪里玩乐呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "我们在纪念庆典期间也要\x01",
            "照常工作，但他却……\x01",
            "真是让人火大啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18EC")

    label("loc_1618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1742")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16E8")

    #C0029
    ChrTalk(
        0xFE,
        (
            "司令那家伙，\x01",
            "在纪念庆典期间完全不见踪影，\x01",
            "不知跑到哪里去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "还说什么『检查游客这种事，\x01",
            "交给准尉来指挥就足够了』。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "话虽如此……\x01",
            "但是好歹也要有个\x01",
            "警备队司令的样子嘛。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_173D")

    label("loc_16E8")


    #C0032
    ChrTalk(
        0xFE,
        "可恶，司令那家伙……真是让人火大。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "其实，米蕾优准尉\x01",
            "更像是这里的领导者呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_173D")

    Jump("loc_18EC")

    label("loc_1742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_17C6")

    #C0034
    ChrTalk(
        0xFE,
        (
            "在这广阔的诺克斯森林地带，\x01",
            "除了警察学校之外，还有一个拘留所。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "那里也是由我们\x01",
            "贝尔加德门的部队来负责看守的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18EC")

    label("loc_17C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1890")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_182E")

    #C0036
    ChrTalk(
        0xFE,
        "刚才有两个游击士来过。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "看上去还很年轻，\x01",
            "但似乎隐藏着相当强的实力。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_188B")

    label("loc_182E")


    #C0038
    ChrTalk(
        0xFE,
        "刚才有两个游击士来过。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "那么年轻，却隐藏着相当强的实力……\x01",
            "真是群不可小看的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_188B")

    Jump("loc_18EC")

    label("loc_1890")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_18EC")
    TurnDirection(0x8, 0x104, 0)

    #C0040
    ChrTalk(
        0xFE,
        (
            "兰迪，\x01",
            "你竟然会在这里露面，\x01",
            "真是没想到啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        "总之，你就随便转转吧。\x02",
    )

    CloseMessageWindow()

    label("loc_18EC")

    TalkEnd(0xFE)
    Return()

    # Function_12_109D end

    def Function_13_18F0(): pass

    label("Function_13_18F0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_196C")

    #C0042
    ChrTalk(
        0xFE,
        (
            "嗯，我的身手好像\x01",
            "变得生疏了很多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "为了让自己能够应对\x01",
            "各种意外事态，\x01",
            "今晚的演习一定要努力才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21A0")

    label("loc_196C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_19DE")

    #C0044
    ChrTalk(
        0xFE,
        (
            "你们似乎调查完\x01",
            "那个可怕的遗迹了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "哎呀，我很佩服你们的胆量啊。\x01",
            "我是无论如何也做不到的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21A0")

    label("loc_19DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1B73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B0A")

    #C0046
    ChrTalk(
        0xFE,
        (
            "我曾经参加过\x01",
            "玛因兹山道遗迹的调查队……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "里面除了幽灵，还有像恶魔一样\x01",
            "的东西在游荡徘徊……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "那种恐怖的景象，我从来都没有见过。\x01",
            "简直就像是做了一场噩梦。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x102,
        "#0101F………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 300)

    #C0050
    ChrTalk(
        0x101,
        (
            "#0000F艾、艾莉。\x01",
            "你的脸色很差啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x102,
        "#0112F没、没什么，我不要紧……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B6E")

    label("loc_1B0A")


    #C0052
    ChrTalk(
        0xFE,
        (
            "……那个遗迹里\x01",
            "到处都是从没见过的怪物。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "说实话，这次光是能平安撤退，\x01",
            "我就觉得很幸运了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B6E")

    Jump("loc_21A0")

    label("loc_1B73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1CAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C48")

    #C0054
    ChrTalk(
        0xFE,
        (
            "昨天的搬运车迟到了很久呢。\x01",
            "我一时冲动，就对运输公司的\x01",
            "比利发了点火……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "他平时明明是很遵守时间的，\x01",
            "这次竟然会迟到那么久，\x01",
            "是不是有什么特殊原因呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        "……我好像做得不太对啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CA8")

    label("loc_1C48")


    #C0057
    ChrTalk(
        0xFE,
        (
            "因为运输公司的比利\x01",
            "没有说明他迟到的理由，\x01",
            "我就不由得发火了……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        "……下次给他道个歉吧。\x02",
    )

    CloseMessageWindow()

    label("loc_1CA8")

    Jump("loc_21A0")

    label("loc_1CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1D26")

    #C0059
    ChrTalk(
        0xFE,
        "今天是从克洛斯贝尔市那里运来物资的日子呢。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "又正好赶上这么忙的时候，\x01",
            "等搬运车一到，就得立刻卸货。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21A0")

    label("loc_1D26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1E5E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E1E")

    #C0061
    ChrTalk(
        0xFE,
        (
            "偶尔也会有一些\x01",
            "想要从陆路步行去\x01",
            "克洛斯贝尔市的游客呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "大多都是些不知道\x01",
            "行路之艰苦的公子哥吧。\x01",
            "真是的……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x102,
        (
            "#0106F（……处理狼形魔兽事件时，\x01",
            "  我们也做了一样的事情呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x103,
        "#0200F（……听起来真刺耳啊。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E59")

    label("loc_1E1E")


    #C0065
    ChrTalk(
        0xFE,
        (
            "真是的，帝国那些富裕阶级\x01",
            "的想法太天真了，真让人头疼。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E59")

    Jump("loc_21A0")

    label("loc_1E5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1EAE")

    #C0066
    ChrTalk(
        0xFE,
        (
            "……我的疲劳还没消除呢。\x01",
            "因为昨天的游客很多，\x01",
            "所以非常忙……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21A0")

    label("loc_1EAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2094")
    TurnDirection(0x9, 0x104, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2023")

    #C0067
    ChrTalk(
        0xFE,
        (
            "兰迪……\x01",
            "下次和我较量一场如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x104,
        (
            "#0305F啊？搞什么啊。\x01",
            "我可没兴趣和男人调情。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "你还在这里的时候，我们一起参加了那么多次演习，\x01",
            "但我连一次都没有赢过你呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "结果就那么分别了，\x01",
            "总觉得你是赢够了就跑，很让人不爽呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        (
            "#0306F啊，原来还有那样的事情啊。\x02\x03",

            "#0300F……呵呵，但是现在稍微有点忙。\x01",
            "下次要是还记得的话，我就奉陪一次吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_208F")

    label("loc_2023")


    #C0072
    ChrTalk(
        0xFE,
        (
            "要是一直维持那种全败的战绩，\x01",
            "身为警备队员，实在是有损声誉啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "兰迪，和我较量的事……\x01",
            "可别忘记哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_208F")

    Jump("loc_21A0")

    label("loc_2094")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_21A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2138")

    #C0074
    ChrTalk(
        0xFE,
        "司令今天不在。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "不……\x01",
            "应该说『今天也不在』才对。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "似乎每天都为了应酬而忙得不可开交呢。\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x104,
        "#0303F（哈……还是老样子啊。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_21A0")

    label("loc_2138")


    #C0078
    ChrTalk(
        0xFE,
        (
            "司令好像每天都为了\x01",
            "应酬而忙得忘乎所以呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "要是没有米蕾优准尉的话，\x01",
            "这个部队早就溃散解体了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21A0")

    TalkEnd(0xFE)
    Return()

    # Function_13_18F0 end

    def Function_14_21A4(): pass

    label("Function_14_21A4")

    TalkBegin(0xFE)

    #C0080
    ChrTalk(
        0xFE,
        (
            "最近这段时间，市内的运送工作太多了，\x01",
            "已经好久都没来这边了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "好，我得赶快把货物\x01",
            "交给这里的队员。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_21A4 end

    def Function_15_2217(): pass

    label("Function_15_2217")

    TalkBegin(0xFE)

    #C0082
    ChrTalk(
        0xFE,
        (
            "这就是警备队正在使用的\x01",
            "装甲车吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "嗯，制造得还真是坚固呢。\x01",
            "虽然也许还比不上帝国的战车。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_2217 end

    def Function_16_2282(): pass

    label("Function_16_2282")

    TalkBegin(0xFE)

    #C0084
    ChrTalk(
        0xFE,
        (
            "都说一个女人在克洛斯贝尔\x01",
            "独自旅行很危险……\x01",
            "但我还是忍不住过来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "呵呵，听说这里至少比以前\x01",
            "安全了很多呢。\x01",
            "一定不会有事的吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_2282 end

    def Function_17_2311(): pass

    label("Function_17_2311")

    TalkBegin(0xFE)

    #C0086
    ChrTalk(
        0xFE,
        "我是从帝国那边走过来的。\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "难得来一次，不如直接\x01",
            "徒步走到克洛斯贝尔市吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "……不过这样终究还是太危险了吧。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_2311 end

    def Function_18_238F(): pass

    label("Function_18_238F")

    TalkBegin(0xFE)

    #C0089
    ChrTalk(
        0xFE,
        "他可真慢啊……\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "我干脆一个人\x01",
            "走到克洛斯贝尔市好了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_238F end

    def Function_19_23D3(): pass

    label("Function_19_23D3")

    TalkBegin(0xFE)

    #C0091
    ChrTalk(
        0xFE,
        (
            "我很喜欢铁路，\x01",
            "正在为它拍照呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "这条线路似乎是警备队专用的，\x01",
            "会驶来什么样的列车呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        "呵呵，真是太期待了。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_23D3 end

    def Function_20_2452(): pass

    label("Function_20_2452")

    TalkBegin(0xFE)

    #C0094
    ChrTalk(
        0xFE,
        "我们接下来正要去帝国那边观光呢。\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "听说那里的街景非常大气华丽哦，\x01",
            "现在就已经开始期待了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_2452 end

    def Function_21_24BA(): pass

    label("Function_21_24BA")

    TalkBegin(0xFE)

    #C0096
    ChrTalk(
        0xFE,
        (
            "老实说，要是去帝国的话，\x01",
            "还是稍微有一点不安呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "因为大家都知道，\x01",
            "帝国曾在克洛斯贝尔发动过战争啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_24BA end

    def Function_22_252D(): pass

    label("Function_22_252D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25E3")

    #C0098
    ChrTalk(
        0xFE,
        (
            "这里既有列车又有巴士，\x01",
            "真是方便得让人羡慕啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "我家门口要是也能\x01",
            "建起列车站或巴士站就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "那样的话，就算没什么正事，\x01",
            "也能随时来克洛斯贝尔玩玩呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2641")

    label("loc_25E3")


    #C0101
    ChrTalk(
        0xFE,
        (
            "我家门口要是也能\x01",
            "建起列车站或巴士站就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "那样的话，就能随时\x01",
            "来克洛斯贝尔玩了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2641")

    TalkEnd(0xFE)
    Return()

    # Function_22_252D end

    def Function_23_2645(): pass

    label("Function_23_2645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x10, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26E8")
    TalkBegin(0xFF)

    #A0103
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士停靠站。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0104
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "由于接到通知，有凶恶的魔兽出没，\x01",
            "因此暂时停止运营。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x95, 2)
    TalkEnd(0xFF)
    Jump("loc_26EB")

    label("loc_26E8")

    Call(0, 6)

    label("loc_26EB")

    Return()

    # Function_23_2645 end

    def Function_24_26EC(): pass

    label("Function_24_26EC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(16650, 400, -10470, 0)
    MoveCamera(295, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22430, 0)
    OP_0D()
    Sleep(500)
    OP_68(14930, 400, 890, 5000)
    MoveCamera(280, 18, 0, 5000)
    OP_6E(510, 5000)
    SetCameraDistance(56040, 5000)
    PlaceName2(340, 200, "c_plac18", 0x0, 4000)
    OP_6F(0x79)
    Sleep(3000)
    OP_68(50970, 1000, -460, 4700)
    MoveCamera(315, 30, 0, 4700)
    OP_6E(510, 4700)
    SetCameraDistance(26660, 4700)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AE9")
    ClearChrFlags(0x13, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_2808")
    ClearMapObjFlags(0x4, 0x4)
    OP_78(0x4, 0x13)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    Jump("loc_281F")

    label("loc_2808")

    ClearMapObjFlags(0x5, 0x4)
    OP_78(0x5, 0x13)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)

    label("loc_281F")

    OP_49()
    SetChrPos(0x13, 63820, 0, -120, 0)
    OP_D3(0x13, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_2868")
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x79, 0xB4, 0x0, 0x20)
    Jump("loc_287E")

    label("loc_2868")

    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)

    label("loc_287E")

    Sleep(2200)

    def lambda_2886():
        OP_95(0xFE, 26120, 0, -90, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2886)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_28B8")
    Sleep(1000)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    Jump("loc_28BE")

    label("loc_28B8")

    Sound(485, 0, 100, 0)

    label("loc_28BE")

    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x13, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_28E9")
    SetChrFlags(0x13, 0x80)
    SetMapObjFlags(0x4, 0x4)
    Jump("loc_2920")

    label("loc_28E9")

    SetChrPos(0x13, 40000, 0, 2500, 0)
    OP_D3(0x13, 0x0, 0x15F90, 0x0, 0x0)
    OP_71(0x5, 0x0, 0x0, 0x0, 0x0)
    OP_79(0x5)
    OP_66(0x2, 0x1)

    label("loc_2920")

    OP_68(50970, 1000, -460, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(26660, 0)
    Sleep(1)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_2A05")
    SetChrPos(0x0, 31190, 0, 26620, 265)
    SetChrPos(0x1, 31190, 0, 26620, 265)
    SetChrPos(0x2, 31190, 0, 26620, 265)
    SetChrPos(0x3, 31190, 0, 26620, 265)
    OP_68(31190, 1000, 26620, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    ClearScenarioFlags(0x7E, 0)
    Jump("loc_2AD4")

    label("loc_2A05")

    SetChrPos(0x0, 39720, 0, -990, 175)
    SetChrPos(0x1, 39720, 0, -990, 175)
    SetChrPos(0x2, 39720, 0, -990, 175)
    SetChrPos(0x3, 39720, 0, -990, 175)
    SetChrPos(0x4, 39720, 0, -990, 175)
    SetChrPos(0x5, 39720, 0, -990, 175)
    Sleep(1)
    OP_68(39720, 1000, -990, 0)
    MoveCamera(310, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    OP_6F(0x1)
    Sleep(1)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2ABF")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_2AC5")

    label("loc_2ABF")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_2AC5")

    Sleep(500)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x7E, 1)

    label("loc_2AD4")

    Call(0, 3)
    Sleep(200)
    FadeToBright(500, 0)
    OP_0D()
    Jump("loc_2C0C")

    label("loc_2AE9")

    Sleep(2500)
    SetChrPos(0x0, 54820, 0, -130, 270)
    SetChrPos(0x1, 56020, 0, -1200, 270)
    SetChrPos(0x2, 56170, 0, 1010, 270)
    SetChrPos(0x3, 57750, 0, -190, 270)
    OP_0D()

    def lambda_2B36():
        OP_95(0xFE, 50820, 0, -130, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2B36)

    def lambda_2B50():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2B50)
    Sleep(100)

    def lambda_2B64():
        OP_95(0xFE, 52020, 0, -1200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2B64)

    def lambda_2B7E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_2B7E)
    Sleep(120)

    def lambda_2B92():
        OP_95(0xFE, 52170, 0, 1010, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2B92)

    def lambda_2BAC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_2BAC)
    Sleep(90)

    def lambda_2BC0():
        OP_95(0xFE, 53750, 0, -190, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2BC0)

    def lambda_2BDA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_2BDA)
    WaitChrThread(0x0, 1)
    WaitChrThread(0x1, 1)
    WaitChrThread(0x2, 1)
    WaitChrThread(0x3, 1)
    WaitChrThread(0x0, 2)
    WaitChrThread(0x1, 2)
    WaitChrThread(0x2, 2)
    WaitChrThread(0x3, 2)
    Sleep(1000)
    Call(0, 3)

    label("loc_2C0C")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_24_26EC end

    def Function_25_2C14(): pass

    label("Function_25_2C14")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch32600.itc", 0x1E)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    SetChrPos(0x14, 19360, 0, 15000, 180)
    SetChrPos(0x101, 18260, 0, 12300, 0)
    SetChrPos(0x102, 19500, 0, 11500, 4)
    SetChrPos(0x103, 21020, 0, 12290, 319)
    SetChrPos(0x104, 19360, 0, 13260, 0)
    OP_68(7070, 1000, 14810, 0)
    MoveCamera(305, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(26990, 0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    OP_68(18760, 1000, 13910, 6000)
    MoveCamera(319, 20, 0, 6000)
    OP_6E(510, 6000)
    SetCameraDistance(17860, 6000)
    OP_6F(0x79)

    #C0105
    ChrTalk(
        0x104,
        "#5P#0300F给，这就是你找的东西。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0106
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "把『装甲车的启动钥匙』\x01",
            "交给了米蕾优准尉。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0107
    ChrTalk(
        0x14,
        (
            "#11P真没想到，竟然\x01",
            "挂在了那种地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#6P#0000F恐怕是司令\x01",
            "在屋顶唱歌时，一时忘我，\x01",
            "不慎掉落的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x14,
        (
            "#11P呼……不过，总算是万幸，\x01",
            "最后终于找到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x14,
        (
            "#11P这下终于可以把\x01",
            "装甲车转移到\x01",
            "游客看不到的地方了。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x14,
        (
            "#11P兰迪，那个……\x01",
            "我算是欠了你一个人情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x104,
        (
            "#5P#0304F没什么大不了的啦。\x02\x03",

            "#0309F算啦，如果你一定\x01",
            "要还这个人情的话……\x01",
            "就和我约会一次来销帐吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x14,
        (
            "#11P真是的……\x01",
            "一点都没变，还是像个傻瓜。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x14,
        (
            "#11P……那么，\x01",
            "真是谢谢大家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#6P#0000F嗯，要是再有什么事情的话，\x01",
            "请尽管向我们提出支援请求吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x14,
        (
            "#11P好的，一定。\x01",
            "……那么，我就先失陪了。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(19040, 1000, 12630, 4000)

    def lambda_2FBC():
        OP_95(0xFE, 23200, 0, 15000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2FBC)
    WaitChrThread(0x14, 1)

    def lambda_2FDA():
        OP_95(0xFE, 23200, 0, 3000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_2FDA)

    def lambda_2FF4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FF4)
    Sleep(100)

    def lambda_3004():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3004)
    Sleep(100)

    def lambda_3014():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3014)
    Sleep(100)

    def lambda_3024():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3024)
    Sleep(100)

    def lambda_3034():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3034)
    Sleep(100)

    def lambda_3044():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3044)
    Sleep(100)

    def lambda_3054():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3054)
    Sleep(100)

    def lambda_3064():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3064)
    WaitChrThread(0x14, 1)

    def lambda_3075():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3075)
    Sleep(100)

    def lambda_3085():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3085)
    Sleep(100)

    def lambda_3095():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3095)
    Sleep(100)

    def lambda_30A5():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_30A5)

    #C0117
    ChrTalk(
        0x104,
        (
            "#11P#0300F……好啦，工作就算是\x01",
            "告一段落了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x102,
        (
            "#6P#0106F不管怎么说……\x01",
            "能找到启动钥匙，真是太好了。\x02\x03",

            "#0108F万一被外人给捡到的话，可就……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#5P#0000F现在回想一下那个掉落的地方，\x01",
            "从某种意义上说，或许算是幸运的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x103,
        (
            "#12P#0203F……应该说恶人反而有好运吧。\x02\x03",

            "#0200F说到底，那个司令要是能尽职一点，\x01",
            "也就不会发生这样的事情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x104,
        (
            "#11P#0303F司令那家伙，一直以来\x01",
            "都只会考虑自己的事情，\x01",
            "真是个不让人省心的混蛋啊。\x02\x03",

            "#0301F如果我们找不到\x01",
            "启动钥匙的话，\x01",
            "他多半就会把责任推卸给米蕾优吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x102,
        (
            "#6P#0106F……该怎么说呢……\x01",
            "真是个无可救药的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        (
            "#5P#0003F……确实如此。\x02\x03",

            "#0000F但是……警备队中也有像\x01",
            "副司令和准尉这种可靠的人。\x02\x03",

            "希望队员们也好好努力，\x01",
            "不要因现状而气馁啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        (
            "#11P#0304F……哈哈，说得也是。\x02\x03",

            "#0300F好啦，罗伊德，\x01",
            "我们也走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        "#5P#0000F嗯，好的。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0126
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【搜寻重要遗失物】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-350, 1540, 12250, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 18260, 0, 12300, 90)
    OP_29(0x19, 0x2, 0x1F)
    OP_29(0x19, 0x1, 0xA)
    OP_29(0x19, 0x4, 0x10)
    Sleep(500)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    OP_49()
    OP_D5(0x1E)
    EventEnd(0x5)
    Return()

    # Function_25_2C14 end

    def Function_26_3477(): pass

    label("Function_26_3477")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0127
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "埃雷波尼亚帝国方向国境\x01",
            "   『贝尔加德门』\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_26_3477 end

    SaveToFile()

Try(main)
