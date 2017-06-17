from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t110b.bin",                # FileName
        "t110b",                    # MapName
        "t110b",                    # Location
        0x0046,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 70, 0, 1, 0, 2],
    )

    BuildStringList((
        "t110b",                  # 0
        "向导巴克雷",             # 1
        "琪雅",                   # 2
        "翠雀酒店方向",           # 3
    ))

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
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

    DeclNpc(0,       0,       23000,   180,  257,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 3,   0.0,                   2.0,                   -0.800000011920929,    400.0,                 [0.09999999403953552,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.0,                  -0.5,                  0.1599999964237213,    1.0])

    PlaceName(0.0, 0.0, -32.0, 0x0000, 0x0000, "翠雀酒店方向")

    ChipFrameInfo(460, 0)                                        # 0

    ScpFunction((
        "Function_0_1CC",          # 00, 0
        "Function_1_27C",          # 01, 1
        "Function_2_27D",          # 02, 2
        "Function_3_29C",          # 03, 3
        "Function_4_EB0",          # 04, 4
    ))


    def Function_0_1CC(): pass

    label("Function_0_1CC")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_204"),
        (1, "loc_210"),
        (2, "loc_21C"),
        (3, "loc_228"),
        (4, "loc_234"),
        (5, "loc_240"),
        (6, "loc_24C"),
        (SWITCH_DEFAULT, "loc_258"),
    )


    label("loc_204")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_210")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_21C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_228")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_234")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_240")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_24C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_258")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_264")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_27B")

    Return()

    # Function_0_1CC end

    def Function_1_27C(): pass

    label("Function_1_27C")

    Return()

    # Function_1_27C end

    def Function_2_27D(): pass

    label("Function_2_27D")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_295")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_295")

    Sound(126, 1, 80, 0)
    Return()

    # Function_2_27D end

    def Function_3_29C(): pass

    label("Function_3_29C")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    SetChrPos(0x101, 600, 200, 0, 0)
    SetChrPos(0xEF, -600, 200, 0, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 0, 750, 29220, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x4)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, 23000, 180)
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BE")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "◆在序章选择缇欧\x01",      # 0
            "◆在序章选择兰迪\x01",      # 1
            "◆不做变更\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_39D"),
        (1, "loc_3AB"),
        (5, "loc_3B9"),
        (SWITCH_DEFAULT, "loc_3B9"),
    )


    label("loc_39D")

    ClearScenarioFlags(0x121, 2)
    SetScenarioFlags(0x121, 3)
    ClearScenarioFlags(0x121, 4)
    Jump("loc_3BE")

    label("loc_3AB")

    ClearScenarioFlags(0x121, 2)
    ClearScenarioFlags(0x121, 3)
    SetScenarioFlags(0x121, 4)
    Jump("loc_3BE")

    label("loc_3B9")

    Jump("loc_3BE")

    label("loc_3BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 3)), scpexpr(EXPR_END)), "loc_3F8")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis247.itp")
    Jump("loc_45E")

    label("loc_3F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 4)), scpexpr(EXPR_END)), "loc_432")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis248.itp")
    Jump("loc_45E")

    label("loc_432")

    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis249.itp")

    label("loc_45E")

    OP_68(0, 3000, 15000, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(60000, 0)

    def lambda_491():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_491)
    Sleep(100)

    def lambda_4A9():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_4A9)
    FadeToBright(1000, 0)
    OP_68(0, 3000, 25000, 8000)
    Sleep(7000)
    OP_0D()
    Fade(1000)
    OP_68(0, 1000, 21000, 0)
    MoveCamera(35, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    SetCameraDistance(20000, 3500)
    OP_0D()
    Sleep(500)
    OP_9B(0x0, 0x8, 0x0, 0x3E8, 0x3E8, 0x0)
    OP_6F(0x79)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_599")

    #C0001
    ChrTalk(
        0x8,
        "#5P欢迎来到米修拉姆迎宾馆。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "#5P二位就是特别任务支援科的\x01",
            "罗伊德先生和艾莉小姐吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_737")

    label("loc_599")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_5FF")

    #C0003
    ChrTalk(
        0x8,
        "#5P欢迎来到米修拉姆迎宾馆。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "二位就是特别任务支援科的\x01",
            "罗伊德先生和缇欧小姐吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_737")

    label("loc_5FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_668")

    #C0005
    ChrTalk(
        0x8,
        "#5P欢迎来到米修拉姆迎宾馆。\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "#5P二位就是特别任务支援科的\x01",
            "罗伊德先生和兰迪先生吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_737")

    label("loc_668")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_6D3")

    #C0007
    ChrTalk(
        0x8,
        "#5P欢迎来到米修拉姆迎宾馆。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "#5P二位就是特别任务支援科的\x01",
            "罗伊德先生和诺艾尔小姐吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_737")

    label("loc_6D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_737")

    #C0009
    ChrTalk(
        0x8,
        "#5P欢迎来到米修拉姆迎宾馆。\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "#5P二位就是特别任务支援科的\x01",
            "罗伊德先生和瓦吉先生吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_737")


    #C0011
    ChrTalk(
        0x101,
        "#00000F#12P嗯，是的。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0012
    ChrTalk(
        0x101,
        "#00005F#12P哎？您好像是……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 3)), scpexpr(EXPR_END)), "loc_80E")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    #A0013
    AnonymousTalk(
        0x101,
        (
            "#00001F在竞拍会的时候，\x01",
            "为我们指路的向导吧……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_809")

    #A0014
    AnonymousTalk(
        0x103,
        "#00205F啊……没错。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_809")

    Jump("loc_910")

    label("loc_80E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 4)), scpexpr(EXPR_END)), "loc_892")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    #A0015
    AnonymousTalk(
        0x101,
        (
            "#00001F在竞拍会的时候，\x01",
            "为我们指路的向导吧……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_88D")

    #A0016
    AnonymousTalk(
        0x104,
        "#00305F哦？是吗？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_88D")

    Jump("loc_910")

    label("loc_892")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    #A0017
    AnonymousTalk(
        0x101,
        (
            "#00001F在竞拍会的时候，\x01",
            "为我们指路的向导吧……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_910")

    #A0018
    AnonymousTalk(
        0x102,
        "#00105F啊……的确如此呢。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_910")

    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)

    #C0019
    ChrTalk(
        0x8,
        (
            "#5P哈哈……\x01",
            "那时真是失礼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "#5P虽然我们的主人\x01",
            "得到了那种下场……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "#5P但以我为代表的众多佣人\x01",
            "被委任处理迎宾馆的管理事务，\x01",
            "可以继续在这里工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "#5P这也多亏迪塔市长的\x01",
            "关怀照顾。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#00004F#12P原来如此……\x01",
            "那真是再好不过了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_A7F")

    #C0024
    ChrTalk(
        0x102,
        (
            "#00102F#12P听说在通商会议时，\x01",
            "各国首脑全都\x01",
            "住在这里。\x02\x03",

            "#00109F真是辛苦各位了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C09")

    label("loc_A7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_ADE")

    #C0025
    ChrTalk(
        0x103,
        (
            "#00204F#12P在通商会议时，\x01",
            "各国首脑好像都住这里吧？\x02\x03",

            "#00202F各位真是辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C09")

    label("loc_ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_B42")

    #C0026
    ChrTalk(
        0x104,
        (
            "#00303F#12P在通商会议时，\x01",
            "各国的大人物好像\x01",
            "都住这里吧？\x02\x03",

            "#00300F真是辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C09")

    label("loc_B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_BA6")

    #C0027
    ChrTalk(
        0x109,
        (
            "#10103F#12P听说在通商会议时，\x01",
            "各国首脑都\x01",
            "住在这里呢……\x02\x03",

            "#10100F真是辛苦你们了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C09")

    label("loc_BA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_C09")

    #C0028
    ChrTalk(
        0x105,
        (
            "#10302F#12P在通商会议时，\x01",
            "那些大人物们好像\x01",
            "都住在这里吧？\x02\x03",

            "#10304F呵呵，辛苦你们了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C09")


    #C0029
    ChrTalk(
        0x8,
        (
            "#5P愧不敢当……\x01",
            "二位过奖了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(3665, 255, 100, 0)    #voice#KeA

    #N0030
    NpcTalk(
        0x9,
        "琪雅的声音",
        "#11P#12A#30W#N啊，来了来了！\x02",
    )
    #Auto

    CloseMessageWindow()

    def lambda_C66():

        label("loc_C66")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_C66")

    QueueWorkItem2(0x8, 2, lambda_C66)
    OP_68(0, 1000, 21500, 2000)
    BeginChrThread(0x9, 3, 0, 4)
    WaitChrThread(0x9, 3)
    OP_6F(0x79)
    EndChrThread(0x8, 0x2)

    #C0031
    ChrTalk(
        0x101,
        "#00002F#12P琪雅，原来你先到了啊。\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x9,
        (
            "#01109F#5P嗯，我正和修利一起\x01",
            "到处探险呢～\x02\x03",

            "#01110F听说那个晚餐会\x01",
            "马上就要开始了～\x02\x03",

            "罗伊德，你们也要\x01",
            "赶快入座哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#00004F#12P哈哈，知道了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_D88")

    #C0034
    ChrTalk(
        0x102,
        (
            "#00102F#12P那就拜托您\x01",
            "为我们带路了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5D")

    label("loc_D88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_DC0")

    #C0035
    ChrTalk(
        0x103,
        (
            "#00202F#12P那就拜托您\x01",
            "为我们带路了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5D")

    label("loc_DC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_DF8")

    #C0036
    ChrTalk(
        0x104,
        (
            "#00309F#12P那就麻烦你\x01",
            "给我们带路啦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5D")

    label("loc_DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_E2E")

    #C0037
    ChrTalk(
        0x109,
        (
            "#10102F#12P那就请您\x01",
            "给我们带路了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5D")

    label("loc_E2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_E5D")

    #C0038
    ChrTalk(
        0x105,
        (
            "#10302F#12P那就拜托你\x01",
            "来带路了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5D")

    OP_93(0x8, 0xB4, 0x1F4)
    Sleep(150)

    #C0039
    ChrTalk(
        0x8,
        (
            "#5P好的，\x01",
            "请随我来。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(20250, 1000)
    OP_6F(0x79)
    OP_0D()
    StopSound(126, 1000, 80)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("t113B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_29C end

    def Function_4_EB0(): pass

    label("Function_4_EB0")


    def lambda_EB5():
        OP_9B(0x1, 0xFE, 0xA, 0x1964, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_EB5)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_4_EB0 end

    SaveToFile()

Try(main)
