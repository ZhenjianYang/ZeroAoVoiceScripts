from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1520.bin",                # FileName
        "t1520",                    # MapName
        "t1520",                    # Location
        0x004E,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1D,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 78, 0, 5, 0, 6],
    )

    BuildStringList((
        "t1520",                  # 0
        "玛罗奈",                 # 1
        "阿修拉主任",             # 2
        "诊断医生贝尔达因",       # 3
        "梅菲尔护士",             # 4
        "塞茜尔",                 # 5
    ))

    AddCharChip((
        "chr/ch25600.itc",                   # 00
        "apl/ch50146.itc",                   # 01
        "chr/ch29300.itc",                   # 02
        "chr/ch29800.itc",                   # 03
        "chr/ch05300.itc",                   # 04
    ))

    DeclNpc(-5199,   0,       17700,   90,   261,  0x0, 0,   0,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(92529,   400,     49430,   315,  469,  0x0, 0,   1,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(-98839,  0,       53500,   180,  389,  0x0, 0,   2,   0,   0,   3,   0,   12,  255,  0)
    DeclNpc(204669,  0,       53000,   90,   389,  0x0, 0,   3,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(154500,  0,       53400,   90,   389,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)

    DeclActor(95330,   0,       56250,   1200,    95330,   550,     56250,   0x007C, 0,  7,  0x0000)

    ChipFrameInfo(400, 0)                                        # 0

    ScpFunction((
        "Function_0_190",          # 00, 0
        "Function_1_240",          # 01, 1
        "Function_2_2A1",          # 02, 2
        "Function_3_302",          # 03, 3
        "Function_4_32D",          # 04, 4
        "Function_5_340",          # 05, 5
        "Function_6_49E",          # 06, 6
        "Function_7_4ED",          # 07, 7
        "Function_8_598",          # 08, 8
        "Function_9_656",          # 09, 9
        "Function_10_104F",        # 0A, 10
        "Function_11_19F6",        # 0B, 11
        "Function_12_1AC3",        # 0C, 12
        "Function_13_1BAC",        # 0D, 13
    ))


    def Function_0_190(): pass

    label("Function_0_190")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_1C8"),
        (1, "loc_1D4"),
        (2, "loc_1E0"),
        (3, "loc_1EC"),
        (4, "loc_1F8"),
        (5, "loc_204"),
        (6, "loc_210"),
        (SWITCH_DEFAULT, "loc_21C"),
    )


    label("loc_1C8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_1D4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_1E0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_1EC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_1F8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_204")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_210")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_21C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_228")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_23F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_228")

    label("loc_23F")

    Return()

    # Function_0_190 end

    def Function_1_240(): pass

    label("Function_1_240")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A0")
    OP_95(0xFE, -310, 0, 17700, 2000, 0x0)
    OP_95(0xFE, -310, 0, 3650, 2000, 0x0)
    OP_95(0xFE, -310, 0, 17700, 2000, 0x0)
    OP_95(0xFE, -14660, 0, 17700, 2000, 0x0)
    Jump("Function_1_240")

    label("loc_2A0")

    Return()

    # Function_1_240 end

    def Function_2_2A1(): pass

    label("Function_2_2A1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_301")
    OP_95(0xFE, 79630, 0, 11390, 2000, 0x0)
    OP_95(0xFE, 98920, 0, 11390, 2000, 0x0)
    OP_95(0xFE, 98920, 0, 2680, 2000, 0x0)
    OP_95(0xFE, 98920, 0, 11390, 2000, 0x0)
    Jump("Function_2_2A1")

    label("loc_301")

    Return()

    # Function_2_2A1 end

    def Function_3_302(): pass

    label("Function_3_302")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_32C")
    OP_94(0xFE, 0xFFFE741A, 0xCD5A, 0xFFFE86D0, 0xD548, 0x3E8)
    Sleep(400)
    Jump("Function_3_302")

    label("loc_32C")

    Return()

    # Function_3_302 end

    def Function_4_32D(): pass

    label("Function_4_32D")

    OP_63(0xFE, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    Return()

    # Function_4_32D end

    def Function_5_340(): pass

    label("Function_5_340")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_354")
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_49D")

    label("loc_354")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_379")
    SetChrPos(0x8, 98920, 0, 10770, 270)
    BeginChrThread(0x8, 0, 0, 2)
    Jump("loc_49D")

    label("loc_379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_38D")
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_49D")

    label("loc_38D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3B7")
    SetChrPos(0x8, 98920, 0, 10770, 270)
    BeginChrThread(0x8, 0, 0, 2)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_49D")

    label("loc_3B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3DC")
    SetChrPos(0x8, 98920, 0, 10770, 270)
    BeginChrThread(0x8, 0, 0, 2)
    Jump("loc_49D")

    label("loc_3DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3F0")
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_49D")

    label("loc_3F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_415")
    SetChrPos(0x8, 98920, 0, 10770, 270)
    BeginChrThread(0x8, 0, 0, 2)
    Jump("loc_49D")

    label("loc_415")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_429")
    BeginChrThread(0x8, 0, 0, 1)
    Jump("loc_49D")

    label("loc_429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_442")
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_49D")

    label("loc_442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_47D")
    SetChrPos(0x8, 98920, 0, 10770, 270)
    BeginChrThread(0x8, 0, 0, 2)
    ClearChrFlags(0x9, 0x80)
    BeginChrThread(0x9, 0, 0, 4)
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_49D")

    label("loc_47D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_49D")
    BeginChrThread(0x8, 0, 0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_49D")
    ClearChrFlags(0xC, 0x80)

    label("loc_49D")

    Return()

    # Function_5_340 end

    def Function_6_49E(): pass

    label("Function_6_49E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_4B0")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EC")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_4EC")

    Return()

    # Function_6_49E end

    def Function_7_4ED(): pass

    label("Function_7_4ED")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着《克洛斯贝尔乡土料理入门》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2, 0x0)"), scpexpr(EXPR_END)), "loc_594")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_594")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『久煮炖菜』\x07\x00",
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_594")

    TalkEnd(0xFF)
    Return()

    # Function_7_4ED end

    def Function_8_598(): pass

    label("Function_8_598")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5AD")
    Call(0, 9)
    Jump("loc_652")

    label("loc_5AD")


    #C0003
    ChrTalk(
        0xC,
        (
            "#01303F如果能得知盖伊那起事件的真相，\x01",
            "我或许就可以向前迈出新的一步了……\x02\x03",

            "#01300F不过，大家一定不要太过逞强哦。\x01",
            "你们全都平安无事地生活，\x01",
            "就是我如今最大的心愿。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_652")

    TalkEnd(0xFE)
    Return()

    # Function_8_598 end

    def Function_9_656(): pass

    label("Function_9_656")

    EventBegin(0x0)
    Fade(500)
    OP_68(153430, 700, 53830, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20790, 0)
    SetChrPos(0x101, 153010, 0, 53370, 90)
    SetChrPos(0x102, 152340, 0, 54310, 90)
    SetChrPos(0x104, 151800, 0, 52830, 90)
    SetChrPos(0x109, 151060, 0, 54090, 90)
    SetChrPos(0x105, 150790, 0, 53090, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis000.itp")
    OP_4B(0xC, 0xFF)
    OP_93(0xC, 0x10E, 0x0)
    OP_0D()

    #C0004
    ChrTalk(
        0xC,
        (
            "#11P#01300F……啊，罗伊德，是你们啊。\x02\x03",

            "已经把赛兰德教授\x01",
            "交付的工作完成了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        "#6P#00000F嗯，刚刚完成。\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x104,
        "#6P#00300F塞茜尔小姐，你在休息吗？\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xC,
        (
            "#11P#01302F呵呵，我今天要值夜班，\x01",
            "所以先回来准备一下。\x02\x03",

            "#01304F我想带一些平时\x01",
            "喜欢喝的红茶，\x01",
            "晚上可以用来提神。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        "#00105F还是和以前一样忙啊……\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        "#6P#00001F一定要注意身体哦。\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xC,
        (
            "#11P#01309F呵呵，不用担心，\x01",
            "我可是很强韧的。\x02\x03",

            "#01304F……这或许也是因为\x01",
            "受了盖伊的影响吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0011
    ChrTalk(
        0x109,
        (
            "#6P#10105F对了，我们进来时，\x01",
            "你好像在看照片……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x105,
        (
            "#6P#10300F照片上的人莫非就是\x01",
            "刚才说的盖伊先生？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xC,
        "#11P#01300F呵呵，要看看吗？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    #A0014
    AnonymousTalk(
        0x101,
        (
            "#00003F这张照片是三年前拍的。\x02\x03",

            "#00002F右边那个人就是\x01",
            "我大哥盖伊·班宁斯。\x02",
        )
    )

    CloseMessageWindow()

    #A0015
    AnonymousTalk(
        0x109,
        (
            "#10105F哎，这个人就是……\x02\x03",

            "#10102F呵呵，真不愧是罗伊德警官的哥哥，\x01",
            "看上去就是个非常正派的人。\x02",
        )
    )

    CloseMessageWindow()

    #A0016
    AnonymousTalk(
        0x104,
        (
            "#00309F塞茜尔小姐真是相当漂亮！！\x02\x03",

            "#00306F唔，我也好想成为\x01",
            "塞茜尔小姐的童年玩伴啊……\x02",
        )
    )

    CloseMessageWindow()

    #A0017
    AnonymousTalk(
        0x102,
        (
            "#00106F呼，兰迪，你可真是的……\x02\x03",

            "#00102F话说回来，这样一看……\x01",
            "盖伊先生和塞茜尔小姐\x01",
            "确实很般配。\x02",
        )
    )

    CloseMessageWindow()

    #A0018
    AnonymousTalk(
        0xC,
        (
            "#01309F呵呵，谢谢。\x01",
            "听你这样说，我非常开心。\x02",
        )
    )

    CloseMessageWindow()

    #A0019
    AnonymousTalk(
        0x105,
        (
            "#10302F呵呵，年幼的罗伊德\x01",
            "也很可爱嘛。\x02\x03",

            "#10304F单看这张照片，\x01",
            "就能隐隐感受到你那能让\x01",
            "纯情少女为之着迷的魔性呢。\x02",
        )
    )

    CloseMessageWindow()

    #A0020
    AnonymousTalk(
        0x101,
        "#00011F#4S哎……！？\x02",
    )

    CloseMessageWindow()

    #A0021
    AnonymousTalk(
        0x109,
        "#10106F（确、确实……）\x02",
    )

    CloseMessageWindow()

    #A0022
    AnonymousTalk(
        0x102,
        (
            "#00111F（如果他当时就是现在这种性格，\x01",
            "  肯定会是个相当危险的人物呢……）\x02",
        )
    )

    CloseMessageWindow()

    #A0023
    AnonymousTalk(
        0x101,
        (
            "#00006F……我好像又被你们\x01",
            "贴上了奇怪的标签。\x02",
        )
    )

    CloseMessageWindow()

    #A0024
    AnonymousTalk(
        0xC,
        "#01309F呵呵……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    #C0025
    ChrTalk(
        0xC,
        (
            "#11P#01303F……如今想来，从拍摄这张照片的那天\x01",
            "到现在，这几年里真是发生了无数变化呢。\x02\x03",

            "#01308F在盖伊不幸亡故之后，\x01",
            "一直都没有任何变化的……\x01",
            "恐怕就只有我了……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#6P#00005F塞茜尔姐姐……\x02\x03",

            "#00003F虽然可能还要再花费一段时间……\x01",
            "但请你等我。\x02\x03",

            "#00000F我一定会调查出\x01",
            "大哥那起事件的真相。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        (
            "#00100F嗯，我们也会\x01",
            "全力协助的。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xC,
        (
            "#11P#01304F……呵呵，谢谢大家。\x02\x03",

            "#01300F不过，一定不要勉强自己哦。\x01",
            "你们全都平安无事地生活，\x01",
            "就是我如今最大的心愿。\x02\x03",

            "#01309F要是受伤住院，\x01",
            "我可就要请赛兰德教授\x01",
            "给你们开很苦的药啦～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0029
    ChrTalk(
        0x104,
        (
            "#6P#00306F那位女教授调制的药\x01",
            "肯定会非常见效吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x105,
        (
            "#6P#10302F呵呵，如果她拿出真本事，\x01",
            "大概连药物的苦涩程度都能随意掌控。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        "#6P#00012F我、我们一定会多加小心的。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x1CB, 3)
    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_CC(0x1, 0xFF, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 152510, 0, 53400, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_93(0xC, 0x5A, 0x0)
    OP_4C(0xC, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_9_656 end

    def Function_10_104F(): pass

    label("Function_10_104F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1149")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F5")

    #C0032
    ChrTalk(
        0x8,
        "（擦擦擦）……¤\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "自从恢复接待门诊患者之后，\x01",
            "医院内的各位都干劲十足。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "为了给大家加油，我也要拿出\x01",
            "比平时更高的干劲来打扫！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1144")

    label("loc_10F5")


    #C0035
    ChrTalk(
        0x8,
        "（擦擦擦）……¤\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "为了给大家加油，我也要拿出\x01",
            "比平时更高的干劲来打扫！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1144")

    Jump("loc_19F2")

    label("loc_1149")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_11EE")

    #C0037
    ChrTalk(
        0x8,
        (
            "最近这段时间，从宿舍中出去的\x01",
            "实习医生和医生们全都是一副沮丧的表情。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "市里那些定期来医院复诊\x01",
            "的患者们几乎都不能来了，\x01",
            "他们都很担心那些患者吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19F2")

    label("loc_11EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1279")

    #C0039
    ChrTalk(
        0x8,
        (
            "多亏有珀利塞小姐和塔普先生\x01",
            "帮我打扫宿舍、运送食物，\x01",
            "真是帮了大忙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "要是他们能从此在这里工作，\x01",
            "那就更让人开心了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19F2")

    label("loc_1279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_12ED")

    #C0041
    ChrTalk(
        0x8,
        (
            "梅菲尔小姐今天\x01",
            "好像在房间中休息。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "大家平时一直都在拼命工作，\x01",
            "希望她能趁此机会好好休息一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19F2")

    label("loc_12ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1475")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13DC")

    #C0043
    ChrTalk(
        0x8,
        (
            "最近这几天，有很多人\x01",
            "来医院探望在袭击事件\x01",
            "中负伤的伤员。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "警察和警备队员的伤势\x01",
            "尤为严重，他们家人的\x01",
            "表情都很暗淡……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "如果自己的家人被卷入到\x01",
            "那种事件……光是想象一下，\x01",
            "我的胸口就会像要裂开一样难受。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1470")

    label("loc_13DC")


    #C0046
    ChrTalk(
        0x8,
        (
            "最近这几天，有很多人\x01",
            "来医院探望在袭击事件\x01",
            "中负伤的伤员。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "如果自己的家人被卷入到\x01",
            "那种事件……光是想象一下，\x01",
            "我的胸口就会像要裂开一样难受。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1470")

    Jump("loc_19F2")

    label("loc_1475")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_14EE")

    #C0048
    ChrTalk(
        0x8,
        (
            "由于发生了列车事故，\x01",
            "众位医生和实习医生\x01",
            "好像全员出动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "我要趁现在把所有角落\x01",
            "都打扫得干干净净。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19F2")

    label("loc_14EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_15E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_157E")

    #C0050
    ChrTalk(
        0x8,
        (
            "据事务长说，\x01",
            "明天一早就会下雨。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "他好像是通过导力网络\x01",
            "收看了天气预报。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "呼，这个世界真是\x01",
            "越来越便捷了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15E0")

    label("loc_157E")


    #C0053
    ChrTalk(
        0x8,
        "听说明天一早就会下雨。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "竟然可以通过导力网络\x01",
            "来收看天气预报，\x01",
            "这个世界真是越来越便捷了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15E0")

    Jump("loc_19F2")

    label("loc_15E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_174B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16CE")

    #C0055
    ChrTalk(
        0x8,
        (
            "亚里欧斯先生在女儿\x01",
            "接受手术的期间，\x01",
            "一直都坐立不安的。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "亚里欧斯先生有『风之剑圣』之称，\x01",
            "在很多人的眼中，简直就像是\x01",
            "身处云端的神人……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "但从他当时那种样子来看，\x01",
            "完全就是个关怀女儿的\x01",
            "普通父亲。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1746")

    label("loc_16CE")


    #C0058
    ChrTalk(
        0x8,
        (
            "亚里欧斯先生在女儿\x01",
            "接受手术的期间，\x01",
            "一直都坐立不安的。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "从他当时那种样子来看，\x01",
            "完全就是个关怀女儿的\x01",
            "普通父亲。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1746")

    Jump("loc_19F2")

    label("loc_174B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_17B8")

    #C0060
    ChrTalk(
        0x8,
        (
            "贝尔达因医生\x01",
            "今天难得休息。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "他最近一直都在\x01",
            "连续工作，这次要是\x01",
            "能充分休息一下就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19F2")

    label("loc_17B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_18D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1862")

    #C0062
    ChrTalk(
        0x8,
        (
            "（擦擦）……¤\x01",
            "这层是女子宿舍。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "我要比打扫男子宿舍时\x01",
            "更加用心。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "……呵呵，只是开个玩笑而已。\x01",
            "只要关系到扫除，我都会无比用心的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18D0")

    label("loc_1862")


    #C0065
    ChrTalk(
        0x8,
        (
            "啊……\x01",
            "难道阿修拉主任\x01",
            "还在睡懒觉吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "嗯……她昨天好像在研究楼\x01",
            "工作到很晚，\x01",
            "硬叫她起床未免有些残忍。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18D0")

    Jump("loc_19F2")

    label("loc_18D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_19F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_199C")

    #C0067
    ChrTalk(
        0x8,
        (
            "（擦擦）……¤\x01",
            "扫除真是一件令人开心的工作～☆\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x8,
        (
            "……啊，你们要找谁呢？\x01",
            "我正在打扫男子宿舍。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "各位医生和实习医生\x01",
            "全都出门了。\x01",
            "你们要是有事，就去病房楼找他们吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_19F2")

    label("loc_199C")


    #C0070
    ChrTalk(
        0x8,
        (
            "（擦擦）……¤\x01",
            "嗯，打扫得非常干净呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "接下来，就去露台呼吸一下\x01",
            "新鲜空气吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19F2")

    TalkEnd(0xFE)
    Return()

    # Function_10_104F end

    def Function_11_19F6(): pass

    label("Function_11_19F6")

    TalkBegin(0xFE)
    OP_64(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A74")

    #C0072
    ChrTalk(
        0x9,
        (
            "……要用导力透视射线\x01",
            "检查到每一个角落哦～¤\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        "……呼……呼……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        "#00006F在、在说梦话吗……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1AAD")

    label("loc_1A74")


    #C0075
    ChrTalk(
        0x9,
        (
            "……哎呀，\x01",
            "感光回路用完了……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        "……呼……呼……\x02",
    )

    CloseMessageWindow()

    label("loc_1AAD")

    OP_63(0xFE, 0x0, 1700, 0x1C, 0x21, 0xFA, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_19F6 end

    def Function_12_1AC3(): pass

    label("Function_12_1AC3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B63")

    #C0077
    ChrTalk(
        0xA,
        (
            "实习医生们让我不要太勉强，\x01",
            "稍微休息一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xA,
        (
            "说起来，我好像有好几个月\x01",
            "都没正经休过假了……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        (
            "难得休假，\x01",
            "今天就彻底放松一下好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1BA8")

    label("loc_1B63")


    #C0080
    ChrTalk(
        0xA,
        "保养身体也是很重要的。\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xA,
        (
            "难得休假，\x01",
            "今天就彻底放松一下好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BA8")

    TalkEnd(0xFE)
    Return()

    # Function_12_1AC3 end

    def Function_13_1BAC(): pass

    label("Function_13_1BAC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1BBD")
    Jump("loc_1D64")

    label("loc_1BBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1BCB")
    Jump("loc_1D64")

    label("loc_1BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1BD9")
    Jump("loc_1D64")

    label("loc_1BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1D64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CCC")

    #C0082
    ChrTalk(
        0xB,
        (
            "自从门诊患者无法入院之后，\x01",
            "最近这段时间\x01",
            "总能休假呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xB,
        (
            "虽然这种情况让人完全高兴不起来，\x01",
            "但护士长对我说，\x01",
            "该休息的时候就要好好休息。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xB,
        (
            "话说回来，放着希伦那家伙不管，\x01",
            "实在是有些担心呢……\x01",
            "稍后去看看她好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1D64")

    label("loc_1CCC")


    #C0085
    ChrTalk(
        0xB,
        (
            "希伦那家伙真是让人放不下心来……\x01",
            "我不在的时候，她该不会\x01",
            "又做出什么奇怪的举动吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xB,
        (
            "……啊，不行不行。\x01",
            "要是总担心希伦，\x01",
            "就不能放松精神休息了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D64")

    TalkEnd(0xFE)
    Return()

    # Function_13_1BAC end

    SaveToFile()

Try(main)
