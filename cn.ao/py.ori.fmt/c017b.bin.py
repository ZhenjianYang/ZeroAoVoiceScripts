from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c017b.bin",                # FileName
        "c017b",                    # MapName
        "c017b",                    # Location
        0x0005,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 3],
    )

    BuildStringList((
        "c017b",                  # 0
        "接待小姐帕尔",           # 1
        "接待小姐辛茜亚",         # 2
        "汉森",                   # 3
        "利乔",                   # 4
        "普拉达",                 # 5
        "贝卡",                   # 6
        "沙扎克",                 # 7
        "奈斯顿经理",             # 8
        "珍妮特",                 # 9
        "德罗缇",                 # 10
        "肯",                     # 11
        "欧奈斯特老人",           # 12
    ))

    AddCharChip((
        "chr/ch27400.itc",                   # 00
        "chr/ch26600.itc",                   # 01
        "chr/ch22000.itc",                   # 02
        "chr/ch24300.itc",                   # 03
        "chr/ch27000.itc",                   # 04
        "chr/ch20000.itc",                   # 05
        "chr/ch10400.itc",                   # 06
        "chr/ch34200.itc",                   # 07
        "chr/ch21600.itc",                   # 08
        "chr/ch34600.itc",                   # 09
        "chr/ch25900.itc",                   # 0A
        "chr/ch22100.itc",                   # 0B
        "chr/ch20500.itc",                   # 0C
    ))

    DeclNpc(7480,    0,       10079,   225,  257,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(5880,    0,       11680,   225,  257,  0x0, 0,   9,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(59,      8000,    30040,   180,  257,  0x0, 0,   10,  0,   0,   0,   0,   9,   255,  0)
    DeclNpc(15979,   0,       9520,    180,  257,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(18110,   8000,    12220,   270,  257,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-11529,  8000,    8510,    225,  257,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-15989,  0,       25739,   180,  257,  0x0, 0,   2,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-2660,   0,       9829,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-6659,   8000,    28870,   0,    257,  0x0, 0,   1,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(13800,   8000,    6199,    225,  257,  0x0, 0,   6,   0,   0,   1,   0,   20,  255,  0)
    DeclNpc(8020,    8000,    17270,   180,  257,  0x0, 0,   7,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-14449,  8000,    14420,   90,   257,  0x0, 0,   8,   0,   0,   0,   0,   22,  255,  0)

    DeclActor(6250,    0,       9040,    1000,    7480,    1500,    10080,   0x007E, 0,  4,  0x0000)
    DeclActor(4440,    0,       10280,   1000,    5880,    1500,    11680,   0x007E, 0,  6,  0x0000)
    DeclActor(-480,    8000,    28360,   1000,    60,      9500,    30040,   0x007E, 0,  8,  0x0000)
    DeclActor(15980,   0,       7760,    1000,    15980,   1500,    9520,    0x007E, 0,  10, 0x0000)
    DeclActor(16480,   8000,    11730,   1000,    18110,   9500,    12220,   0x007E, 0,  12, 0x0000)
    DeclActor(-12390,  8000,    7660,    1000,    -11530,  9500,    8510,    0x007E, 0,  14, 0x0000)
    DeclActor(-16030,  0,       23800,   1000,    -15990,  1500,    25740,   0x007E, 0,  16, 0x0000)
    DeclActor(1670,    0,       13270,   800,     1670,    1500,    13270,   0x007C, 0,  23, 0x0000)

    ChipFrameInfo(920, 0)                                        # 0

    ScpFunction((
        "Function_0_398",          # 00, 0
        "Function_1_448",          # 01, 1
        "Function_2_521",          # 02, 2
        "Function_3_54F",          # 03, 3
        "Function_4_57F",          # 04, 4
        "Function_5_583",          # 05, 5
        "Function_6_63A",          # 06, 6
        "Function_7_63E",          # 07, 7
        "Function_8_717",          # 08, 8
        "Function_9_71B",          # 09, 9
        "Function_10_98B",         # 0A, 10
        "Function_11_98F",         # 0B, 11
        "Function_12_AA3",         # 0C, 12
        "Function_13_AA7",         # 0D, 13
        "Function_14_BB8",         # 0E, 14
        "Function_15_BBC",         # 0F, 15
        "Function_16_D6F",         # 10, 16
        "Function_17_D73",         # 11, 17
        "Function_18_F20",         # 12, 18
        "Function_19_F94",         # 13, 19
        "Function_20_FD8",         # 14, 20
        "Function_21_1067",        # 15, 21
        "Function_22_10D6",        # 16, 22
        "Function_23_1121",        # 17, 23
    ))


    def Function_0_398(): pass

    label("Function_0_398")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3D0"),
        (1, "loc_3DC"),
        (2, "loc_3E8"),
        (3, "loc_3F4"),
        (4, "loc_400"),
        (5, "loc_40C"),
        (6, "loc_418"),
        (SWITCH_DEFAULT, "loc_424"),
    )


    label("loc_3D0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_3DC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_3E8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_3F4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_400")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_40C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_418")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_424")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_430")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_447")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_430")

    label("loc_447")

    Return()

    # Function_0_398 end

    def Function_1_448(): pass

    label("Function_1_448")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_520")
    OP_95(0xFE, 13800, 8000, 6200, 2000, 0x0)
    OP_95(0xFE, 14520, 8000, 20050, 2000, 0x0)
    OP_95(0xFE, 8730, 8000, 20460, 2000, 0x0)
    OP_95(0xFE, 8730, 8000, 20460, 2000, 0x0)
    OP_95(0xFE, 8530, 8000, 26610, 2000, 0x0)
    OP_95(0xFE, -14240, 8000, 26610, 2000, 0x0)
    OP_95(0xFE, -17130, 8000, 23430, 2000, 0x0)
    OP_95(0xFE, -17130, 8000, 7560, 2000, 0x0)
    OP_95(0xFE, -11380, 8000, 2990, 2000, 0x0)
    OP_95(0xFE, 14040, 8000, 2490, 2000, 0x0)
    Jump("Function_1_448")

    label("loc_520")

    Return()

    # Function_1_448 end

    def Function_2_521(): pass

    label("Function_2_521")

    SetChrPos(0x12, 8020, 8000, 17270, 90)
    SetChrPos(0x11, 9070, 8000, 17290, 270)
    BeginChrThread(0x11, 0, 0, 0)
    SetChrFlags(0x11, 0x10)
    Return()

    # Function_2_521 end

    def Function_3_54F(): pass

    label("Function_3_54F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_570")
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    Jump("loc_57E")

    label("loc_570")

    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)

    label("loc_57E")

    Return()

    # Function_3_54F end

    def Function_4_57F(): pass

    label("Function_4_57F")

    Call(0, 5)
    Return()

    # Function_4_57F end

    def Function_5_583(): pass

    label("Function_5_583")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_609")

    #C0001
    ChrTalk(
        0x8,
        (
            "今天的工作结束以后，\x01",
            "我要与辛茜亚前辈\x01",
            "和珍妮特小姐一起去吃饭。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "好久没一起吃饭聊天了，\x01",
            "呵呵，真期待啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_636")

    label("loc_609")


    #C0003
    ChrTalk(
        0x8,
        (
            "好久没一起吃饭聊天了，\x01",
            "呵呵，真期待啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_636")

    TalkEnd(0x8)
    Return()

    # Function_5_583 end

    def Function_6_63A(): pass

    label("Function_6_63A")

    Call(0, 7)
    Return()

    # Function_6_63A end

    def Function_7_63E(): pass

    label("Function_7_63E")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CB")

    #C0004
    ChrTalk(
        0x9,
        (
            "珍妮特小姐\x01",
            "今天非常兴奋，\x01",
            "莫非有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x9,
        (
            "我们又不是第一次三个人\x01",
            "聚在一起吃饭……\x01",
            "她的情绪未免也太高涨了吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_713")

    label("loc_6CB")


    #C0006
    ChrTalk(
        0x9,
        (
            "我们又不是第一次三个人\x01",
            "聚在一起吃饭……\x01",
            "她的情绪未免也太高涨了吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_713")

    TalkEnd(0x9)
    Return()

    # Function_7_63E end

    def Function_8_717(): pass

    label("Function_8_717")

    Call(0, 9)
    Return()

    # Function_8_717 end

    def Function_9_71B(): pass

    label("Function_9_71B")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_728")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_987")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_778")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_778")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_797")
    OP_AF(0x26)
    Jump("loc_7B9")

    label("loc_797")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_7A7")
    OP_AF(0x25)
    Jump("loc_7B9")

    label("loc_7A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_7B7")
    OP_AF(0x24)
    Jump("loc_7B9")

    label("loc_7B7")

    OP_AF(0x23)

    label("loc_7B9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_982")

    label("loc_7C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7DC")
    Jump("loc_982")

    label("loc_7DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_982")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D7")

    #C0007
    ChrTalk(
        0xA,
        (
            "各位知道吗？如果想选购鞋子，\x01",
            "最好等到傍晚之后。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xA,
        (
            "因为人在早晨起床后，\x01",
            "脚部会慢慢舒展开，到了傍晚时分，\x01",
            "将比清晨时大出一里矩左右。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xA,
        (
            "因此，要挑选鞋子的码数，最好还是选择\x01",
            "脚部舒展得最开的傍晚之后。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_982")

    label("loc_8D7")


    #C0010
    ChrTalk(
        0xA,
        (
            "其实，这是因为人在早晨睡醒后，\x01",
            "脚部会慢慢舒展开来，到了傍晚时分，\x01",
            "将比清晨时大出一里矩左右。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xA,
        (
            "因此，如果想买到码数合适的鞋子，\x01",
            "最好选择脚部舒展得最开的傍晚之后。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_982")

    Jump("loc_728")

    label("loc_987")

    TalkEnd(0xA)
    Return()

    # Function_9_71B end

    def Function_10_98B(): pass

    label("Function_10_98B")

    Call(0, 11)
    Return()

    # Function_10_98B end

    def Function_11_98F(): pass

    label("Function_11_98F")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_99C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9F")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9EC")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_9EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0C")
    OP_AF(0x12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A9A")

    label("loc_A0C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A20")
    Jump("loc_A9A")

    label("loc_A20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A9A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0012
    ChrTalk(
        0xB,
        (
            "您好，\x01",
            "欢迎光临『利乔食品店』。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xB,
        (
            "如果您还没有准备好\x01",
            "晚餐所需的食材，\x01",
            "就请在本店选购吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A9A")

    Jump("loc_99C")

    label("loc_A9F")

    TalkEnd(0xB)
    Return()

    # Function_11_98F end

    def Function_12_AA3(): pass

    label("Function_12_AA3")

    Call(0, 13)
    Return()

    # Function_12_AA3 end

    def Function_13_AA7(): pass

    label("Function_13_AA7")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BB4")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B04")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_B04")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B54")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_B23")
    OP_AF(0x21)
    Jump("loc_B45")

    label("loc_B23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_B33")
    OP_AF(0x20)
    Jump("loc_B45")

    label("loc_B33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_B43")
    OP_AF(0x1F)
    Jump("loc_B45")

    label("loc_B43")

    OP_AF(0x1E)

    label("loc_B45")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BAF")

    label("loc_B54")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B68")
    Jump("loc_BAF")

    label("loc_B68")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAF")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0014
    ChrTalk(
        0xC,
        (
            "欢迎光临，\x01",
            "请您尽情享受\x01",
            "晚间购物的乐趣。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BAF")

    Jump("loc_AB4")

    label("loc_BB4")

    TalkEnd(0xC)
    Return()

    # Function_13_AA7 end

    def Function_14_BB8(): pass

    label("Function_14_BB8")

    Call(0, 15)
    Return()

    # Function_14_BB8 end

    def Function_15_BBC(): pass

    label("Function_15_BBC")

    TalkBegin(0xD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6B")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C19")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_C19")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C59")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_C38")
    OP_AF(0x11)
    Jump("loc_C4A")

    label("loc_C38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C48")
    OP_AF(0x10)
    Jump("loc_C4A")

    label("loc_C48")

    OP_AF(0xF)

    label("loc_C4A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D66")

    label("loc_C59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C6D")
    Jump("loc_D66")

    label("loc_C6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D66")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D09")

    #C0015
    ChrTalk(
        0xD,
        "天色已经暗下来了呢。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xD,
        (
            "专为首脑们表演的\x01",
            "那场彩虹剧团演出\x01",
            "应该快要结束了。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xD,
        (
            "唔，希望首脑们\x01",
            "看得开心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_D66")

    label("loc_D09")


    #C0018
    ChrTalk(
        0xD,
        (
            "对了，专为首脑们表演的\x01",
            "那场彩虹剧团演出\x01",
            "应该快要结束了。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xD,
        (
            "唔，希望首脑们\x01",
            "看得开心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D66")

    Jump("loc_BC9")

    label("loc_D6B")

    TalkEnd(0xD)
    Return()

    # Function_15_BBC end

    def Function_16_D6F(): pass

    label("Function_16_D6F")

    Call(0, 17)
    Return()

    # Function_16_D6F end

    def Function_17_D73(): pass

    label("Function_17_D73")

    TalkBegin(0xE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F1C")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DD0")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_DD0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF0")
    OP_AF(0x15)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F17")

    label("loc_DF0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E04")
    Jump("loc_F17")

    label("loc_E04")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F17")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ECC")

    #C0020
    ChrTalk(
        0xE,
        (
            "珍妮特从今天早上开始\x01",
            "就非常兴奋。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xE,
        (
            "而且总是说一些让人\x01",
            "听不懂的话，比如『明天我就要\x01",
            "变成超级珍妮特了』之类的……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xE,
        "不知为什么，我心里非常在意呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_F17")

    label("loc_ECC")


    #C0023
    ChrTalk(
        0xE,
        (
            "珍妮特从今天早上开始\x01",
            "就非常兴奋。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xE,
        "不知为什么，我心里非常在意呢。\x02",
    )

    CloseMessageWindow()

    label("loc_F17")

    Jump("loc_D80")

    label("loc_F1C")

    TalkEnd(0xE)
    Return()

    # Function_17_D73 end

    def Function_18_F20(): pass

    label("Function_18_F20")

    TalkBegin(0xFE)

    #C0025
    ChrTalk(
        0xFE,
        (
            "本店今天将一如往常，\x01",
            "在２０：００准时\x01",
            "结束营业。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "请各位顾客多加注意，\x01",
            "以免漏买商品或遗落随身物品。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_F20 end

    def Function_19_F94(): pass

    label("Function_19_F94")

    TalkBegin(0xFE)

    #C0027
    ChrTalk(
        0xFE,
        (
            "服装合体，\x01",
            "妆容完美。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        "呵呵呵，今晚的我别具一格哦⊥\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_19_F94 end

    def Function_20_FD8(): pass

    label("Function_20_FD8")

    TalkBegin(0xFE)

    #C0029
    ChrTalk(
        0xFE,
        "听好了哦，肯。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "回家之后，要立刻对爸爸说对不起，\x01",
            "接着就紧紧抱住他。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "不用担心，只要我们两人一起夹击他，\x01",
            "就没什么好怕的了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_FD8 end

    def Function_21_1067(): pass

    label("Function_21_1067")

    TalkBegin(0xFE)

    #C0032
    ChrTalk(
        0xFE,
        (
            "妈妈在购物时太过投入了，\x01",
            "不知不觉拖到了这个时间……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "就算是好脾气的爸爸，\x01",
            "这次大概也要生气了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_1067 end

    def Function_22_10D6(): pass

    label("Function_22_10D6")

    TalkBegin(0xFE)

    #C0034
    ChrTalk(
        0xFE,
        "好，差不多也该动身回家了。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        "要是惹恼了老婆子，可就糟糕啦。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_10D6 end

    def Function_23_1121(): pass

    label("Function_23_1121")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "２Ｆ　『卢卡』时装店\x01",
            "２Ｆ　『汉森』鞋店\x01",
            "２Ｆ　『贝卡』饰品店\x01",
            "１Ｆ　『利乔』食品店\x01",
            "１Ｆ　『沙扎克』杂货柜台\x02",
        )
    )

    CloseMessageWindow()

    #A0037
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※若有不明之处，\x01",
            "　敬请随时咨询\x01",
            "  正门综合服务台。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_23_1121 end

    SaveToFile()

Try(main)
