from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t116b.bin",                # FileName
        "t116b",                    # MapName
        "t116b",                    # Location
        0x004A,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 74, 0, 1, 0, 2],
    )

    BuildStringList((
        "t116b",                  # 0
        "艾莉",                   # 1
        "缇欧",                   # 2
        "兰迪",                   # 3
        "瓦吉",                   # 4
        "黑手党",                 # 5
        "黑手党",                 # 6
        "琪雅",                   # 7
        "琪雅",                   # 8
        "SE控制",                 # 9
    ))

    AddCharChip((
        "chr/ch07700.itc",                   # 00
        "chr/ch07800.itc",                   # 01
        "chr/ch07900.itc",                   # 02
        "chr/ch08000.itc",                   # 03
        "apl/ch50363.itc",                   # 04
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

    DeclNpc(699,     0,       2500,    0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(699,     0,       2500,    0,    389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(699,     0,       2500,    0,    389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(1600,    0,       -4699,   180,  389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4000,    0,       1000,    270,  453,  0x0, 0,   4,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(4000,    0,       -1000,   270,  453,  0x0, 0,   4,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-5120,   0,       -230,    1500,    -5120,   800,     -230,    0x007C, 0,  13, 0x0000)
    DeclActor(3780,    0,       3250,    1500,    4710,    2000,    3850,    0x007C, 0,  7,  0x0000)
    DeclActor(-1380,   0,       4940,    1500,    -1380,   1800,    4940,    0x007C, 0,  8,  0x0000)
    DeclActor(-4710,   0,       3940,    1500,    -4710,   1000,    3940,    0x007C, 0,  9,  0x0000)
    DeclActor(-4030,   0,       -3730,   1500,    -4030,   1200,    -3730,   0x007C, 0,  10, 0x0000)

    ScpFunction((
        "Function_0_32C",          # 00, 0
        "Function_1_3E4",          # 01, 1
        "Function_2_3F6",          # 02, 2
        "Function_3_49B",          # 03, 3
        "Function_4_64D",          # 04, 4
        "Function_5_821",          # 05, 5
        "Function_6_A03",          # 06, 6
        "Function_7_BA7",          # 07, 7
        "Function_8_C00",          # 08, 8
        "Function_9_C32",          # 09, 9
        "Function_10_C5E",         # 0A, 10
        "Function_11_C94",         # 0B, 11
        "Function_12_CDC",         # 0C, 12
        "Function_13_1109",        # 0D, 13
        "Function_14_2DC4",        # 0E, 14
        "Function_15_2DE1",        # 0F, 15
        "Function_16_2E00",        # 10, 16
        "Function_17_2E1F",        # 11, 17
        "Function_18_2E73",        # 12, 18
        "Function_19_2EC7",        # 13, 19
        "Function_20_2F91",        # 14, 20
        "Function_21_303B",        # 15, 21
        "Function_22_31DC",        # 16, 22
        "Function_23_3217",        # 17, 23
        "Function_24_32E5",        # 18, 24
        "Function_25_33B3",        # 19, 25
        "Function_26_3488",        # 1A, 26
        "Function_27_3503",        # 1B, 27
    ))


    def Function_0_32C(): pass

    label("Function_0_32C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_36C"),
        (1, "loc_378"),
        (2, "loc_384"),
        (3, "loc_390"),
        (4, "loc_39C"),
        (5, "loc_3A8"),
        (6, "loc_3B4"),
        (SWITCH_DEFAULT, "loc_3C0"),
    )


    label("loc_36C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_378")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_384")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_390")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_39C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_3A8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_3B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_3C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_3CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_3E3")

    Return()

    # Function_0_32C end

    def Function_1_3E4(): pass

    label("Function_1_3E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F5")
    Event(0, 12)

    label("loc_3F5")

    Return()

    # Function_1_3E4 end

    def Function_2_3F6(): pass

    label("Function_2_3F6")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40C")
    OP_66(0x0, 0x1)

    label("loc_40C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_41E")
    OP_70(0x4, 0x78)
    Jump("loc_42A")

    label("loc_41E")

    SetMapObjFrame(0x4, "CA01", 0x1, 0x2)

    label("loc_42A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_436")
    Call(0, 26)

    label("loc_436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_43F")

    label("loc_43F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_465")
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    Jump("loc_490")

    label("loc_465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_47D")
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    Jump("loc_490")

    label("loc_47D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_490")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)

    label("loc_490")

    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)

    label("loc_49A")

    Return()

    # Function_2_3F6 end

    def Function_3_49B(): pass

    label("Function_3_49B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E3")

    #C0001
    ChrTalk(
        0xFE,
        (
            "#5308F话说回来……\x01",
            "全都是十分眼熟的美术品和名画。\x02\x03",

            "到底使用什么渠道，\x01",
            "才能收集到这种商品呢。\x02\x03",

            "#5303F『银』刚才说的\x01",
            "『炸弹』也很令人在意……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0002
    ChrTalk(
        0xFE,
        (
            "#5305F……罗伊德，怎么了？\x02\x03",

            "你的脸色好像不太好……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#5112F……不，没什么。\x02\x03",

            "#5108F（刚才的声音，\x01",
            "  艾莉他们\x01",
            "  果然没听见吗……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_649")

    label("loc_5E3")


    #C0004
    ChrTalk(
        0xFE,
        (
            "#5308F到底是通过什么渠道，\x01",
            "才收集到这种商品的呢。\x02\x03",

            "#5306F鲁巴彻的门路……\x01",
            "似乎比想象的还要宽呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_649")

    TalkEnd(0xFE)
    Return()

    # Function_3_49B end

    def Function_4_64D(): pass

    label("Function_4_64D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BB")

    #C0005
    ChrTalk(
        0xFE,
        (
            "#5400F这些展品好像都是高价物，\x01",
            "不过似乎也有很多恶趣味的东西呢。\x02\x03",

            "#5403F商品果然展现了\x01",
            "主办者的品性吗……\x02\x03",

            "#5408F……话说回来，『银』先生说的\x01",
            "『炸弹』究竟是指什么呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0006
    ChrTalk(
        0xFE,
        (
            "#5400F……罗伊德前辈，怎么了？\x02\x03",

            "从刚才开始，样子就有些奇怪……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#5112F……不，没什么。\x02\x03",

            "#5108F（刚才的声音，\x01",
            "  缇欧他们\x01",
            "  果然没听见吗……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_81D")

    label("loc_7BB")


    #C0008
    ChrTalk(
        0xFE,
        (
            "#5403F……就我个人来说，\x01",
            "没看到什么感兴趣的拍卖品呢。\x02\x03",

            "#5408F本来还期待有\x01",
            "纯金咪西什么的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_81D")

    TalkEnd(0xFE)
    Return()

    # Function_4_64D end

    def Function_5_821(): pass

    label("Function_5_821")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AE")

    #C0009
    ChrTalk(
        0xFE,
        (
            "#5602F那是女武神的石膏雕像吗？\x01",
            "身材还真好啊。\x02\x03",

            "#5606F……话说，除了这个之外，其它那些画啊什么的，\x01",
            "我根本就不知道哪里有欣赏价值呢。\x02\x03",

            "#5601F说起来，『银』那家伙所说的\x01",
            "『炸弹』到底是指什么啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0010
    ChrTalk(
        0xFE,
        (
            "#5605F……喂，怎么了？\x02\x03",

            "#5609F要是肚子疼的话，\x01",
            "让哥哥帮你揉揉如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        (
            "#5112F……不，没什么。\x02\x03",

            "#5108F（刚才的声音，\x01",
            "  兰迪他们\x01",
            "  果然没听见吗……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_9FF")

    label("loc_9AE")


    #C0012
    ChrTalk(
        0xFE,
        (
            "#5601F……炸弹啊……\x02\x03",

            "#5603F从那家伙的说话方式看来，\x01",
            "那似乎不是真正的炸弹。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9FF")

    TalkEnd(0xFE)
    Return()

    # Function_5_821 end

    def Function_6_A03(): pass

    label("Function_6_A03")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B25")

    #C0013
    ChrTalk(
        0xFE,
        (
            "#5705F呼……\x01",
            "似乎全都是些相当昂贵的东西啊。\x02\x03",

            "#5704F反正也被卷进麻烦事了，\x01",
            "不如顺便拿走一件吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#5113F我说啊……\x01",
            "这种事情，我可不能视而不见啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "#5702F呵呵……开个玩笑啦。\x01",
            "我可没有堕落到要偷东西的程度。\x02\x03",

            "#5704F……不过，我可不觉得\x01",
            "这里的商品都来路正当呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_BA3")

    label("loc_B25")


    #C0016
    ChrTalk(
        0xFE,
        (
            "#5702F呵呵……虽说我是不良团伙的头目，\x01",
            "但还没有堕落到要偷东西的程度啦。\x02\x03",

            "#5704F不过，我可不觉得\x01",
            "这里的商品都来路正当呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA3")

    TalkEnd(0xFE)
    Return()

    # Function_6_A03 end

    def Function_7_BA7(): pass

    label("Function_7_BA7")

    TalkBegin(0xFF)
    SetChrName("")

    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里放着女武神的石膏雕像和古陶瓷器，\x01",
            "还有看起来像是诡异面具的东西。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_7_BA7 end

    def Function_8_C00(): pass

    label("Function_8_C00")

    TalkBegin(0xFF)
    SetChrName("")

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里放着禁猎动物的剥制标本。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_8_C00 end

    def Function_9_C32(): pass

    label("Function_9_C32")

    TalkBegin(0xFF)
    SetChrName("")

    #A0019
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里堆靠着美丽的绘画。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_9_C32 end

    def Function_10_C5E(): pass

    label("Function_10_C5E")

    TalkBegin(0xFF)
    SetChrName("")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "这里杂乱无章地放置着古旧的书本。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_10_C5E end

    def Function_11_C94(): pass

    label("Function_11_C94")

    TalkBegin(0xFE)

    #C0021
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "似乎完全失去了意识。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_11_C94 end

    def Function_12_CDC(): pass

    label("Function_12_CDC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-3350, 1200, 0, 0)
    MoveCamera(43, 12, 0, 0)
    MoveCamera(46, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18330, 0)
    SetChrPos(0x101, 6000, 0, 0, 270)
    SetChrPos(0xEF, 7350, 0, 600, 270)
    SetChrPos(0x151, 7000, 0, -600, 270)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis064.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis065.itp")
    FadeToBright(1000, 0)
    OP_68(5940, 1200, 0, 6000)
    OP_6F(0x1)
    Sleep(300)

    #C0023
    ChrTalk(
        0x101,
        "#5105F#11P这里是……\x02",
    )

    CloseMessageWindow()
    OP_C7(0x0, 0x800)
    VolumeBGM(0x28, 0x1F4)
    FadeToDark(500, 0, -1)
    Sound(915, 0, 100, 0)
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    Sleep(200)
    Sound(2179, 255, 75, 0)    #voice#KeA
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    Sleep(200)
    Sound(2044, 255, 75, 0)    #voice#KeA
    OP_CA(0x0, 0x1, 0x3)
    Sleep(1000)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    FadeToBright(500, 0)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    OP_C7(0x1, 0x800)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_F09")

    #C0024
    ChrTalk(
        0x102,
        (
            "#5301F#11P……看起来，这些似乎是要在竞拍会\x01",
            "的后半部分展出拍卖的物品呢。\x02\x03",

            "好像还有很多……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FD2")

    label("loc_F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_F76")

    #C0025
    ChrTalk(
        0x103,
        (
            "#5401F#11P……看来，这些似乎是要在竞拍会\x01",
            "的后半部分展出拍卖的物品呢。\x02\x03",

            "似乎还为数不少……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FD2")

    label("loc_F76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_FD2")

    #C0026
    ChrTalk(
        0x104,
        (
            "#5601F#11P……看来，这些似乎是竞拍会\x01",
            "后半要拍卖的物品呢。\x02\x03",

            "还有很多的样子……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD2")


    #C0027
    ChrTalk(
        0x151,
        (
            "#5704F#11P呵呵，既然要留到后半场才展出，\x01",
            "想必都是些压轴的珍品吧。\x02\x03",

            "#5702F时间也不多了，\x01",
            "分头调查看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#5103F#11P……嗯。\x02\x03",

            "#5108F看起来……\x01",
            "好像真的有什么啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 5130, 0, -200, 270)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    RemoveParty(0x50, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_10C5")
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    RemoveParty(0x1, 0x0)
    Jump("loc_10F6")

    label("loc_10C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_10E0")
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    RemoveParty(0x2, 0x0)
    Jump("loc_10F6")

    label("loc_10E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_10F6")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    RemoveParty(0x3, 0x0)

    label("loc_10F6")

    OP_66(0x0, 0x1)
    SetScenarioFlags(0xA6, 4)
    OP_29(0x47, 0x1, 0xE)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_12_CDC end

    def Function_13_1109(): pass

    label("Function_13_1109")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    SetChrChipPat(0x0, 0x1, 0x4C)
    LoadChrChipPat()
    OP_49()
    LoadChrToIndex("chr/ch31050.itc", 0x1E)
    LoadChrToIndex("chr/ch31051.itc", 0x1F)
    LoadChrToIndex("chr/ch31150.itc", 0x20)
    LoadChrToIndex("chr/ch31151.itc", 0x21)
    LoadChrToIndex("chr/ch08100.itc", 0x23)
    LoadChrToIndex("apl/ch50364.itc", 0x24)
    LoadChrToIndex("apl/ch50365.itc", 0x25)
    LoadChrToIndex("apl/ch50368.itc", 0x26)
    LoadChrToIndex("apl/ch50369.itc", 0x27)
    LoadChrToIndex("chr/ch10800.itc", 0x29)
    LoadChrToIndex("chr/ch31053.itc", 0x2A)
    LoadChrToIndex("chr/ch31153.itc", 0x2B)
    LoadChrToIndex("chr/ch31052.itc", 0x2C)
    LoadChrToIndex("chr/ch31152.itc", 0x2D)
    LoadChrToIndex("chr/ch00000.itc", 0x2E)
    SoundLoad(924)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x25)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x2)
    SetChrFlags(0xE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_11C6")
    AddParty(0x1, 0xEF, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    Jump("loc_11F9")

    label("loc_11C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_11E2")
    AddParty(0x2, 0xEF, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    Jump("loc_11F9")

    label("loc_11E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_11F9")
    AddParty(0x3, 0xEF, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)

    label("loc_11F9")

    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x0)
    OP_4B(0xB, 0xFF)
    FadeToBright(1000, 0)
    OP_68(-3840, 1000, -210, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19330, 0)
    SetCameraDistance(18330, 2000)
    SetChrPos(0x101, -3600, 0, 0, 270)
    SetChrPos(0xEF, 700, 0, 2500, 0)
    SetChrPos(0xB, 1600, 0, -4700, 180)
    SetChrFlags(0x101, 0x8000)
    SetChrFlags(0xEF, 0x8000)
    SetChrFlags(0xB, 0x8000)
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05800.itp")
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2348")
    OP_6F(0x10)

    #C0029
    ChrTalk(
        0x101,
        (
            "#5105F#11P（这个箱子……）\x02\x03",

            "#5101F（看上去很大，\x01",
            "  里面装着什么呢……？）\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(882, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0030
    ChrTalk(
        0x101,
        (
            "#5000F#11P（……虽然上着锁，\x01",
            "  但这种程度的话，还是有办法……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0031
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德从搜查官用的工具盒里\x01",
            "取出了开锁工具。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetCameraDistance(18030, 1500)
    Fade(250)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x2)
    Sound(804, 0, 100, 0)
    OP_6F(0x10)

    #C0032
    ChrTalk(
        0x101,
        (
            "#5003F#11P（在搜查官培训中学到的\x01",
            "  开锁技术……）\x02\x03",

            "#5001F（没想到会在这种地方派上用场……）\x02",
        )
    )

    CloseMessageWindow()
    Sound(833, 0, 100, 0)
    SetCameraDistance(17000, 3000)
    OP_A1(0x101, 0x3E8, 0x4, 0x3, 0x4, 0x3, 0x4)
    Sleep(100)
    OP_A1(0x101, 0x3E8, 0x6, 0x3, 0x4, 0x3, 0x4, 0x3, 0x4)
    Sleep(50)
    Sound(833, 0, 100, 0)
    OP_A1(0x101, 0x3E8, 0x4, 0x3, 0x4, 0x3, 0x4)
    OP_6F(0x10)
    Sound(809, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0033
    ChrTalk(
        0x101,
        "#5002F#11P（──好了。）\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    OP_71(0x4, 0x0, 0x28, 0x0, 0x0)
    Sound(922, 0, 100, 0)
    OP_79(0x4)
    Sleep(300)
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    StopBGM(0x1770)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(2000)
    OP_64(0x101)

    #C0034
    ChrTalk(
        0x101,
        "#5005F#11P……………………哎？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-4500, 1000, 79640, 0)
    MoveCamera(315, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(14860, 2500)
    SetChrPos(0x101, -3600, 0, 80000, 270)
    SetChrPos(0xEF, 700, 0, 82500, 0)
    SetChrPos(0xB, 1600, 0, 76700, 180)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x101, 0x8)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrPos(0xE, -5000, -200, 79750, 90)
    SetChrPos(0xF, -5000, -800, 79750, 90)
    OP_A7(0xE, 0x40, 0x40, 0x40, 0xFF, 0x0)
    SetChrFlags(0xF, 0x8)
    BeginChrThread(0xE, 0, 0, 14)
    OP_70(0x5, 0x28)
    OP_71(0x5, 0x28, 0x78, 0x0, 0x0)
    Sound(923, 0, 100, 0)

    def lambda_1645():
        OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1645)
    WaitChrThread(0xE, 1)
    OP_79(0x5)
    OP_6F(0x10)
    OP_0D()
    SetChrSubChip(0x101, 0x9)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0035
    ChrTalk(
        0x101,
        "#5011F#11P…………啊………………\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrPos(0xE, -5000, 50, 79750, 90)
    ClearChrFlags(0xE, 0x1)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x230), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x230), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x230), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x16)
    OP_68(-4260, 1000, 79730, 0)
    MoveCamera(311, 34, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(9670, 0)
    SetCameraDistance(8670, 10000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7304", 0)
    Sleep(2000)

    #C0036
    ChrTalk(
        0x101,
        (
            "#5005F#30W#11P（莫非……\x01",
            "  这就是罗赞贝尔克工房的……？）\x02\x03",

            "#5008F（简、简直就像是\x01",
            "  活人一样……）\x02\x03",

            "（但、但是，这也太……）\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 50, -1, -1)
    #Sound(2026, 255, 70, 0)    #voice#KeA
    Sleep(300)
    SetChrName("声音")

    #A0037
    AnonymousTalk(
        0xFF,
        "#2S#80W………嗯…………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sleep(150)
    EndChrThread(0xE, 0x0)
    OP_A1(0xE, 0x3E8, 0x4, 0x0, 0x5, 0x6, 0x7)
    Sound(820, 0, 100, 0)
    OP_A1(0xE, 0x3E8, 0x2, 0x9, 0xA)
    OP_A1(0xE, 0x3E8, 0x4, 0xB, 0xC, 0xD, 0xC)
    OP_A1(0xE, 0x3E8, 0x4, 0xB, 0xC, 0xD, 0xC)
    OP_A1(0xE, 0x3E8, 0x3, 0xD, 0xE, 0xF)
    BeginChrThread(0xE, 0, 0, 15)
    Sleep(1000)

    #N0038
    NpcTalk(
        0xF,
        "人偶？",
        "#80W#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    #Sound(2027, 255, 80, 0)    #voice#KeA
    Sleep(500)
    SetChrName("人偶？")

    #A0039
    AnonymousTalk(
        0xFF,
        "#50W……大哥哥，你是谁？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(150)
    Fade(500)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x1)
    BeginChrThread(0xE, 0, 0, 16)
    SetChrPos(0xE, -5000, -200, 79750, 90)
    SetChrFlags(0xE, 0x1)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(2000)
    SetCameraDistance(14000, 0)
    SetCameraDistance(19000, 800)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0040
    ChrTalk(
        0x101,
        "#5007F#4S#11P#16A哇啊啊啊！？\x02",
    )
    #Auto

    OP_6F(0x10)
    Sleep(500)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1A20():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1A20)

    def lambda_1A2D():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1A2D)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0xB, 1)
    OP_68(-4260, 1000, 79730, 2000)
    MoveCamera(311, 22, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(14360, 2000)

    def lambda_1A70():
        OP_95(0xFE, -3250, 0, 81490, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1A70)

    def lambda_1A8A():
        OP_95(0xFE, -2080, 0, 79080, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1A8A)
    WaitChrThread(0xEF, 1)

    def lambda_1AA8():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1AA8)
    WaitChrThread(0xEF, 1)

    def lambda_1AB9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1AB9)
    WaitChrThread(0xB, 1)
    OP_6F(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1B02")

    #C0041
    ChrTalk(
        0x102,
        (
            "#5301F#2P怎、怎么了……？\x02\x03",

            "#5305F！！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B75")

    label("loc_1B02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1B39")

    #C0042
    ChrTalk(
        0x103,
        (
            "#5401F#2P……怎么了？\x02\x03",

            "#5405F！！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B75")

    label("loc_1B39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1B75")

    #C0043
    ChrTalk(
        0x104,
        (
            "#5605F#2P怎么，出什么事了……？\x02\x03",

            "#5601F！！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B75")


    #C0044
    ChrTalk(
        0xB,
        "#5705F#12P……这孩子是………\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#5011F#11P#30W你、你……\x02\x03",

            "为什么会在这种地方……\x02",
        )
    )

    CloseMessageWindow()

    #N0046
    NpcTalk(
        0xF,
        "女孩",
        (
            "#5805F#5P#30W怎么了？\x01",
            "眼睛瞪得那么圆。\x02\x03",

            "#5809F啊哈哈！\x01",
            "大哥哥，好好玩哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#5006F#11P这、这个，好玩什么的先不说……\x02\x03",

            "#5008F难道说，你是偶然\x01",
            "进入这里面的吗……\x02\x03",

            "#5013F你知道自己的爸爸和妈妈\x01",
            "都在哪里吗！？\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xF, -4850, -400, 79950, 135)
    OP_63(0xF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #N0048
    NpcTalk(
        0xE,
        "女孩",
        (
            "#5805F#5P#30W？？？\x02\x03",

            "爸爸？妈妈？\x02\x03",

            "琪雅，不知道那些哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#5003F#11P琪雅……\x01",
            "你的名字叫琪雅吗？\x02\x03",

            "#5008F不过，到底是谁家的……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1DC8")

    #C0050
    ChrTalk(
        0x102,
        (
            "#5306F#2P那、那个，罗伊德……\x02\x03",

            "#5308F看这孩子的打扮，怎么想\x01",
            "也都不像是来宾的孩子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E87")

    label("loc_1DC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1E28")

    #C0051
    ChrTalk(
        0x103,
        (
            "#5406F#2P罗伊德前辈……\x02\x03",

            "#5411F看这孩子的打扮，怎么想\x01",
            "也不像是来宾的孩子……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E87")

    label("loc_1E28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1E87")

    #C0052
    ChrTalk(
        0x104,
        (
            "#5606F#2P喂，罗伊德……\x02\x03",

            "#5601F你看这孩子的打扮，怎么想\x01",
            "也都不像是来宾的孩子吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E87")

    OP_63(0x101, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0053
    ChrTalk(
        0x101,
        (
            "#5006F#11P啊，真是的……\x01",
            "我当然明白啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xB,
        (
            "#5704F#12P呵呵……原来如此呢。\x02\x03",

            "看来，这孩子……\x01",
            "就是所谓的『炸弹』了。\x02\x03",

            "#5702F本应装有罗赞贝尔克工房\x01",
            "人偶的箱子……\x02\x03",

            "如果就这样拿到会场，\x01",
            "然后当众打开盖子的话……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0055
    ChrTalk(
        0x101,
        "#5013F#11P啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1FF1")

    #C0056
    ChrTalk(
        0x102,
        "#5301F#2P原、原来如此……\x02",
    )

    CloseMessageWindow()
    Jump("loc_204E")

    label("loc_1FF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_201E")

    #C0057
    ChrTalk(
        0x103,
        "#5401F#2P……原来如此……\x02",
    )

    CloseMessageWindow()
    Jump("loc_204E")

    label("loc_201E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_204E")

    #C0058
    ChrTalk(
        0x104,
        "#5603F#2P……原来是这么回事吗……\x02",
    )

    CloseMessageWindow()

    label("loc_204E")


    #N0059
    NpcTalk(
        0xF,
        "琪雅",
        (
            "#5800F#5P#30W哦～大哥哥，\x01",
            "你叫罗伊德啊。\x02\x03",

            "#5803F罗伊德……罗伊德……\x02\x03",

            "#5809F嘿嘿……是个好名字哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#5012F#11P谢、谢谢……\x02\x03",

            "#5011F──不对，现在要说的可不是这些啊！\x02\x03",

            "#5013F琪雅！\x01",
            "你还记得其它什么事吗！？\x02\x03",

            "比如说认识的人，\x01",
            "或是住在哪里之类的！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    #Sound(2028, 255, 85, 0)    #voice#KeA
    Sleep(300)

    #N0061
    NpcTalk(
        0xF,
        "琪雅",
        "#5811F#5P……嗯～\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xF, -4850, -400, 79950, 135)
    OP_63(0xF, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xF)

    #N0062
    NpcTalk(
        0xF,
        "琪雅",
        (
            "#5809F#5P嘿嘿……\x01",
            "什么也想不起来啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#5006F#11P（打击）……\x02\x03",

            "#5013F──总、总之，\x01",
            "不能让你继续待在这里。\x02\x03",

            "先从这里出去──\x02",
        )
    )

    CloseMessageWindow()
    Sound(924, 2, 100, 0)
    Sleep(500)
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0064
    ChrTalk(
        0x101,
        "#5010F#11P呜……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_22C8")

    #C0065
    ChrTalk(
        0x102,
        "#5307F#2P不好……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2317")

    label("loc_22C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_22F3")

    #C0066
    ChrTalk(
        0x103,
        "#5407F#2P……糟糕……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2317")

    label("loc_22F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2317")

    #C0067
    ChrTalk(
        0x104,
        "#5607F#2P不妙啊……！\x02",
    )

    CloseMessageWindow()

    label("loc_2317")


    #C0068
    ChrTalk(
        0xB,
        (
            "#5703F#12P哎呀哎呀……\x01",
            "看来已经被发现了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2348")

    Sound(103, 0, 70, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xC, 10000, 0, 80000, 270)
    SetChrPos(0xD, 10000, 0, 80000, 270)

    #N0069
    NpcTalk(
        0xC,
        "男人的声音",
        "#2S什么……！\x02",
    )

    CloseMessageWindow()

    #N0070
    NpcTalk(
        0xC,
        "男人的声音",
        "#2S不可能，竟然有入侵者！？\x02",
    )

    CloseMessageWindow()

    #N0071
    NpcTalk(
        0xD,
        "男人的声音",
        "#2S快、快确认拍卖品！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(103, 0, 100, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7509", 0)
    ReplaceBGM("ed7000", "ed7000")
    ReplaceBGM("ed7513", "ed7509")
    ReplaceBGM("ed7125", "ed7509")
    OP_68(-2500, 1100, 0, 0)
    MoveCamera(40, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18330, 0)
    OP_68(0, 1100, 0, 2000)
    SetChrPos(0x101, -3600, 0, 0, 270)
    SetChrPos(0xEF, -3250, 0, 1490, 0)
    SetChrPos(0xB, -2080, 0, -1080, 180)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0xC, 10000, 0, 0, 270)
    SetChrPos(0xD, 10000, 0, 0, 270)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrPos(0xE, -4850, -200, -250, 90)
    SetChrSubChip(0xE, 0x1C)
    SetChrPos(0xF, -4850, -800, -250, 90)
    OP_70(0x4, 0x78)
    SetMapObjFrame(0x4, "CA01", 0x0, 0x2)
    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0x5)

    def lambda_251E():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_251E)

    def lambda_252B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_252B)

    def lambda_2538():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2538)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0xB, 1)
    BeginChrThread(0xC, 3, 0, 17)
    Sleep(500)
    BeginChrThread(0xD, 3, 0, 18)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    OP_6F(0x1)
    OP_0D()
    BeginChrThread(0x10, 1, 0, 27)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_269D")

    #C0072
    ChrTalk(
        0x104,
        "#5611F#5P……喝……！\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xB,
        "#5707F#6P咻……！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xB, 3, 0, 19)
    BeginChrThread(0x104, 3, 0, 20)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x104, 3)
    Sleep(850)
    OP_68(-1350, 1400, 0, 2000)
    MoveCamera(45, 16, 0, 2000)
    SetCameraDistance(17350, 2000)
    OP_93(0xB, 0x10E, 0x12C)
    OP_93(0x104, 0x10E, 0x1F4)
    OP_6F(0x79)

    #N0074
    NpcTalk(
        0xF,
        "琪雅",
        "#5805F#5P哎～……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        "#5001F#5P兰迪、瓦吉……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xB,
        (
            "#5702F#11P──看样子，\x01",
            "我们接下来就要有所觉悟了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x104,
        (
            "#5601F#11P嗯，这样下去的话，\x01",
            "早晚会被抓到的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27D9")

    label("loc_269D")


    #C0078
    ChrTalk(
        0xB,
        "#5707F#5P咻……！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xB, 3, 0, 21)
    WaitChrThread(0xB, 3)
    Sleep(500)
    OP_68(-1350, 1400, 0, 2000)
    MoveCamera(45, 16, 0, 2000)
    SetCameraDistance(17350, 2000)
    OP_93(0xB, 0x10E, 0x12C)
    OP_6F(0x79)

    #N0079
    NpcTalk(
        0xF,
        "琪雅",
        "#5805F#5P哎～……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_273C")

    #C0080
    ChrTalk(
        0x102,
        "#5305F#5P动、动作好敏捷啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2762")

    label("loc_273C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2762")

    #C0081
    ChrTalk(
        0x103,
        "#5405F#5P动作好敏捷……\x02",
    )

    CloseMessageWindow()

    label("loc_2762")


    #C0082
    ChrTalk(
        0x101,
        "#5013F#5P瓦吉……\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xB,
        (
            "#5706F#11P──看样子，\x01",
            "我们接下来就要有所觉悟了啊。\x02\x03",

            "#5702F这样下去，\x01",
            "一定会被他们抓住的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27D9")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0084
    ChrTalk(
        0x101,
        "#5003F#5P……明白了。\x02",
    )

    CloseMessageWindow()

    def lambda_2811():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2811)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2833")
    Sleep(100)

    def lambda_282B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_282B)

    label("loc_2833")

    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    Sleep(300)
    OP_68(-3650, 1400, 0, 1500)
    SetCameraDistance(15060, 1500)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x7)
    Sleep(500)
    Sound(534, 0, 90, 0)
    Sound(804, 0, 100, 0)
    Fade(500)
    OP_A1(0x101, 0x7D0, 0x4, 0x7, 0x0, 0x1, 0x2)
    SetChrChipByIndex(0x101, 0x2E)
    SetChrSubChip(0x101, 0x0)
    OP_A1(0x101, 0x7D0, 0x5, 0x3, 0x4, 0x5, 0x6, 0x7)
    OP_6F(0x79)
    Sleep(500)
    OP_68(-4100, 1200, 0, 1500)
    SetCameraDistance(14300, 1500)
    Sleep(100)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x5)
    Sound(804, 0, 100, 0)
    OP_6F(0x79)
    OP_A1(0x101, 0x3E8, 0x4, 0x6, 0x7, 0x6, 0x5)

    #C0085
    ChrTalk(
        0x101,
        (
            "#0000F#11P琪雅，\x01",
            "你能和我们一起走吗？\x02\x03",

            "我们一定会保护你的。\x02",
        )
    )

    CloseMessageWindow()

    #N0086
    NpcTalk(
        0xF,
        "琪雅",
        (
            "#5800F#5P？？？\x02\x03",

            "#5810F虽然不太明白，\x01",
            "不过可以哦～\x02\x03",

            "#5809F琪雅，要和罗伊德一起走！\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        "#0002F#11P……乖孩子。\x02",
    )

    CloseMessageWindow()
    OP_68(-4300, 1200, 0, 1000)
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(-3650, 1400, 0, 1000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x0)
    Sound(910, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_6F(0x79)
    OP_0D()

    #N0088
    NpcTalk(
        0x101,
        "琪雅",
        "#5810F#5P哇……！\x02",
    )

    CloseMessageWindow()
    OP_68(-920, 1400, 210, 1200)
    SetCameraDistance(16270, 1200)

    def lambda_2A23():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2A23)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2AE9")

    #C0089
    ChrTalk(
        0x101,
        (
            "#0001F#5P──两位，\x01",
            "都换回便于行动的装束吧。\x02\x03",

            "#0003F还有，必须得联络在外面待命的\x01",
            "兰迪他们——\x02\x03",

            "#0007F接下来，要带着这孩子\x01",
            "逃脱议长宅邸……！\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x102,
        "#5307F……明白了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C53")

    label("loc_2AE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2B9F")

    #C0091
    ChrTalk(
        0x101,
        (
            "#0001F#5P──两位，\x01",
            "都换回便于行动的装束吧。\x02\x03",

            "#0003F还有，必须得联络在外面待命的\x01",
            "艾莉他们——\x02\x03",

            "#0007F接下来，要带着这孩子\x01",
            "逃脱议长宅邸……！\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x103,
        "#5401F明白……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C53")

    label("loc_2B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2C53")

    #C0093
    ChrTalk(
        0x101,
        (
            "#0001F#5P──两位，\x01",
            "都换回便于行动的装束吧。\x02\x03",

            "#0003F还有，必须得联络在外面待命的\x01",
            "艾莉她们——\x02\x03",

            "#0007F接下来，要带着这孩子\x01",
            "逃脱议长宅邸……！\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x104,
        "#5607F#2P是，队长！\x02",
    )

    CloseMessageWindow()

    label("loc_2C53")


    #C0095
    ChrTalk(
        0xB,
        (
            "#5702F#11P呵呵……\x01",
            "事情开始变得有趣了嘛。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16600, 1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x10, 0x1)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x32, 0xFF, 0xFF)
    Call(0, 26)
    OP_32(0x4, 0x0, 0x1D)
    RemoveCraft(0x4, 0xFFFF)
    OP_38(0x4, 0x80, 0x2)
    OP_38(0x4, 0x81, 0x1)
    OP_38(0x4, 0x82, 0x2)
    OP_38(0x4, 0x83, 0x2)
    OP_38(0x4, 0x84, 0x2)
    OP_38(0x4, 0x85, 0x2)
    OP_38(0x4, 0x86, 0x1)
    OP_42(0x4, 0x439, 0xFF)
    OP_42(0x4, 0x5E7, 0xFF)
    OP_42(0x4, 0x64B, 0xFF)
    AddCraft(0x4, 0xBE)
    AddCraft(0x4, 0xBF)
    AddCraft(0x4, 0xC0)
    AddCraft(0x4, 0x10E)
    SetChrChipPat(0x4, 0x6, 0x10E)
    AddCraft(0x4, 0x138)
    OP_42(0x4, 0x86, 0x0)
    OP_42(0x4, 0x77, 0x3)
    OP_42(0x4, 0x65, 0x4)
    OP_42(0x4, 0x6B, 0x5)
    OP_42(0x4, 0x7D, 0x6)
    OP_42(0x4, 0x71, 0x1)
    OP_42(0x4, 0x80, 0x2)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    OP_D5(0x2C)
    OP_D5(0x2D)
    OP_D5(0x2E)
    SetChrChipPat(0x0, 0x1, 0x9A)
    LoadChrChipPat()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2D6C")
    SetChrChipPat(0x1, 0x1, 0x1)
    LoadChrChipPat()
    Jump("loc_2D93")

    label("loc_2D6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2D82")
    SetChrChipPat(0x2, 0x1, 0x2)
    LoadChrChipPat()
    Jump("loc_2D93")

    label("loc_2D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2D93")
    SetChrChipPat(0x3, 0x1, 0x3)
    LoadChrChipPat()

    label("loc_2D93")

    SetChrPos(0x0, -2520, 0, -200, 90)
    OP_70(0x1, 0x5)
    SetMapObjFlags(0x1, 0x10)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0xA6, 5)
    OP_29(0x47, 0x1, 0xF)
    OP_24(0x39C)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_13_1109 end

    def Function_14_2DC4(): pass

    label("Function_14_2DC4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DE0")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x2, 0x1)
    Jump("Function_14_2DC4")

    label("loc_2DE0")

    Return()

    # Function_14_2DC4 end

    def Function_15_2DE1(): pass

    label("Function_15_2DE1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2DFF")
    OP_A1(0xFE, 0x3E8, 0x5, 0x10, 0x11, 0x12, 0x11, 0x10)
    Sleep(3000)
    Jump("Function_15_2DE1")

    label("loc_2DFF")

    Return()

    # Function_15_2DE1 end

    def Function_16_2E00(): pass

    label("Function_16_2E00")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E1E")
    OP_A1(0xFE, 0x3E8, 0x5, 0x18, 0x19, 0x1A, 0x19, 0x18)
    Sleep(3000)
    Jump("Function_16_2E00")

    label("loc_2E1E")

    Return()

    # Function_16_2E00 end

    def Function_17_2E1F(): pass

    label("Function_17_2E1F")

    SetChrPos(0xFE, 9650, 0, 0, 270)

    def lambda_2E35():
        OP_95(0xFE, 4570, 0, 800, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E35)

    def lambda_2E4F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E4F)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_17_2E1F end

    def Function_18_2E73(): pass

    label("Function_18_2E73")

    SetChrPos(0xFE, 9650, 0, 0, 270)

    def lambda_2E89():
        OP_95(0xFE, 4570, 0, -800, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E89)

    def lambda_2EA3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2EA3)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_18_2E73 end

    def Function_19_2EC7(): pass

    label("Function_19_2EC7")

    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    OP_68(3130, 1400, 0, 800)
    MoveCamera(60, 16, 0, 800)
    SetCameraDistance(15330, 800)
    Sound(2091, 255, 100, 0)    #voice#Lazy
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    SetChrSubChip(0xFE, 0x3)

    def lambda_2F1A():
        OP_9D(0xFE, 0xD02, 0x0, 0xFFFFFCCC, 0x640, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F1A)
    Sound(814, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_82(0x1F4, 0x0, 0x1770, 0x190)
    Sound(2093, 255, 100, 0)    #voice#Lazy
    Sound(534, 0, 100, 0)
    OP_A1(0xFE, 0xDAC, 0x2, 0x14, 0x13)
    BeginChrThread(0xD, 3, 0, 24)
    Sleep(350)
    SetChrSubChip(0xFE, 0xE)
    Sleep(50)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x10)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_19_2EC7 end

    def Function_20_2F91(): pass

    label("Function_20_2F91")

    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    Sound(1294, 255, 100, 0)    #voice#Randy
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)

    def lambda_2FBE():
        OP_9D(0xFE, 0xDDE, 0x0, 0x35C, 0x4B0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FBE)
    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Sleep(200)
    OP_82(0x1F4, 0x0, 0x1770, 0x190)
    OP_68(5430, 1400, 0, 200)
    SetCameraDistance(16900, 200)
    SetChrSubChip(0xFE, 0x1)
    Sound(532, 0, 100, 0)
    BeginChrThread(0xC, 3, 0, 25)
    Sleep(500)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x10)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_20_2F91 end

    def Function_21_303B(): pass

    label("Function_21_303B")

    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    OP_68(3130, 1400, 0, 800)
    MoveCamera(60, 16, 0, 800)
    SetCameraDistance(15330, 800)
    Sound(2091, 255, 100, 0)    #voice#Lazy
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    SetChrSubChip(0xFE, 0x3)

    def lambda_308E():
        OP_9D(0xFE, 0xD02, 0x0, 0xFFFFFCCC, 0x640, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_308E)
    Sound(814, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Sleep(200)
    OP_82(0x1F4, 0x0, 0x1770, 0x190)
    Sound(2094, 255, 100, 0)    #voice#Lazy
    Sound(541, 0, 100, 0)
    OP_A1(0xFE, 0xDAC, 0x2, 0xE, 0xC)
    BeginChrThread(0xD, 3, 0, 24)
    OP_A1(0xFE, 0xDAC, 0x3, 0xA, 0x8, 0xC)
    Sleep(350)
    BeginChrThread(0xC, 3, 0, 22)
    OP_A1(0xFE, 0x9C4, 0x2, 0xD, 0x1)
    OP_6F(0x79)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    SetChrSubChip(0xFE, 0x1)

    def lambda_3113():
        OP_9D(0xFE, 0xA0A, 0x0, 0xFFFFF8B2, 0x320, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3113)
    Sound(804, 0, 100, 0)
    WaitChrThread(0xFE, 1)

    def lambda_313A():
        OP_9D(0xFE, 0xC3A, 0x0, 0xFFFFFC90, 0x320, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_313A)
    Sound(534, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_68(4300, 1400, 670, 150)
    OP_82(0x1F4, 0x0, 0x1770, 0x190)
    Sound(2093, 255, 100, 0)    #voice#Lazy
    SetChrSubChip(0xFE, 0x11)
    BeginChrThread(0xC, 3, 0, 23)
    OP_6F(0x79)
    OP_68(3130, 1400, 0, 1000)
    Sleep(500)
    OP_A1(0xFE, 0x3E8, 0x1, 0xD)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x10)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)
    TurnDirection(0xFE, 0xC, 0)
    OP_6F(0x79)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xD, 1)
    Return()

    # Function_21_303B end

    def Function_22_31DC(): pass

    label("Function_22_31DC")

    OP_93(0xFE, 0xE1, 0x1F4)
    SetChrChipByIndex(0xFE, 0x2C)
    OP_A1(0xFE, 0xDAC, 0x2, 0x0, 0x1)
    SetChrFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x3)

    def lambda_31FD():
        OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31FD)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_22_31DC end

    def Function_23_3217(): pass

    label("Function_23_3217")

    PlayEffect(0xA, 0xFF, 0xFF, 0x0, 4570, 800, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3260():
        OP_96(0xFE, 0x1CAC, 0x3E8, 0x9B0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3260)
    WaitChrThread(0xFE, 1)
    PlayEffect(0xA, 0xFF, 0xFE, 0x40, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(400)

    def lambda_32BC():
        OP_96(0xFE, 0x1CAC, 0x0, 0x9B0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32BC)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Sound(514, 0, 100, 0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_23_3217 end

    def Function_24_32E5(): pass

    label("Function_24_32E5")

    PlayEffect(0xA, 0xFF, 0xFF, 0x0, 4570, 800, -800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)

    def lambda_332E():
        OP_96(0xFE, 0x1E1E, 0x3E8, 0xFFFFF70E, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_332E)
    WaitChrThread(0xFE, 1)
    PlayEffect(0xA, 0xFF, 0xFE, 0x40, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(400)

    def lambda_338A():
        OP_96(0xFE, 0x1E1E, 0x0, 0xFFFFF70E, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_338A)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Sound(514, 0, 100, 0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_24_32E5 end

    def Function_25_33B3(): pass

    label("Function_25_33B3")

    PlayEffect(0xA, 0xFF, 0xFF, 0x0, 4570, 800, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x0)

    def lambda_3403():
        OP_96(0xFE, 0x2094, 0x3E8, 0x62C, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3403)
    WaitChrThread(0xFE, 1)
    PlayEffect(0xA, 0xFF, 0xFE, 0x40, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(400)

    def lambda_345F():
        OP_96(0xFE, 0x2094, 0x0, 0x62C, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_345F)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Sound(514, 0, 100, 0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_25_33B3 end

    def Function_26_3488(): pass

    label("Function_26_3488")

    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x4)
    SetChrSubChip(0xD, 0x1)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x1)
    ClearChrFlags(0xD, 0x40)
    ClearChrFlags(0xD, 0x1)
    SetChrPos(0xC, 7340, 0, 2480, 225)
    SetChrPos(0xD, 7590, 0, -1830, 315)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    Return()

    # Function_26_3488 end

    def Function_27_3503(): pass

    label("Function_27_3503")

    OP_25(0x39C, 0x5A)
    Sleep(1000)
    OP_25(0x39C, 0x50)
    Sleep(1000)
    OP_25(0x39C, 0x46)
    Sleep(1000)
    OP_25(0x39C, 0x3C)
    Sleep(1000)
    OP_25(0x39C, 0x32)
    Sleep(1000)
    OP_25(0x39C, 0x28)
    Sleep(1000)
    OP_25(0x39C, 0x1E)
    Sleep(1000)
    OP_25(0x39C, 0x14)
    Sleep(1000)
    OP_25(0x39C, 0xA)
    Sleep(1000)
    OP_24(0x39C)
    Return()

    # Function_27_3503 end

    SaveToFile()

Try(main)
