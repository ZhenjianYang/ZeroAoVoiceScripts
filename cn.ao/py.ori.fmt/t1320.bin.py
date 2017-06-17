from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1320.bin",                # FileName
        "t1320",                    # MapName
        "t1320",                    # Location
        0x00BC,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 188, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1320",                  # 0
        "接待小姐卡尔米娜",       # 1
        "游客",                   # 2
        "游客",                   # 3
        "游客",                   # 4
        "救生员韦伯",             # 5
        "游客",                   # 6
        "游客",                   # 7
        "泳装介绍册",             # 8
    ))

    AddCharChip((
        "chr/ch34600.itc",                   # 00
        "chr/ch24402.itc",                   # 01
        "chr/ch44200.itc",                   # 02
        "chr/ch48200.itc",                   # 03
        "chr/ch23600.itc",                   # 04
        "chr/ch48200.itc",                   # 05
        "chr/ch48300.itc",                   # 06
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

    DeclNpc(-2000,   0,       5150,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-319,    200,     -5050,   90,   389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(1750,    0,       3230,    45,   385,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(106769,  0,       102819,  0,    385,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    452,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 9,   104.0,                 4.5,                   -1.0,                  16.0,                  [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -26.0,                 -2.25,                 0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 10,  8.850000381469727,     1.0,                   -1.0,                  16.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -4.425000190734863,    -0.25,                 0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 11,  88.52999877929688,     1.0,                   -1.0,                  16.0,                  [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -44.26499938964844,    -0.25,                 0.20000000298023224,   1.0])

    DeclActor(-2000,   0,       4650,    2000,    -2000,   1500,    5150,    0x007E, 0,  3,  0x0000)
    DeclActor(99280,   0,       3850,    1200,    99070,   1500,    4220,    0x007C, 0,  8,  0x0000)
    DeclActor(104000,  0,       4600,    1200,    104000,  1500,    4600,    0x007C, 0,  24, 0x0000)
    DeclActor(94000,   0,       4600,    1200,    94000,   1500,    4600,    0x007C, 0,  24, 0x0000)

    ChipFrameInfo(1024, 0)                                       # 0

    ScpFunction((
        "Function_0_400",          # 00, 0
        "Function_1_4B0",          # 01, 1
        "Function_2_5AD",          # 02, 2
        "Function_3_686",          # 03, 3
        "Function_4_68A",          # 04, 4
        "Function_5_7EF",          # 05, 5
        "Function_6_832",          # 06, 6
        "Function_7_86D",          # 07, 7
        "Function_8_95B",          # 08, 8
        "Function_9_AB2",          # 09, 9
        "Function_10_BCE",         # 0A, 10
        "Function_11_C9E",         # 0B, 11
        "Function_12_CF4",         # 0C, 12
        "Function_13_EAF",         # 0D, 13
        "Function_14_1ED6",        # 0E, 14
        "Function_15_1EFB",        # 0F, 15
        "Function_16_1F20",        # 10, 16
        "Function_17_3941",        # 11, 17
        "Function_18_3C5C",        # 12, 18
        "Function_19_44B2",        # 13, 19
        "Function_20_45F3",        # 14, 20
        "Function_21_6816",        # 15, 21
        "Function_22_6EE4",        # 16, 22
        "Function_23_6F21",        # 17, 23
        "Function_24_6F5E",        # 18, 24
    ))


    def Function_0_400(): pass

    label("Function_0_400")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_438"),
        (1, "loc_444"),
        (2, "loc_450"),
        (3, "loc_45C"),
        (4, "loc_468"),
        (5, "loc_474"),
        (6, "loc_480"),
        (SWITCH_DEFAULT, "loc_48C"),
    )


    label("loc_438")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_444")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_450")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_45C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_468")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_474")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_480")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_48C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_498")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_498")

    label("loc_4AF")

    Return()

    # Function_0_400 end

    def Function_1_4B0(): pass

    label("Function_1_4B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 4)), scpexpr(EXPR_END)), "loc_4BE")
    SetChrFlags(0x8, 0x80)

    label("loc_4BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EC")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)

    label("loc_4EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52E")
    SetChrPos(0x8, 96490, 0, 1360, 90)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)

    label("loc_52E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_542")
    ClearScenarioFlags(0x22, 0)
    Event(0, 16)
    Jump("loc_551")

    label("loc_542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_551")
    ClearScenarioFlags(0x22, 3)
    Event(0, 21)

    label("loc_551")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56C")
    SetMapFlags(0x10000000)
    Event(0, 17)

    label("loc_56C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 4)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_59B")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59B")
    SetMapFlags(0x10000000)
    Event(0, 18)

    label("loc_59B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5AC")
    Event(0, 12)

    label("loc_5AC")

    Return()

    # Function_1_4B0 end

    def Function_2_5AD(): pass

    label("Function_2_5AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5BF")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5BF")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5D7")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5EA")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_5EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_5F8")
    ModifyEventFlags(0, 0, 0x80)

    label("loc_5F8")

    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 4)), scpexpr(EXPR_END)), "loc_61D")
    ClearMapObjFlags(0x0, 0x10)
    ClearMapObjFlags(0x1, 0x10)
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)

    label("loc_61D")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_635")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7E, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64B")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_64B")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_663")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_678")
    OP_65(0x0, 0x1)

    label("loc_678")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 4)), scpexpr(EXPR_END)), "loc_685")
    OP_65(0x0, 0x1)

    label("loc_685")

    Return()

    # Function_2_5AD end

    def Function_3_686(): pass

    label("Function_3_686")

    Call(0, 4)
    Return()

    # Function_3_686 end

    def Function_4_68A(): pass

    label("Function_4_68A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6A1")
    Call(0, 13)
    Return()

    label("loc_6A1")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_7E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_76B")

    #C0001
    ChrTalk(
        0x8,
        (
            "多谢你们帮忙击退了\x01",
            "划破泳装的魔兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "但对方毕竟是魔兽，\x01",
            "谁也无法保证它们\x01",
            "不会再次出现……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "今后一定要让米修拉姆的事业部制定\x01",
            "相应对策，以保证魔兽不会再次出现。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7DD")

    label("loc_76B")


    #C0004
    ChrTalk(
        0x8,
        (
            "多谢你们帮忙击退了\x01",
            "划破泳装的魔兽。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "今后一定要让米修拉姆的事业部制定\x01",
            "相应对策，以保证魔兽不会再次出现。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DD")

    Jump("loc_7EB")

    label("loc_7E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_7EB")

    label("loc_7EB")

    TalkEnd(0x8)
    Return()

    # Function_4_68A end

    def Function_5_7EF(): pass

    label("Function_5_7EF")

    TalkBegin(0xFE)

    #C0006
    ChrTalk(
        0xFE,
        "我女朋友正在挑选泳装。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        "……就不能快点选中一件吗？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_7EF end

    def Function_6_832(): pass

    label("Function_6_832")

    TalkBegin(0xFE)

    #C0008
    ChrTalk(
        0xFE,
        "呀！有这么多可爱的泳装啊！\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        "该选哪件好呢～\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_832 end

    def Function_7_86D(): pass

    label("Function_7_86D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_913")
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0010
    ChrTalk(
        0xFE,
        "哇哇哇哇哇！？\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "不、不要带女孩子\x01",
            "进入男更衣室啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#00005F说、说的也是啊，\x01",
            "真对不起……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x153,
        "#01105F哎？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_957")

    label("loc_913")


    #C0014
    ChrTalk(
        0xFE,
        (
            "真、真是的……\x01",
            "完全不能大意。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "差点就被小女孩\x01",
            "看到屁股了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_957")

    TalkEnd(0xFE)
    Return()

    # Function_7_86D end

    def Function_8_95B(): pass

    label("Function_8_95B")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　　在湖水浴场游玩时的注意事项\x01",
            "——————————————————\x01",
            "·请在下水之前务必做好准备运动。\x01",
            "·请不要身着便装下水。\x01",
            "  （服务台提供租借泳装服务）\x01",
            "·请听从救生员的指挥。\x01",
            "——————————————————\x01",
            "  请遵守规章制度，祝您游玩愉快。\x01",
            "  　　　　　　　──米修拉姆事业部\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_8_95B end

    def Function_9_AB2(): pass

    label("Function_9_AB2")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B04")

    #C0017
    ChrTalk(
        0x101,
        (
            "#12500F……这里是女更衣室，\x01",
            "在造成误会之前，还是赶快离开吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B8A")

    #C0018
    ChrTalk(
        0x101,
        (
            "#00000F……哇，\x01",
            "这里是女更衣室。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x153,
        "#01105F罗伊德，要进去吗？\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#00006F啊……不不，不进去。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_BBA")

    label("loc_B8A")


    #C0021
    ChrTalk(
        0x101,
        (
            "#00000F这里是女更衣室……\x01",
            "还是不要进去了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BBA")

    SetChrPos(0x0, 104470, 0, 2310, 180)
    EventEnd(0x4)
    Return()

    # Function_9_AB2 end

    def Function_10_BCE(): pass

    label("Function_10_BCE")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C22")

    #C0022
    ChrTalk(
        0x101,
        (
            "#00000F还没有租到泳装呢，\x01",
            "不能往这边走。\x02\x03",

            "先去服务台租泳装吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7E, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C8A")

    #C0023
    ChrTalk(
        0x101,
        (
            "#00003F没时间再去湖水浴场了。\x02\x03",

            "#00000F赶快去主题公园吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x153,
        "#01109F嗯，出发！！\x02",
    )

    CloseMessageWindow()

    label("loc_C8A")

    SetChrPos(0x0, 7010, 0, 1020, 270)
    EventEnd(0x4)
    Return()

    # Function_10_BCE end

    def Function_11_C9E(): pass

    label("Function_11_C9E")

    EventBegin(0x1)

    #C0025
    ChrTalk(
        0x101,
        (
            "#12500F啊，不能穿成这样\x01",
            "四处乱逛。\x02\x03",

            "还是赶快去湖水浴场吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 91160, 0, 690, 90)
    EventEnd(0x4)
    Return()

    # Function_11_C9E end

    def Function_12_CF4(): pass

    label("Function_12_CF4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -9000, 0, 1000, 90)
    SetChrPos(0x104, -9500, 0, 2130, 90)
    SetChrPos(0x105, -9500, 0, 130, 90)
    OP_68(2400, 1600, 1130, 0)
    MoveCamera(315, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    FadeToBright(1000, 0)
    OP_68(-5400, 1600, 1130, 5000)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    OP_68(-9350, 3500, 1480, 0)
    MoveCamera(316, 12, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18050, 0)
    OP_68(-9350, 1500, 1480, 2000)
    OP_0D()
    OP_6F(0x79)

    #C0026
    ChrTalk(
        0x101,
        (
            "#00002F#5P啊……\x01",
            "这里就是湖水浴场的服务台吧？\x02\x03",

            "#00000F好像可以在这里\x01",
            "租借泳装呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#00309F#5P呼～竟然能建造出\x01",
            "这样的地方，\x01",
            "真是做梦都想象不到啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x105,
        (
            "#10302F#5P呵呵，我们赶快去\x01",
            "租借泳装吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -8000, 0, 1130, 90)
    SetScenarioFlags(0x144, 6)
    EventEnd(0x5)
    Return()

    # Function_12_CF4 end

    def Function_13_EAF(): pass

    label("Function_13_EAF")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51090.itc", 0x1E)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x2)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x9)
    SetChrPos(0xF, -1500, 1000, 3500, 0)
    SetChrFlags(0xF, 0x8)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x101, -2000, 0, 2500, 0)
    SetChrPos(0x104, -3000, 0, 2350, 0)
    SetChrPos(0x105, -1000, 0, 2450, 0)
    SetMapObjFlags(0x0, 0x1000)
    FadeToBright(1000, 0)
    OP_68(-2000, 1000, 3850, 0)
    MoveCamera(315, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(18500, 1500)
    OP_6F(0x79)
    OP_0D()

    #C0029
    ChrTalk(
        0x8,
        (
            "#11P您好，欢迎光临\x01",
            "湖水浴场。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "#11P是特别任务支援科\x01",
            "的各位吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        "#00005F#6P啊，是的。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        (
            "#00302F#6P玛丽亚贝尔大小姐\x01",
            "已经帮我们打过招呼了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#11P是的，到今日中午为止，\x01",
            "由各位包场游玩。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_9B(0x0, 0x8, 0x0, 0xC8, 0x3E8, 0x0)
    Sleep(300)
    Sound(18, 0, 100, 0)
    Fade(250)
    ClearChrFlags(0xF, 0x8)
    OP_0D()

    #C0034
    ChrTalk(
        0x8,
        (
            "#11P我们准备了泳装\x01",
            "照片的图册，\x01",
            "请挑选您喜欢的款式。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        "#00002F#6P嘿，那就来挑挑看吧……\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        "#00309F#6P嗯～该选哪件好呢～\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x105,
        "#10308F#6P……………唔。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xF, 0x80)
    OP_49()
    OP_D7(0x1E)
    Sleep(1000)
    LoadChrToIndex("chr/ch15000.itc", 0x1E)
    LoadChrToIndex("chr/ch15300.itc", 0x1F)
    LoadChrToIndex("chr/ch15400.itc", 0x20)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12900.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12500.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12800.itp")
    SetChrPos(0x101, 100000, 0, 100300, 0)
    SetChrPos(0x104, 100000, 0, 101700, 180)
    SetChrPos(0x105, 109000, 0, 101000, 270)
    SetChrChipByIndex(0x105, 0x20)
    SetChrSubChip(0x105, 0x0)
    OP_68(94020, 1500, 4870, 0)
    MoveCamera(330, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(22000, 4000)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(100000, 2200, 101000, 0)
    MoveCamera(305, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18520, 0)
    OP_68(100000, 1200, 101000, 2000)
    OP_6F(0x79)
    OP_0D()

    #C0038
    ChrTalk(
        0x104,
        (
            "#00316F#11P说起来，罗伊德……\x02\x03",

            "#00315F你觉不觉得，自从加入特别任务支援科，\x01",
            "这是咱们受到的最棒的奖赏！？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#00012F#6P你、你太夸张啦。\x02\x03",

            "#00002F不过，大家将会穿着\x01",
            "什么样的泳装呢……\x01",
            "还真是有点期待啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#00309F#11P对吧对吧⊥\x02\x03",

            "#00301F能看到伊莉娅小姐\x01",
            "和塞茜尔小姐穿泳装的样子啊！！\x02\x03",

            "#00307F而且还有莉夏那样的\x01",
            "超级潜力股！\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#00011F#6P冷、冷静些。\x02\x03",

            "#00006F……嗯，话说回来，\x01",
            "我们的确在不经意间\x01",
            "结识了很多身材出众的女性呢。\x02\x03",

            "#00002F塞茜尔姐姐和莉夏自不必说，\x01",
            "艾莉的身材也相当丰满……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        (
            "#00304F#11P伊莉娅小姐简直就像模特一样，\x01",
            "诺艾尔和芙兰\x01",
            "也很有看点呢。\x02\x03",

            "#00302F至于阿缇和阿修，\x01",
            "也只能期待她们今后的成长了。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        (
            "#00006F#6P你太失礼啦，兰迪。\x02\x03",

            "#00005F啊……说起来，\x01",
            "琪雅会游泳吗？\x02\x03",

            "#00001F之前倒是没问过她。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#00303F#11P唔……那么久以前的事情，\x01",
            "她本人恐怕也不记得了吧。\x02\x03",

            "#00300F最好有人在她旁边照看，\x01",
            "以免她溺水。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        "#00000F#6P嗯，说的对。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(2434, 255, 80, 0)    #voice#Lazy
    Sleep(800)

    #C0046
    ChrTalk(
        0x105,
        "#1P呵呵，真是疼爱孩子的家长啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1635():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1635)
    Sleep(50)

    def lambda_1645():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1645)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    SetCameraDistance(19500, 3000)
    OP_68(102000, 1000, 101000, 3000)
    Sleep(500)
    OP_9B(0x0, 0x105, 0x0, 0xFA0, 0x7D0, 0x0)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(40, 120, -1, -1)

    #A0047
    AnonymousTalk(
        0x101,
        "#00005F瓦吉……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(80, 140, -1, -1)

    #A0048
    AnonymousTalk(
        0x104,
        "#00305F你、你已经换好泳装了啊？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 35, 3)

    #A0049
    AnonymousTalk(
        0x105,
        "嗯，我去外面等你们。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    OP_93(0x105, 0xB4, 0x1F4)
    Sound(2424, 255, 100, 0)    #voice#Lazy
    Sleep(500)
    MoveCamera(325, 18, 0, 4000)

    def lambda_1791():

        label("loc_1791")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_1791")

    QueueWorkItem2(0x101, 2, lambda_1791)

    def lambda_17A3():

        label("loc_17A3")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_17A3")

    QueueWorkItem2(0x104, 2, lambda_17A3)

    def lambda_17B5():
        OP_95(0xFE, 104270, 0, 97380, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_17B5)
    WaitChrThread(0x105, 1)

    def lambda_17D3():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_17D3)
    Sound(121, 0, 100, 0)
    Sleep(500)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x105, 1)
    Sound(890, 0, 100, 0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x104, 0x2)
    OP_6F(0x79)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x104)
    Fade(500)
    OP_68(100410, 1000, 101610, 0)
    MoveCamera(320, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16640, 0)
    OP_68(100240, 1000, 101490, 0)
    MoveCamera(311, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17470, 0)
    OP_0D()

    #C0050
    ChrTalk(
        0x104,
        "#00301F#5P太奇怪了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 500)

    #C0051
    ChrTalk(
        0x101,
        (
            "#00005F#6P奇怪……是说瓦吉吗？\x02\x03",

            "#00012F我觉得他一直\x01",
            "都是个奇怪的家伙。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)

    #C0052
    ChrTalk(
        0x104,
        (
            "#00306F#11P不，我并不是指这个。\x02\x03",

            "#00303F是指那家伙趁我们聊天时\x01",
            "迅速换好泳装的行为。\x02\x03",

            "而且偏偏还选择那种\x01",
            "男女通用的两件式泳装……\x02\x03",

            "#00301F……你不觉得很奇怪吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#00011F#6P的确是有点奇怪，\x01",
            "但也说不清是哪里……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x104,
        (
            "#00306F#11P呼，你可真是个呆子。\x02\x03",

            "#00300F……算了，\x01",
            "我们也赶快换好泳装吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#00000F#6P是啊，不要让瓦吉等太久。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(94150, 1200, 1070, 0)
    MoveCamera(316, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18520, 0)
    SetChrPos(0x101, 94020, 0, 5870, 180)
    SetChrPos(0x104, 94020, 0, 5870, 180)
    SetChrPos(0x105, 94020, 0, 370, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0x1F)
    SetChrSubChip(0x104, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(121, 0, 100, 0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x8)
    Sleep(300)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_79(0x0)
    OP_68(94380, 1200, 1630, 3500)
    BeginChrThread(0x101, 3, 0, 14)
    Sleep(1000)
    BeginChrThread(0x104, 3, 0, 15)
    Sleep(1500)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x8)
    Sleep(300)
    Sound(890, 0, 100, 0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x79)
    Sound(2088, 255, 100, 0)    #voice#Lloyd
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0056
    AnonymousTalk(
        0x101,
        "瓦吉，久等了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Sound(2364, 255, 100, 0)    #voice#Randy
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0057
    AnonymousTalk(
        0x104,
        "好，我们走吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    #C0058
    ChrTalk(
        0x105,
        "#12905F#6P……………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0059
    ChrTalk(
        0x101,
        "#12505F#5P哎，怎么了？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        "#12805F#11P我们身上有什么奇怪的东西吗？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2429, 255, 100, 0)    #voice#Lazy
    Sleep(600)

    #C0061
    ChrTalk(
        0x105,
        (
            "#12904F#6P没什么，我只是在想，\x01",
            "男人穿泳装也并非难以入目嘛。\x02\x03",

            "#12902F你们两个的体格都很不错，\x01",
            "并没让我失望哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0062
    ChrTalk(
        0x101,
        "#12513F#5P那个……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x104,
        "#12801F#11P真是多余的夸奖。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x105,
        (
            "#12909F#6P呵呵，那我们就\x01",
            "赶快去湖水浴场吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_CC(0x1, 0xFF, 0x0)
    OP_4C(0x8, 0xFF)
    ClearMapObjFlags(0x0, 0x1000)
    SetChrChipPat(0x0, 0x1, 0x60)
    LoadChrChipPat()
    SetChrChipPat(0x3, 0x1, 0x61)
    LoadChrChipPat()
    SetChrChipPat(0x4, 0x1, 0x62)
    LoadChrChipPat()
    OP_C7(0x1, 0x17)
    SetChrPos(0x0, 94020, 0, 1060, 90)
    SetScenarioFlags(0x144, 7)
    OP_29(0xA5, 0x1, 0x2)
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    EventEnd(0x5)
    Return()

    # Function_13_EAF end

    def Function_14_1ED6(): pass

    label("Function_14_1ED6")


    def lambda_1EDB():
        OP_9B(0x1, 0xFE, 0xA, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1EDB)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_14_1ED6 end

    def Function_15_1EFB(): pass

    label("Function_15_1EFB")


    def lambda_1F00():
        OP_9B(0x1, 0xFE, 0xFFF6, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1F00)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_15_1EFB end

    def Function_16_1F20(): pass

    label("Function_16_1F20")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03000.itc", 0x1E)
    LoadChrToIndex("apl/ch51322.itc", 0x1F)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    SetChrPos(0x101, 100000, 0, 100300, 0)
    SetChrPos(0x104, 100000, 0, 101700, 180)
    SetChrPos(0x105, 109000, 0, 101000, 270)
    SetChrChipByIndex(0x105, 0x1E)
    SetChrSubChip(0x105, 0x0)
    OP_68(100000, 2200, 101000, 0)
    MoveCamera(305, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18520, 0)
    FadeToBright(1000, 0)
    OP_68(100000, 1200, 101000, 3000)
    OP_6F(0x79)
    OP_0D()

    #C0065
    ChrTalk(
        0x104,
        (
            "#12809F#11P嘿～虽然玩得有些累，\x01",
            "但真是很享受啊。\x02\x03",

            "#12801F唔……要说遗憾，\x01",
            "那就是塞茜尔小姐和莉夏\x01",
            "没有参加沙滩排球啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        "#12505F#6P哎，为什么……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1300)
    OP_64(0x101)
    Sleep(150)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0067
    ChrTalk(
        0x101,
        "#12513F#6P喂、喂！兰迪！\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x104,
        (
            "#12802F#11P嗯？怎么，\x01",
            "你突然想到什么了～？\x02\x03",

            "#12806F对了！说起来，\x01",
            "你还见缝插针，给大小姐和\x01",
            "塞茜尔小姐她们涂了防晒霜吧～\x02\x03",

            "#12801F喂喂，有什么感想？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#12512F#6P没、没有啦……\x02\x03",

            "但不得不说，真是一次\x01",
            "相当刺激的经历……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x104,
        (
            "#12807F#11P什么～！？\x02\x03",

            "#12810F可恶～你竟敢\x01",
            "独自一人享受这种好事！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_9B(0x0, 0x104, 0x0, 0x3E8, 0xBB8, 0x0)
    Fade(350)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1F)
    OP_A1(0x101, 0x3E8, 0x2, 0x0, 0x1)
    OP_63(0x101, 0x96, 1400, 0x28, 0x2B, 0x64, 0x0)
    Sound(908, 0, 70, 0)
    OP_A1(0x101, 0x1F4, 0x6, 0x2, 0x3, 0x2, 0x3, 0x2, 0x3)
    OP_64(0x101)
    OP_0D()

    #C0071
    ChrTalk(
        0x101,
        "#12511F#6P哇，疼疼疼！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 100000, 0, 100300, 90)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x104, 0x8)
    SetChrPos(0x104, 100000, 0, 101000, 180)

    def lambda_22C0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_22C0)
    OP_9B(0x1, 0x104, 0x0, 0xFFFFFD44, 0x7D0, 0x0)
    WaitChrThread(0x101, 2)
    OP_0D()

    #C0072
    ChrTalk(
        0x104,
        (
            "#12803F#11P话说回来，罗伊德。\x02\x03",

            "#12802F谁的泳装形象\x01",
            "最让你动心呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    #Sound(4131, 255, 100, 0)    #voice#Lloyd

    #C0073
    ChrTalk(
        0x101,
        (
            "#12511F#6P哎哎！？\x02\x03",

            "#12508F（唔……\x01",
            "  非要回答的话……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 5, -1, -1)
    SetChrName("")

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K谁的泳装形象最吸引人呢？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        100,
        0,
        (
            "艾莉\x01",        # 0
            "缇欧\x01",        # 1
            "诺艾尔\x01",      # 2
            "芙兰\x01",        # 3
            "琪雅\x01",        # 4
            "塞茜尔\x01",      # 5
            "伊莉娅\x01",      # 6
            "莉夏\x01",        # 7
            "修利\x01",        # 8
            "兰迪\x01",        # 9
            "瓦吉\x01",        # 10
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2473"),
        (1, "loc_25C0"),
        (2, "loc_2702"),
        (3, "loc_2845"),
        (4, "loc_2984"),
        (5, "loc_2AD9"),
        (6, "loc_2C1C"),
        (7, "loc_2D60"),
        (8, "loc_2EB0"),
        (9, "loc_306E"),
        (10, "loc_31AC"),
        (SWITCH_DEFAULT, "loc_32E8"),
    )


    label("loc_2473")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12600.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    #A0075
    AnonymousTalk(
        0x101,
        (
            "#3C（嗯……虽然早就知道\x01",
            "  艾莉的身材很出众了……）\x02\x03",

            "（伤脑筋啊……\x01",
            "  今后一起工作的时候，\x01",
            "  最好能控制住自己，不要胡思乱想。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_32E8")

    label("loc_25C0")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12700.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    #A0076
    AnonymousTalk(
        0x101,
        (
            "#3C（虽然泳装的款式比较保守，\x01",
            "  但楚楚可怜的感觉真是不错……）\x02\x03",

            "（黑色的连体式泳装与\x01",
            "  雪白的肌肤形成鲜明对比……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_32E8")

    label("loc_2702")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13001.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    #A0077
    AnonymousTalk(
        0x101,
        (
            "#3C（诺艾尔的运动式泳装\x01",
            "  很符合她的一贯风格呢。）\x02\x03",

            "（不过，平时一直被\x01",
            "  抑制住了的魅力一下子就\x01",
            "  全展露出来了……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_32E8")

    label("loc_2845")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13100.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    #A0078
    AnonymousTalk(
        0x101,
        (
            "#3C（嗯……要说可爱，\x01",
            "  还是以芙兰的泳装形象\x01",
            "  为最吧？）\x02\x03",

            "（粉色泳装上点缀着水滴图案……\x01",
            "  真适合她的气质呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_32E8")

    label("loc_2984")

    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13200.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    #A0079
    AnonymousTalk(
        0x101,
        (
            "#3C（嗯，还是琪雅穿泳装\x01",
            "  最可爱啊。）\x02\x03",

            "（那件泳装应该是\x01",
            "  艾莉或缇欧帮她挑的吧？）\x02\x03",

            "（虽然是便于行动的简单款式，\x01",
            "  但又不失别致……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_32E8")

    label("loc_2AD9")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13300.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    #A0080
    AnonymousTalk(
        0x101,
        (
            "#3C（塞茜尔姐姐……\x01",
            "  穿成那样，未免有点犯规了吧……）\x02\x03",

            "（说起来，以前好像\x01",
            "  并没有注意过塞茜尔姐姐\x01",
            "  的身材呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_32E8")

    label("loc_2C1C")

    OP_50(0x6C, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13400.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    #A0081
    AnonymousTalk(
        0x101,
        (
            "#3C（伊莉娅小姐……\x01",
            "  果然有大明星的感觉啊。）\x02\x03",

            "（无论在什么时候都如此耀眼……\x01",
            "  也不难理解大家为何都那么喜欢她了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_32E8")

    label("loc_2D60")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13500.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    #A0082
    AnonymousTalk(
        0x101,
        (
            "#3C（唔……以莉夏的身高来说，\x01",
            "  那种身材实在是太犯规了啊……）\x02\x03",

            "（仔细想想的话，她平时就经常穿着\x01",
            "  暴露度接近泳装的舞台装呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_32E8")

    label("loc_2EB0")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13600.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2FB7")

    #A0083
    AnonymousTalk(
        0x101,
        (
            "#3C（哈哈，虽然她平时总像个男孩，\x01",
            "  但终究是个女孩子啊。）\x02\x03",

            "（在初次见面时，还发生过\x01",
            "  一件很严重的误会呢……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3026")

    label("loc_2FB7")


    #A0084
    AnonymousTalk(
        0x101,
        (
            "#3C（哈哈，虽然她平时总像个男孩，\x01",
            "  但终究是个女孩子啊。）\x02\x03",

            "（说起来，在初次介绍时，\x01",
            "  差点就搞错了呢。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3026")

    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_32E8")

    label("loc_306E")

    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12800.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    #A0085
    AnonymousTalk(
        0x101,
        (
            "#3C（说起来……\x01",
            "  兰迪的体格确实很棒呢。）\x02\x03",

            "（如果仔细观察，可以发现很多伤疤……\x01",
            "  应该是在猎兵时代留下的吧？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_32E8")

    label("loc_31AC")

    OP_50(0x69, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12900.itp")
    FadeToDark(300, 0, 100)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetMessageWindowPos(20, 230, -1, 3)

    #A0086
    AnonymousTalk(
        0x101,
        (
            "#3C（说起来……瓦吉的泳装\x01",
            "  真是很令人在意呢。）\x02\x03",

            "（男女通用的两件式泳装……\x01",
            "  也许只是他单纯的喜好而已吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Jump("loc_32E8")

    label("loc_32E8")

    Sleep(300)

    #C0087
    ChrTalk(
        0x105,
        (
            "#1P哎呀呀，两个大男人\x01",
            "在一起聊什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        "#12511F#6P啊！\x02",
    )

    CloseMessageWindow()

    def lambda_3330():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3330)
    Sleep(50)

    def lambda_3340():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3340)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    SetCameraDistance(19500, 3000)
    OP_68(102000, 1000, 101000, 3000)
    Sleep(500)
    OP_9B(0x0, 0x105, 0x0, 0xFA0, 0x7D0, 0x0)
    OP_6F(0x79)

    #C0089
    ChrTalk(
        0x101,
        "#12505F#5P瓦吉……\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x104,
        (
            "#12805F#5P喂喂，\x01",
            "你已经换完衣服了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x105,
        (
            "#10306F#12P呼，年轻人就是\x01",
            "喜欢胡思乱想，\x01",
            "这也是没办法的事啊。\x02\x03",

            "#10302F不过，还是要从容稳重一些，\x01",
            "才能让女孩子接受哦。\x02\x03",

            "#10309F在此基础上让对方明白\x01",
            "你对她有兴趣，就比较完美了。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#12511F#5P不、不是啦！\x01",
            "我们并不是在讨论那种话题！\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x104,
        (
            "#12801F#5P你的观点我基本同意……\x01",
            "但口气未免也太居高临下了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x105,
        "#10302F#12P没办法，谁让我是受欢迎的人呢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0095
    ChrTalk(
        0x105,
        (
            "#10304F#12P呵呵，我先走一步，\x01",
            "回酒店房间了。\x02\x03",

            "#10300F在去主题公园游玩之前，\x01",
            "我想稍微休息一下。\x02\x03",

            "#10302F稍后再见啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0xB4, 0x1F4)
    MoveCamera(325, 18, 0, 4000)

    def lambda_35E5():

        label("loc_35E5")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_35E5")

    QueueWorkItem2(0x101, 2, lambda_35E5)

    def lambda_35F7():

        label("loc_35F7")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_35F7")

    QueueWorkItem2(0x104, 2, lambda_35F7)

    def lambda_3609():
        OP_95(0xFE, 104270, 0, 97380, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3609)
    WaitChrThread(0x105, 1)

    def lambda_3627():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3627)
    Sound(121, 0, 100, 0)
    Sleep(500)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    WaitChrThread(0x105, 1)
    Sound(890, 0, 100, 0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x104, 0x2)
    OP_6F(0x79)
    OP_63(0x104, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(100410, 1000, 101610, 0)
    MoveCamera(320, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16640, 0)
    OP_68(100240, 1000, 101490, 0)
    MoveCamera(311, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17470, 0)
    OP_0D()

    #C0096
    ChrTalk(
        0x104,
        (
            "#12807F#11P可恶，真是难以接受！\x02\x03",

            "#12806F被嘲笑了一顿，而且还没能看到\x01",
            "那家伙换装，总有种莫名的失败感啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#12506F#5P算啦，毕竟对手太难对付了。\x02\x03",

            "#12500F直到现在，\x01",
            "他也会在有兴致的晚上，\x01",
            "外出做男公关的兼职呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x104,
        (
            "#12801F#11P这未免也太让人羡——\x01",
            "不对！未免也太不像话了！\x02\x03",

            "#12803F我一定要跟踪他一次，\x01",
            "揭穿那家伙的真面目！\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        "#12512F#5P（完全没有说服力呢……）\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(17720, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    SetChrName("")

    #A0100
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德等人返回酒店\x01",
            "稍作歇息……\x02\x03",

            "接下来决定各自行动，在采购完毕后\x01",
            "到主题公园门前集合。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    SetChrChipPat(0x0, 0x1, 0x0)
    LoadChrChipPat()
    SetChrChipPat(0x3, 0x1, 0x3)
    LoadChrChipPat()
    SetChrChipPat(0x4, 0x1, 0x4)
    LoadChrChipPat()
    OP_C7(0x1, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("t1080", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_1F20 end

    def Function_17_3941(): pass

    label("Function_17_3941")

    EventBegin(0x0)
    OP_68(-5720, 1600, 1240, 0)
    MoveCamera(312, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25730, 0)
    SetChrPos(0x101, -12960, 0, 640, 90)
    SetChrPos(0x153, -12960, 0, 1770, 90)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    LoadChrToIndex("chr/ch48300.itc", 0x20)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 98840, 0, 1140, 270)
    OP_68(-9290, 1100, 1300, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x2, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x0)
    Sleep(500)

    def lambda_3A0B():
        OP_97(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3A0B)
    Sleep(500)

    def lambda_3A28():
        OP_97(0xFE, 0xBB8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_3A28)
    Sleep(1000)
    Sound(107, 0, 100, 0)
    OP_71(0x2, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    WaitChrThread(0x101, 1)
    Sleep(500)
    TurnDirection(0x153, 0x101, 500)
    Sleep(100)

    #C0101
    ChrTalk(
        0x153,
        (
            "#11P#01105F罗伊德，我们\x01",
            "不去主题公园了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        "#6P#00000F不、不是啦……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x87, 0x1F4)
    Sleep(100)

    #C0103
    ChrTalk(
        0x101,
        "#6P#00005F话说回来，这里还真是冷清啊。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(100)

    #C0104
    ChrTalk(
        0x101,
        (
            "#6P#00003F接待员也不在……\x01",
            "到底去哪里了？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(6090, 1600, 50, 4000)
    OP_6F(0x1)
    Sleep(100)

    #N0105
    NpcTalk(
        0xE,
        "女性的声音",
        "#4P#N#2S……这算怎么回事……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #N0106
    NpcTalk(
        0x8,
        "女性的声音",
        "#4P#N#2S……对、对不起……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x153, 0x5A, 0x0)
    Fade(500)
    OP_68(-9290, 1100, 1300, 0)
    MoveCamera(312, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25730, 0)
    OP_0D()

    #C0107
    ChrTalk(
        0x153,
        "#11P#01105F我听到有人在说话呢！\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#6P#00003F嗯，好像是在\x01",
            "争执……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x15B, 4)
    SetChrPos(0x0, -9420, 0, 610, 90)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_17_3941 end

    def Function_18_3C5C(): pass

    label("Function_18_3C5C")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch23600.itc", 0x1E)
    LoadChrToIndex("chr/ch48200.itc", 0x1F)
    LoadChrToIndex("chr/ch48300.itc", 0x20)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0x8, 96490, 0, 1360, 90)
    SetChrPos(0xC, 96150, 0, 60, 90)
    SetChrPos(0xD, 99300, 0, -400, 315)
    SetChrPos(0xE, 98840, 0, 1140, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_435D")
    OP_68(96990, 1600, 210, 0)
    MoveCamera(44, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15360, 0)
    SetChrPos(0x101, 90240, 0, 570, 90)
    SetChrPos(0x153, 90020, 0, 1390, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #C0109
    ChrTalk(
        0xE,
        (
            "我难得来湖水浴场玩一次，\x01",
            "居然会遇到这种事……\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xE,
        (
            "你们这里的管理部门\x01",
            "难道是摆设吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        "实在抱歉……\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xC,
        (
            "#6P这也怪我\x01",
            "监视不力。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xD,
        (
            "好啦好啦。\x01",
            "人家已经给你道歉了，\x01",
            "就这么算了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xD,
        (
            "反正你也\x01",
            "没有受伤。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xE,
        (
            "不行！我不能接受\x01",
            "就这样了结！\x02",
        )
    )

    CloseMessageWindow()

    #N0116
    NpcTalk(
        0x101,
        "罗伊德的声音",
        "请问……发生什么事了？\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(96820, 1700, -360, 0)
    MoveCamera(308, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17010, 0)
    TurnDirection(0xD, 0x101, 0)
    TurnDirection(0xC, 0x101, 0)
    TurnDirection(0x8, 0x101, 0)

    def lambda_3F14():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3F14)
    Sleep(200)

    def lambda_3F31():
        OP_97(0xFE, 0x3E8, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_3F31)
    Sleep(500)
    WaitChrThread(0x153, 1)

    #C0117
    ChrTalk(
        0x153,
        "#5P#01100F你们在吵架吗？\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xC,
        (
            "#12P你们不是……玛丽亚贝尔小姐\x01",
            "招待的客人吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        (
            "啊啊，真对不起！\x01",
            "我竟然把接待工作扔下不管……\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        (
            "#5P#00000F哪里，这倒不要紧……\x01",
            "请问是不是发生了什么事？\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xE,
        "这还用说吗！\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xE,
        (
            "我刚才正在浴场游泳，\x01",
            "结果突然有人把我的泳装划破了！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0123
    ChrTalk(
        0x101,
        "#5P#00005F把、把泳装……？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x8,
        (
            "其实……自湖水浴场开放以来，\x01",
            "已经发生过两三起女性客人\x01",
            "的泳装被划破的事件了。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x8,
        (
            "在今早的包场时间段中并没有\x01",
            "发生意外，但刚才却……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xD,
        (
            "#12P我们也听说过这方面的传闻，\x01",
            "但却没想到会成为当事人啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(100)
    TurnDirection(0xE, 0xD, 500)
    Sleep(1000)

    #C0127
    ChrTalk(
        0xE,
        (
            "被人划破泳装，\x01",
            "在公众面前丢人出丑的\x01",
            "可是你的女朋友啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xE,
        (
            "你就不能\x01",
            "表现出愤怒吗！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(500)

    #C0129
    ChrTalk(
        0xD,
        "#6P就、就算你这么说，我也……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x8, 500)
    Sleep(500)

    #C0130
    ChrTalk(
        0xE,
        (
            "总之……\x01",
            "你们米修拉姆的负责人\x01",
            "必须给我把犯人抓到！\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xE,
        (
            "否则我就会向你们\x01",
            "发起诉讼！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_427F():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_427F)
    Sleep(100)

    def lambda_428F():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_428F)
    Sleep(1000)

    #C0132
    ChrTalk(
        0x8,
        "#5P这、这……\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xC,
        "#5P实在是很难啊……\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xC,
        (
            "#5P毕竟我们连犯人的样子\x01",
            "都没有见到过。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x153,
        (
            "#5P#01111F（哎～\x01",
            "  事情好像很严重啊。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)
    Sleep(500)

    #C0136
    ChrTalk(
        0x153,
        "#11P#01100F（罗伊德，要不要帮帮他们呢？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_448C")

    label("loc_435D")

    OP_68(96820, 1700, -360, 0)
    MoveCamera(308, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17010, 0)
    SetChrPos(0x101, 91240, 0, 570, 90)
    SetChrPos(0x153, 91020, 0, 1390, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #C0137
    ChrTalk(
        0xE,
        (
            "赶快把划破我泳装\x01",
            "的犯人抓到！\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xE,
        (
            "否则我就会向你们\x01",
            "发起诉讼！\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x8,
        "#5P这、这……\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xC,
        "#5P实在是很难啊……\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xC,
        (
            "#5P毕竟我们连犯人的样子\x01",
            "都没有见到过。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)
    Sleep(500)

    #C0142
    ChrTalk(
        0x153,
        "#11P#01100F（罗伊德，要不要帮帮他们呢？）\x02",
    )

    CloseMessageWindow()

    label("loc_448C")

    Call(0, 19)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 7230, 0, 790, 270)
    EventEnd(0x5)
    Return()

    # Function_18_3C5C end

    def Function_19_44B2(): pass

    label("Function_19_44B2")


    #C0143
    ChrTalk(
        0x101,
        (
            "#5P#00003F（怎么办呢……？\x01",
            "  我们正准备去\x01",
            "  主题公园呢……）\x02",
        )
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
            "【帮忙寻找犯人】\x01",      # 0
            "【放弃】\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_455F")
    Call(0, 20)
    Jump("loc_45F2")

    label("loc_455F")


    #C0144
    ChrTalk(
        0x101,
        (
            "#5P#00003F（大家还在主题公园的门口\x01",
            "  等着我们呢……\x01",
            "  还是不要插手这里的事情了。）\x02\x03",

            "#00000F（这件事情就交给米修拉姆\x01",
            "  的事业部来处理吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15B, 5)

    label("loc_45F2")

    Return()

    # Function_19_44B2 end

    def Function_20_45F3(): pass

    label("Function_20_45F3")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(1000)

    #C0145
    ChrTalk(
        0x101,
        (
            "#5P#00000F……各位，如果可以，\x01",
            "能否把这件事情的详细经过告诉我？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_46B5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_46B5)
    Sleep(100)

    def lambda_46C5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_46C5)
    Sleep(100)

    def lambda_46D5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_46D5)
    Sleep(500)

    #C0146
    ChrTalk(
        0x101,
        (
            "#5P#00004F我身为一名警察，\x01",
            "绝不能对这种卑劣的\x01",
            "犯罪行为视而不见。\x02\x03",

            "#00000F如果顺利，说不定可以\x01",
            "推测出犯人的身份，\x01",
            "能否请各位协助我呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x8,
        (
            "好吧……\x01",
            "那就拜托你了！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(500)

    #C0148
    ChrTalk(
        0xD,
        (
            "#12P哈哈，他会帮我们寻找犯人，\x01",
            "太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xE,
        "哼，那就拜托你了。\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xC,
        (
            "#12P既然如此，在走廊上说这些也不太好，\x01",
            "我们还是去更衣室里谈吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        "#5P#00000F嗯，走吧。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x153,
        "#11P#01109F加油啊，罗伊德！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0153
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【调查划破泳装事件】\x07\x00",
            "开始！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x7E, 0x4, 0x2)
    OP_29(0x7E, 0x1, 0x0)
    OP_68(3220, 1500, 100150, 0)
    MoveCamera(318, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16620, 0)
    SetChrPos(0x101, 3570, 0, 99420, 0)
    SetChrPos(0x153, 4410, 0, 100170, 315)
    SetChrPos(0x8, 1210, 0, 101710, 135)
    SetChrPos(0xC, 840, 0, 100620, 135)
    SetChrPos(0xD, 2970, 0, 102410, 180)
    SetChrPos(0xE, 3930, 0, 102440, 180)
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0154
    ChrTalk(
        0x101,
        (
            "#6P#00001F那么，首先请把事件\x01",
            "发生时的状况告诉我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xE,
        "嗯，好的。\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xE,
        (
            "……我当时和男朋友\x01",
            "一起在湖中游玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xE,
        (
            "打了一阵子水中托球，\x01",
            "还练了练游泳。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xD,
        (
            "之后，我动身上岸，\x01",
            "准备去小卖部\x01",
            "买些饮料。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xD,
        (
            "但我刚离开没多久，\x01",
            "就听到了她的尖叫……\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xD,
        (
            "跑回去一看，\x01",
            "只见她的泳装已经被划破，\x01",
            "慌张地蜷缩在水下。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xE,
        (
            "虽说那位救生员先生\x01",
            "急忙替我拿来了毛巾……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xE,
        (
            "但周围的人全都聚过来看，\x01",
            "真是太糟糕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x101,
        "#6P#00003F原来如此……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xC, 500)
    Sleep(500)

    #C0164
    ChrTalk(
        0x101,
        (
            "#12P#00001F救生员先生\x01",
            "什么都没有目击到吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xC,
        (
            "我虽然一直在监视湖面，\x01",
            "但并没有发现可疑情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xC,
        (
            "在我听到尖叫声，\x01",
            "赶往现场的途中，\x01",
            "也没有看到划破泳装的犯人。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xC,
        (
            "骚乱发生之后，\x01",
            "我还询问了周围的客人，\x01",
            "但谁都没有看到犯人。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xE,
        (
            "连我这个受害人\x01",
            "都没有看见犯人呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 500)
    Sleep(500)

    #C0169
    ChrTalk(
        0xE,
        (
            "我男朋友去买饮料之后，\x01",
            "我还下意识地巡视了四周，\x01",
            "但并没有任何人接近……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xE,
        (
            "在泳装被划破的那一瞬间，我太过吃惊，\x01",
            "所以慌慌张张地蜷缩到了水面下。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        (
            "#6P#00006F这……\x01",
            "可以理解。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)

    #C0172
    ChrTalk(
        0x101,
        (
            "#6P#00001F在以前发生的几起划破泳装事件中，\x01",
            "也没有任何目击者吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x8,
        (
            "嗯，和这次一样，\x01",
            "全都发生在岸边，\x01",
            "但没有任何人看到过犯人。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x8,
        (
            "可泳装每次都像是\x01",
            "被利刃一类的东西所划破的，\x01",
            "如果认定为意外事故，恐怕很难解释得通……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xC,
        (
            "另外，由于多起事件\x01",
            "的手法完全一样，\x01",
            "因此犯人应为同一人……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xC,
        (
            "但我们查看了来客名册，并没有发现\x01",
            "在几起事件发生时都在场的客人。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xC,
        (
            "本想将其认定为意外事故，\x01",
            "就此不了了之，\x01",
            "但却再次发生了同样的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        "#12P#00003F原来如此……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    TurnDirection(0x153, 0x101, 500)
    Sleep(500)

    #C0179
    ChrTalk(
        0x153,
        "#12P#01111F罗伊德，你知道犯人是谁了吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x153, 500)
    Sleep(500)

    #C0180
    ChrTalk(
        0xD,
        (
            "喂喂，小姑娘，\x01",
            "那么着急可不行哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xD,
        (
            "就算是警察，\x01",
            "也不可能听了这些\x01",
            "之后就立刻……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x101,
        (
            "#6P#00003F……不，关于犯人的身份，\x01",
            "我已经有了大致眉目。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0xD, 0x101, 500)
    Sleep(500)

    #C0183
    ChrTalk(
        0xD,
        "真、真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x8,
        (
            "不用去现场\x01",
            "调查一下吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x101,
        (
            "#12P#00003F在一般情况下，的确有那个必要……\x01",
            "但现在就算去现场，应该也找不到什么重要证据。\x02\x03",

            "#00001F由于事件现场是岸边，\x01",
            "经过这么久的时间，\x01",
            "线索恐怕早就消失了。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xC,
        "原、原来如此……\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xC,
        (
            "可是……在这种情况下，\x01",
            "你还能想到犯人是谁吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        (
            "#6P#00000F嗯，将各位提供的证言\x01",
            "综合在一起思考之后，\x01",
            "自然可以推测出真正的犯人。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    Sound(822, 0, 100, 0)
    Sleep(1000)

    #C0189
    ChrTalk(
        0x153,
        "#12P#01109F罗伊德好帅啊！\x02",
    )

    CloseMessageWindow()
    OP_64(0x153)

    #C0190
    ChrTalk(
        0xE,
        (
            "那就不要卖关子了，\x01",
            "赶快告诉我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xE,
        (
            "划破我泳装\x01",
            "的犯人……\x01",
            "究竟是谁呢？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 500)
    Sleep(500)

    #C0192
    ChrTalk(
        0x101,
        (
            "#6P#00001F（没有任何目击者，\x01",
            "  几次事件全部\x01",
            "  发生在水边……）\x02\x03",

            "（另外，泳装是被\x01",
            "  利刃般的东西\x01",
            "  划破的。）\x02\x03",

            "#00003F（通过这些情况来考虑，\x01",
            "  犯人恐怕就是……）\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 3)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_52CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54F7")
    Sleep(500)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0193
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K划破泳装的犯人是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        180,
        0,
        (
            "受害者自己\x01",        # 0
            "受害者的男友\x01",      # 1
            "救生员\x01",            # 2
            "其它\x01",              # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53EF")

    #C0194
    ChrTalk(
        0x101,
        (
            "#6P#00003F通过这些情况来考虑，\x01",
            "犯人并不是现在在场的人\x01",
            "或其他客人。\x02\x03",

            "#00001F真正的犯人\x01",
            "恐怕是……\x01",
            "潜藏在湖水浴场的某种『魔兽』。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53EA")
    OP_2C(0x7E, 0x1)

    label("loc_53EA")

    Jump("loc_54F2")

    label("loc_53EF")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0195
    ChrTalk(
        0x101,
        (
            "#6P#00003F（不对，从现有情况来看，\x01",
            "  犯人不可能是这个人。\x01",
            "  ……再重新考虑一下吧。）\x02\x03",

            "#00001F（没有任何目击者，\x01",
            "  几次事件全部\x01",
            "  发生在水边……）\x02\x03",

            "（另外，泳装是被\x01",
            "  利刃般的东西\x01",
            "  划破的。）\x02\x03",

            "#00003F（通过这些情况来考虑，\x01",
            "  犯人恐怕就是……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54F2")

    Jump("loc_52CB")

    label("loc_54F7")

    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0196
    ChrTalk(
        0xD,
        "魔、魔兽……！？\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xD,
        (
            "是魔兽把我女朋友\x01",
            "的泳装划破的！？\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xE,
        (
            "再、再怎么说，\x01",
            "这也太过荒唐了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xE,
        "有根据吗？根据在哪里！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)

    #C0200
    ChrTalk(
        0x101,
        (
            "#12P#00000F我按顺序来说明吧。\x02\x03",

            "#00003F首先来看\x01",
            "被划破的泳装……\x02\x03",

            "#00001F泳装是被利刃般的东西\x01",
            "所划破的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x8,
        (
            "嗯，是的……\x01",
            "以前的几起事件也是一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        (
            "#12P#00000F那么，请问……\x01",
            "像那样的东西，\x01",
            "可以带进这个湖水浴场吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x8,
        (
            "不……\x01",
            "那恐怕很难。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x8,
        (
            "客人要在接待处\x01",
            "接受严密检查……\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xC,
        (
            "嗯，为了确保安全性，\x01",
            "我们这些职员也会随身携带\x01",
            "小型的简易金属探测器。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xC,
        (
            "正因如此，我们才会\x01",
            "百思不得其解，完全想不出\x01",
            "犯人是如何将那种东西带进…………\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xC,
        "…………啊。\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        (
            "#6P#00000F……不错，也就是说……\x01",
            "犯人并没有\x01",
            "『把利刃带进来』。\x02\x03",

            "#00003F而是——\x01",
            "自己的身体上『原本就拥有』\x01",
            "可以划破泳装的武器……\x02\x03",

            "#00001F如果猜得没错……\x01",
            "那应该就是魔兽的锐利尖爪或牙齿之类的了。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xD,
        (
            "这、这就是断定\x01",
            "犯人为魔兽的根据吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        (
            "#6P#00003F不，如果仅有这点依据，\x01",
            "仍然只算是异想天开的臆测。\x02\x03",

            "#00000F不过，与其它要素相结合以后……\x01",
            "这种推测的可能性便大大增强了。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0xE,
        "其它要素……？\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x101,
        (
            "#6P#00001F这次的事件与之前\x01",
            "发生的几起划破泳装事件\x01",
            "有很多共通点。\x02\x03",

            "#00003F没有目击者……\x01",
            "发生地点是在水边……\x01",
            "手法完全一样……\x02\x03",

            "#00001F从这方面来考虑，\x01",
            "几起事件很可能是由同一犯人所为。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x8,
        (
            "是的，可我们在调查\x01",
            "客人名册的时候，\x01",
            "并没有发现每次都在场的客人……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0214
    ChrTalk(
        0x101,
        (
            "#12P#00003F嗯，这就说明……\x01",
            "犯人并不是以正规方式\x01",
            "进入湖水浴场的客人。\x02\x03",

            "#00000F另外，由于有救生员负责监视，\x01",
            "应该也不可能从对岸游至浴场……\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xC,
        (
            "嗯，如果有人企图那样潜入，\x01",
            "我肯定可以发现……\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x101,
        (
            "#6P#00001F所以……\x01",
            "犯人前往事件现场的\x01",
            "途径只有一个。\x02\x03",

            "那就是艾鲁姆湖的水面下……\x01",
            "犯人有可能是栖息在\x01",
            "那里的水生魔兽。\x02\x03",

            "#00003F由于是小型魔兽，\x01",
            "就算在水中游动，救生员也注意不到，\x01",
            "因此可以悄悄接近浴场中的客人。\x02\x03",

            "#00001F反过来说……\x01",
            "除此之外，再也没有其它方法\x01",
            "可以引起此次事件了。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xD,
        (
            "也、也就是说，这起事件\x01",
            "肯定是由魔兽引起的……\x01",
            "是这样吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x8,
        "道理好像说得通呢……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xE)
    Sleep(500)

    #C0219
    ChrTalk(
        0xE,
        (
            "等、等一下，\x01",
            "你们好像忽略了一个重要的问题吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xE,
        (
            "魔兽为什么要\x01",
            "划破女孩子的\x01",
            "泳装呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xC,
        (
            "这、这确实是个疑问啊……\x01",
            "你怎么想？\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xC,
        (
            "看来……\x01",
            "显然还是某个\x01",
            "变态男子做的吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0223
    ChrTalk(
        0x101,
        (
            "#12P#00006F说、说到动机，\x01",
            "终究还是猜测不到……\x02\x03",

            "#00001F但此次事件肯定\x01",
            "是由魔兽引起的，\x01",
            "这个事实并没有改变。\x02\x03",

            "#00003F也就是说，目前我们也只能得出\x01",
            "『某种魔兽拥有那种特殊习性』\x01",
            "这个结论了……\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x8,
        (
            "不过……\x01",
            "这样的话，我们该怎么办才好呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x8,
        (
            "如果真的有魔兽出没，\x01",
            "恐怕会影响到\x01",
            "米修拉姆事业部的声誉。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x8,
        (
            "最好能想个办法，\x01",
            "趁着这个机会将魔兽赶走……\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xC,
        "但对方的行踪神出鬼没。\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xC,
        (
            "如果我们只是一味等待它的出现，\x01",
            "湖水浴场也就无法\x01",
            "正常运营了。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xE,
        (
            "唔……我已经受害过一次了，\x01",
            "如果抓不到凶手，\x01",
            "以后肯定不敢再来玩了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x153)
    Sleep(500)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0230
    ChrTalk(
        0x153,
        (
            "#12P#01100F既然这样……\x01",
            "琪雅就去当诱饵吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_60A8():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_60A8)
    Sleep(100)

    def lambda_60B8():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_60B8)
    Sleep(100)

    def lambda_60C8():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_60C8)
    Sleep(100)

    def lambda_60D8():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_60D8)
    Sleep(100)

    def lambda_60E8():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_60E8)
    Sleep(500)

    #C0231
    ChrTalk(
        0x101,
        "#6P#00011F琪、琪雅，你在说什么啊？\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x153,
        (
            "#12P#01105F那种魔兽不是喜欢\x01",
            "划破女孩子的泳装吗？\x02\x03",

            "#01103F如果我穿上泳装去水边玩，\x01",
            "它说不定还会再次出现呢。\x02\x03",

            "#01109F到了那时，只要有罗伊德\x01",
            "保护我就没问题了。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x101,
        (
            "#6P#00001F那、那个……\x01",
            "但没理由让琪雅\x01",
            "遭受那种危险啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xD,
        "是、是啊，小姑娘。\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xD,
        (
            "虽然犯人至今为止只是划破了泳装，\x01",
            "但谁也猜不到下一次将会怎样。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x153,
        (
            "#12P#01108F嗯，可是……\x01",
            "如果放着魔兽不管，\x01",
            "贝尔会很烦恼吧？\x02\x03",

            "#01106F好想帮她赶走魔兽，\x01",
            "作为接受招待的回报……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x101,
        "#6P#00003F说、说的也对啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0238
    ChrTalk(
        0x101,
        (
            "#6P#00003F……我明白了。\x02\x03",

            "#00001F虽然不敢保证成功，\x01",
            "但现在也只能采用\x01",
            "琪雅的作战方案了。\x02\x03",

            "#00003F不过，不能由琪雅充当诱饵，\x01",
            "还是拜托其他同伴来帮忙吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x153,
        "#12P#01101F嗯！\x02",
    )

    CloseMessageWindow()

    def lambda_63B6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_63B6)
    Sleep(100)

    def lambda_63C6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_63C6)
    Sleep(100)

    def lambda_63D6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_63D6)
    Sleep(100)

    def lambda_63E6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_63E6)
    Sleep(500)

    #C0240
    ChrTalk(
        0x8,
        (
            "这……\x01",
            "真的不要紧吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)

    #C0241
    ChrTalk(
        0x101,
        (
            "#6P#00000F嗯，我们支援科的成员\x01",
            "早已习惯与魔兽战斗了……\x01",
            "我想应该不会有什么问题。\x02\x03",

            "#00003F问题是，要由谁来\x01",
            "充当诱饵角色呢……\x02\x03",

            "#00000F可以担负这个任务的人\x01",
            "也只有艾莉、缇欧和诺艾尔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x153,
        "#12P#01105F罗伊德，要叫谁呢？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)
    Sleep(500)

    #C0243
    ChrTalk(
        0x101,
        "#6P#00003F嗯，这个嘛……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0244
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K拜托谁来担当诱饵？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【艾莉】\x01",        # 0
            "【缇欧】\x01",        # 1
            "【诺艾尔】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_65AE"),
        (1, "loc_65E5"),
        (2, "loc_661C"),
        (SWITCH_DEFAULT, "loc_6655"),
    )


    label("loc_65AE")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x15B, 6)

    #C0245
    ChrTalk(
        0x101,
        "#6P#00000F……去拜托艾莉帮忙吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6655")

    label("loc_65E5")

    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x15B, 7)

    #C0246
    ChrTalk(
        0x101,
        "#6P#00000F……去拜托缇欧帮忙吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6655")

    label("loc_661C")

    OP_50(0x68, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1C4, 5)

    #C0247
    ChrTalk(
        0x101,
        "#6P#00000F……去拜托诺艾尔帮忙吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6655")

    label("loc_6655")


    #C0248
    ChrTalk(
        0x153,
        "#12P#01109F嗯，一定能成功的！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(500)

    #C0249
    ChrTalk(
        0x101,
        (
            "#6P#00003F情况就是这样……\x01",
            "我们现在准备去\x01",
            "湖水浴场驱赶魔兽。\x02\x03",

            "#00000F二位工作人员能否\x01",
            "帮忙疏散客人？\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x8,
        "嗯，明白了。\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xC,
        (
            "我们会以维护检查为由，\x01",
            "请客人们暂时\x01",
            "回避一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xD,
        "你们一定要小心啊～！\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xE,
        (
            "请把划破我泳装的魔兽\x01",
            "狠狠教训一顿！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xE, 500)
    Sleep(500)

    #C0254
    ChrTalk(
        0x101,
        "#6P#00000F嗯，交给我们吧！\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x153,
        "#12P#01109F那就出发吧！！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_67E7")
    AddParty(0x1, 0xEF, 0xFF)
    OP_29(0x7E, 0x1, 0x1)
    Jump("loc_6809")

    label("loc_67E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_67FF")
    AddParty(0x2, 0xEF, 0xFF)
    OP_29(0x7E, 0x1, 0x2)
    Jump("loc_6809")

    label("loc_67FF")

    AddParty(0x8, 0xEF, 0xFF)
    OP_29(0x7E, 0x1, 0x3)

    label("loc_6809")

    SetScenarioFlags(0x22, 3)
    NewScene("t1310", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_45F3 end

    def Function_21_6816(): pass

    label("Function_21_6816")

    EventBegin(0x0)
    OP_68(-1330, 3100, 1380, 0)
    MoveCamera(318, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17150, 0)
    LoadChrToIndex("chr/ch23600.itc", 0x1E)
    LoadChrToIndex("chr/ch48200.itc", 0x1F)
    LoadChrToIndex("chr/ch48300.itc", 0x20)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xC, 0x0)
    SetChrSubChip(0xD, 0x0)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0x101, -3160, 0, 1570, 45)
    SetChrPos(0x153, -2960, 0, -40, 45)
    SetChrPos(0xEF, -4480, 0, 1090, 45)
    SetChrPos(0xC, 490, 0, 1750, 270)
    SetChrPos(0xD, -570, 0, -680, 315)
    SetChrPos(0xE, -390, 0, 320, 315)
    SetChrPos(0x8, -2000, 0, 5150, 180)
    OP_68(-1330, 1600, 1380, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0256
    ChrTalk(
        0x8,
        "各位真是辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x8,
        (
            "多亏你们，米修拉姆事业部\x01",
            "才能保住自身声誉。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x101,
        "#00002F哈哈，能帮上忙，我深感荣幸。\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x8,
        (
            "真是太谢谢你们了。\x01",
            "该如何道谢才好呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x8,
        (
            "我会负责把开发进程\x01",
            "导致魔兽出现的情况\x01",
            "报告给玛丽亚贝尔小姐。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_6A28")

    #C0261
    ChrTalk(
        0x102,
        "#00100F嗯，那就好。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A71")

    label("loc_6A28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_6A4B")

    #C0262
    ChrTalk(
        0x103,
        "#00200F那就好。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6A71")

    label("loc_6A4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_6A71")

    #C0263
    ChrTalk(
        0x109,
        "#10100F嗯，那就拜托啦。\x02",
    )

    CloseMessageWindow()

    label("loc_6A71")


    #C0264
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，玛丽亚贝尔小姐\x01",
            "肯定能想出什么对策吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 500)
    Sleep(500)

    #C0265
    ChrTalk(
        0xE,
        "#12P呵呵，辛苦了⊥\x02",
    )

    CloseMessageWindow()

    def lambda_6AD0():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AD0)
    Sleep(100)

    def lambda_6AE0():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_6AE0)
    Sleep(100)

    def lambda_6AF0():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_6AF0)
    Sleep(100)

    def lambda_6B00():
        TurnDirection(0xFE, 0xE, 500)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_6B00)
    Sleep(500)

    #C0266
    ChrTalk(
        0xE,
        (
            "#12P你们已经把划破泳装\x01",
            "的魔兽赶跑了吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xD, 500)
    Sleep(500)

    #C0267
    ChrTalk(
        0xE,
        (
            "#12P好，既然如此，\x01",
            "我们就回湖水浴场继续玩吧！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xE, 500)
    Sleep(500)

    #C0268
    ChrTalk(
        0xD,
        (
            "#6P哎！？还要去吗！？\x01",
            "本以为你吃过苦头后，不敢再去了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xE,
        (
            "#12P当然要去啊！\x01",
            "难得来一趟，\x01",
            "必须要玩到尽兴才行。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0x101, 500)
    Sleep(500)

    #C0270
    ChrTalk(
        0xE,
        (
            "#12P呵呵，那我们\x01",
            "就先告辞啦。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xE, 3, 0, 22)
    Sleep(500)
    BeginChrThread(0xD, 3, 0, 23)
    Sleep(2000)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(500)
    TurnDirection(0xC, 0x101, 500)
    Sleep(500)

    #C0271
    ChrTalk(
        0xC,
        (
            "#12P好，我也要\x01",
            "回去继续监视了。\x01",
            "这次真是谢谢你们了。\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0xC, 0xB4, 0x1388, 0x7D0, 0x0)
    Sleep(1000)
    OP_68(-3510, 1300, 960, 3000)
    OP_6F(0x1)
    TurnDirection(0x101, 0x153, 500)
    Sleep(500)

    #C0272
    ChrTalk(
        0x101,
        (
            "#00000F好，我们差不多\x01",
            "也该出发了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x153, 0x101, 500)
    Sleep(500)

    #C0273
    ChrTalk(
        0x153,
        "#6P#01100F嗯！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_6D44")

    #C0274
    ChrTalk(
        0x102,
        (
            "#00104F我还想去时装店\x01",
            "再看看。\x02\x03",

            "#00100F呵呵，一会见哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DE8")

    label("loc_6D44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_6DA4")

    #C0275
    ChrTalk(
        0x103,
        (
            "#00204F我先走一步，\x01",
            "去主题公园等你们。\x02\x03",

            "#00202F蔡特和修利\x01",
            "还在那里等着我呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DE8")

    label("loc_6DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_6DE8")

    #C0276
    ChrTalk(
        0x109,
        (
            "#10100F我还想和芙兰\x01",
            "再逛逛珠宝店。\x02\x03",

            "#10109F一会见吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DE8")


    def lambda_6DED():
        TurnDirection(0xFE, 0xEF, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6DED)
    Sleep(200)

    def lambda_6DFD():
        TurnDirection(0xFE, 0xEF, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_6DFD)
    Sleep(500)

    #C0277
    ChrTalk(
        0x101,
        "#00000F嗯，一会见。\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x153,
        "#12P#01109F一会见！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0279
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "任务【调查划破泳装事件】\x07\x00",
            "完成！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x7E, 0x1, 0x4)
    OP_29(0x7E, 0x1, 0x5)
    OP_29(0x7E, 0x4, 0x10)
    OP_32(0xFF, 0xFE, 0x0)
    OP_69(0xFF, 0x0)
    OP_4C(0x8, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_6EB8")
    RemoveParty(0x1, 0xFF)
    Jump("loc_6ED5")

    label("loc_6EB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_6EC9")
    RemoveParty(0x2, 0xFF)
    Jump("loc_6ED5")

    label("loc_6EC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_6ED5")
    RemoveParty(0x8, 0xFF)

    label("loc_6ED5")

    EventEnd(0x5)
    SetScenarioFlags(0x22, 1)
    NewScene("t1020", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_21_6816 end

    def Function_22_6EE4(): pass

    label("Function_22_6EE4")

    OP_95(0xE, 4990, 0, 50, 2000, 0x0)
    OP_95(0xE, 6570, 0, 1030, 2000, 0x0)
    OP_95(0xE, 10000, 0, 1020, 2000, 0x0)
    Return()

    # Function_22_6EE4 end

    def Function_23_6F21(): pass

    label("Function_23_6F21")

    OP_95(0xD, 4990, 0, 50, 2000, 0x0)
    OP_95(0xD, 6570, 0, 1030, 2000, 0x0)
    OP_95(0xD, 10000, 0, 1020, 2000, 0x0)
    Return()

    # Function_23_6F21 end

    def Function_24_6F5E(): pass

    label("Function_24_6F5E")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0280
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门锁着。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_24_6F5E end

    SaveToFile()

Try(main)
