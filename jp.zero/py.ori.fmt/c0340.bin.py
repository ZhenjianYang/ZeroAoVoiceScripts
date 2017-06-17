from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "イズリ夫人",             # 1
        "フェリック",             # 2
        "シンディ",               # 3
        "イズリ夫人",             # 4
        "アンリ",                 # 5
        "ユンクス",               # 6
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
        "Function_9_E29",          # 09, 9
        "Function_10_1B0F",        # 0A, 10
        "Function_11_29FD",        # 0B, 11
        "Function_12_2ABC",        # 0C, 12
        "Function_13_36D0",        # 0D, 13
        "Function_14_37CD",        # 0E, 14
        "Function_15_3C19",        # 0F, 15
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_845")

    #C0001
    ChrTalk(
        0x8,
        "あら、下が騒がしいですね。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        "何かあったのかしら？\x02",
    )

    CloseMessageWindow()
    Jump("loc_E25")

    label("loc_845")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_8E8")

    #C0003
    ChrTalk(
        0x8,
        (
            "記念祭の一大行事も\x01",
            "ようやく終わりましたね。\x01",
            "孫達も楽しめたようで何よりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "さて……残る行事はあと一つ。\x01",
            "明日はイベントをやらなくてはね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E25")

    label("loc_8E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_98E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_932")

    #C0005
    ChrTalk(
        0x8,
        (
            "洗い物を済ませて、\x01",
            "そろそろ出かけましょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_989")

    label("loc_932")


    #C0006
    ChrTalk(
        0x8,
        (
            "今日は家族みんなで\x01",
            "家事をする日です。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "手分けした方が\x01",
            "早く済みますからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_989")

    Jump("loc_E25")

    label("loc_98E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_AD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A2A")

    #C0008
    ChrTalk(
        0x8,
        (
            "息子はＩＢＣで、\x01",
            "嫁は外国の支社で働いているのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "忙しいのは判るけれど、\x01",
            "孫たちと祭りを過ごすことも\x01",
            "できないのかしらね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD4")

    label("loc_A2A")


    #C0010
    ChrTalk(
        0x8,
        (
            "記念祭であるというのに\x01",
            "息子も嫁も仕事が忙しいといいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "ふう……あたしは\x01",
            "一向に構いませんけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "孫たちは、本当は寂しく\x01",
            "思っているんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_AD4")

    Jump("loc_E25")

    label("loc_AD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_BD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_B68")

    #C0013
    ChrTalk(
        0x8,
        (
            "今日は孫たちをつれて\x01",
            "辺りを一回りしてきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "記念祭は由緒正しいお祭りですから\x01",
            "節度を守って楽しまなくてはね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCF")

    label("loc_B68")


    #C0015
    ChrTalk(
        0x8,
        (
            "記念祭だからといって\x01",
            "そう慌てるものではありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "戸締りはきちんと。\x01",
            "忘れ物はないわね？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_BCF")

    Jump("loc_E25")

    label("loc_BD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_CC9")
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C5A")
    TurnDirection(0xFE, 0x0, 0)

    #C0017
    ChrTalk(
        0x8,
        (
            "あたしはこう見えても\x01",
            "昔は銀髪の令嬢で通っていたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        "ダンスなら大得意ですからね。\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x0, 0x0)
    Jump("loc_CC0")

    label("loc_C5A")


    #C0019
    ChrTalk(
        0x8,
        "そう、もっと腰を落として。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "手は軽く添えるだけでいいのよ。\x01",
            "後はリズムで引き込んでいくの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_CC0")

    OP_4C(0x9, 0xFF)
    Jump("loc_E25")

    label("loc_CC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_D35")

    #C0021
    ChrTalk(
        0x8,
        (
            "今日は古い\x01",
            "友人と会う約束があるのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "さて、お互いの\x01",
            "孫自慢でもしてきましょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E25")

    label("loc_D35")


    #C0023
    ChrTalk(
        0x8,
        (
            "フェリックは少し軽いけれど\x01",
            "心優しくとても良い子です。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "シンディはおませだけれど\x01",
            "明るくて家事が大得意。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "アンリは最近\x01",
            "元気な笑顔を見せてくれますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "……大勢の孫たちに\x01",
            "囲まれてあたしも幸せです。\x01",
            "息子の一番の親孝行だわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_E25")

    TalkEnd(0xFE)
    Return()

    # Function_8_7FA end

    def Function_9_E29(): pass

    label("Function_9_E29")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EBD")
    Jump("loc_F07")

    label("loc_EBD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EDD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F07")

    label("loc_EDD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EFD")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F07")

    label("loc_EFD")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F07")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1056")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F70")

    #C0027
    ChrTalk(
        0xB,
        (
            "はて、ボンドさんが\x01",
            "どうかしたのかしら？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1051")

    label("loc_F70")


    #C0028
    ChrTalk(
        0xB,
        (
            "先ほど、お隣のソフィアさんが\x01",
            "ボンドさんを見かけなかったかと\x01",
            "訪ねてきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xB,
        (
            "ボンドさんはたしかご近所で\x01",
            "証券マンをしてらっしゃる方でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xB,
        (
            "はて、あたしは見ていませんが……\x01",
            "ボンドさんがどうかしたのかしら？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1051")

    Jump("loc_1B07")

    label("loc_1056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_11CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10E7")

    #C0031
    ChrTalk(
        0xB,
        (
            "あたしたち市民は、もう議会に\x01",
            "何も期待していないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xB,
        (
            "ただ終わってくれればよいのです。\x01",
            "……残念な事ですけれどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11C6")

    label("loc_10E7")


    #C0033
    ChrTalk(
        0xB,
        (
            "クロスベルの議会は\x01",
            "もう７０年も\x01",
            "同じ事を繰り返してきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xB,
        (
            "ある時は帝国派、\x01",
            "ある時は共和国派が上に立ち\x01",
            "自分達の利権を主張する……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xB,
        (
            "まったく不毛な事です。\x01",
            "あたしたち市民が興味を失うのも\x01",
            "当然の事でしょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_11C6")

    Jump("loc_1B07")

    label("loc_11CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_12F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_123E")

    #C0036
    ChrTalk(
        0xB,
        (
            "テストの成績よりも\x01",
            "友達と机を並べ\x01",
            "学ぶことが大切でしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xB,
        "あたしはそう思います。\x02",
    )

    CloseMessageWindow()
    Jump("loc_12F2")

    label("loc_123E")


    #C0038
    ChrTalk(
        0xB,
        (
            "アンリの日曜学校の筆記テスト……\x01",
            "また満点だったようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xB,
        (
            "けれども、勉強だけが\x01",
            "人を培うのではありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xB,
        (
            "友達と机を並べる事で\x01",
            "もっと多くを学んで欲しいですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_12F2")

    Jump("loc_1B07")

    label("loc_12F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_13E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_135B")

    #C0041
    ChrTalk(
        0xB,
        (
            "ＩＢＣ事業部の主任なんて言っても\x01",
            "家族を支える者としてはまだまだですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13DF")

    label("loc_135B")


    #C0042
    ChrTalk(
        0xB,
        (
            "たまの休日だからこそ、\x01",
            "だらだらと過ごしてはいけませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xB,
        (
            "こういう時は何かしら\x01",
            "家族サービスを\x01",
            "するものじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_13DF")

    Jump("loc_1B07")

    label("loc_13E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1634")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_14B8")

    #C0044
    ChrTalk(
        0xB,
        (
            "名家の出身と言っても\x01",
            "色んな人間がいますけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xB,
        (
            "少なくともあたしの友人は\x01",
            "みなとても凛とした方ばかりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xB,
        (
            "きっと家の名を背負って生きるのも\x01",
            "見合った覚悟が必要なのでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_162F")

    label("loc_14B8")


    #C0047
    ChrTalk(
        0xB,
        (
            "あたしの古い知り合いの何人かは\x01",
            "名家と呼ばれる家柄の出身です。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xB,
        (
            "クロスベルの名家とされる家々は\x01",
            "いずれも元は交易商の家系……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xB,
        (
            "長い年月の中で優れた人物を輩出し\x01",
            "人々に認められてきた家柄なのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xB,
        (
            "あたしは家柄どうこうという\x01",
            "考えは好きじゃありませんけど、\x01",
            "みなとても凛とした方ばかりよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xB,
        (
            "きっと家の名を背負って生きるのも\x01",
            "見合った覚悟が必要なのでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_162F")

    Jump("loc_1B07")

    label("loc_1634")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1732")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_16AD")

    #C0052
    ChrTalk(
        0xB,
        (
            "アンリは近頃\x01",
            "随分と活発になりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xB,
        (
            "友達が出来たのなら、\x01",
            "その友達に感謝しなくてはね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_172D")

    label("loc_16AD")


    #C0054
    ChrTalk(
        0xB,
        (
            "近頃アンリは\x01",
            "外を遊びまわっているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xB,
        (
            "以前はあんなに\x01",
            "引っ込み思案だったのに。\x01",
            "いい友達でも出来たのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_172D")

    Jump("loc_1B07")

    label("loc_1732")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_17AA")

    #C0056
    ChrTalk(
        0xB,
        (
            "さて、今日は古着の\x01",
            "整理でもしておこうかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xB,
        (
            "季節の変わり目に\x01",
            "子供達が慌てなくて済むようにね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B07")

    label("loc_17AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_18D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_181F")

    #C0058
    ChrTalk(
        0xB,
        (
            "アンリの寝巻きを\x01",
            "編んでいる所なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xB,
        (
            "手編みの方が温かみが\x01",
            "あっていいでしょうから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18D4")

    label("loc_181F")


    #C0060
    ChrTalk(
        0xB,
        (
            "アンリの寝巻きを\x01",
            "編んでいる所なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xB,
        (
            "そりゃあミラさえ出せば\x01",
            "上等な服が買えるでしょうけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xB,
        (
            "アンリはまだ幼いですからね。\x01",
            "手編みの方が温かみがあって\x01",
            "いいでしょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_18D4")

    Jump("loc_1B07")

    label("loc_18D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_19FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_193C")

    #C0063
    ChrTalk(
        0xB,
        (
            "子供たちには沢山経験を積んで\x01",
            "善悪が判るように\x01",
            "育ってほしいものですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19F5")

    label("loc_193C")


    #C0064
    ChrTalk(
        0xB,
        (
            "世の中には良い事と\x01",
            "悪い事があるけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xB,
        (
            "社会が複雑になるにつれて\x01",
            "それが見えにくく\x01",
            "なっているように思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xB,
        (
            "子供たちにはきちんと判るように\x01",
            "育ってほしいものですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_19F5")

    Jump("loc_1B07")

    label("loc_19FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1A4C")

    #C0067
    ChrTalk(
        0xB,
        (
            "男の子は元気が一番。\x01",
            "多少無茶をするくらいが\x01",
            "丁度いいのですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B07")

    label("loc_1A4C")


    #C0068
    ChrTalk(
        0xB,
        (
            "男の子は元気が一番。\x01",
            "あたしはそう思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xB,
        (
            "息子はアンリの一件で\x01",
            "ガミガミと言っていましたけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xB,
        (
            "アンリの年頃なら、\x01",
            "多少無茶をするくらいが\x01",
            "丁度いいんじゃないかしらね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1B07")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_E29 end

    def Function_10_1B0F(): pass

    label("Function_10_1B0F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1C14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1B54")

    #C0071
    ChrTalk(
        0x9,
        (
            "くそう、今日は\x01",
            "俺の当番じゃねえぞっ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C0F")

    label("loc_1B54")


    #C0072
    ChrTalk(
        0x9,
        (
            "シンディのやつ……\x01",
            "俺に家事を押し付けやがったんだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "くそう、今日は議会が終わって\x01",
            "あっちこっちで祝賀パーティが\x01",
            "開かれるってのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "このままじゃ\x01",
            "時間に間に合わねえよ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1C0F")

    Jump("loc_29F9")

    label("loc_1C14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1D58")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1C6F")

    #C0075
    ChrTalk(
        0x9,
        "早く議会、終わんねえかな～。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        "俺もいい加減待ちぼうけだぜ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D53")

    label("loc_1C6F")


    #C0077
    ChrTalk(
        0x9,
        (
            "そろそろ開かれるはずの\x01",
            "『今年度予算成立・祝賀パーティ』に\x01",
            "出席するつもりなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "シンディの意見を聞いてから\x01",
            "婆ちゃんにチェックしてもらって……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x9,
        "今回のおめかしは完璧だぜ。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        "後は議会が終わるのを待つだけだな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1D53")

    Jump("loc_29F9")

    label("loc_1D58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1F0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1DF4")

    #C0081
    ChrTalk(
        0x9,
        (
            "予算議会が終わると\x01",
            "大きなパーティが\x01",
            "あちこちで開かれるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "超有名人とお近づきになるチャンス！\x01",
            "これは見逃せねえよなぁ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F05")

    label("loc_1DF4")


    #C0083
    ChrTalk(
        0x9,
        (
            "よし、今日も念のため\x01",
            "めかしこんでおくか……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x9,
        (
            "……予算議会が終わったって日には\x01",
            "あちこちの財界人のお宅で\x01",
            "祝賀パーティが開かれるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x9,
        (
            "財界切っての有力者、\x01",
            "例えばＩＢＣのクロイス総裁なんかも\x01",
            "出席したりするんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "へっへー、俺も\x01",
            "参加を狙ってるんだよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1F05")

    Jump("loc_29F9")

    label("loc_1F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_204E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1F95")

    #C0087
    ChrTalk(
        0x9,
        (
            "最近はパーティに潜り込むのも\x01",
            "慣れてきたんだけどなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        (
            "政治の世界まで首を突っ込むと\x01",
            "後が怖い気がするぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2049")

    label("loc_1F95")


    #C0089
    ChrTalk(
        0x9,
        (
            "共和国派の議員主催の\x01",
            "パーティに潜り込んで来たんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "議会でヤジを飛ばす段取りとか\x01",
            "大っぴらに話してたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "ぶるぶる……政治の世界ってのは\x01",
            "結構怖いところだよなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2049")

    Jump("loc_29F9")

    label("loc_204E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_211D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_20BA")

    #C0092
    ChrTalk(
        0x9,
        (
            "でもオヤジも婆ちゃんには\x01",
            "頭が上がらないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        "へへっ、ちょっと笑えるよな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2118")

    label("loc_20BA")


    #C0094
    ChrTalk(
        0x9,
        "オヤジ、今日は仕事休みなんだよな。\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x9,
        (
            "普段あんまり顔を\x01",
            "合わせないから居心地悪いぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2118")

    Jump("loc_29F9")

    label("loc_211D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_21E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_218B")

    #C0096
    ChrTalk(
        0x9,
        (
            "議会も近いし、最近は\x01",
            "パーティが多いんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x9,
        "へへ、今日はどこに潜り込むかな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_21DC")

    label("loc_218B")


    #C0098
    ChrTalk(
        0x9,
        "小遣いで白いタキシード買ったんだ。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        "へへ、今夜はこれを着ていこっと。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_21DC")

    Jump("loc_29F9")

    label("loc_21E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2257")
    OP_4B(0x8, 0xFF)

    #C0100
    ChrTalk(
        0x9,
        (
            "まさか婆ちゃんが\x01",
            "ダンスを踊れるとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        (
            "意外だけど頼りになるぜ。\x01",
            "さすが婆ちゃん……！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    Jump("loc_29F9")

    label("loc_2257")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_22CB")
    OP_4B(0xA, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_22BF")

    #C0102
    ChrTalk(
        0x9,
        "だから頼んでるんじゃんか。\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "俺にはどうしても\x01",
            "ダンスが必要なんだよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22C2")

    label("loc_22BF")

    Call(0, 11)

    label("loc_22C2")

    OP_4C(0xA, 0xFF)
    Jump("loc_29F9")

    label("loc_22CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_23E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2337")

    #C0104
    ChrTalk(
        0x9,
        (
            "相手のレディに\x01",
            "恥をかかせるわけにも行くまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        "ダンスの練習しとかなくちゃ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_23E2")

    label("loc_2337")


    #C0106
    ChrTalk(
        0x9,
        (
            "ふっ、俺って顔はいいのに\x01",
            "なぜかパーティじゃ\x01",
            "あまり誘われないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        "よくよく考えて、原因が判ったぜ。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x9,
        "俺、ダンスが下手なんだよね。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        "……練習しよっと。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_23E2")

    Jump("loc_29F9")

    label("loc_23E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_24E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2445")

    #C0110
    ChrTalk(
        0x9,
        "えーと洗濯物はっと……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "うちもメイドとか\x01",
            "雇えばいいのになー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_24DE")

    label("loc_2445")


    #C0112
    ChrTalk(
        0x9,
        "……うちの家事は当番制なんだ。\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x9,
        (
            "ちぇっ、これから帝国人の\x01",
            "友達と遊びに行く予定だったのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "まあいっか……\x01",
            "婆ちゃんには逆らえないしな～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_24DE")

    Jump("loc_29F9")

    label("loc_24E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_263F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2560")

    #C0115
    ChrTalk(
        0x9,
        (
            "社交界に参加するのも\x01",
            "楽じゃないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        (
            "少しは勉強していかないと\x01",
            "話についてけないんだよな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_263A")

    label("loc_2560")


    #C0117
    ChrTalk(
        0x9,
        (
            "百貨店の雑貨コーナーで\x01",
            "政治読本と経済分析の本を\x01",
            "買ってきたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x9,
        (
            "社交界に出入りしたきゃ、\x01",
            "この手の勉強は欠かせないんだよな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        "あとはパーティマナーのハウツー本！\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x9,
        "フッ、次のパーティはバッチリだぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_263A")

    Jump("loc_29F9")

    label("loc_263F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2787")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_267E")

    #C0121
    ChrTalk(
        0x9,
        "社交界ってのも案外難しいんだよな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2782")

    label("loc_267E")


    #C0122
    ChrTalk(
        0x9,
        (
            "この前のパーティで\x01",
            "有名な社長夫人とお近づきになったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        (
            "へへ、有名人と\x01",
            "会話ができるだけでも嬉しいよな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x9,
        (
            "……でも夫人って、\x01",
            "経済理論の研究家としても\x01",
            "知られている人なんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0125
    ChrTalk(
        0x9,
        "話が難しくって、よく判んなかったぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_2782")

    Jump("loc_29F9")

    label("loc_2787")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_28B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2812")

    #C0126
    ChrTalk(
        0x9,
        (
            "婆ちゃんが立派なスーツを\x01",
            "貸してくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x9,
        (
            "……多分親父の若い頃のだな。\x01",
            "へへ、こっそり使ってやろうっと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28B0")

    label("loc_2812")


    #C0128
    ChrTalk(
        0x9,
        (
            "パーティに行くって言ったら\x01",
            "婆ちゃんが立派なスーツを\x01",
            "貸してくれたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x9,
        (
            "へへ、やったね！\x01",
            "これで俺も社交界デビューだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x9,
        "婆ちゃんに感謝感謝っと。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_28B0")

    Jump("loc_29F9")

    label("loc_28B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2945")

    #C0131
    ChrTalk(
        0x9,
        (
            "クロスベルの社交界っていやあ\x01",
            "世界的有名人や財界の著名人が\x01",
            "顔を出すことで有名なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x9,
        "うっしっし、俺も参加してみるかな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_29F9")

    label("loc_2945")


    #C0133
    ChrTalk(
        0x9,
        (
            "紳士淑女が集う晩餐会……\x01",
            "それは社交界の華……！\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x9,
        (
            "……実はさ、今夜とある\x01",
            "資産家のお宅でパーティがあるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x9,
        (
            "へへ、俺も顔を出してみるかな。\x01",
            "社交界って興味あるしな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_29F9")

    TalkEnd(0xFE)
    Return()

    # Function_10_1B0F end

    def Function_11_29FD(): pass

    label("Function_11_29FD")


    #C0136
    ChrTalk(
        0x9,
        "おい妹よ、ダンスの練習相手をしろ。\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xA,
        (
            "えー、なんで～？\x01",
            "そんなの１人でやんなよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x9,
        (
            "１人じゃ出来ないから\x01",
            "頼んでんだよ、バーカ。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xA,
        (
            "バカはお兄ちゃんの方でしょ、\x01",
            "バーカ、バーカ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Return()

    # Function_11_29FD end

    def Function_12_2ABC(): pass

    label("Function_12_2ABC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2C1D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2B3D")

    #C0140
    ChrTalk(
        0xA,
        (
            "お兄ちゃんが\x01",
            "ファッションチェック\x01",
            "しろっていうの。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xA,
        (
            "別にいいけど～、\x01",
            "お兄ちゃんもヒマよね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C18")

    label("loc_2B3D")

    OP_4B(0x9, 0xFF)
    TurnDirection(0x9, 0xA, 500)

    #C0142
    ChrTalk(
        0xA,
        "……さっきのの方がいいかも。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        "お兄ちゃん、よく見ると美形だし。\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x9,
        (
            "『よく見ると』は余計だ。\x01",
            "妹よ、訂正しろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xA,
        (
            "だって普通に見ると\x01",
            "フツーなんだもん。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x9,
        "こらシンディ、真面目にやれ！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0x9, 0xFF)

    label("loc_2C18")

    Jump("loc_36CC")

    label("loc_2C1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2D9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2C98")

    #C0147
    ChrTalk(
        0xA,
        (
            "いい旦那さんをもって\x01",
            "ソフィアさんは幸せだな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xA,
        (
            "あたしも早く\x01",
            "旦那さん欲しいな～、なんて♪\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D96")

    label("loc_2C98")


    #C0149
    ChrTalk(
        0xA,
        (
            "アンリが手伝ってくれると\x01",
            "早く終わって助かるな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xA,
        (
            "そういえば……お隣のハロルドさん、\x01",
            "最近お仕事を再開したんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xA,
        (
            "この前すれ違ったけど……\x01",
            "なんだか前より\x01",
            "一段と優しくなったみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xA,
        (
            "こう、包み込むような\x01",
            "大きな愛を感じちゃったわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_2D96")

    Jump("loc_36CC")

    label("loc_2D9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2E1D")

    #C0153
    ChrTalk(
        0xA,
        (
            "きゃは、あたしは\x01",
            "みっしぃのストラップを\x01",
            "手に入れちゃった～！\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xA,
        (
            "これって結構\x01",
            "レアグッズなのよ。\x01",
            "超ラッキー！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36CC")

    label("loc_2E1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2E95")

    #C0155
    ChrTalk(
        0xA,
        (
            "バシャバシャ……\x01",
            "お皿もコップもぴっかぴか～♪\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xA,
        (
            "早いこと片付けて\x01",
            "パレード見に行かなくっちゃね～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36CC")

    label("loc_2E95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2EED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2ED5")

    #C0157
    ChrTalk(
        0xA,
        (
            "へっへー、百貨店で\x01",
            "何買おうかしら！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EE8")

    label("loc_2ED5")

    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)
    Call(0, 13)
    OP_4C(0x8, 0xFF)
    OP_4C(0xC, 0xFF)

    label("loc_2EE8")

    Jump("loc_36CC")

    label("loc_2EED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2F48")

    #C0158
    ChrTalk(
        0xA,
        "お婆ちゃん、早く行こうよ！\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xA,
        (
            "もー、アンリも\x01",
            "早く仕度しなさいよね～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36CC")

    label("loc_2F48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_30CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2FBA")

    #C0160
    ChrTalk(
        0xA,
        (
            "ソフィアさんって\x01",
            "どこか影がある気がするのよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xA,
        "直接聞いたことはないんだけど。\x02",
    )

    CloseMessageWindow()
    Jump("loc_30C6")

    label("loc_2FBA")


    #C0162
    ChrTalk(
        0xA,
        (
            "ソフィアさんって毎週\x01",
            "教会のミサに参加してるのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xA,
        (
            "ほんとできた人よねー。\x01",
            "料理も上手いし、\x01",
            "旦那さんの仕事も手伝ってるし。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xA,
        (
            "でも……ソフィアさんって\x01",
            "ちょっと影があるっていうか。\x01",
            "どこか思いつめてる気がするのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xA,
        "直接聞いたことはないんだけど……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_30C6")

    Jump("loc_36CC")

    label("loc_30CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3215")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_314C")

    #C0166
    ChrTalk(
        0xA,
        (
            "パパは帰りは遅いし\x01",
            "朝の出勤も早いのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xA,
        (
            "あたし、将来の旦那様は\x01",
            "もっと大らかな職業がいいなー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3210")

    label("loc_314C")


    #C0168
    ChrTalk(
        0xA,
        "パパはＩＢＣの事業部に勤めてるの。\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xA,
        (
            "主任って言ってたから\x01",
            "結構偉い人みたいなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xA,
        (
            "でも帰りは遅いし、\x01",
            "朝の出勤も早いし……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xA,
        (
            "たまには休みを取って\x01",
            "ゆっくりしたらいいのになー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3210")

    Jump("loc_36CC")

    label("loc_3215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3295")
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3289")

    #C0172
    ChrTalk(
        0xA,
        "お兄ちゃんの社交界バカー！\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xA,
        (
            "あたし忙しいんだもん。\x01",
            "お兄ちゃん１人でやんなよー！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_328C")

    label("loc_3289")

    Call(0, 11)

    label("loc_328C")

    OP_4C(0x9, 0xFF)
    Jump("loc_36CC")

    label("loc_3295")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_33A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3312")

    #C0174
    ChrTalk(
        0xA,
        (
            "これからソフィアさんの\x01",
            "お宅でお料理教室があるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xA,
        (
            "今日は海鮮たっぷりの\x01",
            "グラタンを作るのよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_339D")

    label("loc_3312")


    #C0176
    ChrTalk(
        0xA,
        (
            "これからソフィアさんの\x01",
            "お宅でお料理教室があるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xA,
        (
            "えっと今日は\x01",
            "海鮮たっぷりのグラタンね。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xA,
        "うん、持ち物はこんな所かしら。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_339D")

    Jump("loc_36CC")

    label("loc_33A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_34E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3431")

    #C0179
    ChrTalk(
        0xA,
        (
            "明日はソフィアさんのお宅で\x01",
            "お料理教室があるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0xA,
        (
            "ふう、お兄ちゃんも遊んでないで\x01",
            "手伝ってくれたらいいのにな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34E4")

    label("loc_3431")


    #C0181
    ChrTalk(
        0xA,
        (
            "明日はソフィアさんのお宅で\x01",
            "お料理教室があるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xA,
        (
            "ソフィアさん、\x01",
            "お料理が上手だから\x01",
            "時々習いに行ってるわけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xA,
        (
            "ちゃちゃっと掃除を済ませて\x01",
            "準備しておかなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_34E4")

    Jump("loc_36CC")

    label("loc_34E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3619")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_354A")

    #C0184
    ChrTalk(
        0xA,
        "んー、味付けはこんな所かしら。\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xA,
        "あたし家事って結構得意なのよね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3614")

    label("loc_354A")


    #C0186
    ChrTalk(
        0xA,
        "んー、味付けはこんな所かしら。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xA,
        "あたし家事って結構得意なのよね。\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xA,
        (
            "昔からお婆ちゃんに\x01",
            "しつけられてるんだもん。\x01",
            "お料理なんてお手の物よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xA,
        (
            "ふふっ、将来いい\x01",
            "お嫁さんになれると思わない？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3614")

    Jump("loc_36CC")

    label("loc_3619")


    #C0190
    ChrTalk(
        0xA,
        (
            "うちはパパもママも忙しいから\x01",
            "お婆ちゃんが一家の中心なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xA,
        (
            "お兄ちゃんもあたしもアンリも、\x01",
            "お婆ちゃんに育ててもらったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xA,
        (
            "だからみ～んな\x01",
            "お婆ちゃんっ子なのよね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36CC")

    TalkEnd(0xFE)
    Return()

    # Function_12_2ABC end

    def Function_13_36D0(): pass

    label("Function_13_36D0")


    #C0193
    ChrTalk(
        0xA,
        (
            "あたし今日は\x01",
            "百貨店に行きたい！\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x8,
        (
            "アンリはどこか\x01",
            "行きたい所はありませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xC,
        (
            "僕は港湾区の屋台を\x01",
            "見てみたいです！\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x8,
        (
            "分かりました。\x01",
            "今日はそのルートを\x01",
            "行きましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x8,
        (
            "歩き疲れたらすぐに\x01",
            "お婆ちゃんに言うこと。\x01",
            "いいですね？\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x0, 2)
    Return()

    # Function_13_36D0 end

    def Function_14_37CD(): pass

    label("Function_14_37CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3879")

    #C0198
    ChrTalk(
        0xFE,
        (
            "今日は家事の手伝いが\x01",
            "入っちゃって……\x01",
            "遊びに行くのは遅れそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        "リュウ、大人しくしてるかな～。\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "放っておくと\x01",
            "いっつも無茶するんだから……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C15")

    label("loc_3879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_39B9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_38FE")

    #C0201
    ChrTalk(
        0xC,
        (
            "リュウはパレードを\x01",
            "追いかけてたみたいでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0xC,
        (
            "さすがリュウだなぁ……\x01",
            "元気が有り余ってたみたいです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39B4")

    label("loc_38FE")


    #C0203
    ChrTalk(
        0xC,
        (
            "今日は流石に\x01",
            "疲れちゃいました……\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xC,
        (
            "そういえばリュウも\x01",
            "パレードを見に来てた\x01",
            "みたいなんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xC,
        (
            "……お父さんと\x01",
            "口喧嘩しながら歩いてたんです。\x01",
            "だ、大丈夫なのかなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_39B4")

    Jump("loc_3C15")

    label("loc_39B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3A47")

    #C0206
    ChrTalk(
        0xC,
        "えっと、洗い物は、と……\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xC,
        (
            "皆さんもパレードを\x01",
            "見に行くんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xC,
        (
            "今日は人が多いらしいので、\x01",
            "気をつけてくださいね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C15")

    label("loc_3A47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3AD8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3AC0")

    #C0209
    ChrTalk(
        0xC,
        (
            "今日もお婆ちゃんが\x01",
            "連れて行ってくれるんです！\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xC,
        (
            "えへへ、やっぱり\x01",
            "お婆ちゃんは優しいです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AD3")

    label("loc_3AC0")

    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    Call(0, 13)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)

    label("loc_3AD3")

    Jump("loc_3C15")

    label("loc_3AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_3B4D")

    #C0211
    ChrTalk(
        0xC,
        (
            "お婆ちゃんは普段は厳しいけど\x01",
            "お祭りのときはお小遣いをくれるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xC,
        "ふふ、今日は楽しみです。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C15")

    label("loc_3B4D")

    OP_63(0xC, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0213
    ChrTalk(
        0xC,
        "あ、みなさん。\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xC,
        (
            "えへへ、これから家族で\x01",
            "おでかけする所なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xC,
        (
            "お婆ちゃんは普段は厳しいけど\x01",
            "お祭りのときはお小遣いをくれるので……\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xC,
        "ふふ、今日は楽しみです。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_3C15")

    TalkEnd(0xFE)
    Return()

    # Function_14_37CD end

    def Function_15_3C19(): pass

    label("Function_15_3C19")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_3C81")

    #C0217
    ChrTalk(
        0xD,
        (
            "思えば幼い頃も\x01",
            "お袋には家事を叩き込まれたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xD,
        "昔から教育熱心だったからな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CF9")

    label("loc_3C81")


    #C0219
    ChrTalk(
        0xD,
        (
            "お袋に、家の掃除を\x01",
            "するよう言われてな……\x02",
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
            "ううむ、今日は\x01",
            "たまの休日なんだが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_3CF9")

    TalkEnd(0xFE)
    Return()

    # Function_15_3C19 end

    SaveToFile()

Try(main)
