from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c0360.bin",                # FileName
        "c0360",                    # MapName
        "c0360",                    # Location
        0x002D,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "c0360",                  # 0
        "伊梅尔达夫人",           # 1
        "人偶",                   # 2
        "人偶",                   # 3
        "女孩",                   # 4
    ))

    AddCharChip((
        "chr/ch09000.itc",                   # 00
        "apl/ch51445.itc",                   # 01
    ))

    DeclNpc(94540,   29,      6329,    0,    453,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(94199,   1049,    8100,    180,  453,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(95099,   1049,    8100,    180,  453,  0x0, 2,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-570,    0,       6100,    1200,    -570,    1500,    6100,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(384, 0)                                        # 0

    ScpFunction((
        "Function_0_180",          # 00, 0
        "Function_1_230",          # 01, 1
        "Function_2_2C0",          # 02, 2
        "Function_3_349",          # 03, 3
        "Function_4_3F4",          # 04, 4
        "Function_5_736",          # 05, 5
        "Function_6_2B2D",         # 06, 6
        "Function_7_2B78",         # 07, 7
        "Function_8_2BC3",         # 08, 8
        "Function_9_2C0E",         # 09, 9
        "Function_10_2C59",        # 0A, 10
        "Function_11_2CA4",        # 0B, 11
        "Function_12_2CEF",        # 0C, 12
        "Function_13_2D44",        # 0D, 13
        "Function_14_2D8F",        # 0E, 14
        "Function_15_2DDA",        # 0F, 15
        "Function_16_2E25",        # 10, 16
        "Function_17_2E70",        # 11, 17
        "Function_18_2EBB",        # 12, 18
        "Function_19_2F06",        # 13, 19
    ))


    def Function_0_180(): pass

    label("Function_0_180")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1B8"),
        (1, "loc_1C4"),
        (2, "loc_1D0"),
        (3, "loc_1DC"),
        (4, "loc_1E8"),
        (5, "loc_1F4"),
        (6, "loc_200"),
        (SWITCH_DEFAULT, "loc_20C"),
    )


    label("loc_1B8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1C4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1D0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1DC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1E8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1F4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_200")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_20C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_218")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_22F")

    Return()

    # Function_0_180 end

    def Function_1_230(): pass

    label("Function_1_230")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x176, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_253")
    Event(0, 5)

    label("loc_253")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x85, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2BF")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0xA, 0x2)
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BF")

    Return()

    # Function_1_230 end

    def Function_2_2C0(): pass

    label("Function_2_2C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_309")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F84")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    Jump("loc_2F70")

    label("loc_2F70")

    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_2F84")

    Call(0, 1)
    Return()

    # Function_2_2C0 end

    def Function_3_349(): pass

    label("Function_3_349")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着车辆杂志《导力车爱好者月刊 vol.3》。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber('深暗色彩', 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F0")
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "导力车喷漆式样\x01\x07\x02",

            "『深暗色彩』\x07\x00",
            "已经记下来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddItemNumber('深暗色彩', 1)

    label("loc_3F0")

    TalkEnd(0xFF)
    Return()

    # Function_3_349 end

    def Function_4_3F4(): pass

    label("Function_4_3F4")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x179, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DE")

    #C0003
    ChrTalk(
        0x8,
        (
            "哇哈哈，话说回来……\x01",
            "你们真是辛苦了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "托你们的福，这对姐妹人偶\x01",
            "终于找得到买家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#00101F那个……伊梅尔达夫人，\x01",
            "您不害怕吗？\x02\x03",

            "#00106F要是把这种\x01",
            "会显灵的人偶卖掉，\x01",
            "说、说不定会被诅咒的……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "哇哈哈，想做这门生意，\x01",
            "又怎能害怕鬼怪！\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "保管在这间仓库里的物品当中，\x01",
            "还有好几样灵异物品呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "要不要摸摸这枚有灵性的戒指？听说它过去\x01",
            "的几位主人接二连三地遭遇到了不幸呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5AE")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_5AE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5D7")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_5D7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_600")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)

    label("loc_600")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_626")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_626")

    Sleep(1000)

    #C0009
    ChrTalk(
        0x101,
        "#00012F不、不用了。\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        (
            "#00203F（……可能就是因为\x01",
            "  这样的东西都集中在一个地方，\x01",
            "  才产生了超自然的力场呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x104,
        "#00306F（归、归根到底，原因还是在于这个婆婆啊……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x179, 2)
    Jump("loc_732")

    label("loc_6DE")


    #C0012
    ChrTalk(
        0x8,
        (
            "托你们的福，这对姐妹人偶\x01",
            "终于找得到买家了。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "哇哈哈，这可真得\x01",
            "感谢你们呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_732")

    TalkEnd(0x8)
    Return()

    # Function_4_3F4 end

    def Function_5_736(): pass

    label("Function_5_736")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch44400.itc", 0x1E)
    OP_68(-130, 1000, -130, 0)
    MoveCamera(45, 35, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -2070, 0, -1990, 45)
    SetChrPos(0x102, -2070, 0, -1990, 45)
    SetChrPos(0x103, -2070, 0, -1990, 45)
    SetChrPos(0x104, -2070, 0, -1990, 45)
    SetChrPos(0x109, -2070, 0, -1990, 45)
    SetChrPos(0x105, -2070, 0, -1990, 45)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0x101, 3, 0, 6)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 7)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 8)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 9)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 10)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 11)
    OP_68(2840, 1000, 2910, 3000)
    OP_6F(0x1)
    StopBGM(0xFA0)
    WaitChrThread(0x105, 3)

    #C0014
    ChrTalk(
        0x101,
        (
            "#00000F打扰一下，\x01",
            "请问有人在吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    #C0015
    ChrTalk(
        0x104,
        (
            "#00305F……果然\x01",
            "没人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x102,
        (
            "#00105F但是，送货的\x01",
            "地址确实是这里啊。\x02\x03",

            "#00103F而且大门\x01",
            "也没上锁……\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 13000, 1030, 2280, 270)

    #N0017
    NpcTalk(
        0xB,
        "女孩的声音",
        "……大哥哥，你们是谁？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A6C():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A6C)
    Sleep(50)

    def lambda_A7C():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A7C)
    Sleep(50)

    def lambda_A8C():
        TurnDirection(0x109, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A8C)
    Sleep(50)

    def lambda_A9C():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A9C)
    Sleep(50)

    def lambda_AAC():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_AAC)
    Sleep(50)

    def lambda_ABC():
        TurnDirection(0x105, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_ABC)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    Sleep(300)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7562", 0)
    Fade(500)
    OP_68(10720, 1000, 3550, 0)
    MoveCamera(43, 34, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    OP_68(3490, 1000, 2870, 5000)
    OP_95(0xB, 4650, 0, 2360, 2000, 0x0)
    WaitChrThread(0xB, 1)
    OP_6F(0x1)

    #C0018
    ChrTalk(
        0x109,
        "#10105F啊……？\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x102,
        "#00105F有、有人……？\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00005F那、那个……\x01",
            "小妹妹，家里现在就你一个人吗？\x02\x03",

            "#00000F大哥哥是来\x01",
            "送货的……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xB,
        (
            "啊，难道说……\x01",
            "货已经到了！？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xB,
        "快进来快进来！\x02",
    )

    CloseMessageWindow()
    OP_95(0xB, 9850, 1030, 2520, 2000, 0x0)

    def lambda_C1B():
        OP_95(0xFE, 9500, 1050, 10700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_C1B)
    Sleep(500)

    def lambda_C38():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C38)
    Sleep(50)

    def lambda_C48():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C48)
    Sleep(500)

    def lambda_C58():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C58)
    Sleep(50)

    def lambda_C68():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C68)
    Sleep(50)

    def lambda_C78():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C78)
    Sleep(50)

    def lambda_C88():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C88)
    WaitChrThread(0x105, 1)

    #C0023
    ChrTalk(
        0x105,
        (
            "#10309F哈哈，她好像\x01",
            "没怎么听你说话呢。\x02\x03",

            "#10300F看样子，货物\x01",
            "是寄给那孩子的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        (
            "#00106F好、好奇怪啊……\x02\x03",

            "#00101F从没听说过\x01",
            "这里住着那样的孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x104,
        (
            "#00306F但我们确实见到她了……\x01",
            "这就是事实啊。\x02\x03",

            "#00301F到底是怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#00003F不知道……\x02\x03",

            "#00000F总之，\x01",
            "我们进去看看吧。\x02\x03",

            "也许能从那孩子\x01",
            "那里打听到什么呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(8870, 2000, 11100, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    OP_93(0xB, 0x10E, 0x0)
    SetChrPos(0x101, 8080, 1000, 11140, 90)
    SetChrPos(0x102, 7530, 1000, 10180, 90)
    SetChrPos(0x103, 7480, 1000, 11830, 90)
    SetChrPos(0x109, 6000, 1000, 10040, 90)
    SetChrPos(0x104, 6800, 1000, 10800, 90)
    SetChrPos(0x105, 5800, 1000, 11440, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #C0027
    ChrTalk(
        0x101,
        "#00000F那个……这就是送达的货物。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0028
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '小箱子'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交了出去。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    SubItemNumber('小箱子', 1)

    #C0029
    ChrTalk(
        0xB,
        "哇～终于回来了！\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0x87, 0x1F4)
    Sleep(300)

    #C0030
    ChrTalk(
        0xB,
        "……嘿唷。\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x3)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x2)
    SetChrPos(0xA, 10640, 1650, 10400, 270)
    Sound(802, 0, 70, 0)
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    #C0031
    ChrTalk(
        0x104,
        (
            "#00305F（……是个看起来很旧的人偶啊。）\x02\x03",

            "（这也是罗赞贝尔克制作的\x01",
            "  古董人偶吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        (
            "#00103F（不，看起来不像是\x01",
            "  那么昂贵的东西……）\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#00002F莫非这个人偶\x01",
            "是你的东西吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x10E, 0x1F4)
    Sleep(300)

    #C0034
    ChrTalk(
        0xB,
        "不是东西啦～！\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xB,
        (
            "她是我很重要很重要的妹妹。\x01",
            "呵呵，好乖好乖。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        (
            "#00106F原来是这样……\x02\x03",

            "#00109F那、那个……\x01",
            "平安送到真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xB,
        "嗯，谢谢了。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xB,
        (
            "那么，我就把这孩子\x01",
            "带到我的房间去了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x87, 0x1F4)
    Sleep(300)
    Fade(500)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x2)
    Sound(802, 0, 70, 0)
    Sleep(700)
    BeginChrThread(0xB, 3, 0, 12)

    def lambda_112C():

        label("loc_112C")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_112C")

    QueueWorkItem2(0x101, 1, lambda_112C)

    def lambda_113E():

        label("loc_113E")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_113E")

    QueueWorkItem2(0x102, 1, lambda_113E)

    def lambda_1150():

        label("loc_1150")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_1150")

    QueueWorkItem2(0x103, 1, lambda_1150)

    def lambda_1162():

        label("loc_1162")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_1162")

    QueueWorkItem2(0x104, 1, lambda_1162)

    def lambda_1174():

        label("loc_1174")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_1174")

    QueueWorkItem2(0x109, 1, lambda_1174)

    def lambda_1186():

        label("loc_1186")

        TurnDirection(0xFE, 0xB, 0)
        Yield()
        Jump("loc_1186")

    QueueWorkItem2(0x105, 1, lambda_1186)
    OP_68(2500, 2000, 15400, 5000)
    MoveCamera(45, 27, 0, 5000)
    OP_6E(440, 5000)
    SetCameraDistance(22000, 5000)
    OP_0D()
    Sleep(500)
    WaitChrThread(0xB, 3)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x0)

    def lambda_11E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_11E3)

    def lambda_11F4():
        OP_97(0xFE, 0x0, 0x0, 0x60E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_11F4)
    Sleep(500)
    SetChrFlags(0xB, 0x80)
    OP_0D()
    Sleep(500)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sound(104, 0, 100, 0)
    OP_79(0x0)
    Sleep(500)
    Fade(500)
    OP_68(6820, 2000, 11510, 0)
    MoveCamera(0, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20850, 0)
    OP_93(0x103, 0x13B, 0x0)
    OP_0D()

    #C0039
    ChrTalk(
        0x109,
        (
            "#10103F唔……\x01",
            "到底是怎么回事呢？\x02\x03",

            "#10100F家里好像也\x01",
            "没有其他人……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x103,
        "#00203F………………………………\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#00005F……？\x01",
            "缇欧，怎么了？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x103,
        (
            "#00203F……没什么，\x01",
            "多半只是错觉……\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 410, 0, 410, 45)
    OP_4B(0x8, 0xFF)

    #N0043
    NpcTalk(
        0x8,
        "老婆婆的声音",
        "#4S喂，有人在里面吗！？\x02",
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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1419():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1419)
    Sleep(50)

    def lambda_1429():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1429)
    Sleep(50)

    def lambda_1439():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1439)
    Sleep(50)

    def lambda_1449():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1449)
    Sleep(50)

    def lambda_1459():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1459)
    Sleep(50)

    def lambda_1469():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1469)
    WaitChrThread(0x105, 1)

    #C0044
    ChrTalk(
        0x101,
        "#00005F……刚、刚才的声音是……？\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x102,
        (
            "#00105F是……客人吗？\x02\x03",

            "大人好像\x01",
            "都不在，\x01",
            "我们出去迎接一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        "#00000F是、是啊……说得没错。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(670, 1000, 1090, 0)
    MoveCamera(13, 30, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19760, 0)
    SetChrPos(0x101, 9840, 1030, 1950, 270)
    SetChrPos(0x103, 10930, 1030, 1890, 270)
    SetChrPos(0x104, 12090, 1030, 1840, 270)
    SetChrPos(0x102, 9820, 1030, 3070, 270)
    SetChrPos(0x109, 10940, 1030, 3020, 270)
    SetChrPos(0x105, 12100, 1030, 2970, 270)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(2140, 1000, 1810, 5000)
    SetCameraDistance(21780, 5000)

    def lambda_15CA():
        OP_95(0xFE, 2500, 0, 1600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15CA)
    Sleep(50)

    def lambda_15E7():
        OP_95(0xFE, 2500, 0, 2800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_15E7)
    Sleep(50)

    def lambda_1604():
        OP_95(0xFE, 3700, 0, 1600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1604)
    Sleep(50)

    def lambda_1621():
        OP_95(0xFE, 3700, 0, 2800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1621)
    Sleep(50)

    def lambda_163E():
        OP_95(0xFE, 4900, 0, 1600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_163E)
    Sleep(50)

    def lambda_165B():
        OP_95(0xFE, 4900, 0, 2800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_165B)
    WaitChrThread(0x101, 1)

    def lambda_1679():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1679)
    WaitChrThread(0x102, 1)

    def lambda_168A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_168A)
    WaitChrThread(0x103, 1)

    def lambda_169B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_169B)
    WaitChrThread(0x109, 1)

    def lambda_16AC():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_16AC)
    WaitChrThread(0x104, 1)

    def lambda_16BD():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_16BD)
    WaitChrThread(0x105, 1)

    def lambda_16CE():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_16CE)
    OP_6F(0x79)

    #C0047
    ChrTalk(
        0x101,
        (
            "#00005F啊……\x01",
            "是古董店的……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "哎呀，是你们……\x01",
            "在这种地方干什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#00012F呃，这个嘛，\x01",
            "我们是因为工作关系\x01",
            "前来拜访的……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x102,
        "#00105F您到这户人家来有什么事吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0051
    ChrTalk(
        0x8,
        (
            "……工作？\x01",
            "你在说什么呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "这间房子\x01",
            "已经有十多年\x01",
            "都没有住过人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "所以我一直\x01",
            "将这里当作\x01",
            "古董仓库。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    #C0054
    ChrTalk(
        0x8,
        (
            "……怎么了？\x01",
            "你们为什么露出那种目瞪口呆的表情？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_18CE():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_18CE)
    WaitChrThread(0x102, 1)

    def lambda_18DF():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_18DF)
    WaitChrThread(0x103, 1)

    def lambda_18F0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_18F0)
    WaitChrThread(0x109, 1)

    def lambda_1901():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1901)
    WaitChrThread(0x104, 1)

    def lambda_1912():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1912)
    WaitChrThread(0x105, 1)

    def lambda_1923():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1923)

    #C0055
    ChrTalk(
        0x104,
        (
            "#00305F……到、到底是怎么回事？\x02\x03",

            "先不管这所房子\x01",
            "是否归老婆婆所有……\x02\x03",

            "#00303F我们刚才确实\x01",
            "跟一个小女孩说过话吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x105,
        "#10306F没错呢。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x109,
        (
            "#10101F……以、以防万一，\x01",
            "我们去找刚才\x01",
            "那个小女孩问问吧。\x02\x03",

            "说不定其中\x01",
            "有什么内情。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#00003F是、是啊……\x02\x03",

            "#00001F她应该是到起居室\x01",
            "里面的那个房间去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "喂喂，你们别不理睬我，\x01",
            "只顾自说自话啊。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)

    def lambda_1A8B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1A8B)
    WaitChrThread(0x102, 1)

    def lambda_1A9C():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A9C)
    WaitChrThread(0x103, 1)

    def lambda_1AAD():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1AAD)
    WaitChrThread(0x109, 1)

    def lambda_1ABE():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1ABE)
    WaitChrThread(0x104, 1)

    def lambda_1ACF():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1ACF)
    WaitChrThread(0x105, 1)

    def lambda_1AE0():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1AE0)

    #C0060
    ChrTalk(
        0x103,
        "#00205F………………………………\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0xB, 0x1)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x2)
    SetChrPos(0xB, 94200, 1050, 8100, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrSubChip(0xA, 0x2)
    SetChrFlags(0xA, 0x2)
    SetChrPos(0xA, 95100, 1050, 8100, 180)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(99920, 1250, -140, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 100100, 0, -1950, 0)
    SetChrPos(0x103, 100100, 0, -1950, 0)
    SetChrPos(0x102, 100100, 0, -1950, 0)
    SetChrPos(0x104, 100100, 0, -1950, 0)
    SetChrPos(0x109, 100100, 0, -1950, 0)
    SetChrPos(0x105, 100100, 0, -1950, 0)
    SetChrPos(0x8, 100100, 0, -1950, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 13)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 14)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 15)
    Sleep(500)
    OP_68(100100, 1250, 2940, 3000)
    BeginChrThread(0x104, 3, 0, 16)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 17)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 18)
    Sleep(500)
    BeginChrThread(0x8, 3, 0, 19)
    WaitChrThread(0x105, 3)
    OP_6F(0x1)

    #C0061
    ChrTalk(
        0x101,
        (
            "#00005F咦、咦？\x01",
            "刚才那个小女孩去哪里了……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x104,
        "#00305F躲起来了吗……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0xA, 500)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0063
    ChrTalk(
        0x102,
        (
            "#00105F罗、罗伊德……\x01",
            "看、看、看那个……！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        "#00005F咦……\x02",
    )

    CloseMessageWindow()

    def lambda_1DAB():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1DAB)
    Sleep(50)

    def lambda_1DBB():
        TurnDirection(0x105, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1DBB)
    Sleep(50)

    def lambda_1DCB():
        TurnDirection(0x103, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1DCB)
    Sleep(50)

    def lambda_1DDB():
        TurnDirection(0x104, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1DDB)
    Sleep(50)

    def lambda_1DEB():
        TurnDirection(0x109, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1DEB)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    Sleep(50)

    def lambda_1E12():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1E12)
    OP_68(94650, 1250, 8100, 5000)
    MoveCamera(45, 24, 0, 5000)
    OP_6E(440, 5000)
    SetCameraDistance(19000, 5000)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(97220, 1250, 4330, 0)
    MoveCamera(24, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    OP_0D()

    #C0065
    ChrTalk(
        0x101,
        (
            "#00005F那对人偶……\x01",
            "其中一个是\x01",
            "我们送来的……\x02\x03",

            "#00011F另、另一个……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x105,
        "#10301F跟刚才那个小女孩一模一样呢。\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(100210, 1250, 1840, 0)
    MoveCamera(45, 24, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    OP_93(0x8, 0x0, 0x0)
    OP_0D()

    #C0067
    ChrTalk(
        0x8,
        (
            "……你们几个，\x01",
            "也该给我\x01",
            "解释一下了。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "视情节轻重，\x01",
            "我完全可以控告你们非法入侵哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F90():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1F90)
    Sleep(50)

    def lambda_1FA0():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1FA0)
    Sleep(50)

    def lambda_1FB0():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1FB0)
    Sleep(50)

    def lambda_1FC0():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1FC0)
    Sleep(50)

    def lambda_1FD0():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1FD0)
    Sleep(50)

    def lambda_1FE0():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1FE0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)

    #C0069
    ChrTalk(
        0x101,
        (
            "#00006F我、我明白了。\x01",
            "那个，其实是这样……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0070
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将自己为了送货而来此，\x01",
            "以及出来迎接的少女与其中\x01",
            "一个人偶一模一样等情况做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0071
    ChrTalk(
        0x8,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "……哈哈哈，原来如此。\x01",
            "也就是说，那家伙\x01",
            "说的话真的应验了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    Sleep(1000)

    #C0073
    ChrTalk(
        0x109,
        "#10105F那、那个……请问，这是怎么回事？\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "那边的两个人偶，\x01",
            "其中一个是我以前\x01",
            "在外国买到的。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        (
            "听说是仿照着某个名门世家的\x01",
            "女儿们制作的，\x01",
            "是具有灵性的东西哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "由于那是一对双胞胎女孩，\x01",
            "所以制作的是两个一对的人偶，\x01",
            "但我只得到了其中一个。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "这人偶很奇怪，\x01",
            "虽然品质不错，但不知为何，\x01",
            "却总是找不到买家。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#00005F……那个，您说的这些\x01",
            "和这件事到底有什么关系……？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x8,
        "哎呀呀，你真是意外地迟钝啊。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "简单来说，\x01",
            "人偶被送到这个地方，\x01",
            "以及那名神秘少女的出现……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "也许都是因为\x01",
            "人偶拥有了生命\x01",
            "而导致的事情呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    #C0082
    ChrTalk(
        0x101,
        "#00011F#4S……啊！？\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "自古以来，一直有人\x01",
            "宣称『人偶是有生命的』。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "哈哈哈，如此看来，\x01",
            "说不定确实如此呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_255F")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0085
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "是否完成了前作的人偶工房任务？（测试用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【不做变更】\x01",      # 0
            "【已完成】\x01",        # 1
            "【未完成】\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_254B")
    OP_29(0x30, 0x4, 0x10)
    Jump("loc_255F")

    label("loc_254B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_255F")
    OP_29(0x30, 0x3, 0x10)

    label("loc_255F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_25BA")

    #C0086
    ChrTalk(
        0x101,
        (
            "#00005F有生命……\x02\x03",

            "#00003F我、我记得\x01",
            "约鲁古老人以前\x01",
            "就说过类似的话。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25F5")

    label("loc_25BA")


    #C0087
    ChrTalk(
        0x101,
        (
            "#00005F有生命……\x02\x03",

            "#00006F我觉得这终究\x01",
            "还是不大可能。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25F5")


    #C0088
    ChrTalk(
        0x102,
        (
            "#00105F那、那就是说……\x01",
            "出现了人偶的\x01",
            "幽灵吗？！\x02\x03",

            "#00106F这、这……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2642():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2642)
    Sleep(300)

    #C0089
    ChrTalk(
        0x103,
        (
            "#00203F算啦，真假暂且不论……\x02\x03",

            "#00200F总之，这间住宅内\x01",
            "似乎形成了一种\x01",
            "超自然的『力场』。\x02\x03",

            "和以前的『塔』及『僧院』一样，\x01",
            "可以感觉到上级三属性的气息……\x02\x03",

            "也许就是这些因素\x01",
            "引起了某种超自然现象。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2718():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2718)
    Sleep(50)

    def lambda_2728():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2728)
    Sleep(50)

    def lambda_2738():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2738)
    Sleep(50)

    def lambda_2748():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2748)
    Sleep(50)

    def lambda_2758():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2758)
    WaitChrThread(0x105, 1)

    #C0090
    ChrTalk(
        0x102,
        "#00105F超、超自然……\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x105,
        (
            "#10302F就是因为这个原因，\x01",
            "才会让人觉得有些异样吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x104,
        (
            "#00301F虽然我觉得\x01",
            "这种事情很难让人相信……\x02\x03",

            "#00306F但听阿缇这么一说，\x01",
            "就觉得也不是没可能。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x109,
        (
            "#10112F但、但还是\x01",
            "很难相信呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        (
            "哈哈哈……！\x01",
            "你们的反应\x01",
            "很不错嘛。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_286A():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_286A)
    Sleep(50)

    def lambda_287A():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_287A)
    Sleep(50)

    def lambda_288A():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_288A)
    Sleep(50)

    def lambda_289A():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_289A)
    Sleep(50)

    def lambda_28AA():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_28AA)
    Sleep(50)

    def lambda_28BA():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_28BA)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)

    #C0095
    ChrTalk(
        0x8,
        (
            "再怎么说，那也只是隐世者的玩笑话，\x01",
            "至于信或不信，\x01",
            "都是你们的自由……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        "不过，至少有一件事可以确定。\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        "#00005F那、那是……？\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        (
            "这对姐妹人偶总算凑齐了，\x01",
            "终于有希望\x01",
            "找到买家了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "哈哈哈……\x01",
            "这还真是\x01",
            "捡了个大便宜呢。\x02",
        )
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
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0100
    ChrTalk(
        0x104,
        "#00306F这位老婆婆还真是直截了当啊……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x101,
        (
            "#00006F好、好了，不管怎么说……\x01",
            "总算把货物送到了。\x02\x03",

            "#00000F我们这就去向\x01",
            "卡普亚特急便的人报告吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x102,
        (
            "#00106F是、是啊，\x01",
            "我们快走吧……！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 2)
    NewScene("t3510", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_5_736 end

    def Function_6_2B2D(): pass

    label("Function_6_2B2D")


    def lambda_2B32():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2B32)

    def lambda_2B43():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B43)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 3150, 0, 3230, 2000, 0x0)
    OP_93(0x101, 0x2D, 0x1F4)
    Return()

    # Function_6_2B2D end

    def Function_7_2B78(): pass

    label("Function_7_2B78")


    def lambda_2B7D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2B7D)

    def lambda_2B8E():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2B8E)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 3000, 0, 2100, 2000, 0x0)
    OP_93(0x102, 0x2D, 0x1F4)
    Return()

    # Function_7_2B78 end

    def Function_8_2BC3(): pass

    label("Function_8_2BC3")


    def lambda_2BC8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2BC8)

    def lambda_2BD9():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2BD9)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 2140, 0, 3620, 2000, 0x0)
    OP_93(0x103, 0x2D, 0x1F4)
    Return()

    # Function_8_2BC3 end

    def Function_9_2C0E(): pass

    label("Function_9_2C0E")


    def lambda_2C13():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2C13)

    def lambda_2C24():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2C24)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 1840, 0, 2420, 2000, 0x0)
    OP_93(0x104, 0x2D, 0x1F4)
    Return()

    # Function_9_2C0E end

    def Function_10_2C59(): pass

    label("Function_10_2C59")


    def lambda_2C5E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2C5E)

    def lambda_2C6F():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2C6F)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 900, 30, 2330, 2000, 0x0)
    OP_93(0x109, 0x2D, 0x1F4)
    Return()

    # Function_10_2C59 end

    def Function_11_2CA4(): pass

    label("Function_11_2CA4")


    def lambda_2CA9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2CA9)

    def lambda_2CBA():
        OP_95(0xFE, 430, 30, 540, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2CBA)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 1900, 30, 1240, 2000, 0x0)
    OP_93(0x105, 0x2D, 0x1F4)
    Return()

    # Function_11_2CA4 end

    def Function_12_2CEF(): pass

    label("Function_12_2CEF")

    OP_97(0xB, 0x0, 0x0, 0xBB8, 0x7D0, 0x0)
    OP_97(0xB, 0xFFFFE34A, 0x0, 0x0, 0x7D0, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    OP_97(0xB, 0x0, 0x0, 0x60E, 0x7D0, 0x0)
    Return()

    # Function_12_2CEF end

    def Function_13_2D44(): pass

    label("Function_13_2D44")


    def lambda_2D49():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D49)

    def lambda_2D5A():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D5A)
    WaitChrThread(0x101, 1)
    OP_95(0x101, 100000, 30, 4000, 2000, 0x0)
    OP_93(0x101, 0x0, 0x1F4)
    Return()

    # Function_13_2D44 end

    def Function_14_2D8F(): pass

    label("Function_14_2D8F")


    def lambda_2D94():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2D94)

    def lambda_2DA5():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2DA5)
    WaitChrThread(0x102, 1)
    OP_95(0x102, 98890, 30, 3530, 2000, 0x0)
    OP_93(0x102, 0x0, 0x1F4)
    Return()

    # Function_14_2D8F end

    def Function_15_2DDA(): pass

    label("Function_15_2DDA")


    def lambda_2DDF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2DDF)

    def lambda_2DF0():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2DF0)
    WaitChrThread(0x103, 1)
    OP_95(0x103, 101030, 30, 3100, 2000, 0x0)
    OP_93(0x103, 0x0, 0x1F4)
    Return()

    # Function_15_2DDA end

    def Function_16_2E25(): pass

    label("Function_16_2E25")


    def lambda_2E2A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2E2A)

    def lambda_2E3B():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2E3B)
    WaitChrThread(0x104, 1)
    OP_95(0x104, 99700, 30, 2800, 2000, 0x0)
    OP_93(0x104, 0x0, 0x1F4)
    Return()

    # Function_16_2E25 end

    def Function_17_2E70(): pass

    label("Function_17_2E70")


    def lambda_2E75():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2E75)

    def lambda_2E86():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2E86)
    WaitChrThread(0x109, 1)
    OP_95(0x109, 99500, 0, 1800, 2000, 0x0)
    OP_93(0x109, 0x0, 0x1F4)
    Return()

    # Function_17_2E70 end

    def Function_18_2EBB(): pass

    label("Function_18_2EBB")


    def lambda_2EC0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2EC0)

    def lambda_2ED1():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2ED1)
    WaitChrThread(0x105, 1)
    OP_95(0x105, 100860, 0, 1800, 2000, 0x0)
    OP_93(0x105, 0x0, 0x1F4)
    Return()

    # Function_18_2EBB end

    def Function_19_2F06(): pass

    label("Function_19_2F06")


    def lambda_2F0B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_2F0B)

    def lambda_2F1C():
        OP_95(0xFE, 100000, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2F1C)
    WaitChrThread(0x8, 1)
    OP_95(0x8, 100000, 0, 500, 2000, 0x0)
    Return()

    # Function_19_2F06 end

    SaveToFile()

Try(main)
