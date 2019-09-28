from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t1510.bin",                # FileName
        "t1510",                    # MapName
        "t1510",                    # Location
        0x004E,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 78, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1510",                  # 0
        "琪尔修宿舍长",           # 1
        "实习医生芙萝拉",         # 2
        "实习医生利顿",           # 3
        "塞茜尔",                 # 4
        "游击士林",               # 5
        "游击士艾欧莉娅",         # 6
        "游客特耶",               # 7
        "游客帕斯特尔",           # 8
    ))

    AddCharChip((
        "chr/ch24300.itc",                   # 00
        "chr/ch29502.itc",                   # 01
        "chr/ch29402.itc",                   # 02
        "chr/ch32002.itc",                   # 03
        "chr/ch32102.itc",                   # 04
        "chr/ch34302.itc",                   # 05
        "chr/ch23900.itc",                   # 06
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

    DeclNpc(-4809,   0,       11600,   225,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-12069,  150,     14399,   180,  341,  0x0, 0,   1,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(-12069,  150,     11050,   0,    469,  0x0, 0,   2,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(-12479,  150,     6900,    180,  469,  0x0, 0,   3,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(-12319,  150,     3630,    0,    469,  0x0, 0,   4,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-12479,  150,     6900,    180,  469,  0x0, 0,   5,   0,   255, 255, 0,   12,  255,  0)
    DeclNpc(4690,    3750,    15430,   0,    385,  0x0, 0,   6,   0,   0,   0,   0,   13,  255,  0)

    DeclEvent(0x0000, 0, 17,  9.0,                   11.0,                  3.25,                  9.0,                   [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -3.0,                  -5.5,                  -0.6500000357627869,   1.0])

    DeclActor(-6100,   0,       10440,   1000,    -4810,   1500,    11600,   0x007E, 0,  3,  0x0000)
    DeclActor(4390,    3750,    16900,   1000,    4390,    5000,    16900,   0x007C, 0,  11, 0x0000)
    DeclActor(5830,    0,       11730,   1200,    5830,    1500,    11730,   0x007C, 0,  18, 0x0000)

    ScpFunction((
        "Function_0_304",          # 00, 0
        "Function_1_3BC",          # 01, 1
        "Function_2_42C",          # 02, 2
        "Function_3_4D1",          # 03, 3
        "Function_4_4D5",          # 04, 4
        "Function_5_143A",         # 05, 5
        "Function_6_1532",         # 06, 6
        "Function_7_258C",         # 07, 7
        "Function_8_26DA",         # 08, 8
        "Function_9_27A8",         # 09, 9
        "Function_10_2A60",        # 0A, 10
        "Function_11_2FA2",        # 0B, 11
        "Function_12_3006",        # 0C, 12
        "Function_13_31E4",        # 0D, 13
        "Function_14_3299",        # 0E, 14
        "Function_15_42B6",        # 0F, 15
        "Function_16_4E6D",        # 10, 16
        "Function_17_537D",        # 11, 17
        "Function_18_540C",        # 12, 18
    ))


    def Function_0_304(): pass

    label("Function_0_304")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_344"),
        (1, "loc_350"),
        (2, "loc_35C"),
        (3, "loc_368"),
        (4, "loc_374"),
        (5, "loc_380"),
        (6, "loc_38C"),
        (SWITCH_DEFAULT, "loc_398"),
    )


    label("loc_344")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_350")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_35C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_368")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_374")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_380")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_38C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_398")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_3A4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3BB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3A4")

    label("loc_3BB")

    Return()

    # Function_0_304 end

    def Function_1_3BC(): pass

    label("Function_1_3BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3CA")
    Jump("loc_3D8")

    label("loc_3CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3D8")
    ClearChrFlags(0xA, 0x80)

    label("loc_3D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F0")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)

    label("loc_3F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_404")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 14)
    Jump("loc_413")

    label("loc_404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_413")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 15)

    label("loc_413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_42B")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)

    label("loc_42B")

    Return()

    # Function_1_3BC end

    def Function_2_42C(): pass

    label("Function_2_42C")

    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x2, 0x10)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_481")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49D")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_4D0")

    label("loc_49D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B9")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_4D0")

    label("loc_4B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D0")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)

    label("loc_4D0")

    Return()

    # Function_2_42C end

    def Function_3_4D1(): pass

    label("Function_3_4D1")

    Call(0, 4)
    Return()

    # Function_3_4D1 end

    def Function_4_4D5(): pass

    label("Function_4_4D5")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1436")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "休息\x01",      # 2
            "放弃\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_541")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_541")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_571")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_560")
    OP_AF(0x5D)
    Jump("loc_562")

    label("loc_560")

    OP_AF(0x5C)

    label("loc_562")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1431")

    label("loc_571")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_591")
    OP_AF(0x5A)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1431")

    label("loc_591")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5A5")
    Jump("loc_1431")

    label("loc_5A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1431")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_605")

    #C0001
    ChrTalk(
        0x8,
        "您好，欢迎光临！\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "医院也才刚刚开始\x01",
            "今天的营业。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1431")

    label("loc_605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_763")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_704")

    #C0003
    ChrTalk(
        0x8,
        (
            "那群小护士们差不多\x01",
            "该来取病号餐了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "最近的饭菜\x01",
            "受到了住院患者们的好评呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "虽然之前盖巴尔议员\x01",
            "任性地说过『再弄得豪华点』，\x01",
            "让我觉得很生气……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "不过也多亏了他，\x01",
            "才让我对菜式下了一番苦功夫，\x01",
            "总之结果是好的啦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_75E")

    label("loc_704")


    #C0007
    ChrTalk(
        0x8,
        (
            "最近的饭菜\x01",
            "受到了住院患者们的好评呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "这也可以说是盖巴尔议员\x01",
            "一味任性的结果吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_75E")

    Jump("loc_1431")

    label("loc_763")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_7D2")

    #C0009
    ChrTalk(
        0x8,
        (
            "今天早上被抬进来的患者\x01",
            "似乎是受了枪伤。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "真可怕……\x01",
            "希望不要把医院\x01",
            "卷进危险的事件里啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1431")

    label("loc_7D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_840")

    #C0011
    ChrTalk(
        0x8,
        (
            "那两位游击士经常\x01",
            "来医院帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "我们平时总是受她们的关照，\x01",
            "今天就由我来请她们吃饭好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1431")

    label("loc_840")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_8B0")

    #C0013
    ChrTalk(
        0x8,
        (
            "嗯，刚才和你们在一起的\x01",
            "女孩子去哪里了？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "……什么，走散了！？\x01",
            "呼……你们到底在干什么啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1431")

    label("loc_8B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_AF7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A95")

    #C0015
    ChrTalk(
        0x8,
        (
            "嗯，我听到你们刚才的对话了……\x01",
            "你就是塞茜尔的弟弟\x01",
            "的女儿吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x153,
        "#1105F咦，琪雅果然是罗伊德的孩子吗？\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#0011F不、不是啦……！\x01",
            "都说了那是误会啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "啊哈哈，我只是开个玩笑而已。\x01",
            "别当真～别当真。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x153,
        "#1111F嗯？\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#0005F这样啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_9FE")

    #C0021
    ChrTalk(
        0x102,
        (
            "#0102F（呵呵，虽然我早就看出来\x01",
            "  他很好戏弄了……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8D")

    label("loc_9FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_A44")

    #C0022
    ChrTalk(
        0x103,
        (
            "#0202F（罗伊德前辈\x01",
            " 就是那种\x01",
            " 人见人欺的角色啊。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A8D")

    label("loc_A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_A8D")

    #C0023
    ChrTalk(
        0x104,
        (
            "#0309F（哈哈哈，真是个可爱的家伙。\x01",
            " 罗伊德就该保持这样。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A8D")

    SetScenarioFlags(0x0, 0)
    Jump("loc_AF2")

    label("loc_A95")


    #C0024
    ChrTalk(
        0x8,
        "啊哈哈，开你玩笑，是我不好。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "不过，说对不起好像也有点奇怪，\x01",
            "就不要在意这种小事啦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AF2")

    Jump("loc_1431")

    label("loc_AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_B52")

    #C0026
    ChrTalk(
        0x8,
        "啊，欢迎光临。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "市里明明正在举行纪念庆典，\x01",
            "还特意跑到这种地方来啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1431")

    label("loc_B52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_C2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF7")

    #C0028
    ChrTalk(
        0x8,
        (
            "食堂以及病号餐的食材，\x01",
            "都是从一个名叫哈罗德\x01",
            "的商人那买来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "只有他会以那么便宜的价格，\x01",
            "把新鲜又有益于身体健康\x01",
            "的食材卖给我们。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C2A")

    label("loc_BF7")


    #C0030
    ChrTalk(
        0x8,
        (
            "医院烹制料理的食材都是\x01",
            "从哈罗德先生那买来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C2A")

    Jump("loc_1431")

    label("loc_C2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_CD7")

    #C0031
    ChrTalk(
        0x8,
        (
            "在宿舍工作的玛罗奈是\x01",
            "我的侄女。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "我看她在家里帮忙做家务挺闲的，\x01",
            "就让她来这里工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "那孩子的优点就只有爱干净了，\x01",
            "因此很合适\x01",
            "从事清洁工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1431")

    label("loc_CD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_E27")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB8")

    #C0034
    ChrTalk(
        0x8,
        (
            "好不容易等到了纪念庆典，\x01",
            "却住院躺在病床上，\x01",
            "这很让人同情吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "所以我想，\x01",
            "至少在纪念庆典期间\x01",
            "把病号餐做得豪华一点。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "话虽如此，\x01",
            "但也不能让饭菜的营养均衡失调。\x01",
            "只能在创意上多下功夫了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E22")

    label("loc_DB8")


    #C0037
    ChrTalk(
        0x8,
        (
            "至少在纪念庆典期间，\x01",
            "我想把病号餐做得\x01",
            "豪华一点。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "昨天的菜式新加了\x01",
            "豆腐肉饼……\x01",
            "很健康很不错吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E22")

    Jump("loc_1431")

    label("loc_E27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_F1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EBD")

    #C0039
    ChrTalk(
        0x8,
        (
            "这里的实习医生\x01",
            "连吃饭的时候都在学习，\x01",
            "都很努力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "嗯嗯，必须要趁着年轻时多学一些东西。\x01",
            "毕竟关系到美好的未来嘛。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F17")

    label("loc_EBD")


    #C0041
    ChrTalk(
        0x8,
        (
            "为了努力学习的实习医生们，\x01",
            "我来想想能够补脑的\x01",
            "特别菜谱吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        "鱼眼不知道行不行呢？\x02",
    )

    CloseMessageWindow()

    label("loc_F17")

    Jump("loc_1431")

    label("loc_F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_F9B")

    #C0043
    ChrTalk(
        0x8,
        (
            "来食堂吃饭的客人们\x01",
            "都在谈论彩虹剧团哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "新的剧目……\x01",
            "名字是叫『金之太阳、银之月』吧，\x01",
            "我一定要去看看～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1431")

    label("loc_F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_1101")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB7")
    Call(0, 5)
    Jump("loc_10FC")

    label("loc_FB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_106A")

    #C0045
    ChrTalk(
        0x8,
        (
            "住院患者的食物\x01",
            "也是我做的……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "昨天住进了个人病房的\x01",
            "盖巴尔议员说出了『给我牛排』\x01",
            "之类的梦话。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "而我也忍不住反驳道\x01",
            "『想吃牛排的话，\x01",
            "就去西餐厅吧』。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10FC")

    label("loc_106A")


    #C0048
    ChrTalk(
        0x8,
        (
            "昨天住进了个人病房的\x01",
            "盖巴尔议员说出了『给我牛排』\x01",
            "之类的梦话。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "我在烹制料理的时候\x01",
            "也是要考虑营养平衡的，\x01",
            "那种任性的家伙真是让人头疼呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10FC")

    Jump("loc_1431")

    label("loc_1101")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_11B6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_111D")
    Call(0, 5)
    Jump("loc_11B1")

    label("loc_111D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1180")

    #C0050
    ChrTalk(
        0x8,
        (
            "午休也结束了，\x01",
            "宿舍里终于安静下来了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "稍后我也\x01",
            "帮玛罗奈\x01",
            "一起打扫吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11B1")

    label("loc_1180")


    #C0052
    ChrTalk(
        0x8,
        (
            "啊……要是想点东西的话，\x01",
            "不要客气跟我说哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11B1")

    Jump("loc_1431")

    label("loc_11B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1332")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D2")
    Call(0, 5)
    Jump("loc_132D")

    label("loc_11D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12EB")

    #C0053
    ChrTalk(
        0x8,
        (
            "啊，塞茜尔，\x01",
            "休息的时间还没有结束吧，\x01",
            "这就要回去了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "护士本来就很忙的，\x01",
            "所以能休息的时候就要好好休息哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x136,
        (
            "#1302F呵呵，没关系的。\x01",
            "因为见到了罗伊德，\x01",
            "所以疲劳早就消散了。\x02\x03",

            "#1300F宿舍长，谢谢你借\x01",
            "地方给我。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "哈哈，小事一桩。\x01",
            "你也住在我们宿舍嘛。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_132D")

    label("loc_12EB")


    #C0057
    ChrTalk(
        0x8,
        (
            "你们也是，别总是带着塞茜尔\x01",
            "到处乱走。\x01",
            "她的工作可是非常忙的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_132D")

    Jump("loc_1431")

    label("loc_1332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1431")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_134E")
    Call(0, 5)
    Jump("loc_1431")

    label("loc_134E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C8")

    #C0058
    ChrTalk(
        0x8,
        (
            "您好，欢迎光临。\x01",
            "这里是医院职员们的宿舍。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "有的医生值夜班后在这里睡觉，\x01",
            "千万不要把他们吵醒了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1431")

    label("loc_13C8")


    #C0060
    ChrTalk(
        0x8,
        (
            "食堂和宿舍都有\x01",
            "向外来的客人开放。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "要是想吃什么的话，跟我说就行。\x01",
            "我会拿出看家本领\x01",
            "给你们做的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1431")

    Jump("loc_4E2")

    label("loc_1436")

    TalkEnd(0x8)
    Return()

    # Function_4_4D5 end

    def Function_5_143A(): pass

    label("Function_5_143A")


    #C0062
    ChrTalk(
        0x8,
        (
            "这所医院的食物充分考虑到了\x01",
            "营养的平衡。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "总之我的拿手好菜是\x01",
            "手制炖牛肉。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "我会告诉你们做法，\x01",
            "如果方便的话，\x01",
            "你们也试着做做吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0065
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x19D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法被教授了。\x02",
        )
    )

    CloseMessageWindow()

    #A0066
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x19D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x5)
    Return()

    # Function_5_143A end

    def Function_6_1532(): pass

    label("Function_6_1532")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15C6")
    Jump("loc_1610")

    label("loc_15C6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_15E6")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1610")

    label("loc_15E6")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1606")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1610")

    label("loc_1606")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1610")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1728")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B2")

    #C0067
    ChrTalk(
        0xFE,
        "啊……那本书！\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "你们好像顺利找到了呢，\x01",
            "真是太好了。\x01",
            "真抱歉，给你们添麻烦了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_171B")

    label("loc_16B2")


    #C0069
    ChrTalk(
        0xFE,
        (
            "不过，要在那么多书架中\x01",
            "找出一本书，\x01",
            "应该很麻烦吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "真亏你们能找到呢，\x01",
            "是用了所谓的人海战术吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_171B")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_1728")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_181F")

    #C0071
    ChrTalk(
        0xFE,
        (
            "我经常把研究楼资料室中的\x01",
            "医书带出来，\x01",
            "然后在这里学习……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "这次好像是在将医书放回资料室时，\x01",
            "不小心把图书馆的书\x01",
            "也一起放上去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "不好意思，\x01",
            "能不能麻烦你们去资料室帮我找找呢？\x01",
            "就在病房楼顶的研究楼里。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_181F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1840")
    Call(0, 16)
    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    label("loc_1840")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1900")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18CA")

    #C0074
    ChrTalk(
        0xFE,
        (
            "好了……\x01",
            "差不多该开始学习了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "离吃午饭……还有些时间呢。\x01",
            "嗯，只要开始看书，\x01",
            "时间很快就会过去的吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18FB")

    label("loc_18CA")


    #C0076
    ChrTalk(
        0xFE,
        (
            "这所食堂对我来说，\x01",
            "是个非常适合学习的空间。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18FB")

    Jump("loc_2584")

    label("loc_1900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_1976")

    #C0077
    ChrTalk(
        0xFE,
        (
            "嗯，今天的课也全部理解了，\x01",
            "这就是医书从不离身的成果。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "跟我同级的利顿\x01",
            "不知道能不能跟上课程呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2584")

    label("loc_1976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_19FE")

    #C0079
    ChrTalk(
        0xFE,
        (
            "为了准备下次的笔试，我现在正在预习呢。\x01",
            "能不能别来打扰我？\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "虽然距离考试还有很久，\x01",
            "但现在开始预习总没有什么坏处。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2584")

    label("loc_19FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1A59")

    #C0081
    ChrTalk(
        0xFE,
        "哈，外科果然很有趣呢。\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "因为有很多未知技术，\x01",
            "所以真的让人很兴奋呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2584")

    label("loc_1A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_1AC4")

    #C0083
    ChrTalk(
        0xFE,
        (
            "哎，小女孩吗？\x01",
            "没看到呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "要是来了食堂的话，\x01",
            "我应该会发觉的。\x01",
            "所以应该不在这里吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2584")

    label("loc_1AC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_1CEB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CB8")
    SetChrSubChip(0xFE, 0x0)

    #C0085
    ChrTalk(
        0xFE,
        "…………………………¤\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x153,
        (
            "#1110F啊，这个人好像在看\x01",
            "很难懂的书呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#0005F我来看看，尸体解剖学……\x02\x03",

            "#0011F我说，琪雅看这种书还太早呢！！\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x153,
        "#1106F咦？好无聊啊。\x02",
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C1C")
    Jump("loc_1C66")

    label("loc_1C1C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C3C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C66")

    label("loc_1C3C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C5C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C66")

    label("loc_1C5C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C66")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)

    #C0089
    ChrTalk(
        0xFE,
        (
            "……我说……\x01",
            "你们好吵哦……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xFE, 0x0)
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CE6")

    label("loc_1CB8")


    #C0090
    ChrTalk(
        0xFE,
        (
            "真是的……\x01",
            "我正在学习呢，\x01",
            "不要来打扰啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CE6")

    Jump("loc_2584")

    label("loc_1CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1D37")

    #C0091
    ChrTalk(
        0xFE,
        (
            "我总是在看书学习，\x01",
            "所以必须要珍惜\x01",
            "这种现场实习的机会呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2584")

    label("loc_1D37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1DAF")

    #C0092
    ChrTalk(
        0xFE,
        (
            "啊……说起来，明天要开教授会，\x01",
            "所以教授们应该都不在。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "嗯，我还有问题要问，\x01",
            "必须早点去问清楚呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2584")

    label("loc_1DAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1E48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DCA")
    Call(0, 8)
    Jump("loc_1E43")

    label("loc_1DCA")


    #C0094
    ChrTalk(
        0xFE,
        (
            "（狼吞虎咽）……\x01",
            "如果在意这些事情，\x01",
            "那就什么都吃不了啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "自从参加过手术之后，\x01",
            "这种东西对我来说就成了家常便饭。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E43")

    Jump("loc_2584")

    label("loc_1E48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1F5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EF5")

    #C0096
    ChrTalk(
        0xFE,
        (
            "……创立纪念庆典？\x01",
            "嗯……不是特别有兴趣。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "再怎么说，我也是为了学习\x01",
            "才来到克洛斯贝尔的。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "不会像其他人一样，\x01",
            "因为不放假\x01",
            "就唉声叹气。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F55")

    label("loc_1EF5")


    #C0099
    ChrTalk(
        0xFE,
        (
            "而且这本来就是『克洛斯贝尔的』\x01",
            "创立纪念庆典吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "跟雷米菲利亚出身的我\x01",
            "没有什么关系呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F55")

    Jump("loc_2584")

    label("loc_1F5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1FED")

    #C0101
    ChrTalk(
        0xFE,
        (
            "还没有到外科的授课时间，\x01",
            "所以我就在这里一边吃饭一边学习。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "……虽然经常被人说不顾形象，\x01",
            "但是我总觉得浪费吃饭时间\x01",
            "很可惜呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2584")

    label("loc_1FED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2151")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20E6")

    #C0103
    ChrTalk(
        0xFE,
        (
            "我经常随身携带\x01",
            "这本生物解剖书……\x01",
            "是不是看起来很奇怪呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "跟利顿一起吃饭时，\x01",
            "他还生气的对我说\x01",
            "『吃饭的时候别读这个』。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x103,
        (
            "#0203F……要是在吃肉时\x01",
            "看那本书的图解，\x01",
            "大概会失去食欲吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        "嗯～不过我完全没有问题。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_214C")

    label("loc_20E6")


    #C0107
    ChrTalk(
        0xFE,
        (
            "随身携带生物解剖书\x01",
            "果然还是很奇怪吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "但对我来说，这样就可以随时随地学习了，\x01",
            "所以很方便啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_214C")

    Jump("loc_2584")

    label("loc_2151")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_21A6")

    #C0109
    ChrTalk(
        0xFE,
        "啊，已经这么晚了啊。\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "差不多该去研究楼的\x01",
            "资料室做做预习了呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2584")

    label("loc_21A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_22F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2276")

    #C0111
    ChrTalk(
        0xFE,
        (
            "利顿跟我一样是\x01",
            "雷米菲利亚出身的。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "那家伙虽然学习成绩一般，\x01",
            "但是为了能进这所医院\x01",
            "曾经拼命学习过。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "不过，果然还是有些迷糊呢。\x01",
            "明明被魔兽袭击过，\x01",
            "竟然没有一点紧张感……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_22F3")

    label("loc_2276")


    #C0114
    ChrTalk(
        0xFE,
        (
            "利顿这人有些迷糊。\x01",
            "明明被魔兽袭击过，\x01",
            "竟然一点紧张感都没有……\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "嗯，傻人有傻福，真是太好了。\x01",
            "必须要感谢空之女神呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22F3")

    Jump("loc_2584")

    label("loc_22F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_243E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23FA")

    #C0116
    ChrTalk(
        0xFE,
        (
            "这里让人觉得很舒服，\x01",
            "一不注意就会坐上很长时间呢。\x01",
            "而且也非常适合学习。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x136,
        (
            "#1302F芙萝拉\x01",
            "真的很喜欢读书呢，\x01",
            "有热情是件好事。\x02\x03",

            "#1304F但是，注意\x01",
            "不要热衷过头，\x01",
            "忘记了去上课哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "……塞茜尔小姐经常会说一些\x01",
            "像妈妈一样的话呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2439")

    label("loc_23FA")


    #C0119
    ChrTalk(
        0xFE,
        (
            "说起来，马上就要到上课时间了……\x01",
            "差不多该回研究楼去了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2439")

    Jump("loc_2584")

    label("loc_243E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2584")
    SetChrSubChip(0xFE, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2551")

    #C0120
    ChrTalk(
        0xFE,
        "嗯嗯，这里要这样做……\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        "……原来如此！\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        (
            "#0005F（似乎在一边吃饭\x01",
            "　一边读书呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x102,
        (
            "#0105F（似乎是生物学的书呢。\x01",
            "　还附带解剖学图解……）\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        "#0306F（好、好恶心……）\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x103,
        (
            "#0203F（……至少\x01",
            "　那不是吃饭的时候\x01",
            "　该读的东西呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2584")

    label("loc_2551")


    #C0126
    ChrTalk(
        0xFE,
        (
            "吃饭时也要好好学习！\x01",
            "哎呀～外科果然很有趣呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2584")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_6_1532 end

    def Function_7_258C(): pass

    label("Function_7_258C")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2620")
    Jump("loc_266A")

    label("loc_2620")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2640")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_266A")

    label("loc_2640")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2660")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_266A")

    label("loc_2660")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_266A")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26A1")
    Call(0, 8)
    Jump("loc_26D2")

    label("loc_26A1")


    #C0127
    ChrTalk(
        0xFE,
        (
            "呼……在吃饭的时候\x01",
            "竟然还能看得了那种东西。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26D2")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_258C end

    def Function_8_26DA(): pass

    label("Function_8_26DA")

    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)

    #C0128
    ChrTalk(
        0xA,
        (
            "我说芙萝拉，\x01",
            "刚才上课的要点是……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xA,
        (
            "……哇啊！？\x01",
            "吃饭的时候别读那种东西啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x9,
        (
            "吃饭时不学习的话，\x01",
            "不是太浪费时间了嘛。\x01",
            "（狼吞虎咽）……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xA,
        (
            "即使那样，\x01",
            "也不用一边看解剖图……\x01",
            "……呕。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_8_26DA end

    def Function_9_27A8(): pass

    label("Function_9_27A8")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_283C")
    Jump("loc_2886")

    label("loc_283C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_285C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2886")

    label("loc_285C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_287C")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2886")

    label("loc_287C")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2886")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_28FB")

    #C0132
    ChrTalk(
        0xFE,
        "做好不错的礼物了吗？\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "稍后我和艾欧莉娅\x01",
            "也去探望好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A58")

    label("loc_28FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_29DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2995")

    #C0134
    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "你说在为小滴\x01",
            "收集做礼物的材料？\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "这样啊，嗯……\x01",
            "虽然很想帮忙……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "但很不巧，我似乎没有\x01",
            "你们在找的东西。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD1, 4)
    Jump("loc_29DA")

    label("loc_2995")


    #C0137
    ChrTalk(
        0xFE,
        (
            "很不巧，我没有\x01",
            "合适的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        "真不好意思，没有帮到你们的忙。\x02",
    )

    CloseMessageWindow()

    label("loc_29DA")

    Jump("loc_2A58")

    label("loc_29DF")


    #C0139
    ChrTalk(
        0xFE,
        (
            "之前遇到了一个伤员，\x01",
            "所以我就和艾欧莉娅一起\x01",
            "把他送到这里来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "真是的，即使纪念庆典结束了，\x01",
            "也还是一样很忙呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A58")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_27A8 end

    def Function_10_2A60(): pass

    label("Function_10_2A60")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AF4")
    Jump("loc_2B3E")

    label("loc_2AF4")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2B14")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B3E")

    label("loc_2B14")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B34")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2B3E")

    label("loc_2B34")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B3E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2BF0")

    #C0141
    ChrTalk(
        0xFE,
        (
            "小滴一直都在这所医院\x01",
            "住院吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "……好，看在我跟亚里欧斯前辈的交情上，\x01",
            "让我久违地蹭蹭她好了⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xC,
        "……不要乱来。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F9A")

    label("loc_2BF0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_2EA6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E21")

    #C0144
    ChrTalk(
        0xFE,
        (
            "咦，小滴是在找\x01",
            "可以做成礼物的材料吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "嗯……我想想。\x01",
            "我这里有什么材料吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0146
    ChrTalk(
        0xFE,
        (
            "……对了！\x01",
            "有个这样的东西。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0147
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "艾欧莉娅取出了苍耀石的结晶。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0148
    ChrTalk(
        0xFE,
        (
            "这个怎么样！\x01",
            "是在不久前，一位帝国的贸易商\x01",
            "作为工作报酬送给我的。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "小滴也一定会\x01",
            "喜欢这个的！\x01",
            "……给，请拿去吧⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#0011F怎、怎么说也不能收这么贵重的东西！\x02\x03",

            "而且小滴也会感到困扰的……！\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x103,
        (
            "#0203F而且如果收下的话，收集材料的\x01",
            "宗旨不是都已经变了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "嗯，是这样吗？\x01",
            "但是好像没有其它可以用的东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xFE,
        (
            "啊啊，好想为小滴\x01",
            "做点什么啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD1, 5)
    Jump("loc_2EA1")

    label("loc_2E21")


    #C0154
    ChrTalk(
        0xFE,
        (
            "啊啊，好想为小滴\x01",
            "做点什么啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "啊，对了，\x01",
            "要不就给你们这个金耀石吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        "#0006F都、都说了不能收那种贵重物品啦……！\x02",
    )

    CloseMessageWindow()

    label("loc_2EA1")

    Jump("loc_2F9A")

    label("loc_2EA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F41")

    #C0157
    ChrTalk(
        0xFE,
        (
            "刚才送来的那位伤员，\x01",
            "似乎是在郊外遭到了魔兽的袭击。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "魔兽似乎变得\x01",
            "比以前强了很多。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "那位伤员总算捡回了一条命，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F9A")

    label("loc_2F41")


    #C0160
    ChrTalk(
        0xFE,
        "其实我也帮忙进行了手术哦。\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "每当这时我就会想，自己持有医生资格证\x01",
            "实在是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F9A")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_10_2A60 end

    def Function_11_2FA2(): pass

    label("Function_11_2FA2")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0162
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "三楼：女性职员宿舍→\x01\x01",
            "←二楼：男性职员宿舍\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_2FA2 end

    def Function_12_3006(): pass

    label("Function_12_3006")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xE)
    ClearChrFlags(0xE, 0x10)
    TurnDirection(0xE, 0x0, 0)
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_309A")
    Jump("loc_30E4")

    label("loc_309A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_30BA")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30E4")

    label("loc_30BA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30DA")
    OP_52(0xE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30E4")

    label("loc_30DA")

    OP_52(0xE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_30E4")

    OP_52(0xE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3181")

    #C0163
    ChrTalk(
        0xE,
        "（狼吞虎咽）……\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xE,
        (
            "嗯，虽然怀疑过这里的菜\x01",
            "会不会因为口感清淡而不够味道……\x01",
            "但结果却很不错呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_31DC")

    label("loc_3181")


    #C0165
    ChrTalk(
        0xE,
        (
            "呼呼……医院的饭菜\x01",
            "也不能小瞧。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xE,
        (
            "跟我平时吃的\x01",
            "垃圾食品比起来，\x01",
            "要美味一百倍呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31DC")

    SetChrSubChip(0xE, 0x0)
    TalkEnd(0xE)
    Return()

    # Function_12_3006 end

    def Function_13_31E4(): pass

    label("Function_13_31E4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3247")

    #C0167
    ChrTalk(
        0xFE,
        (
            "据说这里是护士们跟\x01",
            "医生们的房间。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "大家住在一起，\x01",
            "好像很快乐的样子。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3295")

    label("loc_3247")


    #C0169
    ChrTalk(
        0xFE,
        (
            "据说这里是护士们跟\x01",
            "医生们的房间。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "跟不认识的人住在一起\x01",
            "肯定很开心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3295")

    TalkEnd(0xFE)
    Return()

    # Function_13_31E4 end

    def Function_14_3299(): pass

    label("Function_14_3299")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch05302.itc", 0x22)
    LoadChrToIndex("chr/ch05300.itc", 0x23)
    OP_68(-6830, 1000, 10260, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, -13400, 200, 6850, 180)
    SetChrPos(0x102, -13700, 200, 3600, 0)
    SetChrPos(0x103, -12800, 200, 3600, 0)
    SetChrPos(0x104, -11900, 200, 3600, 0)
    SetChrChipByIndex(0xB, 0x22)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xB, -12300, 200, 6850, 180)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01300.itp")
    FadeToBright(1000, 0)
    OP_68(-12750, 1000, 5380, 6000)
    OP_0D()
    OP_6F(0x1)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0171
    AnonymousTalk(
        0xB,
        (
            "──初次见面，\x01",
            "我叫塞茜尔·诺伊艾丝。\x02\x03",

            "呵呵，我还以为是哪位，\x01",
            "原来是罗伊德的同事们啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0172
    ChrTalk(
        0x102,
        (
            "#0102F#6P是、是的……\x01",
            "我是艾莉·麦克道尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x103,
        (
            "#0203F#12P你好……\x01",
            "我是缇欧·普拉托。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x104,
        (
            "#0309F#2P我是兰迪·奥兰多！\x01",
            "今后也请多指教哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xB,
        (
            "#1302F#5P呵呵，请多指教。\x02\x03",

            "#1306F啊啊……\x01",
            "我真是太着急下结论了。\x02\x03",

            "还以为一定是罗伊德带着\x01",
            "女朋友来玩了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(500)

    #C0176
    ChrTalk(
        0x101,
        "#0011F#1P等等，姐姐你突然说些什么啊！？\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xB, 0x2)
    Sleep(200)

    #C0177
    ChrTalk(
        0xB,
        (
            "#1309F#11P因为已经三年没见了吧？\x02\x03",

            "我还想是不是已经有了\x01",
            "一两个女朋友，\x01",
            "准备介绍给姐姐认识呢。\x02\x03",

            "#1305F啊，难道\x01",
            "实际上是在交往，\x01",
            "却出于工作原因而不能公开……\x02\x03",

            "#1308F对、对不起，\x01",
            "好像问了不该问的事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        "#0006F#1P我、我说啊……\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xB,
        (
            "#1309F#11P那么……\x01",
            "到底是在跟谁交往呢？\x02\x03",

            "艾莉小姐？还是小缇欧？\x01",
            "还是说同时在跟两个人交往……\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        "#0001F#1P都说了不是啦！\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xB,
        (
            "#1305F#11P哈……\x01",
            "难、难道是在跟那边的男性……\x02\x03",

            "#1306F没关系，我会努力成为\x01",
            "理解那方面兴趣的好姐姐……\x02\x03",

            "#1301F一定会全力支持你的！\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x101,
        (
            "#0012F#1P不对！\x01",
            "这种事情应该反对才是吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x102,
        "#0109F#6P嘻嘻……\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x103,
        (
            "#0202F#12P感觉……\x01",
            "是个很有个性的姐姐呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x104,
        "#0309F#2P哈～天然呆的性格也很棒……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xBB8)

    #C0186
    ChrTalk(
        0x101,
        (
            "#0003F#1P──咳咳。\x02\x03",

            "#0001F说正事吧，塞茜尔姐姐。\x01",
            "我们是来调查魔兽骚乱事件的……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xB,
        (
            "#1303F#11P啊，对了。\x02\x03",

            "#1300F已经得到了护士长的允许，\x01",
            "就让我来说明吧……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xB, 0x0)
    Sleep(200)
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    #C0188
    ChrTalk(
        0xB,
        (
            "#1303F#5P……那是一周之前的晚上。\x02\x03",

            "我们医院的实习医生\x01",
            "被魔兽袭击了。\x02\x03",

            "#1301F但是，情况却有些奇怪……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x103,
        (
            "#0201F#12P我们看过警备队的调查书，\x01",
            "上面写着，那有可能\x01",
            "是被害者的错觉……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xB,
        (
            "#1306F#5P……是这样啊，\x01",
            "那边果然还是半信半疑的呢。\x02\x03",

            "#1301F我也不知道具体情况……\x01",
            "不过他似乎是在病房楼的楼顶上被袭击的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0191
    ChrTalk(
        0x101,
        "#0005F#1P楼顶……！？\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x102,
        "#0101F#6P这到底是怎么一回事呢……？\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xB,
        (
            "#1300F#5P那个，病房楼的楼顶\x01",
            "是个像庭院一样的露台。\x02\x03",

            "深处还建了一座研究楼，\x01",
            "很多医生都在里面。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x104,
        (
            "#0301F#2P原来如此……\x01",
            "也就是说，那是个不会有魔兽\x01",
            "出现的地方了？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xB,
        (
            "#1306F#5P没错……警备队的人们\x01",
            "最后也是这样判断的。\x02\x03",

            "#1308F可是，有些地方终究还是\x01",
            "让人无法释然。\x02\x03",

            "#1301F所以才拜托\x01",
            "你们来调查的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x101,
        (
            "#0006F#1P这、这个～……怎么说呢。\x02\x03",

            "#0008F说实话，我觉得那边并没有\x01",
            "对我们抱有那么大的期待……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xB, 0x2)
    Sleep(200)

    #C0197
    ChrTalk(
        0xB,
        (
            "#1302F#11P呵呵，不要谦虚。\x02\x03",

            "我读过克洛斯贝尔时代周刊了，\x01",
            "你们不是很努力吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0198
    ChrTalk(
        0x101,
        (
            "#0005F#1P啊……\x01",
            "对了，你是说旧城区的那起事件吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 1)), scpexpr(EXPR_END)), "loc_3E0B")

    #C0199
    ChrTalk(
        0x102,
        (
            "#0105F#6P但是最新的报道中，\x01",
            "并没有写解决事件的是我们……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E3A")

    label("loc_3E0B")


    #C0200
    ChrTalk(
        0x104,
        (
            "#0302F#12P莫非把我们的事迹\x01",
            "写得很帅吗！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E3A")

    Sleep(100)
    SetChrSubChip(0xB, 0x0)
    Sleep(200)

    #C0201
    ChrTalk(
        0xB,
        (
            "#1304F#5P呵呵，虽然没有那样写，\x01",
            "但也可以让我感觉到你们的努力了。\x02\x03",

            "#1302F而且在这之前，\x01",
            "有两个受伤的男孩子\x01",
            "住进了我们医院……\x02\x03",

            "我从来探望他们的孩子们那里\x01",
            "听说了一些事情。\x02\x03",

            "#1309F说是欠了\x01",
            "你们很大的人情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        "#0000F#1P这、这样啊……\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x102,
        "#0102F#6P呵呵，真是有趣的巧合呢。\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x104,
        "#0309F#2P哈哈～真让人害羞啊。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x103,
        (
            "#0203F#12P我想兰迪前辈当时的表现\x01",
            "并没有那么活跃……\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xB,
        (
            "#1303F#5P哦，对了……\x02\x03",

            "#1300F受害者本人就在医院里面，\x01",
            "你们最好还是直接去问问他吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x101,
        (
            "#0003F#1P嗯，方便的话，希望姐姐替我们介绍一下。\x02\x03",

            "#0001F还有……\x01",
            "我们想调查一下事发现场。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0xB, 0x2)
    Sleep(200)

    #C0208
    ChrTalk(
        0xB,
        (
            "#1302F#11P知道了，\x01",
            "两边都由我来带路吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(100)
    SetChrSubChip(0xB, 0x0)
    Sleep(200)
    Fade(250)
    SetChrChipByIndex(0xB, 0x23)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0xB, -12300, 0, 6400, 180)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0209
    ChrTalk(
        0x101,
        (
            "#0005F#1P啊，那个……\x01",
            "塞茜尔姐姐，你时间上没问题吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x10E, 0x1F4)

    #C0210
    ChrTalk(
        0xB,
        (
            "#1300F#11P嗯，现在刚好是\x01",
            "休息时间。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0xB4, 0x1F4)
    Sleep(300)

    #C0211
    ChrTalk(
        0xB,
        (
            "#1309F#5P那么我们先去\x01",
            "病房楼的二楼吧。\x02\x03",

            "大家跟我来哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x102,
        "#0102F#6P好的。\x02",
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x103,
        "#0204F#12P……明白。\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x104,
        "#0309F#2P我也一起！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0215
    ChrTalk(
        0x101,
        (
            "#0012F#5P（……大家一下子\x01",
            "　就跟塞茜尔姐姐混熟了呢。）\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(22750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7123", 0)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0xB, 0x80)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    AddParty(0x35, 0xFF, 0xFF)
    SetChrPos(0x0, -10400, 0, 6500, 90)
    SetScenarioFlags(0x62, 0)
    OP_29(0x3F, 0x1, 0x9)
    EventEnd(0x5)
    Return()

    # Function_14_3299 end

    def Function_15_42B6(): pass

    label("Function_15_42B6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch05302.itc", 0x22)
    LoadChrToIndex("chr/ch08202.itc", 0x23)
    OP_68(-9140, 1000, 9070, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(23610, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_4337")
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    Jump("loc_435E")

    label("loc_4337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_434D")
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    Jump("loc_435E")

    label("loc_434D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_435E")
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)

    label("loc_435E")

    SetChrFlags(0xEF, 0x4)
    SetChrChipByIndex(0x153, 0x23)
    SetChrSubChip(0x153, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x153, 0x4)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xEF, 0x4)
    SetChrPos(0x153, -13350, 300, 3500, 0)
    SetChrPos(0x101, -12350, 200, 3500, 0)
    SetChrChipByIndex(0xB, 0x22)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xB, -12350, 200, 6850, 180)
    SetChrPos(0xEF, -13350, 200, 6850, 180)
    FadeToBright(1000, 0)
    OP_68(-12880, 1200, 5390, 5000)
    OP_6F(0x1)
    OP_0D()

    #C0216
    ChrTalk(
        0xB,
        (
            "#1309F#5P呵呵，我稍微\x01",
            "有点着急下结论了。\x02\x03",

            "#1302F十八岁的罗伊德\x01",
            "不可能是九岁左右的小琪雅\x01",
            "的爸爸啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x101,
        (
            "#0006F#12P嗯……那不是理所当然的嘛。\x02\x03",

            "#0001F话说回来，为什么会产生我们\x01",
            "是父女这种奇怪的想法啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xB,
        (
            "#1306F#5P因为，总觉得很有\x01",
            "家人的感觉啊……\x02\x03",

            "#1300F所以我才自然而然地，将罗伊德\x01",
            "误会成小琪雅的爸爸了。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x101,
        "#0011F#12P咦……\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x153, 0x2)

    #C0220
    ChrTalk(
        0x153,
        (
            "#1105F#6P琪雅的爸爸\x01",
            "原来是罗伊德啊！？\x02\x03",

            "#1110F琪雅都不知道呢！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    SetChrSubChip(0x101, 0x1)

    #C0221
    ChrTalk(
        0x101,
        "#0012F#11P不是不是，都说了不是这样的！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x2)
    Sleep(150)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_46AD")

    #C0222
    ChrTalk(
        0xB,
        (
            "#1302F#11P呵呵……\x01",
            "艾莉，你看，\x02\x03",

            "他们两个人这样并排坐在一起，\x01",
            "看起来就像是父女吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x102,
        (
            "#0105F#5P啊……！\x01",
            "这么一说确实很像。\x02\x03",

            "#0104F虽然长相不像，\x01",
            "但就是有父女的感觉……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4816")

    label("loc_46AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_4765")

    #C0224
    ChrTalk(
        0xB,
        (
            "#1302F#11P呵呵……\x01",
            "小缇欧，你看，\x02\x03",

            "他们两个人这样并排坐在一起，\x01",
            "看起来就像是父女吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x103,
        (
            "#0205F#5P……说起来确实很像。\x02\x03",

            "#0204F虽然脸长得不像，\x01",
            "但是很有父女的感觉。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4816")

    label("loc_4765")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_4816")

    #C0226
    ChrTalk(
        0xB,
        (
            "#1302F#11P呵呵……\x01",
            "兰迪，你看，\x02\x03",

            "他们两个人这样并排坐在一起，\x01",
            "看起来就像是父女吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x104,
        (
            "#0305F#5P啊～确实是呢。\x02\x03",

            "#0309F虽然长得一点都不像，\x01",
            "但确实很有父女的感觉。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4816")


    #C0228
    ChrTalk(
        0x101,
        "#0011F#12P是、是那样的吗……？\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x153,
        (
            "#1104F#6P嘿嘿嘿～……\x01",
            "罗伊德是爸爸啊。\x02\x03",

            "#1100F……是不是不要叫罗伊德，\x01",
            "叫爸爸比较好呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x101,
        (
            "#0012F#11P呜……\x01",
            "跟以前一样叫就好了！\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x153,
        "#1103F#6P嗯，这样啊。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x153, 0x0)
    Sleep(300)

    #C0232
    ChrTalk(
        0x153,
        (
            "#1110F#12P但是但是，\x01",
            "塞茜尔真是个好人呢！\x02\x03",

            "#1109F琪雅最喜欢塞茜尔了！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    Sleep(150)

    #C0233
    ChrTalk(
        0xB,
        (
            "#1309F#5P呵呵……\x01",
            "我也最喜欢小琪雅了哦。\x02\x03",

            "我们很合得来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x153,
        "#1109F#12P嗯！\x02",
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    OP_63(0xB, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_4A01")

    #C0235
    ChrTalk(
        0x102,
        (
            "#0102F#5P（呵呵，关系瞬间\x01",
            "　就变得这么好了呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A7C")

    label("loc_4A01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_4A45")

    #C0236
    ChrTalk(
        0x103,
        (
            "#0202F#5P（呵呵，关系瞬间\x01",
            "　就变得这么好了呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A7C")

    label("loc_4A45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_4A7C")

    #C0237
    ChrTalk(
        0x104,
        (
            "#0300F#5P（哈哈，一眨眼就\x01",
            "　混熟了呢。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A7C")


    #C0238
    ChrTalk(
        0x101,
        (
            "#0006F#12P（呼，虽然值得高兴，\x01",
            "　但总觉得有点累啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xB,
        (
            "#1303F#5P……那么……\x01",
            "你们这次是为了小琪雅的记忆而来的吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0xEF, 0x1)

    #C0240
    ChrTalk(
        0x101,
        (
            "#0003F#12P啊，没错……\x01",
            "大致情况就如我之前所说。\x02\x03",

            "#0001F所以想带琪雅来\x01",
            "这所医院的『神经科』看看……\x02\x03",

            "拜托哪个医生比较好呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xB,
        (
            "#1304F#5P呵呵，其实你们应该\x01",
            "也见过的吧？\x02\x03",

            "#1300F就是约亚西姆·琼塔医生哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0242
    ChrTalk(
        0x101,
        (
            "#0005F#12P咦咦……\x01",
            "那个人是『神经科』的！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_4C8F")
    SetChrSubChip(0x102, 0x1)

    #C0243
    ChrTalk(
        0x102,
        "#0105F#6P是、是吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4CDC")

    label("loc_4C8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_4CB8")
    SetChrSubChip(0x103, 0x1)

    #C0244
    ChrTalk(
        0x103,
        "#0205F#6P是吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_4CDC")

    label("loc_4CB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_4CDC")
    SetChrSubChip(0x104, 0x1)

    #C0245
    ChrTalk(
        0x104,
        "#0305F#6P是吗……\x02",
    )

    CloseMessageWindow()

    label("loc_4CDC")


    #C0246
    ChrTalk(
        0xB,
        (
            "#1302F#5P呵呵，平时虽然是个喜欢钓鱼，\x01",
            "看起来很懒散的人……\x02\x03",

            "但是与外表不同，他在外国的医疗机关\x01",
            "可是取得了许多重大研究成果呢。\x02\x03",

            "而在这所医院里，他负责的是\x01",
            "『药物学』和『神经科』两个部门。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        (
            "#0000F#12P是、是这样啊……\x02\x03",

            "那么，关于琪雅，只要\x01",
            "去找那位医生谈一谈……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0xB,
        (
            "#1304F#5P嗯，我想一定\x01",
            "会对你们有所帮助的。\x02\x03",

            "#1302F快点去接待处，\x01",
            "让塞拉小姐帮忙联系一下吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(21610, 3000)
    OP_6F(0x10)
    OP_0D()
    SetScenarioFlags(0x5C, 0)
    NewScene("t1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_15_42B6 end

    def Function_16_4E6D(): pass

    label("Function_16_4E6D")

    EventBegin(0x0)
    Fade(500)
    OP_68(-10080, 1000, 14190, 0)
    MoveCamera(53, 28, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19140, 0)
    SetChrPos(0x101, -10300, 0, 13500, 270)
    SetChrPos(0x102, -10300, 0, 14700, 270)
    SetChrPos(0x103, -9100, 0, 13500, 270)
    SetChrPos(0x104, -9100, 0, 14700, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F16")
    SetChrPos(0x109, -9750, 0, 12300, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_4F41")

    label("loc_4F16")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F41")
    SetChrPos(0x10A, -9750, 0, 12300, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_4F41")

    SetChrSubChip(0x9, 0x1)
    OP_0D()

    #C0249
    ChrTalk(
        0x101,
        (
            "#11P#0000F那个，您是\x01",
            "芙萝拉小姐吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x9,
        (
            "#6P……哎呀，\x01",
            "找我有什么事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        (
            "#11P#0000F我们是克洛斯贝尔警察局·特别\x01",
            "任务支援科的人。\x02\x03",

            "受图书馆的委托，\x01",
            "来回收逾期未还\x01",
            "的书籍……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0252
    ChrTalk(
        0x9,
        "#6P啊，原来是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x9,
        (
            "#6P嗯，\x01",
            "虽然我很想把书还回去……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x9)

    #C0254
    ChrTalk(
        0x102,
        (
            "#11P#0105F难道有什么\x01",
            "无法返还的理由吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x9,
        "#6P嗯，算是吧……\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x9,
        (
            "#6P我经常把研究楼资料室里\x01",
            "的医书带出来，\x01",
            "在这里学习……\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x9,
        (
            "#6P然后在我把书放回资料室的书架上时，\x01",
            "好像不小心把图书馆的书也\x01",
            "一起放上去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x9,
        (
            "#6P等我发觉的时候，\x01",
            "已经忘记\x01",
            "放到哪里去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x103,
        "#11P#0203F……真是个粗心的人呢。\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x104,
        (
            "#11P#0306F算了，事已至此，\x01",
            "也没办法了。\x02\x03",

            "#0300F我也经常会忘记\x01",
            "自己到底将那些写真集\x01",
            "放到哪里去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x103,
        (
            "#11P#0211F……我觉得兰迪前辈的情况\x01",
            "跟这个完全不同。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x101,
        (
            "#11P#0006F总、总之……\x01",
            "逾期未还的书就在资料室的\x01",
            "书架上吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x9,
        (
            "#6P嗯，不会有错的。\x01",
            "虽然有点不好意思，\x01",
            "不过能替我找一找吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x9,
        (
            "#6P资料室就在病房楼\x01",
            "楼顶上的研究楼中。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x101,
        (
            "#11P#0003F我们以前也去过研究楼……\x01",
            "所以知道位置。\x02\x03",

            "#0000F好了，那么\x01",
            "就去找找看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x9, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5363")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_5363")

    SetChrPos(0x0, -10220, 0, 13340, 270)
    OP_29(0x28, 0x1, 0x8)
    EventEnd(0x5)
    Return()

    # Function_16_4E6D end

    def Function_17_537D(): pass

    label("Function_17_537D")

    EventBegin(0x1)

    #C0266
    ChrTalk(
        0x103,
        (
            "#0205F罗伊德前辈，\x01",
            "这下面是食堂……\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x101,
        (
            "#0005F哦，不是这里呢。\x02\x03",

            "#0001F……刚才那些堆在一起的\x01",
            "木箱跟集装箱是……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 9230, 3750, 13010, 0)
    EventEnd(0x4)
    Return()

    # Function_17_537D end

    def Function_18_540C(): pass

    label("Function_18_540C")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0268
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "探视者·门诊患者用住宿设施\x01",
            "※若要使用,请向宿舍长申请\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_18_540C end

    SaveToFile()

Try(main)
