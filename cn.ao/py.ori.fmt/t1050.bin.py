from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1050.bin",                # FileName
        "t1050",                    # MapName
        "t1050",                    # Location
        0x0042,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 66, 0, 3, 0, 4],
    )

    BuildStringList((
        "t1050",                  # 0
        "哈加经理",               # 1
        "洛琪",                   # 2
        "茜特拉丝",               # 3
        "技师",                   # 4
        "占卜师",                 # 5
        "琪雅",                   # 6
        "芙兰",                   # 7
        "塞茜尔",                 # 8
        "伊莉娅",                 # 9
        "莉夏",                   # 10
        "修利",                   # 11
        "玛丽亚贝尔",             # 12
    ))

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch25700.itc",                   # 01
        "chr/ch25600.itc",                   # 02
        "chr/ch26000.itc",                   # 03
        "chr/ch14202.itc",                   # 04
    ))

    DeclNpc(-479,    0,       10050,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-93959,  0,       8260,    0,    385,  0x0, 0,   1,   0,   0,   1,   0,   8,   255,  0)
    DeclNpc(-101819, 0,       8859,    90,   389,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(1059,    0,       10489,   177,  389,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-13359,  150,     15430,   90,   453,  0x0, 0,   4,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(5500,    0,       13500,   1200,    5500,    1500,    13500,   0x007C, 0,  30, 0x0000)
    DeclActor(-20,     0,       8270,    1500,    -480,    1500,    10050,   0x007E, 0,  6,  0x0000)
    DeclActor(12010,   0,       15830,   1200,    12010,   450,     15830,   0x007C, 0,  5,  0x0000)
    DeclActor(1260,    0,       9210,    1500,    1060,    1500,    10490,   0x007E, 0,  11, 0x0000)

    ChipFrameInfo(772, 0)                                        # 0

    ScpFunction((
        "Function_0_304",          # 00, 0
        "Function_1_3BC",          # 01, 1
        "Function_2_41D",          # 02, 2
        "Function_3_47E",          # 03, 3
        "Function_4_586",          # 04, 4
        "Function_5_5D3",          # 05, 5
        "Function_6_680",          # 06, 6
        "Function_7_684",          # 07, 7
        "Function_8_EA3",          # 08, 8
        "Function_9_1317",         # 09, 9
        "Function_10_142C",        # 0A, 10
        "Function_11_168B",        # 0B, 11
        "Function_12_168F",        # 0C, 12
        "Function_13_1844",        # 0D, 13
        "Function_14_23CD",        # 0E, 14
        "Function_15_242D",        # 0F, 15
        "Function_16_2919",        # 10, 16
        "Function_17_2BD6",        # 11, 17
        "Function_18_2C52",        # 12, 18
        "Function_19_2CD3",        # 13, 19
        "Function_20_2D54",        # 14, 20
        "Function_21_2DD5",        # 15, 21
        "Function_22_2E56",        # 16, 22
        "Function_23_2ED7",        # 17, 23
        "Function_24_2F58",        # 18, 24
        "Function_25_2FD9",        # 19, 25
        "Function_26_305A",        # 1A, 26
        "Function_27_30DB",        # 1B, 27
        "Function_28_315C",        # 1C, 28
        "Function_29_31DD",        # 1D, 29
        "Function_30_325E",        # 1E, 30
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

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_41C")
    OP_95(0xFE, -106030, 0, 8260, 2000, 0x0)
    OP_95(0xFE, -106030, 0, 11300, 2000, 0x0)
    OP_95(0xFE, -93960, 0, 11300, 2000, 0x0)
    OP_95(0xFE, -93960, 0, 8260, 2000, 0x0)
    Jump("Function_1_3BC")

    label("loc_41C")

    Return()

    # Function_1_3BC end

    def Function_2_41D(): pass

    label("Function_2_41D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_47D")
    OP_95(0xFE, 106130, 0, 11580, 2000, 0x0)
    OP_95(0xFE, 106130, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 8150, 2000, 0x0)
    OP_95(0xFE, 94190, 0, 11580, 2000, 0x0)
    Jump("Function_2_41D")

    label("loc_47D")

    Return()

    # Function_2_41D end

    def Function_3_47E(): pass

    label("Function_3_47E")

    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4C8")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 106130, 0, 11580, 0)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_576")

    label("loc_4C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_521")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 4270, 0, 7670, 90)
    BeginChrThread(0x9, 0, 0, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 5450, 0, 7670, 270)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51C")
    SetChrFlags(0xC, 0x10)

    label("loc_51C")

    Jump("loc_576")

    label("loc_521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_52F")
    Jump("loc_576")

    label("loc_52F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_568")
    BeginChrThread(0x9, 0, 0, 0)
    SetChrPos(0x9, -100710, 0, 8860, 270)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_576")

    label("loc_568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_576")
    ClearChrFlags(0x9, 0x80)

    label("loc_576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_585")
    ClearScenarioFlags(0x22, 0)
    Event(0, 16)

    label("loc_585")

    Return()

    # Function_3_47E end

    def Function_4_586(): pass

    label("Function_4_586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_598")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_598")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_END)), "loc_5AF")
    ClearMapObjFlags(0x0, 0x10)
    OP_66(0x0, 0x1)

    label("loc_5AF")

    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5C5")
    OP_66(0x3, 0x1)
    Jump("loc_5D2")

    label("loc_5C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5D2")
    OP_66(0x3, 0x1)

    label("loc_5D2")

    Return()

    # Function_4_586 end

    def Function_5_5D3(): pass

    label("Function_5_5D3")

    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "摆放着《恋爱假日　精选食谱集》。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('料理手册', 0x0)"), scpexpr(EXPR_END)), "loc_67C")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B2(0x15)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『考究抹茶拿铁』\x07\x00",
            "的做法已经学会了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_67C")

    TalkEnd(0xFF)
    Return()

    # Function_5_5D3 end

    def Function_6_680(): pass

    label("Function_6_680")

    Call(0, 7)
    Return()

    # Function_6_680 end

    def Function_7_684(): pass

    label("Function_7_684")

    TalkBegin(0x8)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_691")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E9F")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "休息\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E1")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_6E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_701")
    OP_AF(0x64)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E9A")

    label("loc_701")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E9A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_883")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_808")

    #C0003
    ChrTalk(
        0x8,
        (
            "市里的骚乱已经平息了下来，\x01",
            "大家正在检查酒店内的状况。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "话说回来，那棵不可思议的蓝白色大树……\x01",
            "离近望去的话，更觉得诡异了。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "我想各位应该明白，以目前这种状况来看，\x01",
            "米修拉姆很难在短时间内重新开放了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_87E")

    label("loc_808")


    #C0006
    ChrTalk(
        0x8,
        (
            "虽然米修拉姆很难在短时间内重新开放……\x01",
            "但各位难得来此，我们自会用心接待。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "如果想去房间内休息，\x01",
            "请尽管吩咐。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_87E")

    Jump("loc_E9A")

    label("loc_883")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_9A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_944")
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0008
    ChrTalk(
        0x8,
        (
            "呀，罗伊德先生……\x01",
            "欢迎光临。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "虽然本酒店正在停业中，\x01",
            "但我们一直都在用心准备，\x01",
            "以保证随时可以接待客人。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        "如果需要休息，请尽管吩咐。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_99C")

    label("loc_944")


    #C0011
    ChrTalk(
        0x8,
        (
            "唔，话说回来，\x01",
            "为何会响起那种钟声……？\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "奇幻乐园应该也在停业中……\x01",
            "真奇怪啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99C")

    Jump("loc_E9A")

    label("loc_9A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_9AF")
    Jump("loc_E9A")

    label("loc_9AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_C76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B84")

    #C0013
    ChrTalk(
        0x8,
        (
            "哦哦，罗伊德先生，还有琪雅小朋友，\x01",
            "你们回来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        "你们两个在一起，真是太好了。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x153,
        "#01110F嘿嘿嘿，我回来啦。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        "#00002F哈哈，让您担心了，真是不好意思。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        "哪里哪里，没有的事……\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "哦，对了，您的同伴们\x01",
            "刚才已经出门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "他们说，把要办的事情办完之后，\x01",
            "就直接去约定的地方集合……\x01",
            "你们二位也尽快出发为好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00004F说的没错，\x01",
            "谢谢您了。\x02\x03",

            "#00000F好，把要办的事情\x01",
            "都办完之后，\x01",
            "我们也去主题公园吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x153,
        "#01109F嗯！出发！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15A, 7)
    Jump("loc_C71")

    label("loc_B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C23")

    #C0022
    ChrTalk(
        0x8,
        (
            "您的同伴们\x01",
            "刚才已经出门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "他们说，把要办的事情办完之后，\x01",
            "就直接去约定的地方集合……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "罗伊德先生，\x01",
            "你们二位也尽快出发为好吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C71")

    label("loc_C23")


    #C0025
    ChrTalk(
        0x8,
        (
            "您的同伴们\x01",
            "刚才已经出门了。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "罗伊德先生，\x01",
            "你们二位也尽快出发为好吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C71")

    Jump("loc_E9A")

    label("loc_C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_D69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D20")

    #C0027
    ChrTalk(
        0x8,
        (
            "琪雅小朋友刚才\x01",
            "一个人出去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "出于谨慎，我当时叫住了她，\x01",
            "但她让我不用担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        (
            "#00003F（琪雅……\x01",
            "  看来还是去酒店外\x01",
            "  寻找为好。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D64")

    label("loc_D20")


    #C0030
    ChrTalk(
        0x8,
        (
            "琪雅小朋友刚才\x01",
            "一个人出去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "唔，她到底\x01",
            "去什么地方了呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D64")

    Jump("loc_E9A")

    label("loc_D69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_E9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E31")

    #C0032
    ChrTalk(
        0x8,
        (
            "哦，各位客人……\x01",
            "三层贵宾区的\x01",
            "感觉还好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#00000F嗯，非常舒适。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        "那真是再好不过了。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "如果您觉得我们有什么不足之处，\x01",
            "还请随时指出。\x01",
            "我们一定会立刻改进的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E9A")

    label("loc_E31")


    #C0036
    ChrTalk(
        0x8,
        (
            "三层贵宾区的\x01",
            "感觉还好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "如果您觉得我们有什么不足之处，\x01",
            "还请随时指出。\x01",
            "我们一定会立刻改进的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E9A")

    Jump("loc_691")

    label("loc_E9F")

    TalkEnd(0x8)
    Return()

    # Function_7_684 end

    def Function_8_EA3(): pass

    label("Function_8_EA3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_FB1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F39")

    #C0038
    ChrTalk(
        0x9,
        (
            "一段时间无人打扫，\x01",
            "这里就堆积了很多灰尘呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x9,
        (
            "呼……虽然那棵蓝白色的大树让人很不安，\x01",
            "但扫除还是必须要认真做好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_FAC")

    label("loc_F39")


    #C0040
    ChrTalk(
        0x9,
        (
            "为了确保酒店能够随时恢复营业，\x01",
            "我会定期来打扫卫生……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x9,
        (
            "那棵蓝白色的大树\x01",
            "离这里这么近，\x01",
            "真是让人很不安啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FAC")

    Jump("loc_1313")

    label("loc_FB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_10EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1078")

    #C0042
    ChrTalk(
        0x9,
        (
            "就任国防长官的\x01",
            "亚里欧斯先生\x01",
            "刚才从商店街经过。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        (
            "他还带着一个\x01",
            "可爱的小女孩……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#00001F（亚里欧斯先生和琪雅……\x01",
            "  果然来这里了啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x102,
        "#00101F（赶快追吧。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_10E7")

    label("loc_1078")


    #C0046
    ChrTalk(
        0x9,
        (
            "国防长官亚里欧斯先生\x01",
            "刚才从商店街经过。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x9,
        (
            "他带着一个小女孩，\x01",
            "好像去了主题公园那边……\x01",
            "到底要做什么呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10E7")

    Jump("loc_1313")

    label("loc_10EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_10FA")
    Jump("loc_1313")

    label("loc_10FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_115D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1115")
    Call(0, 9)
    Jump("loc_1158")

    label("loc_1115")


    #C0048
    ChrTalk(
        0xFE,
        (
            "拜托了～\x01",
            "让我为瓦吉先生服务吧～！\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        "下次我请你吃冰激凌～！\x02",
    )

    CloseMessageWindow()

    label("loc_1158")

    Jump("loc_1313")

    label("loc_115D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1313")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12AC")
    TurnDirection(0xFE, 0x105, 0)

    #C0050
    ChrTalk(
        0xFE,
        "哎，客人是……瓦吉先生！？\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "莫、莫非今天\x01",
            "预订贵宾区的\x01",
            "客人就是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x105,
        (
            "#10300F哦，应该就是\x01",
            "我们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        "！！！！！！\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "（我、我……\x01",
            "  我为何偏偏在这种日子\x01",
            "  负责普通区的服务啊！！）\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#00005F虽、虽然不知道是怎么回事，\x01",
            "但她好像受了不小的打击呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x105,
        "#10302F呵呵，真是个奇怪的孩子。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1313")

    label("loc_12AC")


    #C0057
    ChrTalk(
        0xFE,
        (
            "我、我……\x01",
            "我为何偏偏在这种日子\x01",
            "负责普通区的服务呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "难得有个可以为\x01",
            "瓦吉先生服务的好机会……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1313")

    TalkEnd(0xFE)
    Return()

    # Function_8_EA3 end

    def Function_9_1317(): pass

    label("Function_9_1317")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0059
    ChrTalk(
        0x9,
        "茜特拉丝，求你啦！\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "今天就让我来负责贵宾区，\x01",
            "给瓦吉先生服务吧～！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xA,
        (
            "在工作时突然把我叫过来，\x01",
            "还以为有什么事呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xA,
        (
            "当初明明是你自己说什么\x01",
            "『贵宾区的服务工作太麻烦了』，\x01",
            "然后硬推给了我。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "那、那种小事就不要在意啦～\x01",
            "下次我请你吃冰激凌～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_9_1317 end

    def Function_10_142C(): pass

    label("Function_10_142C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1546")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14DE")

    #C0064
    ChrTalk(
        0xA,
        (
            "听说麦克道尔议长他们\x01",
            "当时被囚禁在了\x01",
            "迎宾馆。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xA,
        (
            "而且总统还让袭击城市的\x01",
            "那些猎兵在那里看守。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xA,
        (
            "虽说是为了独立，\x01",
            "但总统做得真是很过分啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1541")

    label("loc_14DE")


    #C0067
    ChrTalk(
        0xA,
        (
            "听说麦克道尔议长他们\x01",
            "当时被囚禁在了\x01",
            "迎宾馆。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xA,
        (
            "总统做得十分过分呢……\x01",
            "他被拘捕真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1541")

    Jump("loc_1687")

    label("loc_1546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1609")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15D5")

    #C0069
    ChrTalk(
        0xA,
        (
            "坐在那边的那位女士\x01",
            "就是在主题公园工作的占卜师吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xA,
        (
            "不知何时，她就出现在那里了……\x01",
            "她平时都住在什么地方呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1604")

    label("loc_15D5")


    #C0071
    ChrTalk(
        0xA,
        (
            "……哦，不闲聊了，\x01",
            "还是赶快把扫除做完吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1604")

    Jump("loc_1687")

    label("loc_1609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_1617")
    Jump("loc_1687")

    label("loc_1617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_167E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1632")
    Call(0, 9)
    Jump("loc_1679")

    label("loc_1632")


    #C0072
    ChrTalk(
        0xFE,
        (
            "哎，既然你都这么说了，\x01",
            "让给你倒也没什么……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        "你可真是任性啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1679")

    Jump("loc_1687")

    label("loc_167E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_1687")

    label("loc_1687")

    TalkEnd(0xFE)
    Return()

    # Function_10_142C end

    def Function_11_168B(): pass

    label("Function_11_168B")

    Call(0, 12)
    Return()

    # Function_11_168B end

    def Function_12_168F(): pass

    label("Function_12_168F")

    TalkBegin(0xB)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_169C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1840")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",            # 0
            "改造·合成\x01",      # 1
            "放弃\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_16F2")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_16F2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1712")
    OP_AF(0x65)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_183B")

    label("loc_1712")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_183B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_17B0")

    #C0074
    ChrTalk(
        0xB,
        (
            "明明出现了那种\x01",
            "来历不明的诡异之物，\x01",
            "这里的职员们还真是处乱不惊。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xB,
        (
            "……真想尽快完成检修工作，\x01",
            "早点离开这里啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_183B")

    label("loc_17B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_183B")

    #C0076
    ChrTalk(
        0xB,
        (
            "我正在和酒店的各位员工\x01",
            "趁停业期间一起检修\x01",
            "各种设备。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xB,
        (
            "你们要是有什么事情，\x01",
            "不必客气，尽管和我说。\x01",
            "我可以在空闲时帮帮忙。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_183B")

    Jump("loc_169C")

    label("loc_1840")

    TalkEnd(0xB)
    Return()

    # Function_12_168F end

    def Function_13_1844(): pass

    label("Function_13_1844")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1E48")
    Call(0, 14)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B21")
    EventBegin(0x0)
    Fade(500)
    OP_68(-13160, 1200, 13150, 0)
    MoveCamera(320, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(17640, 0)
    SetChrPos(0x101, -12560, 0, 13000, 0)
    SetChrPos(0x102, -13820, 0, 12710, 45)
    SetChrPos(0x103, -12700, 0, 11800, 0)
    SetChrPos(0x104, -13690, 0, 13610, 45)
    SetChrPos(0xF4, -14000, 0, 11480, 45)
    SetChrPos(0xF5, -14760, 0, 12870, 50)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xC, 0x2)
    OP_0D()

    #C0078
    ChrTalk(
        0xC,
        "#11P啊，那些书……\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xC,
        (
            "#11P不是我在克洛斯贝尔市\x01",
            "时常看到的《沐浴阳光的阿尼艾丝》吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        "#6P#00005F哎，是指这些小说吗？\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x102,
        "#6P#00100F我们已经收集到全套了。\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xC,
        "#11P呵呵，真了不起啊。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xC,
        (
            "#11P我以前也有过\x01",
            "这部小说，\x01",
            "当时看得非常开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xC,
        (
            "#11P虽说是虚构的故事……\x01",
            "但现实中的某人与书中的少女主人公\x01",
            "似乎有一些共通之处呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xC,
        (
            "#11P我准备在这里\x01",
            "继续观望克洛斯贝尔\x01",
            "事件的发展……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xC,
        (
            "#11P要是可以在余暇时看看这部小说，\x01",
            "感觉应该会很不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#6P#00004F（既然如此，要不要\x01",
            "  把小说送给这个人呢……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18A, 5)
    Call(0, 15)
    Jump("loc_1E43")

    label("loc_1B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CA3")
    EventBegin(0x0)
    Fade(500)
    OP_68(-13160, 1200, 13150, 0)
    MoveCamera(320, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(17640, 0)
    SetChrPos(0x101, -12560, 0, 13000, 0)
    SetChrPos(0x102, -13820, 0, 12710, 45)
    SetChrPos(0x103, -12700, 0, 11800, 0)
    SetChrPos(0x104, -13690, 0, 13610, 45)
    SetChrPos(0xF4, -14000, 0, 11480, 45)
    SetChrPos(0xF5, -11330, 0, 11290, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xC, 0x2)
    OP_0D()

    #C0088
    ChrTalk(
        0xC,
        (
            "#11P那些书是我在克洛斯贝尔市\x01",
            "时常看到的《沐浴阳光的阿尼艾丝》呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xC,
        (
            "#11P我准备在这里\x01",
            "旁观克洛斯贝尔\x01",
            "事件的发展……\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xC,
        (
            "#11P要是可以在余暇时看看这部小说，\x01",
            "感觉应该会很不错呢。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 15)
    Jump("loc_1E43")

    label("loc_1CA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DB7")

    #C0091
    ChrTalk(
        0xC,
        (
            "碧之大树……\x01",
            "竟然会出现如此惊人的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xC,
        (
            "塔罗牌、水晶、占星……\x01",
            "我用尽了一切占卜方法，也无法\x01",
            "预测到克洛斯贝尔接下来的命运。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xC,
        (
            "呵呵，真有趣……\x01",
            "这样的情况还是第一次遇到呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xC,
        (
            "克洛斯贝尔究竟会\x01",
            "迎来怎样的未来呢……\x01",
            "我就在这里见证接下来的发展吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1E43")

    label("loc_1DB7")


    #C0095
    ChrTalk(
        0xC,
        (
            "呵呵……也许连『他们』\x01",
            "都没有预料到事态会\x01",
            "发展到如此程度吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xC,
        (
            "克洛斯贝尔究竟会\x01",
            "迎来怎样的未来呢……\x01",
            "我就在这里见证接下来的发展吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E43")

    Jump("loc_23C9")

    label("loc_1E48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_23C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22C8")

    #C0097
    ChrTalk(
        0xC,
        "嗯…………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF), scpexpr(EXPR_AND), scpexpr(EXPR_END)), "loc_1F10")

    #C0098
    ChrTalk(
        0x101,
        (
            "#00005F（这个人……\x01",
            "  好像是主题公园的占卜师吧？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F2F")

    label("loc_1F10")


    #C0099
    ChrTalk(
        0x101,
        "#00005F（这个人是……？）\x02",
    )

    CloseMessageWindow()

    label("loc_1F2F")


    #C0100
    ChrTalk(
        0x102,
        (
            "#00105F（她的面前摆放着\x01",
            "  数张塔罗牌……）\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1FF0")
    Jump("loc_203A")

    label("loc_1FF0")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2010")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_203A")

    label("loc_2010")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2030")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_203A")

    label("loc_2030")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_203A")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    #C0101
    ChrTalk(
        0xC,
        "……请小心。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xC,
        (
            "如果你们准备继续前进……\x01",
            "恐怕将会踏上\x01",
            "极其艰险的道路。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0103
    ChrTalk(
        0x103,
        "#00201F………………！？\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x104,
        "#00305F这、这是什么意思呢……？\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xC,
        (
            "嗯……这种难以解释的组合\x01",
            "究竟该如何解读呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xC,
        (
            "总之，如果你们想继续前进，\x01",
            "最好做足充分的心理准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xC,
        (
            "能否克服无数困难，\x01",
            "保护好最重要的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xC,
        (
            "那就要取决于\x01",
            "你们自身了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)

    #C0109
    ChrTalk(
        0x101,
        (
            "#00003F……虽然不是很明白……\x01",
            "但我会铭记在心的。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xC,
        "呵呵，祝你们此行顺利。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x191, 7)
    SetChrSubChip(0xC, 0x0)
    Jump("loc_23C9")

    label("loc_22C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_237A")

    #C0111
    ChrTalk(
        0xC,
        (
            "如果你们想继续前进，\x01",
            "最好做足充分的心理准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xC,
        (
            "能否克服无数困难，\x01",
            "保护好最重要的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xC,
        (
            "那就要取决于\x01",
            "你们自身了。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xC,
        "呵呵，祝你们此行顺利。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xC, 0x10)
    Jump("loc_23C9")

    label("loc_237A")


    #C0115
    ChrTalk(
        0xC,
        (
            "你们能否克服种种困难，\x01",
            "保护好最重要的人呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xC,
        "呵呵，祝你们此行顺利。\x02",
    )

    CloseMessageWindow()

    label("loc_23C9")

    TalkEnd(0xFE)
    Return()

    # Function_13_1844 end

    def Function_14_23CD(): pass

    label("Function_14_23CD")

    ClearScenarioFlags(0x0, 5)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝１卷', 0x0)"), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝２卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝３卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝４卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝５卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝６卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝７卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝８卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝９卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝10卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝11卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝12卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝13卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('沐浴阳光的阿尼艾丝14卷', 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_242C")
    SetScenarioFlags(0x0, 5)

    label("loc_242C")

    Return()

    # Function_14_23CD end

    def Function_15_242D(): pass

    label("Function_15_242D")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "赠送小说\x01",      # 0
            "不赠送\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28C2")

    #C0117
    ChrTalk(
        0x101,
        (
            "#6P#00000F如不嫌弃……\x01",
            "就请把这些书收下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xC,
        "#11P啊……可以吗？\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x103,
        (
            "#6P#00200F说起来……\x01",
            "这些书也几乎都是别人送给我们的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x104,
        "#6P#00300F不用客气，请收下吧。\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xC,
        (
            "#11P呵呵，那我就\x01",
            "心怀感激地收下啦。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0122
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将全套《沐浴阳光的阿尼艾丝》交了出去。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SubItemNumber('沐浴阳光的阿尼艾丝１卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝２卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝３卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝４卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝５卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝６卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝７卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝８卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝９卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝10卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝11卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝12卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝13卷', 1)
    SubItemNumber('沐浴阳光的阿尼艾丝14卷', 1)

    #C0123
    ChrTalk(
        0xC,
        "#11P……对了。\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xC,
        (
            "#11P说是回赠也许不太礼貌，\x01",
            "不过，就把这个送给你们好了。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0125
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x396),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('塞姆里亚石', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0126
    ChrTalk(
        0x101,
        "#6P#00005F这是……\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xC,
        (
            "#11P这是我以前从某个\x01",
            "特殊渠道得到的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xC,
        (
            "#11P不知你们能否\x01",
            "用得上……\x01",
            "如果不嫌弃，就请拿去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x102,
        (
            "#6P#00105F那个……真的可以吗？\x01",
            "把看起来这么贵重的东西送给我们……\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xC,
        "#11P呵呵，不必在意。\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xC,
        (
            "#11P在克洛斯贝尔的这起事件中，\x01",
            "我仅仅是一名旁观者而已……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xC,
        (
            "#11P不过，如果只是这种程度的介入，\x01",
            "应该不会有人不满的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x4, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x5, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0133
    ChrTalk(
        0xC,
        "#11P呵呵……没什么，我只是自言自语罢了。\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xC,
        "#11P如果可以，希望你们用心保管。\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        "#6P#00000F那个……谢谢了。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x18A, 6)
    Jump("loc_28E9")

    label("loc_28C2")


    #C0136
    ChrTalk(
        0x101,
        "#6P#00000F（嗯……还是算了吧。）\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_28E9")

    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -12560, 0, 13000, 0)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_15_242D end

    def Function_16_2919(): pass

    label("Function_16_2919")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("chr/ch08500.itc", 0x1F)
    LoadChrToIndex("chr/ch05200.itc", 0x20)
    LoadChrToIndex("chr/ch05100.itc", 0x21)
    LoadChrToIndex("chr/ch07500.itc", 0x22)
    LoadChrToIndex("chr/ch10000.itc", 0x23)
    LoadChrToIndex("chr/ch05500.itc", 0x24)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x1F)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x101, 0, 0, 0, 0)
    SetChrPos(0x102, 0, 0, 0, 0)
    SetChrPos(0x103, 0, 0, 0, 0)
    SetChrPos(0x104, 0, 0, 0, 0)
    SetChrPos(0x109, 0, 0, 0, 0)
    SetChrPos(0x105, 0, 0, 0, 0)
    SetChrPos(0xD, 0, 0, 0, 0)
    SetChrPos(0xE, 0, 0, 0, 0)
    SetChrPos(0x10, 0, 0, 0, 0)
    SetChrPos(0xF, 0, 0, 0, 0)
    SetChrPos(0x11, 0, 0, 0, 0)
    SetChrPos(0x12, 0, 0, 0, 0)
    SetChrPos(0x13, 0, 0, 0, 0)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0xE, 0x4)
    ClearChrFlags(0x10, 0x4)
    ClearChrFlags(0xF, 0x4)
    ClearChrFlags(0x11, 0x4)
    ClearChrFlags(0x12, 0x4)
    ClearChrFlags(0x13, 0x4)
    ClearMapObjFlags(0x0, 0x10)
    OP_68(4140, 1000, 8840, 0)
    MoveCamera(315, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23500, 0)
    FadeToBright(1000, 0)
    OP_68(5450, 1000, 10150, 6000)
    BeginChrThread(0x13, 3, 0, 17)
    BeginChrThread(0x10, 3, 0, 18)
    BeginChrThread(0xF, 3, 0, 19)
    BeginChrThread(0xE, 3, 0, 20)
    BeginChrThread(0x11, 3, 0, 22)
    BeginChrThread(0x12, 3, 0, 23)
    BeginChrThread(0xD, 3, 0, 24)
    BeginChrThread(0x102, 3, 0, 25)
    BeginChrThread(0x103, 3, 0, 26)
    BeginChrThread(0x109, 3, 0, 21)
    BeginChrThread(0x105, 3, 0, 29)
    BeginChrThread(0x101, 3, 0, 27)
    BeginChrThread(0x104, 3, 0, 28)
    OP_6F(0x79)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x103, 0x3)
    EndChrThread(0x104, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    EndChrThread(0x10, 0x3)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x11, 0x3)
    EndChrThread(0x12, 0x3)
    EndChrThread(0x13, 0x3)
    SetMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("t1080", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_2919 end

    def Function_17_2BD6(): pass

    label("Function_17_2BD6")

    SetChrPos(0xFE, 3500, 0, 5500, 90)
    OP_9B(0x0, 0xFE, 0xFFD3, 0xFA0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x10CC, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xFFD3, 0x3E8, 0x7D0, 0x1)
    Sound(121, 0, 100, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x0)

    def lambda_2C32():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C32)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_17_2BD6 end

    def Function_18_2C52(): pass

    label("Function_18_2C52")

    SetChrPos(0xFE, 1300, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_2CB3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2CB3)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_18_2C52 end

    def Function_19_2CD3(): pass

    label("Function_19_2CD3")

    SetChrPos(0xFE, 1300, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_2D34():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2D34)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_19_2CD3 end

    def Function_20_2D54(): pass

    label("Function_20_2D54")

    SetChrPos(0xFE, -600, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1518, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_2DB5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2DB5)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_20_2D54 end

    def Function_21_2DD5(): pass

    label("Function_21_2DD5")

    SetChrPos(0xFE, -600, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1518, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_2E36():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E36)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_21_2DD5 end

    def Function_22_2E56(): pass

    label("Function_22_2E56")

    SetChrPos(0xFE, -2500, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1E78, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_2EB7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2EB7)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_22_2E56 end

    def Function_23_2ED7(): pass

    label("Function_23_2ED7")

    SetChrPos(0xFE, -2500, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1E78, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_2F38():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2F38)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_23_2ED7 end

    def Function_24_2F58(): pass

    label("Function_24_2F58")

    SetChrPos(0xFE, -4400, 0, 5500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x251C, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_2FB9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2FB9)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_24_2F58 end

    def Function_25_2FD9(): pass

    label("Function_25_2FD9")

    SetChrPos(0xFE, -6300, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2C88, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_303A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_303A)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_25_2FD9 end

    def Function_26_305A(): pass

    label("Function_26_305A")

    SetChrPos(0xFE, -6300, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2C88, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_30BB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_30BB)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_26_305A end

    def Function_27_30DB(): pass

    label("Function_27_30DB")

    SetChrPos(0xFE, -8200, 0, 5500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x33F4, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_313C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_313C)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_27_30DB end

    def Function_28_315C(): pass

    label("Function_28_315C")

    SetChrPos(0xFE, -10100, 0, 6200, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x3B60, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_31BD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_31BD)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_28_315C end

    def Function_29_31DD(): pass

    label("Function_29_31DD")

    SetChrPos(0xFE, -10100, 0, 4800, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x3B60, 0x7D0, 0x1)
    OP_95(0xFE, 6330, 0, 8330, 2000, 0x1)
    OP_95(0xFE, 6330, 0, 12630, 2000, 0x1)
    OP_95(0xFE, 5620, 0, 13340, 2000, 0x1)

    def lambda_323E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_323E)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_29_31DD end

    def Function_30_325E(): pass

    label("Function_30_325E")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0137
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "～楼梯间～\x01",
            "三层贵宾区\x01",
            "已被包场，\x01",
            "请勿入内。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_30_325E end

    SaveToFile()

Try(main)
