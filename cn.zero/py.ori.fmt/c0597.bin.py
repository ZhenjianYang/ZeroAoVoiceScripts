from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0597.bin",                # FileName
        "c0597",                    # MapName
        "c0597",                    # Location
        0x0029,                     # MapIndex
        "ed7302",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 41, 0, 3, 0, 4],
    )

    BuildStringList((
        "c0597",                  # 0
        "黑手党",                 # 1
        "黑手党",                 # 2
        "黑手党",                 # 3
        "黑手党",                 # 4
        "黑手党",                 # 5
        "加尔西亚",               # 6
        "马尔克尼会长",           # 7
        "红色电磁傲武者",         # 8
        "支援野战机",             # 9
        "支援野战机",             # 10
        "兰迪",                   # 11
        "艾莉",                   # 12
        "缇欧",                   # 13
        "达德利搜查官",           # 14
        "bc0510",                 # 15
    ))

    ATBonus("ATBonus_38C", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_44C", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_450", 5, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_454", 11, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_45C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_460", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_464", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_468", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_42C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_430", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_434", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_438", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_43C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_440", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_444", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_448", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_46C", 0x0012, 34, 6, 180, 0, 0, 0, 0, "bc0510", 0x00000000, 100, 0, 0, 0,
        (
            ("ms68200.dat", "ms68300.dat", "ms68300.dat", 0, 0, 0, "ms68300.dat", 0, "MonsterBattlePostion_44C", "MonsterBattlePostion_42C", "ed7402", "ed7403", "ATBonus_38C"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00300.itc",                   # 00
        "chr/ch00100.itc",                   # 01
        "chr/ch00200.itc",                   # 02
        "chr/ch00900.itc",                   # 03
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
        "monster/ch68250.itc",               # 10
        "monster/ch68251.itc",               # 11
        "monster/ch68350.itc",               # 12
        "monster/ch68350.itc",               # 13
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
    DeclNpc(-6599,   0,       112099,  0,    389,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(4000,    0,       106000,  90,   389,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-3019,   29,      111360,  90,   389,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(6699,    0,       101599,  90,   389,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)

    DeclEvent(0x0000, 0, 13,  0.0,                   48.0,                  -1.0,                  225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -16.0,                 0.20000000298023224,   1.0])

    DeclActor(0,       0,       114800,  1200,    0,       1100,    116500,  0x007C, 0,  6,  0x0000)
    DeclActor(7700,    0,       113500,  1200,    7700,    1500,    113500,  0x007C, 0,  17, 0x0000)
    DeclActor(6000,    0,       6000,    1200,    6000,    1500,    6000,    0x007C, 0,  5,  0x0000)
    DeclActor(0,       0,       64000,   1200,    0,       1500,    64000,   0x007C, 0,  20, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3

    ScpFunction((
        "Function_0_538",          # 00, 0
        "Function_1_5F0",          # 01, 1
        "Function_2_60F",          # 02, 2
        "Function_3_62B",          # 03, 3
        "Function_4_67D",          # 04, 4
        "Function_5_716",          # 05, 5
        "Function_6_809",          # 06, 6
        "Function_7_9C6",          # 07, 7
        "Function_8_ADA",          # 08, 8
        "Function_9_C53",          # 09, 9
        "Function_10_DE4",         # 0A, 10
        "Function_11_F09",         # 0B, 11
        "Function_12_1AF6",        # 0C, 12
        "Function_13_23E8",        # 0D, 13
        "Function_14_2F1F",        # 0E, 14
        "Function_15_3334",        # 0F, 15
        "Function_16_3B07",        # 10, 16
        "Function_17_3B5C",        # 11, 17
        "Function_18_3B9C",        # 12, 18
        "Function_19_3D68",        # 13, 19
        "Function_20_58F6",        # 14, 20
        "Function_21_5C46",        # 15, 21
    ))


    def Function_0_538(): pass

    label("Function_0_538")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_578"),
        (1, "loc_584"),
        (2, "loc_590"),
        (3, "loc_59C"),
        (4, "loc_5A8"),
        (5, "loc_5B4"),
        (6, "loc_5C0"),
        (SWITCH_DEFAULT, "loc_5CC"),
    )


    label("loc_578")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_5D8")

    label("loc_584")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_5D8")

    label("loc_590")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_5D8")

    label("loc_59C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_5D8")

    label("loc_5A8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_5D8")

    label("loc_5B4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_5D8")

    label("loc_5C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5D8")

    label("loc_5CC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5D8")

    label("loc_5D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5EF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_5D8")

    label("loc_5EF")

    Return()

    # Function_0_538 end

    def Function_1_5F0(): pass

    label("Function_1_5F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_60E")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_5F0")

    label("loc_60E")

    Return()

    # Function_1_5F0 end

    def Function_2_60F(): pass

    label("Function_2_60F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_62A")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_2_60F")

    label("loc_62A")

    Return()

    # Function_2_60F end

    def Function_3_62B(): pass

    label("Function_3_62B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_645")
    Event(0, 15)

    label("loc_645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_659")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 11)
    Jump("loc_67C")

    label("loc_659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_66D")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 12)
    Jump("loc_67C")

    label("loc_66D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_67C")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 14)

    label("loc_67C")

    Return()

    # Function_3_62B end

    def Function_4_67D(): pass

    label("Function_4_67D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 0)), scpexpr(EXPR_END)), "loc_692")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x5F, 0)

    label("loc_692")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6AA")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_6AA")

    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6C8")
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)

    label("loc_6C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6D5")
    OP_70(0x11, 0xA)

    label("loc_6D5")

    SetMapObjFlags(0x13, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_6F3")
    OP_65(0x3, 0x1)
    SetMapObjFlags(0x10, 0x10)
    Jump("loc_6FD")

    label("loc_6F3")

    OP_66(0x3, 0x1)
    ClearMapObjFlags(0x10, 0x10)

    label("loc_6FD")

    OP_1B(0x2, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_715")
    OP_1B(0x2, 0x0, 0x15)

    label("loc_715")

    Return()

    # Function_4_67D end

    def Function_5_716(): pass

    label("Function_5_716")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有恢复导力的装置。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7EB")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x12, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x12, 0x0)
    OP_71(0x12, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x12)
    OP_71(0x12, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x12, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_7EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_807")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_807")

    Return()

    # Function_5_716 end

    def Function_6_809(): pass

    label("Function_6_809")

    EventBegin(0x0)
    Fade(1000)
    OP_68(0, 1000, 116100, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 0, 0, 115100, 0)
    OP_0D()
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱被牢牢锁了起来。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8F8")
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "使用宝箱钥匙\x01",      # 0
            "放弃\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8D3"),
        (1, "loc_8DB"),
        (SWITCH_DEFAULT, "loc_8F3"),
    )


    label("loc_8D3")

    Call(0, 19)
    Jump("loc_8F3")

    label("loc_8DB")

    SetChrPos(0x0, 0, 0, 114700, 180)
    EventEnd(0x5)
    Jump("loc_8F3")

    label("loc_8F3")

    Jump("loc_9C5")

    label("loc_8F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_945")

    #C0003
    ChrTalk(
        0x101,
        (
            "#0001F#11P（需要钥匙才能打开啊……\x01",
            "  先调查一下房间吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AC")

    label("loc_945")


    #C0004
    ChrTalk(
        0x101,
        (
            "#0003F#11P（看来很难用\x01",
            "  开锁道具打开呢。）\x02\x03",

            "#0000F（既然如此……\x01",
            "  就在房间中找一找钥匙吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_9AC")

    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 114700, 180)
    SetScenarioFlags(0xC6, 3)
    EventEnd(0x5)

    label("loc_9C5")

    Return()

    # Function_6_809 end

    def Function_7_9C6(): pass

    label("Function_7_9C6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A3C")

    #C0005
    ChrTalk(
        0xFE,
        (
            "#0306F从莱恩福尔特到乌尔努，\x01",
            "买的都是最新型的武器啊……\x02\x03",

            "#0301F这家伙到底拥有\x01",
            "多少财产啊！？\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    Jump("loc_AD6")

    label("loc_A3C")


    #C0006
    ChrTalk(
        0xFE,
        (
            "#0308F这里有关于武器\x01",
            "走私渠道的文件……\x02\x03",

            "#0303F连我所知道的渠道，\x01",
            "也基本都网罗在其中了……\x02\x03",

            "#0300F应该都是加尔西亚大叔\x01",
            "在猎兵时期积累下的人脉吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_AD6")

    TalkEnd(0xFE)
    Return()

    # Function_7_9C6 end

    def Function_8_ADA(): pass

    label("Function_8_ADA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_B5E")

    #C0007
    ChrTalk(
        0x13,
        (
            "#0105F这边也有今年的目录，\x01",
            "不过业绩似乎不怎么样呢……\x02\x03",

            "#0106F好像有点下滑的感觉，\x01",
            "算了，这也是自作自受啊。\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 1)
    Jump("loc_C4F")

    label("loc_B5E")


    #C0008
    ChrTalk(
        0x13,
        (
            "#0108F有那个『黑之竞拍会』的\x01",
            "目录清单呢……\x02\x03",

            "里面详细记录着商品的进货渠道\x01",
            "与得标者的情报……\x02\x03",

            "#0106F真没想到，连传闻被『怪盗Ｂ』\x01",
            "盗走的那副稀世名画也在其中……\x02\x03",

            "#0101F如果将这份清单公开于世的话，\x01",
            "周边诸国恐怕也会陷入巨大的骚乱吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_C4F")

    TalkEnd(0xFE)
    Return()

    # Function_8_ADA end

    def Function_9_C53(): pass

    label("Function_9_C53")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_CF4")

    #C0009
    ChrTalk(
        0x14,
        (
            "#0205F啊，在最近的记录上，\x01",
            "似乎还有警察局长和共和国派\x01",
            "议员的名字呢。\x02\x03",

            "#0206F这样看来，一科会被施加如此大的压力，\x01",
            "可以说是理所当然的吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 2)
    Jump("loc_DE0")

    label("loc_CF4")


    #C0010
    ChrTalk(
        0x14,
        (
            "#0208F这里还有向克洛斯贝尔财政界\x01",
            "人士行贿的详细记录呢。\x02\x03",

            "#0203F不仅是那位议长先生，\x01",
            "帝国派议员、局长级的政府官员，\x01",
            "连警备队的司令都包括在内吗……\x02\x03",

            "#0211F此外，由于用暴力解决了很多\x01",
            "纠纷，因此还从不少企业那里\x01",
            "收取了大额的谢礼呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_DE0")

    TalkEnd(0xFE)
    Return()

    # Function_9_C53 end

    def Function_10_DE4(): pass

    label("Function_10_DE4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_E54")

    #C0011
    ChrTalk(
        0xFE,
        (
            "#0603F这里记录的是\x01",
            "与走私有关的证据……\x02\x03",

            "#0610F哼……\x01",
            "可恶，要是有正式搜查令的话……！\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 3)
    Jump("loc_F05")

    label("loc_E54")


    #C0012
    ChrTalk(
        0xFE,
        (
            "#0608F这些都是和走私\x01",
            "相关的文件啊……\x02\x03",

            "#0606F虽然我们已经大致摸清状况了，\x01",
            "但没想到规模竟然如此庞大……\x02\x03",

            "#0610F哼，要是有正式搜查令的话，\x01",
            "绝对能判他们个\x01",
            "一百年监禁……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_F05")

    TalkEnd(0xFE)
    Return()

    # Function_10_DE4 end

    def Function_11_F09(): pass

    label("Function_11_F09")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31000.itc", 0x1E)
    LoadChrToIndex("chr/ch31100.itc", 0x1F)
    LoadChrToIndex("chr/ch02200.itc", 0x20)
    LoadChrToIndex("chr/ch06202.itc", 0x21)
    OP_68(150, 930, 108140, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(26500, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -1800, 30, 106500, 45)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, -2700, 30, 108400, 90)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, -3000, 20, 107100, 90)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, -1700, 30, 105400, 45)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0xB, -1500, 30, 108200, 90)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, 900, 30, 108000, 270)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xE, 0x21)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrPos(0xE, -200, 100, 112500, 180)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03100.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03000.itp")
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("豪气的声音")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            "你们几个……\x01",
            "居然还有脸回来吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(24500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("穿西装的巨汉")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            "为了把你们保释出来，\x01",
            "你们知道我一共花了多少米拉吗……\x02\x03",

            "想疏通那群议员们，\x01",
            "代价可不小啊……\x02",
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

    #C0015
    ChrTalk(
        0xB,
        "#6P对、对不起，副头目……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xA,
        (
            "#6P我们怎么也没有想到，\x01",
            "在那种地方竟然会有警察……\x02",
        )
    )

    CloseMessageWindow()

    #N0017
    NpcTalk(
        0xD,
        "穿西装的巨汉",
        (
            "#11P#3103F哼……\x01",
            "是叫『特别任务支援科』吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0xE1, 0x1F4)
    Sleep(300)

    #N0018
    NpcTalk(
        0xD,
        "穿西装的巨汉",
        (
            "#5P#3100F──法比奥，莫兰。\x02\x03",

            "让你们吃了苦头的\x01",
            "也是那些小鬼吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        "#6P是、是的……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x9,
        (
            "#12P那个……还要加上旧城区的\x01",
            "那些臭小子……\x02",
        )
    )

    CloseMessageWindow()

    #N0021
    NpcTalk(
        0xD,
        "穿西装的巨汉",
        (
            "#5P#3104F哈，听你这么说，对方根本就是\x01",
            "由女人和小鬼凑成的菜鸟集团啊。\x02\x03",

            "#3100F竟然输给那种小鬼头……\x01",
            "身为专业人士，难道不觉得丢脸吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        "#6P是、是的！！\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x9,
        (
            "#12P这笔账……\x01",
            "一定会让他们加倍奉还的！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xB,
        (
            "#6P听说那些臭小鬼\x01",
            "以中央广场边缘的那栋破楼\x01",
            "为据点……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xC,
        (
            "#6P只要您下达指示，\x01",
            "我们随时都可以打进去……！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xD, 0x10E, 0x1F4)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #N0026
    NpcTalk(
        0xD,
        "穿西装的巨汉",
        "#11P#3107F#4S白痴！\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xB,
        "#6P呜……\x02",
    )

    CloseMessageWindow()

    #N0028
    NpcTalk(
        0xD,
        "穿西装的巨汉",
        (
            "#11P#3107F警察局的臭小鬼们成不了\x01",
            "什么大事！没必要去管他们！\x02\x03",

            "我们必须要击溃的\x01",
            "真正对手是『黑月』……\x02\x03",

            "那些让人火大的，\x01",
            "从东方人街跑出来的杂碎啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xC,
        "#6P可、可是……\x02",
    )

    CloseMessageWindow()

    #N0030
    NpcTalk(
        0xE,
        "发福的男人",
        (
            "#3004F#1P──算了算了，加尔西亚。\x01",
            "我们也不需要那么仓促行事。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_15E5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_15E5)
    WaitChrThread(0xD, 2)

    def lambda_15F6():
        OP_96(0xFE, 0x12C, 0x1E, 0x1A900, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_15F6)
    OP_68(-200, 930, 110500, 2000)
    Sleep(50)

    def lambda_1624():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1624)

    def lambda_1631():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1631)
    Sleep(50)

    def lambda_1641():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1641)

    def lambda_164E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_164E)
    Sleep(50)

    def lambda_165E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_165E)
    WaitChrThread(0xD, 1)
    OP_6F(0x1)

    #C0031
    ChrTalk(
        0xD,
        "#2P#3101F会长，可是……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0032
    AnonymousTalk(
        0xE,
        (
            "就在前几天，因为那些家伙的缘故，\x01",
            "我们失去了一条共和国方面\x01",
            "的进货渠道。\x02\x03",

            "但是别忘了，在我们的背后，\x01",
            "还有哈尔特曼议长这座大靠山。\x02\x03",

            "在克洛斯贝尔地区，\x01",
            "我们仍然拥有他们无法撼动的绝对优势。\x02",
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

    #C0033
    ChrTalk(
        0xD,
        (
            "#2P#3107F但是……\x01",
            "只有『那个男人』是非常危险的！\x02\x03",

            "那个身穿黑衣的男人，唯独他，绝不能掉以轻心……！\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xE,
        (
            "#3002F#5P呵呵……\x01",
            "是指那个把你戏耍了一番的杀手吗？\x02\x03",

            "能与身经百战的原猎兵抗衡，\x01",
            "看来确实是拥有相当强的实力啊。\x02\x03",

            "曹那家伙，想必砸进去了不少钱吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xD,
        "#2P#3101F会、会长……！\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xE,
        (
            "#3004F#5P算了，不用那么担心，\x01",
            "我已经制定了对付『黑月』的策略。\x02\x03",

            "军犬也基本上都安排好了，\x01",
            "今后应该不会再输给他们了吧。\x02\x03",

            "#3001F──比起这些，\x01",
            "更重要的是下个月的『竞拍会』。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0037
    ChrTalk(
        0xD,
        "#2P#3103F是的，我很清楚。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xE,
        (
            "#3003F#5P不管那些家伙有多么猖狂，\x01",
            "也绝不能让他们来扰乱\x01",
            "今年的『竞拍会』……\x02\x03",

            "#3001F警察和协会那边就先别去理会了，\x01",
            "反正这两方也都成不了什么气候。\x02\x03",

            "真正需要提防的还是『黑月』……\x01",
            "必须要制定好万无一失的防备体制，\x01",
            "让那些杀手之流没有任何可乘之机！\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xD,
        "#2P#3101F遵命……！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(25000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c0420", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_F09 end

    def Function_12_1AF6(): pass

    label("Function_12_1AF6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch31000.itc", 0x1E)
    LoadChrToIndex("chr/ch31100.itc", 0x1F)
    LoadChrToIndex("chr/ch02200.itc", 0x20)
    LoadChrToIndex("chr/ch06202.itc", 0x21)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis159.itp")
    OP_68(-200, 1530, 110500, 0)
    MoveCamera(37, 19, 0, 0)
    OP_6E(420, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, -1500, 20, 108400, 0)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 700, 20, 108400, 0)
    SetChrChipByIndex(0xD, 0x20)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, -200, 30, 108900, 0)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xE, 0x21)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrPos(0xE, -200, 100, 112500, 180)
    Sound(818, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("男性的声音")

    #A0040
    AnonymousTalk(
        0xFF,
        "#4S真是的，竟会如此失态！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-200, 1030, 110500, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0041
    ChrTalk(
        0xE,
        (
            "#5P#3007F竟然会沦落到跟区区警察\x01",
            "和谈休战的地步……！\x02\x03",

            "真可恶……\x01",
            "都怪你们太没用了！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xD,
        "#11P#3103F……我无可辩驳。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "#6P但、但是，那个人偶\x01",
            "是会长您亲自……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xE,
        "#5P#3001F什么……？\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xD,
        (
            "#3103F#11P……闭嘴。\x02\x03",

            "#3101F不管怎么说，把那些入侵者\x01",
            "放进来的责任都在我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        "#6P是、是的……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xE,
        (
            "#5P#3001F哼……\x02\x03",

            "#3003F自从那件事发生之后，连哈尔特曼议长\x01",
            "都刻意回避与我们联络……\x02\x03",

            "据说连『黑月』那边都要\x01",
            "发起正式进攻了！\x02\x03",

            "可恶……再这么下去的话……！\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xD,
        (
            "#11P#3104F会长，请您放心。\x02\x03",

            "#3100F目前，我们在克洛斯贝尔\x01",
            "的绝对优势仍然是不可动摇的。\x02\x03",

            "如果我们能想办法撑过\x01",
            "『黑月』的攻势，议长也会……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)

    #C0049
    ChrTalk(
        0xE,
        (
            "#5P#3007F哼，问题是谁能保证我们\x01",
            "一定能撑过他们的攻击呢！？\x02\x03",

            "直到现在，你们也没能把那个叫『银』的\x01",
            "家伙的首级取来啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xD,
        "#11P#3103F那个……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xE,
        (
            "#5P#3001F哼，近期恐怕也\x01",
            "指望不上议长的支援了……\x02\x03",

            "#3003F……可恶，到底该怎么办……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xE)
    Sleep(500)

    #C0052
    ChrTalk(
        0xE,
        (
            "#5P#3004F事到如今，只能不择手段了……\x02\x03",

            "#3002F我决定了──打出我们的王牌吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0053
    ChrTalk(
        0x9,
        "#12P王牌……！？\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        "#6P难、难道说……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xD,
        "#11P#3105F会长，您是说……！\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xE,
        (
            "#5P#3002F哼哼……这有什么好惊讶的？\x02\x03",

            "正是为了应对这种状况，\x01",
            "才应该使用这项最终手段啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xD,
        (
            "#11P#3107F可、可是……\x01",
            "风险终究是太高了啊！\x02\x03",

            "警察那边暂且不说，被协会\x01",
            "察觉到的危险性可无法……！\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xE,
        (
            "#5P#3004F哼哼，在那之前，\x01",
            "只要先把『黑月』彻底击溃就好了。\x02\x03",

            "以前准备的流通网络，也趁此\x01",
            "试用一下吧，这可是难得的机会啊。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(22000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0059
    AnonymousTalk(
        0xE,
        (
            "#3002F克洛斯贝尔黑道势力的霸权──\x01",
            "绝对不会让给外人！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x48, 0x4, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x25, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A0")
    OP_29(0x25, 0x4, 0x40)

    label("loc_22A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22BE")
    OP_29(0x26, 0x4, 0x40)
    Jump("loc_22D0")

    label("loc_22BE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x26, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22D0")
    OP_29(0x26, 0x4, 0x40)

    label("loc_22D0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22EE")
    OP_29(0x27, 0x4, 0x40)
    Jump("loc_2300")

    label("loc_22EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x27, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2300")
    OP_29(0x27, 0x4, 0x40)

    label("loc_2300")

    SubItemNumber('ＺＷＥＩ２企鹅', 1)
    Sleep(1000)
    StopBGM(0x1388)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7000", "ed7000")
    OP_E3(0xA)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E3(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C7(0x0, 0x10)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5F, 0)
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x9A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x5F, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_C7(0x1, 0x10)
    OP_E3(0xB)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5D, 1)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1AF6 end

    def Function_13_23E8(): pass

    label("Function_13_23E8")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00950.itc", 0x22)
    LoadChrToIndex("monster/ch68250.itc", 0x23)
    LoadChrToIndex("monster/ch68252.itc", 0x24)
    LoadChrToIndex("monster/ch68350.itc", 0x25)
    LoadEffect(0x0, "event\\ev502_00.eff")
    OP_68(0, 1130, 51000, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 0, 30, 48000, 0)
    SetChrPos(0x102, -100, 30, 46300, 0)
    SetChrPos(0x104, 900, 30, 45800, 0)
    SetChrPos(0x103, -1200, 30, 46500, 0)
    SetChrPos(0x10A, 1300, 30, 47800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xF, 0xFF)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x2)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x25)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x25)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)

    def lambda_250C():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_250C)

    def lambda_2526():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2526)
    Sleep(50)

    def lambda_2543():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2543)

    def lambda_255D():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_255D)
    Sleep(50)

    def lambda_257A():
        OP_98(0xFE, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_257A)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(0, 1130, 62000, 2000)
    OP_6F(0x1)

    #C0060
    ChrTalk(
        0x101,
        (
            "#0005F难道说，这里就是\x01",
            "马尔克尼会长的房间……？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x104,
        (
            "#0300F从这种奢华无度的外观来看，\x01",
            "应该没错吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(740, 1130, 51250, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19360, 0)
    OP_0D()
    Sleep(300)

    #C0062
    ChrTalk(
        0x10A,
        (
            "#0603F#11P……总之，我们进去吧。\x02\x03",

            "#0601F差不多也该能找到那些家伙\x01",
            "消失的线索了──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(943, 0, 100, 0)
    SetMessageWindowPos(30, 20, -1, -1)
    SetChrName("语音")

    #A0063
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#40WＰＰＰＰＰ……\x01",
            "感知到未注册的入侵者……\x02",
        )
    )

    CloseMessageWindow()

    #A0064
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "解除待命模式……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xBB8)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0065
    ChrTalk(
        0x10A,
        "#0605F#11P！？\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x103,
        "#12P#0201F大家，都退后！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(0, 2430, 55000, 0)
    MoveCamera(25, 25, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(14500, 0)
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0xF, 0x100)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrPos(0xF, 0, 1000, 55000, 180)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    MoveCamera(45, 21, 0, 3500)
    SetCameraDistance(15500, 3500)
    OP_82(0xC8, 0xC8, 0xBB8, 0xBB8)
    PlayEffect(0x0, 0x0, 0xF, 0x40, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(946, 0, 100, 0)
    Sleep(2000)

    def lambda_2905():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_2905)
    Sound(202, 0, 100, 0)
    WaitChrThread(0xF, 2)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)
    OP_68(0, 1430, 55000, 300)

    def lambda_2939():
        OP_9D(0xFE, 0x0, 0x0, 0xD6D8, 0xA, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2939)

    def lambda_2956():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2956)
    Sleep(50)

    def lambda_2973():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2973)
    Sleep(50)

    def lambda_2990():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2990)
    Sleep(50)

    def lambda_29AD():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_29AD)
    Sleep(50)

    def lambda_29CA():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFC18, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_29CA)
    WaitChrThread(0xF, 1)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(19500, 1500)
    OP_82(0x0, 0x2BC, 0xBB8, 0x5DC)
    Sound(813, 0, 80, 0)
    Sound(944, 0, 100, 0)
    OP_6F(0x10)
    Sleep(500)
    Fade(500)
    OP_68(0, 1430, 51300, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    CancelBlur(0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x10A, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    #C0067
    ChrTalk(
        0x101,
        "#0011F#12P什么——！？\x02",
    )

    CloseMessageWindow()
    OP_64(0x101)

    #C0068
    ChrTalk(
        0x102,
        "#0105F#12P这、这是……！？\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#0307F#12P是那些破铜烂铁\x01",
            "的老大吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(945, 0, 100, 0)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    BeginChrThread(0xF, 3, 0, 1)
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sound(943, 0, 100, 0)
    SetMessageWindowPos(30, 70, -1, -1)
    SetChrName("语音")

    #A0070
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "切换到攻击模式……\x02",
        )
    )

    CloseMessageWindow()

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "目标人数五名……\x01",
            "已经确认对方的武装……\x02",
        )
    )

    CloseMessageWindow()

    #A0072
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "展开『野马模式』……\x01",
            "开始进行迎击……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_52(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x10, 2600, 0, 53500, 180)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    BeginChrThread(0x10, 3, 0, 2)
    OP_52(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x11, -2600, 0, 53500, 180)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    BeginChrThread(0x11, 3, 0, 2)
    OP_82(0x96, 0x96, 0xBB8, 0xBB8)
    PlayEffect(0x0, 0x0, 0x10, 0x40, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x11, 0x40, 0, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sound(946, 0, 100, 0)
    Sleep(2000)

    def lambda_2CB3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2CB3)

    def lambda_2CC4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_2CC4)
    Sound(202, 0, 100, 0)
    Sleep(1000)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    Sleep(300)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    WaitChrThread(0x10, 2)
    WaitChrThread(0x11, 2)

    #C0073
    ChrTalk(
        0x103,
        "#0207F#12P#N是远程操纵的攻击装置……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0074
    ChrTalk(
        0x10A,
        (
            "#0607F#12P你们几个，都拿出干劲来！\x02\x03",

            "大家齐心协力，\x01",
            "把这个大家伙收拾掉！\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        "#0007F#12P是！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0xF, 0x3)
    Fade(250)
    Sound(945, 0, 100, 0)
    SetChrChipByIndex(0xF, 0x24)
    SetChrSubChip(0xF, 0x1)
    OP_52(0xF, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sleep(300)

    def lambda_2E88():
        OP_A6(0xFE, 0x32, 0x0, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_2E88)
    WaitChrThread(0xF, 2)
    SetChrFlags(0xF, 0x20)
    Sound(947, 0, 100, 0)
    BlurSwitch(0x15E, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    MoveCamera(30, 15, 0, 350)
    SetCameraDistance(14500, 350)

    def lambda_2ED6():
        OP_96(0xFE, 0x0, 0x0, 0xB798, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_2ED6)
    Sleep(50)
    SetChrSubChip(0xF, 0x2)
    Sleep(300)
    Battle("BattleInfo_46C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0xF, 0xFF)
    EndChrThread(0x10, 0xFF)
    EndChrThread(0x11, 0xFF)
    Call(0, 14)
    Return()

    # Function_13_23E8 end

    def Function_14_2F1F(): pass

    label("Function_14_2F1F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00056.itc", 0x1E)
    LoadChrToIndex("chr/ch00156.itc", 0x1F)
    LoadChrToIndex("chr/ch00256.itc", 0x20)
    LoadChrToIndex("chr/ch00356.itc", 0x21)
    LoadChrToIndex("chr/ch00953.itc", 0x22)
    LoadChrToIndex("monster/ch68250.itc", 0x23)
    LoadChrToIndex("monster/ch68252.itc", 0x24)
    LoadChrToIndex("monster/ch68350.itc", 0x25)
    OP_68(440, 1130, 51170, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19330, 0)
    SetChrPos(0x101, 0, 30, 51000, 0)
    SetChrPos(0x102, -100, 30, 49300, 0)
    SetChrPos(0x104, 900, 30, 48800, 0)
    SetChrPos(0x103, -1200, 30, 49500, 0)
    SetChrPos(0x10A, 1300, 30, 50800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x3)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    OP_68(440, 1130, 50170, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0076
    ChrTalk(
        0x101,
        (
            "#0006F#5P呼、呼……\x01",
            "真是个相当难对付的家伙啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x104,
        (
            "#0306F#11P唉……话说他们之前为什么不用\x01",
            "这个东西去对付『黑月』呢，\x01",
            "实在是难以理解……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x103,
        (
            "#6P#0206F有可能……是因为\x01",
            "控制难度太高了吧……\x02\x03",

            "#0211F如果没有专业的技术人员进行操作，\x01",
            "它很有可能会失控的……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x102,
        (
            "#12P#0106F要是让它跑到市区，\x01",
            "可就难以收场了……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x10A,
        "#11P#0606F嗯，完全没错……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    TurnDirection(0x10A, 0x101, 400)

    #C0081
    ChrTalk(
        0x10A,
        (
            "#11P#0603F好了……\x01",
            "我们已经突破了最后的障碍。\x02\x03",

            "#0601F这就去房间里面调查吧……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3252():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3252)
    Sleep(150)

    def lambda_3262():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3262)
    Sleep(50)
    TurnDirection(0x102, 0x10A, 500)

    #C0082
    ChrTalk(
        0x101,
        "#6P#0000F是……！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_37()
    OP_68(0, 1280, 51000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x0, 0, 30, 51000, 0)
    SetChrPos(0x1, 0, 30, 51000, 0)
    SetChrPos(0x2, 0, 30, 51000, 0)
    SetChrPos(0x3, 0, 30, 51000, 0)
    ModifyEventFlags(0, 0, 0x80)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xC6, 1)
    OP_E0(0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_14_2F1F end

    def Function_15_3334(): pass

    label("Function_15_3334")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 1100, 111500, 0)
    MoveCamera(47, 30, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 300, 0, 99000, 0)
    SetChrPos(0x102, -500, 0, 99000, 0)
    SetChrPos(0x104, -500, 0, 99000, 0)
    SetChrPos(0x103, 300, 0, 99000, 0)
    SetChrPos(0x10A, 800, 0, 99000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1100, 104500, 6000)
    MoveCamera(27, 17, 0, 6000)
    SetCameraDistance(19500, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_343B():
        OP_96(0xFE, 0x1F4, 0x0, 0x1912C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_343B)

    def lambda_3455():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3455)
    Sleep(500)
    BeginChrThread(0x10A, 3, 0, 16)
    Sleep(500)

    def lambda_3472():
        OP_96(0xFE, 0xFFFFFD44, 0x0, 0x1912C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3472)

    def lambda_348C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_348C)
    Sleep(500)

    def lambda_34A0():
        OP_96(0xFE, 0x1F4, 0x0, 0x18B50, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_34A0)

    def lambda_34BA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_34BA)
    Sleep(500)

    def lambda_34CE():
        OP_96(0xFE, 0xFFFFFD44, 0x0, 0x18B50, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_34CE)

    def lambda_34E8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_34E8)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x10A, 3)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    Fade(1000)
    OP_68(780, 1000, 102610, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(17950, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3598")

    #C0083
    ChrTalk(
        0x102,
        (
            "#6P#0101F好豪华的房间啊……\x02\x03",

            "#0103F虽然还比不上哈尔特曼议长\x01",
            "的房间……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3669")

    label("loc_3598")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_360B")

    #C0084
    ChrTalk(
        0x103,
        (
            "#12P#0201F看起来，好像是个装潢得很奢侈的房间呢……\x02\x03",

            "#0203F不过，终究还是比不上议长先生\x01",
            "的房间。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3669")

    label("loc_360B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3669")

    #C0085
    ChrTalk(
        0x104,
        (
            "#6P#0302F嘿……\x01",
            "好豪华的房间啊。\x02\x03",

            "#0309F不过，毕竟还是比不上那个议长\x01",
            "的房间啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3669")


    #C0086
    ChrTalk(
        0x101,
        (
            "#11P#0012F哈，跟那个比就太勉强啦。\x02\x03",

            "#0011F啊……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x104, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_36EE():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_36EE)

    def lambda_36FB():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_36FB)

    def lambda_3708():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3708)

    def lambda_3715():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3715)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_3774")

    #C0087
    ChrTalk(
        0x102,
        "#6P#0108F啊……\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x104,
        "#6P#0306F大小姐……说漏嘴了吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_37FF")

    label("loc_3774")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_37B9")

    #C0089
    ChrTalk(
        0x103,
        "#12P#0205F啊。\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x104,
        "#6P#0306F阿缇……说漏嘴了吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_37FF")

    label("loc_37B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_37FF")

    #C0091
    ChrTalk(
        0x104,
        "#6P#0305F不好……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x103,
        "#12P#0211F兰迪前辈……说漏嘴了。\x02",
    )

    CloseMessageWindow()

    label("loc_37FF")

    OP_93(0x10A, 0x10E, 0x1F4)
    Sleep(300)

    #C0093
    ChrTalk(
        0x10A,
        (
            "#11P#0604F哼……\x01",
            "事到如今，还有什么好掩饰的。\x02\x03",

            "#0602F关于『黑之竞拍会』事件的详细经过，\x01",
            "我们早已经掌握了。\x02\x03",

            "对一科来说，\x01",
            "感觉就像是长年紧盯着的猎物\x01",
            "被人从旁夺走了一样啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#0012F#6P哈哈……\x02\x03",

            "#0003F先、先不管那个了，\x01",
            "总之，这里应该就是会长室了吧。\x02\x03",

            "#0001F看样子，我们已经把鲁巴彻商会内部\x01",
            "整个调查过一遍了……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x10A,
        (
            "#11P#0608F是啊……结果连一个\x01",
            "黑手党都没看到，\x01",
            "失踪的人似乎也不在这里。\x02\x03",

            "#0603F如果说，还留有什么线索的话，\x01",
            "那也只会是在这个房间里了……\x02\x03",

            "#0601F时间宝贵──\x01",
            "大家分头调查吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        "#0013F#6P是！\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x102,
        (
            "#3P#0103F#6P似乎能找到\x01",
            "各种各样的东西呢……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    RemoveParty(0x9, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    OP_68(0, 1200, 101500, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x0, 0, 0, 101500, 0)
    SetMapFlags(0x2000)
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    SetScenarioFlags(0xC6, 2)
    OP_29(0x4C, 0x1, 0x1A)
    OP_1B(0x2, 0x0, 0x15)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_15_3334 end

    def Function_16_3B07(): pass

    label("Function_16_3B07")


    def lambda_3B0C():
        OP_96(0xFE, 0x320, 0x0, 0x18A88, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3B0C)

    def lambda_3B26():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_3B26)
    WaitChrThread(0x10A, 1)

    def lambda_3B3B():
        OP_95(0xFE, 2000, 0, 102400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3B3B)
    WaitChrThread(0x10A, 1)
    OP_93(0x10A, 0x0, 0x1F4)
    Return()

    # Function_16_3B07 end

    def Function_17_3B5C(): pass

    label("Function_17_3B5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B72")
    Call(0, 18)
    Jump("loc_3B9B")

    label("loc_3B72")

    TalkBegin(0xFF)
    SetChrName("")

    #A0098
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "柜子里摆放着陈年好酒。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_3B9B")

    Return()

    # Function_17_3B5C end

    def Function_18_3B9C(): pass

    label("Function_18_3B9C")

    EventBegin(0x0)
    Fade(1000)
    OP_68(7700, 1200, 113000, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 6700, 0, 113000, 90)
    OP_0D()
    SetChrName("")

    #A0099
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "柜子里摆放着陈年好酒。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0100
    ChrTalk(
        0x101,
        (
            "#0005F#6P（看上去，都是些\x01",
            "  很高档的酒……）\x02\x03",

            "#0000F（……难道说……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0101
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将瓶子一个个地拿起，检查瓶子下面。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0102
    ChrTalk(
        0x101,
        "#0002F#6P（猜中了……！）\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0103
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x32F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('库雷斯队员的问诊表', 1)

    #C0104
    ChrTalk(
        0x101,
        (
            "#0004F#6P（这种手下们无论如何都不会\x01",
            "  去碰的地方……）\x02\x03",

            "#0000F（算是藏东西的惯例地点吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 6700, 0, 113000, 90)
    SetScenarioFlags(0xC6, 4)
    EventEnd(0x5)
    Return()

    # Function_18_3B9C end

    def Function_19_3D68(): pass

    label("Function_19_3D68")

    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis092.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis093.itp")
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis091.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis091.itp")
    Sound(809, 0, 100, 0)
    Sleep(600)
    Sound(14, 0, 100, 0)
    OP_71(0x11, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x11)
    Sleep(500)

    #C0105
    ChrTalk(
        0x101,
        (
            "#0000F#11P（好……打开了。）\x02\x03",

            "#0008F（这里有好多文件……\x01",
            "  ……嗯，我看看……）\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0106
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x331),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('易碎品的小包裹', 1)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0107
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x332),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('发往住宅街的送货单', 1)

    #A0108
    AnonymousTalk(
        0x101,
        (
            "#0005F（有了……！）\x02\x03",

            "#0003F（黑手党果然与违禁药物脱不开关系……）\x02\x03",

            "（『真知』……\x01",
            "  就是那个教团制造的药物吗……）\x02\x03",

            "#0013F（黑手党和教团之间到底有什么关系呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0109
    ChrTalk(
        0x101,
        (
            "#0001F#11P（哎，宝箱的角落里好像有什么东西……）\x02\x03",

            "（……这是警察的……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0110
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x333),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('蓝花', 1)

    #A0111
    AnonymousTalk(
        0x101,
        "#0005F（…………哎……………）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(1000)
    OP_C9(0x3, 0x0, 0xFFFDF0A8, 0xFFFDF0A8, 0x0)
    OP_C9(0x3, 0x1, 0x7D0, 0x7D0, 0x0)
    OP_CA(0x0, 0xFF, 0x0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x7D0, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x0, 0x0)
    Sleep(1000)
    FadeToDark(0, 0, -1)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0xBB8, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x9, 0xFF, 0xFF)
    OP_68(0, 900, 110000, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -200, 20, 107400, 0)
    SetChrPos(0x102, -1900, 30, 108500, 0)
    SetChrPos(0x103, -1500, 30, 107700, 0)
    SetChrPos(0x104, 1200, 30, 108100, 330)
    SetChrPos(0x10A, 0, 20, 109200, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetMapObjFrame(0xFF, "sakebin", 0x0, 0x1)
    ClearMapObjFlags(0x13, 0x4)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7122", 0)
    SetCameraDistance(18000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0112
    ChrTalk(
        0x10A,
        (
            "#0603F#11P──所有失踪市民的名字\x01",
            "都记录在这份资料上。\x02\x03",

            "这样，就取得黑手党\x01",
            "传播违禁药物的证据了。\x02\x03",

            "#0601F而且，所谓的违禁药物，正是疑似由\x01",
            "那个教团制造出来的『真知』吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x103,
        "#12P#0208F………………………………\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x102,
        (
            "#12P#0106F黑手党究竟是怎么\x01",
            "得到那种东西的……\x02\x03",

            "#0108F从进货清单来看，\x01",
            "应该是由某人\x01",
            "直接提供的……\x02\x03",

            "#0101F那个人会是\x01",
            "与教团有关联的人物吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#12P#0003F──肯定没错吧。\x02\x03",

            "#0001F从这些材料上看，应该是从数年前开始\x01",
            "就与那个人有联系了。\x02\x03",

            "对方似乎还提供了给军犬\x01",
            "投喂药物，进而轻易\x01",
            "控制它们的技术。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x104,
        (
            "#0306F原来如此，训练军犬这种事情，\x01",
            "即使是猎兵团，也要花费很多工夫。\x02\x03",

            "#0301F他们能轻易动用如此大量的军犬，\x01",
            "我一直觉得有点不对劲呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x10A,
        (
            "#0603F#11P都是因为有教团的相关人员\x01",
            "从旁协助吗……\x02\x03",

            "#0608F不过，那究竟是谁呢……？\x02\x03",

            "从这种频繁的交涉次数来看，\x01",
            "肯定是住在\x01",
            "克洛斯贝尔的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#12P#0003F……想不出呢。\x02\x03",

            "#0013F但我总觉得，无论是失踪者的去向，\x01",
            "还是那些黑手党不在此处的理由……\x02\x03",

            "这些状况应该都在\x01",
            "那个人物的掌握之中。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x103,
        (
            "#12P#0206F……我也有同感。\x02\x03",

            "#0208F那种蓝色药物，\x01",
            "恐怕就是教团在数年前曾给我\x01",
            "服用过的『真知』的改良版……\x02\x03",

            "#0201F之后那个人物最终将它完善……\x01",
            "然后又提供给黑手党了吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_46FF():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_46FF)
    WaitChrThread(0x103, 2)
    Sleep(300)

    def lambda_471F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_471F)
    Sleep(50)

    def lambda_472F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_472F)
    Sleep(50)
    TurnDirection(0x104, 0x103, 500)

    #C0120
    ChrTalk(
        0x102,
        "#5P#0101F缇欧……\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        (
            "#0004F#11P不用担心……\x01",
            "有我们和你在一起。\x02\x03",

            "#0000F绝对不会──\x01",
            "让缇欧再次经历那种噩梦了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0122
    ChrTalk(
        0x103,
        "#6P#0202F罗伊德前辈……\x02",
    )

    CloseMessageWindow()

    def lambda_47DF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_47DF)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)

    #C0123
    ChrTalk(
        0x104,
        (
            "#0304F总之，我们必须要把那家伙好好修理一顿，\x01",
            "因为已经完全能够确定他不是什么好人了。\x02\x03",

            "#0301F不过，如此一来……\x01",
            "怎么才能把他揪出来，才是目前最大的问题啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x102,
        (
            "#5P#0108F是啊……\x01",
            "我们的人手实在是远远不足。\x02\x03",

            "既要追查消失的黑手党，\x01",
            "又要搜索失踪者，\x01",
            "再加上空港那边的炸弹恐吓信……\x02\x03",

            "#0106F……如果没有来自上级的压力，\x01",
            "终究也能想办法应对，可是……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x10A,
        (
            "#0606F#11P哼……没想到连警察局长\x01",
            "都与他们狼狈为奸啊。\x02\x03",

            "要不是这样，早就应该集结警察局全体成员\x01",
            "的力量，设立特别对应部门了……\x02\x03",

            "#0610F难道就没有一点廉耻心吗……！\x01",
            "这些玷污警察荣誉的败类……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4A12():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4A12)
    Sleep(50)

    def lambda_4A22():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4A22)
    Sleep(50)

    def lambda_4A32():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4A32)
    Sleep(50)
    TurnDirection(0x104, 0x10A, 500)

    #C0126
    ChrTalk(
        0x101,
        "#12P#0005F达德利警官……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0127
    ChrTalk(
        0x101,
        (
            "#12P#0003F──我有个提议。\x02\x03",

            "#0001F要不要向游击士协会\x01",
            "请求协助呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
    MoveCamera(43, 21, 0, 1200)
    OP_68(250, 900, 108770, 1200)

    def lambda_4B4E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_4B4E)
    Sleep(100)

    def lambda_4B5E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4B5E)
    Sleep(50)

    def lambda_4B6E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4B6E)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)
    OP_6F(0x1)

    #C0128
    ChrTalk(
        0x102,
        "#5P#0100F啊……\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x104,
        (
            "#11P#0302F哦哦……！\x01",
            "对啊，还有这招呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x10A,
        (
            "#0607F#5P别、别说蠢话了！\x02\x03",

            "如果这么做的话，\x01",
            "警察局内部的丑闻岂不就\x01",
            "全部暴露给协会了吗──\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        (
            "#12P#0006F这也没办法吧……\x01",
            "这毕竟是全体警察的过错。\x02\x03",

            "我们一直都对这些黑幕视而不见、\x01",
            "无所作为，所以全都负有责任。\x02\x03",

            "#0013F既然是全体警察的过错，那么我们\x01",
            "至少该坦然正视，而不是遮遮掩掩，不是吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x10A,
        "#0610F#5P呃……\x02",
    )

    CloseMessageWindow()

    def lambda_4D02():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_4D02)
    Sleep(50)

    def lambda_4D12():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4D12)
    Sleep(50)

    def lambda_4D22():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4D22)
    Sleep(300)

    #C0133
    ChrTalk(
        0x103,
        (
            "#6P#0211F的确，在我们纠结这些事的时候，\x01",
            "失踪的人们不知道\x01",
            "会遭遇到什么危险呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x104,
        (
            "#12P#0300F而且也不知道那些玩失踪的\x01",
            "黑手党们都在干什么啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x102,
        (
            "#6P#0101F我认为，现在已经不是\x01",
            "顾及颜面的时候了。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1388)

    #C0136
    ChrTalk(
        0x10A,
        "#0603F#5P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10A)
    Sleep(100)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)

    #C0137
    ChrTalk(
        0x10A,
        (
            "#0604F#5P哼……赛尔盖长官也真是的，\x01",
            "召集的都是些什么部下啊。\x02\x03",

            "#0600F好吧──\x01",
            "与协会交涉的事情就交给你们了。\x02\x03",

            "我会避开上级的耳目，偷偷从一科\x01",
            "调出一些可以自由行动的人手。\x02\x03",

            "#0603F根据具体情况，也许还会去\x01",
            "请求二科的援助。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x101,
        (
            "#12P#0002F达德利警官……\x02\x03",

            "#0004F……非常感谢，\x01",
            "感谢您接受我们的提议。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x10A,
        (
            "#0602F#5P哼……不要搞错。\x02\x03",

            "我个人并不赞同你们，只是从现状来看，\x01",
            "已经没有比这更好的选择了。\x02\x03",

            "#0603F比起这些──班宁斯。\x02\x03",

            "#0601F关于这枚徽章，你有何看法？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        "#12P#0008F啊……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Sleep(500)

    #A0141
    AnonymousTalk(
        0x102,
        "#0108F这枚有损伤痕迹的警察徽章……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0142
    AnonymousTalk(
        0x104,
        (
            "#0301F真的是……\x01",
            "你哥哥的徽章吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0143
    AnonymousTalk(
        0x101,
        (
            "#0006F嗯，我想多半没错。\x02\x03",

            "#0000F缇欧应该也\x01",
            "觉得眼熟吧……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0144
    AnonymousTalk(
        0x103,
        (
            "#0204F是的……\x02\x03",

            "应该就是在捣毁那个教团据点的时候\x01",
            "被弄伤的……\x02\x03",

            "#0202F他说，这损伤的痕迹正是荣誉的勋章。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0145
    AnonymousTalk(
        0x10A,
        (
            "#0606F哼，原来如此啊……\x02\x03",

            "#0608F……难怪当时不管别人怎么劝说，\x01",
            "他也坚持不肯换成新的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    #C0146
    ChrTalk(
        0x101,
        (
            "#12P#0000F达德利警官……\x01",
            "您原来是大哥的同事吧？\x02\x03",

            "在大哥被调到一科的那段时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x10A,
        (
            "#0603F#5P算是吧……\x02\x03",

            "#0601F老实说，那个男人的作风\x01",
            "与一科真是完全不合呢。\x02\x03",

            "态度强硬，又行事莽撞，\x01",
            "总是擅做主张，招惹众人的注目……\x02\x03",

            "跟我的性格尤为不合，\x01",
            "我们总是在办案时发生冲突。\x02\x03",

            "#0604F然而——他确实是一位很优秀的搜查官。\x01",
            "在一科，从没有人否认过这一点。\x02\x03",

            "当然也包括我在内。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x101,
        "#12P#0005F达德利警官……\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x10A,
        (
            "#0606F#5P……当他不幸殉职的时候，\x01",
            "我们一科的人体会到了\x01",
            "远远超出预想的失落。\x02\x03",

            "虽然脾气非常不合……\x01",
            "但在内心深处，可能一直都对他那\x01",
            "破天荒的行动力抱有期待吧。\x02\x03",

            "#0608F我们拼命地搜寻犯人，\x01",
            "但最后也没有找到线索……\x02\x03",

            "#0603F──抱歉，\x01",
            "又让你回想起沉痛的往事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#12P#0011F请、请不用介意。\x02\x03",

            "#0006F毕竟……独自进行调查的大哥\x01",
            "也有一定的责任……\x02\x03",

            "#0002F您能这样评价\x01",
            "大哥的殉职，\x01",
            "我已经感到很欣慰了。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x10A,
        (
            "#0602F#5P是吗……\x02\x03",

            "#0603F──不过，事到如今，\x01",
            "嫌疑人再次浮出水面了。\x02\x03",

            "虽然我们当时就曾\x01",
            "怀疑过这种可能性……\x02\x03",

            "#0601F但如今，你总算有机会为哥哥报仇，\x01",
            "完成他生前未能实现的愿望了──\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        (
            "#12P#0004F不……\x01",
            "现在先不考虑大哥的事情了。\x02\x03",

            "#0008F比起这些，还有堆积如山的问题\x01",
            "等着我们去解决……\x02\x03",

            "#0000F把一切都平息之后，我再去考虑那件事吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_564B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_564B)
    Sleep(50)

    def lambda_565B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_565B)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)

    #C0153
    ChrTalk(
        0x103,
        "#6P#0202F罗伊德前辈……\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x102,
        (
            "#6P#0104F你可真是……\x01",
            "太认真尽责了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x104,
        (
            "#11P#0309F算啦，这才是\x01",
            "这家伙的作风嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x10A,
        (
            "#0604F#5P呵──我明白了。\x02\x03",

            "#0602F那么，我们就分头行动，\x01",
            "去做各自该做的事情吧！\x02\x03",

            "就算是为了不输给那个出格到\x01",
            "让人火大，却又始终勇往直前的男人，\x01",
            "我们也要加倍努力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x101,
        "#12P#0000F是……！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(17500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0x1770)
    WaitBGM()
    OP_CA(0x1, 0x0, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis161.itp")
    OP_29(0x4C, 0x4, 0x10)
    SubItemNumber('库雷斯队员的问诊表', 1)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E3(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_DE(0x28, 0x0)
    OP_DE(0x1E, 0x0)
    OP_DE(0x1F, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C7(0x0, 0x10)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5F, 0)
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x9B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x5F, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_BA(0x9)
    RemoveParty(0x9, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_C7(0x1, 0x10)
    ReplaceBGM("ed7000", "ed7000")
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("t3010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_3D68 end

    def Function_20_58F6(): pass

    label("Function_20_58F6")

    EventBegin(0x0)
    Fade(1000)
    OP_68(0, 1150, 63000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 0, 30, 62300, 0)
    SetChrPos(0x102, -1400, 30, 60500, 0)
    SetChrPos(0x104, -1400, 30, 59400, 0)
    SetChrPos(0x103, -100, 30, 59400, 0)
    SetChrPos(0x10A, 1000, 30, 61000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    #C0158
    ChrTalk(
        0x101,
        (
            "#0003F（黑手党老大的房间……\x01",
            "  总算来到这里了啊。）\x02\x03",

            "#0008F（我想，在开始调查这个房间后，\x01",
            "  从很多意义上来说，恐怕就不能再回头了。）\x02\x03",

            "#0013F（要怎么做呢……？）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0159
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "进入这扇门以后，就不能再自由出入\x01",
            "克洛斯贝尔市以外的地方了。\x02\x03",

            "因此有可能会无法完成进行到一半的委托任务，\x01",
            "请多加注意。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Sleep(300)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【开门并进入房间】\x01",      # 0
            "【暂时离开】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5B22"),
        (1, "loc_5BF0"),
        (SWITCH_DEFAULT, "loc_5C43"),
    )


    label("loc_5B22")

    Sound(103, 0, 100, 0)
    OP_71(0x10, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x10)
    FadeToDark(1000, 0, -1)

    def lambda_5B46():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5B46)
    Sleep(100)

    def lambda_5B63():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_5B63)
    Sleep(100)

    def lambda_5B80():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B80)
    Sleep(100)

    def lambda_5B9D():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5B9D)
    Sleep(100)

    def lambda_5BBA():
        OP_96(0xFE, 0x0, 0x0, 0x105B8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5BBA)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x10A, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    OP_65(0x3, 0x1)
    Call(0, 15)
    Jump("loc_5C43")

    label("loc_5BF0")

    SetChrPos(0x0, 0, 30, 61800, 180)
    SetChrPos(0x1, 0, 30, 61800, 180)
    SetChrPos(0x2, 0, 30, 61800, 180)
    SetChrPos(0x3, 0, 30, 61800, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_5C43")

    label("loc_5C43")

    EventEnd(0x5)
    Return()

    # Function_20_58F6 end

    def Function_21_5C46(): pass

    label("Function_21_5C46")

    EventBegin(0x1)

    #C0160
    ChrTalk(
        0x101,
        (
            "#0013F现在可不是外出的时候……\x01",
            "立刻把这个房间彻底调查一下吧！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 0, 0, 100500, 0)
    EventEnd(0x4)
    Return()

    # Function_21_5C46 end

    SaveToFile()

Try(main)
