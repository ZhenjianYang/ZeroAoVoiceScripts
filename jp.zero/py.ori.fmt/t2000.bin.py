from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "カーター隊員",           # 1
        "ロギンス隊員",           # 2
        "ビリー",                 # 3
        "観光客",                 # 4
        "観光客",                 # 5
        "観光客",                 # 6
        "観光客",                 # 7
        "観光客",                 # 8
        "観光客",                 # 9
        "観光客",                 # 10
        "観光客クルル",           # 11
        "バス",                   # 12
        "ミレイユ准尉",           # 13
        "西クロスベル街道",       # 14
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

    PlaceName(73.0, 0.0, -4.0, 0x0000, 0x0000, "西クロスベル街道")
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
        "Function_6_7B3",          # 06, 6
        "Function_7_872",          # 07, 7
        "Function_8_98E",          # 08, 8
        "Function_9_A23",          # 09, 9
        "Function_10_FD5",         # 0A, 10
        "Function_11_10C4",        # 0B, 11
        "Function_12_10D2",        # 0C, 12
        "Function_13_1A4B",        # 0D, 13
        "Function_14_23C7",        # 0E, 14
        "Function_15_2444",        # 0F, 15
        "Function_16_24C3",        # 10, 16
        "Function_17_2566",        # 11, 17
        "Function_18_25EE",        # 12, 18
        "Function_19_263A",        # 13, 19
        "Function_20_26DD",        # 14, 20
        "Function_21_2749",        # 15, 21
        "Function_22_27CA",        # 16, 22
        "Function_23_2904",        # 17, 23
        "Function_24_29B9",        # 18, 24
        "Function_25_2EE1",        # 19, 25
        "Function_26_3824",        # 1A, 26
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x113, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_762")
    Sound(14, 0, 100, 0)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x646, 1)"), scpexpr(EXPR_END)), "loc_6EB")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x113, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_75D")

    label("loc_6EB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x646),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x646),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x6, 0x1E, 0x0, 0x0, 0x0)

    label("loc_75D")

    Jump("loc_7A7")

    label("loc_762")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_7A7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_666 end

    def Function_6_7B3(): pass

    label("Function_6_7B3")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バス停がある。\x01",
            "バスで移動しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "クロスベル市西口\x01",            # 0
            "停留所（警察学校付近）\x01",      # 1
            "やめる\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_84A")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_86A")

    label("loc_84A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_86A")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1030", 0, 0, 0)
    IdleLoop()

    label("loc_86A")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_6_7B3 end

    def Function_7_872(): pass

    label("Function_7_872")

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

    def lambda_948():
        OP_95(0xFE, 27000, 0, 23850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_948)
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

    # Function_7_872 end

    def Function_8_98E(): pass

    label("Function_8_98E")

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

    # Function_8_98E end

    def Function_9_A23(): pass

    label("Function_9_A23")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)    #voice#Noel
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FCD")

    Menu(
        0,
        32,
        26,
        1,
        (
            "警備隊車両で移動をする\x01",      # 0
            "ここで休憩をする\x01",            # 1
            "やめる\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F6A")
    Sound(1500, 255, 100, 0)    #voice#Noel
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD3")
    MenuCmd(1, 1, "★クロスベル市・中央広場")
    MenuCmd(3, 1, 0x0)
    Jump("loc_AEF")

    label("loc_AD3")

    MenuCmd(1, 1, "　クロスベル市・中央広場")

    label("loc_AEF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B21")
    MenuCmd(1, 1, "★クロスベル市・東出口")
    MenuCmd(3, 1, 0x1)
    Jump("loc_B3B")

    label("loc_B21")

    MenuCmd(1, 1, "　クロスベル市・東出口")

    label("loc_B3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6D")
    MenuCmd(1, 1, "★クロスベル市・西出口")
    MenuCmd(3, 1, 0x2)
    Jump("loc_B87")

    label("loc_B6D")

    MenuCmd(1, 1, "　クロスベル市・西出口")

    label("loc_B87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB9")
    MenuCmd(1, 1, "★クロスベル市・南出口")
    MenuCmd(3, 1, 0x3)
    Jump("loc_BD3")

    label("loc_BB9")

    MenuCmd(1, 1, "　クロスベル市・南出口")

    label("loc_BD3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C05")
    MenuCmd(1, 1, "★クロスベル市・北出口")
    MenuCmd(3, 1, 0x4)
    Jump("loc_C1F")

    label("loc_C05")

    MenuCmd(1, 1, "　クロスベル市・北出口")

    label("loc_C1F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C49")
    MenuCmd(1, 1, "★タングラム門")
    MenuCmd(3, 1, 0x5)
    Jump("loc_C5B")

    label("loc_C49")

    MenuCmd(1, 1, "　タングラム門")

    label("loc_C5B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C85")
    MenuCmd(1, 1, "★ベルガード門")
    MenuCmd(3, 1, 0x6)
    Jump("loc_C97")

    label("loc_C85")

    MenuCmd(1, 1, "　ベルガード門")

    label("loc_C97")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC5")
    MenuCmd(1, 1, "★ウルスラ医科大学")
    MenuCmd(3, 1, 0x7)
    Jump("loc_CDB")

    label("loc_CC5")

    MenuCmd(1, 1, "　ウルスラ医科大学")

    label("loc_CDB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D05")
    MenuCmd(1, 1, "★アルモリカ村")
    MenuCmd(3, 1, 0x8)
    Jump("loc_D17")

    label("loc_D05")

    MenuCmd(1, 1, "　アルモリカ村")

    label("loc_D17")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D43")
    MenuCmd(1, 1, "★マインツ鉱山町")
    MenuCmd(3, 1, 0x9)
    Jump("loc_D57")

    label("loc_D43")

    MenuCmd(1, 1, "　マインツ鉱山町")

    label("loc_D57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D89")
    MenuCmd(1, 1, "★マインツ山道・隧道内")
    MenuCmd(3, 1, 0xA)
    Jump("loc_DA3")

    label("loc_D89")

    MenuCmd(1, 1, "　マインツ山道・隧道内")

    label("loc_DA3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC9")
    MenuCmd(1, 1, "★星見の塔")
    MenuCmd(3, 1, 0xB)
    Jump("loc_DD7")

    label("loc_DC9")

    MenuCmd(1, 1, "　星見の塔")

    label("loc_DD7")

    MenuCmd(1, 1, "　やめる")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F5B")
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
        (0, "loc_EAE"),
        (1, "loc_EBC"),
        (2, "loc_ECA"),
        (3, "loc_ED8"),
        (4, "loc_EE6"),
        (5, "loc_EF4"),
        (6, "loc_F02"),
        (7, "loc_F10"),
        (8, "loc_F1E"),
        (9, "loc_F2C"),
        (10, "loc_F3A"),
        (11, "loc_F48"),
        (SWITCH_DEFAULT, "loc_F56"),
    )


    label("loc_EAE")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_F56")

    label("loc_EBC")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_F56")

    label("loc_ECA")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_F56")

    label("loc_ED8")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_F56")

    label("loc_EE6")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_F56")

    label("loc_EF4")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_F56")

    label("loc_F02")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_F56")

    label("loc_F10")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_F56")

    label("loc_F1E")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_F56")

    label("loc_F2C")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_F56")

    label("loc_F3A")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_F56")

    label("loc_F48")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_F56")

    label("loc_F56")

    Jump("loc_F65")

    label("loc_F5B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F65")

    Jump("loc_FC8")

    label("loc_F6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB5")
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
    Jump("loc_FC8")

    label("loc_FB5")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_FC8")

    Jump("loc_A3D")

    label("loc_FCD")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_A23 end

    def Function_10_FD5(): pass

    label("Function_10_FD5")

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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_10A9")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_10AF")

    label("loc_10A9")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_10AF")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_FD5 end

    def Function_11_10C4(): pass

    label("Function_11_10C4")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)
    Return()

    # Function_11_10C4 end

    def Function_12_10D2(): pass

    label("Function_12_10D2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1209")

    #C0005
    ChrTalk(
        0xFE,
        (
            "このベルガード門では\x01",
            "帝国方面の国境を警備しているぞ。\x02",
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
            "あれ……？\x01",
            "あんた、もしかしてランディか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        "#0300F……よっ、久しぶりだな。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "はは……また来てくれて嬉しいぜ。\x01",
            "もうこっちには顔を出さないと\x01",
            "思ってたからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        "まぁ、ゆっくりしてってくれ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8C, 0)
    Jump("loc_1A47")

    label("loc_1209")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1288")

    #C0010
    ChrTalk(
        0xFE,
        "今晩は夜間演習が行われる予定でな。\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "日頃のうっ憤も相当溜まってる。\x01",
            "こういう機会に上手く晴らさないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A47")

    label("loc_1288")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_130D")

    #C0012
    ChrTalk(
        0xFE,
        (
            "昨日タングラム門の方から\x01",
            "例の遺跡の調査報告書が\x01",
            "届いたらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "司令のヤツは気にも\x01",
            "留めてないようだったがな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A47")

    label("loc_130D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1510")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_147E")
    TurnDirection(0x8, 0x104, 0)

    #C0014
    ChrTalk(
        0xFE,
        "ランディ、今日は一体どうしたんだ？\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x104,
        (
            "#0300Fああ、お前らが撤収した\x01",
            "遺跡の調査を\x01",
            "引き受けることになったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        "な、なんだって……？\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x104,
        (
            "#0300F話を聞いた感じだと、\x01",
            "司令閣下がタングラム門に\x01",
            "押し付けたっぽいな。\x02\x03",

            "#0309Fはは、手柄は俺たちが頂くからな。\x01",
            "ざまーみろだ。\x02\x03",

            "#0300F……って司令に言っといてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        "……自分で言え。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_150B")

    label("loc_147E")


    #C0019
    ChrTalk(
        0xFE,
        (
            "いやしかし……あんたらが\x01",
            "タングラム門の隊員と\x01",
            "一緒に調査してくれるなら心強い。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "頼むぞ、俺たちの不始末を\x01",
            "なんとかつけてやってくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_150B")

    Jump("loc_1A47")

    label("loc_1510")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1551")

    #C0021
    ChrTalk(
        0xFE,
        (
            "今日でこの忙しいのも終わる……\x01",
            "といいなぁ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A47")

    label("loc_1551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1678")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1629")
    TurnDirection(0x8, 0x104, 0)

    #C0022
    ChrTalk(
        0xFE,
        "ランディ、記念祭は堪能してるか？\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x104,
        "#0306Fこっちも仕事だっつの。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "いや……自由に歩きまわれる分\x01",
            "あんたらがうらやましいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "ただ立ってるってのも\x01",
            "なかなか辛いもんだぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1673")

    label("loc_1629")


    #C0026
    ChrTalk(
        0xFE,
        (
            "仕事とはいえ、\x01",
            "色々な場所に行けていいな。\x01",
            "あんたらがうらやましいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1673")

    Jump("loc_1A47")

    label("loc_1678")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_16FF")

    #C0027
    ChrTalk(
        0xFE,
        (
            "あぁ、今頃司令のヤツは\x01",
            "どこぞで遊んでんのかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "俺たちは記念祭中も\x01",
            "かまわず勤務だってのに……\x01",
            "ムカムカするぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A47")

    label("loc_16FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1849")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E5")

    #C0029
    ChrTalk(
        0xFE,
        (
            "司令のヤツ、\x01",
            "記念祭中はまるまるどこかへ\x01",
            "出かけてるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "『観光客の検分くらい\x01",
            "  准尉の指揮だけで充分だ』だとよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "そりゃそうだけどさ……\x01",
            "少しは警備隊司令らしいことを\x01",
            "してくれってんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1844")

    label("loc_17E5")


    #C0032
    ChrTalk(
        0xFE,
        "くそ、司令のヤツ……頭にくるぜ。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "実質、ミレイユ准尉が\x01",
            "ここのトップみたいなもんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1844")

    Jump("loc_1A47")

    label("loc_1849")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_18E3")

    #C0034
    ChrTalk(
        0xFE,
        (
            "このあたりに広がるノックス森林地帯には\x01",
            "警察学校のほかに、留置場があるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "そこの警備も俺たち\x01",
            "ベルガード門の部隊が担当してるぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A47")

    label("loc_18E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_19D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_196B")

    #C0036
    ChrTalk(
        0xFE,
        "さっき、遊撃士の連中が来たんだ。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "見たところ随分若いみたいだが、\x01",
            "かなりの実力を隠し持ってると見た。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19CE")

    label("loc_196B")


    #C0038
    ChrTalk(
        0xFE,
        "さっき、遊撃士の連中が来たんだ。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "あの若さでかなりの実力を\x01",
            "秘めている……侮れない奴らだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19CE")

    Jump("loc_1A47")

    label("loc_19D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1A47")
    TurnDirection(0x8, 0x104, 0)

    #C0040
    ChrTalk(
        0xFE,
        (
            "ランディ、\x01",
            "あんたが顔を出してくれるとは\x01",
            "思ってもみなかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        "ま、ゆっくりしてってくれ。\x02",
    )

    CloseMessageWindow()

    label("loc_1A47")

    TalkEnd(0xFE)
    Return()

    # Function_12_10D2 end

    def Function_13_1A4B(): pass

    label("Function_13_1A4B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1AE5")

    #C0042
    ChrTalk(
        0xFE,
        (
            "ううむ、すっかり体が\x01",
            "なまってしまっている気がするな。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "不意の事態に\x01",
            "対応できるようにするためにも\x01",
            "今夜の演習はがんばらないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23C3")

    label("loc_1AE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1B67")

    #C0044
    ChrTalk(
        0xFE,
        (
            "あんたら、あの恐ろしい遺跡を\x01",
            "調査したらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "いや、その度胸には感服するよ。\x01",
            "俺には到底マネできないな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23C3")

    label("loc_1B67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1D34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CB3")

    #C0046
    ChrTalk(
        0xFE,
        (
            "俺はマインツ山道の遺跡の\x01",
            "調査隊に入っていたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "中には幽霊や悪魔のようなものが\x01",
            "ウヨウヨいたんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "あんな光景は今まで見た事がない。\x01",
            "まるで悪い夢でも見ているようだった。\x02",
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
            "#0000Fエ、エリィ。\x01",
            "顔が真っ青だぞ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x102,
        "#0112Fだ、大、大丈夫ですっ……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D2F")

    label("loc_1CB3")


    #C0052
    ChrTalk(
        0xFE,
        (
            "……あの遺跡の中は\x01",
            "見た事もない化け物でいっぱいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "正直、今回ばかりは撤収できて\x01",
            "幸運だと思ってしまったくらいだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D2F")

    Jump("loc_23C3")

    label("loc_1D34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1E96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E19")

    #C0054
    ChrTalk(
        0xFE,
        (
            "昨日は運搬車が随分遅れて来てな。\x01",
            "つい運送会社のビリーに\x01",
            "憎まれ口を叩いてしまったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "いつも時間通りに来る彼が\x01",
            "あんなに遅れるんだ。\x01",
            "なにか事情があったんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        "……悪いことをしたな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E91")

    label("loc_1E19")


    #C0057
    ChrTalk(
        0xFE,
        (
            "運送会社のビリーが\x01",
            "遅れた理由を話さなかったので\x01",
            "つい憎まれ口を叩いてしまったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        "……今度一言謝っておくか。\x02",
    )

    CloseMessageWindow()

    label("loc_1E91")

    Jump("loc_23C3")

    label("loc_1E96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1F17")

    #C0059
    ChrTalk(
        0xFE,
        "今日はクロスベル市から物資が届く日だ。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "忙しいことだし、運搬車が着いたら\x01",
            "さっさと降ろしてもらわないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23C3")

    label("loc_1F17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_205D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_201F")

    #C0061
    ChrTalk(
        0xFE,
        (
            "たまに陸路を歩いて\x01",
            "クロスベル市に行こうとする\x01",
            "観光客がいてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "大方、陸路の厳しさを\x01",
            "未だに分かってないボンボンだろう。\x01",
            "まったく……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x102,
        (
            "#0106F（……狼魔獣事件の時に\x01",
            "  同じ事をしたわね……）\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x103,
        "#0200F（……耳が痛いですね。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2058")

    label("loc_201F")


    #C0065
    ChrTalk(
        0xFE,
        (
            "まったく、帝国の富裕層というのは\x01",
            "考えが甘くて困る。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2058")

    Jump("loc_23C3")

    label("loc_205D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_20B1")

    #C0066
    ChrTalk(
        0xFE,
        (
            "……まだ疲れがとれん。\x01",
            "昨日は観光客が多くて\x01",
            "忙しかったからな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23C3")

    label("loc_20B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2299")
    TurnDirection(0x9, 0x104, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2232")

    #C0067
    ChrTalk(
        0xFE,
        (
            "ランディ……\x01",
            "今度、手合わせしてくれないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x104,
        (
            "#0305Fん？　なんでだよ。\x01",
            "男とジャレあう趣味はねぇぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "お前がいた頃、演習で相対した時は\x01",
            "一度も勝てなかったからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "あのまま別れては\x01",
            "勝ち逃げされたようで気分が悪い。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x104,
        (
            "#0306Fあー、そんなこともあったっけなぁ。\x02\x03",

            "#0300F……まぁ、今はちょいと忙しいんでな。\x01",
            "今度覚えてたら付き合ってやるよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2294")

    label("loc_2232")


    #C0072
    ChrTalk(
        0xFE,
        (
            "負けたままでは\x01",
            "警備隊員としての沽券に関わる。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "ランディ、手合わせのこと……\x01",
            "忘れるなよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2294")

    Jump("loc_23C3")

    label("loc_2299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_23C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_234B")

    #C0074
    ChrTalk(
        0xFE,
        "今日は司令は不在だ。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "いや……\x01",
            "今日も、と言った方が正しいか。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "毎日毎日、接待で大忙しみたいだな。\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x104,
        "#0303F（ハッ……相変わらずかよ。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23C3")

    label("loc_234B")


    #C0078
    ChrTalk(
        0xFE,
        (
            "司令は毎日毎日、\x01",
            "接待で大忙しみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "ミレイユ准尉がいなければこんな部隊、\x01",
            "とっくに空中分解してるだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23C3")

    TalkEnd(0xFE)
    Return()

    # Function_13_1A4B end

    def Function_14_23C7(): pass

    label("Function_14_23C7")

    TalkBegin(0xFE)

    #C0080
    ChrTalk(
        0xFE,
        (
            "最近市内の配達が多かったから、\x01",
            "この辺に来るのは久しぶりだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "さて、とっとと隊員さんに\x01",
            "荷物を渡しちまうか。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_23C7 end

    def Function_15_2444(): pass

    label("Function_15_2444")

    TalkBegin(0xFE)

    #C0082
    ChrTalk(
        0xFE,
        (
            "これが警備隊で使われてる\x01",
            "装甲車か……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "ふーん、なかなか頑丈な作りをしてるね。\x01",
            "帝国の戦車には負けるだろうけど。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_15_2444 end

    def Function_16_24C3(): pass

    label("Function_16_24C3")

    TalkBegin(0xFE)

    #C0084
    ChrTalk(
        0xFE,
        (
            "クロスベルで女の一人旅は\x01",
            "危ないって言われたけど……\x01",
            "結局我慢しきれずに来ちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "ま、昔よりは大分\x01",
            "安全になってるって話だし。\x01",
            "きっと大丈夫よね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_16_24C3 end

    def Function_17_2566(): pass

    label("Function_17_2566")

    TalkBegin(0xFE)

    #C0086
    ChrTalk(
        0xFE,
        "帝国方面から歩いてきたんだ。\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "さあて、折角だからこのまま\x01",
            "クロスベル市まで徒歩で行こうかなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "……流石に危ないか。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_17_2566 end

    def Function_18_25EE(): pass

    label("Function_18_25EE")

    TalkBegin(0xFE)

    #C0089
    ChrTalk(
        0xFE,
        "彼、遅いな～。\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "一人でクロスベル市まで\x01",
            "行っちゃおうかしら。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_25EE end

    def Function_19_263A(): pass

    label("Function_19_263A")

    TalkBegin(0xFE)

    #C0091
    ChrTalk(
        0xFE,
        (
            "僕は鉄道が好きでね。\x01",
            "写真を撮らせてもらってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "この路線は警備隊専用らしいね。\x01",
            "どんな列車が来るんだろうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        "ふふ、楽しみでならないよ。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_263A end

    def Function_20_26DD(): pass

    label("Function_20_26DD")

    TalkBegin(0xFE)

    #C0094
    ChrTalk(
        0xFE,
        "今から帝国の方へ観光に行くんじゃ。\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "なかなか豪勢な町並みと聞くからのう。\x01",
            "今から楽しみじゃ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_26DD end

    def Function_21_2749(): pass

    label("Function_21_2749")

    TalkBegin(0xFE)

    #C0096
    ChrTalk(
        0xFE,
        (
            "実は帝国に行くのは\x01",
            "少しだけ不安なんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "クロスベルで紛争が起こっていた時代を\x01",
            "私たちは知っていますからねぇ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_2749 end

    def Function_22_27CA(): pass

    label("Function_22_27CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_288C")

    #C0098
    ChrTalk(
        0xFE,
        (
            "列車もバスもあるなんて、\x01",
            "便利でうらやましいなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "あたしの家の前にも\x01",
            "駅やバス停ができればいいのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "そしたら、用がなくたって\x01",
            "クロスベルに来ちゃうんだけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2900")

    label("loc_288C")


    #C0101
    ChrTalk(
        0xFE,
        (
            "あたしの家の前にも\x01",
            "駅やバス停ができればいいのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "そしたら、ちょくちょく\x01",
            "クロスベルに遊びに来られるよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2900")

    TalkEnd(0xFE)
    Return()

    # Function_22_27CA end

    def Function_23_2904(): pass

    label("Function_23_2904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x10, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_29B5")
    TalkBegin(0xFF)

    #A0103
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バスの停留所がある。\x02",
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
            "凶悪な魔獣出没中との通報を受け、\x01",
            "現在運行を見合わせております。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x95, 2)
    TalkEnd(0xFF)
    Jump("loc_29B8")

    label("loc_29B5")

    Call(0, 6)

    label("loc_29B8")

    Return()

    # Function_23_2904 end

    def Function_24_29B9(): pass

    label("Function_24_29B9")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2DB6")
    ClearChrFlags(0x13, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_2AD5")
    ClearMapObjFlags(0x4, 0x4)
    OP_78(0x4, 0x13)
    SetMapObjFrame(0x4, "light", 0x0, 0x1)
    Jump("loc_2AEC")

    label("loc_2AD5")

    ClearMapObjFlags(0x5, 0x4)
    OP_78(0x5, 0x13)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)

    label("loc_2AEC")

    OP_49()
    SetChrPos(0x13, 63820, 0, -120, 0)
    OP_D3(0x13, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_2B35")
    SetMapObjFlags(0x4, 0x1000)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x79, 0xB4, 0x0, 0x20)
    Jump("loc_2B4B")

    label("loc_2B35")

    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)

    label("loc_2B4B")

    Sleep(2200)

    def lambda_2B53():
        OP_95(0xFE, 26120, 0, -90, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2B53)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_2B85")
    Sleep(1000)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    Jump("loc_2B8B")

    label("loc_2B85")

    Sound(485, 0, 100, 0)

    label("loc_2B8B")

    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x13, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_2BB6")
    SetChrFlags(0x13, 0x80)
    SetMapObjFlags(0x4, 0x4)
    Jump("loc_2BED")

    label("loc_2BB6")

    SetChrPos(0x13, 40000, 0, 2500, 0)
    OP_D3(0x13, 0x0, 0x15F90, 0x0, 0x0)
    OP_71(0x5, 0x0, 0x0, 0x0, 0x0)
    OP_79(0x5)
    OP_66(0x2, 0x1)

    label("loc_2BED")

    OP_68(50970, 1000, -460, 0)
    MoveCamera(315, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(26660, 0)
    Sleep(1)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_2CD2")
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
    Jump("loc_2DA1")

    label("loc_2CD2")

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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2D8C")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_2D92")

    label("loc_2D8C")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_2D92")

    Sleep(500)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x7E, 1)

    label("loc_2DA1")

    Call(0, 3)
    Sleep(200)
    FadeToBright(500, 0)
    OP_0D()
    Jump("loc_2ED9")

    label("loc_2DB6")

    Sleep(2500)
    SetChrPos(0x0, 54820, 0, -130, 270)
    SetChrPos(0x1, 56020, 0, -1200, 270)
    SetChrPos(0x2, 56170, 0, 1010, 270)
    SetChrPos(0x3, 57750, 0, -190, 270)
    OP_0D()

    def lambda_2E03():
        OP_95(0xFE, 50820, 0, -130, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2E03)

    def lambda_2E1D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_2E1D)
    Sleep(100)

    def lambda_2E31():
        OP_95(0xFE, 52020, 0, -1200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2E31)

    def lambda_2E4B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_2E4B)
    Sleep(120)

    def lambda_2E5F():
        OP_95(0xFE, 52170, 0, 1010, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2E5F)

    def lambda_2E79():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x2, 2, lambda_2E79)
    Sleep(90)

    def lambda_2E8D():
        OP_95(0xFE, 53750, 0, -190, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2E8D)

    def lambda_2EA7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3, 2, lambda_2EA7)
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

    label("loc_2ED9")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_24_29B9 end

    def Function_25_2EE1(): pass

    label("Function_25_2EE1")

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
        "#5P#0300Fほらよ、探しモンだ。\x02",
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
            "ランディはミレイユ准尉に\x01",
            "『装甲車の起動キー』を渡した。\x02",
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
            "#11Pまさか、あんな場所に\x01",
            "引っかかっているなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#6P#0000Fおそらく、\x01",
            "司令が屋上で歌った拍子に\x01",
            "落としてしまったんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x14,
        (
            "#11Pはぁ……でもよかったです、\x01",
            "キーが見つかって。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x14,
        (
            "#11Pようやくこれで、装甲車を\x01",
            "観光客の目に届かない場所に\x01",
            "移動できます。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x14,
        (
            "#11Pランディ、あなたにも、その……\x01",
            "借りができてしまったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x104,
        (
            "#5P#0304Fいいってことよ。\x02\x03",

            "#0309Fま、どうしても\x01",
            "返してくれるってんなら……\x01",
            "デート１回で帳消しにしてやるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x14,
        (
            "#11Pもう……\x01",
            "バカは変わらないんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x14,
        (
            "#11P……それでは皆さん、\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#6P#0000Fええ、また何かあったら\x01",
            "要請を出してください。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x14,
        (
            "#11Pはい、是非とも。\x01",
            "……それでは、失礼します。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(19040, 1000, 12630, 4000)

    def lambda_32F1():
        OP_95(0xFE, 23200, 0, 15000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_32F1)
    WaitChrThread(0x14, 1)

    def lambda_330F():
        OP_95(0xFE, 23200, 0, 3000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_330F)

    def lambda_3329():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3329)
    Sleep(100)

    def lambda_3339():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3339)
    Sleep(100)

    def lambda_3349():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3349)
    Sleep(100)

    def lambda_3359():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3359)
    Sleep(100)

    def lambda_3369():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3369)
    Sleep(100)

    def lambda_3379():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3379)
    Sleep(100)

    def lambda_3389():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3389)
    Sleep(100)

    def lambda_3399():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3399)
    WaitChrThread(0x14, 1)

    def lambda_33AA():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_33AA)
    Sleep(100)

    def lambda_33BA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_33BA)
    Sleep(100)

    def lambda_33CA():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_33CA)
    Sleep(100)

    def lambda_33DA():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_33DA)

    #C0117
    ChrTalk(
        0x104,
        (
            "#11P#0300F……さーて、\x01",
            "これにて一件落着ってか？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x102,
        (
            "#6P#0106Fそれにしても……\x01",
            "起動キーが見つかってよかったわね。\x02\x03",

            "#0108Fもし部外者に拾われていたりしたら……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#5P#0000F落ちてた場所を考えると、\x01",
            "ある意味運がよかったのかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x103,
        (
            "#12P#0203F……悪運が強かった、の間違いでしょう。\x02\x03",

            "#0200Fそもそも司令がしっかりしていれば\x01",
            "このような事は起こらなかったワケですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x104,
        (
            "#11P#0303F司令のヤツは昔っから\x01",
            "自分の事しか考えてねぇ\x01",
            "ロクでなし野郎だからな。\x02\x03",

            "#0301F多分、起動キーが\x01",
            "見つからなかったとしても\x01",
            "ミレイユに責任をなすりつけてたろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x102,
        (
            "#6P#0106F……なんていうか……\x01",
            "本当にどうしようもない人ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        (
            "#5P#0003F……確かにな。\x02\x03",

            "#0000Fでも……副司令や准尉みたいな\x01",
            "しっかりした人も間違いなくいるんだ。\x02\x03",

            "隊員たちも、現状に腐らずに\x01",
            "頑張っていってほしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        (
            "#11P#0304F……ハハ、そうだな。\x02\x03",

            "#0300Fよっしゃロイド、\x01",
            "俺たちも行くとしようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        "#5P#0000Fああ、そうしよう。\x02",
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
            "クエスト【重要紛失物の捜索】\x07\x00",
            "を達成した！\x02",
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

    # Function_25_2EE1 end

    def Function_26_3824(): pass

    label("Function_26_3824")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0127
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレボニア帝国方面国境\x01",
            "   『ベルガード門』\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_26_3824 end

    SaveToFile()

Try(main)
