from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t1090.bin",                # FileName
        "t1090",                    # MapName
        "t1090",                    # Location
        0x0042,                     # MapIndex
        "ed7565",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 66, 0, 2, 0, 3],
    )

    BuildStringList((
        "t1090",                  # 0
        "キーア",                 # 1
        "ティオ",                 # 2
        "エリィ",                 # 3
    ))

    AddCharChip((
        "chr/ch08200.itc",                   # 00
        "chr/ch00200.itc",                   # 01
        "chr/ch00100.itc",                   # 02
    ))

    DeclNpc(-98199,  800,     -3890,   0,    389,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-98370,  0,       -200,    180,  389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-96000,  0,       3400,    0,    389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)

    DeclActor(-98200,  0,       -2640,   1200,    -98200,  2500,    -3890,   0x007E, 0,  4,  0x0000)

    ChipFrameInfo(312, 0)                                        # 0

    ScpFunction((
        "Function_0_138",          # 00, 0
        "Function_1_1F0",          # 01, 1
        "Function_2_2C1",          # 02, 2
        "Function_3_35F",          # 03, 3
        "Function_4_372",          # 04, 4
        "Function_5_434",          # 05, 5
        "Function_6_51C",          # 06, 6
        "Function_7_723",          # 07, 7
    ))


    def Function_0_138(): pass

    label("Function_0_138")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_178"),
        (1, "loc_184"),
        (2, "loc_190"),
        (3, "loc_19C"),
        (4, "loc_1A8"),
        (5, "loc_1B4"),
        (6, "loc_1C0"),
        (SWITCH_DEFAULT, "loc_1CC"),
    )


    label("loc_178")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_184")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_190")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_19C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1A8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1B4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1CC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1D8")

    label("loc_1EF")

    Return()

    # Function_0_138 end

    def Function_1_1F0(): pass

    label("Function_1_1F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C0")
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x258, 0xDAC)
    Sleep(400)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x190, 0xEA6)
    Sleep(250)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xDAC)
    Sleep(400)
    OP_63(0xFE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x190, 0xEA6)
    Sleep(250)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x258, 0xDAC)
    Sleep(400)
    OP_9C(0xFE, 0x0, 0x0, 0x0, 0x1F4, 0xEA6)
    Sleep(350)
    Jump("Function_1_1F0")

    label("loc_2C0")

    Return()

    # Function_1_1F0 end

    def Function_2_2C1(): pass

    label("Function_2_2C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_2CF")
    Jump("loc_35E")

    label("loc_2CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_2DD")
    Jump("loc_35E")

    label("loc_2DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_2EB")
    Jump("loc_35E")

    label("loc_2EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_2F9")
    Jump("loc_35E")

    label("loc_2F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_307")
    Jump("loc_35E")

    label("loc_307")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_315")
    Jump("loc_35E")

    label("loc_315")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_323")
    Jump("loc_35E")

    label("loc_323")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_355")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x1)
    BeginChrThread(0x8, 0, 0, 1)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_35E")

    label("loc_355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_35E")

    label("loc_35E")

    Return()

    # Function_2_2C1 end

    def Function_3_35F(): pass

    label("Function_3_35F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_371")
    OP_65(0x0, 0x1)

    label("loc_371")

    Return()

    # Function_3_35F end

    def Function_4_372(): pass

    label("Function_4_372")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_383")
    Jump("loc_430")

    label("loc_383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_391")
    Jump("loc_430")

    label("loc_391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_39F")
    Jump("loc_430")

    label("loc_39F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_3AD")
    Jump("loc_430")

    label("loc_3AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_3BB")
    Jump("loc_430")

    label("loc_3BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_3C9")
    Jump("loc_430")

    label("loc_3C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_427")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E4")
    Call(0, 6)
    Jump("loc_422")

    label("loc_3E4")

    SetChrPos(0x8, -98200, 800, -3890, 0)

    #C0001
    ChrTalk(
        0x8,
        "#01109Fフカフカベッド、キモチいいよー！\x02",
    )

    CloseMessageWindow()

    label("loc_422")

    Jump("loc_430")

    label("loc_427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_430")

    label("loc_430")

    TalkEnd(0x8)
    Return()

    # Function_4_372 end

    def Function_5_434(): pass

    label("Function_5_434")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_445")
    Jump("loc_518")

    label("loc_445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_453")
    Jump("loc_518")

    label("loc_453")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_461")
    Jump("loc_518")

    label("loc_461")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_471")
    Jump("loc_518")

    label("loc_471")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_47F")
    Jump("loc_518")

    label("loc_47F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_48D")
    Jump("loc_518")

    label("loc_48D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_49B")
    Jump("loc_518")

    label("loc_49B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_50F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B6")
    Call(0, 6)
    Jump("loc_50A")

    label("loc_4B6")


    #C0002
    ChrTalk(
        0x9,
        (
            "#00202Fこのベッドには心惹かれますが……\x02\x03",

            "#00206F……とりあえずは荷解きですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_50A")

    Jump("loc_518")

    label("loc_50F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_518")

    label("loc_518")

    TalkEnd(0xFE)
    Return()

    # Function_5_434 end

    def Function_6_51C(): pass

    label("Function_6_51C")

    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x8, -98200, 800, -3890, 0)

    def lambda_53A():
        TurnDirection(0x0, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_53A)
    Sleep(0)

    def lambda_54A():
        TurnDirection(0x1, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_54A)
    Sleep(0)

    def lambda_55A():
        TurnDirection(0x2, 0x8, 0)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_55A)
    Sleep(0)
    WaitChrThread(0x0, 0)
    WaitChrThread(0x1, 0)
    WaitChrThread(0x2, 0)

    #C0003
    ChrTalk(
        0x8,
        (
            "#01109F見て見て、ティオ！\x01",
            "すっごくフカフカだよー！\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x9,
        (
            "#00202Fこのベッド、かなりいい素材が\x01",
            "使われているみたいですね。\x02\x03",

            "#00204Fせっかくです、私も……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_611():
        TurnDirection(0x0, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_611)
    Sleep(50)

    def lambda_621():
        TurnDirection(0x1, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_621)
    Sleep(50)

    def lambda_631():
        TurnDirection(0x2, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_631)
    Sleep(50)
    WaitChrThread(0x0, 0)
    WaitChrThread(0x1, 0)
    WaitChrThread(0x2, 0)

    #C0005
    ChrTalk(
        0x101,
        (
            "#00006F２人して騒ぐと\x01",
            "さすがにうるさいと思うぞ……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)

    #C0006
    ChrTalk(
        0x9,
        "#00206F……無論、冗談です。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0007
    ChrTalk(
        0x104,
        "#00306F（ぜってぇ本気だったろ……）\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 3)
    OP_4C(0x9, 0xFF)
    OP_4C(0x8, 0xFF)
    TurnDirection(0x9, 0x8, 0)
    Return()

    # Function_6_51C end

    def Function_7_723(): pass

    label("Function_7_723")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_734")
    Jump("loc_99B")

    label("loc_734")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_742")
    Jump("loc_99B")

    label("loc_742")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_750")
    Jump("loc_99B")

    label("loc_750")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_760")
    Jump("loc_99B")

    label("loc_760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_76E")
    Jump("loc_99B")

    label("loc_76E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_77C")
    Jump("loc_99B")

    label("loc_77C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_78A")
    Jump("loc_99B")

    label("loc_78A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_992")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90D")

    #C0008
    ChrTalk(
        0xA,
        (
            "#00100Fまさかセシルさんたちが\x01",
            "来ているなんて驚いたわね。\x02\x03",

            "#00106Fこういう事を仕組むのは\x01",
            "ベルらしいというかなんというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、おかげでいきなり\x01",
            "脅威の男女比率になったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#00009Fでも、嬉しいサプライズ\x01",
            "だったのは確かだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xA,
        (
            "#00109Fま、まあそうだけど。\x02\x03",

            "#00106F子供の頃からなにかと\x01",
            "驚かされてばっかりだから、\x01",
            "ちょっと悔しいのよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_98D")

    label("loc_90D")


    #C0012
    ChrTalk(
        0xA,
        (
            "#00100Fそうそう、少し前に\x01",
            "ベルから聞いたんだけど、\x01",
            "ビーチはとても綺麗な所みたい。\x02\x03",

            "#00109Fふふ、楽しみにしておかないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_98D")

    Jump("loc_99B")

    label("loc_992")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_99B")

    label("loc_99B")

    TalkEnd(0xFE)
    Return()

    # Function_7_723 end

    SaveToFile()

Try(main)
