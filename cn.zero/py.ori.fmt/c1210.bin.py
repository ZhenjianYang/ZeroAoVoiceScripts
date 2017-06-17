from ZeroScenarioHelper import *

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
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 33, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1210",                  # 0
        "曹",                     # 1
        "黑月成员",               # 2
        "刘",                     # 3
        "银",                     # 4
        "艾玛搜查官",             # 5
        "达德利搜查官",           # 6
    ))

    AddCharChip((
        "chr/ch31500.itc",                   # 00
        "chr/ch06300.itc",                   # 01
        "chr/ch31400.itc",                   # 02
        "chr/ch06302.itc",                   # 03
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

    DeclNpc(6000,    0,       0,       270,  261,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-34979,  0,       1870,    270,  389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   2,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-72300,  0,       1900,    2000,    -72300,  1500,    1900,    0x007C, 0,  8,  0x0000)
    DeclActor(-37230,  0,       7940,    2000,    -37230,  1500,    7940,    0x007C, 0,  8,  0x0000)

    ScpFunction((
        "Function_0_220",          # 00, 0
        "Function_1_2D8",          # 01, 1
        "Function_2_334",          # 02, 2
        "Function_3_3E4",          # 03, 3
        "Function_4_432",          # 04, 4
        "Function_5_1DFD",         # 05, 5
        "Function_6_2496",         # 06, 6
        "Function_7_4D7A",         # 07, 7
        "Function_8_4DCB",         # 08, 8
    ))


    def Function_0_220(): pass

    label("Function_0_220")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_260"),
        (1, "loc_26C"),
        (2, "loc_278"),
        (3, "loc_284"),
        (4, "loc_290"),
        (5, "loc_29C"),
        (6, "loc_2A8"),
        (SWITCH_DEFAULT, "loc_2B4"),
    )


    label("loc_260")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_26C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_278")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_284")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_290")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_29C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_2A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_2B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_2C0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_2D7")

    Return()

    # Function_0_220 end

    def Function_1_2D8(): pass

    label("Function_1_2D8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F7")
    Event(0, 4)
    Jump("loc_311")

    label("loc_2F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_311")
    Event(0, 6)

    label("loc_311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_320")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 5)

    label("loc_320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_333")
    ClearChrFlags(0x9, 0x80)

    label("loc_333")

    Return()

    # Function_1_2D8 end

    def Function_2_334(): pass

    label("Function_2_334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A4")
    SetMapObjFrame(0xFF, "c122_tesri02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tama00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tama01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kuro01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato", 0x0, 0x1)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x4, 0x2)
    ClearMapObjFlags(0x5, 0x2)
    Jump("loc_3E3")

    label("loc_3A4")

    SetMapObjFrame(0xFF, "c122_tesri01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mae", 0x0, 0x1)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x1, 0x2)
    ClearMapObjFlags(0x2, 0x2)
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)

    label("loc_3E3")

    Return()

    # Function_2_334 end

    def Function_3_3E4(): pass

    label("Function_3_3E4")

    TalkBegin(0xFE)

    #N0001
    NpcTalk(
        0xFE,
        "男性",
        "让各位久等了。\x02",
    )

    CloseMessageWindow()

    #N0002
    NpcTalk(
        0xFE,
        "男性",
        (
            "──请进，\x01",
            "这里便是分公司的经理室。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_3E4 end

    def Function_4_432(): pass

    label("Function_4_432")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    OP_68(-2500, 900, 0, 0)
    MoveCamera(47, 33, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -1900, 0, -600, 90)
    SetChrPos(0x102, -1900, 0, 500, 90)
    SetChrPos(0x103, -3000, 0, -600, 90)
    SetChrPos(0x104, -3000, 0, 500, 90)
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 5600, 50, 0, 270)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03200.itp")
    FadeToBright(1000, 0)
    OP_0D()

    #N0003
    NpcTalk(
        0x8,
        "青年的声音",
        "#6P呀，欢迎欢迎。\x02",
    )

    CloseMessageWindow()
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
    OP_68(4500, 900, 0, 2000)
    SetCameraDistance(23500, 2000)
    MoveCamera(47, 27, 0, 2000)
    OP_6F(0x11)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 5700, 0, -1600, 270)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_92(0x8, 0x125C, 0xFFFFF5D8, 0x1F4)

    def lambda_614():
        OP_95(0xFE, 4700, 0, -2600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_614)
    WaitChrThread(0x8, 1)

    def lambda_632():
        OP_95(0xFE, 200, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_632)
    Sleep(1300)
    Fade(500)
    OP_68(-530, 1000, 80, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(21000, 0)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x10E, 0x0)

    #C0004
    ChrTalk(
        0x101,
        (
            "#6P#0003F初次见面，您好……\x02\x03",

            "#0000F我是克洛斯贝尔警察局·特别\x01",
            "任务支援科的罗伊德·班宁斯，请多指教。\x02",
        )
    )

    CloseMessageWindow()

    #N0005
    NpcTalk(
        0x8,
        "东方长相的青年",
        (
            "#3204F#11P呵呵……\x01",
            "彼此彼此，请多指教。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("东方长相的青年")

    #A0006
    AnonymousTalk(
        0xFF,
        (
            "我就是负责管理『黑月贸易公司』\x01",
            "克洛斯贝尔分公司的\x01",
            "曹·李。\x02\x03",

            "罗伊德先生……\x01",
            "还有艾莉小姐、兰迪先生、\x01",
            "缇欧小姐，应该没错吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
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
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0007
    ChrTalk(
        0x101,
        "#6P#0011F什么……\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#0105F为、为什么\x01",
            "连我们的名字都……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "#3204F#11P呵呵，那就不卖关子了，\x01",
            "因为我也是克洛斯贝尔时代周刊的忠实读者。\x02\x03",

            "#3200F在刊物上看到了有关你们的报道后，\x01",
            "就成为各位的支持者了。\x02\x03",

            "#3209F说来也有点不好意思，在那之后我就用了\x01",
            "一些方法，调查了诸位的名字。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        "#6P#0003F是、是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x104,
        (
            "#0306F#6P（喂喂……\x01",
            "  一上来就先发制人吗……）\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x103,
        "#3P#0201F（计谋派的能人……名不虚传呢。）\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#3209F#11P哎呀～就我个人来说，\x01",
            "能与各位见面，真是无比荣幸啊……\x02\x03",

            "#3200F请问，今日前来，有何贵干呢？\x02\x03",

            "难道说，敝公司的经营活动\x01",
            "出现了什么问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#6P#0006F……不，\x01",
            "并不是因为这个。\x02\x03",

            "#0001F其实，我们正在\x01",
            "调查与『彩虹剧团』\x01",
            "相关的事件。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "#3205F#11P『彩虹剧团』……\x01",
            "哦哦，就是那个很有名的剧团吧！\x02\x03",

            "#3206F哎呀～自从来到克洛斯贝尔之后，\x01",
            "我就一直想去看一次他们的表演呢。\x01",
            "但因为工作太忙，实在是腾不出时间。\x02\x03",

            "#3200F话说回来，\x01",
            "他们的新剧好像要公演了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        "#6P#0000F嗯，是的……\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x102,
        (
            "#0103F……其实，正是这次的新剧公演\x01",
            "稍微出了一点小问题。\x02\x03",

            "#0100F作为调查工作的一环，\x01",
            "我们希望能向您提几个问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "#3203F#11P唔……\x01",
            "好像是遇到了什么麻烦吧。\x02\x03",

            "#3200F我明白了，\x01",
            "愿闻其详。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21300, 1500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sleep(500)
    OP_68(270, 800, 4510, 0)
    MoveCamera(69, 21, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrPos(0x101, -2600, 50, 4000, 90)
    SetChrPos(0x102, -2600, 50, 5000, 90)
    SetChrPos(0x103, -2600, 0, 2200, 45)
    SetChrPos(0x104, -2300, 0, 1400, 45)
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 750, 50, 4500, 270)
    SetCameraDistance(20500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(300)

    #C0019
    ChrTalk(
        0x8,
        "#5P#3203F嗯……是『银』吗？\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#6P#0000F据我们所知，\x01",
            "卡尔瓦德共和国的东方人街\x01",
            "正是贵公司总部的所在地……\x02\x03",

            "所以我们猜测，您也许会了解些什么，\x01",
            "至少也该知道这个名字。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "#5P#3204F呵呵……原来如此。\x02\x03",

            "#3200F听阁下的意思，\x01",
            "似乎就是怀疑那个名为『银』的\x01",
            "犯罪者与我们存在着某种关系吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#6P#0003F不，我们完全没有那种意思。\x02\x03",

            "#0000F只是因为现有情报实在太少……\x01",
            "所以才抱着病急乱投医的想法，\x01",
            "前来拜访您的。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "#5P#3204F呵呵，也罢。\x02\x03",

            "#3200F我所知道的也只是些一般的情报……\x01",
            "关于『银』的传说，就让我来为诸位\x01",
            "进行稍微详细一些的介绍吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#6P#0001F……拜托您了。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "#5P#3200F──『银』这个名字，\x01",
            "在共和国的东方人街可是非常有名的。\x02\x03",

            "#3203F着黑衣、戴面具，\x01",
            "绝不露出真实面孔的神秘刺客……\x02\x03",

            "如影子般现身，如影子般离去，\x01",
            "只要是被他盯上的猎物，就绝无逃脱的可能……\x02\x03",

            "#3201F而且……接下来才是关键所在，\x01",
            "传说他拥有不老不死之身。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0026
    ChrTalk(
        0x101,
        "#6P#0005F不、不老不死？\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        "#0101F#6P那是怎么回事……\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "#5P#3203F据说，『银』作为刺客而行动，\x01",
            "至今似乎已有一百多年了。\x02\x03",

            "说到一百年前，正好是卡尔瓦德共和国\x01",
            "刚刚经过民主化的时期呢。\x02\x03",

            "#3201F而且，如果调查当时的记录，\x01",
            "确实会频繁发现『银』的名字。\x02\x03",

            "在动乱时期，众多政要人物一个接一个地\x01",
            "葬身于这个身着黑衣的神秘魔人手中。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0029
    ChrTalk(
        0x101,
        (
            "#6P#0003F……故事越来越\x01",
            "荒诞无稽了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x104,
        (
            "#0300F#4P果然只是个传说而已，\x01",
            "其实他根本就不存在吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        "#5P#3209F不——他是存在的。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0032
    ChrTalk(
        0x101,
        "#6P#0013F……！？\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x104,
        "#0301F#4P什么……？\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20300, 60000)

    #C0034
    ChrTalk(
        0x8,
        (
            "#5P#3202F在东方人街的黑道世界中，\x01",
            "『银』可并不只是传说而已。\x02\x03",

            "虽然他的真实身份未明，\x01",
            "但只要符合某些条件的话，就可以用钱\x01",
            "雇佣到这个最强的暗杀者……\x02\x03",

            "他精通所有的暗器和咒符之术，\x01",
            "是个身法迅如鬼神的黑暗武术家……\x02\x03",

            "关于他的存在，在那个世界是广为人知的。\x02\x03",

            "#3204F据传闻说，他被某个组织视作\x01",
            "重要的王牌，经常被派去执行任务……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x102,
        "#0101F#6P………………………………\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x103,
        "#0201F#12P……那个组织是……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#5P#3205F啊，对了。\x01",
            "那个『银』……\x02\x03",

            "据说，他最近好像在\x01",
            "东方人街中消失了踪迹呢。\x02\x03",

            "#3204F似乎接到了那个组织\x01",
            "交代的重大任务……\x02\x03",

            "#3202F因此，前往了某个自治州。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#6P#0013F你……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "#5P#3202F呵呵，怎么了吗？\x02\x03",

            "我还没有说出\x01",
            "那个组织的名字哦。\x02\x03",

            "#3209F至于那个自治州在何处，我也并不知道呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#6P#0010F可恶……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        (
            "#0103F#6P……看来，贵公司和\x01",
            "『鲁巴彻』并无区别呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "#5P#3204F呵呵，请不要把我们与那种\x01",
            "小小的地方组织相提并论……\x01",
            "本来是想这么说。\x02\x03",

            "但鲁巴彻也有自己的优势，在这座特殊的城市中，\x01",
            "他们确实拥有着无懈可击的适应性。\x02\x03",

            "#3200F不可否认，他们很强。\x01",
            "即使是我，也感到颇为棘手呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x104,
        "#0301F#4P喂喂……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x103,
        "#0211F#12P……说得可真坦白啊。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "#5P#3209F呵呵，我所说的也只是\x01",
            "『商业』方面的竞争而已哦。\x02\x03",

            "#3200F在克洛斯贝尔这个地方，\x01",
            "自由竞争可是受法律保护的……\x02\x03",

            "难道有什么问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        "#6P#0008F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)
    Sleep(300)

    #C0047
    ChrTalk(
        0x101,
        (
            "#6P#0003F……请容我一问。\x02\x03",

            "#0001F在与鲁巴彻的竞争中，\x01",
            "也涉及到了彩虹剧团吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0048
    ChrTalk(
        0x8,
        "#5P#3205F哦，怎么说……？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#6P#0001F之前，鲁巴彻商会的会长\x01",
            "曾向彩虹剧团提出邀请，\x01",
            "有意赞助他们去帝都进行演出。\x02\x03",

            "贵公司是否也曾考虑过\x01",
            "类似的事情呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "#5P#3204F呵呵，共和国那边\x01",
            "的确有此意向。\x02\x03",

            "但不巧的是，敝公司\x01",
            "的业务并不涉及演艺方面。\x02\x03",

            "#3201F──其实我也觉得很不可思议。\x02\x03",

            "那封恐吓信的末尾处，\x01",
            "为什么会署上那个名字呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        "#6P#0006F……原来如此。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, -2300, 0, 4000, 90)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0052
    ChrTalk(
        0x101,
        (
            "#6P#0003F──您提供的情报很有参考价值，\x01",
            "非常感谢您的合作。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B3E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1B3E)
    Sleep(100)

    def lambda_1B4E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1B4E)
    Sleep(300)

    #C0053
    ChrTalk(
        0x103,
        "#0205F#11P罗伊德前辈……？\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x104,
        "#0301F#11P喂，这样就行了吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0055
    ChrTalk(
        0x101,
        (
            "#0006F#5P就算继续问下去，\x01",
            "恐怕也不会再有什么收获了。\x02\x03",

            "#0000F而且，他们好像也很忙的，\x01",
            "我们差不多也该告辞了。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x102,
        "#0108F#5P……是啊。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "#5P#3204F呵呵，多谢体谅。\x02\x03",

            "#3205F──啊，对了，罗伊德先生。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 500)

    def lambda_1C91():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1C91)

    #C0058
    ChrTalk(
        0x101,
        "#6P#0013F……请问还有什么事吗？\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "#5P#3200F呵呵……\x01",
            "不要摆出那么可怕的表情嘛。\x02\x03",

            "我刚才说过……\x01",
            "我是各位的支持者，\x01",
            "这可是真心话哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        "#6P#0011F哎……\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "#5P#3204F这次的事件……\x01",
            "我也很感兴趣。\x02\x03",

            "身为你们的支持者，\x01",
            "很想知道你们会如何将此事解决……\x02\x03",

            "#3202F我非常期待最后的结果哦。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    SetScenarioFlags(0x5C, 0)
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_432 end

    def Function_5_1DFD(): pass

    label("Function_5_1DFD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00500.itc", 0x1E)
    LoadChrToIndex("apl/ch50237.itc", 0x1F)
    LoadEffect(0x0, "event\\ev202_00.eff")
    OP_68(6280, 900, 1830, 0)
    MoveCamera(50, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21760, 0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 5800, 0, 3300, 180)
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x2)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 5600, 50, 0, 270)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("青年的声音")

    #A0062
    AnonymousTalk(
        0xFF,
        "哎呀，真是得救了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(20760, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0063
    ChrTalk(
        0x8,
        (
            "#11P#3206F要是事态继续发展下去的话，\x01",
            "后果可真是难以预料呢……\x02\x03",

            "暗杀市长的嫌疑差一点\x01",
            "就落到我们的头上了。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#0700F哼……都是因为你和共和国派\x01",
            "的议员纠缠不清，事态才会至此。\x02\x03",

            "暗中把我的名字告知那个秘书的\x01",
            "帝国派议长——哈尔特曼……\x02\x03",

            "恐怕也是从鲁巴彻的\x01",
            "会长那里听来的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#11P#3204F嗯，应该是这样吧。\x02\x03",

            "他大概也没想到一个秘书\x01",
            "竟能做到图谋暗杀的地步……\x02\x03",

            "#3200F但毫无疑问，\x01",
            "他的目的明显就是利用我们，\x01",
            "来对共和国派造成打击。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#0702F哼，真是个有因必有果的城市。\x02\x03",

            "#0700F先不说那个……\x01",
            "你最好不要总是用『我们』这个词。\x02\x03",

            "我可不想与你们混为一谈。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#11P#3206F哎呀呀，还真是冷淡啊。\x02\x03",

            "#3200F算了，至于和议员那边的关系，\x01",
            "只要我有意，随时都可以斩断。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 5630, 0, -1610, 180)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_93(0x8, 0x2D, 0x190)
    OP_68(7110, 900, 1620, 1500)
    SetChrFlags(0x8, 0x4)

    def lambda_21F0():
        OP_96(0xFE, 0x1C84, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_21F0)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x5A, 0x190)
    OP_6F(0x1)
    Sleep(500)

    #C0068
    ChrTalk(
        0x8,
        (
            "#5P#3204F──正如之前传达给您的一样，\x01",
            "我们的攻势将在纪念庆典之后开始……\x02\x03",

            "#3210F最终日的准备就拜托您了，\x01",
            "『银』大人。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#5P哼……好吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x5A, 0x190)
    Sound(1569, 255, 100, 0)    #voice#Yin
    Sleep(1000)

    #C0070
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#5P到时间了──告辞。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayEffect(0x0, 0xFF, 0xB, 0x40, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(859, 0, 100, 0)
    SetChrChip(0x0, 0xB, 0x1E, 0x12C)

    def lambda_232D():
        OP_95(0xFE, 7300, 0, 3300, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_232D)

    def lambda_2347():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2347)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xB, 2)
    SetChrChip(0x1, 0xB, 0x0, 0x0)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    Sleep(1000)
    OP_68(7300, 900, 1000, 2000)
    MoveCamera(40, 17, 0, 2000)
    SetCameraDistance(18500, 2000)
    OP_6F(0x79)
    Sleep(300)

    #C0071
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#3209F哈哈……\x01",
            "还是老样子，总是这么神出鬼没的……\x02\x03",

            "#3210F不过，这个『到时间』……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x190)
    Sleep(300)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(130)
    SetChrSubChip(0x8, 0x1)
    Sleep(130)
    SetChrSubChip(0x8, 0x2)
    Sleep(130)
    SetChrSubChip(0x8, 0x3)
    Sound(882, 0, 100, 0)
    Sleep(500)
    OP_6F(0x10)

    #C0072
    ChrTalk(
        0x8,
        (
            "#11P#3204F呵呵……\x01",
            "到底是指什么『时间』呢。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    SetScenarioFlags(0x5C, 2)
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_1DFD end

    def Function_6_2496(): pass

    label("Function_6_2496")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30500.itc", 0x1E)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    LoadChrToIndex("apl/ch50237.itc", 0x20)
    OP_68(1100, 1100, 0, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -4300, 0, 0, 90)
    SetChrPos(0x102, -4300, 0, 0, 90)
    SetChrPos(0x103, -4300, 0, 0, 90)
    SetChrPos(0x104, -4300, 0, 0, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 2200, 0, 0, 270)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, 2800, 0, -1000, 270)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xC, -200, 0, 900, 90)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, 300, 0, 0, 90)
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00600.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03200.itp")
    FadeToBright(1000, 0)
    OP_0D()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0073
    AnonymousTalk(
        0xD,
        (
            "──曹先生，\x01",
            "今天真是劳扰甚多。\x02\x03",

            "如果方便的话，希望您能提供\x01",
            "更加详细的情况。那样一来，\x01",
            "我们才能为您提供更多帮助。\x02",
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

    #C0074
    ChrTalk(
        0x8,
        (
            "#3204F#11P呵呵，真是多谢您的好意。\x01",
            "不过，事情毕竟发生在深夜。\x02\x03",

            "#3200F袭击者究竟是何人，\x01",
            "为什么会以敝公司为目标，\x01",
            "我们实在是毫无头绪呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xD,
        (
            "#6P#0603F……话虽如此，但贵公司\x01",
            "的防卫战真是做得相当出色啊。\x02\x03",

            "#0600F虽然一楼和二楼的状况都惨不忍睹，\x01",
            "但是这间屋子却完好无损。\x02\x03",

            "在对手使用了重机枪武装的情况下，\x01",
            "你们到底是如何做到的呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "#3209F#11P哈哈，实在是不敢当。\x02\x03",

            "#3200F只是，最后还是让\x01",
            "袭击者逃掉了呢。\x02\x03",

            "#3206F我们这里有好几个人都被送往医院……\x01",
            "哎呀呀，真是场大灾难。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xD,
        (
            "#6P#0603F我们对此也深表同情。\x01",
            "那么──\x02",
        )
    )

    CloseMessageWindow()
    Sound(811, 0, 100, 0)
    Sleep(500)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrPos(0x101, -4800, -1000, 0, 90)

    #N0078
    NpcTalk(
        0x101,
        "罗伊德的声音",
        "#2P──打扰了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(103, 0, 100, 0)
    OP_68(-500, 1100, 0, 1500)
    SetCameraDistance(24000, 1500)
    SetChrPos(0x101, -4300, 0, 0, 90)

    def lambda_29C4():
        OP_96(0xFE, 0xFFFFF894, 0x0, 0xFFFFFDA8, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29C4)

    def lambda_29DE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_29DE)

    def lambda_29EF():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_29EF)
    Sleep(50)

    def lambda_29FF():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_29FF)

    def lambda_2A0C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2A0C)
    Sleep(50)

    def lambda_2A1C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2A1C)
    Sleep(150)

    def lambda_2A2C():
        OP_96(0xFE, 0xFFFFF894, 0x0, 0x1F4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A2C)

    def lambda_2A46():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2A46)
    Sleep(400)

    def lambda_2A5A():
        OP_96(0xFE, 0xFFFFF448, 0x0, 0xFFFFFDA8, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2A5A)

    def lambda_2A74():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2A74)
    Sleep(350)

    def lambda_2A88():
        OP_96(0xFE, 0xFFFFF448, 0x0, 0x1F4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2A88)

    def lambda_2AA2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2AA2)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0079
    ChrTalk(
        0xD,
        "#11P#0605F你们……！？\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xC,
        "#5P特、特别任务支援科……\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "#11P#3205F哦，罗伊德先生，\x01",
            "还有支援科的诸位也来了吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#6P#0003F打扰了，曹先生。\x02\x03",

            "#0000F虽然知道您很忙，但还是希望能占用您\x01",
            "少许时间，进行一些询问，不知是否方便？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "#11P#3204F嗯，当然没问题。\x02\x03",

            "#3210F──那么，达德利先生，\x01",
            "您辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xD,
        "#11P#0610F哼……失陪了！\x02",
    )

    CloseMessageWindow()

    def lambda_2C3E():

        label("loc_2C3E")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2C3E")

    QueueWorkItem2(0x101, 2, lambda_2C3E)

    def lambda_2C50():

        label("loc_2C50")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2C50")

    QueueWorkItem2(0x102, 2, lambda_2C50)

    def lambda_2C62():

        label("loc_2C62")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2C62")

    QueueWorkItem2(0x103, 2, lambda_2C62)

    def lambda_2C74():

        label("loc_2C74")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2C74")

    QueueWorkItem2(0x104, 2, lambda_2C74)

    def lambda_2C86():
        OP_98(0xFE, 0x0, 0x0, 0x640, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C86)

    def lambda_2CA0():
        OP_98(0xFE, 0x0, 0x0, 0x640, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2CA0)
    Sleep(200)

    def lambda_2CBD():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2CBD)

    def lambda_2CCA():
        OP_98(0xFE, 0x0, 0x0, 0x640, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2CCA)

    def lambda_2CE4():
        OP_98(0xFE, 0x0, 0x0, 0x640, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2CE4)
    Sleep(500)
    OP_68(-820, 1100, 110, 1000)

    def lambda_2D12():
        OP_96(0xFE, 0xFFFFF768, 0x0, 0x0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2D12)
    WaitChrThread(0xD, 1)
    WaitChrThread(0x101, 1)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xD)
    Sleep(300)

    #C0085
    ChrTalk(
        0xD,
        (
            "#12P#0603F（虽然有些窝火，不过……\x01",
            "　那家伙就交给你们了。）\x02\x03",

            "#0600F（尽可能多套出\x01",
            "  一些情报吧。）\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        "#0005F#5P（啊……是！）\x02",
    )

    CloseMessageWindow()

    def lambda_2DD4():
        OP_95(0xFE, -4800, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2DD4)
    Sleep(600)
    BeginChrThread(0xC, 3, 0, 7)
    Sleep(100)

    def lambda_2DFA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2DFA)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xD, 2)
    WaitChrThread(0xC, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    Sound(104, 0, 100, 0)
    OP_68(1100, 1000, 0, 1500)
    SetCameraDistance(22500, 1500)
    OP_92(0x101, 0xFFFFFF38, 0xFFFFFDA8, 0x1F4)

    def lambda_2E68():
        OP_95(0xFE, -200, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2E68)
    OP_92(0x102, 0xFFFFFF38, 0x1F4, 0x1F4)

    def lambda_2E8F():
        OP_95(0xFE, -200, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2E8F)
    OP_92(0x103, 0xFFFFFA88, 0xFFFFFDA8, 0x1F4)

    def lambda_2EB6():
        OP_95(0xFE, -1400, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2EB6)
    OP_92(0x104, 0xFFFFFA88, 0x1F4, 0x1F4)

    def lambda_2EDD():
        OP_95(0xFE, -1400, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2EDD)
    WaitChrThread(0x101, 1)

    def lambda_2EFB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2EFB)
    WaitChrThread(0x102, 1)

    def lambda_2F0C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2F0C)
    WaitChrThread(0x103, 1)

    def lambda_2F1D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2F1D)
    WaitChrThread(0x104, 1)

    def lambda_2F2E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2F2E)
    WaitChrThread(0x104, 2)
    OP_6F(0x11)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0087
    AnonymousTalk(
        0x8,
        (
            "呵呵，好久不见了啊。\x01",
            "罗伊德先生，还有各位。\x02\x03",

            "你们好像在纪念庆典的最终日\x01",
            "表现得颇为活跃吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)

    #C0088
    ChrTalk(
        0x101,
        (
            "#6P#0003F是从『银』那里得到的情报吗……\x02\x03",

            "#0001F──我们『特别任务支援科』\x01",
            "并不拘泥于通常的调查体制。\x02\x03",

            "正因如此，我们这次能否\x01",
            "别兜圈子，开诚布公地交谈呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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

    def lambda_3128():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3128)
    Sleep(50)

    def lambda_3138():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3138)
    WaitChrThread(0x104, 2)

    #C0089
    ChrTalk(
        0x8,
        "#3210F#11P哦……？\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x102,
        "#0105F#5P罗、罗伊德……？\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#5P#0006F与这个人交流的话，\x01",
            "互相试探也只是浪费时间而已。\x02\x03",

            "#0000F这次要问的事情有不少，\x01",
            "不如就单刀直入吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x104,
        (
            "#6P#0306F喂喂……\x01",
            "说得可真直接啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x103,
        (
            "#6P#0202F罗伊德前辈……\x01",
            "偶尔也很大胆呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        "#3202F#11P呵呵……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #C0095
    ChrTalk(
        0x8,
        "#11P#3209F#4S哈哈哈哈哈哈！\x02",
    )

    CloseMessageWindow()

    def lambda_3292():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3292)

    def lambda_329F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_329F)

    def lambda_32AC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_32AC)
    WaitChrThread(0x101, 2)
    Sleep(300)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sound(820, 0, 100, 0)
    Sleep(130)
    SetChrSubChip(0x8, 0x1)
    Sleep(130)
    SetChrSubChip(0x8, 0x2)
    Sleep(130)
    SetChrSubChip(0x8, 0x3)
    Sound(882, 0, 100, 0)
    Sleep(500)

    #C0096
    ChrTalk(
        0x8,
        (
            "#3204F#11P──不愧是罗伊德先生，\x01",
            "我果然没有看错人。\x02\x03",

            "#3210F好吧，\x01",
            "我也不喜欢\x01",
            "无意义地兜圈子。\x02\x03",

            "只要在我能回答的范围之内，\x01",
            "无论什么都可以告诉你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#6P#0004F──非常感谢。\x02\x03",

            "#0001F想询问您的，\x01",
            "主要是以下三点。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x0, 1)
    ClearScenarioFlags(0x0, 2)

    label("loc_33DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4938")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_346C")
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【关于袭击者的真实身份】\x01",      # 0
            "【关于今后的对策】\x01",            # 1
            "【关于琪雅的来历】\x01",            # 2
            "【放弃提问】\x01",                  # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_34CF")

    label("loc_346C")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【关于袭击者的真实身份】\x01",      # 0
            "【关于今后的对策】\x01",            # 1
            "【关于琪雅的来历】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_34CF")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_34F1"),
        (1, "loc_3C26"),
        (2, "loc_4262"),
        (3, "loc_492B"),
        (SWITCH_DEFAULT, "loc_4933"),
    )


    label("loc_34F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B51")

    #C0098
    ChrTalk(
        0x101,
        (
            "#6P#0001F关于昨晚的袭击者……\x01",
            "您确定就是鲁巴彻的成员吗？\x02\x03",

            "有没有可能是与他们\x01",
            "毫不相关的人所为呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "#3200F#11P呵呵……\x01",
            "你首先想到的是这方面的疑问吗？\x02\x03",

            "#3204F──刘，\x01",
            "你来回答他吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xA,
        "#11P是。\x02",
    )

    CloseMessageWindow()

    def lambda_35CB():
        OP_96(0xFE, 0x834, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_35CB)
    WaitChrThread(0xA, 1)
    Sleep(300)

    #C0101
    ChrTalk(
        0xA,
        (
            "#11P……袭击者们虽然都蒙住了面孔，\x01",
            "企图隐藏身份，但毫无疑问，\x01",
            "他们就是鲁巴彻的成员。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xA,
        (
            "#11P不光是武器装备相同，\x01",
            "更重要的是，连战斗习惯也很相似。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "#11P那种东西可不是\x01",
            "简简单单就能模仿出来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        "#6P#0005F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x104,
        (
            "#6P#0306F可是，如果真是如此，\x01",
            "就有点难以理解了。\x02\x03",

            "#0301F据说，你们『黑月』的成员\x01",
            "全都是相当厉害的武术家。\x02\x03",

            "#0300F这位老兄，你的身手\x01",
            "想必也相当了得吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xA,
        "#11P……不敢当。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x104,
        (
            "#6P#0303F而鲁巴彻那边，\x01",
            "虽然也称得上是专业战斗者，\x01",
            "但并不是人人都有你们这种水平……\x02\x03",

            "既然如此，你们为何却在\x01",
            "战斗中被他们压制到如此程度呢……\x02\x03",

            "#0301F难道那个人称『杀戮之熊』\x01",
            "的大叔也参加袭击行动了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "#3204F#11P不，那位营业总部部长\x01",
            "似乎并没有参加呢。\x02\x03",

            "#3200F身为他左右手的那些原猎兵，\x01",
            "好像也都没有参与其中。\x02\x03",

            "参加袭击的人，在鲁巴彻中\x01",
            "应该都是些战斗力普通的家伙吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        "#6P#0013F那为何还……\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        (
            "#11P──他们的战斗技术虽然一般，\x01",
            "但是力量与速度都非同寻常。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xA,
        (
            "#11P仅用单手就能轻松使用重型机关枪，\x01",
            "完全凭借力量强行突破进来。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xA,
        (
            "#11P正因如此，我们的防线被完全击溃，\x01",
            "一直被他们压制到了二楼。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x104,
        "#6P#0301F这……\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x103,
        "#6P#0201F………………………………\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x8,
        (
            "#3200F#11P不光是力量和速度，\x01",
            "他们的身体强韧度也非常惊人呢。\x02\x03",

            "#3204F拜其所赐，我们也只得\x01",
            "动用了一些危险的招数。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        "#0101F危、危险的招数……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#6P#0001F……看来，您本人\x01",
            "也是一位高手吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x8,
        (
            "#3210F#11P呵呵，与『银』大人相比的话，\x01",
            "在下这点微末道行与外行人别无二致。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_3B2D():
        OP_96(0xFE, 0xAF0, 0x0, 0xFFFFFC18, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3B2D)
    WaitChrThread(0xA, 1)
    Sleep(300)
    SetScenarioFlags(0x0, 0)
    Jump("loc_3C21")

    label("loc_3B51")


    #C0119
    ChrTalk(
        0x8,
        (
            "#3204F#11P虽然他们都蒙上了面孔，\x01",
            "企图隐瞒身份，但肯定都是\x01",
            "鲁巴彻的普通成员，绝不会有错。\x02\x03",

            "#3200F虽然他们的战斗技术很普通……\x01",
            "但却拥有异常的力量、速度、\x01",
            "以及身体强韧度。\x02\x03",

            "#3209F呵呵，这究竟是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C21")

    Jump("loc_4933")

    label("loc_3C26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_419C")

    #C0120
    ChrTalk(
        0x101,
        (
            "#6P#0003F那我就不绕圈子，直接发问了。\x02\x03",

            "#0001F──遭遇到了这种事件，\x01",
            "您今后打算如何应对呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x8,
        (
            "#3210F#11P呵呵……\x01",
            "原来你只是想问这个啊。\x02\x03",

            "如果你想一想我们是做哪行的，\x01",
            "这个问题也就没必要再问了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        "#6P#0013F………………………………\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x102,
        "#0103F报复——是这样吧。\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x8,
        (
            "#3204F#11P呵呵，\x01",
            "别说得那么难听嘛。\x02\x03",

            "说到底，我们毕竟是一家商业公司……\x01",
            "我刚刚说的，也只是『危机管理』而已。\x02\x03",

            "#3210F当遇到公司利益受损的状况时，\x01",
            "就要用适当的方法来改善它……\x02\x03",

            "这有什么不对吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x104,
        "#6P#0301F唔……\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x103,
        (
            "#6P#0211F……同样的话，\x01",
            "果然还是要看使用哪种说法啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0127
    ChrTalk(
        0x101,
        (
            "#6P#0001F所谓的『适当的方法』，其中也包括\x01",
            "向贵公司的『总部』提出增援请求吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0128
    ChrTalk(
        0x102,
        "#0108F啊……\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x104,
        "#6P#0301F向『黑月』的总部要求增援吗……\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x8,
        (
            "#3209F#11P哈哈，还真是坦诚直率的人啊。\x02\x03",

            "#3204F──我这个人也是很要面子的。\x01",
            "以现阶段来说，暂时还没有那个打算。\x02\x03",

            "#3210F不过，根据今后的发展情况，\x01",
            "也不能完全排除『总部』那边\x01",
            "强行介入此事的可能性……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        "#6P#0013F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x8,
        (
            "#3200F#11P呵呵，当然，至少在短期之内，\x01",
            "应该还能抑制住总部直接干涉的意愿吧。\x02\x03",

            "#3204F──不管怎么说，\x01",
            "在未能彻底摸清对方状况的情势下，\x01",
            "我们也无法做出有效的应对。\x02\x03",

            "如今，我们正在请人\x01",
            "帮忙打探那边的情况呢。\x02\x03",

            "#3200F请的自然是那位最值得信赖的协助者。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x103,
        "#6P#0205F『银』吗……\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x104,
        (
            "#6P#0306F呼，在如今这种局势下，\x01",
            "他确实是最合适的人选吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_425D")

    label("loc_419C")


    #C0135
    ChrTalk(
        0x8,
        (
            "#3204F#11P虽然存在『总部』介入的可能性，\x01",
            "但在现阶段，我仍然希望由我们\x01",
            "克洛斯贝尔分公司来独自处理此事。\x02\x03",

            "#3200F如今，我们正在请人\x01",
            "帮忙打探那边的情况呢。\x02\x03",

            "请的自然是那位最值得信赖的协助者。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_425D")

    Jump("loc_4933")

    label("loc_4262")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4860")

    #C0136
    ChrTalk(
        0x101,
        (
            "#6P#0003F这个问题或许与此次事件\x01",
            "并没有直接的关系，\x01",
            "但机会难得，请容我一问。\x02\x03",

            "#0001F──您真的不清楚\x01",
            "有关琪雅的事情吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_42ED():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_42ED)
    Sleep(50)

    def lambda_42FD():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_42FD)
    Sleep(300)

    #C0137
    ChrTalk(
        0x103,
        "#6P#0205F啊……\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x102,
        "#0101F#5P罗伊德，那个……\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x8,
        (
            "#3205F#11P唔，琪雅……吗？\x02\x03",

            "#3209F那是人名吗？\x01",
            "还是什么暗号呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        "#6P#0013F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "#3206F#11P失礼了──\x01",
            "看来你是认真的啊。\x02\x03",

            "#3200F我只知道，\x01",
            "这是在那场竞拍会上\x01",
            "被你们解救的少女的名字。\x02\x03",

            "也知道我们那位协助者\x01",
            "当时曾给过你们几句建议。\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x3C, 0x1F4)
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(500)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0142
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "在那里面的房间中，\x01",
            "存放着将在竞拍会后半场展出的拍卖品……\x02\x03",

            "根据『黑月』收到的情报，\x01",
            "里面似乎藏着很有趣的『炸弹』哦。\x02\x03",

            "你们不妨去亲眼确认一下吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)

    def lambda_451B():
        OP_93(0xFE, 0x5A, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_451B)

    def lambda_4528():
        OP_93(0xFE, 0x5A, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4528)
    FadeToBright(500, 0)
    OP_0D()
    VolumeBGM(0x64, 0x1F4)
    Sleep(500)

    #C0143
    ChrTalk(
        0x8,
        (
            "#3203F#11P『将会在竞拍会的最后\x01",
            "  被展出的大皮箱……』\x02\x03",

            "『那里面放有威胁到鲁巴彻\x01",
            "  地位的「炸弹」』\x02\x03",

            "#3201F──这则情报，通过种种的\x01",
            "复杂途径，最终传到了我们这里。\x02\x03",

            "情报提供者不详……\x01",
            "虽然直到最后也没能查出他的身份，\x01",
            "但这反而增加了它的可信度。\x02\x03",

            "#3204F因此，谨慎起见，我们便委托\x01",
            "那位协助者去确认一下。\x02\x03",

            "#3210F但真是做梦也没有想到，\x01",
            "那个『炸弹』的真面目\x01",
            "竟然是这样的。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x104,
        (
            "#6P#0301F真是的，怎么每个人\x01",
            "都一口咬定自己毫不知情。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x102,
        (
            "#0106F如果这些话都是真的……\x02\x03",

            "#0101F那么，关于那位情报提供者，\x01",
            "您有什么猜测吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x8,
        (
            "#3204F#11P这个嘛，按照常理来考虑的话，\x01",
            "应该是鲁巴彻那边\x01",
            "出现了内鬼。\x02\x03",

            "通过其传达情报的高超手段也能看出，\x01",
            "他似乎是个毫无破绽的精干之辈呢。\x02\x03",

            "#3200F──总而言之，关于琪雅的事情，\x01",
            "我们所知道的也只有这么多。\x02\x03",

            "不知各位可否相信呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            "#6P#0006F……明白了，\x01",
            "感谢您坦率的回答。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4926")

    label("loc_4860")


    #C0148
    ChrTalk(
        0x8,
        (
            "#3203F#11P关于琪雅的身世，\x01",
            "很遗憾，我们也一无所知。\x02\x03",

            "#3200F如果我们的情报网\x01",
            "今后探查到了类似的人物，\x01",
            "也会通知各位一声的。\x02\x03",

            "#3209F──我们也曾因为处理不当而引发误会，\x01",
            "权当作是向各位表示歉意吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4926")

    Jump("loc_4933")

    label("loc_492B")

    SetScenarioFlags(0x0, 3)
    Jump("loc_4933")

    label("loc_4933")

    Jump("loc_33DC")

    label("loc_4938")


    #C0149
    ChrTalk(
        0x8,
        (
            "#3200F#11P那么……\x01",
            "您的问题就只有这些了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#6P#0003F嗯，感谢您耐心\x01",
            "解答了这么多疑问。\x02\x03",

            "#0001F我可以将这次对话的内容概要\x01",
            "报告给警察局总部吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x8,
        (
            "#3204F#11P呵呵，请随意……\x02\x03",

            "#3200F──啊，罗伊德先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        "#6P#0005F嗯……？\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x8,
        (
            "#3200F#11P老实说，这次的袭击，\x01",
            "颇有些出乎我的意料。\x02\x03",

            "我本以为早就看透了\x01",
            "他们的战斗力、关系网，\x01",
            "以及思考定式。\x02\x03",

            "#3204F因此断定他们在当前的局势下\x01",
            "不会做出铤而走险的事情……\x02\x03",

            "#3210F然而，结果却完全颠覆了我的预测……\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x101,
        "#6P#0001F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x8,
        (
            "#3209F#11P哼哼，所以说，\x01",
            "我现在正处于极度兴奋的状态之中。\x02\x03",

            "事态发展居然会超出我的掌控，\x01",
            "像这样的情况，\x01",
            "真是已经多年未遇了啊。\x02\x03",

            "#3202F如此一来，我终于可以发挥全力，\x01",
            "尽情展现出所有的力量与智慧了……\x02\x03",

            "这愉悦的感觉，已让我热血沸腾了。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        "#6P#0013F！？\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x104,
        "#6P#0310F喂喂……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x102,
        "#0110F……你……\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x103,
        "#6P#0206F真是不得了……\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x8,
        (
            "#3204F#11P呵呵，我可没打算被\x01",
            "区区警察扫了兴致……\x02\x03",

            "不过，对于各位，姑且便破例一次，\x01",
            "提供一个特别的『机会』吧。\x02\x03",

            "#3202F在我们认真起来，正式展开行动之前，\x01",
            "你们能否拿出什么像样的解决方法呢……\x02\x03",

            "就让我好好期待一下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x5C, 3)
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_2496 end

    def Function_7_4D7A(): pass

    label("Function_7_4D7A")


    def lambda_4D7F():
        OP_95(0xFE, -1600, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4D7F)
    WaitChrThread(0xC, 1)

    def lambda_4D9D():
        OP_95(0xFE, -4800, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_4D9D)
    Sleep(900)

    def lambda_4DBA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_4DBA)
    WaitChrThread(0xC, 1)
    Return()

    # Function_7_4D7A end

    def Function_8_4DCB(): pass

    label("Function_8_4DCB")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0161
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门紧紧关着。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_8_4DCB end

    SaveToFile()

Try(main)
