from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t113b.bin",                # FileName
        "t113b",                    # MapName
        "t113b",                    # Location
        0x0049,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 73, 0, 0, 0, 1],
    )

    BuildStringList((
        "t113b",                  # 0
        "琪雅",                   # 1
        "芙兰",                   # 2
        "塞茜尔",                 # 3
        "伊莉娅",                 # 4
        "莉夏",                   # 5
        "修利",                   # 6
        "玛丽亚贝尔",             # 7
        "迪塔市长",               # 8
        "艾莉",                   # 9
        "缇欧",                   # 10
        "兰迪",                   # 11
        "诺艾尔",                 # 12
        "瓦吉",                   # 13
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

    ChipFrameInfo(524, 0)                                        # 0

    ScpFunction((
        "Function_0_20C",          # 00, 0
        "Function_1_21C",          # 01, 1
        "Function_2_21D",          # 02, 2
    ))


    def Function_0_20C(): pass

    label("Function_0_20C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_21B")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_21B")

    Return()

    # Function_0_20C end

    def Function_1_21C(): pass

    label("Function_1_21C")

    Return()

    # Function_1_21C end

    def Function_2_21D(): pass

    label("Function_2_21D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_23A")
    RemoveParty(0x1, 0xFF)
    Jump("loc_279")

    label("loc_23A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_24B")
    RemoveParty(0x2, 0xFF)
    Jump("loc_279")

    label("loc_24B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_25C")
    RemoveParty(0x3, 0xFF)
    Jump("loc_279")

    label("loc_25C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_26D")
    RemoveParty(0x8, 0xFF)
    Jump("loc_279")

    label("loc_26D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_279")
    RemoveParty(0x4, 0xFF)

    label("loc_279")

    LoadChrToIndex("chr/ch08202.itc", 0x1E)
    LoadChrToIndex("chr/ch08502.itc", 0x1F)
    LoadChrToIndex("chr/ch05202.itc", 0x20)
    LoadChrToIndex("chr/ch05102.itc", 0x21)
    LoadChrToIndex("chr/ch07502.itc", 0x22)
    LoadChrToIndex("chr/ch10002.itc", 0x23)
    LoadChrToIndex("chr/ch05502.itc", 0x24)
    LoadChrToIndex("chr/ch05602.itc", 0x25)
    LoadChrToIndex("chr/ch00102.itc", 0x26)
    LoadChrToIndex("chr/ch00202.itc", 0x27)
    LoadChrToIndex("chr/ch00302.itc", 0x28)
    LoadChrToIndex("chr/ch02902.itc", 0x29)
    LoadChrToIndex("chr/ch03002.itc", 0x2A)
    LoadChrToIndex("chr/ch00002.itc", 0x2B)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02800.itp")
    OP_68(2100, 3100, -8280, 0)
    MoveCamera(28, 11, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(26140, 0)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x1)
    SetChrPos(0x101, -2000, 180, -4900, 90)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -2000, 180, -8900, 90)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 2000, 180, -16900, 270)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x2)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 2000, 180, -8900, 270)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 2000, 180, -6900, 270)
    SetChrChipByIndex(0xA, 0x22)
    SetChrSubChip(0xA, 0x2)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 2000, 180, -12900, 270)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x2)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 2000, 180, -10900, 270)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x2)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 2000, 180, -4900, 270)
    SetChrChipByIndex(0xF, 0x25)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 0, 180, -1500, 180)
    SetChrChipByIndex(0x10, 0x26)
    SetChrSubChip(0x10, 0x1)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -2000, 180, -6900, 90)
    SetChrChipByIndex(0x11, 0x27)
    SetChrSubChip(0x11, 0x1)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -2000, 180, -10900, 90)
    SetChrChipByIndex(0x12, 0x28)
    SetChrSubChip(0x12, 0x1)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -2000, 180, -12900, 90)
    SetChrChipByIndex(0x13, 0x29)
    SetChrSubChip(0x13, 0x2)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 2000, 180, -14900, 270)
    SetChrChipByIndex(0x14, 0x2A)
    SetChrSubChip(0x14, 0x1)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -2000, 180, -14900, 90)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "不久后，罗伊德一行人全部聚集到\x01",
            "迎宾馆的宴会大厅……\x02\x03",

            "很快，迪塔市长与其女儿\x01",
            "玛丽亚贝尔也一同到场。\x02\x03",

            "迪塔市长为自己的迟来而道歉，\x01",
            "并与大家一一寒暄……\x02\x03",

            "豪华又愉快的晚餐会\x01",
            "就这样开始了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7162", 0)
    OP_68(2100, 1100, -8280, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    MoveCamera(32, 11, 0, 100000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0002
    AnonymousTalk(
        0xF,
        (
            "哎呀呀，抱歉抱歉，\x01",
            "我来迟了。\x02\x03",

            "身为招待者，本应提前\x01",
            "到场才是，真是不好意思。\x02",
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

    #C0003
    ChrTalk(
        0x101,
        (
            "#00004F#6P哪里的话，我们都知道\x01",
            "您的工作很繁忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x11,
        "#00202F#6P您辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xE,
        (
            "#02904F#11P但爸爸如此繁忙，\x01",
            "也可以说是自作自受呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xF,
        (
            "#02809F#5P哈哈哈，嗯，\x01",
            "确实如你所说啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x10,
        "#00106F#6P贝尔，你可真是的……\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xB,
        (
            "#01703F#11P我整天都在练习和演出，\x01",
            "并不了解详细情况……\x02\x03",

            "#01700F但您好像又做出了\x01",
            "相当大胆的提案啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xF,
        (
            "#02804F#5P哈哈，其实我从刚刚就任开始，\x01",
            "就在考虑这件事情了。\x02\x03",

            "原本并没打算\x01",
            "在那种时候提出……\x01",
            "但当时形势所迫，已经没有退路了。\x02\x03",

            "#02800F所以我就下定决心，\x01",
            "准备豪赌一场。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xB,
        (
            "#01704F#11P呵呵，原来如此。\x02\x03",

            "#01702F既然已经登上舞台，\x01",
            "就必须要坚持到演出结束……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xF,
        (
            "#02803F#5P正是如此。\x02\x03",

            "#02800F我听说彩虹剧团\x01",
            "准备推出新版本的\x01",
            "『金之太阳、银之月』。\x02\x03",

            "在你们首次公演的一周之后，\x01",
            "我准备举办一场居民投票活动，\x01",
            "调查大家对独立问题的看法。\x02\x03",

            "#02804F我觉得这也是一种缘分，\x01",
            "所以此次特意邀请了各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        "#00005F#6P是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xB,
        (
            "#01709F#11P呵呵，拜您所赐，\x01",
            "我们享受到了一次愉快的休假。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xC,
        "#01804F#11P非常感谢。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xD,
        "#04203F#11P……谢啦。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xA,
        (
            "#05902F#11P呵呵，我身为一名局外人，\x01",
            "也跟她们一起前来，真是有些不好意思……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xF,
        (
            "#02805F#5P哪里哪里，没有的事。\x02\x03",

            "#02800F我经常听乌尔斯拉医院的\x01",
            "工作人员们谈起你。\x02\x03",

            "听说你非常认真尽职，\x01",
            "简直就像是圣女乌尔斯拉转世呢。\x02\x03",

            "#02809F能与你见面，我深感荣幸。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xA,
        (
            "#05905F#11P这、这真是\x01",
            "过奖了……\x02\x03",

            "#05904F得到如此赞誉，实在是我的光荣。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xE,
        (
            "#02906F#11P爸爸可真是的，\x01",
            "从刚才开始，就一直只对\x01",
            "妙龄女性们赞不绝口……\x02\x03",

            "#02900F多少也该慰劳一下\x01",
            "罗伊德警官他们吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xF,
        (
            "#02805F#5P哦，真是失礼了。\x02\x03",

            "#02809F哈哈哈，在坐的尽是些美丽小姐，\x01",
            "我虽然已经一把年纪了，却还是兴奋不已呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        "#00012F#6P哈哈……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x12,
        (
            "#00309F#6P不管怎么说，真是很感谢\x01",
            "您招待我们过来度假。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x14,
        (
            "#10304F#6P#N是啊，\x01",
            "很有助于转换心情。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0024
    ChrTalk(
        0x13,
        "#10109F#11P市长，谢谢您了。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x9,
        "#06409F#11P我玩得非常开心！\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        "#01109F#6P琪雅也很开心。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xF,
        "#02804F#5P哈哈，那真是再好不过了。\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xF)

    #C0028
    ChrTalk(
        0xF,
        (
            "#02803F#5P抱歉，我又要重提不愉快的话题了，\x01",
            "那真是一起很不幸的事件啊。\x02\x03",

            "#02801F就算是企图爆破\x01",
            "兰花塔的恐怖分子……\x02\x03",

            "也不应该以那种形式\x01",
            "惨死收场，他们的罪孽\x01",
            "并没有深重到如此程度。\x02\x03",

            "#02803F为了不让那样的事件再度发生，\x01",
            "我一定会倾尽全力。\x02\x03",

            "#02800F这也是为了让大家相信\x01",
            "这个世界上还存在着『正义』。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x13,
        "#10108F#11P啊……\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#00008F#6P迪塔市长……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x10,
        (
            "#00104F#6P……听您这样一说，\x01",
            "我似乎也可以渐渐释怀了。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x11,
        (
            "#00203F#6P但是，说到调查独立意向\x01",
            "的居民投票活动……\x02\x03",

            "#00200F如果赞同的意见占到多数，\x01",
            "我们就能够独立了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xF,
        (
            "#02806F#5P不，居民投票这个活动本身\x01",
            "并没有决定是否可以独立的效力。\x02\x03",

            "#02804F但投票的结果却可以向\x01",
            "境外各国传达我们的意向。\x02\x03",

            "接下来，将会慢慢形成国际舆论，\x01",
            "我们就在那种环境下努力摆脱\x01",
            "两大国的束缚，从而获得独立……\x02\x03",

            "#02800F这就是我策划的剧本。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x12,
        "#00303F#6P原来如此……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x14,
        (
            "#10302F#6P#N说起来虽然轻松，\x01",
            "但这条道路似乎相当险峻吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0036
    ChrTalk(
        0x13,
        "#10101F#11P瓦、瓦吉……！\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xF,
        (
            "#02803F#5P无妨，正如你所说。\x02\x03",

            "#02801F以地缘政治学的观点来说，\x01",
            "克洛斯贝尔想成为独立国家\x01",
            "是相当困难的……\x02\x03",

            "#02800F但我认为人类\x01",
            "并不是一种只会\x01",
            "随波逐流的生物。\x02\x03",

            "就算面对困境，我们也要\x01",
            "坚持追求理想与荣耀……\x02\x03",

            "#02804F我相信克洛斯贝尔的各位\x01",
            "蕴藏着那样的力量与希望。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x10,
        "#00102F#6P……迪塔叔叔……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#00003F#6P追求理想与荣耀\x01",
            "的力量与希望吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xC,
        "#01808F#11P…………………………\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xB,
        "#01704F#11P嗯……原来如此。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xF,
        (
            "#02803F#5P克洛斯贝尔今后也许会\x01",
            "踏上一条困难重重的艰辛之路……\x02\x03",

            "我们这些长辈自然会\x01",
            "拿出不惜粉身碎骨的觉悟，\x01",
            "尽全力为你们开拓未来的道路。\x02\x03",

            "#02800F但是，继承我们的心血，\x01",
            "并完成更高的目标，\x01",
            "就是你们这些年轻人的任务了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0043
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "迪塔市长环视了整席，\x01",
            "随后将头深深低下。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    #C0044
    ChrTalk(
        0xF,
        (
            "#02804F#5P在座的各位，\x01",
            "请用你们自己的方式，\x01",
            "为克洛斯贝尔的明天而努力吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2100, 1350, -8280, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，晚餐会结束，\x01",
            "大家返回酒店三层……\x02\x03",

            "虽然保持着一股不可思议的兴奋感，\x01",
            "但终究已经玩得筋疲力尽的罗伊德等人\x01",
            "很快便回各自的房间休息了。\x02\x03",

            "随后──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 1)
    NewScene("e430B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_21D end

    SaveToFile()

Try(main)
