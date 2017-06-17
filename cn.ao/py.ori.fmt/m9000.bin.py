from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m9000.bin",                # FileName
        "m9000",                    # MapName
        "m9000",                    # Location
        0x00BE,                     # MapIndex
        "ed7353",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 190, 0, 1, 0, 2],
    )

    BuildStringList((
        "m9000",                  # 0
        "格蕾丝",                 # 1
        "神狼蔡特",               # 2
        "芙兰",                   # 3
        "约纳",                   # 4
        "阿巴斯",                 # 5
        "梅尔卡瓦九号机",         # 6
    ))

    AddCharChip((
        "chr/ch06000.itc",                   # 00
        "chr/ch02708.itc",                   # 01
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-15500,  -4980,   -23200,  180,  405,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(14000,   -2000,   13500,   1200,    14000,   -1000,   13500,   0x007C, 0,  12, 0x0000)

    ChipFrameInfo(468, 0)                                        # 0

    ScpFunction((
        "Function_0_1D4",          # 00, 0
        "Function_1_284",          # 01, 1
        "Function_2_2CC",          # 02, 2
        "Function_3_36F",          # 03, 3
        "Function_4_38B",          # 04, 4
        "Function_5_396",          # 05, 5
        "Function_6_62B",          # 06, 6
        "Function_7_871",          # 07, 7
        "Function_8_B7A",          # 08, 8
        "Function_9_D6C",          # 09, 9
        "Function_10_D91",         # 0A, 10
        "Function_11_DA3",         # 0B, 11
        "Function_12_F92",         # 0C, 12
        "Function_13_116E",        # 0D, 13
        "Function_14_1D0E",        # 0E, 14
        "Function_15_1D3A",        # 0F, 15
        "Function_16_1D77",        # 10, 16
        "Function_17_1DA0",        # 11, 17
        "Function_18_1DD3",        # 12, 18
        "Function_19_1E06",        # 13, 19
        "Function_20_1E39",        # 14, 20
        "Function_21_1E58",        # 15, 21
        "Function_22_1E77",        # 16, 22
        "Function_23_1E96",        # 17, 23
        "Function_24_1EDD",        # 18, 24
        "Function_25_1F10",        # 19, 25
        "Function_26_2239",        # 1A, 26
    ))


    def Function_0_1D4(): pass

    label("Function_0_1D4")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
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

    # Function_0_1D4 end

    def Function_1_284(): pass

    label("Function_1_284")

    Call(0, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_2A4")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x22, 0)
    Event(0, 13)
    Jump("loc_2CB")

    label("loc_2A4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BA")
    Event(0, 11)
    Jump("loc_2CB")

    label("loc_2BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CB")
    Event(0, 10)

    label("loc_2CB")

    Return()

    # Function_1_284 end

    def Function_2_2CC(): pass

    label("Function_2_2CC")

    OP_F0(0x1, 0x320)
    OP_1B(0x1, 0x0, 0x9)
    SetMapObjFrame(0xFF, "CA_stop", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_327")
    OP_70(0x1, 0x3C)
    SetMapObjFrame(0x3, "black_add", 0x2, "night")
    SetMapObjFrame(0x3, "blue", 0x2, "night")
    SetMapObjFrame(0xFF, "CA_stop", 0x0, 0x2)
    Jump("loc_357")

    label("loc_327")

    OP_70(0x1, 0x0)
    SetMapObjFrame(0x3, "black_add", 0x2, "day")
    SetMapObjFrame(0x3, "blue", 0x2, "day")
    SetMapObjFrame(0xFF, "CA_stop", 0x1, 0x2)

    label("loc_357")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36A")
    OP_70(0x2, 0x3C)
    Jump("loc_36E")

    label("loc_36A")

    OP_70(0x2, 0x0)

    label("loc_36E")

    Return()

    # Function_2_2CC end

    def Function_3_36F(): pass

    label("Function_3_36F")

    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -4750, -3200, -10350, 0)
    Return()

    # Function_3_36F end

    def Function_4_38B(): pass

    label("Function_4_38B")

    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x8, 0x80)
    Return()

    # Function_4_38B end

    def Function_5_396(): pass

    label("Function_5_396")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_4F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B4")
    Call(0, 6)
    Jump("loc_4ED")

    label("loc_3B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_465")

    #C0001
    ChrTalk(
        0x9,
        (
            "#01203F#3C过去的『幻之至宝』\x01",
            "最终选择了自我毁灭的道路……\x02\x03",

            "#01200F难保琪雅不会\x01",
            "得出与其相同\x01",
            "的结论。\x02\x03",

            "人类之子啊，快去将琪雅带回，\x01",
            "阻止那种情况的发生吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4ED")

    label("loc_465")


    #C0002
    ChrTalk(
        0x9,
        (
            "#01203F#3C琪雅未必不会像\x01",
            "当年的『幻之至宝』一样，\x01",
            "最后走上相同的道路。\x02\x03",

            "#01200F人类之子啊，快去将琪雅带回，\x01",
            "阻止那种情况的发生吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4ED")

    Jump("loc_627")

    label("loc_4F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_627")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CA")

    #C0003
    ChrTalk(
        0x9,
        (
            "#01203F#3C琪雅肯定就在\x01",
            "『大树』中的某个地方。\x02\x03",

            "#01200F如果不出意外，恐怕就在最深处……\x01",
            "与库罗伊斯家族的那个女孩，\x01",
            "还有身为幕后黑手的律师在一起。\x02\x03",

            "如果需要我的帮助，\x01",
            "随时都可以呼唤我。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_627")

    label("loc_5CA")


    #C0004
    ChrTalk(
        0x9,
        (
            "#01203F#3C琪雅肯定就在\x01",
            "『大树』中的某处。\x02\x03",

            "#01200F如果需要我的帮助，\x01",
            "随时都可以呼唤我。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_627")

    TalkEnd(0xFE)
    Return()

    # Function_5_396 end

    def Function_6_62B(): pass

    label("Function_6_62B")


    #C0005
    ChrTalk(
        0x9,
        (
            "#01203F#3C过去的『幻之至宝』\x01",
            "最终选择了自我毁灭的道路……\x02\x03",

            "罗伊德，我当时和你说过这件事。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#00001F嗯，那是为了防止自己\x01",
            "失去控制，伤害到本应守护\x01",
            "的人们……\x02\x03",

            "#00003F……身为『零之至宝』的琪雅\x01",
            "也会遭遇同样的下场吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x9,
        (
            "#01200F#3C……目前还无法断言。\x02\x03",

            "但琪雅已经化身为『零之至宝』，\x01",
            "并创造出了这棵可与女神之力\x01",
            "相匹敌的『大树』。\x02\x03",

            "如今谁也无法保证\x01",
            "这种巨大的力量\x01",
            "可以一直得到控制。\x02\x03",

            "#01203F也就是说，琪雅未必不会\x01",
            "与当年的『幻之至宝』\x01",
            "走上相同的道路。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        (
            "#00003F是吗……\x02\x03",

            "#00001F不，只要还有我们在，\x01",
            "就绝对不会让那种情况发生……！\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x9,
        "#01200F#3C……呵呵，这才像你。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 0)
    Return()

    # Function_6_62B end

    def Function_7_871(): pass

    label("Function_7_871")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_9FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_88F")
    Call(0, 8)
    Jump("loc_9F9")

    label("loc_88F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_985")

    #C0010
    ChrTalk(
        0x8,
        (
            "#02105F真没想到你们能\x01",
            "把亚里欧斯·马克莱因\x01",
            "打败啊。\x02\x03",

            "#02102F呵呵，\x01",
            "你们有了如此显著的成长，\x01",
            "姐姐我也很高兴呢☆\x02\x03",

            "#02104F凭你们现在的实力，无论面对什么难关，\x01",
            "也都可以顺利跨越的。\x02\x03",

            "#02109F大家继续努力，\x01",
            "共同迎接美好的结局吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_9F9")

    label("loc_985")


    #C0011
    ChrTalk(
        0x8,
        (
            "#02104F凭你们现在的实力，无论面对什么难关，\x01",
            "也都可以顺利跨越的。\x02\x03",

            "#02109F大家继续努力，\x01",
            "共同迎接美好的结局吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F9")

    Jump("loc_B76")

    label("loc_9FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_B76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B00")

    #C0012
    ChrTalk(
        0x8,
        (
            "#02104F我要趁在『大树』的这段时间，\x01",
            "尽量多拍些照片。\x02\x03",

            "#02100F回到通讯社之后，\x01",
            "我一定会把此次事件\x01",
            "的真相一举公开……\x02\x03",

            "#02102F所以你们一定要继续努力，\x01",
            "将这起事件完美解决哦！\x02\x03",

            "#02109F到时候，我一定会为你们\x01",
            "写一篇最棒的社会新闻！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_B76")

    label("loc_B00")


    #C0013
    ChrTalk(
        0x8,
        (
            "#02100F罗伊德，你们一定要继续努力，\x01",
            "将这起事件完美解决哦！\x02\x03",

            "#02109F到时候，我一定会为你们\x01",
            "写一篇最棒的社会新闻！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B76")

    TalkEnd(0xFE)
    Return()

    # Function_7_871 end

    def Function_8_B7A(): pass

    label("Function_8_B7A")


    #C0014
    ChrTalk(
        0x8,
        (
            "#02105F听说你们已经把\x01",
            "亚里欧斯·马克莱因打败了？\x02\x03",

            "#02106F呼……\x01",
            "真没想到你们\x01",
            "能做得这么出色……\x02\x03",

            "#02109F看来『克洛斯贝尔的英雄』\x01",
            "这个称号也要易主了呢。\x01",
            "哎呀呀～真是个爆炸性的消息！\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#00004F哈哈……太过奖了。\x02\x03",

            "#00000F而且，我认为亚里欧斯先生\x01",
            "依然是克洛斯贝尔的英雄，\x01",
            "这是不会改变的。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "#02104F呵呵……\x01",
            "罗伊德，你真是成长了不少呢。\x02\x03",

            "#02102F你们已经超越了亚里欧斯先生，\x01",
            "接下来，无论再面对什么难关，\x01",
            "也一定可以顺利跨越。\x02\x03",

            "#02109F大家继续努力，\x01",
            "共同迎接美好的结局吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        "#00000F是！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 0)
    Return()

    # Function_8_B7A end

    def Function_9_D6C(): pass

    label("Function_9_D6C")

    EventBegin(0x2)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    EventEnd(0x5)
    NewScene("e3020", 107, 0, 0)
    IdleLoop()
    Return()

    # Function_9_D6C end

    def Function_10_D91(): pass

    label("Function_10_D91")

    EventBegin(0x2)
    FadeToDark(0, 0, -1)
    OP_0D()
    PartySelect(2)
    EventEnd(0x5)
    Return()

    # Function_10_D91 end

    def Function_11_DA3(): pass

    label("Function_11_DA3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    SoundLoad(497)
    Call(0, 4)
    ClearChrFlags(0xD, 0x80)
    OP_78(0x0, 0xD)
    OP_49()
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_71(0x0, 0x1, 0x78, 0x0, 0x20)
    SetMapObjFlags(0x4, 0x4)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0xD, -20000, 8250, -17000, 0)
    OP_D5(0xD, 0x0, 0x4F588, 0x0, 0x0)

    def lambda_E30():
        OP_96(0xFE, 0xFFFFB1E0, 0xFFFFDFC6, 0xFFFFBD98, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_E30)

    def lambda_E4A():
        OP_D5(0xFE, 0x0, 0x4CE78, 0x0, 0x2328)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_E4A)
    OP_68(-20000, 12500, -17000, 0)
    MoveCamera(20, -25, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(40000, 0)
    OP_68(-20000, -1250, -17000, 10000)
    MoveCamera(10, 20, 0, 10000)
    SetCameraDistance(35000, 10000)
    SetEventSkip(0x0, "loc_EE1")
    Sound(497, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(7000)
    StopSound(497, 1000, 80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_EE1")

    EndChrThread(0xD, 0x1)
    EndChrThread(0xD, 0x2)
    SetChrPos(0xD, -20000, -8250, -17000, 315)
    OP_D5(0xD, 0x0, 0x4CE78, 0x0, 0x0)
    OP_70(0x0, 0x116)
    ClearMapObjFlags(0x4, 0x4)
    Call(0, 3)
    ClearChrFlags(0x0, 0x80)
    ClearChrBattleFlags(0x0, 0x8000)
    ClearChrFlags(0x1, 0x80)
    ClearChrBattleFlags(0x1, 0x8000)
    ClearChrFlags(0x2, 0x80)
    ClearChrBattleFlags(0x2, 0x8000)
    ClearChrFlags(0x3, 0x80)
    ClearChrBattleFlags(0x3, 0x8000)
    OP_68(-16200, -980, -20800, 0)
    MoveCamera(10, 16, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x0, -16200, -4980, -20800, 135)
    OP_69(0xFF, 0x0)
    Sleep(500)
    ClearMapFlags(0x8000000)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_11_DA3 end

    def Function_12_F92(): pass

    label("Function_12_F92")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B0, 0)), scpexpr(EXPR_END)), "loc_FD1")
    TalkBegin(0xFF)
    SetChrName("")

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "好像已经没有反应了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_1168")

    label("loc_FD1")

    EventBegin(0x1)

    #A0019
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有块水晶。\x01",
            "要触碰吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1166")
    Fade(500)
    SetChrPos(0x0, 12730, -2000, 12430, 54)
    SetChrPos(0x1, 12050, -2000, 13180, 54)
    SetChrPos(0x2, 11370, -2000, 11590, 54)
    SetChrPos(0x3, 10590, -2000, 12660, 54)
    OP_68(10200, 2000, 10420, 0)
    MoveCamera(16, 48, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(11000, 0)
    OP_0D()
    Sleep(500)
    SetMapObjFrame(0x3, "black_add", 0x2, "to_d")
    SetMapObjFrame(0x3, "blue", 0x2, "to_d")
    Sleep(1000)
    Sound(211, 0, 100, 0)
    Sleep(2000)
    SetMapObjFrame(0x3, "black_add", 0x2, "day")
    SetMapObjFrame(0x3, "blue", 0x2, "day")
    Fade(500)
    OP_68(5100, 1000, -3760, 0)
    MoveCamera(10, 32, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(22000, 0)
    OP_0D()
    Sound(155, 2, 100, 0)
    OP_71(0x1, 0x3C, 0x0, 0x0, 0x0)
    OP_82(0x64, 0x0, 0xBB8, 0x7D0)
    Sleep(2000)
    OP_70(0x1, 0x0)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0xC8, 0x3E8, 0x64)
    Sleep(1500)
    SetMapObjFrame(0xFF, "CA_stop", 0x1, 0x2)
    SetScenarioFlags(0x1B0, 0)

    label("loc_1166")

    EventEnd(0x5)

    label("loc_1168")

    ClearMapFlags(0x8000000)
    Return()

    # Function_12_F92 end

    def Function_13_116E(): pass

    label("Function_13_116E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1190")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_1190")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A4")
    AddParty(0x4, 0xFF, 0xFF)

    label("loc_11A4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B8")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_11B8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11CC")
    AddParty(0x9, 0xFF, 0xFF)

    label("loc_11CC")

    LoadChrToIndex("chr/ch06100.itc", 0x1E)
    LoadChrToIndex("chr/ch06710.itc", 0x1F)
    LoadChrToIndex("chr/ch06900.itc", 0x20)
    LoadChrToIndex("chr/ch06000.itc", 0x21)
    LoadChrToIndex("apl/ch50010.itc", 0x22)
    LoadEffect(0x0, "event\\eva02_00.eff")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis064.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis065.itp")
    SetMapObjFlags(0x4, 0x4)
    SetChrPos(0x101, -10750, -5000, -17000, 0)
    SetChrPos(0x102, -11650, -4900, -16800, 0)
    SetChrPos(0x103, -11500, -4900, -17650, 0)
    SetChrPos(0x104, -13350, -5000, -18600, 0)
    SetChrPos(0x109, -12150, -5000, -18750, 0)
    SetChrPos(0x105, -14400, -5000, -20000, 0)
    SetChrPos(0x106, -11200, -5000, -18950, 0)
    SetChrPos(0x10A, -12750, -5000, -19450, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    ClearChrFlags(0x7, 0x80)
    ClearChrBattleFlags(0x7, 0x8000)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -17200, -5000, -19900, 0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -16200, -4900, -20850, 0)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -17300, -4900, -19700, 0)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -4750, -3200, -10350, 0)
    SetChrFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(14280, 6300, -9970, 0)
    MoveCamera(331, 2, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(20430, 0)
    Sleep(1000)
    PlayBGM("ed7353", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x161), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(2000, 0)
    OP_68(14280, 6300, -9970, 10000)
    MoveCamera(355, -1, 0, 10000)
    OP_6E(1000, 10000)
    SetCameraDistance(6250, 10000)
    OP_0D()
    PlaceName2(340, 200, "c_plac57", 0x0, 3000)
    OP_6F(0x79)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x10A, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    BeginChrThread(0x8, 0, 0, 25)
    BeginChrThread(0xC, 0, 0, 14)
    BeginChrThread(0x10A, 0, 0, 17)
    BeginChrThread(0x106, 0, 0, 18)
    BeginChrThread(0x105, 0, 0, 19)
    BeginChrThread(0x109, 0, 0, 20)
    BeginChrThread(0x104, 0, 0, 21)
    BeginChrThread(0x103, 0, 0, 22)
    BeginChrThread(0x102, 0, 0, 23)
    BeginChrThread(0x101, 0, 0, 24)
    OP_68(-12130, 6300, -25840, 8000)
    MoveCamera(5, 4, 0, 8000)
    OP_6E(1000, 8000)
    SetCameraDistance(55600, 8000)
    OP_6F(0x79)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    BeginChrThread(0xA, 0, 0, 15)
    BeginChrThread(0xB, 0, 0, 16)
    OP_68(-9070, -2500, -16590, 0)
    MoveCamera(26, 3, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(17460, 0)
    Fade(500)
    OP_0D()
    OP_68(-11740, -4400, -13060, 7000)
    MoveCamera(339, 15, 0, 7000)
    OP_6E(1000, 7000)
    SetCameraDistance(15430, 7000)
    OP_6F(0x79)
    OP_68(-9910, -3500, -15330, 0)
    MoveCamera(345, 13, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(7890, 0)
    Fade(500)
    OP_0D()
    Sleep(500)

    #C0020
    ChrTalk(
        0x101,
        "#00007F#6P……这里是……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x102,
        "#00108F#6P真的在那棵大树之内吗……？\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x104,
        (
            "#00301F#6P虽然早就知道这棵树很大，\x01",
            "但也不至于如此夸张吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        (
            "#00208F#6P……莫非内部的空间\x01",
            "扭曲了吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    EndChrThread(0x8, 0x0)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x8, 0x2)
    SetChrPos(0x8, -4750, -3200, -10350, 0)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    OP_68(-9240, 4700, -5380, 0)
    MoveCamera(3, 8, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(12530, 0)
    OP_68(-8600, 7000, -5750, 6000)
    MoveCamera(2, -28, 0, 6000)
    OP_6E(1000, 6000)
    SetCameraDistance(23250, 6000)
    OP_6F(0x79)
    Sleep(1000)
    VolumeBGM(0x3C, 0x1F4)
    FadeToDark(500, 0, -1)
    Sound(824, 0, 80, 0)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    Sleep(200)
    Sound(4130, 255, 100, 0)    #voice#KeA
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0, 0x0)
    Sleep(200)
    Sound(3044, 255, 100, 0)    #voice#KeA
    OP_CC(0x0, 0x1, 0x3)
    Sleep(1000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    FadeToBright(800, 0)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    Sleep(500)

    #C0024
    ChrTalk(
        0x101,
        "#00013F#5P#N………………………………\x02",
    )

    CloseMessageWindow()
    OP_68(-10420, -3600, -12460, 6000)
    MoveCamera(321, 19, 0, 6000)
    OP_6E(1000, 6000)
    SetCameraDistance(16760, 6000)
    Sleep(3000)
    OP_6F(0x79)

    #C0025
    ChrTalk(
        0xA,
        (
            "#01909F#6P哈哈哈哈……\x01",
            "太漂亮了……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x109,
        (
            "#10101F#6P和身处外面时相比，\x01",
            "简直就像是完全不同的大树……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x106,
        (
            "#10708F#6P#N无数光芒……\x01",
            "都在被大树吸收。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0028
    ChrTalk(
        0xB,
        (
            "#02300F#6P该怎么说呢……就像是\x01",
            "导力网络的概念图啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "#02109F#6P嗯……话说回来，\x01",
            "到处都是值得拍照的好地方！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 0, 0, 26)
    Sleep(2000)
    Fade(500)
    OP_68(-9910, -3500, -15330, 0)
    MoveCamera(345, 13, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(8280, 0)
    OP_0D()
    Sleep(300)

    #C0030
    ChrTalk(
        0xC,
        (
            "#12100F#6P前方存在着\x01",
            "重力扭曲现象，\x01",
            "因此梅尔卡瓦无法继续前进了。\x02\x03",

            "除了徒步行进之外，恐怕别无它法。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x105,
        (
            "#10406F#5P哎呀呀，真麻烦啊。\x02\x03",

            "#10400F不过，只要到外围来，\x01",
            "就可以乘坐梅尔卡瓦驶向大树之外了。\x02\x03",

            "一旦有紧急情况，\x01",
            "我们可以随时离开大树。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)

    #C0032
    ChrTalk(
        0x101,
        "#00001F#11P是吗……知道了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 500)
    Sleep(300)

    #C0033
    ChrTalk(
        0x10A,
        (
            "#00603F#6P总之，我们首先要划分出\x01",
            "探索小组和待命小组。\x02\x03",

            "#00601F没有在这里悠闲眺望风景的时间了，\x01",
            "我们立刻行动吧，班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 500)
    Sleep(100)

    #C0034
    ChrTalk(
        0x101,
        "#00007F#5P是……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    EndChrThread(0x8, 0x0)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x0)
    OP_68(-8600, 7000, -5750, 0)
    MoveCamera(2, -28, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(5000, 2000)
    OP_0D()
    OP_6F(0x79)

    #C0035
    ChrTalk(
        0x101,
        (
            "#00003F#6P#N（琪雅应该就在\x01",
            "  这棵大树中的某个地方……）\x02\x03",

            "#00013F（……无论如何也要………\x01",
            "  将她找到！）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(3000, 2000)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_37()
    ClearMapObjFlags(0x4, 0x4)
    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearParty()
    PartySelect(0)
    PartySelect(2)
    OP_37()
    SetChrPos(0x0, -8000, -4990, -15300, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -1750, -3000, -7890, 0)
    BeginChrThread(0x8, 0, 0, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A7, 2)
    OP_29(0xB2, 0x1, 0x1)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0x6, 0x0, 0x64)
    ClearMapFlags(0x8000000)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    SetChrFlags(0x8, 0x8000)
    Return()

    # Function_13_116E end

    def Function_14_1D0E(): pass

    label("Function_14_1D0E")

    Sleep(2500)
    OP_95(0xFE, -15500, -4900, -21500, 2000, 0x0)
    OP_95(0xFE, -12100, -5000, -18300, 2000, 0x0)
    Return()

    # Function_14_1D0E end

    def Function_15_1D3A(): pass

    label("Function_15_1D3A")

    OP_95(0xFE, -15800, -4900, -21200, 1000, 0x0)
    OP_95(0xFE, -14120, -4900, -21350, 1000, 0x0)
    OP_95(0xFE, -13200, -5000, -20500, 1000, 0x0)
    Return()

    # Function_15_1D3A end

    def Function_16_1D77(): pass

    label("Function_16_1D77")

    OP_95(0xFE, -16000, -4900, -21350, 2000, 0x0)
    OP_95(0xFE, -14000, -5000, -19600, 2000, 0x0)
    Return()

    # Function_16_1D77 end

    def Function_17_1DA0(): pass

    label("Function_17_1DA0")

    Sleep(2250)
    OP_95(0xFE, -9850, -4900, -16800, 2000, 0x0)
    OP_95(0xFE, -8250, -5000, -17100, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_17_1DA0 end

    def Function_18_1DD3(): pass

    label("Function_18_1DD3")

    Sleep(2000)
    OP_95(0xFE, -8800, -5000, -16350, 3000, 0x0)
    OP_95(0xFE, -6750, -5000, -16000, 3000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_18_1DD3 end

    def Function_19_1E06(): pass

    label("Function_19_1E06")

    Sleep(2300)
    OP_95(0xFE, -11750, -5000, -17500, 2000, 0x0)
    OP_95(0xFE, -11250, -5000, -16350, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_19_1E06 end

    def Function_20_1E39(): pass

    label("Function_20_1E39")

    Sleep(2100)
    OP_95(0xFE, -7350, -5000, -14500, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_20_1E39 end

    def Function_21_1E58(): pass

    label("Function_21_1E58")

    Sleep(2150)
    OP_95(0xFE, -10300, -5000, -15500, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_21_1E58 end

    def Function_22_1E77(): pass

    label("Function_22_1E77")

    Sleep(1900)
    OP_95(0xFE, -9000, -5000, -15500, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_22_1E77 end

    def Function_23_1E96(): pass

    label("Function_23_1E96")

    Sleep(1800)
    OP_95(0xFE, -11900, -4800, -16700, 2000, 0x0)
    OP_95(0xFE, -10300, -5000, -13500, 2000, 0x0)
    OP_95(0xFE, -10000, -5000, -14000, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_23_1E96 end

    def Function_24_1EDD(): pass

    label("Function_24_1EDD")

    Sleep(1700)
    OP_95(0xFE, -9050, -4900, -15150, 2000, 0x0)
    OP_95(0xFE, -9120, -5000, -13060, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_24_1EDD end

    def Function_25_1F10(): pass

    label("Function_25_1F10")

    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_1F20():
        OP_96(0xFE, 0xFFFFF538, 0xFFFFF448, 0xFFFFE796, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1F20)

    def lambda_1F3A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1F3A)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 30, 0)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_1FA2():
        OP_96(0xFE, 0xFFFFFF74, 0xFFFFF448, 0xFFFFE53E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1FA2)

    def lambda_1FBC():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1FBC)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 50, 0)
    Sleep(1000)

    label("loc_2017")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2230")
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_202F():
        OP_96(0xFE, 0xFFFFF948, 0xFFFFF448, 0xFFFFD9F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_202F)

    def lambda_2049():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2049)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_20B1():
        OP_95(0xFE, -4800, -3200, -10140, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_20B1)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(2000)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2134():
        OP_96(0xFE, 0xFFFFF538, 0xFFFFF448, 0xFFFFE796, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2134)

    def lambda_214E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_214E)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_21B6():
        OP_96(0xFE, 0xFFFFFF74, 0xFFFFF448, 0xFFFFE53E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_21B6)

    def lambda_21D0():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_21D0)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 100, 0)
    Sleep(1000)
    Jump("loc_2017")

    label("loc_2230")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_1F10 end

    def Function_26_2239(): pass

    label("Function_26_2239")

    Sleep(200)

    label("loc_223C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_231F")
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_2254():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2254)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 100, 0)
    Sleep(700)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)

    def lambda_22B8():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_22B8)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 100, 0)
    Sleep(700)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(4000)
    Jump("loc_223C")

    label("loc_231F")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    Return()

    # Function_26_2239 end

    SaveToFile()

Try(main)
