from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m9013.bin",                # FileName
        "m9013",                    # MapName
        "m9013",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 100000, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "m9013",                  # 0
        "盖伊",                   # 1
        "SE制御",                 # 2
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(276, 0)                                        # 0

    ScpFunction((
        "Function_0_114",          # 00, 0
        "Function_1_124",          # 01, 1
        "Function_2_129",          # 02, 2
        "Function_3_26F7",         # 03, 3
        "Function_4_270A",         # 04, 4
        "Function_5_2751",         # 05, 5
        "Function_6_2775",         # 06, 6
        "Function_7_2799",         # 07, 7
        "Function_8_2832",         # 08, 8
        "Function_9_2853",         # 09, 9
        "Function_10_287E",        # 0A, 10
        "Function_11_28E5",        # 0B, 11
        "Function_12_2916",        # 0C, 12
        "Function_13_2941",        # 0D, 13
        "Function_14_2962",        # 0E, 14
        "Function_15_298D",        # 0F, 15
        "Function_16_29B1",        # 10, 16
        "Function_17_29ED",        # 11, 17
    ))


    def Function_0_114(): pass

    label("Function_0_114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_123")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_123")

    Return()

    # Function_0_114 end

    def Function_1_124(): pass

    label("Function_1_124")

    OP_F0(0x1, 0x320)
    Return()

    # Function_1_124 end

    def Function_2_129(): pass

    label("Function_2_129")

    EventBegin(0x0)
    FadeToDark(0, 16777215, -1)
    Call(0, 17)
    LoadChrToIndex("chr/ch12100.itc", 0x1E)
    LoadChrToIndex("apl/ch51751.itc", 0x1F)
    SoundLoad(111)
    SoundLoad(125)
    SoundLoad(109)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07801.itp")
    OP_68(0, 2500, 0, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(27000, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    SetChrPos(0x101, 0, -750, 750, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, -750, -2750, 0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(111, 2, 80, 0)
    Sound(125, 2, 40, 0)
    Sound(109, 2, 30, 0)
    OP_68(40000, 150, -50000, 0)
    MoveCamera(306, 14, 8, 0)
    OP_6E(700, 0)
    SetCameraDistance(35000, 0)
    OP_68(-20000, 150, 25000, 16000)
    MoveCamera(306, 14, 6, 16000)
    OP_6E(700, 16000)
    SetCameraDistance(35000, 16000)
    PlaceName2(340, 200, "c_plac63", 0x0, 6000)
    FadeToBright(3000, 16777215)
    Sleep(15600)
    Fade(500)
    OP_68(0, 750, 250, 0)
    MoveCamera(210, 8, -5, 0)
    OP_6E(700, 0)
    SetCameraDistance(34500, 0)
    OP_68(0, 750, 750, 7500)
    MoveCamera(135, 14, 5, 7500)
    OP_6E(700, 7500)
    SetCameraDistance(18500, 7500)
    OP_6F(0x79)
    SetCameraDistance(13600, 100000)
    Sleep(500)

    #C0001
    ChrTalk(
        0x101,
        (
            "#00005F#11P#30W这里是……\x02\x03",

            "#00008F……大家……\x01",
            "还有琪雅……都去哪里了？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_93(0x101, 0x59, 0x190)
    Sleep(800)
    OP_93(0x101, 0x10F, 0x190)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)

    #C0002
    ChrTalk(
        0x101,
        (
            "#00006F#5P#30W……不管怎么想，\x01",
            "这里都不像是普通的地方。\x02\x03",

            "#00008F看来还是不要\x01",
            "漫无目的地四处乱走为好……\x02\x03",

            "#00003F……………………………………\x02",
        )
    )

    CloseMessageWindow()
    MoveCamera(135, 14, 4, 2000)
    SetCameraDistance(13600, 10000)
    Sleep(200)
    OP_93(0x101, 0x0, 0x190)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(500)

    #C0003
    ChrTalk(
        0x101,
        (
            "#00003F#11P#30W……话说回来，这到底是怎么回事呢？\x01",
            "明明处在这种空无一物的奇异场所……\x02\x03",

            "#00000F但不知为何……我却丝毫没有\x01",
            "不安和恐惧的感觉。\x02\x03",

            "#00008F……这个地方究竟是……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(250, 10, -1, -1)
    SetChrName("男人的声音")

    #A0004
    AnonymousTalk(
        0xFF,
        (
            "#3C无论遇到什么情况，\x01",
            "都能够保持冷静，毫不慌张，\x01",
            "努力把握现场的状况……\x02\x03",

            "看来你已经很有\x01",
            "搜查官的风范了啊。\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(223, 0, 50, 0)
    Sound(920, 0, 50, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, 750, 0, 1500)
    MoveCamera(135, 14, 0, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(13600, 1500)

    def lambda_609():
        OP_95(0xFE, 0, -750, -1400, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_609)

    def lambda_623():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x4B0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_623)

    def lambda_634():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_634)
    OP_6F(0x79)
    CancelBlur(0)
    SetCameraDistance(13000, 3000)
    Sleep(500)

    #C0005
    ChrTalk(
        0x101,
        "#00005F#6P#30W…………………………\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x1000)

    #N0006
    NpcTalk(
        0x8,
        "？？？",
        "#11P#30W怎么了？罗伊德。\x02",
    )

    CloseMessageWindow()

    #N0007
    NpcTalk(
        0x8,
        "？？？",
        (
            "#11P#30W久别重逢，\x01",
            "让你惊讶得连话都说不出了吗？\x02",
        )
    )

    CloseMessageWindow()
    PlayBGM("ed7534", 0)
    SetCameraDistance(11000, 100000)
    Sleep(500)
    BeginChrThread(0x9, 1, 0, 16)

    #C0008
    ChrTalk(
        0x101,
        (
            "#00011F#6P#40W哥、哥哥……\x02\x03",

            "#00002F是……是哥哥吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0009
    AnonymousTalk(
        0x8,
        (
            "#30W#0C哈哈，为何一本正经地\x01",
            "叫什么『哥哥』？\x02\x03",

            "就像以前那样，\x01",
            "直接喊『大哥』不好吗？\x02\x03",

            "这里只有我们两人，\x01",
            "你不必拘谨，可以尽情撒撒娇哦。\x02",
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

    #C0010
    ChrTalk(
        0x101,
        (
            "#00006F#6P#30W……这～\x01",
            "不用你多事啦！\x02\x03",

            "#00002F话说回来，这种轻佻的口气……\x01",
            "正是大哥的特点呢……\x02\x03",

            "但也不像在做梦……\x01",
            "这到底是怎么回事……？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W哦，这个地方似乎是\x01",
            "那孩子内心的一部分。\x02\x03",

            "#07808F包含了一切可能性，\x01",
            "能够重新建构世界的『零』之世界……\x02\x03",

            "#07800F大致就是这么一个地方吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#00005F#6P#30W『零』之世界……\x02\x03",

            "#00013F大哥……\x01",
            "……哥哥你会出现在此，\x01",
            "也是由于这个缘故吗？\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 5)
    WaitChrThread(0x8, 1)

    #C0013
    ChrTalk(
        0x8,
        (
            "#07803F#11P#30W嗯，那孩子恐怕是\x01",
            "通过干涉过去的时间与空间，\x01",
            "从而了解到了我的存在。\x02\x03",

            "#07808F而且，她为了你和塞茜尔……\x01",
            "还有亚里欧斯和缇欧他们，\x01",
            "说不定会让我复活。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0014
    ChrTalk(
        0x101,
        "#00011F#6P#30W让大哥……复活！？\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 6)
    WaitChrThread(0x8, 1)

    #C0015
    ChrTalk(
        0x8,
        (
            "#07800F#11P#30W嗯，准确来说，\x01",
            "其实是将现在的世界重新改写为\x01",
            "『我没有死的世界』。\x02\x03",

            "#07802F怎么样？罗伊德。\x02\x03",

            "#07809F如果哥哥能回来，你会高兴吗？\x01",
            "还是觉得很烦啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#00002F#6P#40W…………哈哈……………\x02\x03",

            "#00004F那还用说……当然是……\x01",
            "很高兴啊……\x02\x03",

            "#00008F………可是……那样就…………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #C0017
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W……那样就否定了\x01",
            "在我死去之后，一直都在拼命\x01",
            "奋斗的人们所付出的努力……\x02\x03",

            "#07810F呼，这自然是难免的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#00008F#6P#40W………………………………………\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "#07803F#11P#30W是叫『特别任务支援科』吧？\x02\x03",

            "#07802F我也加入这个部门，\x01",
            "与你们一起解决各种各样的事件……\x01",
            "那样的世界或许也是可以创造出来的……\x02\x03",

            "#07804F但那并不是你们现在的世界。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00002F#6P#40W…………嗯………………\x02\x03",

            "#00006F如果真的存在那样的世界，\x01",
            "那该有多么快乐，多么开心……\x01",
            "……肯定会是个无比幸福的世界……\x02\x03",

            "#00008F#50W……但即使如此……我也………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)

    def lambda_E09():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E09)
    WaitChrThread(0x101, 2)
    Sleep(750)

    #C0021
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W好，可以了。\x02\x03",

            "#07800F能听到你这么说，\x01",
            "我感到很骄傲。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 750, 500, 1500)
    MoveCamera(135, 14, 3, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(11000, 1500)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x1000)
    OP_9B(0x1, 0x8, 0x0, 0x60E, 0x3E8, 0x0)
    OP_6F(0x79)
    BeginChrThread(0x8, 1, 0, 7)
    WaitChrThread(0x8, 1)
    Sleep(500)
    BeginChrThread(0x8, 1, 0, 8)
    WaitChrThread(0x8, 1)
    Sleep(300)

    #C0022
    ChrTalk(
        0x8,
        (
            "#07809F#11P#40W……当年那个爱撒娇的孩子，\x01",
            "如今已经长这么大了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#00015F#6P#50W我、我才没有\x01",
            "向大哥撒过娇呢……\x02\x03",

            "#00008F……如果是和塞茜尔姐姐，倒还有过几次……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        "#07804F#11P#40W哈哈……好像是呢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)
    Sleep(500)

    #C0025
    ChrTalk(
        0x8,
        (
            "#07803F#11P#30W……塞茜尔也该为自己\x01",
            "踏出新的一步了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(120)
    SetChrSubChip(0x8, 0x10)
    Sleep(120)
    SetChrSubChip(0x8, 0x9)
    Sleep(300)

    #C0026
    ChrTalk(
        0x8,
        (
            "#07802F#11P#30W要不然，你就鼓起勇气，\x01",
            "向她发起进攻如何？\x02\x03",

            "#07809F不过她天生就有些迟钝，\x01",
            "未必能察觉到你的心意呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        (
            "#00006F#6P#30W胡说八道……\x01",
            "不要小看塞茜尔姐姐。\x02\x03",

            "#00013F她可是很优秀的女性，\x01",
            "配大哥你简直是浪费呢……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1323")

    #C0028
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W哈哈，说的没错。\x02\x03",

            "#07800F话说回来，你好像已经\x01",
            "找到意中人了呢，\x01",
            "看来是我多管闲事了。\x02\x03",

            "#07809F是叫艾莉吧？\x01",
            "虽然是位大小姐，但是意志坚强，\x01",
            "而且有很强的行动力和包容力。\x02\x03",

            "#07802F真是个才貌双全的好女孩，\x01",
            "配你好像有点可惜呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#00002F#6P#30W哈哈……我也这么觉得。\x02\x03",

            "#00006F如果可以……\x01",
            "真希望让大哥也见见艾莉。\x02\x03",

            "#00008F还有缇欧和兰迪……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W缇欧啊……虽然经历过很多事情，\x01",
            "但还是长成了一个好孩子，这就再好不过了。\x02\x03",

            "#07800F兰迪好像有点傻气，不过，\x01",
            "看起来也是个挺有意思的家伙。\x02\x03",

            "#07809F看来你遇上了很好的同伴呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21DF")

    label("loc_1323")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D2")

    #C0031
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W哈哈，没错。\x02\x03",

            "#07800F话说回来，你好像已经\x01",
            "找到意中人了呢，\x01",
            "看来是我多管闲事了。\x02\x03",

            "#07809F真没想到你会和\x01",
            "缇欧走到一起啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#00011F#6P#30W我、我们并不是\x01",
            "那种关系啦……\x02\x03",

            "#00004F不过，我想守护她，她在我心中\x01",
            "非常重要，这一点倒是可以肯定的。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W是吗……她好像已经\x01",
            "可以露出灿烂的笑容了。\x02\x03",

            "#07802F总之，将来肯定是很有希望的，\x01",
            "你可要好好把握住她哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        (
            "#00002F#6P#30W哈哈……现在说这些还太早啦。\x02\x03",

            "#00006F……如果可以，\x01",
            "真希望让大哥也见见缇欧。\x02\x03",

            "#00008F还有艾莉和兰迪……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W艾莉就是那位才貌双全，\x01",
            "行动力很强的大小姐吧？\x02\x03",

            "#07800F兰迪好像有点傻气，不过，\x01",
            "看起来也是个挺有意思的家伙。\x02\x03",

            "#07809F看来你遇上了很好的同伴呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21DF")

    label("loc_15D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1833")

    #C0036
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W哈哈，没错。\x02\x03",

            "#07800F话说回来，你好像已经\x01",
            "找到意中人了呢，\x01",
            "看来是我多管闲事了。\x02\x03",

            "#07809F是叫诺艾尔吧？\x01",
            "确实是个坦率的好女孩，\x01",
            "配你好像有点浪费呢。\x02\x03",

            "#07802F不过，那种直来直去的\x01",
            "单纯性格倒是和你很合拍。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x101,
        (
            "#00002F#6P#30W哈哈……我也这么觉得。\x02\x03",

            "#00006F如果可以……\x01",
            "真希望让大哥也见见诺艾尔。\x02\x03",

            "#00008F还有艾莉和兰迪，\x01",
            "当然还有缇欧……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W缇欧啊……虽然经历过很多事情，\x01",
            "但还是长成了一个好孩子，这就再好不过了。\x02\x03",

            "#07800F艾莉就是那位才貌双全，\x01",
            "行动力很强的大小姐吧？\x02\x03",

            "兰迪好像有点傻气，不过，\x01",
            "看起来也是个挺有意思的家伙。\x02\x03",

            "#07809F看来你遇上了很好的同伴呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21DF")

    label("loc_1833")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AB3")

    #C0039
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W哈哈，没错。\x02\x03",

            "#07800F话说回来，你好像已经\x01",
            "找到意中人了呢，\x01",
            "看来是我多管闲事了。\x02\x03",

            "#07809F是叫莉夏吧？\x02\x03",

            "#07802F她似乎背负着很多沉重的经历，\x01",
            "但确实是个开朗的好女孩，\x01",
            "配你好像有点浪费呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#00011F#6P#30W我、我们并不是\x01",
            "那种关系啦……\x02\x03",

            "#00004F不过，我想守护她，\x01",
            "这一点倒是可以肯定的。\x02\x03",

            "#00008F如果可以……\x01",
            "真希望让大哥也见见莉夏。\x02\x03",

            "还有艾莉和兰迪，\x01",
            "当然还有缇欧……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W缇欧啊……虽然经历过很多事情，\x01",
            "但还是长成了一个好孩子，这就再好不过了。\x02\x03",

            "#07800F艾莉就是那位才貌双全，\x01",
            "行动力很强的大小姐吧？\x02\x03",

            "兰迪好像有点傻气，不过，\x01",
            "看起来也是个挺有意思的家伙。\x02\x03",

            "#07809F看来你遇上了很好的同伴呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21DF")

    label("loc_1AB3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D23")

    #C0042
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W哈哈，说的没错。\x02\x03",

            "#07802F话说回来，你可要\x01",
            "用心寻找自己的意中人哦。\x02\x03",

            "虽然我也明白，与搭档\x01",
            "共同进退也是一件开心的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        "#00005F#6P#30W啊，是指兰迪吗？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W他似乎是个有点傻气，\x01",
            "但内心很坚强的家伙。\x02\x03",

            "#07800F和你这种严肃认真的人\x01",
            "好像也很合得来……\x02\x03",

            "#07809F看来是个很好的搭档呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W是啊……我也这么觉得。\x02\x03",

            "#00008F如果可以……\x01",
            "真希望让大哥也见见兰迪。\x02\x03",

            "还有缇欧和艾莉……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W缇欧啊……虽然经历过很多事情，\x01",
            "但还是长成了一个好孩子，这就再好不过了。\x02\x03",

            "#07800F艾莉就是那位才貌双全，\x01",
            "行动力很强的大小姐吧？\x02\x03",

            "#07809F看来你遇上了很好的同伴呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21DF")

    label("loc_1D23")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FE1")

    #C0047
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W哈哈，说的没错。\x02\x03",

            "#07802F话说回来，你可要\x01",
            "用心寻找自己的意中人哦。\x02\x03",

            "虽然我也明白，与同性伙伴\x01",
            "共同进退也是一件开心的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        "#00005F#6P#30W啊，是指瓦吉吗？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W虽然是个神秘兮兮的家伙，\x01",
            "但好像值得信赖。\x02\x03",

            "#07800F和你这种严肃认真的性格\x01",
            "也能形成很好的互补……\x02\x03",

            "#07809F这也算是一种缘分吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W是啊……我也这么觉得。\x02\x03",

            "#00008F如果可以……\x01",
            "真希望让大哥也见见瓦吉。\x02\x03",

            "还有艾莉和兰迪，\x01",
            "当然还有缇欧……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W缇欧啊……虽然经历过很多事情，\x01",
            "但还是长成了一个好孩子，这就再好不过了。\x02\x03",

            "#07800F艾莉就是那位才貌双全，\x01",
            "行动力很强的大小姐吧？\x02\x03",

            "兰迪好像有点傻气，不过，\x01",
            "看起来也是个挺有意思的家伙。\x02\x03",

            "#07809F看来你遇上了很好的同伴呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21DF")

    label("loc_1FE1")


    #C0052
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W哈哈，说的没错。\x02\x03",

            "#07803F话说回来，你可要\x01",
            "用心寻找自己的意中人哦。\x02\x03",

            "#07802F虽然我也明白，与同伴们\x01",
            "共同进退也是一件开心的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#00012F#6P#30W哈哈……实在是无法反驳呢。\x02\x03",

            "#00008F如果可以……\x01",
            "真希望让大哥也见见大家。\x02\x03",

            "比如艾莉和兰迪，\x01",
            "当然还有缇欧……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W缇欧啊……虽然经历过很多事情，\x01",
            "但还是长成了一个好孩子，这就再好不过了。\x02\x03",

            "#07800F艾莉就是那位才貌双全，\x01",
            "行动力很强的大小姐吧？\x02\x03",

            "兰迪好像有点傻气，不过，\x01",
            "看起来也是个挺有意思的家伙。\x02\x03",

            "#07809F看来你遇上了很好的同伴呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21DF")


    #C0055
    ChrTalk(
        0x101,
        "#00002F#6P#30W嗯……是最棒的同伴们。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 11)
    BeginChrThread(0x101, 1, 0, 12)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x1000)
    SetChrChipByIndex(0x101, 0xFF)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x1000)
    SetChrSubChip(0x101, 0xE)
    BeginChrThread(0x101, 0, 0, 3)
    OP_68(0, 750, 800, 1500)
    MoveCamera(135, 14, 3, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(12000, 1500)
    WaitChrThread(0x101, 0)
    OP_6F(0x79)

    #C0056
    ChrTalk(
        0x101,
        (
            "#00004F#6P#30W……大哥，我该走了。\x02\x03",

            "为了带着最重要的人，\x01",
            "回到大家的身边。\x02\x03",

            "#00000F今后……还能再次见面吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W嗯，那当然。\x02\x03",

            "#07810F我就在你们身边。\x02\x03",

            "想哭的时候，想撒娇的时候，\x01",
            "随时都可以叫我。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#00012F#6P#30W哈哈……我知道了。\x02\x03",

            "#00002F但是，只要大家一起努力，\x01",
            "共同把握未知的明天……\x02\x03",

            "#00004F今后无论遇到多少困难，\x01",
            "我们也会顺利跨越『壁障』。\x02\x03",

            "#00000F所以……一定没问题的，\x01",
            "你就放心看着吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "#07809F#11P#30W哈哈，口气不小嘛。\x02\x03",

            "#07804F现在的你，一定可以\x01",
            "真正意义上地找到那孩子。\x02\x03",

            "#07800F#30W#11P快把封闭在壳中的公主殿下找到，\x01",
            "然后给她一个紧紧的拥抱吧！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0060
    ChrTalk(
        0x101,
        (
            "#00000F#6P#30W#4S嗯……！\x02\x03",

            "#00014F#3S再见了……大哥！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(480, 350, 5260, 3500)
    MoveCamera(34, 8, 0, 3500)
    OP_6E(700, 3500)
    SetCameraDistance(13230, 3500)
    BeginChrThread(0x101, 0, 0, 4)
    OP_6F(0x79)
    WaitChrThread(0x101, 0)
    Sleep(1000)
    Fade(500)
    OP_68(0, 350, 400, 0)
    MoveCamera(135, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12000, 0)
    SetCameraDistance(10500, 3000)
    Sleep(1500)
    BeginChrThread(0x8, 1, 0, 13)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)
    SetCameraDistance(10000, 15000)

    #C0061
    ChrTalk(
        0x8,
        (
            "#07804F#11P#30W……这才对。只要还活着，\x01",
            "就总要面对随时都有可能出现的『壁障』。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    BeginChrThread(0x8, 1, 0, 14)
    WaitChrThread(0x8, 1)
    Sleep(200)

    #C0062
    ChrTalk(
        0x8,
        (
            "#07810F#11P#30W最重要的是，要有勇于跨越壁障的意志，\x01",
            "并努力寻找隐藏在前方的光明……\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 15)
    WaitChrThread(0x8, 1)

    #C0063
    ChrTalk(
        0x8,
        "#07804F#11P#30W加油吧……罗伊德·班宁斯。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(12000, 3000)
    FadeToDark(2000, 0, -1)
    Sleep(300)
    SetChrSubChip(0x8, 0x16)
    Sleep(143)
    SetChrSubChip(0x8, 0x15)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    StopSound(111, 2000, 30)
    StopSound(125, 2000, 20)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("m9014", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_129 end

    def Function_3_26F7(): pass

    label("Function_3_26F7")

    OP_9B(0x1, 0x101, 0x0, 0xFFFFFD12, 0x320, 0x0)
    Sleep(400)
    Return()

    # Function_3_26F7 end

    def Function_4_270A(): pass

    label("Function_4_270A")

    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0xFA0, 0x1)

    def lambda_2725():
        OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2725)
    Sleep(3000)

    def lambda_273D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_273D)
    Sleep(1500)
    EndChrThread(0xFE, 0x1)
    Return()

    # Function_4_270A end

    def Function_5_2751(): pass

    label("Function_5_2751")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(167)
    SetChrSubChip(0xFE, 0xD)
    Sleep(167)
    SetChrSubChip(0xFE, 0xE)
    Sleep(500)
    Return()

    # Function_5_2751 end

    def Function_6_2775(): pass

    label("Function_6_2775")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xE)
    Sleep(150)
    SetChrSubChip(0xFE, 0xD)
    Sleep(150)
    SetChrSubChip(0xFE, 0x0)
    Sleep(500)
    Return()

    # Function_6_2775 end

    def Function_7_2799(): pass

    label("Function_7_2799")

    Sound(812, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(125)
    SetChrSubChip(0xFE, 0x1)
    Sleep(125)
    SetChrSubChip(0xFE, 0x2)
    Sleep(125)
    SetChrSubChip(0xFE, 0x3)
    Sleep(125)
    BeginChrThread(0x101, 1, 0, 10)
    Sound(898, 0, 50, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(143)
    SetChrSubChip(0xFE, 0x6)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x3)
    Sleep(143)
    SetChrSubChip(0xFE, 0x4)
    Sleep(143)
    SetChrSubChip(0xFE, 0x5)
    Sleep(143)
    SetChrSubChip(0xFE, 0x6)
    Sleep(143)
    SetChrSubChip(0xFE, 0x7)
    Sleep(143)
    SetChrSubChip(0xFE, 0x8)
    Sleep(143)
    SetChrSubChip(0xFE, 0x9)
    WaitChrThread(0x101, 1)
    Return()

    # Function_7_2799 end

    def Function_8_2832(): pass

    label("Function_8_2832")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x9)
    Sleep(120)
    SetChrSubChip(0xFE, 0x10)
    Sleep(120)
    SetChrSubChip(0xFE, 0x11)
    Return()

    # Function_8_2832 end

    def Function_9_2853(): pass

    label("Function_9_2853")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x18)
    Sleep(120)
    SetChrSubChip(0xFE, 0x19)
    Sleep(120)
    SetChrSubChip(0xFE, 0x1A)
    Sleep(120)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(120)
    Return()

    # Function_9_2853 end

    def Function_10_287E(): pass

    label("Function_10_287E")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1A)
    Sleep(143)
    SetChrSubChip(0xFE, 0x19)
    Sleep(143)
    SetChrSubChip(0xFE, 0x18)
    Sleep(143)
    SetChrSubChip(0xFE, 0x19)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1A)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1B)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1A)
    Sleep(143)
    SetChrSubChip(0xFE, 0x19)
    Sleep(143)
    SetChrSubChip(0xFE, 0x18)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1D)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1E)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1F)
    Return()

    # Function_10_287E end

    def Function_11_28E5(): pass

    label("Function_11_28E5")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Sound(898, 0, 30, 0)
    SetChrSubChip(0xFE, 0x9)
    Sleep(143)
    SetChrSubChip(0xFE, 0xA)
    Sleep(143)
    SetChrSubChip(0xFE, 0xB)
    Sleep(143)
    SetChrSubChip(0xFE, 0x0)
    Sleep(429)
    Return()

    # Function_11_28E5 end

    def Function_12_2916(): pass

    label("Function_12_2916")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x1F)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1E)
    Sleep(143)
    SetChrSubChip(0xFE, 0x1D)
    Sleep(143)
    SetChrSubChip(0xFE, 0x18)
    Sleep(429)
    Return()

    # Function_12_2916 end

    def Function_13_2941(): pass

    label("Function_13_2941")

    Fade(250)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    Sound(812, 0, 30, 0)
    SetChrSubChip(0xFE, 0x12)
    Sleep(300)
    Return()

    # Function_13_2941 end

    def Function_14_2962(): pass

    label("Function_14_2962")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x12)
    Sleep(120)
    SetChrSubChip(0xFE, 0x13)
    Sleep(120)
    SetChrSubChip(0xFE, 0x14)
    Sleep(120)
    SetChrSubChip(0xFE, 0x15)
    Sleep(300)
    Return()

    # Function_14_2962 end

    def Function_15_298D(): pass

    label("Function_15_298D")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x15)
    Sleep(150)
    SetChrSubChip(0xFE, 0x16)
    Sleep(150)
    SetChrSubChip(0xFE, 0x17)
    Sleep(500)
    Return()

    # Function_15_298D end

    def Function_16_29B1(): pass

    label("Function_16_29B1")

    StopSound(109, 1000, 20)
    OP_25(0x6F, 0x4B)
    Sleep(100)
    OP_25(0x6F, 0x46)
    Sleep(100)
    OP_25(0x6F, 0x41)
    Sleep(100)
    OP_25(0x6F, 0x3C)
    Sleep(100)
    OP_25(0x6F, 0x37)
    Sleep(100)
    OP_25(0x6F, 0x32)
    Sleep(100)
    OP_25(0x6F, 0x2D)
    Sleep(100)
    OP_25(0x6F, 0x28)
    Return()

    # Function_16_29B1 end

    def Function_17_29ED(): pass

    label("Function_17_29ED")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 1)), scpexpr(EXPR_END)), "loc_2A0F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A91")

    label("loc_2A0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 2)), scpexpr(EXPR_END)), "loc_2A27")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A91")

    label("loc_2A27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 3)), scpexpr(EXPR_END)), "loc_2A3F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A91")

    label("loc_2A3F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 4)), scpexpr(EXPR_END)), "loc_2A57")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A91")

    label("loc_2A57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 5)), scpexpr(EXPR_END)), "loc_2A6F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A91")

    label("loc_2A6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 6)), scpexpr(EXPR_END)), "loc_2A87")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2A91")

    label("loc_2A87")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2A91")

    Return()

    # Function_17_29ED end

    SaveToFile()

Try(main)
