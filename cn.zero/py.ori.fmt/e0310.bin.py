from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "e0310.bin",                # FileName
        "e0310",                    # MapName
        "e0310",                    # Location
        0x0001,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e0310",                  # 0
        "哈罗德",                 # 1
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_C0",           # 00, 0
        "Function_1_D0",           # 01, 1
        "Function_2_D1",           # 02, 2
        "Function_3_7E5",          # 03, 3
    ))


    def Function_0_C0(): pass

    label("Function_0_C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_CF")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 2)

    label("loc_CF")

    Return()

    # Function_0_C0 end

    def Function_1_D0(): pass

    label("Function_1_D0")

    Return()

    # Function_1_D0 end

    def Function_2_D1(): pass

    label("Function_2_D1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50101.itc", 0x1E)
    LoadChrToIndex("chr/ch00002.itc", 0x1F)
    LoadChrToIndex("chr/ch00102.itc", 0x20)
    LoadChrToIndex("chr/ch00202.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    SoundLoad(460)
    OP_68(210, 1100, -880, 0)
    MoveCamera(320, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11750, 0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 850, 100, -2000, 180)
    SetChrPos(0x102, 950, 100, 550, 180)
    SetChrPos(0x103, 50, 100, 550, 180)
    SetChrPos(0x104, -850, 100, 550, 180)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -650, 100, -1850, 180)
    Sound(460, 2, 100, 0)
    BeginChrThread(0x101, 3, 0, 3)
    FadeToBright(1000, 0)
    SetCameraDistance(10750, 2000)
    OP_6F(0x10)
    OP_0D()
    Sleep(100)
    SetChrSubChip(0x101, 0x2)
    Sleep(200)

    #C0001
    ChrTalk(
        0x101,
        (
            "#0000F#12P……真不好意思，\x01",
            "麻烦您特意送我们回去。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "#3609F#5P哈哈，不用客气，\x01",
            "只是顺路罢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x104,
        (
            "#0302F#11P不过，能拥有自己的车子，\x01",
            "可真是很厉害啊。\x02\x03",

            "这一定非常贵吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x103,
        (
            "#0203F#11P这种级别的私家车，\x01",
            "价格应该在八十万米拉左右。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        "#0005F#12P八十万米拉……真的很昂贵呢。\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "#3604F#5P呵呵，作为贸易商人，\x01",
            "这也算是生意工具吧。\x02\x03",

            "#3600F虽然也可以乘坐巴士，\x01",
            "但在很多时候，\x01",
            "时间并不允许呢……\x02\x03",

            "于是，我在去年下定决心，\x01",
            "咬牙买了下来。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x102,
        (
            "#0104F#11P呵呵，除了工作原因之外，\x01",
            "好像还有其它理由吧？\x02\x03",

            "#0102F比如说，想尽早见到\x01",
            "等待自己回家的妻子和儿子。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0008
    ChrTalk(
        0x8,
        "#3609F#5P哈哈……被你说中了呢。\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x104,
        (
            "#0302F#11P原来如此，好像还精心\x01",
            "准备了礼物呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        (
            "#0202F#11P……这就是所谓的\x01",
            "顾家好男人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "#3604F#5P哎呀……哪里的话。\x02\x03",

            "#3600F我平时总是要东奔西跑，\x01",
            "所以经常会冷落\x01",
            "妻子和儿子……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        "#0000F#12P您的儿子今年多大呢？\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#3609F#5P今年五岁了。\x02\x03",

            "虽然还不能去主日学校上学，\x01",
            "但好奇心非常旺盛……\x02\x03",

            "#3600F那种对任何事物都充满好奇心的性格，\x01",
            "真是给妻子添了不少麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#0002F#12P是吗……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        "#0102F#11P呵呵，看起来，好像是很幸福的一家人嘛。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "#3609F#5P哈哈……那当然。\x02\x03",

            "#3608F#30W而且我──我们\x01",
            "必须要幸福。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1500)

    #C0017
    ChrTalk(
        0x101,
        "#0005F#12P哎……？\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "#3605F#5P啊，没什么……\x01",
            "对不起，我在自言自语。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0019
    ChrTalk(
        0x8,
        (
            "#3600F#5P喔……这就要开出古道了。\x02\x03",

            "车会向右拐弯，\x01",
            "各位，请坐稳哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    OP_25(0x1CC, 0x5A)
    Sleep(80)
    OP_25(0x1CC, 0x50)
    Sleep(80)
    OP_25(0x1CC, 0x46)
    Sleep(80)
    OP_25(0x1CC, 0x3C)
    Sleep(80)
    OP_25(0x1CC, 0x32)
    Sleep(80)
    OP_25(0x1CC, 0x28)
    Sleep(80)
    OP_25(0x1CC, 0x1E)
    Sleep(80)
    OP_25(0x1CC, 0x14)
    Sleep(80)
    OP_25(0x1CC, 0xA)
    Sleep(80)
    OP_25(0x1CC, 0x0)
    OP_24(0x1CC)
    SetScenarioFlags(0x5C, 0)
    NewScene("r0030", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_D1 end

    def Function_3_7E5(): pass

    label("Function_3_7E5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_809")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_3_7E5")

    label("loc_809")

    Return()

    # Function_3_7E5 end

    SaveToFile()

Try(main)
