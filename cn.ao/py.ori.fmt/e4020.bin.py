from ScenarioHelper import *

def main():
    CreateScenaFile(
        "e4020.bin",                # FileName
        "e4020",                    # MapName
        "e4020",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, -123000, 0, 106000, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4020",                  # 0
        "科洛蒂娅公主",           # 1
        "雷克特书记官",           # 2
        "洛克史密斯总统",         # 3
        "琪雅",                   # 4
        "滴",                     # 5
        "椅子",                   # 6
        "椅子",                   # 7
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(388, 0)                                        # 0

    ScpFunction((
        "Function_0_184",          # 00, 0
        "Function_1_1B9",          # 01, 1
        "Function_2_1BA",          # 02, 2
        "Function_3_1275",         # 03, 3
        "Function_4_12CA",         # 04, 4
        "Function_5_131F",         # 05, 5
        "Function_6_1374",         # 06, 6
        "Function_7_13C9",         # 07, 7
        "Function_8_141E",         # 08, 8
        "Function_9_1473",         # 09, 9
        "Function_10_24AC",        # 0A, 10
    ))


    def Function_0_184(): pass

    label("Function_0_184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_198")
    ClearScenarioFlags(0x22, 0)
    Event(0, 9)
    Jump("loc_1A7")

    label("loc_198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1A7")
    ClearScenarioFlags(0x22, 1)
    Event(0, 10)

    label("loc_1A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B8")
    Event(0, 2)

    label("loc_1B8")

    Return()

    # Function_0_184 end

    def Function_1_1B9(): pass

    label("Function_1_1B9")

    Return()

    # Function_1_1B9 end

    def Function_2_1BA(): pass

    label("Function_2_1BA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11000.itc", 0x1E)
    LoadChrToIndex("chr/ch12400.itc", 0x1F)
    SetChrPos(0x0, -55750, 0, 113000, 180)
    SetChrPos(0x1, -55100, 0, 114400, 180)
    SetChrPos(0x2, -53700, 0, 114400, 180)
    SetChrPos(0x3, -53000, 0, 113300, 270)
    SetChrPos(0x4, -52300, 0, 114700, 270)
    SetChrPos(0x5, -51200, 0, 114200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -53000, 0, -2900, 270)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -55000, 0, -2900, 90)
    OP_68(-54000, 1100, 113000, 0)
    MoveCamera(51, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15820, 0)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_316")

    #C0001
    ChrTalk(
        0x101,
        "#00005F#5P（那是……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_406")

    label("loc_316")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_345")

    #C0002
    ChrTalk(
        0x102,
        "#00105F#5P（那是……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_406")

    label("loc_345")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_378")

    #C0003
    ChrTalk(
        0x103,
        "#00205F#5P（……那是……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_406")

    label("loc_378")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AD")

    #C0004
    ChrTalk(
        0x104,
        "#00301F#5P（怎么回事……？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_406")

    label("loc_3AD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3DC")

    #C0005
    ChrTalk(
        0x109,
        "#10105F#5P（哎……？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_406")

    label("loc_3DC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_406")

    #C0006
    ChrTalk(
        0x105,
        "#10302F#5P（哦……？）\x02",
    )

    CloseMessageWindow()

    label("loc_406")

    StopBGM(0xFA0)
    OP_68(-54000, 1100, 100000, 3000)
    Sleep(1500)
    Fade(1000)
    OP_68(-54000, 1100, 3100, 0)
    MoveCamera(125, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_68(-54000, 1100, -2900, 3000)
    OP_0D()
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)
    Sleep(300)
    OP_68(-53970, 1100, -3250, 2000)
    MoveCamera(129, 16, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(14000, 2000)
    OP_6F(0x79)
    MoveCamera(133, 18, 0, 50000)
    SetCameraDistance(13270, 50000)
    Sleep(300)

    #C0007
    ChrTalk(
        0x8,
        (
            "#5P#07004F是吗……\x01",
            "你见到了露西学姐……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        (
            "#12P#11506F是啊，不久前，去雷米菲利亚\x01",
            "出差的时候，正好撞到她了。\x02\x03",

            "我本想立刻逃跑，\x01",
            "但还是被她逮住了呢。\x02\x03",

            "#11501F你猜我被她揍了几拳？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "#5P#07002F……一拳也没有。\x02\x03",

            "#07009F而且她肯定紧紧抱住了你，\x01",
            "还大哭了一场吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x9,
        "#12P#11501F……唔。\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "#5P#07004F呵呵……\x01",
            "因为我能体会到\x01",
            "露西学姐的心情。\x02\x03",

            "#07001F我想，她应该已经\x01",
            "察觉到前辈平时都在从事着\x01",
            "多么危险的工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x9,
        (
            "#12P#11506F唉……女人的直觉，\x01",
            "有时候真是敏锐得可怕啊。\x02\x03",

            "#11510F实在是太难对付了。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#5P#07004F呵呵，这都是你自作自受。\x02\x03",

            "#07008F……真是让人怀念啊。\x02\x01",

            "#07002F我一直都没能和雷欧学长他们见上一面，\x01",
            "以后要是有机会，真希望能开一场同学会。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        "#12P#11501F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "#5P#07003F……前辈，这种态度可不行哦。\x02\x03",

            "#07002F在这种时候，你应该回答：\x01",
            "『好啊，那我们就在米修拉姆\x01",
            "　办一场豪华盛宴吧！』才对。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "#12P#11504F哈哈……被你将了一军呢。\x02\x03",

            "#11500F虽然还无法做出承诺，\x01",
            "不过，我会尽量努力的。\x02\x03",

            "别抱太大期望，等我的消息吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "#5P#07009F明白了，\x01",
            "我十分期待那一天的到来。\x02\x03",

            "#07002F好，就聊到这里吧，\x01",
            "我先告辞了。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x9,
        (
            "#12P#11509F嗯，替我向基库\x01",
            "那家伙问声好。\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x8, 0xFFFF379C, 0xFFFFFC18, 0x15E)
    Sleep(300)
    OP_68(-52720, 1100, -2590, 3500)
    MoveCamera(133, 18, 0, 3500)
    SetCameraDistance(13270, 3500)

    def lambda_935():
        OP_95(0xFE, -51300, 0, -1000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_935)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x5A, 0x1F4)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x1)

    def lambda_975():
        OP_95(0xFE, -48300, 0, -1000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_975)
    Sleep(1000)

    def lambda_992():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_992)
    WaitChrThread(0x8, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x1)
    Sleep(300)

    #C0019
    ChrTalk(
        0x9,
        (
            "#11P#11506F哎呀呀……\x01",
            "她真的成长了呢。\x02\x03",

            "#11500F不愧是下任女王陛下，\x01",
            "你们也这么觉得吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#00011F……！\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x105,
        "#10302F呵呵，原来早就发现我们了呢。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-55530, 1100, -1440, 3000)
    MoveCamera(125, 21, 0, 3000)
    OP_6E(550, 3000)
    SetCameraDistance(16650, 3000)

    def lambda_A88():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_A88)
    SetChrPos(0x101, -56200, 0, 7600, 180)
    SetChrPos(0x102, -54900, 0, 7600, 180)
    SetChrPos(0x103, -55900, 0, 8700, 180)
    SetChrPos(0x104, -54600, 0, 8700, 180)
    SetChrPos(0x109, -56200, 0, 9800, 180)
    SetChrPos(0x105, -54900, 0, 9800, 180)

    def lambda_AFB():
        OP_97(0x101, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AFB)
    Sleep(50)

    def lambda_B18():
        OP_97(0x102, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B18)
    Sleep(50)

    def lambda_B35():
        OP_97(0x103, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B35)
    Sleep(50)

    def lambda_B52():
        OP_97(0x104, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B52)
    Sleep(50)

    def lambda_B6F():
        OP_97(0x109, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B6F)
    Sleep(50)

    def lambda_B8C():
        OP_97(0x105, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B8C)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    #C0022
    ChrTalk(
        0x101,
        (
            "#6P#00006F……抱歉，\x01",
            "我们并不是故意\x01",
            "要偷听的。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x102,
        (
            "#00103F#6P只是……\x01",
            "不由自主地听了下去。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x103,
        (
            "#6P#00202F说起来，艾莉前辈\x01",
            "好像听得津津有味呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    #C0025
    ChrTalk(
        0x102,
        "#5P#00112F缇、缇欧！\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x104,
        (
            "#00309F#6P哎呀～话说回来，还真是很奇怪啊。\x02\x03",

            "#00302F对方可是一国的公主，\x01",
            "你那种态度未免也太随便了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        (
            "#11503F#11P哦，因为她是我上学时的学妹。\x02\x03",

            "#11500F不过，并不是指主日学校，\x01",
            "而是杰尼丝王立学院。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x105,
        (
            "#10305F#6P杰尼丝王立学院……\x01",
            "那是利贝尔王国的\x01",
            "著名高等学府吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        (
            "#00108F#6P是的，那所学校\x01",
            "也接收了很多外国留学生……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x109,
        (
            "#6P#10105F也就是说，你是由\x01",
            "国家出资去留学的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x9,
        (
            "#11504F#11P不，只是私人赞助而已，\x01",
            "是吉利亚斯那大叔送我去的。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        "#6P#00013F！\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x9,
        (
            "#11504F#11P那么，我也\x01",
            "就此告辞啦。\x02\x03",

            "#11505F哦，对了，那两只老狐狸\x01",
            "好像叫你们去谈话吧？\x02\x03",

            "#11509F他们两个都是很棘手的人物，\x01",
            "你们可要多加小心哟～\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        "#6P#00011F啊……\x02",
    )

    CloseMessageWindow()

    def lambda_EFF():

        label("loc_EFF")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_EFF")

    QueueWorkItem2(0x101, 2, lambda_EFF)

    def lambda_F11():

        label("loc_F11")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_F11")

    QueueWorkItem2(0x102, 2, lambda_F11)

    def lambda_F23():

        label("loc_F23")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_F23")

    QueueWorkItem2(0x103, 2, lambda_F23)

    def lambda_F35():

        label("loc_F35")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_F35")

    QueueWorkItem2(0x109, 2, lambda_F35)

    def lambda_F47():

        label("loc_F47")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_F47")

    QueueWorkItem2(0x105, 2, lambda_F47)

    def lambda_F59():

        label("loc_F59")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_F59")

    QueueWorkItem2(0x104, 2, lambda_F59)

    def lambda_F6B():
        OP_95(0xFE, -57100, 0, -1400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F6B)
    WaitChrThread(0x9, 1)

    def lambda_F89():
        OP_95(0xFE, -57100, 0, 1900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_F89)
    WaitChrThread(0x9, 1)
    StopBGM(0x1770)
    Fade(500)
    OP_68(-54000, 1100, 103000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, -56200, 0, 98800, 0)
    SetChrPos(0x102, -54900, 0, 98800, 0)
    SetChrPos(0x103, -55900, 0, 99900, 0)
    SetChrPos(0x104, -54600, 0, 99900, 0)
    SetChrPos(0x109, -56200, 0, 101000, 0)
    SetChrPos(0x105, -54900, 0, 101000, 0)
    SetChrPos(0x9, -55500, 0, 103000, 0)
    ClearChrFlags(0x9, 0x4)
    OP_68(-54000, 1100, 113000, 5000)
    SetCameraDistance(17500, 5000)

    def lambda_1075():
        OP_95(0xFE, -55500, 0, 112500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1075)
    WaitChrThread(0x9, 1)

    def lambda_1093():
        OP_95(0xFE, -51500, 0, 112500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1093)
    WaitChrThread(0x9, 1)

    def lambda_10B1():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_10B1)
    Sleep(500)

    def lambda_10CE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_10CE)
    WaitChrThread(0x9, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0x9, 0x80)
    OP_6F(0x79)
    Fade(500)
    OP_68(-55640, 1100, 100200, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_0D()

    #C0035
    ChrTalk(
        0x103,
        (
            "#12P#00211F……还是老样子，\x01",
            "言行举止实在是太古怪了。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x105,
        (
            "#10304F#11P利贝尔下任女王的学长，\x01",
            "同时还是帝国的情报军官……\x02\x03",

            "#10302F呵呵，对他越来越有兴趣了。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x101,
        (
            "#12P#00003F……不管怎么说，\x01",
            "至少可以肯定，他是在\x01",
            "『铁血宰相』的指挥下行动。\x02\x03",

            "#00001F他究竟有何目的呢……\x01",
            "看来有必要调查清楚。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    SetScenarioFlags(0x142, 2)
    EventEnd(0x5)
    NewScene("c1550", 126, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1BA end

    def Function_3_1275(): pass

    label("Function_3_1275")


    def lambda_127A():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_127A)

    def lambda_1294():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1294)
    WaitChrThread(0xFE, 1)

    def lambda_12A9():
        OP_95(0xFE, -122600, 0, 205400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12A9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_3_1275 end

    def Function_4_12CA(): pass

    label("Function_4_12CA")


    def lambda_12CF():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12CF)

    def lambda_12E9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_12E9)
    WaitChrThread(0xFE, 1)

    def lambda_12FE():
        OP_95(0xFE, -122600, 0, 206600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12FE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_4_12CA end

    def Function_5_131F(): pass

    label("Function_5_131F")


    def lambda_1324():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1324)

    def lambda_133E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_133E)
    WaitChrThread(0xFE, 1)

    def lambda_1353():
        OP_95(0xFE, -121500, 0, 204600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1353)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_5_131F end

    def Function_6_1374(): pass

    label("Function_6_1374")


    def lambda_1379():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1379)

    def lambda_1393():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1393)
    WaitChrThread(0xFE, 1)

    def lambda_13A8():
        OP_95(0xFE, -121500, 0, 207400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13A8)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_6_1374 end

    def Function_7_13C9(): pass

    label("Function_7_13C9")


    def lambda_13CE():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13CE)

    def lambda_13E8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13E8)
    WaitChrThread(0xFE, 1)

    def lambda_13FD():
        OP_95(0xFE, -120800, 0, 205400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13FD)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_7_13C9 end

    def Function_8_141E(): pass

    label("Function_8_141E")


    def lambda_1423():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1423)

    def lambda_143D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_143D)
    WaitChrThread(0xFE, 1)

    def lambda_1452():
        OP_95(0xFE, -120800, 0, 206600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1452)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_8_141E end

    def Function_9_1473(): pass

    label("Function_9_1473")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11712.itc", 0x1E)
    LoadChrToIndex("chr/ch00002.itc", 0x1F)
    LoadChrToIndex("chr/ch00102.itc", 0x20)
    LoadChrToIndex("chr/ch00202.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch02902.itc", 0x23)
    LoadChrToIndex("chr/ch03002.itc", 0x24)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07500.itp")
    SetChrPos(0x101, -117500, 0, 206000, 270)
    SetChrPos(0x102, -117500, 0, 206000, 270)
    SetChrPos(0x103, -117500, 0, 206000, 270)
    SetChrPos(0x104, -117500, 0, 206000, 270)
    SetChrPos(0x109, -117500, 0, 206000, 270)
    SetChrPos(0x105, -117500, 0, 206000, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -130000, 50, 206000, 90)
    OP_68(-120300, 1100, 206000, 0)
    MoveCamera(55, 13, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    FadeToBright(1000, 0)
    StopBGM(0x1388)
    ClearMapObjFlags(0x7, 0x10)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x7)
    OP_68(-126300, 1100, 206000, 5000)
    SetCameraDistance(18500, 5000)
    BeginChrThread(0x101, 3, 0, 3)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 4)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 5)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 6)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 7)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 8)
    Sleep(1700)
    Sound(104, 0, 100, 0)
    OP_71(0x7, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x7)
    WaitChrThread(0x105, 3)

    #C0038
    ChrTalk(
        0x101,
        (
            "#00003F#11P打扰了，阁下。\x02\x03",

            "#00001F克洛斯贝尔警察局·特别任务支援科，\x01",
            "应邀前来拜访。\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7583", 0)

    #C0039
    ChrTalk(
        0xA,
        (
            "#6P#07509F哦，你们来了啊。\x02\x03",

            "#07500F不用拘束，\x01",
            "来，都坐下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#00000F#11P好、好的。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        "#00104F#11P那就恭敬不如从命了……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-128500, 2700, 105900, 0)
    MoveCamera(303, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_68(-128500, 900, 105900, 3000)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x109, 0x23)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x24)
    SetChrSubChip(0x105, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, -128400, 50, 103900, 0)
    SetChrPos(0x102, -128199, 50, 107200, 200)
    SetChrPos(0x103, -127500, 50, 103900, 0)
    SetChrPos(0x104, -126700, 50, 107200, 200)
    SetChrPos(0x109, -126600, 50, 103900, 0)
    SetChrPos(0x105, -125700, 50, 103900, 0)
    SetChrPos(0xA, -130000, 50, 105900, 90)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xD, 0x80)
    OP_78(0xA, 0xD)
    ClearChrFlags(0xE, 0x80)
    OP_78(0xB, 0xE)
    OP_49()
    SetChrPos(0xD, -128100, 0, 107500, 20)
    OP_D5(0xD, 0x0, 0x4E20, 0x0, 0x0)
    SetChrPos(0xE, -126600, 0, 107500, 20)
    OP_D5(0xE, 0x0, 0x4E20, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    SetCameraDistance(15500, 80000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0042
    AnonymousTalk(
        0xA,
        (
            "哈哈哈，突然叫你们过来，\x01",
            "是不是吓到了？\x02\x03",

            "哎呀～因为除了这种时候，\x01",
            "我也挤不出其它时间了。\x02\x03",

            "你们应该正忙着吧？真是抱歉啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0043
    ChrTalk(
        0x101,
        "#6P#00011F哪、哪里的话。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        "#00102F您的关心令我们不胜惶恐。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    #C0045
    ChrTalk(
        0xA,
        (
            "#07505F#5P哦，你是麦克道尔阁下的\x01",
            "孙女吧？\x02\x03",

            "我以前好像在庆祝会之类的\x01",
            "活动中见过你。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        (
            "#00104F是的，我随外公一同前往共和国\x01",
            "访问时，有幸与您见了一面。\x02\x03",

            "#00100F那是前年的事情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xA,
        (
            "#07509F#5P哦，听你一说，我也想起来了。\x02\x03",

            "#07500F说起来，麦克道尔阁下竟然卸去\x01",
            "市长一职，就任为自治州议长……\x02\x03",

            "#07504F都已经那么大年纪了，还能保有如此热情，\x01",
            "实在是政治家的楷模啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x102,
        (
            "#00109F呵呵，外公若能听到您这番\x01",
            "赞美，一定会很高兴的。\x02\x03",

            "#00108F对了，阁下，您今天召见我们，\x01",
            "究竟有何要事呢？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(300)

    #C0049
    ChrTalk(
        0xA,
        (
            "#07509F#5P哈哈哈，没什么，\x01",
            "只是我听雾香说起过你们。\x02\x03",

            "#07500F那场『黑之竞拍会』的经过，\x01",
            "听起来真是让人痛快淋漓啊。\x02\x03",

            "#07503F也许我不该说出这样的话，\x01",
            "但之前那个名叫哈尔特曼的议长……\x01",
            "实在是个令人厌恶的家伙。\x02\x03",

            "#07500F你们是直接致使他\x01",
            "下台的大功臣，\x01",
            "所以我想和各位见上一面。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#6P#00002F不、不胜荣幸。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        (
            "#12P#00306F其实那家伙只是\x01",
            "自取灭亡而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        (
            "#6P#00208F……是啊。\x01",
            "从他与那种教团相互勾结的一刻开始，\x01",
            "就已经注定要出局了……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xA,
        (
            "#07505F#5P啊，对了，说起那个教团……\x02\x03",

            "#07503F『Ｄ∴Ｇ教团』──\x01",
            "他们在大陆各地都犯下过无数恶行，\x01",
            "但最大的受害者还要属我国。\x02\x03",

            "#07501F全靠各位，才将那个教团彻底消灭，\x01",
            "我必须要正式表达谢意啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#6P#00011F哪、哪里的话……\x01",
            "我们只是完成了自己的本职工作而已。\x02\x03",

            "#00004F而且，我们的贡献\x01",
            "实在是微不足道……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xA,
        (
            "#07509F#5P哈哈哈，不必谦虚了。\x02\x03",

            "听说当时的状况十分危急，\x01",
            "连警备队都被操纵了。\x02\x03",

            "#07502F在那种情况下，你们为了保护\x01",
            "一名少女，毅然向邪恶的教团发起抗争……\x02\x03",

            "哎呀呀，这般壮举，普通人可做不来！\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#6P#00012F这……您真是过誉了。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        "#00103F您太过奖了，实在愧不敢当。\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xA,
        (
            "#07506F#5P老实说，如果当时没有妥善解决，\x01",
            "那起事件必定会演变为相当严重的问题。\x02\x03",

            "ＩＢＣ会被邪恶的教团占领，\x01",
            "国际贸易与金融业务都将被迫中止……\x02\x03",

            "#07501F一旦陷入那种局面，连共和国的经济\x01",
            "都将遭受相当巨大的损害。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        "#6P#00001F……！\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        "#00108F……这……\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xA,
        (
            "#07505F#5P唔……如此说来，\x01",
            "如果不给你们颁发荣誉勋章，\x01",
            "实在是说不过去呢。\x02\x03",

            "#07509F好，等我回国之后，\x01",
            "立刻就为你们筹办豪华的授勋仪式！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#6P#00011F这、这……！\x01",
            "请您等一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x103,
        (
            "#6P#00211F那只是自治州内的问题而已，\x01",
            "如果接受共和国政府颁发的勋章，\x01",
            "似乎有些奇怪呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        (
            "#12P#00306F而且我们已经从麦克道尔\x01",
            "老爷子那里拿到表彰奖状了。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xA,
        (
            "#07504F#5P不，这没什么好奇怪的。\x02\x03",

            "#07502F克洛斯贝尔的问题也就是\x01",
            "我们宗主国的问题啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0066
    ChrTalk(
        0x101,
        "#6P#00013F……唔。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x102,
        "#00108F……阁下…………\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xA,
        (
            "#07509F#5P哈哈哈，\x01",
            "不要摆出那种表情嘛。\x02\x03",

            "#07502F『铁血宰相』好像\x01",
            "也要召见你们吧？\x02\x03",

            "本想和各位多聊聊，\x01",
            "不过，你们差不多也该过去了。\x02\x03",

            "#07504F哦，对了，我一定会给各位\x01",
            "准备勋章的，你们就好好期待吧。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x23, 1)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_9_1473 end

    def Function_10_24AC(): pass

    label("Function_10_24AC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11600.itc", 0x1E)
    LoadChrToIndex("chr/ch05410.itc", 0x1F)
    LoadChrToIndex("apl/ch51603.itc", 0x20)
    LoadChrToIndex("apl/ch51604.itc", 0x21)
    LoadEffect(0x0, "event\\ev500_00.eff")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis412.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12300.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11202.itp")
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 26500, 0, 26800, 0)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 26500, 0, 19000, 0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x0, 31000, 0, 23000, 0)
    PlayEffect(0x0, 0xFF, 0xB, 0x1, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetMapObjFrame(0xFF, "wlight_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "toreru", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back_pano", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ent01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ent02", 0x0, 0x1)
    OP_68(26500, 1000, 26800, 0)
    MoveCamera(41, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16340, 0)
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    SetCameraDistance(15340, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_64(0xB)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0069
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#40W…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #N0070
    NpcTalk(
        0xC,
        "少女的声音",
        "琪雅……\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xB, 0xB4, 0x1F4)
    Fade(500)
    OP_68(26500, 1000, 24400, 0)
    MoveCamera(137, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "toreru", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back_pano", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ent01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ent02", 0x1, 0x1)
    OP_68(26500, 1000, 23450, 1500)
    OP_0D()
    OP_6F(0x79)

    #C0071
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12302F#5P啊，滴……\x02\x03",

            "你的眼睛已经没问题了吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_68(26500, 1000, 25480, 3000)
    SetCameraDistance(14500, 3000)

    def lambda_2867():
        OP_95(0xFE, 26500, 0, 24900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2867)
    WaitChrThread(0xC, 1)
    OP_6F(0x79)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0072
    AnonymousTalk(
        0xC,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#30W嗯……已经不会头晕目眩了，\x01",
            "连色彩都能清晰分辨……\x02\x03",

            "这一切……\x01",
            "都多亏了琪雅呢。\x02\x03",

            "……真是太感谢你了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    #C0073
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#5P#12309F嘿嘿……太好了。\x02\x03",

            "#12302F不过，这也是因为滴和医院的\x01",
            "各位一直都非常努力哦。\x02\x03",

            "琪雅只是在\x01",
            "最后推了一把而已。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xC,
        "#11P#11226F是吗……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#5P#12304F而且，总算拥有了这种『力量』，\x01",
            "如果不有效利用，未免也太可惜了。\x02\x03",

            "#12314F嘿嘿，能把滴的眼睛治好，\x01",
            "我变成这样也算值得——\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(14000, 500)
    Fade(250)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x20)
    OP_0D()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0076
    ChrTalk(
        0xC,
        "#11P#11232F#4S……不！\x02",
    )

    CloseMessageWindow()

    def lambda_2AE0():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2AE0)
    WaitChrThread(0xC, 2)
    Sleep(300)

    #C0077
    ChrTalk(
        0xC,
        (
            "#11P#11226F#30W……我、我现在确实很高兴……\x02\x03",

            "我一直都为眼睛看不到而感到不安……\x01",
            "……总觉得自己是爸爸的累赘……\x02\x03",

            "#11228F明明和你成为了好朋友，\x01",
            "却连你长什么样子都不知道……！\x02\x03",

            "#11227F现在终于能看到你的样子，\x01",
            "我高兴得连眼泪都流出来了……！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(26500, 1000, 25870, 600)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xC, 0x2)
    ClearChrFlags(0xC, 0x20)

    def lambda_2C1A():
        OP_95(0xFE, 26500, 0, 25400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2C1A)
    WaitChrThread(0xC, 1)
    Sound(812, 0, 100, 0)
    OP_6F(0x79)
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0078
    ChrTalk(
        0xC,
        (
            "#11P#11232F#4S可是……琪雅，\x01",
            "你这样下去真的好吗！？\x02\x03",

            "#3S和罗伊德警官他们分开，\x01",
            "还被迫去做那种事……！\x02\x03",

            "#11227F我觉得……这样\x01",
            "绝对是错的！\x02\x03",

            "玛丽亚贝尔小姐，还有迪塔先生都错了！\x02\x03",

            "#11232F#40W……就连……#500W……#40W爸爸也……！\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#5P#12312F#30W滴……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_68(26500, 1000, 25400, 1000)

    def lambda_2D6D():
        OP_95(0xFE, 26500, 0, 26000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2D6D)
    WaitChrThread(0xB, 1)
    Sleep(300)
    Fade(500)
    OP_68(26500, 1000, 25800, 0)
    MoveCamera(41, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    SetMapObjFrame(0xFF, "wlight_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "toreru", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back_pano", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ent01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ent02", 0x0, 0x1)
    SetCameraDistance(13000, 13000)
    Sleep(300)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xB, 0x20)
    SetChrChipByIndex(0xC, 0x21)
    SetChrSubChip(0xC, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x20)
    OP_0D()
    Sound(898, 0, 100, 0)
    Sleep(100)
    SetChrSubChip(0xB, 0x1)
    SetChrSubChip(0xC, 0x11)
    Sleep(100)
    SetChrSubChip(0xB, 0x2)
    SetChrSubChip(0xC, 0x12)
    Sleep(100)
    SetChrSubChip(0xB, 0x3)
    SetChrSubChip(0xC, 0x13)
    Sleep(100)
    SetChrSubChip(0xB, 0x4)
    SetChrSubChip(0xC, 0x14)
    Sleep(100)
    SetChrSubChip(0xB, 0x5)
    SetChrSubChip(0xC, 0x15)
    Sleep(100)
    SetChrSubChip(0xB, 0x6)
    SetChrSubChip(0xC, 0x16)
    Sleep(500)

    #C0080
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#5P#12304F#40W谢谢你……\x01",
            "我最喜欢你了，滴。\x02\x03",

            "#12302F不过……我没事的。\x02\x03",

            "因为这是在知晓一切的情况下，\x01",
            "我自己做出的决定……\x02\x03",

            "#12309F所以呢……\x01",
            "你不必那么担心哦。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(13500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xA)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_E5(0xB)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("t6050", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_24AC end

    SaveToFile()

Try(main)
