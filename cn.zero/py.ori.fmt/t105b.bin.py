from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t105b.bin",                # FileName
        "t105b",                    # MapName
        "t105b",                    # Location
        0x0043,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 67, 0, 4, 0, 5],
    )

    BuildStringList((
        "t105b",                  # 0
        "哈加经理",               # 1
        "洛琪",                   # 2
        "茜特拉丝",               # 3
        "游客",                   # 4
        "游客",                   # 5
        "游客",                   # 6
    ))

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch25600.itc",                   # 01
        "chr/ch25700.itc",                   # 02
        "chr/ch32300.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch20202.itc",                   # 06
        "chr/ch20302.itc",                   # 07
    ))

    DeclNpc(-479,    0,       10050,   180,  257,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-93959,  0,       8260,    270,  257,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(94190,   0,       11579,   90,   257,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-99480,  0,       -80559,  90,   257,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(97559,   150,     -84309,  90,   341,  0x0, 0,   6,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(100540,  150,     -84309,  270,  341,  0x0, 0,   7,   0,   255, 255, 0,   13,  255,  0)

    DeclActor(-20,     0,       8270,    1500,    -480,    1500,    10050,   0x007E, 0,  7,  0x0000)
    DeclActor(5500,    0,       13500,   1200,    5500,    1500,    13500,   0x007C, 0,  15, 0x0000)
    DeclActor(-96600,  0,       120560,  1500,    -96600,  1000,    120560,  0x007C, 0,  6,  0x0000)

    ScpFunction((
        "Function_0_208",          # 00, 0
        "Function_1_2C0",          # 01, 1
        "Function_2_321",          # 02, 2
        "Function_3_382",          # 03, 3
        "Function_4_3AD",          # 04, 4
        "Function_5_3CF",          # 05, 5
        "Function_6_3D0",          # 06, 6
        "Function_7_46F",          # 07, 7
        "Function_8_473",          # 08, 8
        "Function_9_4ED",          # 09, 9
        "Function_10_548",         # 0A, 10
        "Function_11_596",         # 0B, 11
        "Function_12_5FC",         # 0C, 12
        "Function_13_623",         # 0D, 13
        "Function_14_63C",         # 0E, 14
        "Function_15_120E",        # 0F, 15
    ))


    def Function_0_208(): pass

    label("Function_0_208")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_248"),
        (1, "loc_254"),
        (2, "loc_260"),
        (3, "loc_26C"),
        (4, "loc_278"),
        (5, "loc_284"),
        (6, "loc_290"),
        (SWITCH_DEFAULT, "loc_29C"),
    )


    label("loc_248")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_254")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_260")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_26C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_278")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_284")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_290")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_29C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_2A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2BF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2A8")

    label("loc_2BF")

    Return()

    # Function_0_208 end

    def Function_1_2C0(): pass

    label("Function_1_2C0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_320")
    OP_95(0xFE, -106030, 0, 8260, 2000, 0x0)
    OP_95(0xFE, -106030, 0, 11300, 2000, 0x0)
    OP_95(0xFE, -93960, 0, 11300, 2000, 0x0)
    OP_95(0xFE, -93960, 0, 8260, 2000, 0x0)
    Jump("Function_1_2C0")

    label("loc_320")

    Return()

    # Function_1_2C0 end

    def Function_2_321(): pass

    label("Function_2_321")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_381")
    OP_95(0xFE, 106130, 0, 11580, 2000, 0x0)
    OP_95(0xFE, 106130, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 11580, 2000, 0x0)
    Jump("Function_2_321")

    label("loc_381")

    Return()

    # Function_2_321 end

    def Function_3_382(): pass

    label("Function_3_382")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3AC")
    OP_94(0xFE, 0xFFFE730C, 0xFFFEC082, 0xFFFE8086, 0xFFFECBC2, 0x3E8)
    Sleep(400)
    Jump("Function_3_382")

    label("loc_3AC")

    Return()

    # Function_3_382 end

    def Function_4_3AD(): pass

    label("Function_4_3AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_3BC")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 14)

    label("loc_3BC")

    BeginChrThread(0x9, 0, 0, 1)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 3)
    Return()

    # Function_4_3AD end

    def Function_5_3CF(): pass

    label("Function_5_3CF")

    Return()

    # Function_5_3CF end

    def Function_6_3D0(): pass

    label("Function_6_3D0")

    OP_F2(0x3)
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_451")
    SoundLoad(13)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_451")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46D")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_46D")

    Return()

    # Function_6_3D0 end

    def Function_7_46F(): pass

    label("Function_7_46F")

    Call(0, 8)
    Return()

    # Function_7_46F end

    def Function_8_473(): pass

    label("Function_8_473")

    TalkBegin(0x8)

    #C0001
    ChrTalk(
        0x8,
        (
            "瓦吉先生带来的客人们……\x01",
            "要出门吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "如果准备享用晚餐的话，\x01",
            "推荐去商店街里面那家名为\x01",
            "『幸运』的西餐厅哦。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    # Function_8_473 end

    def Function_9_4ED(): pass

    label("Function_9_4ED")

    TalkBegin(0xFE)

    #C0003
    ChrTalk(
        0xFE,
        (
            "啊，瓦吉先生\x01",
            "不知跑到哪里去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "我还想再好好欣赏一下\x01",
            "他那美丽的面孔呢⊥\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_9_4ED end

    def Function_10_548(): pass

    label("Function_10_548")

    TalkBegin(0xFE)

    #C0005
    ChrTalk(
        0xFE,
        (
            "要申请\x01",
            "客房服务吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "请您稍等，\x01",
            "稍后会为您送上\x01",
            "葡萄酒与小吃。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_548 end

    def Function_11_596(): pass

    label("Function_11_596")

    TalkBegin(0xFE)

    #C0007
    ChrTalk(
        0xFE,
        (
            "呼～……\x01",
            "还好订到房间了……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "哎呀，一直坚持下来，\x01",
            "等待别人取消预订，\x01",
            "总算是有回报了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_596 end

    def Function_12_5FC(): pass

    label("Function_12_5FC")

    TalkBegin(0xFE)

    #C0009
    ChrTalk(
        0xFE,
        "为了纪念庆典的夜晚，干杯。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_5FC end

    def Function_13_623(): pass

    label("Function_13_623")

    TalkBegin(0xFE)

    #C0010
    ChrTalk(
        0xFE,
        "呵呵，干杯。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_623 end

    def Function_14_63C(): pass

    label("Function_14_63C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_6AB")
    SetChrPos(0x101, -97500, 0, 124700, 0)
    SetChrPos(0x102, -96400, 0, 124700, 0)
    SetChrPos(0x103, -96400, 0, 123500, 0)
    SetChrPos(0x104, -97500, 0, 123500, 0)
    SetChrPos(0x151, -98000, 0, 121100, 0)
    Jump("loc_76C")

    label("loc_6AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_70E")
    SetChrPos(0x101, -97500, 0, 124700, 0)
    SetChrPos(0x102, -96400, 0, 123500, 0)
    SetChrPos(0x103, -96400, 0, 124700, 0)
    SetChrPos(0x104, -97500, 0, 123500, 0)
    SetChrPos(0x151, -98000, 0, 121100, 0)
    Jump("loc_76C")

    label("loc_70E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_76C")
    SetChrPos(0x101, -97500, 0, 124700, 0)
    SetChrPos(0x102, -97500, 0, 123500, 0)
    SetChrPos(0x103, -96400, 0, 123500, 0)
    SetChrPos(0x104, -96400, 0, 124700, 0)
    SetChrPos(0x151, -98000, 0, 121100, 0)

    label("loc_76C")

    OP_68(-97030, 900, 124240, 0)
    MoveCamera(330, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(19350, 0)
    FadeToBright(2000, 0)
    SetCameraDistance(18350, 3000)
    OP_6F(0x10)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_889")

    #C0011
    ChrTalk(
        0x103,
        "#0202F#6P……好漂亮……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        "#5302F#6P呵呵，是啊……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#5006F#6P没想到晚上\x01",
            "居然会放烟花。\x02\x03",

            "#5000F这是纪念庆典的独有节目吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x104,
        (
            "#0300F#6P不，好像每天都会如此哦。\x02\x03",

            "主题公园的夜晚，\x01",
            "才刚刚开始吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3C")

    label("loc_889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_965")

    #C0015
    ChrTalk(
        0x103,
        "#5402F#6P……好漂亮……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x102,
        "#0102F#6P呵呵，是啊……\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#5006F#6P没想到晚上\x01",
            "居然会放烟花呢。\x02\x03",

            "#5000F这是纪念庆典独有的节目吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x104,
        (
            "#0300F#6P不，好像每天都会如此哦。\x02\x03",

            "主题公园的夜晚，\x01",
            "才刚刚开始吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3C")

    label("loc_965")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_A3C")

    #C0019
    ChrTalk(
        0x103,
        "#0202F#6P……好漂亮……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x102,
        "#0102F#6P呵呵，是啊……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#5006F#6P没想到晚上\x01",
            "居然会放烟花呢。\x02\x03",

            "#5000F这是纪念庆典独有的节目吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x104,
        (
            "#5600F#6P不，好像每天都会如此哦。\x02\x03",

            "主题公园的夜晚，\x01",
            "才刚刚开始吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3C")


    #C0023
    ChrTalk(
        0x151,
        (
            "#5704F#6P夜间游行，\x01",
            "还有被彩灯装点的观览车……\x02\x03",

            "呵呵，这可是向女孩子\x01",
            "示爱的绝佳场景哦。\x02\x03",

            "#5700F──那么，\x01",
            "我就先走一步啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-97750, 900, 123480, 2000)

    def lambda_B26():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B26)
    Sleep(50)

    def lambda_B36():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B36)
    Sleep(50)

    def lambda_B46():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B46)
    Sleep(50)

    def lambda_B56():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B56)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    #C0024
    ChrTalk(
        0x101,
        (
            "#5000F#11P这样啊……你是要去见\x01",
            "某位女士吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x151,
        "#5702F#6P呵呵，算是吧。\x02",
    )

    CloseMessageWindow()
    OP_93(0x151, 0xB4, 0x190)
    Sleep(300)

    #C0026
    ChrTalk(
        0x151,
        (
            "#5704F#11P那么，愿女神赐予你们幸运。\x02\x03",

            "#5702F如果你们没有搞砸的话，\x01",
            "我们就在拍卖会场中再见吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(1424, 255, 90, 0)    #voice#Lazy
    Sleep(500)
    OP_68(-99750, 900, 120550, 3500)
    OP_95(0x151, -100000, 0, 116800, 2000, 0x1)

    def lambda_C61():
        OP_95(0xFE, -100000, 0, 114300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x151, 1, lambda_C61)
    Sleep(300)

    def lambda_C7E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x151, 2, lambda_C7E)
    Sound(121, 0, 100, 0)
    WaitChrThread(0x151, 1)
    WaitChrThread(0x151, 2)
    Sound(890, 0, 100, 0)
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(-97040, 900, 124460, 0)
    MoveCamera(330, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17300, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_DDD")

    #C0027
    ChrTalk(
        0x104,
        (
            "#0306F#11P哎呀呀……\x01",
            "真是个嚣张的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x103,
        (
            "#0206F#12P既是不良团伙的头目，\x01",
            "又是上流阶级中的贵客……\x02\x03",

            "#0211F他在各方面都很可疑呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        (
            "#5304F#11P不过，说实话，他能够告诉我们\x01",
            "竞拍会的情报，真是帮大忙了。\x02\x03",

            "#5300F我们算是欠了他一个人情呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FDE")

    label("loc_DDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_EE0")

    #C0030
    ChrTalk(
        0x104,
        (
            "#0306F#11P哎呀呀……\x01",
            "真是个嚣张的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x103,
        (
            "#5406F#11P既是不良团伙的头目，\x01",
            "又是上流阶级中的贵客……\x02\x03",

            "#5411F他在各方面都很可疑呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        (
            "#0104F#12P不过，说实话，他能够告诉我们\x01",
            "竞拍会的情报，真是帮大忙了。\x02\x03",

            "#0100F我们算是欠了他一个人情呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FDE")

    label("loc_EE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_FDE")

    #C0033
    ChrTalk(
        0x104,
        (
            "#5606F#11P哎呀呀……\x01",
            "真是个嚣张的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        (
            "#0206F#12P既是不良团伙的头目，\x01",
            "又是上流阶级中的贵客……\x02\x03",

            "#0211F他在各方面都很可疑呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x102,
        (
            "#0104F#11P不过，说实话，他能够告诉我们\x01",
            "竞拍会的情报，真是帮大忙了。\x02\x03",

            "#0100F我们算是欠了他一个人情呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FDE")


    #C0036
    ChrTalk(
        0x101,
        "#5000F#11P嗯……\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_93(0x101, 0x87, 0x190)
    Sleep(300)

    #C0037
    ChrTalk(
        0x101,
        (
            "#5003F#5P──我们差不多也该\x01",
            "前往拍卖会场了。\x02\x03",

            "#5001F必须要想办法混过入口的检查，\x01",
            "潜入到会场里。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1078():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1078)
    Sleep(50)

    def lambda_1088():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1088)
    Sleep(50)

    def lambda_1098():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1098)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_10CD")

    #C0038
    ChrTalk(
        0x102,
        "#5301F#12P嗯……没错！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1112")

    label("loc_10CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_10F3")

    #C0039
    ChrTalk(
        0x103,
        "#5401F#12P是……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1112")

    label("loc_10F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1112")

    #C0040
    ChrTalk(
        0x104,
        "#5601F#12P明白！\x02",
    )

    CloseMessageWindow()

    label("loc_1112")

    SetCameraDistance(17600, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1167")
    AddParty(0x1, 0xEF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_1196")

    label("loc_1167")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1181")
    AddParty(0x2, 0xEF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_1196")

    label("loc_1181")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1196")
    AddParty(0x3, 0xEF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)

    label("loc_1196")

    SetChrPos(0x0, -99730, 0, 120850, 180)
    SetScenarioFlags(0xA4, 7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11C8")
    OP_29(0x24, 0x4, 0x40)
    Jump("loc_11DA")

    label("loc_11C8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x24, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11DA")
    OP_29(0x24, 0x4, 0x40)

    label("loc_11DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_11EB")
    OP_DE(0x2A, 0x0)
    Jump("loc_1208")

    label("loc_11EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_11FC")
    OP_DE(0x2B, 0x0)
    Jump("loc_1208")

    label("loc_11FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1208")
    OP_DE(0x2C, 0x0)

    label("loc_1208")

    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_14_63C end

    def Function_15_120E(): pass

    label("Function_15_120E")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0041
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "    ～楼梯间～\x01",
            "现在三楼的ＶＩＰ层\x01",
            "已被包场，\x01",
            "无关人士请勿入内。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_15_120E end

    SaveToFile()

Try(main)
