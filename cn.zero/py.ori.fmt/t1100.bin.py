from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t1100.bin",                # FileName
        "t1100",                    # MapName
        "t1100",                    # Location
        0x0046,                     # MapIndex
        "ed7111",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 70, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1100",                  # 0
        "黑衣人",                 # 1
        "黑衣人",                 # 2
        "黑衣人",                 # 3
        "黑衣人",                 # 4
        "加尔西亚",               # 5
        "翠雀酒店方向",           # 6
    ))

    AddCharChip((
        "chr/ch36000.itc",                   # 00
        "chr/ch36100.itc",                   # 01
    ))

    DeclNpc(-2299,   0,       18149,   180,  453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(2299,    0,       18149,   180,  453,  0x0, 0,   1,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 11,  0.0,                   0.0,                   -1.0,                  100.0,                 [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.0,                  -0.0,                  0.19999998807907104,   1.0])

    PlaceName(0.0, 0.0, -32.0, 0x0000, 0x0000, "翠雀酒店方向")

    ScpFunction((
        "Function_0_1CC",          # 00, 0
        "Function_1_284",          # 01, 1
        "Function_2_2B3",          # 02, 2
        "Function_3_349",          # 03, 3
        "Function_4_11F2",         # 04, 4
        "Function_5_1230",         # 05, 5
        "Function_6_1275",         # 06, 6
        "Function_7_12BA",         # 07, 7
        "Function_8_12D0",         # 08, 8
        "Function_9_12E6",         # 09, 9
        "Function_10_12FC",        # 0A, 10
        "Function_11_1312",        # 0B, 11
    ))


    def Function_0_1CC(): pass

    label("Function_0_1CC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_20C"),
        (1, "loc_218"),
        (2, "loc_224"),
        (3, "loc_230"),
        (4, "loc_23C"),
        (5, "loc_248"),
        (6, "loc_254"),
        (SWITCH_DEFAULT, "loc_260"),
    )


    label("loc_20C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_218")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_224")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_230")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_23C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_248")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_254")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_260")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_26C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_283")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_26C")

    label("loc_283")

    Return()

    # Function_0_1CC end

    def Function_1_284(): pass

    label("Function_1_284")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_295")
    Event(0, 3)

    label("loc_295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 1)), scpexpr(EXPR_END)), "loc_2B2")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)

    label("loc_2B2")

    Return()

    # Function_1_284 end

    def Function_2_2B3(): pass

    label("Function_2_2B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F3")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "t1100_sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "t1100_sky_y", 0x1, 0x1)
    Jump("loc_317")

    label("loc_2F3")

    SetMapObjFrame(0xFF, "t1100_sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "t1100_sky_y", 0x0, 0x1)

    label("loc_317")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32F")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_32F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_342")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_342")

    Sound(126, 1, 80, 0)
    Return()

    # Function_2_2B3 end

    def Function_3_349(): pass

    label("Function_3_349")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch36000.itc", 0x1E)
    LoadChrToIndex("chr/ch36100.itc", 0x1F)
    LoadChrToIndex("chr/ch02200.itc", 0x20)
    OP_68(0, 1600, -23850, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(19210, 0)
    SetChrPos(0x101, 0, 0, -21970, 0)
    SetChrPos(0x102, -780, 0, -22750, 0)
    SetChrPos(0x103, 850, 0, -23240, 0)
    SetChrPos(0x104, 180, 0, -24710, 0)
    FadeToBright(1000, 0)
    OP_68(0, 1600, -22350, 1700)
    Sleep(1500)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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

    #C0001
    ChrTalk(
        0x101,
        "#0013F#5P啊……！\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x104,
        "#0301F#11P那个吗……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(3790, 500, 33620, 0)
    MoveCamera(26, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(80770, 0)
    PlaceName2(340, 200, "c_plac21", 0x0, 3000)
    MoveCamera(37, 23, 0, 8000)
    OP_6F(0x40)
    Sleep(500)
    Fade(500)
    OP_68(0, 1600, -22350, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(19210, 0)
    OP_0D()
    Sleep(500)

    #C0003
    ChrTalk(
        0x101,
        (
            "#0001F#5P那就是哈尔特曼议长宅邸……\x02\x03",

            "#0003F好华丽啊……\x01",
            "与其说是私人住宅，不如说是个城堡。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x102,
        (
            "#0103F#5P是啊，谁让他出身于克洛斯贝尔\x01",
            "家世悠久的名门贵族呢……\x02\x03",

            "#0100F据说，那个住宅在百年前，\x01",
            "也就是在帝国统治的时代，\x01",
            "是被当做总督宅邸而建造的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#0306F#11P再怎么说，这也太雄伟了吧。\x02\x03",

            "#0301F又不是真正的帝国大贵族。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x103,
        (
            "#0203F#11P在那种地方\x01",
            "举行的『竞拍会』……\x02\x03",

            "#0200F看来，规模一定不小呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        "#0008F#5P啊──\x02",
    )

    CloseMessageWindow()
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0008
    ChrTalk(
        0x101,
        "#0013F#5P那是……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(0, 1500, 26500, 0)
    MoveCamera(36, 16, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20210, 0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 1500, 25000, 5000)
    SetChrPos(0xC, -10, 800, 29110, 0)
    SetChrPos(0xA, -10, 800, 29110, 0)
    SetChrPos(0xB, -10, 800, 29110, 0)
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 3, 0, 5)
    Sleep(1000)
    BeginChrThread(0xB, 3, 0, 6)
    Sleep(1000)
    BeginChrThread(0xC, 3, 0, 4)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    OP_6F(0x1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis064.itp")

    #C0009
    ChrTalk(
        0xC,
        (
            "#3103F#5P──警备工作的安排和往年一样。\x02\x03",

            "#3101F但是，今年比较特别，考虑到『黑月』\x01",
            "的那些家伙有可能会耍什么手段。\x02\x03",

            "所以，除了持有邀请卡的宾客，\x01",
            "其他人一律不可放行。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xA,
        "#12P遵命！\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xB,
        "#6P副头目准备做什么呢？\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xC,
        (
            "#3104F#5P我来负责宅邸内部的警备工作。\x02\x03",

            "对方毕竟是神出鬼没的家伙，\x01",
            "提高警惕总没坏处吧。\x02\x03",

            "#3100F……说起来，\x01",
            "拍卖品全都搬进去了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xB,
        "#6P嗯，今天早上就办妥了。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xB,
        "#6P那个人偶应该是最后一个了。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xC,
        (
            "#3104F#5P这次的热门货物之一吗……\x01",
            "到底会拍到什么价格呢。\x02\x03",

            "#3101F总之，离开场还有几个小时。\x02\x03",

            "切勿掉以轻心啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xB,
        "#6P是……！\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xA,
        "#12P您辛苦了！\x02",
    )

    CloseMessageWindow()
    OP_93(0xC, 0x0, 0x1F4)

    def lambda_A94():
        OP_95(0xFE, -10, 800, 29110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_A94)
    Sleep(1200)

    def lambda_AB1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_AB1)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xC, 2)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    Sleep(500)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sleep(30)
    Sound(890, 0, 100, 0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    Fade(1000)
    SetChrPos(0x101, -3000, 0, -28000, 0)
    SetChrPos(0x102, -3570, 0, -29080, 0)
    SetChrPos(0x103, -2930, 0, -30390, 0)
    SetChrPos(0x104, -2350, 0, -28980, 0)
    OP_68(-2890, 3000, -29150, 0)
    MoveCamera(351, 14, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(15440, 0)
    OP_68(-2890, 1500, -29150, 3000)
    OP_6F(0x1)
    OP_0D()

    #C0018
    ChrTalk(
        0x104,
        (
            "#0301F#6P──出现了吗。\x02\x03",

            "那个大叔好像已经\x01",
            "到里面去了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x103,
        (
            "#0201F#6P就是那个名叫加尔西亚，\x01",
            "曾经当过猎兵的黑手党副头目吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x102,
        (
            "#0103F#6P宴会的开始时间\x01",
            "是晚上七点……\x02\x03",

            "#0101F他们好像从现在就开始警备工作了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    #C0021
    ChrTalk(
        0x101,
        (
            "#0001F#5P嗯……这正说明他们的\x01",
            "警惕心十分之强吧。\x02\x03",

            "#0008F该怎么办呢……\x02\x03",

            "虽然有邀请卡，\x01",
            "但好像也不是那么简单就能进去的。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x104,
        (
            "#0306F#6P而且，里面也有不少家伙\x01",
            "能认出我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        (
            "#0206F#6P看样子，需要采取\x01",
            "一些特别手段呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#0003F#5P……………………………\x02\x03",

            "#0000F……总之，\x01",
            "暂且离开这里吧。\x02\x03",

            "要是被那些人发现的话，\x01",
            "可就彻底前功尽弃了。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        "#0100F#6P是啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_DCF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DCF)
    Sleep(100)

    def lambda_DDF():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DDF)

    def lambda_DEC():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DEC)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_93(0x101, 0xB4, 0x0)
    OP_93(0x102, 0xB4, 0x0)
    OP_93(0x103, 0xB4, 0x0)
    OP_93(0x104, 0xB4, 0x0)
    OP_68(-2860, 1500, -32040, 3000)

    def lambda_E32():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E32)
    Sleep(200)

    def lambda_E4A():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E4A)
    Sleep(200)

    def lambda_E62():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E62)
    Sleep(400)

    def lambda_E7A():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E7A)
    Sleep(1000)
    VolumeBGM(0x28, 0x1F4)
    FadeToDark(500, 0, -1)
    Sound(915, 0, 100, 0)
    OP_0D()
    EndChrThread(0x103, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x101, 0x1)
    OP_C7(0x0, 0x800)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    Sleep(200)
    Sound(2179, 255, 65, 0)    #voice#KeA
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_C7(0x1, 0x800)
    FadeToBright(500, 0)
    OP_68(-2860, 1500, -32040, 0)
    MoveCamera(351, 14, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(17870, 0)
    BeginChrThread(0x103, 3, 0, 8)
    BeginChrThread(0x102, 3, 0, 9)
    BeginChrThread(0x104, 3, 0, 10)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0026
    ChrTalk(
        0x101,
        "#0005F#5P哎……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x104, 3)

    def lambda_F8A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F8A)
    Sleep(100)

    def lambda_F9A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F9A)

    def lambda_FA7():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_FA7)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    Fade(1000)
    OP_68(7430, 7600, 6620, 0)
    MoveCamera(329, 10, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(54410, 0)
    OP_68(2020, 7600, 3200, 8000)
    OP_0D()
    Sleep(1000)
    SetMessageWindowPos(5, 250, -1, -1)

    #A0027
    AnonymousTalk(
        0x101,
        (
            "#0005F#5P#40W（…………刚才那是……………）\x02\x03",

            "#0001F#40W（………幻听吗……还是………）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(1000)
    OP_68(-2860, 3000, -32040, 0)
    MoveCamera(351, 14, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(17870, 0)
    OP_68(-2860, 1500, -32040, 4000)
    OP_6F(0x1)
    OP_0D()

    #C0028
    ChrTalk(
        0x103,
        "#0205F#6P#N……罗伊德前辈？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0029
    ChrTalk(
        0x102,
        "#0105F#6P怎么了？\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#0008F#5P没什么……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_93(0x101, 0xB4, 0x1F4)

    #C0031
    ChrTalk(
        0x101,
        (
            "#0006F#5P──抱歉，\x01",
            "好像是我的错觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        "#0100F#6P？？？\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x104,
        (
            "#0300F#12P虽然不知道是怎么回事，\x01",
            "总之，先离开这里吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        "#0200F#6P#N………………………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0xA4, 1)
    OP_29(0x47, 0x1, 0x2)
    EventEnd(0x5)
    NewScene("t1010", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_3_349 end

    def Function_4_11F2(): pass

    label("Function_4_11F2")


    def lambda_11F7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11F7)
    OP_95(0xFE, -50, 800, 27060, 2000, 0x1)
    OP_95(0xFE, 0, 400, 25800, 2000, 0x0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_4_11F2 end

    def Function_5_1230(): pass

    label("Function_5_1230")


    def lambda_1235():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1235)
    OP_95(0xFE, -50, 800, 27060, 2000, 0x1)
    OP_95(0xFE, 700, 0, 23800, 2000, 0x0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_5_1230 end

    def Function_6_1275(): pass

    label("Function_6_1275")


    def lambda_127A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_127A)
    OP_95(0xFE, -50, 800, 27060, 2000, 0x1)
    OP_95(0xFE, -700, 0, 23800, 2000, 0x0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_6_1275 end

    def Function_7_12BA(): pass

    label("Function_7_12BA")


    def lambda_12BF():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12BF)
    Return()

    # Function_7_12BA end

    def Function_8_12D0(): pass

    label("Function_8_12D0")


    def lambda_12D5():
        OP_9B(0x0, 0xFE, 0x0, 0x578, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12D5)
    Return()

    # Function_8_12D0 end

    def Function_9_12E6(): pass

    label("Function_9_12E6")


    def lambda_12EB():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12EB)
    Return()

    # Function_9_12E6 end

    def Function_10_12FC(): pass

    label("Function_10_12FC")


    def lambda_1301():
        OP_9B(0x0, 0xFE, 0x0, 0x640, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1301)
    Return()

    # Function_10_12FC end

    def Function_11_1312(): pass

    label("Function_11_1312")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1387")

    #C0035
    ChrTalk(
        0x101,
        (
            "#0001F现在还是尽量避开\x01",
            "鲁巴彻那些家伙吧。\x02\x03",

            "虽然有邀请卡，\x01",
            "但好像并不是那么简单\x01",
            "就能混进去的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA4, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1478")

    #C0036
    ChrTalk(
        0x151,
        (
            "#5705F……哎，不是要去\x01",
            "精品店吗？\x02\x03",

            "#5702F不过，如果就这样直接进去，\x01",
            "然后被黑手党的那帮家伙发现，\x01",
            "好像也挺有趣的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x101,
        (
            "#0006F啊，不……\x01",
            "还是不要那么做了。\x02\x03",

            "#0001F为了不暴露身份，\x01",
            "先去精品店换上正装吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_14C0")

    label("loc_1478")


    #C0038
    ChrTalk(
        0x101,
        (
            "#0001F门口有人在看守……\x01",
            "进入会场之前，还是先到\x01",
            "精品店换上正装吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C0")

    Sleep(50)
    SetChrPos(0x0, 0, 200, -1700, 180)
    EventEnd(0x4)
    OP_68(0, 1600, -1700, 0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    Return()

    # Function_11_1312 end

    SaveToFile()

Try(main)
