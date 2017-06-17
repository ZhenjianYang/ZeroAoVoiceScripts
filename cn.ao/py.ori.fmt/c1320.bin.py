from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1320.bin",                # FileName
        "c1320",                    # MapName
        "c1320",                    # Location
        0x001F,                     # MapIndex
        "ed7522",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 31, 0, 1, 0, 3],
    )

    BuildStringList((
        "c1320",                  # 0
        "研究员库雷",             # 1
        "研究员达比德",           # 2
        "人偶",                   # 3
    ))

    AddCharChip((
        "chr/ch32800.itc",                   # 00
        "chr/ch29402.itc",                   # 01
    ))

    DeclNpc(-3099,   -479,    22659,   315,  257,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-4699,   -379,    22700,   315,  325,  0x0, 0,   1,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(0,       -280,    16660,   1100,    0,       -130,    16660,   0x007C, 0,  7,  0x0000)

    ChipFrameInfo(324, 0)                                        # 0

    ScpFunction((
        "Function_0_144",          # 00, 0
        "Function_1_1F4",          # 01, 1
        "Function_2_236",          # 02, 2
        "Function_3_23D",          # 03, 3
        "Function_4_2BA",          # 04, 4
        "Function_5_3D4",          # 05, 5
        "Function_6_4EC",          # 06, 6
        "Function_7_7E9",          # 07, 7
        "Function_8_1A57",         # 08, 8
        "Function_9_1AA2",         # 09, 9
        "Function_10_1B18",        # 0A, 10
        "Function_11_1B63",        # 0B, 11
    ))


    def Function_0_144(): pass

    label("Function_0_144")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_17C"),
        (1, "loc_188"),
        (2, "loc_194"),
        (3, "loc_1A0"),
        (4, "loc_1AC"),
        (5, "loc_1B8"),
        (6, "loc_1C4"),
        (SWITCH_DEFAULT, "loc_1D0"),
    )


    label("loc_17C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_188")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_194")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1A0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1AC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1B8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1F3")

    Return()

    # Function_0_144 end

    def Function_1_1F4(): pass

    label("Function_1_1F4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_215")
    ClearScenarioFlags(0x25, 1)
    Call(0, 2)

    label("loc_215")

    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_235")
    SetChrFlags(0x8, 0x10)

    label("loc_235")

    Return()

    # Function_1_1F4 end

    def Function_2_236(): pass

    label("Function_2_236")

    Sound(160, 0, 100, 0)
    Return()

    # Function_2_236 end

    def Function_3_23D(): pass

    label("Function_3_23D")

    SetMapObjFrame(0xFF, "monita2_add", 0x2, "nomal")
    SetMapObjFrame(0xFF, "monita3_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita4_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "monita5_add", 0x0, 0x1)
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B9")
    OP_66(0x0, 0x1)
    ClearMapObjFlags(0x5, 0x4)

    label("loc_2B9")

    Return()

    # Function_3_23D end

    def Function_4_2BA(): pass

    label("Function_4_2BA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CF")
    Call(0, 6)
    Jump("loc_3D0")

    label("loc_2CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_376")

    #C0001
    ChrTalk(
        0xFE,
        (
            "顺便一说，罗伯兹主任\x01",
            "正在爱普斯泰恩财团\x01",
            "所在的楼层努力工作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "好像是在寻找\x01",
            "盗取兰花塔\x01",
            "构造图的黑客……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "黑客为什么要\x01",
            "盗走那种东西呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3D0")

    label("loc_376")


    #C0004
    ChrTalk(
        0xFE,
        (
            "罗伯兹主任好像正在寻找\x01",
            "盗取兰花塔构造图的黑客……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "黑客为什么要\x01",
            "盗走那种东西呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D0")

    TalkEnd(0xFE)
    Return()

    # Function_4_2BA end

    def Function_5_3D4(): pass

    label("Function_5_3D4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E9")
    Call(0, 6)
    Jump("loc_4E8")

    label("loc_3E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A9")

    #C0006
    ChrTalk(
        0xFE,
        (
            "玛丽亚贝尔小姐\x01",
            "非常能使唤人……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "但她既然把系统管理这份\x01",
            "责任重大的工作交给了我，\x01",
            "我就必须要努力完成。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "你们是来寻找\x01",
            "大小姐那些\x01",
            "失窃人偶的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "请加油\x01",
            "找哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4E8")

    label("loc_4A9")


    #C0010
    ChrTalk(
        0xFE,
        (
            "你们是来寻找\x01",
            "大小姐那些\x01",
            "失窃人偶的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "请加油\x01",
            "找哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E8")

    TalkEnd(0xFE)
    Return()

    # Function_5_3D4 end

    def Function_6_4EC(): pass

    label("Function_6_4EC")

    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x0, 500)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_588")
    Jump("loc_5D2")

    label("loc_588")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5A8")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5D2")

    label("loc_5A8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5C8")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5D2")

    label("loc_5C8")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5D2")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)

    #C0012
    ChrTalk(
        0x8,
        "哎，你们是……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x9,
        (
            "你们好像是\x01",
            "特别任务支援科的成员吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        (
            "哈哈，好久不见啦，\x01",
            "还记得我们吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x103,
        (
            "#00200F是ＩＢＣ技术部的\x01",
            "库雷先生和达比德先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#00000F好久不见。\x01",
            "……你们好像很忙吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "嗯，自从导力网络开始普及之后，\x01",
            "系统管理工作比以前\x01",
            "更加繁忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "总之，我一定会努力完成任务的。\x01",
            "毕竟大小姐很重视这方面的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x102,
        (
            "#00109F呵呵，在贝尔手下工作\x01",
            "应该很辛苦吧……\x01",
            "请加油吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x9,
        "嗯，谢谢。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x9,
        (
            "你们是来寻找大小姐那些\x01",
            "失窃人偶的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x9,
        "请加油找哦。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0x13B, 0x1F4)
    OP_4C(0x8, 0xFF)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x1C6, 2)
    Return()

    # Function_6_4EC end

    def Function_7_7E9(): pass

    label("Function_7_7E9")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-820, 900, 14940, 0)
    MoveCamera(32, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13870, 0)
    SetChrPos(0x101, 40, -510, 15350, 0)
    SetChrPos(0x102, -1100, -590, 14550, 0)
    SetChrPos(0x103, -70, -590, 13800, 0)
    SetChrPos(0x104, 1090, -590, 14550, 0)
    SetChrPos(0x109, -1030, -590, 13110, 0)
    SetChrPos(0x105, 970, -590, 13140, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    LoadChrToIndex("apl/ch51099.itc", 0x1E)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0xB)
    SetChrPos(0xA, 0, -130, 16660, 0)
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x20)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x8, 0xFF)
    LoadChrToIndex("chr/ch29400.itc", 0x1F)
    FadeToBright(500, 0)
    OP_0D()

    #C0023
    ChrTalk(
        0x101,
        "#12P#00000F找到了……最后的箱子！\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x103,
        (
            "#12P#00203F『前往高耸入云的摩天大楼，\x01",
            "　由十六层之顶下行二十一层，\x01",
            "　寻找众多窥视异界的窗口』……\x02\x03",

            "#00200FＩＢＣ大楼共有十六层，\x01",
            "从最顶层下行二十一层，就是地下五层。\x01",
            "……也就是这里了。\x02\x03",

            "#00200F而『众多窥视异界的窗口』\x01",
            "就是指这些可以\x01",
            "监测导力网络的显示屏。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x104,
        (
            "#12P#00300F听你这样一说，除了这里之外，\x01",
            "还真是没有其它可能了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        "#12P#00000F好，那我们就赶快确认一下吧。\x02",
    )

    CloseMessageWindow()
    Sound(1024, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x1, 0x14, 0x1, 0x8)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_79(0x5)
    Sleep(1000)

    #C0027
    ChrTalk(
        0x102,
        (
            "#6P#00100F这个人偶是『爱丽丝』……\x01",
            "在贝尔的众多收藏品之中，\x01",
            "好像是她最喜欢的一个。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#12P#00005F因为这已经是最后一个了，\x01",
            "所以并没有贴怪盗Ｂ的卡片呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x105,
        "#12P#10300F呵呵，也就是说，我们完成委托了吧？\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x109,
        "#6P#10106F呼，真是个漫长的任务啊……\x02",
    )

    CloseMessageWindow()
    Sound(1026, 0, 100, 0)
    Sleep(1000)
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
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0031
    ChrTalk(
        0x101,
        "#12P#00005F哎……？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        "#12P#00301F怎、怎么了？\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 1, 0, 8)
    BeginChrThread(0x9, 1, 0, 9)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)

    #C0033
    ChrTalk(
        0x8,
        "#6P你们几个，发生什么事了吗？\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x9,
        (
            "#6P我好像听见收到导力邮件\x01",
            "的提示音了……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        (
            "#6P哎？那不是玛丽亚贝尔\x01",
            "大小姐的人偶吗！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D4D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D4D)
    Sleep(50)

    def lambda_D5D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D5D)
    Sleep(50)

    def lambda_D6D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D6D)
    Sleep(50)

    def lambda_D7D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D7D)
    Sleep(50)

    def lambda_D8D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D8D)
    Sleep(50)

    def lambda_D9D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D9D)
    Sleep(100)

    #C0036
    ChrTalk(
        0x101,
        (
            "#11P#00005F嗯，应该已经在这里\x01",
            "放上一段时间了……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x103,
        (
            "#12P#00203F唔……说起来，\x01",
            "偏偏在这种时候收到邮件，\x01",
            "实在是令人在意呢。\x02\x03",

            "#00200F我可以查看邮件内容吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x103, 500)

    #C0038
    ChrTalk(
        0x8,
        (
            "#6P啊，嗯……\x01",
            "总觉得有些诡异，就拜托你了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(50, 720, 17660, 0)
    MoveCamera(33, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13720, 0)
    SetChrPos(0x101, -1060, -280, 17870, 0)
    SetChrPos(0x102, 1060, -280, 17990, 0)
    SetChrPos(0x104, -540, -280, 16850, 0)
    SetChrPos(0x109, 630, -280, 17010, 0)
    SetChrPos(0x105, -50, -280, 16120, 0)
    SetChrPos(0x8, -920, -600, 14160, 0)
    SetChrPos(0x9, 750, -600, 14180, 0)
    SetChrFlags(0xA, 0x80)
    SetMapObjFlags(0x5, 0x4)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    EndChrThread(0x103, 0x0)
    SetChrBattleFlags(0x103, 0x4)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x103, -40, -130, 18520, 0)
    Sleep(1500)
    FadeToBright(500, 0)
    OP_0D()
    OP_63(0x103, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)
    Sound(836, 0, 100, 0)

    #C0039
    ChrTalk(
        0x103,
        (
            "#11P#00203F（敲击键盘……）\x02\x03",

            "#00205F……哎……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#6P#00005F怎么了？缇欧。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x103,
        (
            "#11P#00201F……发件人的名字……\x01",
            "是『怪盗Ｂ』……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0042
    ChrTalk(
        0x102,
        "#00105F什么！？\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        "怪、怪盗Ｂ……！？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        "他、他究竟是从何处……\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#6P#00001F……缇欧，\x01",
            "打开看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x103,
        "#11P#00201F……明白了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, 100)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0047
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "发件人：怪盗Ｂ\x01",
            "邮件名：无题\x02",
        )
    )

    CloseMessageWindow()

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "致各位亲爱的特别任务支援科成员──\x01\x01",
            "首先，请容我\x01",
            "衷心感谢大家\x01",
            "陪我完成了此次的余兴节目。\x02",
        )
    )

    CloseMessageWindow()

    #A0049
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本人对人偶的所有者玛丽亚贝尔女士，\x01",
            "以及人偶的制作者约鲁古大师多有冒犯，\x01",
            "在此致以诚挚歉意。\x01\x01",
            "但本人已尽最大努力保管，并没有\x01",
            "让这些顶级艺术品受到丝毫损伤，\x01",
            "因此还请各位安心。\x02",
        )
    )

    CloseMessageWindow()

    #A0050
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "不久之后，\x01",
            "本人就将离开此地。\x01",
            "再会了，特别任务支援科的诸位。\x02",
        )
    )

    CloseMessageWindow()

    #A0051
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『噬身之蛇』执行者Ｎｏ．Ⅹ──\x01",
            "『怪盗绅士』布卢布兰在此向女神祈祷。\x01",
            "　\x01",
            "祝愿大家一切顺利，\x01",
            "并期待各位今后继续成长。\x02",
        )
    )

    CloseMessageWindow()

    #A0052
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ＰＳ：\x01",
            "此封导力邮件将会自动删除，\x01",
            "且无法保存，请不必徒劳尝试。\x01",
            "  　　　　　　　　　　　　　──怪盗Ｂ\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(500, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0x8)
    OP_64(0x9)

    #C0053
    ChrTalk(
        0x101,
        "#6P#00005F……这……这………………\x02",
    )

    CloseMessageWindow()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0054
    ChrTalk(
        0x101,
        "#6P#00011F#4S……这封邮件到底是怎么回事！？\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x105,
        (
            "#12P#10302F呵呵，没想到突然\x01",
            "接到了这种自白书啊。\x02\x03",

            "#10304F『噬身之蛇』的执行者\x01",
            "『怪盗绅士』吗……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_15FD")

    #C0056
    ChrTalk(
        0x102,
        (
            "#00106F说、说起来，\x01",
            "他上次就曾暗示过\x01",
            "自己与小玲存在一些关系……\x02\x03",

            "#00107F对、对了，缇欧！\x01",
            "可以把这封邮件保存出来吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1682")

    label("loc_15FD")


    #C0057
    ChrTalk(
        0x102,
        (
            "#00106F如、如果是这样的话，\x01",
            "也就可以解释怪盗Ｂ的\x01",
            "盗窃手段为何如此高超了……\x02\x03",

            "#00107F对、对了，缇欧！\x01",
            "可以把这封邮件保存出来吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1682")


    #C0058
    ChrTalk(
        0x101,
        (
            "#6P#00005F对、对啊！\x01",
            "也许可以从中发现一些重要线索……！\x02",
        )
    )

    CloseMessageWindow()
    Sound(836, 0, 100, 0)

    #C0059
    ChrTalk(
        0x103,
        (
            "#11P#00203F（快速敲击键盘……）\x01",
            "已经尝试过了……不行。\x02\x03",

            "#00200F在打开邮件的同时，\x01",
            "数据似乎就已经开始\x01",
            "慢慢删除了。\x02\x03",

            "#00206F虽然对其它资料并无影响，\x01",
            "但恢复数据几乎是不可能的。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        (
            "#6P#00306F哎呀呀，准备得真是周到啊。\x02\x03",

            "#00301F昨天在地下空间\x01",
            "布置陷阱的那个混蛋也是一样，\x01",
            "到最后我们也还是对他一无所知。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x109,
        (
            "#12P#10103F是啊……\x02\x03",

            "#10101F从他们的黑客手段来看，\x01",
            "必定拥有相当\x01",
            "惊人的技术力。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        "我、我们到现在还没搞明白……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "……对了！库雷！\x01",
            "赶快去确认我们的数据\x01",
            "有没有受到影响！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "说、说的对。\x01",
            "说不定那封邮件含有病毒。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "事情就是这样，\x01",
            "我们就先失陪了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    BeginChrThread(0x8, 1, 0, 10)
    BeginChrThread(0x9, 1, 0, 11)
    Sleep(1200)
    OP_93(0x101, 0xB4, 0x1F4)

    #C0066
    ChrTalk(
        0x101,
        (
            "#6P#00003F不、不管怎么说……\x01",
            "我们总算把所有\x01",
            "罗赞贝尔克人偶都找回来了。\x02\x03",

            "#00000F现在就给玛丽亚贝尔小姐\x01",
            "送过去吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x1)

    def lambda_19B0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_19B0)
    Sleep(50)

    def lambda_19C0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_19C0)
    Sleep(50)

    def lambda_19D0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_19D0)
    Sleep(50)

    def lambda_19E0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_19E0)
    Sleep(100)

    #C0067
    ChrTalk(
        0x102,
        "#00100F嗯……我们走吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    ClearChrBattleFlags(0x103, 0x4)
    ClearChrFlags(0x103, 0x4)
    SetChrFlags(0x103, 0x8000)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    OP_64(0x8)
    OP_64(0x9)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x22, 1)
    NewScene("c1340", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_7E9 end

    def Function_8_1A57(): pass

    label("Function_8_1A57")

    OP_93(0xFE, 0xBE, 0x1F4)
    OP_95(0xFE, -3750, -600, 19550, 2000, 0x0)
    OP_95(0xFE, -3600, -600, 15950, 2000, 0x0)
    OP_95(0xFE, -2560, -600, 14690, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_8_1A57 end

    def Function_9_1AA2(): pass

    label("Function_9_1AA2")

    Sleep(1000)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x4)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0xFE, -4560, -480, 21280, 135)
    OP_0D()
    OP_95(0xFE, -3750, -600, 19550, 2000, 0x0)
    OP_95(0xFE, -3600, -600, 15950, 2000, 0x0)
    OP_95(0xFE, -3430, -600, 15650, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_9_1AA2 end

    def Function_10_1B18(): pass

    label("Function_10_1B18")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, -3720, -600, 15980, 2000, 0x0)
    OP_95(0xFE, -3470, -600, 20320, 2000, 0x0)
    OP_95(0xFE, -5210, -480, 21950, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_10_1B18 end

    def Function_11_1B63(): pass

    label("Function_11_1B63")

    OP_93(0xFE, 0x2D, 0x1F4)
    OP_95(0xFE, 3720, -600, 15950, 2000, 0x0)
    OP_95(0xFE, 3610, -600, 20460, 2000, 0x0)
    OP_95(0xFE, 5110, -480, 21860, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_11_1B63 end

    SaveToFile()

Try(main)
