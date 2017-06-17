from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "e3010.bin",                # FileName
        "e3010",                    # MapName
        "e3010",                    # Location
        0x0000,                     # MapIndex
        "ed7515",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e3010",                  # 0
        "赛尔盖科长",             # 1
        "蔡特",                   # 2
        "船",                     # 3
        "SE控制",                 # 4
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_128",          # 00, 0
        "Function_1_138",          # 01, 1
        "Function_2_14E",          # 02, 2
        "Function_3_D36",          # 03, 3
        "Function_4_D60",          # 04, 4
        "Function_5_D91",          # 05, 5
        "Function_6_DAB",          # 06, 6
        "Function_7_DF7",          # 07, 7
        "Function_8_E36",          # 08, 8
    ))


    def Function_0_128(): pass

    label("Function_0_128")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_137")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 2)

    label("loc_137")

    Return()

    # Function_0_128 end

    def Function_1_138(): pass

    label("Function_1_138")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 0)), scpexpr(EXPR_END)), "loc_14D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x5F, 0)

    label("loc_14D")

    Return()

    # Function_1_138 end

    def Function_2_14E(): pass

    label("Function_2_14E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02702.itc", 0x1E)
    LoadChrToIndex("apl/ch50542.itc", 0x1F)
    SoundLoad(483)
    SoundLoad(126)
    SetChrChipPat(0x0, 0x1, 0x0)
    LoadChrChipPat()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis157.itp")
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    BeginChrThread(0x9, 3, 0, 3)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x8, 0, 300, -1500, 180)
    SetChrPos(0x133, 0, 900, 3300, 0)
    SetChrPos(0x9, -750, 900, 3300, 0)
    SetChrPos(0x101, 0, 900, 300, 0)
    SetChrPos(0x102, -900, 900, 1000, 90)
    SetChrPos(0x103, 900, 900, 1000, 270)
    SetChrPos(0x104, -900, 900, 2100, 90)
    SetChrPos(0x105, 900, 900, 2100, 270)
    BeginChrThread(0xB, 0, 0, 7)
    FadeToBright(1000, 0)
    BeginChrThread(0xB, 1, 0, 4)
    OP_68(690, 9850, 800, 0)
    MoveCamera(250, 6, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(46340, 0)
    OP_68(690, 3850, 800, 5000)
    OP_6F(0x1)
    Sleep(1000)
    EndChrThread(0xB, 0x0)
    EndChrThread(0xB, 0x1)
    OP_0D()
    Fade(1000)
    BeginChrThread(0xB, 1, 0, 5)
    OP_68(160, 1750, 1530, 0)
    MoveCamera(219, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15070, 0)
    OP_0D()
    Sleep(500)
    EndChrThread(0xB, 0x1)

    #C0001
    ChrTalk(
        0x8,
        (
            "#1003F#5P……原来如此。\x02\x03",

            "#1001F算了，彻底无视\x01",
            "我的忠告这件事\x01",
            "先暂且不谈……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    #C0002
    ChrTalk(
        0x101,
        "#0008F#11P对、对不起……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "#1000F#5P问题是那个孩子。\x02\x03",

            "#1003F根据事情的发展走向，\x01",
            "有可能会演变成很严重的问题。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    def lambda_3ED():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3ED)

    def lambda_3FA():
        TurnDirection(0xFE, 0x133, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3FA)
    Sleep(100)

    def lambda_40A():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_40A)

    def lambda_417():
        TurnDirection(0xFE, 0x133, 300)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_417)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)

    #C0004
    ChrTalk(
        0x104,
        (
            "#0303F#11P是啊……\x02\x03",

            "#0301F在竞拍会上，差点被当做人偶\x01",
            "进行拍卖的孩子……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x105,
        (
            "#0406F#5P嗯，真是会引发很多\x01",
            "不好的联想呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x103,
        "#0208F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x102,
        (
            "#0106F#5P……真是没想到，\x01",
            "我本以为，即使是黑手党，也不会\x01",
            "愚蠢到做出这种事情呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x133, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x133, 0xB4, 0x1F4)

    #C0008
    ChrTalk(
        0x133,
        (
            "#5805F#12P嗯～？\x02\x03",

            "#5810F琪雅会遇到\x01",
            "很不好的事情吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        (
            "#0004F#5P别担心……\x01",
            "我们不会让那种事情发生的。\x02\x03",

            "#0001F对了，琪雅。\x02\x03",

            "除了名字之外，\x01",
            "你有没有想起其它的事情呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x133,
        (
            "#5811F#12P嗯～……\x02\x03",

            "#5809F……嘿嘿嘿，\x01",
            "完全想不起来哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        "#0006F#5P是吗……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        "#0108F#5P这可难办了呢……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x104,
        "#0308F#11P………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0014
    ChrTalk(
        0x101,
        "#0001F#5P说起来，兰迪……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)
    Sleep(300)

    #C0015
    ChrTalk(
        0x104,
        (
            "#0304F#11P──哦，关于我的事情，\x01",
            "以后有机会时会告诉你们的。\x02\x03",

            "#0300F……如果我还能\x01",
            "继续留在支援科的话。\x02",
        )
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
    Sleep(1000)

    def lambda_78F():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_78F)
    Sleep(50)

    def lambda_79F():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_79F)
    Sleep(50)

    def lambda_7AF():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7AF)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x105, 1)

    #C0016
    ChrTalk(
        0x101,
        "#0013F#5P……我要生气了，兰迪。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x103,
        (
            "#0201F#6P兰迪前辈，\x01",
            "想开玩笑也要看看气氛啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        (
            "#0101F#5P嗯，不要说那种\x01",
            "根本不好笑的玩笑啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x104,
        "#0302F#11P………抱歉。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x133,
        "#5801F#12P嗯……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x133, 0x9, 500)
    Sleep(300)

    #C0021
    ChrTalk(
        0x133,
        (
            "#5810F#6P喂，狗狗，\x01",
            "罗伊德他们怎么了？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x9,
        "#1203F#11P呜噜噜噜……\x02",
    )

    CloseMessageWindow()
    OP_93(0x105, 0x0, 0x190)

    #C0023
    ChrTalk(
        0x105,
        (
            "#0409F#5P呵呵，这也算是\x01",
            "青春的一种吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x133, 0xB4, 0x1F4)

    #C0024
    ChrTalk(
        0x133,
        "#5805F#12P青春～？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_98C():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_98C)
    Sleep(50)

    def lambda_99C():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_99C)
    Sleep(50)

    def lambda_9AC():
        TurnDirection(0xFE, 0x133, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9AC)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0025
    ChrTalk(
        0x104,
        (
            "#0309F#11P哈哈……\x01",
            "一点都不紧张了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#0012F#5P说起来，\x01",
            "直到刚才，我们还一直处在\x01",
            "被黑手党追击的危机中呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        "#0102F#5P总觉得没有什么真实感呢……\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x103,
        (
            "#0202F#5P……但很遗憾，\x01",
            "那些并不是梦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "#1004F#5P呵呵……\x02\x03",

            "#1002F算了，总之，一切事情\x01",
            "都等回到支援科之后再说吧。\x02\x03",

            "我想，从明天开始……\x01",
            "暂时就要进入严守戒备的状态了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B15():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B15)
    Sleep(50)

    def lambda_B25():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B25)
    Sleep(50)

    def lambda_B35():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B35)
    Sleep(50)

    def lambda_B45():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B45)
    Sleep(50)

    def lambda_B55():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B55)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)

    #C0030
    ChrTalk(
        0x101,
        "#0001F#12P……是……！\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x133,
        "#5809F#12P是～！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(0, 6850, -23170, 0)
    MoveCamera(180, 1, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(35770, 0)
    OP_68(0, 6850, 20170, 6000)
    BeginChrThread(0xB, 1, 0, 6)
    OP_0D()
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    WaitChrThread(0xB, 0)
    WaitChrThread(0xB, 1)
    SetScenarioFlags(0x5A, 2)
    ClearScenarioFlags(0x5A, 3)
    OP_BA(0x4)
    RemoveParty(0x4, 0x0)
    RemoveParty(0x32, 0x0)
    OP_29(0x44, 0x4, 0x10)
    OP_29(0x47, 0x4, 0x10)
    OP_29(0x45, 0x4, 0x20)
    SubItemNumber('纯白之石', 1)
    SubItemNumber(0x32A, 1)
    SubItemNumber('沉重货物', 1)
    SubItemNumber(0x2DB, 1)
    SubItemNumber('迷你沙袋', 1)
    SubItemNumber('红莲钩', 1)
    SubItemNumber(0x33B, 1)
    SubItemNumber('影丸储蓄罐', 1)
    SubItemNumber('点唱机', 1)
    SubItemNumber('咪雪玩偶', 1)
    SubItemNumber('冲浪板', 1)
    OP_E3(0xA)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_E3(0x3)
    Sleep(100)
    MiniGame(0x2B, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_DE(0x27, 0x0)
    OP_DE(0x1E, 0x0)
    OP_DE(0x1F, 0x0)
    Sleep(100)
    OP_68(-1000000, 0, 0, 0)
    OP_C7(0x0, 0x10)
    OP_50(0x50, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5F, 0)
    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0x99), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ShowSaveMenu()
    ClearScenarioFlags(0x5F, 0)
    MiniGame(0x2B, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_C7(0x1, 0x10)
    OP_E3(0xB)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x1E3)
    OP_24(0x7E)
    SetScenarioFlags(0x5D, 3)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_14E end

    def Function_3_D36(): pass

    label("Function_3_D36")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D41")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D5F")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("loc_D41")

    label("loc_D5F")

    Return()

    # Function_3_D36 end

    def Function_4_D60(): pass

    label("Function_4_D60")

    Sound(483, 2, 0, 0)
    Sleep(200)
    OP_25(0x1E3, 0xA)
    Sleep(200)
    OP_25(0x1E3, 0x14)
    Sleep(200)
    OP_25(0x1E3, 0x1E)
    Sleep(200)
    OP_25(0x1E3, 0x28)
    Sleep(200)
    OP_25(0x1E3, 0x32)
    Sleep(200)
    OP_25(0x1E3, 0x3C)
    Return()

    # Function_4_D60 end

    def Function_5_D91(): pass

    label("Function_5_D91")

    OP_25(0x1E3, 0x46)
    Sleep(100)
    OP_25(0x1E3, 0x50)
    Sleep(100)
    OP_25(0x1E3, 0x5A)
    Sleep(100)
    OP_25(0x1E3, 0x64)
    Return()

    # Function_5_D91 end

    def Function_6_DAB(): pass

    label("Function_6_DAB")

    Sleep(2500)
    OP_25(0x1E3, 0x5A)
    Sleep(400)
    OP_25(0x1E3, 0x50)
    Sleep(400)
    OP_25(0x1E3, 0x46)
    Sleep(400)
    OP_25(0x1E3, 0x3C)
    Sleep(400)
    OP_25(0x1E3, 0x32)
    Sleep(400)
    OP_25(0x1E3, 0x28)
    Sleep(400)
    OP_25(0x1E3, 0x1E)
    Sleep(400)
    BeginChrThread(0xB, 0, 0, 8)
    OP_25(0x1E3, 0x14)
    Sleep(400)
    OP_25(0x1E3, 0xA)
    Sleep(400)
    OP_24(0x1E3)
    Return()

    # Function_6_DAB end

    def Function_7_DF7(): pass

    label("Function_7_DF7")

    Sound(126, 2, 0, 0)
    Sleep(100)
    OP_25(0x7E, 0xA)
    Sleep(100)
    OP_25(0x7E, 0x14)
    Sleep(100)
    OP_25(0x7E, 0x1E)
    Sleep(100)
    OP_25(0x7E, 0x28)
    Sleep(100)
    OP_25(0x7E, 0x32)
    Sleep(100)
    OP_25(0x7E, 0x3C)
    Sleep(100)
    OP_25(0x7E, 0x46)
    Sleep(100)
    OP_25(0x7E, 0x50)
    Return()

    # Function_7_DF7 end

    def Function_8_E36(): pass

    label("Function_8_E36")

    OP_25(0x7E, 0x3C)
    Sleep(200)
    OP_25(0x7E, 0x32)
    Sleep(200)
    OP_25(0x7E, 0x28)
    Sleep(200)
    OP_25(0x7E, 0x1E)
    Sleep(200)
    OP_25(0x7E, 0x14)
    Sleep(200)
    OP_25(0x7E, 0xA)
    Sleep(200)
    OP_24(0x7E)
    Return()

    # Function_8_E36 end

    SaveToFile()

Try(main)
