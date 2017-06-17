from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1210.bin",                # FileName
        "c1210",                    # MapName
        "c1210",                    # Location
        0x0021,                     # MapIndex
        "ed7114",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 33, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1210",                  # 0
        "曹",                     # 1
        "刘",                     # 2
        "秦",                     # 3
        "黑月成员",               # 4
        "SE控制",                 # 5
    ))

    AddCharChip((
        "chr/ch06302.itc",                   # 00
        "chr/ch31400.itc",                   # 01
        "chr/ch45000.itc",                   # 02
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   1,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   2,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-72300,  0,       1900,    500,     -72300,  1500,    1900,    0x007C, 0,  14, 0x0000)
    DeclActor(-37230,  0,       7940,    500,     -37230,  1500,    7940,    0x007C, 0,  14, 0x0000)
    DeclActor(5000,    0,       6440,    500,     5000,    1500,    6440,    0x007C, 0,  14, 0x0000)
    DeclActor(3430,    0,       70,      500,     5650,    1500,    40,      0x007E, 0,  3,  0x0000)

    ChipFrameInfo(504, 0)                                        # 0

    ScpFunction((
        "Function_0_1F8",          # 00, 0
        "Function_1_2A8",          # 01, 1
        "Function_2_3C3",          # 02, 2
        "Function_3_45A",          # 03, 3
        "Function_4_4FB",          # 04, 4
        "Function_5_59C",          # 05, 5
        "Function_6_640",          # 06, 6
        "Function_7_747",          # 07, 7
        "Function_8_C2E",          # 08, 8
        "Function_9_24A7",         # 09, 9
        "Function_10_25B4",        # 0A, 10
        "Function_11_2826",        # 0B, 11
        "Function_12_3677",        # 0C, 12
        "Function_13_46A6",        # 0D, 13
        "Function_14_46B9",        # 0E, 14
    ))


    def Function_0_1F8(): pass

    label("Function_0_1F8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_230"),
        (1, "loc_23C"),
        (2, "loc_248"),
        (3, "loc_254"),
        (4, "loc_260"),
        (5, "loc_26C"),
        (6, "loc_278"),
        (SWITCH_DEFAULT, "loc_284"),
    )


    label("loc_230")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_23C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_248")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_254")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_260")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_26C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_278")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_284")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_290")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_290")

    label("loc_2A7")

    Return()

    # Function_0_1F8 end

    def Function_1_2A8(): pass

    label("Function_1_2A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2ED")
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 5600, 50, 0, 270)

    label("loc_2ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_301")
    ClearScenarioFlags(0x22, 0)
    Event(0, 7)
    Jump("loc_310")

    label("loc_301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_310")
    ClearScenarioFlags(0x22, 1)
    Event(0, 12)

    label("loc_310")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33F")
    Event(0, 8)

    label("loc_33F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_385")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 5800, 0, 1300, 270)
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0xA, 0x40)

    label("loc_385")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C2")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 5800, 0, -1460, 270)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0x9, 0x40)

    label("loc_3C2")

    Return()

    # Function_1_2A8 end

    def Function_2_3C3(): pass

    label("Function_2_3C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_3D8")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_3D8")

    SetMapObjFrame(0xFF, "c122_tesri02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tama00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tama01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kuro01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato", 0x0, 0x1)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x4, 0x2)
    ClearMapObjFlags(0x5, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_459")
    OP_66(0x3, 0x1)

    label("loc_459")

    Return()

    # Function_2_3C3 end

    def Function_3_45A(): pass

    label("Function_3_45A")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48A")
    Call(0, 9)
    Jump("loc_4F7")

    label("loc_48A")


    #C0001
    ChrTalk(
        0x8,
        (
            "#03200F话说回来，\x01",
            "各位此时来访，\x01",
            "对我们而言实在是意想不到的幸运。\x02\x03",

            "#03204F那么，秦少爷\x01",
            "就托付给你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F7")

    TalkEnd(0x8)
    Return()

    # Function_3_45A end

    def Function_4_4FB(): pass

    label("Function_4_4FB")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52B")
    Call(0, 9)
    Jump("loc_598")

    label("loc_52B")


    #C0002
    ChrTalk(
        0x8,
        (
            "#03200F话说回来，\x01",
            "各位此时来访，\x01",
            "对我们而言实在是意想不到的幸运。\x02\x03",

            "#03204F那么，秦少爷\x01",
            "就托付给你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_598")

    TalkEnd(0x8)
    Return()

    # Function_4_4FB end

    def Function_5_59C(): pass

    label("Function_5_59C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_621")

    #C0003
    ChrTalk(
        0x9,
        (
            "如果有空接受委托了，\x01",
            "还请尽早回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x9,
        (
            "秦少爷自不必说，\x01",
            "我们的时间也是很有限的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63C")

    label("loc_621")


    #C0005
    ChrTalk(
        0x9,
        (
            "秦少爷，\x01",
            "请一路小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63C")

    TalkEnd(0xFE)
    Return()

    # Function_5_59C end

    def Function_6_640(): pass

    label("Function_6_640")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_743")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6E7")

    #C0006
    ChrTalk(
        0xA,
        (
            "大姐姐，\x01",
            "我会在这里等你的。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xA,
        "你一定要回来啊！\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#00100F那个，虽然无法向你保证……\x01",
            "但我一定会尽力的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_743")

    label("loc_6E7")


    #C0009
    ChrTalk(
        0xA,
        (
            "我可不管你们有事没事，\x01",
            "赶快把那些都解决掉，然后回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xA,
        (
            "你们并没有选择\x01",
            "拒绝的权利！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_743")

    TalkEnd(0xFE)
    Return()

    # Function_6_640 end

    def Function_7_747(): pass

    label("Function_7_747")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06300.itc", 0x1E)
    LoadChrToIndex("chr/ch31400.itc", 0x1F)
    LoadChrToIndex("chr/ch31500.itc", 0x20)
    LoadChrToIndex("apl/ch50237.itc", 0x21)
    SoundLoad(128)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 7200, 0, 0, 90)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 6000, 0, 1500, 135)
    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -6000, 0, 0, 90)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    OP_68(9200, 1100, 0, 0)
    MoveCamera(47, 15, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20000, 0)
    SetMapObjFrame(0xFF, "hikari_add", 0x0, 0x1)
    Sound(128, 2, 50, 0)
    OP_68(7200, 1100, 0, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0011
    ChrTalk(
        0x8,
        (
            "#03204F哎呀呀，真是个有趣的偶然。\x02\x03",

            "#03210F『黑之竞拍会』时也是一样，\x01",
            "他们确实很有缘呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x9,
        "#5P不过，曹先生……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x9,
        (
            "#5P艾鲁姆湖的南岸\x01",
            "究竟发生了什么事？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "#03204F这个嘛，现在也只能\x01",
            "赌一赌『他』的直觉了。\x02\x03",

            "#03200F不良团伙首领的魔人化，\x01",
            "还有『蛇』和『教会』的介入……\x02\x03",

            "我们现在最重要的事情就是\x01",
            "尽可能地消除一切盲点。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x9,
        "#5P……的确。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0xB, 0x80)
    Sound(886, 0, 50, 0)
    Sleep(150)
    Sound(886, 0, 40, 0)
    Sleep(150)
    Sound(886, 0, 40, 0)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #N0016
    NpcTalk(
        0xB,
        "男人的声音",
        "打、打搅了！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(250)
    OP_68(-3000, 700, 0, 0)
    MoveCamera(40, 27, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(17500, 0)
    OP_68(4900, 1100, 0, 2000)
    MoveCamera(40, 19, 0, 2000)
    SetCameraDistance(19500, 2000)
    Sound(103, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_A9C():
        OP_96(0xFE, 0x8FC, 0x0, 0x0, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_A9C)

    def lambda_AB6():

        label("loc_AB6")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_AB6")

    QueueWorkItem2(0x8, 2, lambda_AB6)
    Sleep(50)

    def lambda_ACB():

        label("loc_ACB")

        TurnDirection(0xFE, 0xB, 500)
        Yield()
        Jump("loc_ACB")

    QueueWorkItem2(0x9, 2, lambda_ACB)

    def lambda_ADD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_ADD)
    WaitChrThread(0xB, 1)
    EndChrThread(0x8, 0x2)
    EndChrThread(0x9, 0x2)
    OP_6F(0x79)

    #C0017
    ChrTalk(
        0x9,
        (
            "#11P怎么了？方！\x01",
            "为何如此惊慌失措！？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xB,
        "#6P对、对不起。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xB,
        (
            "#6P那个……监视班刚刚发来了\x01",
            "令人难以置信的报告。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x9,
        "#11P难以置信的报告……？\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        "#03205F…………………………………\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    Sleep(130)
    SetChrSubChip(0x8, 0x1)
    Sleep(130)
    SetChrSubChip(0x8, 0x2)
    Sleep(130)
    Sound(318, 0, 100, 0)
    SetChrSubChip(0x8, 0x3)
    Sleep(800)

    #C0022
    ChrTalk(
        0x8,
        (
            "#03201F方，\x01",
            "把详细情况告诉我。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 2000)
    StopSound(128, 2000, 40)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("e4500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_747 end

    def Function_8_C2E(): pass

    label("Function_8_C2E")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    AddParty(0xA1, 0xFF, 0xFF)
    SetChrFlags(0x1A2, 0x80)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 5800, 0, -1460, 270)
    OP_4B(0x9, 0xFF)
    OP_68(3470, 1000, -250, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 2300, 0, 470, 90)
    SetChrPos(0x102, 2130, 0, -650, 90)
    SetChrPos(0x104, 1020, 0, 1050, 90)
    SetChrPos(0x109, 810, 0, -120, 90)
    SetChrPos(0x105, 1030, 0, -1210, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x8, 0x0)
    SetCameraDistance(21120, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0023
    ChrTalk(
        0x8,
        (
            "#11P#03200F呀，你们来了啊。\x02\x03",

            "#03209F欢迎各位来到\x01",
            "『黑月贸易公司』。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#6P#00001F……打扰了。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        (
            "#6P#00103F我们按照您的吩咐\x01",
            "上来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "#11P#03200F呵呵……\x01",
            "兰迪先生，真是好久没见了。\x02\x03",

            "#03204F我一直在盼望你回来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#6P#00303F……那可真是谢谢了，\x01",
            "你好像还是老样子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "#11P#03204F哈哈，我就把这句话\x01",
            "当作夸奖好了。\x02\x03",

            "#03209F说起来～真没想到兰迪先生\x01",
            "竟与深红商会有所牵连。\x02\x03",

            "连我都吃了一惊呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x104,
        "#6P#00301F哼……\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#6P#00001F看来您对『他们』\x01",
            "有一定程度的了解吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "#11P#03204F嗯，其实我们\x01",
            "曾有过一些往来呢。\x02\x03",

            "#03200F兰迪先生或许也\x01",
            "了解一二吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        (
            "#6P#00303F嗯……在一年前左右，\x01",
            "叔叔他们曾潜入东方人街，\x01",
            "当时好像与『黑月』交战过吧？\x02\x03",

            "#00301F而且听说是\x01",
            "相当惨烈的恶战。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_101D")

    #C0033
    ChrTalk(
        0x101,
        "#6P#00003F……是啊。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        (
            "#6P#00108F达德利警官\x01",
            "也提起过这件事情……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1068")

    label("loc_101D")


    #C0035
    ChrTalk(
        0x102,
        "#6P#00105F说起来……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#6P#00003F达德利警官\x01",
            "也提起过这件事情呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1068")


    #C0037
    ChrTalk(
        0x8,
        (
            "#11P#03204F呵呵，反正当时\x01",
            "确实闹得很凶。\x02\x03",

            "#03200F所幸最后以平手收场，\x01",
            "彼此之间没有留下什么宿怨……\x02\x03",

            "#03209F不过有几位黑月长老\x01",
            "直到现在都无法释怀，\x01",
            "光是听到他们的名字都会气到快晕过去。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0038
    ChrTalk(
        0x109,
        "#6P#10106F那、那么严重……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x105,
        (
            "#6P#10302F呵呵，想必发生过\x01",
            "不少事情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "#11P#03203F关于鲁巴彻的旧址，\x01",
            "虽然很遗憾，但我们也只能放弃了。\x02\x03",

            "#03200F与鲁巴彻那种黑手党组织不同，\x01",
            "在商业活动中，『深红商会』与我们\x01",
            "应该不会有什么直接竞争……\x02\x03",

            "#03210F所以，关于这方面的问题，\x01",
            "你们大可以安心哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#6P#00003F……那真是十分感谢。\x01",
            "（完全无法相信啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        (
            "#6P#00105F那么，您刚才所说的那件\x01",
            "『要委托我们的事情』是……？\x02\x03",

            "#00103F本以为肯定和\x01",
            "深红商会有关呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        "嗯，其实──\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 5080, 0, 7720, 180)
    OP_A7(0x1A2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    Sound(121, 0, 100, 0)
    OP_71(0x3, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x3)
    Sleep(500)

    #N0044
    NpcTalk(
        0x1A2,
        "男孩的声音",
        (
            "#5P#N好慢啊，曹！\x01",
            "你到底在干什么！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x8, 0x2)

    def lambda_147B():

        label("loc_147B")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_147B")

    QueueWorkItem2(0x101, 1, lambda_147B)
    Sleep(50)

    def lambda_1490():

        label("loc_1490")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_1490")

    QueueWorkItem2(0x102, 1, lambda_1490)
    Sleep(50)

    def lambda_14A5():

        label("loc_14A5")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_14A5")

    QueueWorkItem2(0x104, 1, lambda_14A5)
    Sleep(50)

    def lambda_14BA():

        label("loc_14BA")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_14BA")

    QueueWorkItem2(0x109, 1, lambda_14BA)
    Sleep(50)

    def lambda_14CF():

        label("loc_14CF")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_14CF")

    QueueWorkItem2(0x105, 1, lambda_14CF)
    Sleep(50)

    def lambda_14E4():

        label("loc_14E4")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_14E4")

    QueueWorkItem2(0x9, 1, lambda_14E4)
    Sleep(300)
    OP_68(4460, 1100, 100, 3000)

    def lambda_150A():
        OP_95(0xFE, 5800, 0, 1300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_150A)
    Sleep(100)

    def lambda_1527():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_1527)
    WaitChrThread(0x1A2, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x9, 0x1)
    OP_6F(0x1)

    #C0045
    ChrTalk(
        0x8,
        "#11P#03200F哦哦，秦少爷。\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x9,
        "您有什么吩咐吗？\x02",
    )

    CloseMessageWindow()

    #N0047
    NpcTalk(
        0x1A2,
        "男孩",
        (
            "什么吩咐不吩咐！\x01",
            "你究竟要让我等多久啊！？\x02",
        )
    )

    CloseMessageWindow()

    #N0048
    NpcTalk(
        0x1A2,
        "男孩",
        (
            "什么时候才能\x01",
            "给我找到向导！？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        (
            "如果您愿意，我们随时\x01",
            "都可以随您一起──\x02",
        )
    )

    CloseMessageWindow()

    #N0050
    NpcTalk(
        0x1A2,
        "男孩",
        "不行！同样的话，不要让我重复很多次！\x02",
    )

    CloseMessageWindow()

    #N0051
    NpcTalk(
        0x1A2,
        "男孩",
        (
            "难得来克洛斯贝尔玩一趟，\x01",
            "要是让你们陪游，岂不是让人完全没有兴致了吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "#11P#03209F呵呵，已经遵照您的吩咐，\x01",
            "安排了合适的向导人员。\x02\x03",

            "#03204F那就是『他们』。\x02",
        )
    )

    CloseMessageWindow()

    #N0053
    NpcTalk(
        0x1A2,
        "男孩",
        "什么……？\x02",
    )

    CloseMessageWindow()
    OP_68(3470, 1000, -250, 1500)
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_1797():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1797)
    Sleep(50)

    def lambda_17A7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_17A7)
    Sleep(50)

    def lambda_17B7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_17B7)
    Sleep(50)

    def lambda_17C7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_17C7)
    Sleep(50)

    def lambda_17D7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_17D7)
    Sleep(300)

    #C0054
    ChrTalk(
        0x101,
        "#6P#00005F那、那个，曹先生……？\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x109,
        (
            "#6P#10105F莫非您要委托\x01",
            "我们的事情就是……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(50)
    OP_93(0x9, 0x10E, 0x1F4)
    Sleep(300)

    #C0056
    ChrTalk(
        0x8,
        (
            "#11P#03200F呵呵，我先来介绍一下。\x02\x03",

            "#03204F这位是秦少爷，\x01",
            "『黑月』某位长老\x01",
            "的孙子。\x02\x03",

            "#03209F希望你们能带领秦少爷，\x01",
            "在克洛斯贝尔市内游览一圈。\x01",
            "请务必帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        "#6P#00106F果、果然如此……\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x104,
        "#6P#00306F喂喂，你是认真的吗？\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x105,
        "#6P#10300F呵呵，真是一件意想不到的委托啊。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x1A2,
        (
            "#11P这些人就是向导吗～？\x01",
            "只不过是一群普通年轻人而已嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x1A2,
        (
            "#11P难道就不能叫伊莉娅·普拉提耶\x01",
            "或迪塔·库罗伊斯\x01",
            "之类的人过来吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x8, 0x2)

    #C0062
    ChrTalk(
        0x8,
        (
            "#11P#03209F哈哈，那终究是\x01",
            "太困难了……\x02\x03",

            "#03200F这几位在克洛斯贝尔\x01",
            "也是相当有名的名人哦。\x02\x03",

            "#03204F他们可是解决了之前\x01",
            "那起事件的最大功臣呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0063
    ChrTalk(
        0x1A2,
        "#11P嘿，原来如此。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x1A2,
        (
            "#11P你们就是解决了教团事件\x01",
            "的『特别任务支援科』吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x8, 0x0)

    def lambda_1BE5():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BE5)
    Sleep(50)

    def lambda_1BF5():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1BF5)
    Sleep(50)

    def lambda_1C05():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1C05)
    Sleep(50)

    def lambda_1C15():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1C15)
    Sleep(50)

    def lambda_1C25():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1C25)
    Sleep(300)

    #C0065
    ChrTalk(
        0x101,
        "#6P#00005F哎……！？\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        "#6P#00105F你、你为何会……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "秦少爷身为长老的孙子，\x01",
            "是个相当厉害的情报通。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "他在来到克洛斯贝尔之前，\x01",
            "就已经学习过很多相关知识了。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x1A2,
        "#11P哼哼，这是自然。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x1A2,
        (
            "#11P我可是长老的孙子，\x01",
            "肩负着整个『黑月』\x01",
            "未来的男子汉。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x1A2,
        (
            "#11P对自己的要求自然不能\x01",
            "像你们这种凡夫俗子一样低。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x104,
        "#6P#00306F（这臭小鬼……）\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x109,
        "#6P#10102F（算啦算啦，兰迪前辈。）\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x1A2,
        (
            "#11P也罢，如果你们无论如何也想当\x01",
            "我的向导，倒也不是完全不行……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x1A2,
        (
            "#11P就把教团事件那时的\x01",
            "事情说给我听——\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    #C0076
    ChrTalk(
        0x1A2,
        "#11P哎……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0077
    ChrTalk(
        0x101,
        "#6P#00005F？？？\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x102,
        "#6P#00105F怎、怎么了？\x02",
    )

    CloseMessageWindow()

    def lambda_1F10():

        label("loc_1F10")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_1F10")

    QueueWorkItem2(0x101, 1, lambda_1F10)
    Sleep(50)

    def lambda_1F25():

        label("loc_1F25")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_1F25")

    QueueWorkItem2(0x102, 1, lambda_1F25)
    Sleep(50)

    def lambda_1F3A():

        label("loc_1F3A")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_1F3A")

    QueueWorkItem2(0x104, 1, lambda_1F3A)
    Sleep(50)

    def lambda_1F4F():

        label("loc_1F4F")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_1F4F")

    QueueWorkItem2(0x109, 1, lambda_1F4F)
    Sleep(50)

    def lambda_1F64():

        label("loc_1F64")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_1F64")

    QueueWorkItem2(0x105, 1, lambda_1F64)
    OP_95(0x1A2, 4900, 0, 2510, 2000, 0x0)
    TurnDirection(0x1A2, 0x102, 500)
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0079
    ChrTalk(
        0x1A2,
        "#11P命、#800W命、#800W命……\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    #C0080
    ChrTalk(
        0x1A2,
        "#11P#5S命运中的女性啊……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x101, 0x1)
    OP_68(3060, 1100, -70, 2000)
    MoveCamera(52, 19, 0, 2000)
    OP_6E(380, 2000)
    SetCameraDistance(22270, 2000)
    OP_95(0x1A2, 2800, 0, 2150, 4000, 0x0)

    def lambda_2049():
        OP_95(0xFE, 2300, 0, 470, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_2049)
    OP_93(0x101, 0x5A, 0x0)
    OP_93(0x104, 0x5A, 0x0)
    OP_93(0x109, 0x5A, 0x0)

    def lambda_2078():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2078)

    def lambda_208D():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_208D)

    def lambda_20A2():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_20A2)

    def lambda_20B7():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_20B7)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    TurnDirection(0x101, 0x1A2, 500)

    #C0081
    ChrTalk(
        0x101,
        "#6P#00011F哇哇……！？\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x102,
        "#12P#00105F呀……\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x1A2,
        (
            "这美妙的目光！\x01",
            "光泽柔顺的银灰色长发！\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x1A2,
        (
            "还有那充满包容感觉\x01",
            "的完美身材！\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x1A2,
        (
            "竟、竟然在这种地方\x01",
            "遇到了我理想中的女性！\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x1A2,
        (
            "大姐姐！\x01",
            "你的名字是什么！？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x102,
        (
            "#12P#00100F那个……\x01",
            "艾莉，艾莉·麦克道尔。\x02\x03",

            "#00109F呵呵，请多关照哦，秦少爷。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x1A2,
        (
            "艾莉姐姐……\x01",
            "……连名字都这么动听……！\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x1A2,
        (
            "原来如此，我就是为了与你相遇，\x01",
            "才会来到克洛斯贝尔……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0090
    ChrTalk(
        0x101,
        "#6P#00005F（这……该说什么才好呢……）\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x104,
        (
            "#6P#00306F（真是的，不但狂妄自大，\x01",
            "  而且还是个相当早熟的小鬼啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x109,
        (
            "#6P#10109F（啊哈哈……\x01",
            "  艾莉小姐很有异性缘呢。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x8, 500)
    Sleep(300)

    #C0093
    ChrTalk(
        0x1A2,
        "#6P曹！我很满意！\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x1A2,
        (
            "#6P赶快让这位大姐姐\x01",
            "带我出去游览吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "#11P#03204F呵呵，那真是再好不过。\x02\x03",

            "#03209F那么，各位，\x01",
            "秦少爷就托付给你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        (
            "#6P#00011F请、请等一下！\x02\x03",

            "#00003F（给黑月长老的孙子做向导……\x01",
            "  要不要接受呢？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x73, 0x4, 0x2)
    Call(0, 10)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_8_C2E end

    def Function_9_24A7(): pass

    label("Function_9_24A7")

    EventBegin(0x0)
    Fade(500)
    AddParty(0xA1, 0xFF, 0xFF)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0xA, 0x80)
    OP_68(3470, 1000, -250, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x1A2, 5800, 0, 1300, 270)
    SetChrPos(0x101, 2300, 0, 470, 90)
    SetChrPos(0x102, 2130, 0, -650, 90)
    SetChrPos(0x104, 1020, 0, 1050, 90)
    SetChrPos(0x109, 810, 0, -120, 90)
    SetChrPos(0x105, 1030, 0, -1210, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x8, 0x0)
    OP_0D()

    #C0097
    ChrTalk(
        0x8,
        (
            "#11P#03200F怎么了？罗伊德警官。\x02\x03",

            "可以带秦少爷\x01",
            "游览克洛斯贝尔吗？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 10)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_9_24A7 end

    def Function_10_25B4(): pass

    label("Function_10_25B4")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "接受委托\x01",        # 0
            "再考虑一下\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2618"),
        (1, "loc_2620"),
        (SWITCH_DEFAULT, "loc_27D0"),
    )


    label("loc_2618")

    Call(0, 11)
    Jump("loc_27D0")

    label("loc_2620")


    #C0098
    ChrTalk(
        0x101,
        (
            "#6P#00003F对不起，\x01",
            "我们现在还腾不出时间……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    #C0099
    ChrTalk(
        0x1A2,
        (
            "#11P什、什么……？\x01",
            "竟然拒绝给我做向导吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        (
            "#12P#00106F抱歉哦，秦少爷，\x01",
            "我们必须先把工作完成。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        (
            "#6P#00000F那个……稍后再来\x01",
            "接受委托可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "#11P#03204F嗯，当然没问题。\x02\x03",

            "#03200F不过秦少爷的耐性\x01",
            "是很有限的，等不了太久。\x02\x03",

            "还请各位尽快回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x1A2,
        "#11P我会等你的，早点回来吧！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    RemoveParty(0xA1, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 5800, 0, 1300, 270)
    BeginChrThread(0xA, 0, 0, 0)
    ClearChrFlags(0xA, 0x40)
    SetScenarioFlags(0x154, 6)
    Jump("loc_27D0")

    label("loc_27D0")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 900, 0, 50, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_71(0x3, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x3)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 5800, 0, -1460, 270)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0x9, 0x40)
    EventEnd(0x5)
    Return()

    # Function_10_25B4 end

    def Function_11_2826(): pass

    label("Function_11_2826")


    #C0104
    ChrTalk(
        0x101,
        (
            "#6P#00003F……明白了，\x01",
            "我们接受委托。\x02\x03",

            "#00000F至于在市里的\x01",
            "具体游览路线……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 6)), scpexpr(EXPR_END)), "loc_2A61")

    #C0105
    ChrTalk(
        0x8,
        (
            "#11P#03200F哦，这些事情就请\x01",
            "直接询问秦少爷吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)

    #C0106
    ChrTalk(
        0x8,
        (
            "#11P#03209F那么，秦少爷，\x01",
            "请一路小心。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x8, 500)
    Sleep(300)

    #C0107
    ChrTalk(
        0x1A2,
        "#6P嗯，我知道！\x02",
    )

    CloseMessageWindow()

    def lambda_2908():

        label("loc_2908")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2908")

    QueueWorkItem2(0x101, 1, lambda_2908)
    Sleep(50)

    def lambda_291D():

        label("loc_291D")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_291D")

    QueueWorkItem2(0x102, 1, lambda_291D)
    Sleep(50)

    def lambda_2932():

        label("loc_2932")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2932")

    QueueWorkItem2(0x104, 1, lambda_2932)
    Sleep(50)

    def lambda_2947():

        label("loc_2947")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2947")

    QueueWorkItem2(0x109, 1, lambda_2947)
    Sleep(50)

    def lambda_295C():

        label("loc_295C")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_295C")

    QueueWorkItem2(0x105, 1, lambda_295C)
    OP_95(0x1A2, 4900, 0, 2510, 2000, 0x0)
    OP_68(3060, 1100, -70, 2000)
    MoveCamera(52, 19, 0, 2000)
    OP_6E(380, 2000)
    SetCameraDistance(22270, 2000)
    SetChrSubChip(0x8, 0x0)
    OP_95(0x1A2, 2800, 0, 2150, 2000, 0x0)

    def lambda_29C8():
        OP_95(0xFE, 2300, 0, 470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_29C8)
    OP_93(0x101, 0x5A, 0x0)
    OP_93(0x104, 0x5A, 0x0)
    OP_93(0x109, 0x5A, 0x0)

    def lambda_29F7():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29F7)

    def lambda_2A0C():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2A0C)

    def lambda_2A21():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2A21)

    def lambda_2A36():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2A36)
    WaitChrThread(0x101, 1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    OP_6F(0x79)
    Jump("loc_2ACE")

    label("loc_2A61")


    #C0108
    ChrTalk(
        0x8,
        (
            "#11P#03200F哦，这些事情就请\x01",
            "直接询问秦少爷吧。\x02\x03",

            "#03209F那么，秦少爷，\x01",
            "请一路小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x1A2,
        "#6P嗯，我知道！\x02",
    )

    CloseMessageWindow()

    label("loc_2ACE")

    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    #C0110
    ChrTalk(
        0x1A2,
        (
            "#5P好啦，大姐姐，\x01",
            "我们赶快出发吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B05():
        OP_95(0xFE, 1310, 0, -400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_2B05)

    def lambda_2B1F():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B1F)

    def lambda_2B2C():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2B2C)

    def lambda_2B39():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2B39)
    WaitChrThread(0x109, 1)

    def lambda_2B4A():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B4A)

    def lambda_2B5F():
        OP_9B(0x1, 0xFE, 0xB4, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2B5F)

    def lambda_2B74():
        OP_9B(0x1, 0xFE, 0xB4, 0x320, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2B74)
    OP_68(930, 1100, -390, 1500)
    WaitChrThread(0x109, 1)

    def lambda_2B9E():

        label("loc_2B9E")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2B9E")

    QueueWorkItem2(0x101, 1, lambda_2B9E)
    Sleep(50)

    def lambda_2BB3():

        label("loc_2BB3")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2BB3")

    QueueWorkItem2(0x104, 1, lambda_2BB3)
    Sleep(50)

    def lambda_2BC8():

        label("loc_2BC8")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2BC8")

    QueueWorkItem2(0x109, 1, lambda_2BC8)
    Sleep(50)

    def lambda_2BDD():

        label("loc_2BDD")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_2BDD")

    QueueWorkItem2(0x105, 1, lambda_2BDD)

    def lambda_2BEF():
        OP_97(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_2BEF)

    def lambda_2C09():
        OP_97(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2C09)
    WaitChrThread(0x102, 1)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    OP_6F(0x1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0111
    ChrTalk(
        0x102,
        "#11P#00105F等、等一下，秦少爷……？\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#5P#00005F那个……难道你想\x01",
            "两个人在市里游览吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    #C0113
    ChrTalk(
        0x1A2,
        (
            "#12P哎～？因为一大群人\x01",
            "一起行动很烦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x1A2,
        (
            "#12P所以让我和大姐姐\x01",
            "独处就好啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#5P#00001F唔……就算你这么说……\x02\x03",

            "#00003F（虽说是长老的孙子，但应该\x01",
            "  还不至于被人盯上吧，不过……）\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        (
            "#11P#00103F……咳咳。\x02\x03",

            "#00100F秦少爷，如今临近通商会议，\x01",
            "任何情况都有可能发生。\x02\x03",

            "#00104F为了你的安全而考虑，\x01",
            "最好还是有护卫人员陪同哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    #C0117
    ChrTalk(
        0x1A2,
        (
            "#6P唔～既然大姐姐都这么说了，\x01",
            "那也没办法。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    #C0118
    ChrTalk(
        0x1A2,
        (
            "#12P好，那就再加上两人吧，\x01",
            "你们要保护好我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x1A2,
        (
            "#12P至于剩下的两人……\x01",
            "就在不即不离的距离下\x01",
            "保护我们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x1A2,
        "#12P这样如何？\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        "#5P#00005F哎……\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x104,
        "#5P#00303F……安排得相当合理呢。\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x109,
        (
            "#5P#10100F嗯，如果要给重要人士安排警卫，\x01",
            "这种人员配置非常合适。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x105,
        "#11P#10300F呵呵，那就这么决定了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(300)

    #C0125
    ChrTalk(
        0x105,
        (
            "#11P#10300F由你来担任近距离护卫之一吧，\x01",
            "另外一人要选择谁呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        "#5P#00003F这个嘛……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【邀请兰迪同行】\x01",        # 0
            "【邀请诺艾尔同行】\x01",      # 1
            "【邀请瓦吉同行】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_30E3"),
        (1, "loc_320F"),
        (2, "loc_3347"),
        (SWITCH_DEFAULT, "loc_347C"),
    )


    label("loc_30E3")

    SetScenarioFlags(0x1C4, 6)
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0127
    ChrTalk(
        0x101,
        (
            "#11P#00000F兰迪，\x01",
            "可以一起吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0128
    ChrTalk(
        0x104,
        (
            "#6P#00300F嗯，知道了。\x02\x03",

            "#00304F那我们就拿出些干劲，\x01",
            "开始执行向导＆护卫任务吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    #C0129
    ChrTalk(
        0x101,
        (
            "#11P#00000F另外两人就依照他刚才所说的，\x01",
            "在后方跟随我们，\x01",
            "并随时观察情况。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    #C0130
    ChrTalk(
        0x109,
        "#6P#10100F知道了。\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x105,
        "#12P#10300F呵呵，明白。\x02",
    )

    CloseMessageWindow()
    Jump("loc_347C")

    label("loc_320F")

    SetScenarioFlags(0x1C4, 7)
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    #C0132
    ChrTalk(
        0x101,
        (
            "#11P#00000F诺艾尔，\x01",
            "可以一起吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    #C0133
    ChrTalk(
        0x109,
        (
            "#6P#10100F嗯，明白了。\x02\x03",

            "#10101F虽说是观光游览，但我们不能松懈，\x01",
            "一起认真完成护卫任务吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        (
            "#11P#00000F另外两人就依照他刚才所说的，\x01",
            "在后方跟随我们，\x01",
            "并随时观察情况。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(300)

    #C0135
    ChrTalk(
        0x104,
        "#6P#00300F嗯，包在我身上吧。\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x105,
        "#12P#10300F呵呵，明白。\x02",
    )

    CloseMessageWindow()
    Jump("loc_347C")

    label("loc_3347")

    SetScenarioFlags(0x1C5, 0)
    TurnDirection(0x101, 0x105, 500)
    Sleep(300)

    #C0137
    ChrTalk(
        0x101,
        (
            "#5P#00000F瓦吉，\x01",
            "可以一起吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x105,
        (
            "#12P#10304F呵呵，明白。\x02\x03",

            "#10302F既然如此，\x01",
            "我们就陪同他一起尽情游览吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(300)

    #C0139
    ChrTalk(
        0x101,
        (
            "#11P#00000F另外两人就依照他刚才所说的，\x01",
            "在后方跟随我们，\x01",
            "并随时观察情况。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3422():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3422)
    Sleep(50)

    def lambda_3432():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3432)
    Sleep(300)

    #C0140
    ChrTalk(
        0x104,
        "#6P#00300F嗯，包在我身上吧。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x109,
        "#6P#10100F知道了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_347C")

    label("loc_347C")

    TurnDirection(0x101, 0x1A2, 500)
    Sleep(300)

    #C0142
    ChrTalk(
        0x101,
        (
            "#5P#00000F……好啦，\x01",
            "这样可以吗？秦少爷。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_34BA():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_34BA)
    Sleep(50)

    def lambda_34CA():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_34CA)
    Sleep(50)

    def lambda_34DA():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_34DA)
    Sleep(300)

    #C0143
    ChrTalk(
        0x1A2,
        "#12P嗯，很好。\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x1A2,
        (
            "#12P另外，直接叫我秦就可以了。\x01",
            "你们又不是黑月的成员。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        "#5P#00009F哈哈……知道啦，秦。\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x1A2,
        (
            "#12P好！\x01",
            "那我们就赶快出门吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x1A2,
        (
            "#12P至于我想去的地方，\x01",
            "到了外面再详细说！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0148
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【带领少年秦游览市区】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1C5, 1)
    OP_29(0x73, 0x1, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 900, 0, 50, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_71(0x3, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x3)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 5800, 0, -1460, 270)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x80)
    EventEnd(0x5)
    Return()

    # Function_11_2826 end

    def Function_12_3677(): pass

    label("Function_12_3677")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31400.itc", 0x1E)
    OP_4B(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 3420, 0, 3170, 180)
    OP_68(3470, 1000, -250, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x1A2, 5800, 0, 1300, 180)
    SetChrPos(0x101, 2300, 0, 470, 90)
    SetChrPos(0x102, 2130, 0, -650, 90)
    SetChrPos(0x104, 1020, 0, 1050, 90)
    SetChrPos(0x109, 810, 0, -120, 90)
    SetChrPos(0x105, 1030, 0, -1210, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x8, 0x2)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0149
    AnonymousTalk(
        0x8,
        (
            "#11P#03204F#N呵呵，您似乎玩得很开心呢，\x01",
            "这真是再好不过。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(1000, 0)
    OP_0D()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 2)), scpexpr(EXPR_END)), "loc_37CF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_37CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 4)), scpexpr(EXPR_END)), "loc_37E2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_37E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 7)), scpexpr(EXPR_END)), "loc_37F5")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_37F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 0)), scpexpr(EXPR_END)), "loc_3808")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 1)), scpexpr(EXPR_END)), "loc_381B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_381B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 0)), scpexpr(EXPR_END)), "loc_382E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_382E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x154, 5)), scpexpr(EXPR_END)), "loc_3841")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 5)), scpexpr(EXPR_END)), "loc_3854")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3854")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 0)), scpexpr(EXPR_END)), "loc_3867")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3867")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3906")

    #C0150
    ChrTalk(
        0x1A2,
        "#5P嗯，此行非常有意义！\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x1A2,
        (
            "#5P克洛斯贝尔并不是\x01",
            "只有彩虹剧团和主题公园！\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x1A2,
        (
            "#5P我总算明白你这样的精干之人\x01",
            "为何会对这里如此执著了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39BD")

    label("loc_3906")


    #C0153
    ChrTalk(
        0x1A2,
        "#5P嗯，此行非常有意义！\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x1A2,
        (
            "#5P虽然我本想\x01",
            "再多逛逛的……\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x1A2,
        (
            "#5P不过，原来克洛斯贝尔并不是\x01",
            "只有彩虹剧团和主题公园！\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x1A2,
        (
            "#5P我总算明白你这样的精干之人\x01",
            "为何会对这里如此执著了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39BD")


    #C0157
    ChrTalk(
        0x8,
        "#11P#03200F哈哈，真是不敢当。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    #C0158
    ChrTalk(
        0x8,
        (
            "#11P#03200F罗伊德警官、艾莉小姐，\x01",
            "还有其他几位。\x02\x03",

            "#03209F我实在没想到你们\x01",
            "能让秦少爷如此开心。\x02\x03",

            "#03204F非常感谢，\x01",
            "大家真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x101,
        "#6P#00000F哪里，这没什么。\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x102,
        (
            "#6P#00102F呵呵，我们此行\x01",
            "也很愉快呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x9, 2580, 0, 1630, 2000, 0x0)

    def lambda_3ADA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3ADA)
    Sleep(50)

    def lambda_3AEA():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3AEA)
    Sleep(50)

    def lambda_3AFA():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3AFA)
    Sleep(50)

    def lambda_3B0A():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3B0A)
    Sleep(50)

    def lambda_3B1A():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3B1A)
    Sleep(50)

    def lambda_3B2A():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3B2A)
    Sleep(300)

    #C0161
    ChrTalk(
        0x9,
        (
            "区区薄礼，不成敬意，\x01",
            "但还请各位收下。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0162
    ChrTalk(
        0x101,
        (
            "#12P#00003F啊，我们是警察，\x01",
            "不能收取这种东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x8,
        (
            "#11P#03204F呵呵，我正是考虑到了这一点，\x01",
            "所以才没有将金钱当作谢礼。\x02\x03",

            "#03210F这份谢礼与我们无关，\x01",
            "就当作是各位与秦少爷结识的留念，\x01",
            "这样就可以收下了吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3CA9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3CA9)
    Sleep(50)

    def lambda_3CB9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3CB9)
    Sleep(50)

    def lambda_3CC9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3CC9)
    Sleep(50)

    def lambda_3CD9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3CD9)
    Sleep(50)

    def lambda_3CE9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3CE9)
    Sleep(300)

    #C0164
    ChrTalk(
        0x101,
        "#6P#00011F唔……\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x102,
        "#6P#00105F这……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x8, 500)
    Sleep(300)

    #C0166
    ChrTalk(
        0x1A2,
        "#5P曹，你的头脑好灵活啊！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    #C0167
    ChrTalk(
        0x1A2,
        (
            "#11P嗯，大家不用客气！\x01",
            "请收下吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x104,
        "#6P#00306F（没办法啊……）\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x105,
        (
            "#6P#10302F（呵呵，人家都这么说了，\x01",
            "  我们也只能收下啦。）\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x109,
        "#6P#10106F（确、确实如此。）\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        (
            "#6P#00001F……明白了，\x01",
            "既然不是钱，我们就收下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x102,
        "#6P#00100F非常感谢。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)
    Sleep(300)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3EB7")
    OP_29(0x73, 0x1, 0xD)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0173
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '月灵玉'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('月灵玉', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_3F04")

    label("loc_3EB7")

    OP_29(0x73, 0x1, 0xE)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0174
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '云之使者'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('云之使者', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_3F04")

    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    #C0175
    ChrTalk(
        0x101,
        (
            "#6P#00000F那么，我们\x01",
            "就此告辞了。\x02\x03",

            "#00009F秦，再见啦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    #C0176
    ChrTalk(
        0x102,
        "#6P#00109F呵呵，要保重哦。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    #C0177
    ChrTalk(
        0x1A2,
        "#11P嗯，大姐姐，你们也要保重身体！\x02",
    )

    CloseMessageWindow()

    def lambda_3FAB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3FAB)
    Sleep(100)

    def lambda_3FBB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3FBB)
    Sleep(100)

    def lambda_3FCB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3FCB)
    Sleep(100)

    def lambda_3FDB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FDB)
    Sleep(100)

    def lambda_3FEB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3FEB)
    WaitChrThread(0x104, 1)

    def lambda_3FFC():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3FFC)
    WaitChrThread(0x109, 1)

    def lambda_401A():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_401A)
    WaitChrThread(0x105, 1)

    def lambda_4038():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4038)
    WaitChrThread(0x101, 1)

    def lambda_4056():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4056)
    WaitChrThread(0x102, 1)

    def lambda_4074():
        OP_97(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4074)

    def lambda_408E():

        label("loc_408E")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_408E")

    QueueWorkItem2(0x9, 1, lambda_408E)
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)
    OP_68(4059, 1100, 340, 4000)
    MoveCamera(41, 23, 0, 4000)
    OP_6E(380, 4000)
    SetCameraDistance(21210, 4000)
    BeginChrThread(0xC, 1, 0, 13)
    OP_63(0x1A2, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x102, 1)
    Sleep(2000)
    OP_64(0xFFFF)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    EndChrThread(0x9, 0x1)

    #C0178
    ChrTalk(
        0x1A2,
        "………………………………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x2)

    def lambda_4139():

        label("loc_4139")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_4139")

    QueueWorkItem2(0x9, 1, lambda_4139)
    Sleep(300)

    #C0179
    ChrTalk(
        0x8,
        (
            "#11P#03200F呵呵，在街上走了这么久，\x01",
            "肯定很累了吧？\x02\x03",

            "#03204F我在房间里为您准备了\x01",
            "很高级的点心哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x1A2, 0x8, 500)
    Sleep(300)

    #C0180
    ChrTalk(
        0x1A2,
        (
            "#5P是、是吗，\x01",
            "你果然很善解人意呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x1A2,
        (
            "#5P嗯嗯，我回去之后一定\x01",
            "会仔细报告给爷爷的。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(4950, 1100, 3350, 3000)
    OP_95(0x1A2, 5000, 0, 5850, 2000, 0x0)
    OP_6F(0x1)
    Sound(103, 0, 100, 0)
    OP_71(0x3, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x3)
    Sleep(500)

    def lambda_426C():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_426C)
    Sleep(500)

    def lambda_4289():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A2, 2, lambda_4289)
    Sleep(500)
    Sound(104, 0, 100, 0)
    OP_71(0x3, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x3)
    Sleep(500)
    OP_6F(0x1)
    EndChrThread(0x9, 0x1)
    OP_68(5090, 1100, 880, 3000)
    OP_6F(0x1)

    #C0182
    ChrTalk(
        0x8,
        (
            "#11P#03204F呵呵，小小年纪就如此聪明，\x01",
            "今后必成大器呢。\x02\x03",

            "#03202F将来能否成为我的助力呢……\x01",
            "真是太期待了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)
    Sleep(300)

    #C0183
    ChrTalk(
        0x9,
        "#6P……是啊。\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x9,
        (
            "#6P但话说回来，这次的决定\x01",
            "是不是过于冒险了……？\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x9,
        (
            "#6P万一他们向\x01",
            "秦少爷下手，\x01",
            "曹先生可就要承担责任了……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)

    #C0186
    ChrTalk(
        0x8,
        (
            "#11P#03200F呵呵，若真的出现那种情况，\x01",
            "便只能说明他和我的天命已尽。\x02\x03",

            "#03204F不过，『他们』并没有那么愚蠢，\x01",
            "不会在这种时候惹出事端。\x02\x03",

            "#03201F对了，我们的人有什么收获吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x9,
        (
            "#6P是的，发现了两名\x01",
            "尾随秦少爷他们的人士。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x9,
        "#6P现在已经派人分别监视住他们了。\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x8,
        (
            "#11P#03204F很好，就在暗中盯紧他们，\x01",
            "不要被发现。\x02\x03",

            "#03200F一定要小心『商会』的\x01",
            "那些家伙突然横插一手。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x9,
        "#6P明白了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0191
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【带领少年秦游览市区】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x1000)
    OP_49()
    OP_D7(0x1E)
    RemoveParty(0xA1, 0xFF)
    OP_29(0x73, 0x4, 0x10)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_45CD")
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_45F6")

    label("loc_45CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_45E4")
    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_45F6")

    label("loc_45E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_45F6")
    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_45F6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_460F")
    OP_2C(0x73, 0x3)
    Jump("loc_467D")

    label("loc_460F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_463C")
    OP_2C(0x73, 0x2)
    Jump("loc_467D")

    label("loc_463C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4669")
    OP_2C(0x73, 0x1)
    Jump("loc_467D")

    label("loc_4669")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_467D")
    OP_2C(0x73, 0x0)

    label("loc_467D")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopBGM(0xFA0)
    WaitBGM()
    EventEnd(0x5)
    SetScenarioFlags(0x22, 6)
    NewScene("c1200", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_12_3677 end

    def Function_13_46A6(): pass

    label("Function_13_46A6")

    Sleep(1300)
    Sound(103, 0, 100, 0)
    Sleep(2000)
    Sound(104, 0, 100, 0)
    Return()

    # Function_13_46A6 end

    def Function_14_46B9(): pass

    label("Function_14_46B9")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0192
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门紧紧关闭着。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_14_46B9 end

    SaveToFile()

Try(main)
