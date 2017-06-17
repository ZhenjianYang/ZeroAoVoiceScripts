from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "e0010.bin",                # FileName
        "e0010",                    # MapName
        "e0010",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e0010",                  # 0
        "驾驶员",                 # 1
        "乘客",                   # 2
        "乘客",                   # 3
        "乘客",                   # 4
        "黑发女性",               # 5
        "老婆婆",                 # 6
        "老人",                   # 7
        "贸易商",                 # 8
        "女性",                   # 9
        "哥哥",                   # 10
        "妹妹",                   # 11
        "父亲",                   # 12
        "男孩",                   # 13
        "SE控制",                 # 14
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_268",          # 00, 0
        "Function_1_2B4",          # 01, 1
        "Function_2_2B5",          # 02, 2
        "Function_3_A26",          # 03, 3
        "Function_4_A4B",          # 04, 4
        "Function_5_F86",          # 05, 5
        "Function_6_12AC",         # 06, 6
        "Function_7_12E5",         # 07, 7
        "Function_8_131E",         # 08, 8
        "Function_9_135A",         # 09, 9
        "Function_10_1396",        # 0A, 10
        "Function_11_13DE",        # 0B, 11
        "Function_12_1449",        # 0C, 12
        "Function_13_14AA",        # 0D, 13
        "Function_14_14EE",        # 0E, 14
        "Function_15_15B2",        # 0F, 15
        "Function_16_3110",        # 10, 16
        "Function_17_3154",        # 11, 17
        "Function_18_3198",        # 12, 18
    ))


    def Function_0_268(): pass

    label("Function_0_268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_27C")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 2)
    Jump("loc_2B3")

    label("loc_27C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_290")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 4)
    Jump("loc_2B3")

    label("loc_290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_2A4")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 5)
    Jump("loc_2B3")

    label("loc_2A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 3)), scpexpr(EXPR_END)), "loc_2B3")
    ClearScenarioFlags(0x5C, 3)
    Event(0, 15)

    label("loc_2B3")

    Return()

    # Function_0_268 end

    def Function_1_2B4(): pass

    label("Function_1_2B4")

    Return()

    # Function_1_2B4 end

    def Function_2_2B5(): pass

    label("Function_2_2B5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("apl/ch50119.itc", 0x22)
    LoadChrToIndex("chr/ch20402.itc", 0x23)
    LoadChrToIndex("chr/ch20302.itc", 0x24)
    LoadChrToIndex("chr/ch22302.itc", 0x25)
    SoundLoad(468)
    OP_68(46910, 1100, -180, 0)
    MoveCamera(328, 24, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(16350, 0)
    OP_68(52300, 1100, -180, 10000)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x2)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x25)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0x101, 52250, 0, 800, 0)
    SetChrPos(0x102, 55000, 150, 200, 270)
    SetChrPos(0x103, 55000, 150, 1450, 270)
    SetChrPos(0x104, 53300, 150, 1700, 180)
    SetChrPos(0x8, 43870, -200, 1800, 270)
    SetChrPos(0x9, 46150, 150, -1840, 270)
    SetChrPos(0xA, 48050, 150, 1880, 270)
    SetChrPos(0xB, 48050, 150, 880, 270)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Sound(468, 2, 100, 0)
    BeginChrThread(0x101, 3, 0, 3)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0001
    ChrTalk(
        0x101,
        "#0000F#6P………………………………\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x102,
        "#0100F#6P黄昏的景色真美呢……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x103,
        (
            "#0203F#4P是啊……\x01",
            "感觉美丽得有些让人不敢直视。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x104, 0x0)
    Sleep(300)

    #C0004
    ChrTalk(
        0x104,
        (
            "#0304F#11P哈～话说，导力车\x01",
            "还真是好方便啊。\x02\x03",

            "#0300F不过，咱们支援科要是也能\x01",
            "配备专用车就更好了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0005
    ChrTalk(
        0x101,
        (
            "#0006F#6P哈，应该很难吧。\x02\x03",

            "#0000F虽然其它搜查科\x01",
            "好像都有自己的车…\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    Sleep(200)

    #C0006
    ChrTalk(
        0x103,
        (
            "#0200F#4P……确实，在搜查一科，\x01",
            "每名调查员应该都配备有\x01",
            "自己的专用车辆呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    #C0007
    ChrTalk(
        0x101,
        "#0005F#5P是、是吗！？\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#0106F#6P那样的话，待遇也\x01",
            "实在是太过优厚了……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x104,
        (
            "#0306F#5P哎呀呀……这种时候就更加感觉\x01",
            "不被重视很辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#0006F#5P算了，没有的东西，\x01",
            "再想也没有用……\x02\x03",

            "#0000F而且，像这样徒步行走，\x01",
            "你们不觉得也是一种很好的锻炼吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x103,
        (
            "#0203F#4P虽然并非本意……\x01",
            "但也许确实如此呢。\x02\x03",

            "#0211F不过，今天已经没有时间\x01",
            "再继续调查下去了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#0003F#5P嗯，剩下的就是北部的矿山镇了。\x02\x03",

            "#0000F就按照刚才说的那样，\x01",
            "今天先回去整理一下调查报告书，\x01",
            "明天再去拜访那里吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x103,
        "#0206F#4P呼……了解。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        (
            "#0109F#6P呵呵……\x01",
            "今天还真是累了呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    Sleep(200)
    OP_63(0x104, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1200)

    #C0015
    ChrTalk(
        0x104,
        (
            "#0309F#11P嗯～……\x01",
            "不过，塞茜尔小姐真是太棒了。\x02\x03",

            "#0307F好，要是下次有机会，就以\x01",
            "联谊会的名义，与她拉近个人关系吧……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0016
    ChrTalk(
        0x101,
        "#0006F#6P兰迪真有精神啊……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    BeginChrThread(0x15, 0, 0, 16)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    WaitChrThread(0x15, 0)
    OP_24(0x1D4)
    SetScenarioFlags(0x5C, 0)
    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_2B5 end

    def Function_3_A26(): pass

    label("Function_3_A26")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A4A")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_3_A26")

    label("loc_A4A")

    Return()

    # Function_3_A26 end

    def Function_4_A4B(): pass

    label("Function_4_A4B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch21102.itc", 0x22)
    LoadChrToIndex("chr/ch21602.itc", 0x23)
    LoadChrToIndex("apl/ch50382.itc", 0x24)
    SoundLoad(468)
    OP_68(147980, 1000, 1450, 0)
    MoveCamera(330, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(16170, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_AD5")
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_AFC")

    label("loc_AD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_AEB")
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_AFC")

    label("loc_AEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_AFC")
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)

    label("loc_AFC")

    SetChrFlags(0xEF, 0x4)
    SetChrFlags(0x153, 0x2)
    SetChrFlags(0x153, 0x10)
    SetChrFlags(0x153, 0x4)
    SetChrChipByIndex(0x153, 0x24)
    SetChrSubChip(0x153, 0x0)
    SetChrPos(0x101, 148050, 150, 1800, 180)
    SetChrPos(0x153, 147350, 350, 1800, 0)
    SetChrPos(0xEF, 146600, 150, 1800, 180)
    SetChrChipByIndex(0x9, 0x22)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 145000, 150, 790, 90)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, 145000, 150, -100, 90)
    SetMapObjFrame(0xFF, "bg00_y", 0x0, 0x1)
    Sound(468, 2, 100, 0)
    BeginChrThread(0x101, 3, 0, 3)
    FadeToBright(1000, 0)
    OP_68(146980, 1000, 1450, 3000)
    OP_0D()
    OP_6F(0x1)
    Sound(2033, 255, 100, 0)    #voice#KeA
    Sleep(1800)
    SetChrSubChip(0x153, 0x1)
    Sleep(300)

    #C0017
    ChrTalk(
        0x153,
        (
            "#1109F#5P喂喂，罗伊德！\x01",
            "好漂亮哦～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    SetChrSubChip(0x101, 0x2)
    Sleep(100)
    SetChrSubChip(0xEF, 0x1)
    Sleep(200)

    #C0018
    ChrTalk(
        0x101,
        "#0011F#11P声、声音太大了……！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xEF, 0x0)
    Sleep(100)
    SetChrSubChip(0xEF, 0x2)
    Sleep(200)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_C97")

    #C0019
    ChrTalk(
        0x102,
        (
            "#0106F#11P对、对不起……\x01",
            "这孩子实在是太吵闹了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D14")

    label("loc_C97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_CD8")

    #C0020
    ChrTalk(
        0x103,
        (
            "#0206F#11P……对不起。\x01",
            "这孩子实在是太吵闹了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D14")

    label("loc_CD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_D14")

    #C0021
    ChrTalk(
        0x104,
        (
            "#0306F#11P不好意思啊。\x01",
            "这小鬼实在是太吵闹了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D14")


    #C0022
    ChrTalk(
        0x9,
        (
            "#5P呵呵，没关系啊。\x01",
            "小孩子就是应该有活力。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xA,
        (
            "#1P呵呵，你们是要去\x01",
            "探望什么人吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#0000F#11P不，我们稍微有些事情，\x01",
            "要去咨询医院的医生……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x153, 0x0)

    #C0025
    ChrTalk(
        0x153,
        (
            "#1107F#5P快看快看，那边有\x01",
            "小小的孤岛哦～！\x02\x03",

            "#1109F形状真奇怪，好有趣～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0xEF, 0x0)
    Sleep(100)
    SetChrSubChip(0xEF, 0x1)

    #C0026
    ChrTalk(
        0x101,
        "#0012F#12P哎呀哎呀……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_EA0")

    #C0027
    ChrTalk(
        0x102,
        (
            "#0102F#6P呵呵……\x01",
            "她好像很高兴呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F05")

    label("loc_EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_ED4")

    #C0028
    ChrTalk(
        0x103,
        (
            "#0202F#6P呵……\x01",
            "她好像很开心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F05")

    label("loc_ED4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_F05")

    #C0029
    ChrTalk(
        0x104,
        (
            "#0309F#6P哈哈……\x01",
            "她好像很兴奋啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F05")

    SetCameraDistance(15670, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0xEF, 0x4)
    SetChrChipByIndex(0xEF, 0xFF)
    SetChrSubChip(0xEF, 0x0)
    ClearChrFlags(0x153, 0x4)
    ClearChrFlags(0x153, 0x2)
    ClearChrFlags(0x153, 0x10)
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    BeginChrThread(0x15, 0, 0, 16)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x15, 0)
    OP_24(0x1D4)
    SetScenarioFlags(0x5C, 1)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_A4B end

    def Function_5_F86(): pass

    label("Function_5_F86")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 2600, -500, -450, 270)
    SetChrPos(0x102, 2600, -500, 450, 270)
    SetChrPos(0x103, 3700, -500, 450, 270)
    SetChrPos(0x104, 3700, -500, -450, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(900, 900, 0, 0)
    MoveCamera(270, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17800, 0)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    SetMapObjFrame(0xFF, "bg00_y", 0x2, "stop")
    SetMapObjFrame(0xFF, "effect00_add", 0x0, 0x1)
    FadeToBright(1000, 0)
    OP_68(400, 900, 0, 2500)
    BeginChrThread(0x101, 3, 0, 6)
    BeginChrThread(0x102, 3, 0, 7)
    BeginChrThread(0x103, 3, 0, 8)
    BeginChrThread(0x104, 3, 0, 9)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(0, 900, 0, 0)
    OP_68(0, 900, -2500, 4000)
    MoveCamera(320, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17800, 0)
    Sleep(1500)
    BeginChrThread(0x101, 3, 0, 10)
    Sleep(200)
    BeginChrThread(0x104, 3, 0, 11)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 12)
    Sleep(150)
    BeginChrThread(0x103, 3, 0, 13)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    Sleep(2000)
    FadeToBright(1000, 0)
    OP_68(0, 500, 500, 0)
    MoveCamera(320, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17800, 0)
    SetChrPos(0x101, 600, 0, -4800, 0)
    SetChrPos(0x102, 800, 0, 2300, 0)
    SetChrPos(0x103, 0, 0, 3700, 0)
    SetChrPos(0x104, -800, 0, 2600, 0)
    OP_68(0, 500, 4500, 6000)

    def lambda_11BA():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11BA)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)
    OP_0D()

    #C0030
    ChrTalk(
        0x101,
        (
            "#0008F#6P花和慰问品\x01",
            "都留在座位上……\x02\x03",

            "#0013F看起来，像是\x01",
            "正要去医院呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x102,
        "#0106F#6P嗯……\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x103,
        (
            "#0208F#6P咪西玩偶……\x01",
            "大概是送给\x01",
            "小患者的慰问品吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x104,
        "#0306F#6P嗯……大概吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(17200, 2500)
    OP_6F(0x79)
    OP_0D()
    SetScenarioFlags(0x5C, 2)
    NewScene("r1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_F86 end

    def Function_6_12AC(): pass

    label("Function_6_12AC")


    def lambda_12B1():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12B1)

    def lambda_12C6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12C6)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    OP_93(0xFE, 0xB4, 0x12C)
    Return()

    # Function_6_12AC end

    def Function_7_12E5(): pass

    label("Function_7_12E5")


    def lambda_12EA():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12EA)

    def lambda_12FF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12FF)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_7_12E5 end

    def Function_8_131E(): pass

    label("Function_8_131E")


    def lambda_1323():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1323)
    Sleep(500)

    def lambda_133B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_133B)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    OP_93(0xFE, 0x13B, 0x12C)
    Return()

    # Function_8_131E end

    def Function_9_135A(): pass

    label("Function_9_135A")


    def lambda_135F():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_135F)
    Sleep(500)

    def lambda_1377():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1377)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Sleep(500)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_9_135A end

    def Function_10_1396(): pass

    label("Function_10_1396")

    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_13A2():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13A2)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_13C2():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13C2)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_10_1396 end

    def Function_11_13DE(): pass

    label("Function_11_13DE")

    Sleep(500)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_13ED():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13ED)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)

    def lambda_140D():
        OP_9B(0x0, 0xFE, 0x0, 0x898, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_140D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_142D():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_142D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_11_13DE end

    def Function_12_1449(): pass

    label("Function_12_1449")

    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_1455():
        OP_9B(0x0, 0xFE, 0x0, 0x4B0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1455)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)

    def lambda_1475():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1475)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_1495():
        OP_9B(0x0, 0xFE, 0x0, 0x320, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1495)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_1449 end

    def Function_13_14AA(): pass

    label("Function_13_14AA")

    Sleep(500)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_14B9():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14B9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)

    def lambda_14D9():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14D9)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_13_14AA end

    def Function_14_14EE(): pass

    label("Function_14_14EE")

    EventBegin(0x0)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【老人】\x01",            # 0
            "【老婆婆】\x01",          # 1
            "【黑发女性】\x01",        # 2
            "【年轻的女性】\x01",      # 3
            "【贸易商】\x01",          # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_155F"),
        (1, "loc_156D"),
        (2, "loc_157B"),
        (3, "loc_1589"),
        (4, "loc_1597"),
        (SWITCH_DEFAULT, "loc_15A5"),
    )


    label("loc_155F")

    OP_60(0x0)
    OP_29(0x1B, 0x1, 0xE)
    Jump("loc_15A5")

    label("loc_156D")

    OP_60(0x0)
    OP_29(0x1B, 0x1, 0xF)
    Jump("loc_15A5")

    label("loc_157B")

    OP_60(0x0)
    OP_29(0x1B, 0x1, 0x10)
    Jump("loc_15A5")

    label("loc_1589")

    OP_60(0x0)
    OP_29(0x1B, 0x1, 0x11)
    Jump("loc_15A5")

    label("loc_1597")

    OP_60(0x0)
    OP_29(0x1B, 0x1, 0x12)
    Jump("loc_15A5")

    label("loc_15A5")

    SetScenarioFlags(0x5C, 0)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_14EE end

    def Function_15_15B2(): pass

    label("Function_15_15B2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("apl/ch50119.itc", 0x22)
    LoadChrToIndex("chr/ch07302.itc", 0x23)
    LoadChrToIndex("chr/ch24102.itc", 0x24)
    LoadChrToIndex("chr/ch20802.itc", 0x25)
    LoadChrToIndex("chr/ch33000.itc", 0x26)
    LoadChrToIndex("chr/ch24500.itc", 0x27)
    LoadChrToIndex("chr/ch21202.itc", 0x28)
    LoadChrToIndex("chr/ch21302.itc", 0x29)
    LoadChrToIndex("chr/ch21002.itc", 0x2A)
    LoadChrToIndex("chr/ch21402.itc", 0x2B)
    SoundLoad(474)
    OP_68(47090, 1100, -430, 0)
    MoveCamera(328, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23180, 0)
    OP_68(51930, 1100, 120, 8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xD, 0x24)
    SetChrSubChip(0xD, 0x1)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0xE, 0x25)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0xF, 0x26)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrChipByIndex(0x10, 0x27)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrChipByIndex(0x11, 0x28)
    SetChrSubChip(0x11, 0x2)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x1)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrChipByIndex(0x13, 0x2A)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrChipByIndex(0x14, 0x2B)
    SetChrSubChip(0x14, 0x2)
    SetChrPos(0x101, 52250, 150, 1700, 180)
    SetChrPos(0x102, 55000, 150, 200, 270)
    SetChrPos(0x103, 55000, 150, 1450, 270)
    SetChrPos(0x104, 53300, 150, 1700, 180)
    SetChrPos(0x8, 43870, -200, 1800, 270)
    SetChrPos(0xC, 48000, 150, -2000, 270)
    SetChrPos(0xD, 44000, 150, -2000, 270)
    SetChrPos(0xE, 46000, 150, -2000, 270)
    SetChrPos(0xF, 50270, -250, -2029, 225)
    SetChrPos(0x10, 49540, -250, 1520, 270)
    SetChrPos(0x11, 48000, 150, 600, 270)
    SetChrPos(0x12, 48000, 150, 1600, 270)
    SetChrPos(0x13, 46000, 150, 600, 270)
    SetChrPos(0x14, 46000, 150, 1600, 270)
    SetMapObjFrame(0xFF, "bg00_y", 0x0, 0x1)
    PlayBGM("ed7516", 0)
    Sound(474, 2, 0, 0)
    BeginChrThread(0x15, 0, 0, 17)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    EndChrThread(0x15, 0x0)

    #C0034
    ChrTalk(
        0x101,
        (
            "#5P#0001F（首先……\x01",
            "　来整理一下有关假货贩子\x01",
            "　的情报吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x103,
        (
            "#12P#0203F（那些假货贩子们是从\x01",
            "　车站、空港和唐古拉姆门\x01",
            "　这几条路线分头而来的……）\x02\x03",

            "#0200F（根据从警察局总部得到的情报，\x01",
            "　确实就是这样的。）\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#5P#0000F（嗯，正是如此。）\x02\x03",

            "#0003F（然后，既然情报准确，\x01",
            "　嫌疑人应该就在\x01",
            "　这辆巴士的乘客中。）\x02\x03",

            "（还有……\x01",
            "　根据这些情报来分析，\x01",
            "　就有一个事实浮出水面了。）\x02\x03",

            "#0001F（这辆巴士中的假货贩子，\x01",
            "　恐怕是……）\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【单独行动的】\x01",          # 0
            "【两人一组行动的】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1A48"),
        (1, "loc_1F60"),
        (SWITCH_DEFAULT, "loc_2659"),
    )


    label("loc_1A48")

    OP_60(0x0)
    OP_2C(0x1B, 0x1)

    #C0037
    ChrTalk(
        0x101,
        (
            "#5P#0001F（……是单独行动的。）\x02\x03",

            "#0003F（而且，这个人在假货贩子团伙中，\x01",
            "　应该也是头目般的存在。）\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x104,
        (
            "#11P#0305F（喂喂，真的假的……\x01",
            "　头目级的人物，难道会\x01",
            "　一个人单独行动吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#12P#0105F（这种情况倒也并非没有可能……\x01",
            "　不过，根据在哪里呢？）\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#5P#0004F（很简单。）\x02\x03",

            "（那些家伙为了来这里做生意，\x01",
            "　就必须要偷偷把假货\x01",
            "　运进克洛斯贝尔。）\x02\x03",

            "#0000F（乘坐巴士来通过唐古拉姆门，\x01",
            "　明显不是适当的运货通道。）\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x103,
        (
            "#12P#0203F（确实……如你所说呢。）\x02\x03",

            "#0200F（如果我是假货贩子，\x01",
            "　恐怕会把运货任务交给从车站和空港\x01",
            "　潜入克洛斯贝尔的那些同伴。）\x02\x03",

            "（和国境门不同，车站和空港\x01",
            "　并不会对共和国和帝国方面的\x01",
            "　入境人员进行太过严密的检查。）\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        (
            "#11P#0303F（另外，像运货这种危险的任务，\x01",
            "　一般都会交给下面的人去做，这也是惯例。）\x02\x03",

            "（利用排除法来思考……\x01",
            "　车站或空港这两条线路\x01",
            "　是用来运送货物的……）\x02\x03",

            "#0301F（而头目则只携带少量行李，\x01",
            "　完全不会被人怀疑，就这么毫无危险，\x01",
            "　悠哉悠哉地前往克洛斯贝尔吗。）\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        "#5P#0000F（就是这么一回事。）\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#12P#0103F（虽然只是根据现场情况而做出的推测……\x01",
            "　但确实很有说服力呢。）\x02\x03",

            "#0101F（这样一来，两人出行的\x01",
            "　兄妹游客，还有那位带着小孩的旅行者，\x01",
            "　就可以从嫌疑犯的名单中排除了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#5P#0001F（……嗯，然后……）\x02\x03",

            "#0003F（刚才，在和乘客们对话的时候……\x01",
            "　有一个人说的话让我十分在意。）\x02\x03",

            "（如果所料不差，\x01",
            "　那个人恐怕就是假货贩子的头目了。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2659")

    label("loc_1F60")

    OP_60(0x0)

    #C0046
    ChrTalk(
        0x101,
        (
            "#5P#0003F（……是两人一组行动的。）\x02\x03",

            "#0001F（在假货商人的团伙中，\x01",
            "　多半也有专门负责运货的成员。）\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        "#11P#0305F（……运货的二人组！？）\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#5P#0001F（那些家伙为了来这里做生意，\x01",
            "　就必须要偷偷把假货\x01",
            "　运进克洛斯贝尔。）\x02\x03",

            "#0003F（如果一个人单独带着货物入境，\x01",
            "　肯定会非常显眼，未免太过艰难了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x104,
        (
            "#11P#0305F（也就是说……\x01",
            "　嫌疑人是那对兄妹旅行者，\x01",
            "　或是那位带着小孩的乘客吗？）\x02\x03",

            "#0306F（这个……再怎么说，\x01",
            "　未免也太过出人意表了吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x103,
        "#12P#0200F（……真的是那样的吗？）\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        "#5P#0005F（……哎？）\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        (
            "#12P#0203F（如果我是假货贩子，\x01",
            "　恐怕会把运货任务交给从车站和空港\x01",
            "　潜入克洛斯贝尔的那些同伴。）\x02\x03",

            "#0200F（和国境门不同，车站和空港\x01",
            "　并不会对共和国和帝国方面的\x01",
            "　入境人员进行太过严密的检查。）\x02\x03",

            "（所以，唐古拉姆门\x01",
            "　实在不是一条适合\x01",
            "　运送货物的路线。）\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        (
            "#12P#0103F（确实……）\x02\x03",

            "#0101F（这样看来，乘坐这辆巴士\x01",
            "　的假货商人，恐怕……\x01",
            "　是单独行动的可能性会比较高呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        "#5P#0005F单独行动……！？\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x102,
        (
            "#12P#0101F（嗯，而且……\x01",
            "　这个人，在假货商团伙中，\x01",
            "　应该也是个首领级别的角色。）\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        (
            "#11P#0305F（……是吗……）\x02\x03",

            "#0303F（像运货这种危险的任务，\x01",
            "　一般都会交给下面的人去做，这也是惯例。）\x02\x03",

            "（利用排除法来思考……\x01",
            "　车站或空港这两条线路\x01",
            "　是用来运送货物的……）\x02\x03",

            "#0301F（而头目则只携带着少量行李，\x01",
            "　完全不会被人怀疑，就这么毫无危险，\x01",
            "　悠哉悠哉地前往克洛斯贝尔吗。）\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#5P#0005F（原来是这么回事吗……）\x02\x03",

            "#0006F（多谢了，各位。\x01",
            "　看来是我考虑得不太周全。）\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        (
            "#12P#0100F（呵呵，没关系啦。\x01",
            "　如果总是将问题交给你一个人来思考，\x01",
            "　我们也会无法成长的。）\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x103,
        "#12P#0200F（也不能总是让前辈一个人出风头啊。）\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        "#11P#0309F（哈哈，说的对呢。）\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#5P#0001F（不过，这样一来……\x01",
            "　我也想到了一名\x01",
            "　可疑的人物呢。）\x02\x03",

            "#0003F（刚才，在和乘客们对话的时候……\x01",
            "　有一个人说的话让我十分在意。）\x02\x03",

            "#0001F（如果所料不差，\x01",
            "　那个人恐怕就是假货贩子的头目了。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2659")

    label("loc_2659")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0062
    ChrTalk(
        0x104,
        "#11P#0301F（就是你刚才说的那个家伙吗……）\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x103,
        "#12P#0203F（……嫌疑人还剩下五名。）\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(45920, 1100, -1670, 0)
    MoveCamera(358, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(18520, 0)
    OP_0D()
    SetMessageWindowPos(350, 0, -1, -1)

    #A0064
    AnonymousTalk(
        0x103,
        (
            "#0200F（①声称自己是要来克洛斯贝尔钓鱼的\x01",
            "　那个倔强乖僻的老人。）\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(43880, 1100, -1880, 0)
    MoveCamera(358, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(18520, 0)
    OP_0D()

    #A0065
    AnonymousTalk(
        0x103,
        (
            "#0200F（②说自己和孙子已经三年未见的\x01",
            "　那位温和的老婆婆。）\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(48010, 1100, -1960, 0)
    MoveCamera(52, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(17640, 0)
    OP_0D()

    #A0066
    AnonymousTalk(
        0x103,
        (
            "#0200F（③让人感觉到明显不是等闲之辈的\x01",
            "　那位黑发女性。）\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(49460, 1100, 1460, 0)
    MoveCamera(335, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(18520, 0)
    OP_0D()

    #A0067
    AnonymousTalk(
        0x103,
        (
            "#0200F（④对那位黑发女性抱有很深怀疑的\x01",
            "　那个年轻女性。）\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(50240, 1100, -1870, 0)
    MoveCamera(47, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(19450, 0)
    OP_0D()

    #A0068
    AnonymousTalk(
        0x103,
        (
            "#0200F（⑤还有，来往于克洛斯贝尔和共和国的\x01",
            "　那名贸易商人……）\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(51930, 1100, 120, 0)
    MoveCamera(328, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(23180, 0)
    OP_0D()

    #C0069
    ChrTalk(
        0x102,
        "#12P#0105F（不过，在这些人当中，真的有……？）\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#5P#0003F（……嗯，不会有错。）\x02\x03",

            "#0001F（在这些人之中，\x01",
            "　假货商人的头目正是……）\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_305B")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【老人】\x01",            # 0
            "【老婆婆】\x01",          # 1
            "【黑发女性】\x01",        # 2
            "【年轻的女性】\x01",      # 3
            "【贸易商】\x01",          # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A66"),
        (1, "loc_2A97"),
        (2, "loc_2AC6"),
        (3, "loc_2AF7"),
        (4, "loc_2B2A"),
        (SWITCH_DEFAULT, "loc_2B5B"),
    )


    label("loc_2A66")

    OP_60(0x0)

    #C0071
    ChrTalk(
        0x101,
        "#5P#0001F（……是那位老人。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0xE)
    Jump("loc_2B5B")

    label("loc_2A97")

    OP_60(0x0)

    #C0072
    ChrTalk(
        0x101,
        "#5P#0001F（是那位老婆婆。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0xF)
    Jump("loc_2B5B")

    label("loc_2AC6")

    OP_60(0x0)

    #C0073
    ChrTalk(
        0x101,
        "#5P#0001F（是那个黑发女性。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x10)
    Jump("loc_2B5B")

    label("loc_2AF7")

    OP_60(0x0)

    #C0074
    ChrTalk(
        0x101,
        "#5P#0001F（是那个年轻的女性。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x11)
    Jump("loc_2B5B")

    label("loc_2B2A")

    OP_60(0x0)

    #C0075
    ChrTalk(
        0x101,
        "#5P#0001F（是那个贸易商人。）\x02",
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x1, 0x12)
    Jump("loc_2B5B")

    label("loc_2B5B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0076
    ChrTalk(
        0x104,
        "#11P#0301F（……真的没错吗？）\x02",
    )

    CloseMessageWindow()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【没错】\x01",              # 0
            "【重新考虑一下】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2BC5"),
        (1, "loc_2E7E"),
        (SWITCH_DEFAULT, "loc_3056"),
    )


    label("loc_2BC5")

    OP_60(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0xF)"), scpexpr(EXPR_END)), "loc_2BDA")
    OP_2C(0x1B, 0x2)

    label("loc_2BDA")


    #C0077
    ChrTalk(
        0x101,
        (
            "#5P#0001F（……嗯。\x01",
            "　假货商人的头目，除了那个人\x01",
            "　之外，再没有别的可能了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x102,
        "#12P#0105F（是……这样啊。）\x02",
    )

    CloseMessageWindow()
    Sound(801, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("广播")

    #A0079
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──本巴士即将达到\x01",
            "克洛斯贝尔市东出口。\x02",
        )
    )

    CloseMessageWindow()

    #A0080
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在下车时，\x01",
            "请您注意不要遗失随身物品。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0081
    ChrTalk(
        0x103,
        "#12P#0200F（好像马上就要到站了呢。）\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x102,
        "#12P#0101F（……接下来就是重头戏了。）\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x101,
        (
            "#5P#0001F（到站之后，一定要\x01",
            "　盯紧嫌疑人。）\x02\x03",

            "（各位，请一定要集中注意力啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x104,
        (
            "#11P#0304F（不用你说我们也知道啦。）\x02\x03",

            "#0300F（罗伊德，首先由你\x01",
            "　去将嫌疑人的伪装\x01",
            "　揭开吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        "#5P#0001F（嗯，交给我吧……！）\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    Fade(500)
    OP_68(47810, 1100, -1860, 0)
    MoveCamera(44, 27, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(18710, 0)
    OP_0D()
    SetCameraDistance(17710, 2000)
    OP_6F(0x10)

    #C0086
    ChrTalk(
        0xC,
        "#11P#3403F………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3056")

    label("loc_2E7E")

    OP_60(0x0)

    #C0087
    ChrTalk(
        0x101,
        (
            "#5P#0003F（……这么一说，\x01",
            "　稍微有点没自信呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x104,
        "#11P#0306F（嘿……你在干什么嘛！）\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x102,
        "#12P#0106F（唉……打起精神来啊。）\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#5P#0011F（抱、抱歉，\x01",
            "　让我再重新考虑一下。）\x02\x03",

            "#0003F（那个时候……\x01",
            "　有个人明显的说漏了嘴，\x01",
            "　讲了些很奇怪的话。）\x02\x03",

            "（把某些根本就不可能发生的事情，\x01",
            "　说得理所当然……）\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x104,
        (
            "#11P#0300F（马上就要到克洛斯贝尔市了。\x01",
            "　赶快做出判断吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#5P#0001F（在这些人当中，\x01",
            "　假货商人的头目就是……）\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x1B, 0x2, 0xE)
    OP_29(0x1B, 0x2, 0xF)
    OP_29(0x1B, 0x2, 0x10)
    OP_29(0x1B, 0x2, 0x11)
    OP_29(0x1B, 0x2, 0x12)
    Jump("loc_3056")

    label("loc_3056")

    Jump("loc_29E8")

    label("loc_305B")

    FadeToDark(1000, 0, -1)
    OP_0D()
    BeginChrThread(0x15, 0, 0, 18)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x15, 0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    OP_24(0x1DA)
    SetScenarioFlags(0x5C, 0)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_15_15B2 end

    def Function_16_3110(): pass

    label("Function_16_3110")

    OP_25(0x1D4, 0x5A)
    Sleep(80)
    OP_25(0x1D4, 0x50)
    Sleep(80)
    OP_25(0x1D4, 0x46)
    Sleep(80)
    OP_25(0x1D4, 0x3C)
    Sleep(80)
    OP_25(0x1D4, 0x32)
    Sleep(80)
    OP_25(0x1D4, 0x28)
    Sleep(80)
    OP_25(0x1D4, 0x1E)
    Sleep(80)
    OP_25(0x1D4, 0x14)
    Sleep(80)
    OP_25(0x1D4, 0xA)
    Sleep(80)
    OP_25(0x1D4, 0x0)
    Return()

    # Function_16_3110 end

    def Function_17_3154(): pass

    label("Function_17_3154")

    OP_25(0x1DA, 0xA)
    Sleep(80)
    OP_25(0x1DA, 0x14)
    Sleep(80)
    OP_25(0x1DA, 0x1E)
    Sleep(80)
    OP_25(0x1DA, 0x28)
    Sleep(80)
    OP_25(0x1DA, 0x32)
    Sleep(80)
    OP_25(0x1DA, 0x3C)
    Sleep(80)
    OP_25(0x1DA, 0x46)
    Sleep(80)
    OP_25(0x1DA, 0x50)
    Sleep(80)
    OP_25(0x1DA, 0x5A)
    Sleep(80)
    OP_25(0x1DA, 0x64)
    Return()

    # Function_17_3154 end

    def Function_18_3198(): pass

    label("Function_18_3198")

    OP_25(0x1DA, 0x5A)
    Sleep(80)
    OP_25(0x1DA, 0x50)
    Sleep(80)
    OP_25(0x1DA, 0x46)
    Sleep(80)
    OP_25(0x1DA, 0x3C)
    Sleep(80)
    OP_25(0x1DA, 0x32)
    Sleep(80)
    OP_25(0x1DA, 0x28)
    Sleep(80)
    OP_25(0x1DA, 0x1E)
    Sleep(80)
    OP_25(0x1DA, 0x14)
    Sleep(80)
    OP_25(0x1DA, 0xA)
    Sleep(80)
    OP_25(0x1DA, 0x0)
    Return()

    # Function_18_3198 end

    SaveToFile()

Try(main)
