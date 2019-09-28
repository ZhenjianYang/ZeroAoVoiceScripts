from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0310.bin",                # FileName
        "c0310",                    # MapName
        "c0310",                    # Location
        0x002B,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 43, 0, 4, 0, 5],
    )

    BuildStringList((
        "c0310",                  # 0
        "海尔玛",                 # 1
        "乔安娜",                 # 2
        "麦克道尔市长",           # 3
        "伊斯",                   # 4
        "雕像",                   # 5
    ))

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch25700.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
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

    DeclNpc(0,       0,       0,       180,  257,  0x0, 0,   0,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(-45349,  59,      3900,    360,  257,  0x0, 0,   1,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 12,  41.130001068115234,    44.029998779296875,    0.05999999865889549,   9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -20.565000534057617,   -14.676666259765625,   -0.012000001035630703, 1.0])

    DeclActor(-40820,  0,       40910,   1500,    -40820,  1500,    40910,   0x007C, 0,  13, 0x0000)

    ScpFunction((
        "Function_0_254",          # 00, 0
        "Function_1_30C",          # 01, 1
        "Function_2_337",          # 02, 2
        "Function_3_362",          # 03, 3
        "Function_4_38D",          # 04, 4
        "Function_5_518",          # 05, 5
        "Function_6_592",          # 06, 6
        "Function_7_1B43",         # 07, 7
        "Function_8_1EB2",         # 08, 8
        "Function_9_1F72",         # 09, 9
        "Function_10_3618",        # 0A, 10
        "Function_11_3868",        # 0B, 11
        "Function_12_4514",        # 0C, 12
        "Function_13_5157",        # 0D, 13
    ))


    def Function_0_254(): pass

    label("Function_0_254")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_294"),
        (1, "loc_2A0"),
        (2, "loc_2AC"),
        (3, "loc_2B8"),
        (4, "loc_2C4"),
        (5, "loc_2D0"),
        (6, "loc_2DC"),
        (SWITCH_DEFAULT, "loc_2E8"),
    )


    label("loc_294")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_2A0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_2AC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_2B8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_2C4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_2D0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_2DC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_2E8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_2F4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_30B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2F4")

    label("loc_30B")

    Return()

    # Function_0_254 end

    def Function_1_30C(): pass

    label("Function_1_30C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_336")
    OP_94(0xFE, 0xFFFFF63C, 0x0, 0x9C4, 0x73A, 0x3E8)
    Sleep(300)
    Jump("Function_1_30C")

    label("loc_336")

    Return()

    # Function_1_30C end

    def Function_2_337(): pass

    label("Function_2_337")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_361")
    OP_94(0xFE, 0xFFFFF8B2, 0x1A36, 0x744, 0x26DE, 0x3E8)
    Sleep(300)
    Jump("Function_2_337")

    label("loc_361")

    Return()

    # Function_2_337 end

    def Function_3_362(): pass

    label("Function_3_362")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38C")
    OP_94(0xFE, 0xA00A, 0xA05A, 0xB31A, 0xB220, 0x3E8)
    Sleep(300)
    Jump("Function_3_362")

    label("loc_38C")

    Return()

    # Function_3_362 end

    def Function_4_38D(): pass

    label("Function_4_38D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_39C")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 11)

    label("loc_39C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3C7")
    SetChrPos(0x8, 0, 4059, 7760, 180)
    BeginChrThread(0x8, 0, 0, 2)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_517")

    label("loc_3C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3F1")
    SetChrPos(0x8, 0, 4059, 7760, 180)
    BeginChrThread(0x8, 0, 0, 2)
    SetChrFlags(0x9, 0x80)
    Jump("loc_517")

    label("loc_3F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_41C")
    SetChrPos(0x8, 0, 4059, 7760, 180)
    BeginChrThread(0x8, 0, 0, 2)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_517")

    label("loc_41C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_436")
    BeginChrThread(0x8, 0, 0, 1)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_517")

    label("loc_436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_461")
    SetChrPos(0x8, 0, 4059, 13210, 360)
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_517")

    label("loc_461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_49D")
    SetChrPos(0x8, 2580, 4000, 13150, 45)
    SetChrPos(0x9, -44780, 60, 47510, 270)
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_517")

    label("loc_49D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4C8")
    SetChrPos(0x9, 43580, 0, 43630, 180)
    BeginChrThread(0x8, 0, 0, 1)
    BeginChrThread(0x9, 0, 0, 3)
    Jump("loc_517")

    label("loc_4C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4F3")
    SetChrPos(0x8, 0, 4059, 7760, 180)
    BeginChrThread(0x8, 0, 0, 2)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_517")

    label("loc_4F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 4)), scpexpr(EXPR_END)), "loc_50D")
    BeginChrThread(0x8, 0, 0, 1)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_517")

    label("loc_50D")

    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)

    label("loc_517")

    Return()

    # Function_4_38D end

    def Function_5_518(): pass

    label("Function_5_518")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53F")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_53F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_558")
    OP_10(0x0, 0x0)
    OP_10(0xB, 0x1)
    Jump("loc_55E")

    label("loc_558")

    OP_10(0x0, 0x1)
    OP_10(0xB, 0x0)

    label("loc_55E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_57A")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_591")

    label("loc_57A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_591")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_591")

    label("loc_591")

    Return()

    # Function_5_518 end

    def Function_6_592(): pass

    label("Function_6_592")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_74C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_62E")

    #C0001
    ChrTalk(
        0xFE,
        (
            "老爷只听得进\x01",
            "艾莉小姐的意见。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "实在非常抱歉，\x01",
            "只能拜托您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x102,
        (
            "#0100F外公是政治家……\x01",
            "我也不知道他能不能\x01",
            "听进我的话。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_747")

    label("loc_62E")


    #C0004
    ChrTalk(
        0xFE,
        (
            "其实刚才接到了联络，\x01",
            "听说老爷今天也要加班。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "唉，真担心老爷的身体。\x01",
            "等议会结束后，\x01",
            "必须先让老爷好好休息一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x102,
        (
            "#0103F外公他也很固执……\x01",
            "现在不管我们怎么说，他应该都听不进去吧。\x02\x03",

            "#0100F如果以后遇到合适的时机，\x01",
            "我会再劝劝他的。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "好，实在非常抱歉，\x01",
            "只能拜托您了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_747")

    Jump("loc_1B3F")

    label("loc_74C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_860")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7CA")

    #C0008
    ChrTalk(
        0xFE,
        (
            "听说昨天在港湾区\x01",
            "发生了枪击事件……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "不知道本德先生有没有\x01",
            "被卷入什么恐怖事件中，\x01",
            "真让人担心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_85B")

    label("loc_7CA")


    #C0010
    ChrTalk(
        0xFE,
        (
            "刚才库雷优夫人\x01",
            "来过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "说是没找到自己的丈夫本德先生。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "唉，到底发生了什么事呢？\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "听说最近发生了很多事件……\x01",
            "真让人担心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_85B")

    Jump("loc_1B3F")

    label("loc_860")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_973")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8C8")

    #C0014
    ChrTalk(
        0xFE,
        (
            "我服侍老爷\x01",
            "已经足足有四十年了。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "所以绝对\x01",
            "无法原谅\x01",
            "哈尔特曼议长的态度。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_96E")

    label("loc_8C8")


    #C0016
    ChrTalk(
        0xFE,
        (
            "哈尔特曼议长\x01",
            "和老爷同是自治州代表，\x01",
            "应该担负着统率议会的责任……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "但他却对议会的松散状态\x01",
            "不管不顾……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "那种态度肯定\x01",
            "是故意在为难老爷，\x01",
            "真是不可原谅。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_96E")

    Jump("loc_1B3F")

    label("loc_973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_BD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCC, 3)), scpexpr(EXPR_END)), "loc_A3A")

    #C0019
    ChrTalk(
        0xFE,
        (
            "预算会议的结束时间延迟了，\x01",
            "所以老爷还要继续加班。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "嗯，最让人担心的果然\x01",
            "还是老爷的身体啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "离市长选举\x01",
            "仅剩四个月了。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        (
            "#0108F是啊……\x01",
            "希望外公可不要太勉强啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BD4")

    label("loc_A3A")

    TurnDirection(0xFE, 0x102, 500)

    #C0023
    ChrTalk(
        0xFE,
        (
            "哦，艾莉小姐，\x01",
            "您今天的气色好像不是很好啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        (
            "#0105F咦…………！？\x01",
            "没、没有啦。\x02\x03",

            "#0103F海尔玛先生，\x01",
            "你别乱说啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "这样啊……不过，\x01",
            "说到小姐最怕的东西，\x01",
            "应该只有那个或者是那个了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "不对不对，好像小时候也\x01",
            "很怕些鬼怪之类的。\x01",
            "唔……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#0309F大小姐，没想到你\x01",
            "也有害怕的东西啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x109,
        (
            "#0503F对不起，向你们提出了\x01",
            "奇怪的委托……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        (
            "#0112F我、我可不害怕，\x01",
            "诺艾尔小姐也请不必自责啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCC, 3)

    label("loc_BD4")

    Jump("loc_1B3F")

    label("loc_BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_EB0")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C57")

    #C0030
    ChrTalk(
        0xFE,
        (
            "是吗……\x01",
            "总之，这栋宅邸里是\x01",
            "非常安全的。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "如果发生了什么，\x01",
            "请务必躲到这里来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4C")

    label("loc_C57")


    #C0032
    ChrTalk(
        0xFE,
        (
            "是艾莉小姐，还有各位啊，\x01",
            "老爷已经把事情的大致情况\x01",
            "告诉我了……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "…………………………（四下张望）\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        "#2S……这栋宅邸里是非常安全的。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "#2S如果发生了什么，\x01",
            "  请务必躲到这里来！\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        (
            "#0100F谢、谢谢你，海尔玛先生。\x01",
            "不过已经没事了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_D4C")

    Jump("loc_EAB")

    label("loc_D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_DB6")

    #C0037
    ChrTalk(
        0xFE,
        (
            "是吗……\x01",
            "总之，这栋宅邸里是\x01",
            "非常安全的。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "如果发生了什么，\x01",
            "请务必躲到这里来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_EAB")

    label("loc_DB6")


    #C0039
    ChrTalk(
        0xFE,
        (
            "是支援科的各位啊，\x01",
            "老爷已经把事情的大致情况\x01",
            "告诉我了……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "…………………………（四下张望）\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "……我们麦克道尔官邸\x01",
            "是非常安全的。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "如果发生了什么，\x01",
            "请务必和艾莉小姐一起\x01",
            "躲到这里来！\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        (
            "#0000F谢、谢谢您。\x01",
            "……不过已经没事了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_EAB")

    Jump("loc_1B3F")

    label("loc_EB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_120E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_FED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA0")

    #C0044
    ChrTalk(
        0xFE,
        (
            "哎呀呀，刚才\x01",
            "真是吓了一跳啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "真是，也不知道那东西是\x01",
            "什么时候跑进来的……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "等老爷回来后，\x01",
            "必须马上告诉他啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        (
            "#0100F也、也是哦……\x01",
            "那就麻烦你简单\x01",
            "跟外公说下。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        "好，非常乐意效劳。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FE8")

    label("loc_FA0")


    #C0049
    ChrTalk(
        0xFE,
        (
            "不过，怪盗Ｂ……\x01",
            "他竟然会来这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "我以后必须\x01",
            "更加提高警惕啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FE8")

    Jump("loc_1209")

    label("loc_FED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1058")

    #C0051
    ChrTalk(
        0xFE,
        (
            "最近，艾莉小姐表现活跃的消息，\x01",
            "是唯一可以让\x01",
            "老爷开心的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "希望您能更加\x01",
            "努力工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1209")

    label("loc_1058")

    TurnDirection(0xFE, 0x102, 500)

    #C0053
    ChrTalk(
        0xFE,
        "是艾莉小姐啊。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "老爷今天好像\x01",
            "会提早回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x102,
        (
            "#0105F这样啊……\x02\x03",

            "#0104F太好了，外公偶尔就该像这样\x01",
            "好好放松休息一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "嗯，乔安娜也正在干劲十足地\x01",
            "准备晚餐呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "……艾莉小姐，您和您的朋友们\x01",
            "也留下来一起用晚餐吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        (
            "#0105F啊……\x01",
            "……今天还有很重要的工作要完成……\x02\x03",

            "#0106F抱歉哦，\x01",
            "也不知道那工作什么时候能做完。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        "这样啊，是我考虑不周。\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        "那我先去做准备，好迎接老爷回来。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "希望您能更加\x01",
            "努力工作。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1209")

    Jump("loc_1B3F")

    label("loc_120E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_12ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1281")

    #C0062
    ChrTalk(
        0xFE,
        "老爷的责任感太强了……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "虽然我很担心他的身体，\x01",
            "但我只是一介佣人，\x01",
            "很难劝得了他啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12E8")

    label("loc_1281")


    #C0064
    ChrTalk(
        0xFE,
        (
            "老爷这几天连续出席了\x01",
            "多个活动和宴会，一定很疲惫了。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "嗯，虽然我一直请求\x01",
            "他能偶尔早点回来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_12E8")

    Jump("loc_1B3F")

    label("loc_12ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_14E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1347")

    #C0066
    ChrTalk(
        0xFE,
        "这样啊，那可真令人遗憾。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "那就等到十几年后\x01",
            "再打开看看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DB")

    label("loc_1347")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x102, 500)
    Sleep(500)

    #C0068
    ChrTalk(
        0xFE,
        (
            "哦哦，艾莉小姐！\x01",
            "您回来得正是时候……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x102,
        "#0105F海尔玛先生，怎么了吗！？\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "我们刚才打扫的时候\x01",
            "在阁楼上发现了这个木箱……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "我猜应该是小姐您小时候\x01",
            "放宝物的箱子吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "呵呵，那时候的小姐\x01",
            "真是可爱啊，\x01",
            "总是喜欢收集一些很漂亮的小东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        "小姐，您看这个木箱要如何处理？\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x102,
        (
            "#0113F……放回\x01",
            "原来的地方吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        (
            "#0000F（原来艾莉也有过\x01",
            "  这么少女气的爱好啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_14DB")

    Jump("loc_1B3F")

    label("loc_14E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_167A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1545")

    #C0076
    ChrTalk(
        0xFE,
        (
            "我太大惊小怪了，\x01",
            "实在非常抱歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "因为老爷不在家，\x01",
            "所以就想打扫一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1675")

    label("loc_1545")


    #C0078
    ChrTalk(
        0xFE,
        (
            "是艾莉小姐啊。\x01",
            "我太大惊小怪了，\x01",
            "实在非常抱歉。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x102,
        (
            "#0100F海尔玛先生，你今天\x01",
            "好像特别有干劲啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        "哈哈，这没什么。\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "每年这个时候，\x01",
            "老爷都会去参加各种活动，\x01",
            "几乎不怎么回家。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "家里只剩些佣人，\x01",
            "所以我都会趁这个时候做一次大扫除。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "艾莉小姐去留学的那段时间，\x01",
            "我每年都保持着这个习惯。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1675")

    Jump("loc_1B3F")

    label("loc_167A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_17A9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16F7")

    #C0084
    ChrTalk(
        0xFE,
        (
            "考虑到老爷的身份，\x01",
            "我也无法太过强求他不要勉强自己。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "站在佣人的立场上，\x01",
            "心情还真是很矛盾啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17A4")

    label("loc_16F7")


    #C0086
    ChrTalk(
        0xFE,
        (
            "老爷的身体\x01",
            "终于有点好转了。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "应该是那些\x01",
            "具有滋补效果的食物\x01",
            "起作用了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "不过，还是希望\x01",
            "老爷不要总那么勉强自己……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        "虽然考虑到老爷的身份，这也是很难的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_17A4")

    Jump("loc_1B3F")

    label("loc_17A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_184B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17C4")
    Call(0, 8)
    Jump("loc_1846")

    label("loc_17C4")


    #C0090
    ChrTalk(
        0xFE,
        (
            "我女儿乔安娜从七岁开始\x01",
            "就一直负责照顾艾莉小姐的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "所以她一直都\x01",
            "非常担心小姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        "如有什么失礼之处，还请多多包涵。\x02",
    )

    CloseMessageWindow()

    label("loc_1846")

    Jump("loc_1B3F")

    label("loc_184B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8D, 2)), scpexpr(EXPR_END)), "loc_1B3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1866")
    Call(0, 8)
    Jump("loc_1B37")

    label("loc_1866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_19EA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_18B3")

    #C0093
    ChrTalk(
        0xFE,
        "我好像太多管闲事了。\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        "希望您能更加努力工作。\x02",
    )

    CloseMessageWindow()
    Jump("loc_19E5")

    label("loc_18B3")


    #C0095
    ChrTalk(
        0xFE,
        (
            "听说小姐您昨天\x01",
            "遇到了阿奈斯特先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "……他应该也是因为\x01",
            "担心小姐您，\x01",
            "才提出了那些意见吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "我的心情\x01",
            "也与他相同。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "看到小姐您这么苦恼迷惘的样子，\x01",
            "我们都很心疼。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x102,
        (
            "#0104F……海尔玛先生，谢谢你。\x02\x03",

            "#0100F不过已经没事了。\x01",
            "我已经不再迷惘了。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        "这样啊。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "哈哈，那我是\x01",
            "多管闲事了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_19E5")

    Jump("loc_1B37")

    label("loc_19EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A42")

    #C0102
    ChrTalk(
        0xFE,
        (
            "各位，小姐就拜托\x01",
            "你们照顾了。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "因为小姐她是我\x01",
            "最引以为傲的人啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B37")

    label("loc_1A42")


    #C0104
    ChrTalk(
        0xFE,
        (
            "……各位是小姐的同事吧。\x01",
            "久仰大名啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "各位，小姐就拜托\x01",
            "你们照顾了。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "小姐从小\x01",
            "就非常优秀，\x01",
            "而且还非常可爱……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "因为小姐她是我\x01",
            "最引以为傲的人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x102,
        (
            "#0112F……海尔玛先生，你也\x01",
            "别再说些多余的事了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        "哈哈，是我失礼了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1B37")

    Jump("loc_1B3F")

    label("loc_1B3C")

    Call(0, 7)

    label("loc_1B3F")

    TalkEnd(0xFE)
    Return()

    # Function_6_592 end

    def Function_7_1B43(): pass

    label("Function_7_1B43")

    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x8, 0x102, 500)
    Sleep(500)

    #C0110
    ChrTalk(
        0x8,
        "这不是……艾莉小姐吗！？\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "真是久疏问候了。\x01",
            "自从您在当警察前回来过一次之后，\x01",
            "就没有再回来过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        (
            "#0103F海尔玛先生，抱歉啊，\x01",
            "我的确太久没回来了。\x02\x03",

            "#0100F你们都还好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        "是的，我们都很好。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "我和乔安娜\x01",
            "连一次病都没生过。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x8,
        (
            "老爷也还是一如往常，\x01",
            "总是十分忙碌。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        "#0100F呵呵，外公也有很多棘手的问题要处理啊……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x104,
        (
            "#0300F（小声……不愧是大小姐的家啊，\x01",
            "  看起来就透着富贵之气。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D47")

    #C0118
    ChrTalk(
        0x103,
        (
            "#0200F（而且艾莉前辈与管家大叔的对话\x01",
            "  也有种娴熟自然的感觉。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DD2")

    label("loc_1D47")


    #C0119
    ChrTalk(
        0x103,
        (
            "#0200F（嗯，我记得之前\x01",
            "  好像曾来过一次，\x01",
            "  宅邸内部的装修也很气派。）\x02\x03",

            "（而且艾莉前辈与管家大叔的对话\x01",
            "  好像也有种娴熟自然的感觉。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DD2")


    #C0120
    ChrTalk(
        0x101,
        (
            "#0000F（哈哈……因为麦克道尔家\x01",
            "  从以前就是名门望族啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x103, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x102, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)

    #C0121
    ChrTalk(
        0x102,
        (
            "#0106F……就因为知道会这样，\x01",
            "所以才一直不想\x01",
            "带你们来的啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8D, 2)
    Return()

    # Function_7_1B43 end

    def Function_8_1EB2(): pass

    label("Function_8_1EB2")


    #C0122
    ChrTalk(
        0xFE,
        "各位，你们要看小说吗？\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "这本书是我工作之余用来消遣的，\x01",
            "现在已经看完了，\x01",
            "就送给你们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        "请千万不要客气。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0125
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2C9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('黑市医生格伦　４卷', 1)
    SetScenarioFlags(0x9C, 3)
    Return()

    # Function_8_1EB2 end

    def Function_9_1F72(): pass

    label("Function_9_1F72")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_20ED")
    TurnDirection(0x9, 0x102, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1FF3")

    #C0126
    ChrTalk(
        0xFE,
        (
            "我听说特别任务支援科的工作\x01",
            "做得非常出色，\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "希望各位今后能再接再厉。\x01",
            "……我等着您回来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E8")

    label("loc_1FF3")


    #C0128
    ChrTalk(
        0xFE,
        (
            "老爷今天好像\x01",
            "会晚点回家。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        "……小姐您这是在工作吗？\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "我听说特别任务支援科的工作\x01",
            "做得非常出色，\x01",
            "希望您能继续加油。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x102,
        (
            "#0100F嗯，谢谢你，乔安娜。\x01",
            "外公就拜托你照顾了。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        "是的，请放心交给我吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_20E8")

    Jump("loc_3614")

    label("loc_20ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_22AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2131")
    TurnDirection(0x9, 0x102, 0)

    #C0134
    ChrTalk(
        0xFE,
        "……艾莉小姐，请您务必注意身体。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22A7")

    label("loc_2131")


    #C0135
    ChrTalk(
        0xFE,
        "最近听说了很多事件的传闻呢。\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "警察的工作一定很忙，\x01",
            "我很担心您的身体啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x102,
        (
            "#0100F哈哈……我觉得\x01",
            "反倒是乔安娜和海尔玛先生\x01",
            "你们更让人担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#0000F艾莉家平时\x01",
            "好像只有佣人在啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_END)), "loc_2277")

    #C0140
    ChrTalk(
        0x104,
        (
            "#0300F这附近治安不错，\x01",
            "应该没问题的。\x02\x03",

            "#0303F……虽然隔壁的\x01",
            "事件有些让人难以捉摸。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22A4")

    label("loc_2277")


    #C0141
    ChrTalk(
        0x104,
        (
            "#0300F但这附近治安不错，\x01",
            "应该没问题的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22A4")

    SetScenarioFlags(0x0, 1)

    label("loc_22A7")

    Jump("loc_3614")

    label("loc_22AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2573")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2350")
    TurnDirection(0xFE, 0x102, 500)

    #C0142
    ChrTalk(
        0xFE,
        "艾莉小姐……\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "如果有可怕的事件发生，\x01",
            "希望您千万不要勉强啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x102,
        (
            "#0106F（我明明已经尽力掩饰了，\x01",
            "  为什么还是被发现了啊……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_256E")

    label("loc_2350")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0xFE, 0x102, 500)

    #C0145
    ChrTalk(
        0xFE,
        (
            "………………………………？\x01",
            "…………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        "艾莉小姐，那个……\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x102,
        "#0100F怎、怎么了，乔安娜？\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "如果您遇到什么害怕的事，\x01",
            "请随时叫我过去。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "就像以前一样……\x01",
            "无论是睡觉，还是晚上去洗手间，\x01",
            "我都会陪着您。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0150
    ChrTalk(
        0x109,
        (
            "#0500F很抱歉，\x01",
            "真的很抱歉……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x102,
        (
            "#0113F真、真是的……\x01",
            "这都是陈年旧事啦……！\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x103,
        (
            "#0200F以前都是多亏了乔安娜小姐\x01",
            "的照顾啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        (
            "#0000F（哈哈……\x01",
            "  没想到她竟然有这么可爱的一面。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_256E")

    Jump("loc_3614")

    label("loc_2573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2927")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_27D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2654")
    TurnDirection(0xFE, 0x102, 500)

    #C0154
    ChrTalk(
        0xFE,
        "……晚上我做点好吃的。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "希望您能留下来\x01",
            "和老爷一起用餐。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x102,
        (
            "#0104F嗯，好吧。\x02\x03",

            "#0100F……那就麻烦你\x01",
            "去准备了。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "…………………………（慌慌张张）\x01",
            "请放心交给我吧……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27D2")

    label("loc_2654")

    TurnDirection(0xFE, 0x102, 500)
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0158
    ChrTalk(
        0xFE,
        "………………………………！\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "艾莉小姐……\x01",
            "您没事吧……！\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x102,
        (
            "#0103F乔安娜……抱歉啊。\x01",
            "我这么久没回来。\x02\x03",

            "#0100F也让你为我\x01",
            "担了不少心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        "……………………（紧张紧张）\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        "我一直都坚信小姐不会有事的。\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x102,
        (
            "#0109F哈哈，这样啊……\x02\x03",

            "#0100F谢谢，晚上我会再\x01",
            "回来一趟的。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "…………………………（慌慌张张）\x01",
            "好、好的，我等着您回来……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_27D2")

    Jump("loc_2922")

    label("loc_27D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2812")

    #C0165
    ChrTalk(
        0xFE,
        (
            "……小姐\x01",
            "就拜托各位照顾了。（低头行礼）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2922")

    label("loc_2812")

    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0166
    ChrTalk(
        0xFE,
        "………………………………！\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        "那个，请问艾莉小姐她……\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        (
            "#0006F抱歉啊，她今天\x01",
            "没和我们一起行动。\x02\x03",

            "#0000F不过她很好，\x01",
            "不用担心。\x01",
            "而且事件也算暂时解决了。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        "………………………………（点头）\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "小姐\x01",
            "就拜托各位照顾了。（低头行礼）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2922")

    Jump("loc_3614")

    label("loc_2927")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2C11")
    TurnDirection(0x9, 0x102, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2ABE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A7E")

    #C0171
    ChrTalk(
        0xFE,
        (
            "艾莉小姐……事情我听说了。\x01",
            "您是在对付怪盗Ｂ吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(1000)

    #C0172
    ChrTalk(
        0xFE,
        (
            "那个，下次\x01",
            "请把乔安娜的平底锅\x01",
            "也带去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0173
    ChrTalk(
        0x102,
        "#0105F谢、谢谢你，乔安娜。\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        "#0000F（是想让艾莉拿平底锅来防御吗。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2AB9")

    label("loc_2A7E")


    #C0175
    ChrTalk(
        0xFE,
        "小姐……\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "……您在工作的时候，\x01",
            "请务必要注意身体。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AB9")

    Jump("loc_2C0C")

    label("loc_2ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2B20")

    #C0177
    ChrTalk(
        0xFE,
        (
            "老爷今天好像\x01",
            "能早点回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "………………………………\x01",
            "艾莉小姐，工作加油啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C0C")

    label("loc_2B20")


    #C0179
    ChrTalk(
        0xFE,
        (
            "老爷今天好像\x01",
            "能早点回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        "……………那个…………\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xFE)

    #C0181
    ChrTalk(
        0xFE,
        "……没什么。\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        "各位，工作请加油哦。\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x104,
        (
            "#0300F（喂，是不是有什么话\x01",
            "  想对大小姐说啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x102,
        (
            "#0103F（抱歉啊，乔安娜，\x01",
            "  我今天工作很忙……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2C0C")

    Jump("loc_3614")

    label("loc_2C11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2C5D")

    #C0185
    ChrTalk(
        0xFE,
        "今天有庆典游行吧。\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        "孩子们看上去好像都很开心，真好。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3614")

    label("loc_2C5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2D81")
    TurnDirection(0x9, 0x102, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2CB0")

    #C0187
    ChrTalk(
        0xFE,
        (
            "我每天都会打扫\x01",
            "您的房间。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        "……请不必担心。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2D7C")

    label("loc_2CB0")


    #C0189
    ChrTalk(
        0xFE,
        "艾莉小姐……\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "我每天都会帮您铺好床，\x01",
            "您随时都可以回来休息。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x102,
        "#0105F谢、谢谢你，乔安娜。\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x104,
        (
            "#0300F（该说这位女仆是保护过度，\x01",
            "  还是过于多虑呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x102,
        (
            "#0100F（乔安娜其实和我\x01",
            "  同岁哦。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2D7C")

    Jump("loc_3614")

    label("loc_2D81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2E2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2DD0")

    #C0194
    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        "老爷的身体真让人担心啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E27")

    label("loc_2DD0")


    #C0196
    ChrTalk(
        0xFE,
        "我在打扫老爷的房间。\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        "顺便调整一下窗帘……\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        "因为过强的日照会有害健康。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2E27")

    Jump("loc_3614")

    label("loc_2E2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3078")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2E7D")
    TurnDirection(0x9, 0x102, 0)

    #C0199
    ChrTalk(
        0xFE,
        (
            "小姐，\x01",
            "工作请加油哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        "我会一直支持您的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3073")

    label("loc_2E7D")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x102, 500)
    Sleep(500)

    #C0201
    ChrTalk(
        0xFE,
        "艾莉小姐……\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "实在抱歉，我之前\x01",
            "一直误会了……\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x102,
        (
            "#0105F乔安娜……？\x01",
            "（发生什么事了吗……）\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "特别任务支援科是一个\x01",
            "非常出色的部门吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        (
            "我已经听说了，它是一个比搜查一科的权限还要大，\x01",
            "获得过无数功勋，\x01",
            "精英云集的部门……\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "……还请您\x01",
            "原谅我之前的误会。\x02",
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
    Sleep(1000)

    #C0207
    ChrTalk(
        0x104,
        "#0306F（不，这下就是评价过高了。）\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x102,
        (
            "#0108F（真难办……\x01",
            "  乔安娜看问题有些\x01",
            "  太极端了啊……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3073")

    Jump("loc_3614")

    label("loc_3078")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3247")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_30F9")

    #C0209
    ChrTalk(
        0xFE,
        (
            "我听说支援科的赛尔盖警督\x01",
            "一天到晚总是无所事事，\x01",
            "是个毫无建树的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        "……………………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_3242")

    label("loc_30F9")


    #C0211
    ChrTalk(
        0xFE,
        (
            "……支援科的负责人\x01",
            "是一位名叫赛尔盖的警督吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "我听说他一天到晚总是无所事事，\x01",
            "是个毫无建树的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        "……………………………………\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x101,
        "#0003F（科长很不被信任啊……）\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x104,
        (
            "#0306F（不过，这也难怪吧。）\x02\x03",

            "#0300F（希望他不会被麦克道尔家的权势\x01",
            "  所击垮啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0216
    ChrTalk(
        0x102,
        "#0103F（……才不会有那种事。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3242")

    Jump("loc_3614")

    label("loc_3247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8D, 3)), scpexpr(EXPR_END)), "loc_3611")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_343F")
    TurnDirection(0x9, 0x102, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_32C4")

    #C0217
    ChrTalk(
        0xFE,
        (
            "我觉得凭艾莉小姐您的学识，\x01",
            "无论什么工作都能轻松胜任。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "……欢迎您\x01",
            "随时回来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_343A")

    label("loc_32C4")


    #C0219
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x102,
        "#0105F乔安娜，怎么了吗？\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        "没事，就是……\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "我听说，特别任务支援科\x01",
            "是个不被看好的部门。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        "………………………………\x02",
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

    #C0224
    ChrTalk(
        0x103,
        (
            "#0200F（艾莉前辈，她好像很\x01",
            "  担心你啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x102,
        (
            "#0103F（抱歉啊，乔安娜……\x01",
            "  但我还想在\x01",
            "  支援科努力一下。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_343A")

    Jump("loc_360C")

    label("loc_343F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_34A3")

    #C0226
    ChrTalk(
        0xFE,
        (
            "我觉得凭艾莉小姐您的学识，\x01",
            "无论什么工作都能轻松胜任。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "……欢迎您\x01",
            "随时回来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_360C")

    label("loc_34A3")


    #C0228
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x102,
        "#0105F乔安娜，怎么了？\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0xFE,
        "没事，就是……\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "我听说，特别任务支援科\x01",
            "是个不被看好的部门。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        "………………………………\x02",
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

    #C0233
    ChrTalk(
        0x103,
        (
            "#0200F（艾莉前辈，她好像很\x01",
            "  担心你啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x102,
        (
            "#0106F（好、好像是吧。\x01",
            "  乔安娜就是容易担心……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_360C")

    Jump("loc_3614")

    label("loc_3611")

    Call(0, 10)

    label("loc_3614")

    TalkEnd(0xFE)
    Return()

    # Function_9_1F72 end

    def Function_10_3618(): pass

    label("Function_10_3618")

    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x102, 500)
    Sleep(500)

    #C0235
    ChrTalk(
        0x9,
        "啊……\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x9,
        "艾莉小姐……\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x102,
        (
            "#0100F乔安娜，好久不见。\x02\x03",

            "抱歉啊，\x01",
            "也没打声招呼，突然就这样回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x9,
        "……………………（紧张紧张）\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x9,
        (
            "那我马上去做饭，\x01",
            "刚刚正好在准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x9,
        (
            "……那个，您是辞去警察的工作\x01",
            "回来了吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    #C0241
    ChrTalk(
        0x9,
        "您的睡衣我洗好了，还是放在原来的地方……\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x9,
        (
            "还有还有，我每天都会将\x01",
            "您房间的床铺好，\x01",
            "您随时都可以去休息……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x102,
        (
            "#0106F那个，抱歉啊。\x01",
            "我只是来看看乔安娜你的……\x02\x03",

            "并没有辞去警察的工作。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x9)

    #C0244
    ChrTalk(
        0x9,
        (
            "这、这样啊。\x01",
            "……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x9,
        (
            "实在不好意思。\x01",
            "那个，工作请加油哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x102,
        (
            "#0100F……嗯。\x01",
            "谢谢你，乔安娜。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8D, 3)
    Return()

    # Function_10_3618 end

    def Function_11_3868(): pass

    label("Function_11_3868")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50235.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch50236.itc", 0x20)
    OP_68(45500, 1200, 48400, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, 44700, 250, 48500, 90)
    SetChrFlags(0xA, 0x20)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x514), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xA, 46100, 550, 48650, 180)
    ClearMapObjFlags(0x5, 0x4)
    ClearChrFlags(0xB, 0x80)
    OP_78(0x5, 0xB)
    OP_49()
    SetChrPos(0xB, 44500, 0, 48600, 0)
    OP_D3(0xB, 0x0, 0x0, 0x0, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0247
    AnonymousTalk(
        0x102,
        (
            "怎、怎么会……\x02\x03",

            "竟然明天就要重回工作岗位，\x01",
            "这未免也太快了……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(20000, 2500)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    #C0248
    ChrTalk(
        0xA,
        (
            "#11P#6503F说什么呢，我这只是些\x01",
            "碰伤和扭伤而已。\x02\x03",

            "#6500F休息了五天，\x01",
            "不如说反而养足了精力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x102,
        (
            "#6P#0106F请、请您别开玩笑啊！\x02\x03",

            "#0108F遇上了那么严重的事，\x01",
            "而且首席秘书也不在了……\x02\x03",

            "#0101F您现在必须得\x01",
            "好好休息！\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xA,
        (
            "#11P#6500F创立纪念庆典也临近了，\x01",
            "工作都堆积如山了。\x02\x03",

            "#6509F仅凭这种程度的小事，\x01",
            "还不足以让我放弃市长的责任。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x102,
        "#6P#0106F这种程度……\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)

    #C0252
    ChrTalk(
        0x102,
        (
            "#6P#0108F外公您……\x01",
            "不难受……不悔恨吗？\x02\x03",

            "您对阿奈斯特先生如此器重，\x01",
            "可他却背叛了您……\x02\x03",

            "为什么您还……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xA, 0x0)
    Sleep(300)

    #C0253
    ChrTalk(
        0xA,
        (
            "#5P#6503F……如果说这次的事件对我\x01",
            "没有打击，那是骗人的。\x02\x03",

            "我查了一下，他好像从很早之前开始\x01",
            "就一直偷偷挪用事务所的资金。\x02\x03",

            "最后被过大的精神压力逼得走投无路，\x01",
            "才做出了那种冲动之举。\x02\x03",

            "没能及时发现并阻止他，\x01",
            "我也有责任。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x102,
        "#6P#0105F……外公……\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xA,
        (
            "#5P#6501F──不过，我是政治家。\x02\x03",

            "我已经发誓要将这把老骨头\x01",
            "全部奉献给克洛斯贝尔自治州的现在和未来了。\x02\x03",

            "无论发生什么事，\x01",
            "我能做的也只有全力履行自己的职责。\x02\x03",

            "我一直都是这样要求自己的。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x102,
        "#6P#0108F……………………………………\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    #C0257
    ChrTalk(
        0xA,
        (
            "#11P#6503F抱歉啊，艾莉。\x02\x03",

            "十年前……\x01",
            "我同样也没能挽留住\x01",
            "你的父亲莱昂。\x02\x03",

            "#6503F而且还任凭我的女儿……你的母亲\x01",
            "就那样离家而去。\x02\x03",

            "而且，如今我仍然还是一样无能……\x01",
            "完全没有改变现状的力量，\x01",
            "却必须一直守着克洛斯贝尔市长这个职位。\x02\x03",

            "#6501F你……应该很恨我吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x102,
        (
            "#6P#0101F怎么会……！\x01",
            "外公一直都是我的骄傲！\x02\x03",

            "#0108F而且我和父亲、母亲\x01",
            "偶尔也有联系……\x02\x03",

            "#0106F虽然一度十分伤心……\x01",
            "但我已经努力从悲伤中走出来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xA,
        "#11P#6500F艾莉……\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x102,
        (
            "#6P#0103F我之所以会成为警察……\x01",
            "也是想用别的方式来\x01",
            "帮助外公。\x02\x03",

            "而且我坚信这也会对\x01",
            "克洛斯贝尔有所帮助……\x02\x03",

            "#0108F……不过，发生了那种事，\x01",
            "阿奈斯特先生也不在了……\x02\x03",

            "#0101F我、我果然还是应该辞去警察的工作，\x01",
            "回来帮外公吧──\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0261
    ChrTalk(
        0xA,
        "#11P#6507F#4S#N别说傻话！\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0262
    ChrTalk(
        0x102,
        "#6P#0105F外、外公……？\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xA,
        (
            "#11P#6501F……如果你对你所选的路\x01",
            "感到后悔，\x01",
            "的确应该马上回来。\x02\x03",

            "不过，你并没有感到过后悔吧？\x02\x03",

            "既然如此，若你还是轻易说出要改变人生道路\x01",
            "之类的话，便是对许多人的不尊重、不负责。\x02\x03",

            "#6503F对你的同事、对我，\x01",
            "……特别是对你自己。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x102,
        "#6P#0108F啊……\x02",
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xA,
        (
            "#11P#6500F你不用担心我。\x02\x03",

            "秘书又不是只有一个人，\x01",
            "而且到了紧急关头，\x01",
            "海尔玛也能帮我的。\x02\x03",

            "本打算下次市长选举时就隐退，\x01",
            "但现在变得有些困难了……\x02\x03",

            "#6509F不过没什么，只是将闲适的隐居生活\x01",
            "再推迟五年而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x102,
        "#6P#0106F………………………………\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xA,
        (
            "#11P#6503F所以……\x01",
            "你要将自己所选的道路走到底。\x02\x03",

            "至少……\x01",
            "走到你满意为止。\x02\x03",

            "#6500F这对我来说\x01",
            "就是最大的慰藉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x102,
        "#6P#0108F外公……\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xA,
        (
            "#11P#6503F而且，在这次的事件中，\x01",
            "如果没有你们的帮助，\x01",
            "我恐怕已经不在人世了吧。\x02\x03",

            "#6500F自豪吧，\x01",
            "为你们的努力与成长感到自豪吧。\x02\x03",

            "然后不断磨练自己，\x01",
            "成为更加耀眼的存在。\x02\x03",

            "#6509F就像彩虹剧团\x01",
            "这次的新剧一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x102,
        (
            "#6P#0105F啊……\x02\x03",

            "#0102F我明白了，外公……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x102, 0x4)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 44700, 0, 47600, 90)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(500)
    SetCameraDistance(19500, 800)
    Fade(500)
    SetChrSubChip(0x102, 0x1)
    Sound(804, 0, 80, 0)
    Sleep(100)
    SetChrSubChip(0x102, 0x2)
    OP_0D()
    Sleep(500)

    #C0271
    ChrTalk(
        0x102,
        (
            "#6P#0104F艾莉·麦克道尔──\x02\x03",

            "#0100F明天就重回岗位，\x01",
            "并且会更加努力……！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 1)
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_3868 end

    def Function_12_4514(): pass

    label("Function_12_4514")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x8, 0xFF)
    EndChrThread(0x8, 0x0)
    OP_68(41010, 1500, 43700, 0)
    MoveCamera(47, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21780, 0)
    SetChrPos(0x101, 41690, 60, 43300, 90)
    SetChrPos(0x102, 41690, 60, 44420, 90)
    SetChrPos(0x103, 40640, 60, 43300, 90)
    SetChrPos(0x104, 40550, 60, 44420, 90)
    SetChrPos(0x8, 37190, 60, 43820, 90)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xC, 0x80)
    OP_78(0x6, 0xC)
    OP_49()
    SetChrPos(0xC, 45500, 0, 43500, 0)
    ClearMapObjFlags(0x3, 0x4)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    OP_0D()

    #C0272
    ChrTalk(
        0x102,
        "#5P#0105F啊……！？\x02",
    )

    CloseMessageWindow()
    OP_68(43290, 1500, 44170, 2000)
    MoveCamera(54, 18, 0, 2000)

    def lambda_4639():
        OP_9B(0x0, 0xFE, 0x0, 0x4B0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4639)

    def lambda_464E():
        OP_9B(0x0, 0xFE, 0x0, 0x4B0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_464E)

    def lambda_4663():
        OP_9B(0x0, 0xFE, 0x0, 0x4B0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4663)

    def lambda_4678():
        OP_9B(0x0, 0xFE, 0x0, 0x4B0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4678)
    Sleep(2000)

    #C0273
    ChrTalk(
        0x101,
        "#12P#0011F这……这是……！？\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x104,
        "#6P#0305F喂喂，难道……\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x103,
        (
            "#12P#0200F没错，\x01",
            "这正是市政厅被盗的雕像\x01",
            "『圣徒的祈祷』吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x102,
        (
            "#6P#0105F为什么……\x01",
            "为什么会在外公的房间里！？\x02",
        )
    )

    CloseMessageWindow()

    #N0277
    NpcTalk(
        0x8,
        "男性的声音",
        "#2P小姐，发生什么事了吗？\x02",
    )

    CloseMessageWindow()
    OP_68(42240, 1500, 44090, 1800)
    MoveCamera(55, 26, 0, 1800)

    def lambda_4789():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4789)
    Sleep(12)

    def lambda_4799():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4799)

    def lambda_47A6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_47A6)
    Sleep(15)

    def lambda_47B6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_47B6)

    def lambda_47C3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_47C3)
    OP_95(0x8, 40640, 60, 43910, 1500, 0x0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0278
    ChrTalk(
        0x8,
        (
            "#6P啊，这是……！？\x01",
            "是各位搬进来的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x103,
        "#11P#0203F并非如此。\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x101,
        (
            "#11P#0001F说来话长……\x01",
            "这似乎是那个名为\x01",
            "怪盗Ｂ的盗贼所为吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x8,
        (
            "#6P怪盗Ｂ……\x01",
            "是那个有名的……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x102,
        (
            "#5P#0101F海尔玛先生，今天没有什么\x01",
            "可疑的人来家里吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x8,
        "#6P嗯，今天一个客人都没有。\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x8,
        (
            "#6P老爷今天很忙，\x01",
            "所以没有人来。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x104,
        (
            "#5P#0306F居然根本就没人目击到，\x01",
            "这到底是怎么搬进来的啊？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4972():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4972)
    Sleep(50)

    def lambda_4982():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4982)
    Sleep(50)

    def lambda_4992():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4992)
    Sleep(50)

    def lambda_49A2():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_49A2)
    Sleep(500)

    #C0286
    ChrTalk(
        0x101,
        (
            "#12P#0003F关于这个问题，\x01",
            "真是毫无头绪……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0287
    ChrTalk(
        0x101,
        (
            "#12P#0005F等一下，\x01",
            "雕像的侧面好像有张卡片……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4A29():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4A29)

    def lambda_4A36():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4A36)

    def lambda_4A43():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4A43)
    OP_95(0x101, 44380, 0, 42120, 1000, 0x0)
    OP_93(0x101, 0x2D, 0x190)
    Sleep(800)
    OP_95(0x101, 42890, 60, 43300, 1000, 0x0)

    def lambda_4A82():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4A82)

    def lambda_4A8F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4A8F)

    def lambda_4A9C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4A9C)

    def lambda_4AA9():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4AA9)
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(600)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0288
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "特别任务支援科的诸位，辛苦了。\x01",
            "多亏诸位赏光参加此次余兴节目，\x01",
            "我才能进一步享受到\x01",
            "这座虚构之城的庆典。\x01",
            "在此对诸位的勇气与努力表示敬意。\x02",
        )
    )

    CloseMessageWindow()

    #A0289
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "遗憾的是，我也有自己的立场，\x01",
            "因此，现阶段我不会再重临此地，\x01",
            "敬请安心。\x02",
        )
    )

    CloseMessageWindow()

    #A0290
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ＰＳ．昨天我那只小猫知己\x01",
            "      承蒙各位照顾了。\x01",
            "      再次对诸位的诚意表示感谢。\x01",
            "                ──怪盗Ｂ\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(500)

    #C0291
    ChrTalk(
        0x103,
        (
            "#12P#0200F看来对方\x01",
            "好像很乐在其中啊。\x01",
            "……有些不甘心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x102,
        (
            "#5P#0105F话说回来，\x01",
            "这里的『小猫知己』是指……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0293
    ChrTalk(
        0x101,
        "#12P#0001F莫非是……那只『小猫』吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0294
    ChrTalk(
        0x104,
        (
            "#6P#0305F……就是指玲吗！？\x02\x03",

            "#0301F嗯……如果假设\x01",
            "结社和怪盗Ｂ有所关联，\x01",
            "那也不是不可能……\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x101,
        (
            "#12P#0008F……不过现阶段还无法确认，\x01",
            "就先放到一边吧。\x02\x03",

            "#0006F话说回来……怪盗Ｂ这家伙，\x01",
            "还真是擅长\x01",
            "将别人耍得团团转啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x103,
        "#12P#0203F每次都这样，真让人火大。\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x102,
        (
            "#5P#0103F不过还好……\x01",
            "对方好像也没打算把\x01",
            "事情弄大。\x02\x03",

            "#0100F他应该不会再引起\x01",
            "比这更严重的事件了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x104,
        (
            "#6P#0306F虽然最后没能逮捕他……\x01",
            "不过，这次这种结局\x01",
            "已经算是不错了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        (
            "#12P#0003F也对……反正被盗的东西\x01",
            "都顺利找回来了。\x02\x03",

            "#0001F好，既然如此，那就……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4F97():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4F97)
    Sleep(50)

    def lambda_4FA7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_4FA7)
    Sleep(50)

    def lambda_4FB7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_4FB7)
    Sleep(50)

    def lambda_4FC7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_4FC7)
    Sleep(300)
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    Sleep(300)
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0300
    ChrTalk(
        0x101,
        (
            "#12P#0006F……总之，\x01",
            "先联系下市政厅的库利普先生，\x01",
            "让他找些运送员来把这个搬走吧。\x02\x03",

            "这座雕像这么大，\x01",
            "仅凭我们可搬不动。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x102,
        (
            "#6P#0106F是啊……\x01",
            "他到底是\x01",
            "怎么搬进来的呢？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c1110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_4514 end

    def Function_13_5157(): pass

    label("Function_13_5157")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0302
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "书架上有本书，书名为\x01",
            "《猫也做得到！美味蛋糕的制作方法》。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x11)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_521B")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0303
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法写在书里。\x02",
        )
    )

    CloseMessageWindow()

    #A0304
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x11)

    label("loc_521B")

    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_13_5157 end

    SaveToFile()

Try(main)
