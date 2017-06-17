from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0340.bin",                # FileName
        "c0340",                    # MapName
        "c0340",                    # Location
        0x002D,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 45, 0, 6, 0, 7],
    )

    BuildStringList((
        "c0340",                  # 0
        "伊兹丽夫人",             # 1
        "菲利克",                 # 2
        "辛迪",                   # 3
        "伊兹丽夫人",             # 4
        "亨利",                   # 5
        "约库斯",                 # 6
    ))

    AddCharChip((
        "chr/ch21700.itc",                   # 00
        "chr/ch21702.itc",                   # 01
        "chr/ch22000.itc",                   # 02
        "chr/ch22100.itc",                   # 03
        "chr/ch22200.itc",                   # 04
        "chr/ch27600.itc",                   # 05
    ))

    DeclNpc(40669,   0,       9600,    360,  389,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(32659,   0,       5679,    180,  261,  0x0, 0,   2,   0,   0,   3,   0,   10,  255,  0)
    DeclNpc(4980,    0,       8989,    89,   261,  0x0, 0,   3,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(36700,   250,     2000,    270,  261,  0x0, 0,   1,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(5329,    0,       3990,    90,   389,  0x0, 0,   4,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(689,     0,       990,     225,  389,  0x0, 0,   5,   0,   0,   2,   0,   15,  255,  0)

    ScpFunction((
        "Function_0_194",          # 00, 0
        "Function_1_24C",          # 01, 1
        "Function_2_359",          # 02, 2
        "Function_3_384",          # 03, 3
        "Function_4_3AF",          # 04, 4
        "Function_5_3FC",          # 05, 5
        "Function_6_427",          # 06, 6
        "Function_7_7A7",          # 07, 7
        "Function_8_7FA",          # 08, 8
        "Function_9_D69",          # 09, 9
        "Function_10_17B7",        # 0A, 10
        "Function_11_2431",        # 0B, 11
        "Function_12_24D4",        # 0C, 12
        "Function_13_2ED0",        # 0D, 13
        "Function_14_2F8F",        # 0E, 14
        "Function_15_32D1",        # 0F, 15
    ))


    def Function_0_194(): pass

    label("Function_0_194")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1D4"),
        (1, "loc_1E0"),
        (2, "loc_1EC"),
        (3, "loc_1F8"),
        (4, "loc_204"),
        (5, "loc_210"),
        (6, "loc_21C"),
        (SWITCH_DEFAULT, "loc_228"),
    )


    label("loc_1D4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_1E0")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_1EC")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_1F8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_204")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_210")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_21C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_228")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_234")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_24B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_234")

    label("loc_24B")

    Return()

    # Function_0_194 end

    def Function_1_24C(): pass

    label("Function_1_24C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_358")

    def lambda_25C():
        OP_96(0x8, 0x9858, 0x0, 0x2008, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_25C)

    def lambda_276():
        OP_96(0x9, 0x9858, 0x0, 0x22F6, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_276)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    Sleep(200)

    def lambda_29B():
        OP_96(0x8, 0x9664, 0x0, 0x1E78, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_29B)

    def lambda_2B5():
        OP_96(0x9, 0x9664, 0x0, 0x2166, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2B5)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    Sleep(200)

    def lambda_2DA():
        OP_96(0x8, 0x9858, 0x0, 0x1DB0, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2DA)

    def lambda_2F4():
        OP_96(0x9, 0x9858, 0x0, 0x209E, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2F4)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    Sleep(200)

    def lambda_319():
        OP_96(0x8, 0x9A4C, 0x0, 0x1EDC, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_319)

    def lambda_333():
        OP_96(0x9, 0x9A4C, 0x0, 0x21CA, 0x384, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_333)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    Sleep(200)
    Jump("Function_1_24C")

    label("loc_358")

    Return()

    # Function_1_24C end

    def Function_2_359(): pass

    label("Function_2_359")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_383")
    OP_94(0xFE, 0xFFFFF510, 0xFFFFFF56, 0x11D0, 0x94C, 0x3E8)
    Sleep(300)
    Jump("Function_2_359")

    label("loc_383")

    Return()

    # Function_2_359 end

    def Function_3_384(): pass

    label("Function_3_384")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3AE")
    OP_94(0xFE, 0x7738, 0x1126, 0x852A, 0x1D38, 0x3E8)
    Sleep(300)
    Jump("Function_3_384")

    label("loc_3AE")

    Return()

    # Function_3_384 end

    def Function_4_3AF(): pass

    label("Function_4_3AF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3FB")
    OP_95(0xFE, 1790, 0, 500, 900, 0x0)
    Sleep(500)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_95(0xFE, 1790, 0, 1500, 900, 0x0)
    Sleep(500)
    OP_93(0xFE, 0xB4, 0x1F4)
    Jump("Function_4_3AF")

    label("loc_3FB")

    Return()

    # Function_4_3AF end

    def Function_5_3FC(): pass

    label("Function_5_3FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_426")
    OP_94(0xFE, 0xF32, 0x2C6, 0x139C, 0x2634, 0x3E8)
    Sleep(300)
    Jump("Function_5_3FC")

    label("loc_426")

    Return()

    # Function_5_3FC end

    def Function_6_427(): pass

    label("Function_6_427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_45B")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x9, 5020, 0, 7310, 90)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_7A6")

    label("loc_45B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4A0")
    SetChrPos(0x9, 1790, 0, 1100, 270)
    SetChrPos(0xA, -180, 0, 1100, 90)
    BeginChrThread(0x9, 0, 0, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49B")
    SetChrFlags(0xA, 0x10)

    label("loc_49B")

    Jump("loc_7A6")

    label("loc_4A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4CA")
    SetChrFlags(0xA, 0x80)
    SetChrPos(0x9, 40670, 0, 9600, 360)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_7A6")

    label("loc_4CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4EE")
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 3670, 0, 9770, 0)
    Jump("loc_7A6")

    label("loc_4EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_506")
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jump("loc_7A6")

    label("loc_506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_523")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_7A6")

    label("loc_523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_57D")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrPos(0x8, 5310, 0, 4019, 90)
    SetChrPos(0xA, 1090, 0, 620, 315)
    SetChrPos(0xC, 280, 0, 1480, 135)
    Jump("loc_7A6")

    label("loc_57D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_5D7")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x8, 4980, 0, 8220, 135)
    SetChrPos(0xA, 5020, 0, 7310, 89)
    SetChrPos(0xC, 2970, 0, 4630, 270)
    SetChrFlags(0xA, 0x10)
    Jump("loc_7A6")

    label("loc_5D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_640")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x8, 760, 0, 340, 0)
    SetChrPos(0xA, 1420, 0, 1650, 225)
    SetChrPos(0xC, -30, 0, 1380, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63B")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xC, 0x10)

    label("loc_63B")

    Jump("loc_7A6")

    label("loc_640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_68F")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0x8, 600, 0, 960, 0)
    SetChrPos(0xA, -5660, -500, 3990, 90)
    BeginChrThread(0x8, 0, 0, 2)
    Jump("loc_7A6")

    label("loc_68F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_6B4")
    SetChrPos(0x9, 40670, 0, 9600, 360)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_7A6")

    label("loc_6B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_6FE")
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    SetChrPos(0x8, 39000, 0, 8200, 360)
    SetChrPos(0x9, 39000, 0, 8950, 180)
    BeginChrThread(0x8, 1, 0, 1)
    Jump("loc_7A6")

    label("loc_6FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_743")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0x9, 3150, 0, 8500, 90)
    SetChrPos(0xA, 4850, 0, 8500, 270)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_7A6")

    label("loc_743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_760")
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0x8, 0x80)
    Jump("loc_7A6")

    label("loc_760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_76E")
    Jump("loc_7A6")

    label("loc_76E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_793")
    SetChrPos(0xA, 4340, 0, 5610, 315)
    BeginChrThread(0xA, 0, 0, 5)
    Jump("loc_7A6")

    label("loc_793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_7A1")
    Jump("loc_7A6")

    label("loc_7A1")

    SetChrFlags(0xA, 0x80)

    label("loc_7A6")

    Return()

    # Function_6_427 end

    def Function_7_7A7(): pass

    label("Function_7_7A7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7C0")
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_7C6")

    label("loc_7C0")

    OP_10(0x0, 0x1)
    OP_10(0x3, 0x0)

    label("loc_7C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E2")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_7F9")

    label("loc_7E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7F9")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_7F9")

    label("loc_7F9")

    Return()

    # Function_7_7A7 end

    def Function_8_7FA(): pass

    label("Function_8_7FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_839")

    #C0001
    ChrTalk(
        0x8,
        "哎呀，下面好吵啊。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        "发生什么事了吗？\x02",
    )

    CloseMessageWindow()
    Jump("loc_D65")

    label("loc_839")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_8CA")

    #C0003
    ChrTalk(
        0x8,
        (
            "纪念庆典最盛大的活动\x01",
            "终于也结束了。\x01",
            "孙子们能开心比什么都重要。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "那么……还剩下一条行程安排，\x01",
            "明天也要按计划把事情完成呀。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D65")

    label("loc_8CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_958")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_904")

    #C0005
    ChrTalk(
        0x8,
        (
            "等洗完衣服，\x01",
            "我也出去走走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_953")

    label("loc_904")


    #C0006
    ChrTalk(
        0x8,
        (
            "今天是一家人\x01",
            "一起大扫除的日子。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "大家分工合作\x01",
            "就能早点完成打扫了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_953")

    Jump("loc_D65")

    label("loc_958")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_A69")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_9EC")

    #C0008
    ChrTalk(
        0x8,
        (
            "我儿子在ＩＢＣ工作，\x01",
            "儿媳在外资企业的分公司工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "虽然我知道他们很忙，\x01",
            "但至少在庆典期间也要回来\x01",
            "陪孙子们玩一玩啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A64")

    label("loc_9EC")


    #C0010
    ChrTalk(
        0x8,
        (
            "难得的纪念庆典，\x01",
            "儿子和儿媳却都说工作很忙不能回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "唉……我倒是\x01",
            "无所谓，\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "不过孙子们\x01",
            "应该会很寂寞吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_A64")

    Jump("loc_D65")

    label("loc_A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_B5A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_AF8")

    #C0013
    ChrTalk(
        0x8,
        (
            "今天我准备带孙子们\x01",
            "在附近逛逛。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "纪念庆典是个悠久的传统庆典，\x01",
            "虽然玩的时候要注意节制，但不好好享受就太可惜了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B55")

    label("loc_AF8")


    #C0015
    ChrTalk(
        0x8,
        (
            "就算是纪念庆典，\x01",
            "也不用那么急急忙忙的。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "窗户要关好……\x01",
            "嗯，应该没忘什么东西吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_B55")

    Jump("loc_D65")

    label("loc_B5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_C2D")
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BD6")
    TurnDirection(0xFE, 0x0, 0)

    #C0017
    ChrTalk(
        0x8,
        (
            "别看我现在上了年纪，\x01",
            "年轻时也是银发飘飘，很受欢迎的。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        "我还很擅长跳舞哦。\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x0)
    Jump("loc_C24")

    label("loc_BD6")


    #C0019
    ChrTalk(
        0x8,
        "像这样，腰放低点，\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "然后将手轻轻搭上，\x01",
            "剩下的只要跟着节奏就行了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_C24")

    OP_4C(0x9, 0xFF)
    Jump("loc_D65")

    label("loc_C2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C89")

    #C0021
    ChrTalk(
        0x8,
        (
            "我今天约了一个\x01",
            "老朋友见面。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "呵呵，要不要互相吹捧下\x01",
            "自己的孙子们呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D65")

    label("loc_C89")


    #C0023
    ChrTalk(
        0x8,
        (
            "菲利克虽然有点调皮，\x01",
            "但其实是个善良的孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "辛迪比较早熟，\x01",
            "但很开朗，也很会做家务。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "最近，亨利的脸上\x01",
            "一直挂着灿烂的笑容。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "……有这么多孙子，\x01",
            "真是幸福啊。\x01",
            "儿子做得最孝顺的事就是给我生了这几个孙子。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_D65")

    TalkEnd(0xFE)
    Return()

    # Function_8_7FA end

    def Function_9_D69(): pass

    label("Function_9_D69")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_DFD")
    Jump("loc_E47")

    label("loc_DFD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E1D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E47")

    label("loc_E1D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E3D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E47")

    label("loc_E3D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E47")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_F42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_EA8")

    #C0027
    ChrTalk(
        0xB,
        (
            "那个……本德先生\x01",
            "出什么事了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F3D")

    label("loc_EA8")


    #C0028
    ChrTalk(
        0xB,
        (
            "住在隔壁的索菲亚夫人\x01",
            "刚才过来问我\x01",
            "有没有见过本德先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xB,
        (
            "本德先生好像是住这附近的\x01",
            "一位证券经理吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xB,
        (
            "我也没见过他……\x01",
            "本德先生怎么了？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_F3D")

    Jump("loc_17AF")

    label("loc_F42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1089")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_FBB")

    #C0031
    ChrTalk(
        0xB,
        (
            "我们这些市民，\x01",
            "已经对议会不抱一丝希望了。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xB,
        (
            "……虽然很令人遗憾，\x01",
            "但还是希望赶快结束算了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1084")

    label("loc_FBB")


    #C0033
    ChrTalk(
        0xB,
        (
            "克洛斯贝尔的议会\x01",
            "在七十多年来一直\x01",
            "都反复做着同样的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xB,
        (
            "有时帝国派掌权，\x01",
            "有时共和国派掌权，\x01",
            "但都是追求自己的利益……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xB,
        (
            "议会从没做出一点成绩。\x01",
            "我们这些市民会对其失望，\x01",
            "也是理所当然的了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1084")

    Jump("loc_17AF")

    label("loc_1089")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_116D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10EA")

    #C0036
    ChrTalk(
        0xB,
        (
            "比起考试成绩，\x01",
            "与朋友一起学习的过程\x01",
            "更加重要。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xB,
        "我是这样想的呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1168")

    label("loc_10EA")


    #C0038
    ChrTalk(
        0xB,
        (
            "亨利在主日学校的考试……\x01",
            "好像又是满分。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xB,
        (
            "一个人只懂得\x01",
            "学习书本知识是不够的。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xB,
        (
            "希望他能多学学\x01",
            "怎样跟朋友相处。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1168")

    Jump("loc_17AF")

    label("loc_116D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_122E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_11C5")

    #C0041
    ChrTalk(
        0xB,
        (
            "我儿子虽然是ＩＢＣ事业部的主任，\x01",
            "但作为一家之主还远远不够。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1229")

    label("loc_11C5")


    #C0042
    ChrTalk(
        0xB,
        (
            "正因为是难得的休息日，\x01",
            "才更不能懒懒散散的。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xB,
        (
            "这种时候就应该\x01",
            "和家人一起\x01",
            "共享天伦之乐啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1229")

    Jump("loc_17AF")

    label("loc_122E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_140A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_12D6")

    #C0044
    ChrTalk(
        0xB,
        (
            "说起名门出身的人，\x01",
            "性格往往各不相同。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xB,
        (
            "但至少我的朋友都是\x01",
            "一些严肃认真的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xB,
        (
            "一定是因为背负着家族之名，\x01",
            "所以必须具备相应的觉悟吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1405")

    label("loc_12D6")


    #C0047
    ChrTalk(
        0xB,
        (
            "我有几个老朋友\x01",
            "都是名门出身的。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xB,
        (
            "克洛斯贝尔现在这些有名望的家族，\x01",
            "以前都是经商起家的……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xB,
        (
            "在悠长的年月中人才辈出，\x01",
            "逐渐被世人所认可，最终成为了名门世家。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xB,
        (
            "我虽然并不是很喜欢\x01",
            "世家传承这种观点。\x01",
            "但大家都是一些严肃认真的人哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xB,
        (
            "一定是因为背负着家族之名，\x01",
            "所以必须具备相应的觉悟吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1405")

    Jump("loc_17AF")

    label("loc_140A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_14CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1471")

    #C0052
    ChrTalk(
        0xB,
        (
            "亨利最近\x01",
            "变得很活泼。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xB,
        (
            "如果是交了朋友的缘故，\x01",
            "那就必须感谢那个朋友啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14C7")

    label("loc_1471")


    #C0054
    ChrTalk(
        0xB,
        (
            "最近亨利\x01",
            "经常去外面玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xB,
        (
            "以前明明都会\x01",
            "一直闷在家里的。\x01",
            "是因为交了朋友吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_14C7")

    Jump("loc_17AF")

    label("loc_14CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1532")

    #C0056
    ChrTalk(
        0xB,
        (
            "今天来\x01",
            "整理整理旧衣服吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xB,
        (
            "免得到了换季时期，\x01",
            "孩子们又会慌慌张张地找不到衣服。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17AF")

    label("loc_1532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1609")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1587")

    #C0058
    ChrTalk(
        0xB,
        (
            "我正在帮亨利\x01",
            "织新睡衣哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xB,
        (
            "手工织的应该\x01",
            "会比较暖和。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1604")

    label("loc_1587")


    #C0060
    ChrTalk(
        0xB,
        (
            "我正在帮亨利\x01",
            "织新睡衣哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xB,
        (
            "虽然只要花点钱\x01",
            "就能买到好品质的衣服，\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xB,
        (
            "但亨利年纪还小，\x01",
            "手工织的应该\x01",
            "会比较暖和。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1604")

    Jump("loc_17AF")

    label("loc_1609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_16E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1662")

    #C0063
    ChrTalk(
        0xB,
        (
            "希望孩子们能多\x01",
            "经历点事情，\x01",
            "这样他们才能懂得如何去分辨善恶。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16DB")

    label("loc_1662")


    #C0064
    ChrTalk(
        0xB,
        (
            "这世上有好人\x01",
            "也有坏人……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xB,
        (
            "社会越来越复杂，\x01",
            "善恶就\x01",
            "越来越难分辨。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xB,
        (
            "所以希望孩子们能\x01",
            "学会如何去分辨善恶。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_16DB")

    Jump("loc_17AF")

    label("loc_16E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1724")

    #C0067
    ChrTalk(
        0xB,
        (
            "男孩子最重要的是要有精神。\x01",
            "稍微调皮点\x01",
            "是最好的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17AF")

    label("loc_1724")


    #C0068
    ChrTalk(
        0xB,
        (
            "男孩子最重要的是要有精神。\x01",
            "我是这样认为的。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xB,
        (
            "虽然我儿子总会\x01",
            "唠唠叨叨地对亨利说教，\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xB,
        (
            "但亨利这个年纪，\x01",
            "稍微调皮点\x01",
            "是最好的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_17AF")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_D69 end

    def Function_10_17B7(): pass

    label("Function_10_17B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_188A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_17FC")

    #C0071
    ChrTalk(
        0x9,
        (
            "可恶，今天根本就\x01",
            "没有轮到我做家务啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1885")

    label("loc_17FC")


    #C0072
    ChrTalk(
        0x9,
        (
            "辛迪那家伙……\x01",
            "把家务活全都推给我了！\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "可恶，\x01",
            "今天的会议结束后，\x01",
            "各处都会举办庆祝宴会。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "这样下去，\x01",
            "我会来不及参加的……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1885")

    Jump("loc_242D")

    label("loc_188A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1996")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_18D9")

    #C0075
    ChrTalk(
        0x9,
        "预算会议怎么不早点结束啊。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        "我可是等了很久的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1991")

    label("loc_18D9")


    #C0077
    ChrTalk(
        0x9,
        (
            "我等下准备去参加\x01",
            "即将举办的\x01",
            "『本年度预算通过·庆祝宴会』。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "我咨询了辛迪的意见，\x01",
            "也让奶奶帮我检查了……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        "这次打扮得可以说非常完美。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        "接下来只要等着会议结束就行了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1991")

    Jump("loc_242D")

    label("loc_1996")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1AF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1A16")

    #C0081
    ChrTalk(
        0x9,
        (
            "预算会议一结束，\x01",
            "各处都会举办盛大的\x01",
            "庆祝宴会。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "这可是接近那些名人的大好机会！\x01",
            "绝对不能错过～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AED")

    label("loc_1A16")


    #C0083
    ChrTalk(
        0x9,
        (
            "好，今天得\x01",
            "用心打扮一番了……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "……预算会议结束后，\x01",
            "许多财政界人士都会\x01",
            "在自己的宅邸中举办庆祝宴会。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x9,
        (
            "届时，那些财政界的大人物，\x01",
            "比如ＩＢＣ的库罗伊斯总裁\x01",
            "也会出席哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "嘿嘿，所以\x01",
            "我也得去参加啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1AED")

    Jump("loc_242D")

    label("loc_1AF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1BEC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1B5F")

    #C0087
    ChrTalk(
        0x9,
        (
            "最近也习惯\x01",
            "混进各种宴会了……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        (
            "但一想到要真正走进政治世界，\x01",
            "就觉得很害怕呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BE7")

    label("loc_1B5F")


    #C0089
    ChrTalk(
        0x9,
        (
            "我之前混进了\x01",
            "共和国派议员主办的宴会。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "他们竟然明目张胆地\x01",
            "筹划要在议会上喝倒彩。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "（发抖）……政治的世界\x01",
            "真是可怕啊……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1BE7")

    Jump("loc_242D")

    label("loc_1BEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1C85")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1C36")

    #C0092
    ChrTalk(
        0x9,
        (
            "不过老爸他\x01",
            "害怕奶奶。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        "嘿嘿，有些好笑啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C80")

    label("loc_1C36")


    #C0094
    ChrTalk(
        0x9,
        "老爸他今天休息哦。\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x9,
        (
            "平时都没怎么回过家，\x01",
            "见到他真是不习惯啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1C80")

    Jump("loc_242D")

    label("loc_1C85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1D2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1CE7")

    #C0096
    ChrTalk(
        0x9,
        (
            "随着议会的临近，最近\x01",
            "有很多宴会哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x9,
        "嘿嘿，今天要参加哪个宴会呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D2A")

    label("loc_1CE7")


    #C0098
    ChrTalk(
        0x9,
        "我用零花钱买了一件白色燕尾服。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        "嘿嘿，今晚就穿那件吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1D2A")

    Jump("loc_242D")

    label("loc_1D2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1D99")
    OP_4B(0x8, 0xFF)

    #C0100
    ChrTalk(
        0x9,
        (
            "没想到奶奶\x01",
            "竟然会跳舞……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        (
            "虽然有点意外，\x01",
            "但真不愧是奶奶，果然可靠啊……！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    Jump("loc_242D")

    label("loc_1D99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1DF7")
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1DEB")

    #C0102
    ChrTalk(
        0x9,
        "所以我不是正在拜托你嘛。\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "我一定得\x01",
            "学好跳舞！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DEE")

    label("loc_1DEB")

    Call(0, 11)

    label("loc_1DEE")

    OP_4C(0xA, 0xFF)
    Jump("loc_242D")

    label("loc_1DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1EE7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1E3F")

    #C0104
    ChrTalk(
        0x9,
        (
            "可不能让\x01",
            "舞伴丢脸啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        "必须得好好练习。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EE2")

    label("loc_1E3F")


    #C0106
    ChrTalk(
        0x9,
        (
            "唉，我明明长得不错啊，\x01",
            "为什么在宴会上\x01",
            "都没什么人约我跳舞呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        "仔细想想，终于知道原因了。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x9,
        "肯定是因为我的舞跳得不好。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        "……所以必须好好练习啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1EE2")

    Jump("loc_242D")

    label("loc_1EE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1FB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1F3B")

    #C0110
    ChrTalk(
        0x9,
        "嗯，要洗的衣服在……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "要是我们家也请个\x01",
            "佣人就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FB2")

    label("loc_1F3B")


    #C0112
    ChrTalk(
        0x9,
        "……我们家是轮流做家务活的。\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x9,
        (
            "真是，等下还和帝国的朋友约好\x01",
            "要一起去玩的……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "算了……\x01",
            "也不能违抗奶奶～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1FB2")

    Jump("loc_242D")

    label("loc_1FB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_20D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_201C")

    #C0115
    ChrTalk(
        0x9,
        (
            "步入社交界\x01",
            "真不轻松啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        (
            "不好好丰富知识的话，\x01",
            "就跟不上大家的话题了～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D4")

    label("loc_201C")


    #C0117
    ChrTalk(
        0x9,
        (
            "我去百货店的杂货柜台\x01",
            "买了政治读物和\x01",
            "经济分析的书哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x9,
        (
            "要想出入社交界，\x01",
            "就一定要了解这方面的知识～\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        "等下要再去买一本宴会礼仪的书！\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x9,
        "呼，下一个宴会我一定会表现完美。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_20D4")

    Jump("loc_242D")

    label("loc_20D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_21ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_210C")

    #C0121
    ChrTalk(
        0x9,
        "社交界意外地很复杂啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_21E8")

    label("loc_210C")


    #C0122
    ChrTalk(
        0x9,
        (
            "在之前的宴会上，\x01",
            "我认识了一位有名的经理夫人哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        (
            "嘿嘿，能跟名人说话，\x01",
            "真是开心啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x9,
        (
            "……话说，那位夫人\x01",
            "也是一位很有名的\x01",
            "经济理论研究学者哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0125
    ChrTalk(
        0x9,
        "她说的话很深奥，我都不是很懂。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_21E8")

    Jump("loc_242D")

    label("loc_21ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_22FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2264")

    #C0126
    ChrTalk(
        0x9,
        (
            "奶奶借给我一套\x01",
            "很气派的西装哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x9,
        (
            "……应该是老爸年轻时穿的吧。\x01",
            "嘿嘿，我偷偷把它穿出去。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22F8")

    label("loc_2264")


    #C0128
    ChrTalk(
        0x9,
        (
            "我跟奶奶说要去一个宴会，\x01",
            "她马上就借给我一套\x01",
            "很气派的西装哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x9,
        (
            "嘿嘿，太好了！\x01",
            "这样一来，我就能在社交界崭露头角了。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x9,
        "真是感谢奶奶啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_22F8")

    Jump("loc_242D")

    label("loc_22FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2385")

    #C0131
    ChrTalk(
        0x9,
        (
            "克洛斯贝尔的社交界经常会出现\x01",
            "世界性名人以及财经界的重量级人物，\x01",
            "这点是众所周知的。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x9,
        "很好很好，我也要去参加看看。\x02",
    )

    CloseMessageWindow()
    Jump("loc_242D")

    label("loc_2385")


    #C0133
    ChrTalk(
        0x9,
        (
            "绅士淑女齐聚的晚宴……\x01",
            "那便是社交界的精华所在……！\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x9,
        (
            "……其实，今天晚上\x01",
            "在某个资产家的宅邸里有一场宴会，\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x9,
        (
            "嘿嘿，我也去露个脸吧。\x01",
            "我对社交界很感兴趣啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_242D")

    TalkEnd(0xFE)
    Return()

    # Function_10_17B7 end

    def Function_11_2431(): pass

    label("Function_11_2431")


    #C0136
    ChrTalk(
        0x9,
        "喂，妹妹啊，当我的练习舞伴吧。\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        (
            "咦，为什么啊～？\x01",
            "你自己一个人去练不就行了！\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x9,
        (
            "一个人练不了啦，\x01",
            "笨蛋，拜托了。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xA,
        (
            "哥哥你才是笨蛋吧。\x01",
            "笨蛋，笨蛋！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_11_2431 end

    def Function_12_24D4(): pass

    label("Function_12_24D4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_260B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_253B")

    #C0140
    ChrTalk(
        0xA,
        (
            "哥哥让我\x01",
            "对他的打扮\x01",
            "提点意见。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xA,
        (
            "我是无所谓啦～\x01",
            "不过哥哥也真是闲呀～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2606")

    label("loc_253B")

    OP_4B(0x9, 0xFF)
    TurnDirection(0x9, 0xA, 500)

    #C0142
    ChrTalk(
        0xA,
        "……刚才那件可能比较好。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        "哥哥，仔细一看，你还挺帅的嘛。\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x9,
        (
            "『仔细一看』是多余的啦。\x01",
            "笨蛋妹妹，快给我更正。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xA,
        (
            "因为你平时看起来\x01",
            "都很普通啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x9,
        "辛迪，给我认真点啦！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0x9, 0xFF)

    label("loc_2606")

    Jump("loc_2ECC")

    label("loc_260B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_274D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_267A")

    #C0147
    ChrTalk(
        0xA,
        (
            "有个那么好的丈夫，\x01",
            "索菲亚夫人真是幸福啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xA,
        (
            "我也想早点\x01",
            "有个好丈夫啊～开玩笑啦¤\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2748")

    label("loc_267A")


    #C0149
    ChrTalk(
        0xA,
        (
            "有亨利来帮我的忙，就能\x01",
            "早点结束啦，真是得救了呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xA,
        (
            "话说回来……隔壁的哈罗德先生\x01",
            "最近又重新开始工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xA,
        (
            "我之前有遇到他……\x01",
            "看起来好像\x01",
            "比以前更温柔了。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xA,
        (
            "能让人感受到\x01",
            "具有无限包容力的爱。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2748")

    Jump("loc_2ECC")

    label("loc_274D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_27AD")

    #C0153
    ChrTalk(
        0xA,
        (
            "呀哈～我刚买到了\x01",
            "咪西的\x01",
            "挂饰哦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xA,
        (
            "这可是\x01",
            "很珍贵的周边哦。\x01",
            "真的超幸运！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ECC")

    label("loc_27AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2811")

    #C0155
    ChrTalk(
        0xA,
        (
            "（溅水声）……\x01",
            "盘子和杯子都要洗得闪闪发亮～¤\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xA,
        (
            "得快点洗完，\x01",
            "然后去看游行～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ECC")

    label("loc_2811")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2863")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_284B")

    #C0157
    ChrTalk(
        0xA,
        (
            "嘿嘿，在百货店\x01",
            "要买点什么呢！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_285E")

    label("loc_284B")

    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)
    Call(0, 13)
    OP_4C(0x8, 0xFF)
    OP_4C(0xC, 0xFF)

    label("loc_285E")

    Jump("loc_2ECC")

    label("loc_2863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_28AA")

    #C0158
    ChrTalk(
        0xA,
        "奶奶，快走啦！\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xA,
        (
            "真是的，亨利你也\x01",
            "快点准备啦～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ECC")

    label("loc_28AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_29E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_290E")

    #C0160
    ChrTalk(
        0xA,
        (
            "我总觉得索菲亚夫人\x01",
            "好像有什么不愿提起的过去……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xA,
        "虽然没直接问过她。\x02",
    )

    CloseMessageWindow()
    Jump("loc_29E4")

    label("loc_290E")


    #C0162
    ChrTalk(
        0xA,
        (
            "索菲亚夫人每星期\x01",
            "都会坚持参加教堂的弥撒。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xA,
        (
            "真是很厉害啊。\x01",
            "又擅长烹饪，\x01",
            "还能帮助丈夫工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xA,
        (
            "不过……我总觉得索菲亚夫人\x01",
            "好像有什么不愿提起的过去……\x01",
            "或者是有什么想不开的。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xA,
        "虽然没直接问过她啦……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_29E4")

    Jump("loc_2ECC")

    label("loc_29E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2AE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2A4C")

    #C0166
    ChrTalk(
        0xA,
        (
            "爸爸总是\x01",
            "早出晚归哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xA,
        (
            "希望我将来的丈夫\x01",
            "能有个比较轻松自由的职业。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ADC")

    label("loc_2A4C")


    #C0168
    ChrTalk(
        0xA,
        "爸爸在ＩＢＣ的事业部上班。\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xA,
        (
            "是事业部的主任，\x01",
            "听起来好像大人物哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xA,
        (
            "不过他总是\x01",
            "早出晚归……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xA,
        (
            "偶尔也要请个假，\x01",
            "好好休息下啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2ADC")

    Jump("loc_2ECC")

    label("loc_2AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2B49")
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2B3D")

    #C0172
    ChrTalk(
        0xA,
        "哥哥你这个社交界笨蛋！\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xA,
        (
            "我很忙啊。\x01",
            "你自己一个人去练吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B40")

    label("loc_2B3D")

    Call(0, 11)

    label("loc_2B40")

    OP_4C(0x9, 0xFF)
    Jump("loc_2ECC")

    label("loc_2B49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2C48")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2BBE")

    #C0174
    ChrTalk(
        0xA,
        (
            "我接下来要去索菲亚夫人家的\x01",
            "烹饪教室上课哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xA,
        (
            "今天要做的是\x01",
            "内容丰盛的海鲜奶汁烤菜哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C43")

    label("loc_2BBE")


    #C0176
    ChrTalk(
        0xA,
        (
            "我接下来要去索菲亚夫人家的\x01",
            "烹饪教室上课哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xA,
        (
            "今天要做的是\x01",
            "内容丰盛的海鲜奶汁烤菜哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xA,
        "嗯，要带的东西应该都备齐了吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2C43")

    Jump("loc_2ECC")

    label("loc_2C48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2D53")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2CBD")

    #C0179
    ChrTalk(
        0xA,
        (
            "明天我要去索菲亚夫人家的\x01",
            "烹饪教室上课哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xA,
        (
            "哼，哥哥要是能少玩一会，\x01",
            "来帮帮我就好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D4E")

    label("loc_2CBD")


    #C0181
    ChrTalk(
        0xA,
        (
            "明天我要去索菲亚夫人家的\x01",
            "烹饪教室上课哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xA,
        (
            "因为索菲亚夫人\x01",
            "很擅长烹饪，\x01",
            "所以我经常会去跟她学习。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xA,
        (
            "要赶快打扫完，\x01",
            "然后去做准备呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2D4E")

    Jump("loc_2ECC")

    label("loc_2D53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2E45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2DA2")

    #C0184
    ChrTalk(
        0xA,
        "嗯，调味这样就行了吧。\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xA,
        "我算是很擅长家务的哦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2E40")

    label("loc_2DA2")


    #C0186
    ChrTalk(
        0xA,
        "嗯，调味这样就行了吧。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xA,
        "我算是很擅长家务的哦。\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xA,
        (
            "这都是奶奶以前\x01",
            "教我的。\x01",
            "烹饪更是小菜一碟哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xA,
        (
            "呵呵，你们不觉得我将来\x01",
            "能成为一个好妻子吗？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2E40")

    Jump("loc_2ECC")

    label("loc_2E45")


    #C0190
    ChrTalk(
        0xA,
        (
            "我们家爸爸和妈妈都很忙，\x01",
            "所以奶奶是家里的主心骨哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xA,
        (
            "哥哥、亨利还有我，\x01",
            "都是奶奶一手带大的。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xA,
        (
            "所以我们都很\x01",
            "喜欢粘着奶奶～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ECC")

    TalkEnd(0xFE)
    Return()

    # Function_12_24D4 end

    def Function_13_2ED0(): pass

    label("Function_13_2ED0")


    #C0193
    ChrTalk(
        0xA,
        (
            "我今天\x01",
            "想去百货店！\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x8,
        (
            "亨利你\x01",
            "有想去的地方吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xC,
        (
            "我想去逛逛\x01",
            "港湾区的露天市场！\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x8,
        (
            "我知道了，\x01",
            "那我们今天\x01",
            "就去这些地方吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x8,
        (
            "走累了的话，\x01",
            "要告诉奶奶哦，\x01",
            "知道了吧？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_13_2ED0 end

    def Function_14_2F8F(): pass

    label("Function_14_2F8F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3017")

    #C0198
    ChrTalk(
        0xFE,
        (
            "今天我要帮忙\x01",
            "做家务……\x01",
            "应该会迟点再去玩。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        "不知道隆有没有乖乖的呢～\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "只要一不管他，\x01",
            "他就会闯点什么祸……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32CD")

    label("loc_3017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_30F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3076")

    #C0201
    ChrTalk(
        0xC,
        (
            "隆想追在\x01",
            "游行队伍后面跑。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xC,
        (
            "真不愧是隆啊……\x01",
            "好像精神过头了点。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30F0")

    label("loc_3076")


    #C0203
    ChrTalk(
        0xC,
        (
            "今天真的\x01",
            "好累啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xC,
        (
            "话说起来，\x01",
            "隆好像也去\x01",
            "看游行了。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xC,
        (
            "……听说是和他爸爸边\x01",
            "斗嘴边看的。\x01",
            "应、应该没事吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_30F0")

    Jump("loc_32CD")

    label("loc_30F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3159")

    #C0206
    ChrTalk(
        0xC,
        "嗯，要洗的衣服在……\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xC,
        (
            "各位也要去\x01",
            "看游行吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xC,
        (
            "今天人好像很多，\x01",
            "要小心啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32CD")

    label("loc_3159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_31CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_31B2")

    #C0209
    ChrTalk(
        0xC,
        (
            "奶奶今天也要\x01",
            "带我们去玩！\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xC,
        (
            "嘿嘿嘿，果然\x01",
            "还是奶奶最好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31C5")

    label("loc_31B2")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    Call(0, 13)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)

    label("loc_31C5")

    Jump("loc_32CD")

    label("loc_31CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3229")

    #C0211
    ChrTalk(
        0xC,
        (
            "奶奶虽然平时有点严厉，\x01",
            "但一到庆典就会给我们零花钱哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xC,
        "呵呵，好期待啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_32CD")

    label("loc_3229")

    OP_63(0xC, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0213
    ChrTalk(
        0xC,
        "啊，是各位啊。\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xC,
        (
            "嘿嘿嘿，我们正要\x01",
            "一家人一起出去。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xC,
        (
            "奶奶虽然平时有点严厉，\x01",
            "但一到庆典就会给我们零花钱哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xC,
        "呵呵，好期待啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_32CD")

    TalkEnd(0xFE)
    Return()

    # Function_14_2F8F end

    def Function_15_32D1(): pass

    label("Function_15_32D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3339")

    #C0217
    ChrTalk(
        0xD,
        (
            "从小时候起，\x01",
            "老妈就开始教我做家务了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xD,
        "她一直都对教育孩子的事情非常上心……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3395")

    label("loc_3339")


    #C0219
    ChrTalk(
        0xD,
        (
            "老妈让我\x01",
            "把家里打扫一下……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0220
    ChrTalk(
        0xD,
        (
            "唔唔，难得\x01",
            "今天休息……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_3395")

    TalkEnd(0xFE)
    Return()

    # Function_15_32D1 end

    SaveToFile()

Try(main)
