from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c017c.bin",                # FileName
        "c017c",                    # MapName
        "c017c",                    # Location
        0x0005,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 5, 0, 2, 0, 3],
    )

    BuildStringList((
        "c017c",                  # 0
        "接待小姐帕尔",           # 1
        "接待小姐辛茜亚",         # 2
        "汉森",                   # 3
        "利乔",                   # 4
        "普拉达",                 # 5
        "贝卡",                   # 6
        "沙扎克",                 # 7
        "达德利搜查官",           # 8
        "奈斯顿经理",             # 9
        "珍妮特",                 # 10
        "巴乔",                   # 11
        "德罗缇",                 # 12
        "肯",                     # 13
        "欧奈斯特老人",           # 14
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
        "chr/ch20400.itc",                   # 08
        "chr/ch21600.itc",                   # 09
        "chr/ch00900.itc",                   # 0A
        "chr/ch34600.itc",                   # 0B
        "chr/ch25900.itc",                   # 0C
    ))

    DeclNpc(7480,    0,       10079,   225,  257,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(5880,    0,       11680,   225,  257,  0x0, 0,   11,  0,   0,   0,   0,   7,   255,  0)
    DeclNpc(59,      8000,    30040,   180,  257,  0x0, 0,   12,  0,   0,   0,   0,   9,   255,  0)
    DeclNpc(15979,   0,       9520,    180,  257,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(18110,   8000,    12220,   270,  257,  0x0, 0,   4,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-11529,  8000,    8510,    225,  257,  0x0, 0,   5,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-15989,  0,       25739,   180,  257,  0x0, 0,   2,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-5250,   8000,    5360,    360,  385,  0x0, 0,   10,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-2660,   0,       9829,    180,  257,  0x0, 0,   0,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(-6659,   8000,    28870,   0,    257,  0x0, 0,   1,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(14930,   0,       2589,    90,   257,  0x0, 0,   8,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(13800,   8000,    6199,    225,  257,  0x0, 0,   6,   0,   0,   1,   0,   22,  255,  0)
    DeclNpc(8020,    8000,    17270,   180,  257,  0x0, 0,   7,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-14449,  8000,    14420,   90,   257,  0x0, 0,   9,   0,   0,   0,   0,   24,  255,  0)

    DeclActor(6250,    0,       9040,    1000,    7480,    1500,    10080,   0x007E, 0,  4,  0x0000)
    DeclActor(4440,    0,       10280,   1000,    5880,    1500,    11680,   0x007E, 0,  6,  0x0000)
    DeclActor(-480,    8000,    28360,   1000,    60,      9500,    30040,   0x007E, 0,  8,  0x0000)
    DeclActor(15980,   0,       7760,    1000,    15980,   1500,    9520,    0x007E, 0,  10, 0x0000)
    DeclActor(16480,   8000,    11730,   1000,    18110,   9500,    12220,   0x007E, 0,  12, 0x0000)
    DeclActor(-12390,  8000,    7660,    1000,    -11530,  9500,    8510,    0x007E, 0,  14, 0x0000)
    DeclActor(-16030,  0,       23800,   1000,    -15990,  1500,    25740,   0x007E, 0,  16, 0x0000)
    DeclActor(1670,    0,       13270,   800,     1670,    1500,    13270,   0x007C, 0,  26, 0x0000)

    ScpFunction((
        "Function_0_3E0",          # 00, 0
        "Function_1_498",          # 01, 1
        "Function_2_571",          # 02, 2
        "Function_3_60F",          # 03, 3
        "Function_4_63F",          # 04, 4
        "Function_5_643",          # 05, 5
        "Function_6_D1E",          # 06, 6
        "Function_7_D22",          # 07, 7
        "Function_8_14C8",         # 08, 8
        "Function_9_14CC",         # 09, 9
        "Function_10_19AD",        # 0A, 10
        "Function_11_19B1",        # 0B, 11
        "Function_12_1D6F",        # 0C, 12
        "Function_13_1D73",        # 0D, 13
        "Function_14_21E1",        # 0E, 14
        "Function_15_21E5",        # 0F, 15
        "Function_16_28AE",        # 10, 16
        "Function_17_28B2",        # 11, 17
        "Function_18_2DAF",        # 12, 18
        "Function_19_30F7",        # 13, 19
        "Function_20_38C4",        # 14, 20
        "Function_21_3C4B",        # 15, 21
        "Function_22_3FB4",        # 16, 22
        "Function_23_4228",        # 17, 23
        "Function_24_4694",        # 18, 24
        "Function_25_492E",        # 19, 25
        "Function_26_49C1",        # 1A, 26
        "Function_27_4A95",        # 1B, 27
    ))


    def Function_0_3E0(): pass

    label("Function_0_3E0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_420"),
        (1, "loc_42C"),
        (2, "loc_438"),
        (3, "loc_444"),
        (4, "loc_450"),
        (5, "loc_45C"),
        (6, "loc_468"),
        (SWITCH_DEFAULT, "loc_474"),
    )


    label("loc_420")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_42C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_438")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_444")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_450")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_45C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_468")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_474")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_480")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_497")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_480")

    label("loc_497")

    Return()

    # Function_0_3E0 end

    def Function_1_498(): pass

    label("Function_1_498")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_570")
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
    Jump("Function_1_498")

    label("loc_570")

    Return()

    # Function_1_498 end

    def Function_2_571(): pass

    label("Function_2_571")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_590")
    SetChrPos(0x12, -14920, 0, 10470, 0)
    Jump("loc_5F8")

    label("loc_590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_59E")
    Jump("loc_5F8")

    label("loc_59E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5AC")
    Jump("loc_5F8")

    label("loc_5AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_5CB")
    SetChrPos(0x12, -14920, 0, 10470, 0)
    Jump("loc_5F8")

    label("loc_5CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_5EA")
    SetChrPos(0x12, -14920, 0, 10470, 0)
    Jump("loc_5F8")

    label("loc_5EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_5F8")
    ClearChrFlags(0xF, 0x80)

    label("loc_5F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60E")
    SetMapFlags(0x10000000)
    Event(0, 27)

    label("loc_60E")

    Return()

    # Function_2_571 end

    def Function_3_60F(): pass

    label("Function_3_60F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_630")
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    Jump("loc_63E")

    label("loc_630")

    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)

    label("loc_63E")

    Return()

    # Function_3_60F end

    def Function_4_63F(): pass

    label("Function_4_63F")

    Call(0, 5)
    Return()

    # Function_4_63F end

    def Function_5_643(): pass

    label("Function_5_643")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_683")

    #C0001
    ChrTalk(
        0x8,
        (
            "斯克特下周\x01",
            "好像又要出差呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        "……唉。\x02",
    )

    CloseMessageWindow()
    Jump("loc_D1A")

    label("loc_683")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_790")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72B")
    OP_4B(0x9, 0xFF)

    #C0003
    ChrTalk(
        0x8,
        (
            "……看到前辈\x01",
            "叹气的瞬间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "嗯～像前辈这种成熟的女性，\x01",
            "果然是性感非常啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    #C0005
    ChrTalk(
        0x9,
        (
            "对、对客人说什么呢，\x01",
            "帕尔……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x0)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_78B")

    label("loc_72B")


    #C0006
    ChrTalk(
        0x8,
        (
            "像前辈这种成熟的女性，\x01",
            "哪怕只是叹口气，\x01",
            "也都性感非常啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        "为什么男人们不来追求前辈呢～\x02",
    )

    CloseMessageWindow()

    label("loc_78B")

    Jump("loc_D1A")

    label("loc_790")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_A1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CA")
    OP_4B(0x9, 0xFF)

    #C0008
    ChrTalk(
        0x101,
        (
            "#0001F（嗯，她们两位\x01",
            "  可能知道些什么吧……）\x02",
        )
    )

    CloseMessageWindow()

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德出示了柯林的照片，\x01",
            "并询问对方是否有什么线索。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0010
    ChrTalk(
        0x8,
        "是走失的孩子吗……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x0, 500)

    #C0011
    ChrTalk(
        0x9,
        (
            "哎呀，走失的孩子啊……\x01",
            "那可真令人担心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x9,
        (
            "可是我好像\x01",
            "没有什么头绪呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8A5():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_8A5)

    def lambda_8B2():
        TurnDirection(0x9, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_8B2)
    WaitChrThread(0x8, 2)

    #C0013
    ChrTalk(
        0x9,
        "帕尔，你见过吗？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "嗯……我好像\x01",
            "也没有印象。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "游行队伍经过的时候，\x01",
            "是有好几个小孩子……\x01",
            "不过他们都有父母带着。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_93E():
        TurnDirection(0x8, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_93E)

    def lambda_94B():
        TurnDirection(0x9, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_94B)
    WaitChrThread(0x8, 2)

    #C0016
    ChrTalk(
        0x9,
        (
            "对不起，\x01",
            "我想这孩子应该\x01",
            "没来过我们百货店。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#0000F是吗……\x01",
            "谢谢你们了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)
    OP_93(0x9, 0xE1, 0x0)
    OP_4C(0x9, 0xFF)
    Jump("loc_A1A")

    label("loc_9CA")


    #C0018
    ChrTalk(
        0x8,
        (
            "来我们百货店的孩子们\x01",
            "应该都有父母带着。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "好像没看见\x01",
            "你们在找的孩子哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A1A")

    Jump("loc_D1A")

    label("loc_A1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_B2C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AC7")
    OP_4B(0x9, 0xFF)

    #C0020
    ChrTalk(
        0x8,
        (
            "……看到前辈\x01",
            "叹气的瞬间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "嗯～像前辈这种成熟的女性，\x01",
            "果然是性感非常啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    #C0022
    ChrTalk(
        0x9,
        (
            "对、对客人说什么呢，\x01",
            "帕尔……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x0)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_B27")

    label("loc_AC7")


    #C0023
    ChrTalk(
        0x8,
        (
            "像前辈这种成熟的女性，\x01",
            "哪怕只是叹口气，\x01",
            "也都性感非常啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        "为什么男人们不来追求前辈呢～\x02",
    )

    CloseMessageWindow()

    label("loc_B27")

    Jump("loc_D1A")

    label("loc_B2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_BC6")

    #C0025
    ChrTalk(
        0x8,
        (
            "经理的那些企划，\x01",
            "对员工来说，\x01",
            "有不少实施起来都比较有难度。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "即使如此，大家也都会追随他，\x01",
            "因为大家都确信经理的企划\x01",
            "一定会有效果的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D1A")

    label("loc_BC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_C1E")

    #C0027
    ChrTalk(
        0x8,
        (
            "昨天有孩子走丢了，\x01",
            "真是不得了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "人一多，果然\x01",
            "就容易出事呀……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D1A")

    label("loc_C1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_C95")

    #C0029
    ChrTalk(
        0x8,
        (
            "前辈是很受女孩子\x01",
            "憧憬的类型，\x01",
            "所以有很多女性朋友呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "……但也很想听听\x01",
            "她与男人之间的绯闻啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D1A")

    label("loc_C95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_D1A")

    #C0031
    ChrTalk(
        0x8,
        (
            "我以前和斯克特\x01",
            "在米修拉姆约会的时候，\x01",
            "也曾见到过咪西。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "咪西可是\x01",
            "十分可爱的哦。\x01",
            "呵呵，有机会的话，你们也去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1A")

    TalkEnd(0x8)
    Return()

    # Function_5_643 end

    def Function_6_D1E(): pass

    label("Function_6_D1E")

    Call(0, 7)
    Return()

    # Function_6_D1E end

    def Function_7_D22(): pass

    label("Function_7_D22")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_D9A")

    #C0033
    ChrTalk(
        0x9,
        "欢迎光临『时代』百货店。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x9,
        "本日营业到晚上二十三时为止。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        (
            "请不必着急，\x01",
            "尽情享受购物时光吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14C4")

    label("loc_D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_EA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E30")

    #C0036
    ChrTalk(
        0x9,
        "唉……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x9,
        (
            "哎呀，真是失礼了。\x01",
            "竟然在顾客的面前叹气，\x01",
            "难道是我太累了吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x9,
        (
            "这种时候，真想去\x01",
            "慢跑一下，放松放松啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_E9B")

    label("loc_E30")


    #C0039
    ChrTalk(
        0x9,
        (
            "纪念庆典结束之后，要是有休假，\x01",
            "就绕着市内\x01",
            "慢跑一周吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x9,
        (
            "假日就应该这样度过呢，\x01",
            "而且我又是单身……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E9B")

    Jump("loc_14C4")

    label("loc_EA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_10D0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1083")
    OP_4B(0x8, 0xFF)

    #C0041
    ChrTalk(
        0x101,
        (
            "#0001F（嗯，她们两位\x01",
            "  可能知道些什么吧……）\x02",
        )
    )

    CloseMessageWindow()

    #A0042
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德出示了柯林的照片，\x01",
            "并询问对方是否有什么线索。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0043
    ChrTalk(
        0x9,
        (
            "哎呀，走失的孩子……\x01",
            "那可真令人担心呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F5C():
        TurnDirection(0x8, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_F5C)

    def lambda_F69():
        TurnDirection(0x9, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_F69)
    WaitChrThread(0x8, 2)

    #C0044
    ChrTalk(
        0x9,
        "帕尔，你见过吗？\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "嗯……我好像\x01",
            "也没有印象。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "游行队伍经过的时候，\x01",
            "是有好几个小孩子……\x01",
            "不过他们都有父母带着。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FF5():
        TurnDirection(0x8, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_FF5)

    def lambda_1002():
        TurnDirection(0x9, 0x0, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1002)
    WaitChrThread(0x8, 2)

    #C0047
    ChrTalk(
        0x9,
        (
            "十分抱歉，\x01",
            "我想这孩子应该\x01",
            "没来过我们百货店。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#0000F是吗……\x01",
            "谢谢你们了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 6)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)
    OP_93(0x8, 0xE1, 0x0)
    OP_4C(0x8, 0xFF)
    Jump("loc_10CB")

    label("loc_1083")


    #C0049
    ChrTalk(
        0x9,
        "我也没印象呢……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        (
            "十分抱歉，\x01",
            "我想这孩子应该\x01",
            "没来过我们百货店。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10CB")

    Jump("loc_14C4")

    label("loc_10D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_11D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1166")

    #C0051
    ChrTalk(
        0x9,
        "唉……\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x9,
        (
            "哎呀，真是失礼了。\x01",
            "竟然在顾客的面前叹气，\x01",
            "难道是我太累了吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x9,
        (
            "这种时候，真想去\x01",
            "慢跑一下，放松放松啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_11D1")

    label("loc_1166")


    #C0054
    ChrTalk(
        0x9,
        (
            "纪念庆典结束之后，要是有休假，\x01",
            "就绕着市内\x01",
            "慢跑一周吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x9,
        (
            "假日就应该这样度过呢，\x01",
            "而且我又是单身……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D1")

    Jump("loc_14C4")

    label("loc_11D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_125F")

    #C0056
    ChrTalk(
        0x9,
        (
            "为了迎接纪念庆典的最终日，\x01",
            "经理准备了新的企划。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x9,
        (
            "经理的企划创意新颖，\x01",
            "总是很受顾客支持。\x01",
            "这次一定也很值得期待哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14C4")

    label("loc_125F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_12E0")

    #C0058
    ChrTalk(
        0x9,
        (
            "旅行中如果缺少什么用品，\x01",
            "请务必来本店选购。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x9,
        (
            "百货店『时代』\x01",
            "一定会备齐顾客们所需要的商品，\x01",
            "恭候您的光临。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14C4")

    label("loc_12E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_145F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13BA")

    #C0060
    ChrTalk(
        0x9,
        (
            "不久前来到克洛斯贝尔的\x01",
            "游击士艾丝蒂尔小姐……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "她似乎也是斯托雷加公司\x01",
            "运动鞋的铁杆支持者哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x9,
        (
            "我也很喜欢慢跑，\x01",
            "所以也爱购买运动鞋呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "呵呵，我竟然\x01",
            "会和顾客\x01",
            "如此意气相投。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_145A")

    label("loc_13BA")


    #C0064
    ChrTalk(
        0x9,
        (
            "游击士艾丝蒂尔小姐\x01",
            "好像也是斯托雷加公司的支持者，\x01",
            "我和她真是意气相投。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "虽然我很注意不要公私混淆……\x01",
            "呵呵，但能遇到兴趣相投的人，\x01",
            "实在是很令人高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_145A")

    Jump("loc_14C4")

    label("loc_145F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_14C4")

    #C0066
    ChrTalk(
        0x9,
        (
            "在昨天的活动中，\x01",
            "有许多顾客\x01",
            "都是全家人一起来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x9,
        (
            "咪西的登场\x01",
            "让孩子们\x01",
            "兴奋不已呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14C4")

    TalkEnd(0x9)
    Return()

    # Function_7_D22 end

    def Function_8_14C8(): pass

    label("Function_8_14C8")

    Call(0, 9)
    Return()

    # Function_8_14C8 end

    def Function_9_14CC(): pass

    label("Function_9_14CC")

    TalkBegin(0xA)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19A9")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1529")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1529")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1559")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1548")
    OP_AF(0x22)
    Jump("loc_154A")

    label("loc_1548")

    OP_AF(0x21)

    label("loc_154A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_19A4")

    label("loc_1559")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_156D")
    Jump("loc_19A4")

    label("loc_156D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19A4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1605")

    #C0068
    ChrTalk(
        0xA,
        (
            "我完全忘记\x01",
            "普拉达小姐说要跟我\x01",
            "进行销售比赛的事情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xA,
        (
            "哎呀呀，一专心做生意，\x01",
            "胜败什么的就都无所谓了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A4")

    label("loc_1605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1672")

    #C0070
    ChrTalk(
        0xA,
        (
            "高跟鞋是更能\x01",
            "突出女人味的鞋子。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xA,
        (
            "虽然不适合运动，\x01",
            "但在社交宴会等场合中\x01",
            "可是必备的哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A4")

    label("loc_1672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1746")

    #C0072
    ChrTalk(
        0xA,
        (
            "斯托雷加公司制造的鞋子\x01",
            "在运动鞋爱好者之中十分受欢迎。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xA,
        (
            "兼具运动性和时尚感，\x01",
            "既结实又耐磨，\x01",
            "如此受欢迎，也是理所当然的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xA,
        (
            "顺便一提，游击士艾丝蒂尔小姐\x01",
            "似乎也是斯托雷加公司的支持者哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A4")

    label("loc_1746")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_17DC")

    #C0075
    ChrTalk(
        0xA,
        (
            "我发现有些人，\x01",
            "一到了克洛斯贝尔，\x01",
            "就会购买方便活动的凉鞋。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xA,
        (
            "我们这里销售的鞋，\x01",
            "几乎都很适合在克洛斯贝尔行走，\x01",
            "所以推荐购买哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A4")

    label("loc_17DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1869")

    #C0077
    ChrTalk(
        0xA,
        (
            "在休息之类的时间，\x01",
            "辛茜亚小姐偶尔会上来\x01",
            "看看慢跑鞋。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xA,
        (
            "对年轻女性来说，慢跑是非常有利于\x01",
            "健康的运动哦，多跑跑很不错的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19A4")

    label("loc_1869")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_19A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1933")

    #C0079
    ChrTalk(
        0xA,
        (
            "普拉达小姐\x01",
            "说要和我在纪念庆典期间\x01",
            "进行销售比赛呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xA,
        (
            "说是和平时的销量比较，\x01",
            "看看能增加百分之几。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xA,
        (
            "在个体经营时代，\x01",
            "我和普拉达小姐经常这样竞争，\x01",
            "借此来互相提高呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_19A4")

    label("loc_1933")


    #C0082
    ChrTalk(
        0xA,
        (
            "普拉达小姐\x01",
            "说要和我在纪念庆典期间\x01",
            "进行销售比赛呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xA,
        (
            "我当然要接受了。\x01",
            "呵呵，令人回想起了个体经营时代呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19A4")

    Jump("loc_14D9")

    label("loc_19A9")

    TalkEnd(0xA)
    Return()

    # Function_9_14CC end

    def Function_10_19AD(): pass

    label("Function_10_19AD")

    Call(0, 11)
    Return()

    # Function_10_19AD end

    def Function_11_19B1(): pass

    label("Function_11_19B1")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_19BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D6B")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A0E")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1A0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A2E")
    OP_AF(0x12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1D66")

    label("loc_1A2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A42")
    Jump("loc_1D66")

    label("loc_1A42")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D66")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1AA9")

    #C0084
    ChrTalk(
        0xB,
        (
            "好，今天也要\x01",
            "鼓足干劲哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xB,
        (
            "要向女儿认输\x01",
            "还为时过早呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D66")

    label("loc_1AA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1AEE")

    #C0086
    ChrTalk(
        0xB,
        "欢迎光临～！\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xB,
        (
            "哎呀呀，一下子\x01",
            "多了好多顾客呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D66")

    label("loc_1AEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1B75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B3E")

    #C0088
    ChrTalk(
        0xB,
        (
            "珍妮特今天\x01",
            "好像心不在焉的。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xB,
        "在干什么呢……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1B70")

    label("loc_1B3E")


    #C0090
    ChrTalk(
        0xB,
        (
            "珍妮特真是个\x01",
            "奇怪的女孩啊，\x01",
            "时常会担心她呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B70")

    Jump("loc_1D66")

    label("loc_1B75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_1C57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BF5")

    #C0091
    ChrTalk(
        0xB,
        (
            "刚才的顾客，\x01",
            "竟然买了\x01",
            "半打葡萄酒回去呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xB,
        (
            "呼……虽说是为了庆祝庆典，\x01",
            "但会不会喝得太多了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1C52")

    label("loc_1BF5")


    #C0093
    ChrTalk(
        0xB,
        (
            "因为要庆祝庆典，\x01",
            "大家都买了\x01",
            "好多酒回去。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xB,
        (
            "呼，会不会喝得太多了呢……\x01",
            "真令人担心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C52")

    Jump("loc_1D66")

    label("loc_1C57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1CB7")

    #C0095
    ChrTalk(
        0xB,
        (
            "这种什锦果篮\x01",
            "很适合在家庭聚会中分享哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xB,
        (
            "欢迎欢迎，请您\x01",
            "瞧一瞧、看一看～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D66")

    label("loc_1CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1D66")

    #C0097
    ChrTalk(
        0xB,
        (
            "欢迎来到『利乔食品店』\x01",
            "柜台～\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xB,
        (
            "这种帝国产的熏肉\x01",
            "最适合做火腿三明治哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xB,
        (
            "加上阿尔摩利卡产的生菜，\x01",
            "就能做出爽口的三明治。\x01",
            "要不要做来当纪念庆典的便餐呢～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D66")

    Jump("loc_19BE")

    label("loc_1D6B")

    TalkEnd(0xB)
    Return()

    # Function_11_19B1 end

    def Function_12_1D6F(): pass

    label("Function_12_1D6F")

    Call(0, 13)
    Return()

    # Function_12_1D6F end

    def Function_13_1D73(): pass

    label("Function_13_1D73")

    TalkBegin(0xC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21DD")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DD0")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1DD0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1DEF")
    OP_AF(0x1F)
    Jump("loc_1DF1")

    label("loc_1DEF")

    OP_AF(0x1E)

    label("loc_1DF1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_21D8")

    label("loc_1E00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E14")
    Jump("loc_21D8")

    label("loc_1E14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21D8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1F16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EA4")

    #C0100
    ChrTalk(
        0xC,
        (
            "汉森先生真是的，\x01",
            "把销售比赛的事情\x01",
            "忘得一干二净了。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xC,
        "唉，他从前就是个我行我素的人。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1F11")

    label("loc_1EA4")


    #C0102
    ChrTalk(
        0xC,
        (
            "不过，嗯……即便\x01",
            "只是形式上的比赛，\x01",
            "也还是让我觉得很开心呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xC,
        (
            "这都要感谢愿意接受比赛的\x01",
            "汉森先生呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F11")

    Jump("loc_21D8")

    label("loc_1F16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1F97")

    #C0104
    ChrTalk(
        0xC,
        (
            "克洛斯贝尔的顾客们，\x01",
            "大多都有很不错的\x01",
            "品位呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xC,
        (
            "我得不断引进最时尚的流行服饰，\x01",
            "时常给客人们新鲜感才行呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D8")

    label("loc_1F97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_203B")

    #C0106
    ChrTalk(
        0xC,
        (
            "我实在不太喜欢\x01",
            "帝国富裕阶层的服装。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xC,
        (
            "虽然品质一流，华丽气派，\x01",
            "但总是给人一种\x01",
            "千篇一律的感觉。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xC,
        (
            "我还是希望制造商\x01",
            "能多少追求一下原创性呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D8")

    label("loc_203B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_20C9")

    #C0109
    ChrTalk(
        0xC,
        (
            "所谓时尚，\x01",
            "并不是只要穿上\x01",
            "高价的服饰就好。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xC,
        (
            "重要的是整体的和谐……\x01",
            "也就是平衡感。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xC,
        (
            "呵呵，客人您似乎\x01",
            "很明白这点呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D8")

    label("loc_20C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2139")

    #C0112
    ChrTalk(
        0xC,
        (
            "外国顾客的服饰，\x01",
            "大多都个性鲜明呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xC,
        (
            "身为时装店的经营者，\x01",
            "从顾客身上也能学到不少东西呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21D8")

    label("loc_2139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_21D8")

    #C0114
    ChrTalk(
        0xC,
        (
            "和汉森先生的销售比赛，\x01",
            "真是十分开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xC,
        (
            "仔细想来，汉森先生\x01",
            "开时装店的时候，\x01",
            "我一直也没赢过他……\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xC,
        (
            "错失胜利的屈辱，\x01",
            "这次一定要全数奉还。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21D8")

    Jump("loc_1D80")

    label("loc_21DD")

    TalkEnd(0xC)
    Return()

    # Function_13_1D73 end

    def Function_14_21E1(): pass

    label("Function_14_21E1")

    Call(0, 15)
    Return()

    # Function_14_21E1 end

    def Function_15_21E5(): pass

    label("Function_15_21E5")

    TalkBegin(0xD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_21F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28AA")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2242")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2242")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2272")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2261")
    OP_AF(0x25)
    Jump("loc_2263")

    label("loc_2261")

    OP_AF(0x24)

    label("loc_2263")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_28A5")

    label("loc_2272")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2286")
    Jump("loc_28A5")

    label("loc_2286")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28A5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_23E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2370")

    #C0117
    ChrTalk(
        0xD,
        (
            "纪念庆典的最终日是个特别的日子，\x01",
            "似乎有很多人都想借此机会\x01",
            "表白心意呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xD,
        (
            "准备了价值三个月工资的戒指，\x01",
            "等待求婚机会的男性……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xD,
        (
            "无论时代如何变化，\x01",
            "这个风俗也都不会改变吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_23DC")

    label("loc_2370")


    #C0120
    ChrTalk(
        0xD,
        (
            "准备了价值三个月工资的戒指，\x01",
            "等待求婚机会的男性……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xD,
        (
            "虽然是上一代人的风俗，\x01",
            "不过到底也是件好事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23DC")

    Jump("loc_28A5")

    label("loc_23E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2557")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24C9")

    #C0122
    ChrTalk(
        0xD,
        (
            "以前，人称『怪盗Ｂ』的盗贼\x01",
            "出现在帝国时，有些轻率的人甚至\x01",
            "发出了支持他的呼声。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xD,
        (
            "听说，一部分狂热的崇拜者\x01",
            "最后还将支持怪盗的留言\x01",
            "送去了通讯社。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xD,
        (
            "对身为盗窃对象的宝石商来说，\x01",
            "这可不是闹着玩的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2552")

    label("loc_24C9")


    #C0125
    ChrTalk(
        0xD,
        (
            "以前，人称『怪盗Ｂ』的盗贼\x01",
            "出现在帝国时，有些轻率的人甚至\x01",
            "发出了支持他的呼声。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xD,
        (
            "将区区盗贼视作英雄的心情，\x01",
            "我实在是难以理解呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2552")

    Jump("loc_28A5")

    label("loc_2557")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_26D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_263B")

    #C0127
    ChrTalk(
        0xD,
        (
            "你们知道一个名为\x01",
            "『怪盗Ｂ』的奇怪人物吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xD,
        (
            "他以前经常在帝国作案，\x01",
            "只偷盗有隐情的美术品，\x01",
            "是个有些奇怪的盗贼。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xD,
        (
            "我以前当美术品销售商的时候，\x01",
            "朋友也曾遭窃过。\x01",
            "哎呀呀，还真是会给人添麻烦啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_26D2")

    label("loc_263B")


    #C0130
    ChrTalk(
        0xD,
        (
            "名为『怪盗Ｂ』的奇怪人物……\x01",
            "有传闻说，从两年前开始，在利贝尔就有人\x01",
            "声称目击过遭他盗窃的受害现场。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xD,
        (
            "……说不定，他也会来\x01",
            "我们克洛斯贝尔市呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26D2")

    Jump("loc_28A5")

    label("loc_26D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2772")

    #C0132
    ChrTalk(
        0xD,
        (
            "最近的克洛斯贝尔时代周刊，\x01",
            "该说感觉刊登了很多花边新闻吗……\x01",
            "怎么说呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xD,
        (
            "……但即使如此，还是让人忍不住要看，\x01",
            "果然是有某种魅力吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28A5")

    label("loc_2772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_27D9")

    #C0134
    ChrTalk(
        0xD,
        "听说有人在旧城区那边大闹了一场啊。\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xD,
        (
            "哎呀呀，也不考虑一下\x01",
            "会给居民造成多少麻烦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28A5")

    label("loc_27D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_28A5")

    #C0136
    ChrTalk(
        0xD,
        (
            "每年的这个时期，\x01",
            "销量都会骤然上升呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xD,
        (
            "本店出售的装饰品中\x01",
            "有不少价格不菲的高档货，\x01",
            "但大家的消费热情却丝毫都不受影响呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xD,
        (
            "卖得多虽然是好事，\x01",
            "但若是头脑发热，奢侈浪费，\x01",
            "我可不赞成呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28A5")

    Jump("loc_21F2")

    label("loc_28AA")

    TalkEnd(0xD)
    Return()

    # Function_15_21E5 end

    def Function_16_28AE(): pass

    label("Function_16_28AE")

    Call(0, 17)
    Return()

    # Function_16_28AE end

    def Function_17_28B2(): pass

    label("Function_17_28B2")

    TalkBegin(0xE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DAB")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_290F")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_290F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_299F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_292E")
    OP_AF(0x1B)
    Jump("loc_2990")

    label("loc_292E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_293E")
    OP_AF(0x1A)
    Jump("loc_2990")

    label("loc_293E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_294E")
    OP_AF(0x19)
    Jump("loc_2990")

    label("loc_294E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_295E")
    OP_AF(0x18)
    Jump("loc_2990")

    label("loc_295E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_296E")
    OP_AF(0x17)
    Jump("loc_2990")

    label("loc_296E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_297E")
    OP_AF(0x16)
    Jump("loc_2990")

    label("loc_297E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_298E")
    OP_AF(0x15)
    Jump("loc_2990")

    label("loc_298E")

    OP_AF(0x14)

    label("loc_2990")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2DA6")

    label("loc_299F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29B3")
    Jump("loc_2DA6")

    label("loc_29B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2DA6")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2A75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A27")

    #C0139
    ChrTalk(
        0xE,
        (
            "哟，今早\x01",
            "有新书到货哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xE,
        (
            "存货不多，\x01",
            "想买的话请趁早哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2A70")

    label("loc_2A27")


    #C0141
    ChrTalk(
        0xE,
        "这本书很受欢迎呢。\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xE,
        (
            "白天就有可能卖完，\x01",
            "要购买的话，还请趁早哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A70")

    Jump("loc_2DA6")

    label("loc_2A75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2AD8")

    #C0143
    ChrTalk(
        0xE,
        (
            "在纪念庆典期间，\x01",
            "有不少人都站在书架前，白看个没完。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xE,
        "唉，就不能买几本吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DA6")

    label("loc_2AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2BD3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B62")

    #C0145
    ChrTalk(
        0xE,
        (
            "克洛斯贝尔时代周刊\x01",
            "似乎在纪念庆典的最终日\x01",
            "也会坚持出版呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xE,
        (
            "嗯～记者们也很努力啊，\x01",
            "连我都深感佩服呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2BCE")

    label("loc_2B62")


    #C0147
    ChrTalk(
        0xE,
        (
            "克洛斯贝尔时代周刊似乎\x01",
            "要在纪念庆典的最终日出版最新一期。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xE,
        (
            "如果你们也是忠实读者，\x01",
            "最好留意一下哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BCE")

    Jump("loc_2DA6")

    label("loc_2BD3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_2C52")

    #C0149
    ChrTalk(
        0xE,
        (
            "欢迎光临，\x01",
            "有什么要买的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xE,
        (
            "药品之类的东西，\x01",
            "最好要常备一些哦。\x01",
            "人生莫测，不知何时就会发生什么意外的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DA6")

    label("loc_2C52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2D3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CCF")

    #C0151
    ChrTalk(
        0xE,
        (
            "这里从昨天开始出售\x01",
            "克洛斯贝尔的地图和巴士时刻表了。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xE,
        (
            "会有人去\x01",
            "克洛斯贝尔市以外的地方吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2D36")

    label("loc_2CCF")


    #C0153
    ChrTalk(
        0xE,
        (
            "外国人似乎\x01",
            "都打算趁着纪念庆典期间\x01",
            "四处玩个遍呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xE,
        (
            "好像也有人会到\x01",
            "克洛斯贝尔市以外的地方去呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D36")

    Jump("loc_2DA6")

    label("loc_2D3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2DA6")

    #C0155
    ChrTalk(
        0xE,
        (
            "彩虹剧团的宣传册\x01",
            "终于再次到货了。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xE,
        (
            "之前总是处于脱销状态呢，\x01",
            "受欢迎的程度真是令人惊叹啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DA6")

    Jump("loc_28BF")

    label("loc_2DAB")

    TalkEnd(0xE)
    Return()

    # Function_17_28B2 end

    def Function_18_2DAF(): pass

    label("Function_18_2DAF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_300F")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0157
    ChrTalk(
        0xFE,
        "#0600F……又是你们吗……\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0158
    ChrTalk(
        0x101,
        "#0005F达、达德利搜查官！？\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x102,
        "#0100F那个……真是好巧呢。\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x104,
        "#0305F来买东西的吗？\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "#0601F……怎么可能！\x01",
            "是在克洛斯贝尔市内进行重点警备。\x02\x03",

            "#0603F在中央广场和大道，\x01",
            "还有港湾区等人群聚集的地方，\x01",
            "都会定期派人巡逻。\x02\x03",

            "以防有罪犯或者\x01",
            "恐怖分子趁乱\x01",
            "混进纪念庆典。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        "#0001F是、是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x103,
        (
            "#0200F真意外，您也会做这种\x01",
            "基层工作啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "#0603F呼……跟你们谈这些\x01",
            "也无济于事啊。\x02\x03",

            "#0600F赶快回去工作吧，\x01",
            "他们也交给你们\x01",
            "很多杂务吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB1, 6)
    Jump("loc_30F3")

    label("loc_300F")


    #C0165
    ChrTalk(
        0xFE,
        (
            "#0606F……不过今年的\x01",
            "人流量可真是多到夸张啊。\x02\x03",

            "#0608F这种景象，要是让恐怖分子或猎兵团看见，\x01",
            "一定会欣喜若狂吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        (
            "#0005F（我觉得他是有点\x01",
            "  担心过头了……）\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x102,
        (
            "#0103F（是啊，要是有外国要人\x01",
            "  来访的话，也还可以理解……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30F3")

    TalkEnd(0xFE)
    Return()

    # Function_18_2DAF end

    def Function_19_30F7(): pass

    label("Function_19_30F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_337C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32DC")

    #C0168
    ChrTalk(
        0xFE,
        (
            "我们正在举行纪念庆典结束的特卖会，\x01",
            "今天的营业时间预计比平日\x01",
            "延长两小时左右。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "深夜时段的百货店，\x01",
            "所有店铺都将以酬宾特价供应商品，\x01",
            "以表达对顾客们的感谢之情。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x102,
        "#0100F唔……虽然很吸引人……\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        (
            "#0000F但今天还有正事，\x01",
            "必须要去米修拉姆疗养地……\x02\x03",

            "#0003F……真是很抱歉，\x01",
            "让大家都陪我一起。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x104,
        (
            "#0300F不过就是错过了一场特卖会而已嘛，\x01",
            "别这么严肃啦。\x02\x03",

            "哈哈，不过……\x01",
            "要比赶不上好时机的话，\x01",
            "咱们可真算得上是天下第一啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x103,
        "#0211F……一点都不好笑。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3377")

    label("loc_32DC")


    #C0174
    ChrTalk(
        0xFE,
        (
            "深夜时段的百货店，\x01",
            "所有店铺都将以酬宾特价供应商品，\x01",
            "以表达对顾客们的感谢之情。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "在纪念庆典那渐深的夜色下，\x01",
            "还请光临本百货店，尽情享受购物的乐趣。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3377")

    Jump("loc_38C0")

    label("loc_337C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_3409")

    #C0176
    ChrTalk(
        0xFE,
        (
            "偶尔会看到像是同行的游客\x01",
            "在店内环视。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "如果在看过本店之后，\x01",
            "能够产生更多顾客至上的百货店，\x01",
            "我是非常欢迎他们来参观的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C0")

    label("loc_3409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_3504")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_349C")

    #C0178
    ChrTalk(
        0xFE,
        (
            "呀……你们\x01",
            "似乎在找人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "不介意的话，\x01",
            "请到综合服务台\x01",
            "询问一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xFE,
        (
            "本百货店的接待人员\x01",
            "可能会有什么头绪。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_34FF")

    label("loc_349C")


    #C0181
    ChrTalk(
        0xFE,
        (
            "唔，既然那两人\x01",
            "都没有见过……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "应该就是没有\x01",
            "来过本百货店吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "没能帮上忙，\x01",
            "实在抱歉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34FF")

    Jump("loc_38C0")

    label("loc_3504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3591")

    #C0184
    ChrTalk(
        0xFE,
        (
            "偶尔会看到像是同行的游客\x01",
            "在店内环视。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "如果在看过本店之后，\x01",
            "能够产生更多顾客至上的百货店，\x01",
            "我是非常欢迎他们来参观的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C0")

    label("loc_3591")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3629")

    #C0186
    ChrTalk(
        0xFE,
        (
            "关于本百货店的商品和店铺的质量，\x01",
            "身为经理，我一定会负起责任，\x01",
            "亲自进行监督的。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "万一您遇到\x01",
            "缺陷商品或不当的接待，\x01",
            "请随时告诉我。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C0")

    label("loc_3629")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_368B")

    #C0188
    ChrTalk(
        0xFE,
        (
            "近年来，游客不断增多，\x01",
            "本店也生意兴隆。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "客人您要是方便的话，\x01",
            "请随便看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C0")

    label("loc_368B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3709")

    #C0190
    ChrTalk(
        0xFE,
        (
            "本百货店也出售大量\x01",
            "克洛斯贝尔的\x01",
            "本地特产。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "非常适合当作观光时购买的土特产。\x01",
            "方便的话，\x01",
            "请务必来看看。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C0")

    label("loc_3709")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_38C0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3857")

    #C0192
    ChrTalk(
        0xFE,
        (
            "昨天，我们从米修拉姆疗养地\x01",
            "请来了『咪西』\x01",
            "参加我们的活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "顾客们的评价也很好，\x01",
            "百货店的销售额也比上个年度增加了１２％。\x01",
            "企划大获成功。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x103,
        (
            "#0205F……竟、竟然\x01",
            "举行了这种活动……\x02\x03",

            "#0201F（要是没有和约纳打游戏的话，\x01",
            "  就不会错过了……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x101,
        "#0000F缇、缇欧？\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x103,
        (
            "#0203F……我没事，\x01",
            "请不必在意。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_38C0")

    label("loc_3857")


    #C0197
    ChrTalk(
        0xFE,
        (
            "昨天和『咪西』\x01",
            "联合展开的活动\x01",
            "圆满结束了。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "人气吉祥物的影响力果然很大啊，\x01",
            "做这个企划真是值得。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38C0")

    TalkEnd(0xFE)
    Return()

    # Function_19_30F7 end

    def Function_20_38C4(): pass

    label("Function_20_38C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_39A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3948")

    #C0199
    ChrTalk(
        0xFE,
        (
            "帕尔前辈真幸福啊，\x01",
            "有个游击士未婚夫，\x01",
            "真令人羡慕。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "我也想要一个\x01",
            "能察觉到我魅力的\x01",
            "未婚夫啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_399C")

    label("loc_3948")


    #C0201
    ChrTalk(
        0xFE,
        (
            "纪念庆典时的顾客们，\x01",
            "我也努力物色过了……\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xFE,
        (
            "唉，可是很少有人\x01",
            "会注意到我呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_399C")

    Jump("loc_3C47")

    label("loc_39A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_39EE")

    #C0203
    ChrTalk(
        0xFE,
        "咪西很可爱吧！？\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "唉，我也想\x01",
            "摸摸那毛茸茸的身体啊～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C47")

    label("loc_39EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3A36")
    OP_93(0xFE, 0x0, 0x0)

    #C0205
    ChrTalk(
        0xFE,
        "游行、游行……¤\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "今天要不要\x01",
            "旷一下工呢⊥\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C47")

    label("loc_3A36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_3A73")

    #C0207
    ChrTalk(
        0xFE,
        "唉，肚子饿了～\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "工作怎么\x01",
            "还没结束啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C47")

    label("loc_3A73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3B0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AD9")

    #C0209
    ChrTalk(
        0xFE,
        "啊，欢迎光临～\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "客人也是来参观纪念庆典的吗～？\x01",
            "真好啊～好羡慕啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_3B08")

    label("loc_3AD9")


    #C0211
    ChrTalk(
        0xFE,
        (
            "我也很想去玩……\x01",
            "可是好遗憾，还要工作呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B08")

    Jump("loc_3C47")

    label("loc_3B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3C47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BDD")

    #C0212
    ChrTalk(
        0xFE,
        "#4S纪念庆典万岁～！\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "……可是呢，\x01",
            "其实我有点在意……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "从昨天开始，店里\x01",
            "就一直有个可疑的人呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "是个戴眼镜、穿西装\x01",
            "的男人……\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "好可疑，\x01",
            "该不会是恐怖分子吧……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_3C47")

    label("loc_3BDD")


    #C0217
    ChrTalk(
        0xFE,
        (
            "戴眼镜、穿西装的可疑男人……\x01",
            "现在好像在二楼的卖场。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "是不是应该报警\x01",
            "比较好呢……（自言自语）……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C47")

    TalkEnd(0xFE)
    Return()

    # Function_20_38C4 end

    def Function_21_3C4B(): pass

    label("Function_21_3C4B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3CEF")

    #C0219
    ChrTalk(
        0xFE,
        (
            "呼～结果，在今年的纪念庆典，\x01",
            "我也是过着在家里学习和到百货店跑腿\x01",
            "这两点一线的生活啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "好想早点通过实习医生的考试，\x01",
            "去乌尔斯拉医院工作啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FB0")

    label("loc_3CEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3D75")

    #C0221
    ChrTalk(
        0xFE,
        (
            "……啊！\x01",
            "这不是比父母要我买的东西\x01",
            "便宜十米拉吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        "太好了，多出的钱就当是跑腿费了～！\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        "……虽然只有十米拉。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FB0")

    label("loc_3D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3DE5")

    #C0224
    ChrTalk(
        0xFE,
        (
            "虽说是进口食品，\x01",
            "但还真是相当便宜啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "只用一条铁路就可以进口，\x01",
            "运输费用几乎等于免费吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FB0")

    label("loc_3DE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_3E3A")

    #C0226
    ChrTalk(
        0xFE,
        "参考书，参考书……\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "唉，纪念庆典也快结束了，\x01",
            "落榜生真痛苦啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FB0")

    label("loc_3E3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3E9E")

    #C0228
    ChrTalk(
        0xFE,
        (
            "希伦姐\x01",
            "昨天回家的时候，\x01",
            "都已经傍晚了。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "难得的休假，\x01",
            "却只有晚饭时\x01",
            "才能团聚。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FB0")

    label("loc_3E9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3FB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F32")

    #C0230
    ChrTalk(
        0xFE,
        (
            "搞什么嘛，希伦姐\x01",
            "怎么还不来啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "因为今天休假，\x01",
            "说好要我来接她的……\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0xFE,
        (
            "不、不会又给\x01",
            "梅菲尔小姐添麻烦了吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_3FB0")

    label("loc_3F32")


    #C0233
    ChrTalk(
        0xFE,
        (
            "希伦姐以前就\x01",
            "一直给从小玩到大的\x01",
            "梅菲尔小姐添麻烦。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xFE,
        (
            "真是的……\x01",
            "该不会是忘记了和我的约定，\x01",
            "自己到纪念庆典中玩去了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FB0")

    TalkEnd(0xFE)
    Return()

    # Function_21_3C4B end

    def Function_22_3FB4(): pass

    label("Function_22_3FB4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4031")

    #C0235
    ChrTalk(
        0xFE,
        (
            "我看了早上发的传单，真是吓了一跳呢！\x01",
            "竟然说今天要一直开到深夜！\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        (
            "啊啊，到底要怎样\x01",
            "诱惑我才甘心啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4224")

    label("loc_4031")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_408B")

    #C0237
    ChrTalk(
        0xFE,
        (
            "好吧～商店基本\x01",
            "都逛过一次了……\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "差不多该去一楼\x01",
            "买晚饭的材料了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4224")

    label("loc_408B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4103")

    #C0239
    ChrTalk(
        0xFE,
        (
            "首～先～呢……\x01",
            "今天也要逛逛『卢卡』时装店～！\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "虽然不是每天都会出新时装，\x01",
            "不过总是忍不住去看呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4224")

    label("loc_4103")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_415E")

    #C0241
    ChrTalk(
        0xFE,
        "那个和这个，还有那个……\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        (
            "呀，怎么办啊！\x01",
            "无法决定到底该买哪个了～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4224")

    label("loc_415E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_41C9")

    #C0243
    ChrTalk(
        0xFE,
        (
            "肯那孩子，陪我来买东西时，\x01",
            "从来都不会摆出不耐烦的脸色。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xFE,
        "嗯嗯，我真是有个好儿子啊⊥\x02",
    )

    CloseMessageWindow()
    Jump("loc_4224")

    label("loc_41C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4224")

    #C0245
    ChrTalk(
        0xFE,
        (
            "为了奖励每天努力的自己，\x01",
            "就尽情挥霍私房钱吧～！\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xFE,
        (
            "今天想买什么\x01",
            "就买什么！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4224")

    TalkEnd(0xFE)
    Return()

    # Function_22_3FB4 end

    def Function_23_4228(): pass

    label("Function_23_4228")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4295")

    #C0247
    ChrTalk(
        0xFE,
        (
            "唉……\x01",
            "我今天要一直跟着妈妈逛到深夜……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xFE,
        (
            "不过妈妈和其他的客人们\x01",
            "好像都很开心呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4690")

    label("loc_4295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA2, 4)), scpexpr(EXPR_END)), "loc_42F6")

    #C0249
    ChrTalk(
        0xFE,
        (
            "呼，妈妈好像终于\x01",
            "把所有商店\x01",
            "都逛了一个遍。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0xFE,
        (
            "看腻时的表情\x01",
            "真是一目了然呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4690")

    label("loc_42F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_4451")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43F1")

    #C0251
    ChrTalk(
        0x101,
        (
            "#0001F（嗯，这孩子\x01",
            "  可能知道些什么吧……）\x02",
        )
    )

    CloseMessageWindow()

    #A0252
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德出示了柯林的照片，\x01",
            "并询问对方是否有什么线索。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0253
    ChrTalk(
        0xFE,
        "哎？这个……\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "嗯～没有见过。\x01",
            "我不认识这孩子呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        (
            "#0000F是吗……\x01",
            "谢谢，帮大忙了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xAB, 7)
    OP_D0(0x2, (scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 25)
    Jump("loc_444C")

    label("loc_43F1")


    #C0256
    ChrTalk(
        0xFE,
        (
            "对不起，\x01",
            "我好像没见过这孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xFE,
        (
            "今天虽然\x01",
            "也来了不少小孩子，\x01",
            "但我不记得见过像他的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_444C")

    Jump("loc_4690")

    label("loc_4451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_44B2")

    #C0258
    ChrTalk(
        0xFE,
        (
            "呼，妈妈好像终于\x01",
            "把所有商店\x01",
            "都逛了一个遍。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0xFE,
        (
            "看腻时的表情\x01",
            "真是一目了然呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4690")

    label("loc_44B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_452C")

    #C0260
    ChrTalk(
        0xFE,
        (
            "妈妈对时装店里那些商品的\x01",
            "兴趣比别人多一倍。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0xFE,
        (
            "……妈妈能一直保持着年轻的心态，\x01",
            "应该是值得高兴的吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4690")

    label("loc_452C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_458A")

    #C0262
    ChrTalk(
        0xFE,
        (
            "妈妈决定不了买什么东西\x01",
            "是家常便饭。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "唉，还要等几个小时\x01",
            "才能回家呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4690")

    label("loc_458A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_463C")

    #C0264
    ChrTalk(
        0xFE,
        (
            "妈妈买东西时总是逛个没完，\x01",
            "要是放着她不管，一定会在\x01",
            "百货店里晃悠一整天吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0xFE,
        (
            "所以爸爸要我\x01",
            "负责跟着妈妈。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "这可是关系到家庭存亡的\x01",
            "大问题，我不得不做呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4690")

    label("loc_463C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4690")

    #C0267
    ChrTalk(
        0xFE,
        (
            "妈妈经常说\x01",
            "要奖励自己……\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        (
            "其实也应该\x01",
            "奖励一下\x01",
            "一直陪她逛的我吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4690")

    TalkEnd(0xFE)
    Return()

    # Function_23_4228 end

    def Function_24_4694(): pass

    label("Function_24_4694")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_473C")

    #C0269
    ChrTalk(
        0xFE,
        (
            "昨天把在这里选购\x01",
            "的胸针送给老伴了，\x01",
            "她高兴得不得了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "我以前总是大男子主义，\x01",
            "就爱装腔作势，\x01",
            "真是惭愧呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        (
            "今后也时不时地\x01",
            "送她点礼物吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_492A")

    label("loc_473C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4792")

    #C0272
    ChrTalk(
        0xFE,
        (
            "唔唔……伤脑筋。\x01",
            "我实在是没有什么送礼物的经验，\x01",
            "搞不清该选什么啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_492A")

    label("loc_4792")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_47CD")

    #C0273
    ChrTalk(
        0xFE,
        (
            "那么……到底送什么，\x01",
            "才能让老伴开心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_492A")

    label("loc_47CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 6)), scpexpr(EXPR_END)), "loc_483F")

    #C0274
    ChrTalk(
        0xFE,
        "还是应该送正统的戒指吧。\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "可是，如果送老伴这个，\x01",
            "就会想起求婚时的情景，\x01",
            "实在是难为情呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_492A")

    label("loc_483F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_48A7")

    #C0276
    ChrTalk(
        0xFE,
        (
            "难得的纪念庆典，\x01",
            "我正在选购很早以前就计划\x01",
            "送给老伴的礼物。\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xFE,
        "唔……该送什么好呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_492A")

    label("loc_48A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_492A")

    #C0278
    ChrTalk(
        0xFE,
        (
            "在昨天的典礼上，\x01",
            "听到了麦克道尔市长\x01",
            "的精彩演讲。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "他好像和那个\x01",
            "哈尔特曼议长是对立关系，\x01",
            "希望他今后也多加努力啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_492A")

    TalkEnd(0xFE)
    Return()

    # Function_24_4694 end

    def Function_25_492E(): pass

    label("Function_25_492E")

    Jc((scpexpr(EXPR_23, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49C0")

    #C0280
    ChrTalk(
        0x160,
        (
            "#3300F（中央广场的探听\x01",
            "  就到此为止吧？）\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x101,
        (
            "#0000F（嗯，应该足够了。）\x02\x03",

            "（接下来就去\x01",
            "  站前街道探听吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_D0(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xB9, 5)
    OP_29(0x46, 0x1, 0x7)

    label("loc_49C0")

    Return()

    # Function_25_492E end

    def Function_26_49C1(): pass

    label("Function_26_49C1")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0282
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

    #A0283
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※若有不明之处，\x01",
            "  敬请随时咨询\x01",
            "  正门综合服务台。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_26_49C1 end

    def Function_27_4A95(): pass

    label("Function_27_4A95")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(0, 3300, 19500, 0)
    MoveCamera(57, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(44000, 0)
    SetChrPos(0x101, 600, 30, -2000, 0)
    SetChrPos(0x160, -600, 30, -2200, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x160, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    OP_68(0, 1300, 7500, 7000)
    MoveCamera(40, 25, 0, 7000)
    SetCameraDistance(29000, 7000)
    FadeToBright(2000, 0)
    Sleep(5000)

    def lambda_4B7E():
        OP_96(0xFE, 0x258, 0x1E, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4B7E)

    def lambda_4B98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4B98)
    Sleep(100)

    def lambda_4BAC():
        OP_96(0xFE, 0xFFFFFDA8, 0x1E, 0x708, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x160, 1, lambda_4BAC)

    def lambda_4BC6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x160, 2, lambda_4BC6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x160, 1)
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 1200, 2500, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(19000, 0)
    OP_0D()

    #C0284
    ChrTalk(
        0x101,
        (
            "#0006F人真多啊……\x02\x03",

            "#0000F不过，最好还是\x01",
            "在这里探听一遍。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x160,
        (
            "#12P#3300F玲也赞成。\x02\x03",

            "#3304F反正只要问问接待员姐姐们\x01",
            "和儿童顾客就可以了吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x160, 500)

    #C0286
    ChrTalk(
        0x101,
        (
            "#0012F#11P嗯，我也这么想……\x02\x03",

            "#0000F……小玲，你好聪明呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x160, 0x101, 500)
    Sleep(150)

    #C0287
    ChrTalk(
        0x160,
        (
            "#6P#3309F呵呵，\x01",
            "关于这点，玲还是有些自信的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 0, 0, 2500, 0)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0xA2, 3)
    EventEnd(0x5)
    Return()

    # Function_27_4A95 end

    SaveToFile()

Try(main)
