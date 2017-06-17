from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1020.bin",                # FileName
        "c1020",                    # MapName
        "c1020",                    # Location
        0x0014,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 20, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1020",                  # 0
        "セルダン支部長",         # 1
        "コパン",                 # 2
        "ペーター",               # 3
    ))

    AddCharChip((
        "chr/ch32200.itc",                   # 00
        "chr/ch23600.itc",                   # 01
        "chr/ch24200.itc",                   # 02
    ))

    DeclNpc(7230,    0,       9069,    180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-519,    0,       43310,   90,   389,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(7530,    0,       6780,    0,    261,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)

    DeclActor(6580,    0,       7980,    1500,    7230,    1500,    9070,    0x007E, 0,  3,  0x0000)
    DeclActor(470,     0,       43660,   1200,    470,     1500,    43360,   0x007C, 0,  14, 0x0000)

    ScpFunction((
        "Function_0_178",          # 00, 0
        "Function_1_230",          # 01, 1
        "Function_2_3DC",          # 02, 2
        "Function_3_410",          # 03, 3
        "Function_4_414",          # 04, 4
        "Function_5_FB5",          # 05, 5
        "Function_6_28CE",         # 06, 6
        "Function_7_2E7F",         # 07, 7
        "Function_8_3ABC",         # 08, 8
        "Function_9_3D97",         # 09, 9
        "Function_10_4651",        # 0A, 10
        "Function_11_481E",        # 0B, 11
        "Function_12_48DB",        # 0C, 12
        "Function_13_6C2F",        # 0D, 13
        "Function_14_6EC2",        # 0E, 14
    ))


    def Function_0_178(): pass

    label("Function_0_178")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1B8"),
        (1, "loc_1C4"),
        (2, "loc_1D0"),
        (3, "loc_1DC"),
        (4, "loc_1E8"),
        (5, "loc_1F4"),
        (6, "loc_200"),
        (SWITCH_DEFAULT, "loc_20C"),
    )


    label("loc_1B8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1C4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1D0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1DC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1E8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_1F4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_200")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_20C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_218")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_218")

    label("loc_22F")

    Return()

    # Function_0_178 end

    def Function_1_230(): pass

    label("Function_1_230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_26A")
    SetChrPos(0x9, -3550, 0, 51630, 0)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, 4310, 0, 310, 90)
    Jump("loc_3B5")

    label("loc_26A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_27D")
    SetChrFlags(0xA, 0x80)
    Jump("loc_3B5")

    label("loc_27D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_290")
    SetChrFlags(0xA, 0x80)
    Jump("loc_3B5")

    label("loc_290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2A3")
    SetChrFlags(0xA, 0x80)
    Jump("loc_3B5")

    label("loc_2A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2B1")
    Jump("loc_3B5")

    label("loc_2B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2C4")
    SetChrFlags(0xA, 0x80)
    Jump("loc_3B5")

    label("loc_2C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2D7")
    SetChrFlags(0xA, 0x80)
    Jump("loc_3B5")

    label("loc_2D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2F6")
    SetChrPos(0xA, 4310, 0, 310, 90)
    Jump("loc_3B5")

    label("loc_2F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_304")
    Jump("loc_3B5")

    label("loc_304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_317")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_3B5")

    label("loc_317")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_32A")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_3B5")

    label("loc_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_342")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)
    Jump("loc_3B5")

    label("loc_342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_37E")
    SetChrPos(0x9, -3550, 0, 51630, 0)
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_379")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_379")

    Jump("loc_3B5")

    label("loc_37E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_3B5")
    SetChrPos(0x9, -3550, 0, 51630, 0)
    ClearChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B5")
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0xA, 0x10)

    label("loc_3B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DB")
    SetMapFlags(0x10000000)
    Event(0, 8)

    label("loc_3DB")

    Return()

    # Function_1_230 end

    def Function_2_3DC(): pass

    label("Function_2_3DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F8")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_40F")

    label("loc_3F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_40F")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_40F")

    label("loc_40F")

    Return()

    # Function_2_3DC end

    def Function_3_410(): pass

    label("Function_3_410")

    Call(0, 4)
    Return()

    # Function_3_410 end

    def Function_4_414(): pass

    label("Function_4_414")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43E")
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    Call(0, 9)
    Return()

    label("loc_43E")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_D4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_585")

    #C0001
    ChrTalk(
        0x8,
        (
            "そうだロイド団員、\x01",
            "『段位認定試験』のことは知っているか？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "釣公師団では、腕前に応じた\x01",
            "『段位』って物を認定してるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "フハハ、立派な釣師段位ともなれば\x01",
            "一部のスジじゃ賞賛を浴びること間違いなしだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "まァ判らん事があれば尋ねてくれ。\x01",
            "俺が懇切丁寧に教えてやるからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6E, 1)
    TalkEnd(0x8)
    Return()

    label("loc_585")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_8F7")

    #C0005
    ChrTalk(
        0x8,
        "ようこそ、釣公師団へ！\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "ほほう、君がロイド団員だな？\x01",
            "かねがね話は聞いているぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "コパンのやつに誘われて\x01",
            "ウチに入団したそうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "俺は釣公師団・クロスベル支部の\x01",
            "支部長を務めるセルダンだ。\x01",
            "以後宜しくな、ロイド団員！\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        (
            "#0003Fええと、どうも……\x02\x03",

            "#0005Fというか、自分はいつの間に\x01",
            "釣公師団……に\x01",
            "入団したんですか？\x02\x03",

            "#0003F確かに以前\x01",
            "釣竿を受け取りましたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "ふはは、細かい事は気にするな！\x01",
            "君はもはや俺たちの同志も同然だぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        (
            "#0006F（ご、強引な人だな……）\x02\x03",

            "#0000F（まあ同じ趣味を持ってる人たちみたいだ、\x01",
            "  釣りの話なんかは合いそうだけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "そうだロイド団員、\x01",
            "『段位認定試験』のことは知っているか？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "釣公師団では、腕前に応じた\x01",
            "『段位』って物を認定してるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "フハハ、立派な釣師段位ともなれば\x01",
            "一部のスジじゃ賞賛を浴びること間違いなしだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "まァ判らん事があれば尋ねてくれ。\x01",
            "俺が懇切丁寧に教えてやるからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6E, 1)
    TalkEnd(0x8)
    Return()

    label("loc_8F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4D")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_A39")

    #C0016
    ChrTalk(
        0x8,
        (
            "おめでとう！\x01",
            "ついに入団したそうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "しかしコパンの奴も手が早いなァ。\x01",
            "俺が直々に勧誘しようと思っていた所を……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#0003F……やっぱり\x01",
            "そうだったんですか。\x02\x03",

            "#0005Fというか、自分はいつの間に\x01",
            "釣公師団……に\x01",
            "入団したんですか？\x02\x03",

            "#0003F釣竿を受け取った覚えしか\x01",
            "ないんですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B6A")

    label("loc_A39")


    #C0019
    ChrTalk(
        0x8,
        (
            "入団おめでとう！\x01",
            "ロイド団員、会えるのを楽しみにしていたぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "俺は釣公師団・クロスベル支部の\x01",
            "支部長を務めるセルダンだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        "以後宜しくな、ロイド団員！\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#0004Fはは、どうも……\x02\x03",

            "#0005Fというか、自分はいつの間に\x01",
            "釣公師団……に\x01",
            "入団したんですか？\x02\x03",

            "#0003F釣竿を受け取った覚えしか\x01",
            "ないんですが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B6A")


    #C0023
    ChrTalk(
        0x8,
        (
            "ふはは、細かい事は気にするな！\x01",
            "君はもはや俺たちの同志も同然だぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#0003F（ご、強引な人だな……）\x02\x03",

            "#0000F（まあ同じ趣味を持ってる人たちみたいだ、\x01",
            "  釣りの話なんかは合いそうだけど。）\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "そうだロイド団員、\x01",
            "『段位認定試験』のことは知っているか？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "釣公師団では、腕前に応じた\x01",
            "『段位』って物を認定してるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "フハハ、立派な釣師段位ともなれば\x01",
            "一部のスジじゃ賞賛を浴びること間違いなしだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "まァ判らん事があれば尋ねてくれ。\x01",
            "俺が懇切丁寧に教えてやるからな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6E, 1)
    TalkEnd(0x8)
    Return()

    label("loc_D4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 1)), scpexpr(EXPR_END)), "loc_FA7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D60")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA2")
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E21")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DCC")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_DCC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DEC")
    OP_AF(0x37)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E1C")

    label("loc_DEC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E00")
    Jump("loc_E1C")

    label("loc_E00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_E1C")

    Jump("loc_F9D")

    label("loc_E21")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_F11")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",            # 0
            "段位認定をする\x01",      # 1
            "買い物をする\x01",        # 2
            "やめる\x01",              # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E83")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_E83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA7")
    Call(0, 13)
    Call(0, 12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F0C")

    label("loc_EA7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EDC")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ECB")
    OP_AF(0x36)
    Jump("loc_ECD")

    label("loc_ECB")

    OP_AF(0x37)

    label("loc_ECD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F0C")

    label("loc_EDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EF0")
    Jump("loc_F0C")

    label("loc_EF0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F0C")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_F0C")

    Jump("loc_F9D")

    label("loc_F11")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",            # 0
            "段位認定をする\x01",      # 1
            "やめる\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F6D")
    Call(0, 13)
    Call(0, 12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F9D")

    label("loc_F6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F81")
    Jump("loc_F9D")

    label("loc_F81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F9D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_F9D")

    Jump("loc_D60")

    label("loc_FA2")

    Jump("loc_FAA")

    label("loc_FA7")

    Call(0, 5)

    label("loc_FAA")

    TalkEnd(0x8)
    OP_93(0x8, 0xB4, 0x0)
    Return()

    # Function_4_414 end

    def Function_5_FB5(): pass

    label("Function_5_FB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_103B")

    #C0029
    ChrTalk(
        0x8,
        (
            "２軒先にアカシア荘って\x01",
            "アパートがあるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "確か一室が空家になってたはずだ。\x01",
            "探してるのはそこの事じゃねえか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28CD")

    label("loc_103B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_147B")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1260")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_119F")

    #C0031
    ChrTalk(
        0x8,
        "ロイド団員はこんな話を知っているか？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "クロスベルには、伝説のヌシ\x01",
            "『サーペントヘッド』って奴がいるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "エルム湖を根城にしている\x01",
            "それはもう凶暴な奴でな、\x01",
            "昔は漁師にも恐れられていたらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "だが、奴はここ十数年\x01",
            "まったく目撃されてねえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "もしこいつを釣り上げられたら\x01",
            "勲章モノなんだがなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_125B")

    label("loc_119F")


    #C0036
    ChrTalk(
        0x8,
        (
            "『サーペントヘッド』はまさに\x01",
            "ヌシの中のヌシ……\x01",
            "奴を釣り上げるのは俺たち釣公師団の夢だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "ここ十数年は目撃されてねえが、\x01",
            "『特級釣師』になったお前さんなら\x01",
            "可能性はあるかもなァ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_125B")

    Jump("loc_1476")

    label("loc_1260")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13F6")

    #C0038
    ChrTalk(
        0x8,
        (
            "さすがロイド団員だ、\x01",
            "《釣聖》になっても謙虚だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "ふはは、気に入ったぜ！\x01",
            "今夜あたり夜釣りにいかねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "うちの支部は親睦会を兼ねて\x01",
            "よく行くんだよなァ、夜釣り！\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        (
            "#0000Fはは、すみません。\x01",
            "今夜はちょっと……\x02\x03",

            "また時間が取れたら\x01",
            "喜んで付き合いますけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        "ふははは、断り方まで謙虚だな！\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "よし、都合のいい日に声を掛けてくれ。\x01",
            "祝いを兼ねて釣り大会と行こうじゃねえか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1476")

    label("loc_13F6")


    #C0044
    ChrTalk(
        0x8,
        (
            "ロイド団員の\x01",
            "《釣聖》認定祝いをしねえとなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "サーペントヘッドを釣り上げた武勇伝も\x01",
            "ゆっくり聞かせてくれよ、ふははは！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1476")

    Jump("loc_28CD")

    label("loc_147B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1505")

    #C0046
    ChrTalk(
        0x8,
        (
            "日が落ちるな……\x01",
            "どこかの街道にでも\x01",
            "出掛けてみるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "今日の夜釣りは\x01",
            "前代未聞の超大物が\x01",
            "掛かりそうな予感がするぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28CD")

    label("loc_1505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_15EB")

    #C0048
    ChrTalk(
        0x8,
        (
            "おかしいな……\x01",
            "ヨアヒム師と連絡が取れねえんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "昨晩は一緒に\x01",
            "夜釣りをする約束だったんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#0006F（……例の成分検査に\x01",
            "  夢中になってるのかな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        (
            "#0300F（あの先生なら\x01",
            "  十分ありうる話だよなぁ。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28CD")

    label("loc_15EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1693")

    #C0052
    ChrTalk(
        0x8,
        (
            "ゴルドサモーナは\x01",
            "マインツ方面のどこかに\x01",
            "棲息するという幻の魚だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "流れるような流線型に\x01",
            "輝く金色の鱗……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "まさにサモーナの中の\x01",
            "サモーナだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28CD")

    label("loc_1693")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1800")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17A9")

    #C0055
    ChrTalk(
        0x8,
        "ロイド団員、大変だぞ！\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "今朝ヨアヒム団員が\x01",
            "ノーブルカルプの超大物を\x01",
            "釣り上げやがったんだ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "これで奴は特級釣師に昇格だ。\x01",
            "やられちまったなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        (
            "#0200Fヨアヒム先生……\x01",
            "相変わらずですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#0000F後でセシル姉に\x01",
            "言いつけておこうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17FB")

    label("loc_17A9")


    #C0060
    ChrTalk(
        0x8,
        (
            "ヨアヒム団員は\x01",
            "特級釣師に昇格だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "これからは\x01",
            "ヨアヒム師と呼ばねえとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17FB")

    Jump("loc_28CD")

    label("loc_1800")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1872")

    #C0062
    ChrTalk(
        0x8,
        (
            "そういえばロイド団員、\x01",
            "近頃姿を見なかったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "腕が鈍らねえよう\x01",
            "一日一釣を心がけておけよ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28CD")

    label("loc_1872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1A65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19E1")

    #C0064
    ChrTalk(
        0x8,
        (
            "実は記念祭に合わせて\x01",
            "イベントを考えていてなァ……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "リベールから１人\x01",
            "凄腕釣師をお呼びしようかと\x01",
            "思ってるんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x8, 0x101, 500)

    #C0066
    ChrTalk(
        0x8,
        (
            "ん、そういや……\x01",
            "君の名も『ロイド』だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        "ふはは、こいつはいいぜ……！\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        (
            "#0005Fは、はあ……？？\x01",
            "……何の話ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "いやいや、何でもねえよ。\x01",
            "まだ決まった話じゃねえしなァ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A60")

    label("loc_19E1")


    #C0070
    ChrTalk(
        0x8,
        (
            "記念祭に合わせて、リベールから\x01",
            "凄腕釣師をお呼びしようかと\x01",
            "思ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "特別ゲストって奴さ。\x01",
            "ふはは、楽しみだなァ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A60")

    Jump("loc_28CD")

    label("loc_1A65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1C24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BB9")

    #C0072
    ChrTalk(
        0x8,
        (
            "この時期の朝釣りといえば\x01",
            "ウルスラ間道だろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "実はウルスラ病院には\x01",
            "我らが同士が居てな。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x8,
        (
            "よく仕事を抜け出しては\x01",
            "釣りにかまけているはずだぞ、\x01",
            "ふははは！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0075
    ChrTalk(
        0x101,
        "#0005Fウルスラ病院の釣り好き……？\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x104,
        "#0306Fま、まさかなぁ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C1F")

    label("loc_1BB9")


    #C0077
    ChrTalk(
        0x8,
        (
            "この時期の朝釣りといえば\x01",
            "ウルスラ間道だろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "ロイド団員も気が向いたら\x01",
            "行ってみるといい！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C1F")

    Jump("loc_28CD")

    label("loc_1C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1CB7")

    #C0079
    ChrTalk(
        0x8,
        (
            "思ったように釣れねえときは\x01",
            "竿やエサの種類を変えてみるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        "釣れる魚が変わってくるぞ。\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        "ま、試行錯誤してみることだな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_28CD")

    label("loc_1CB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1EF3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E37")

    #C0082
    ChrTalk(
        0x8,
        "釣公師団へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "ロイド団員、\x01",
            "釣りははかどっているか？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#0000Fはは、まあまあと言ったところです。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "そうかァ、まあ警察官は\x01",
            "忙しいと聞くからな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DEB")

    #C0086
    ChrTalk(
        0x8,
        (
            "十分な釣果を上げたら\x01",
            "ぜひ報告に来てくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "段位が上がるたびに\x01",
            "豪華な賞品を進呈しているからな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E2F")

    label("loc_1DEB")


    #C0088
    ChrTalk(
        0x8,
        (
            "大物が釣れたら\x01",
            "ぜひ報告に来てくれよ。\x01",
            "楽しみにさせてもらうぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E2F")

    SetScenarioFlags(0x0, 0)
    Jump("loc_1EEE")

    label("loc_1E37")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1EB3")

    #C0089
    ChrTalk(
        0x8,
        (
            "段位認定試験は\x01",
            "指定の魚を釣る事を\x01",
            "条件としている。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "十分な釣果を上げたら\x01",
            "ぜひ報告に来てくれよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EEE")

    label("loc_1EB3")


    #C0091
    ChrTalk(
        0x8,
        (
            "ロイド団員、また大物が釣れたら\x01",
            "ぜひ報告に来てくれよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EEE")

    Jump("loc_28CD")

    label("loc_1EF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_229C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21EB")
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x8, 0x101, 0)
    TurnDirection(0xA, 0x101, 0)

    #C0092
    ChrTalk(
        0xA,
        "ロイドさん、ご存知ですか？\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        (
            "実は先日、もう１人\x01",
            "団員が増えたんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        "#0000Fへえ、そうなんですか。\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "おう、なんと女性釣師だ。\x01",
            "それもとびっきり凄腕のなァ。\x02",
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
    Sleep(1200)

    #C0096
    ChrTalk(
        0xA,
        (
            "エステルという方で、\x01",
            "有名な遊撃士だそうですよ。\x01",
            "雑誌で見た事はありませんか？\x02",
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
    Sleep(1200)

    #C0097
    ChrTalk(
        0x8,
        (
            "俺も一度同伴させてもらったが\x01",
            "遊撃士だけあって\x01",
            "さすが見事な反射神経だった……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        (
            "フフ、ロイド団員よ。\x01",
            "強敵出現だなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        (
            "#0006Fそれ以前から\x01",
            "強敵なんですけど……\x01",
            "（まさか釣りまでやるとは……）\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x104,
        (
            "#0300Fエステルちゃん、\x01",
            "何でもアリだな……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x0, 0x0)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x6C, 6)
    Jump("loc_2297")

    label("loc_21EB")


    #C0101
    ChrTalk(
        0x8,
        (
            "エステル団員は\x01",
            "リベール王国に居た頃から\x01",
            "釣りを嗜んでいたという……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "リベールといえば\x01",
            "我ら釣公師団発祥の地。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "ロイド団員、お前さんも\x01",
            "うかうかしてられねえなァ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2297")

    Jump("loc_28CD")

    label("loc_229C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2584")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2368")

    #C0104
    ChrTalk(
        0x8,
        (
            "我が釣公師団は\x01",
            "釣り文化の普及のために\x01",
            "活動する集団だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        (
            "高い目標意識を持つため\x01",
            "『段位認定試験』も実施しているぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "判らん事があれば\x01",
            "いつでも俺に声を掛けるがいい！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_257F")

    label("loc_2368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24FF")

    #C0107
    ChrTalk(
        0x8,
        (
            "さすがロイド団員だ、\x01",
            "《釣聖》になっても謙虚だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "ふはは、気に入ったぜ！\x01",
            "今夜あたり夜釣りにいかねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        (
            "うちの支部は親睦会を兼ねて\x01",
            "よく行くんだよなァ、夜釣り！\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#0000Fはは、すみません。\x01",
            "今夜はちょっと……\x02\x03",

            "また時間が取れたら\x01",
            "喜んで付き合いますけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        "ふははは、断り方まで謙虚だな！\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x8,
        (
            "よし、都合のいい日に声を掛けてくれ。\x01",
            "祝いを兼ねて\x01",
            "釣り大会と行こうじゃねえか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_257F")

    label("loc_24FF")


    #C0113
    ChrTalk(
        0x8,
        (
            "ロイド団員の\x01",
            "《釣聖》認定祝いをしねえとなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "サーペントヘッドを釣り上げた武勇伝も\x01",
            "ゆっくり聞かせてくれよ、ふははは！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_257F")

    Jump("loc_28CD")

    label("loc_2584")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_266B")
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0115
    ChrTalk(
        0x8,
        (
            "コパンの奴、また\x01",
            "大物を釣り上げやがったなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x8,
        (
            "ペーター、こいつぁ\x01",
            "俺たちも負けてられねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xA,
        (
            "そうですねぇ、\x01",
            "腕が疼いてきましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xA,
        (
            "うふふ、今晩辺り\x01",
            "夜釣りにでも\x01",
            "繰り出しましょうか。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    Jump("loc_28CD")

    label("loc_266B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_271F")

    #C0119
    ChrTalk(
        0x8,
        (
            "ペーター団員、\x01",
            "俺がイベント好きなのは\x01",
            "知っているだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        (
            "ふはは、渓流流し釣り大会でも\x01",
            "開催しちまうかなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x102,
        "#0105F（どういう人たちなのかしら……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_28CD")

    label("loc_271F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2808")

    #C0122
    ChrTalk(
        0x8,
        (
            "我ら釣公師団は\x01",
            "いつでも団員大募集だ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 0)

    #C0123
    ChrTalk(
        0x8,
        (
            "どうだ青年、俺たちの\x01",
            "仲間に入らねぇか？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x8,
        (
            "フハハ、経験者なら\x01",
            "大歓迎してやるぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            "#0006Fすみません、仕事中なもので……\x01",
            "（研修中にそんな余裕はないよ……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_28CD")

    label("loc_2808")


    #C0126
    ChrTalk(
        0x8,
        (
            "我ら釣公師団は\x01",
            "いつでも団員大募集だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x8,
        (
            "嘘だと思うなら入団してみるがいい。\x01",
            "フハハハハ！\x02",
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
    Sleep(1200)

    label("loc_28CD")

    Return()

    # Function_5_FB5 end

    def Function_6_28CE(): pass

    label("Function_6_28CE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2959")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2923")

    #C0128
    ChrTalk(
        0xFE,
        "ほれ、エサっす。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        "たんと食べるっすねー。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2954")

    label("loc_2923")


    #C0130
    ChrTalk(
        0xFE,
        (
            "……アカムシが余ったんで。\x01",
            "それだけっすよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2954")

    Jump("loc_2E7B")

    label("loc_2959")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2967")
    Jump("loc_2E7B")

    label("loc_2967")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2A99")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A00")

    #C0131
    ChrTalk(
        0xFE,
        "あ、どうもっす。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "支部長たちは下にいるんで\x01",
            "話あったらどうぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "段位認定試験の事とかは\x01",
            "聞いといて損はないっすよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x70, 6)
    Jump("loc_2A94")

    label("loc_2A00")


    #C0134
    ChrTalk(
        0xFE,
        (
            "エサによって掛かる魚も\x01",
            "変わってくるんすよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "目当ての魚が釣れないときは\x01",
            "エサを変えてみるといいっす。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        "ま、エサ選びは試行錯誤っすねー。\x02",
    )

    CloseMessageWindow()

    label("loc_2A94")

    Jump("loc_2E7B")

    label("loc_2A99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2C51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BAF")

    #C0137
    ChrTalk(
        0xFE,
        (
            "あれ、皆さんもバスで\x01",
            "戻ってきたんすか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "同じ便じゃなかった\x01",
            "気がするっすけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        "……まあいいや。\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "支部長たちに話はしておいたっす。\x01",
            "皆さん下にいるんで、\x01",
            "何かあったらどうぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "段位認定試験の事とかは\x01",
            "聞いといて損はないっすよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x70, 6)
    Jump("loc_2C4C")

    label("loc_2BAF")


    #C0142
    ChrTalk(
        0xFE,
        "どうもっす。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "自分よくここに出入りしてるんで\x01",
            "分からない事あったら\x01",
            "聞いてくれていいっすよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "そのうちオススメの釣りポイントとか\x01",
            "お教えするっす。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C4C")

    Jump("loc_2E7B")

    label("loc_2C51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_2C5F")
    Jump("loc_2E7B")

    label("loc_2C5F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D1E")

    #C0145
    ChrTalk(
        0xFE,
        (
            "なんでオレが\x01",
            "水槽の世話なんてー。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "あー、ダルい。\x01",
            "面倒っすねー……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            " #0005Fか、かなり大きい水槽ですね。\x01",
            "（どういう施設なんだろう、\x01",
            "  ここは……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2D79")

    label("loc_2D1E")


    #C0148
    ChrTalk(
        0xFE,
        (
            "ちなみにこの水槽は\x01",
            "オーバルストアの特注品っすよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        "ウチの支部長、金持ちっすから。\x02",
    )

    CloseMessageWindow()

    label("loc_2D79")

    Jump("loc_2E7B")

    label("loc_2D7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E24")

    #C0150
    ChrTalk(
        0xFE,
        (
            "『釣公師団』ってのは\x01",
            "クロスベルに住む釣り好き集団っす。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        "ま、いちおーオレも団員っすねー。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "団員Ｎｏ．３、コパン。\x01",
            "段位は特級釣師っす。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E7B")

    label("loc_2E24")


    #C0153
    ChrTalk(
        0xFE,
        (
            "オレも団員っすけど。\x01",
            "あんまツルむの苦手なんすよねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        "なんかダルいっすしー。\x02",
    )

    CloseMessageWindow()

    label("loc_2E7B")

    TalkEnd(0xFE)
    Return()

    # Function_6_28CE end

    def Function_7_2E7F(): pass

    label("Function_7_2E7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EA9")
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    Call(0, 9)
    Return()

    label("loc_2EA9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3096")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F76")

    #C0155
    ChrTalk(
        0xFE,
        (
            "おやロイド団員、\x01",
            "これから夜釣りでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        "うふふ、頑張ってくださいねぇ。\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "貴方なら特級釣師以上を\x01",
            "狙えるかもしれません。\x01",
            "そんな気がするんですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2FD4")

    label("loc_2F76")


    #C0158
    ChrTalk(
        0xFE,
        (
            "ロイド団員なら特級釣師以上の\x01",
            "称号を狙えるかもしれません。\x01",
            "夜釣り、頑張ってくださいねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FD4")

    Jump("loc_3091")

    label("loc_2FD9")


    #C0159
    ChrTalk(
        0xFE,
        (
            "それにしても、\x01",
            "さすがロイド団員ですねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "入団して僅かな期間で\x01",
            "《釣聖》になられるなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "うふふ、これからも共に\x01",
            "釣公師団・クロスベル支部を\x01",
            "盛り上げて行きましょうねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3091")

    Jump("loc_3AB8")

    label("loc_3096")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_314F")

    #C0162
    ChrTalk(
        0xFE,
        (
            "リベールからのゲストの方は\x01",
            "先週帰国してしまったんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "いやはや、あの方との勝負は\x01",
            "いい経験になりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "私ももっともっと\x01",
            "腕を磨かないといけませんねえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AB8")

    label("loc_314F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_31FB")

    #C0165
    ChrTalk(
        0xFE,
        (
            "今日は私も釣りに\x01",
            "出かけるつもりなんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "あの遊撃士のエステルさんも\x01",
            "順調に釣果を\x01",
            "挙げているそうですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "うふふ、負けて\x01",
            "いられませんねえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AB8")

    label("loc_31FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3342")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_329E")

    #C0168
    ChrTalk(
        0xFE,
        (
            "ロイド団員、\x01",
            "西クロスベル街道には\x01",
            "行ってみましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "最近は導力バスも\x01",
            "本数が増えましたからねえ。\x01",
            "どこへなり釣りに行けますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_333D")

    label("loc_329E")


    #C0170
    ChrTalk(
        0xFE,
        (
            "ああ、ちなみにコパン君は\x01",
            "マインツ山道に行っているそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "恐らく、山道途中のバス停で降りた\x01",
            "滝の辺りでしょうねえ。\x01",
            "彼のお気に入りの場所なんですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_333D")

    Jump("loc_3AB8")

    label("loc_3342")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_36E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3643")
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x8, 0x101, 0)
    TurnDirection(0xA, 0x101, 0)

    #C0172
    ChrTalk(
        0xA,
        "ロイドさん、ご存知ですか？\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xA,
        (
            "今日もう１人\x01",
            "団員が増えたんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        "#0000Fへえ、そうなんですか。\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x8,
        (
            "おう、なんと女性釣師だ。\x01",
            "それもとびっきり凄腕のなァ。\x02",
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
    Sleep(1200)

    #C0176
    ChrTalk(
        0xA,
        (
            "エステルという方で、\x01",
            "有名な遊撃士だそうですよ。\x01",
            "雑誌で見た事はありませんか？\x02",
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
    Sleep(1200)

    #C0177
    ChrTalk(
        0x8,
        (
            "俺も一度同伴させてもらったが\x01",
            "遊撃士だけあって\x01",
            "さすが見事な反射神経だった……\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x8,
        (
            "フフ、ロイド団員よ。\x01",
            "強敵出現だなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        (
            "#0006Fそれ以前から\x01",
            "強敵なんですけど……\x01",
            "（まさか釣りまでやるとは……）\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x104,
        (
            "#0300Fエステルちゃん、\x01",
            "何でもアリだな……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xA, 0x0, 0x0)
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x6C, 6)
    Jump("loc_36DD")

    label("loc_3643")


    #C0181
    ChrTalk(
        0xFE,
        (
            "エステルさんはリベールで\x01",
            "かなり高位の釣り称号を\x01",
            "お持ちだったそうですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "お仕事が忙しいそうですけど、\x01",
            "一度釣り勝負でも\x01",
            "してみたいものですねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36DD")

    Jump("loc_3AB8")

    label("loc_36E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_39AF")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3825")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37B6")

    #C0183
    ChrTalk(
        0xFE,
        "コパン君から聞きましたよ！\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "いやあ新しい仲間が\x01",
            "増えると嬉しいものですねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "釣果を上げられた時は\x01",
            "ぜひここにいらしてください。\x01",
            "我々も楽しみにしていますから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3820")

    label("loc_37B6")


    #C0186
    ChrTalk(
        0xFE,
        (
            "うふふ、釣果を上げられた時は\x01",
            "ぜひここにいらしてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "私たちも楽しみに\x01",
            "していますからねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3820")

    Jump("loc_39AA")

    label("loc_3825")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_393E")

    #C0188
    ChrTalk(
        0xFE,
        (
            "ロイド団員、《釣聖》の称号、\x01",
            "おめでとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "釣公師団はこのクロスベルと\x01",
            "リベール王国に拠点があるんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "《釣聖》になったのは\x01",
            "ロイド団員で２人目ということに\x01",
            "なりますねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "ちなみに《リベールの釣聖》は\x01",
            "女性の遊撃士の方だそうですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_39AA")

    label("loc_393E")


    #C0192
    ChrTalk(
        0xFE,
        (
            "ロイド団員、《釣聖》の称号、\x01",
            "おめでとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "これからも支部を\x01",
            "盛り上げて行きましょうねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39AA")

    Jump("loc_3AB8")

    label("loc_39AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_39C0")
    Call(0, 4)
    Jump("loc_3AB8")

    label("loc_39C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A5F")

    #C0194
    ChrTalk(
        0xFE,
        (
            "うふふ、マインツ山道の\x01",
            "渓流で流し釣りですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "楽しみですねえ。\x01",
            "ワクワクしちゃいますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x101,
        "#0000F（何だか話し中みたいだな……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AB8")

    label("loc_3A5F")


    #C0197
    ChrTalk(
        0xFE,
        (
            "皆さんも機会があれば\x01",
            "ぜひ釣公師団に入ってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        "うふふ、歓迎いたしますよ。\x02",
    )

    CloseMessageWindow()

    label("loc_3AB8")

    TalkEnd(0xFE)
    Return()

    # Function_7_2E7F end

    def Function_8_3ABC(): pass

    label("Function_8_3ABC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(470, 1400, 310, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22440, 0)
    SetChrPos(0x101, -1580, 0, -580, 45)
    SetChrPos(0x102, -580, 0, -1580, 45)
    SetChrPos(0x104, -1580, 0, -2580, 45)
    SetChrPos(0x103, -2580, 0, -1580, 45)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(1850, 1400, 1760, 3000)
    MoveCamera(45, 34, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(20100, 3000)

    def lambda_3BAD():
        OP_95(0xFE, 1310, 0, 2330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3BAD)

    def lambda_3BC7():
        OP_95(0xFE, 2310, 0, 1130, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3BC7)

    def lambda_3BE1():
        OP_95(0xFE, 1310, 0, 130, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3BE1)

    def lambda_3BFB():
        OP_95(0xFE, 110, 0, 1130, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3BFB)

    def lambda_3C15():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3C15)

    def lambda_3C26():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3C26)

    def lambda_3C37():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3C37)

    def lambda_3C48():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3C48)
    Sleep(3000)

    #C0199
    ChrTalk(
        0x101,
        (
            "#5P#0005F遊撃士協会の右隣……\x01",
            "あれ、ここが空家な筈なんだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(3480, 1400, 3380, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24740, 0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_0D()
    Sleep(700)

    #C0200
    ChrTalk(
        0x103,
        (
            "#5P#0200Fどう見ても\x01",
            "空家ではありませんね……\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x104,
        (
            "#11P#0300F一応受付にいる人に\x01",
            "話を聞いてみるか？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 1210, 0, 1210, 45)
    SetChrPos(0x1, 1210, 0, 1210, 45)
    SetChrPos(0x2, 1210, 0, 1210, 45)
    SetChrPos(0x3, 1210, 0, 1210, 45)
    ClearMapFlags(0x10000000)
    OP_29(0x3, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_8_3ABC end

    def Function_9_3D97(): pass

    label("Function_9_3D97")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_68(5760, 1300, 6920, 0)
    MoveCamera(19, 19, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22710, 0)
    SetChrPos(0x101, 4560, 0, 6480, 45)
    SetChrPos(0x102, 5370, 0, 5660, 45)
    SetChrPos(0x103, 3590, 0, 5480, 45)
    SetChrPos(0x104, 4390, 0, 4680, 45)
    OP_93(0x8, 0x87, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0202
    ChrTalk(
        0xA,
        (
            "#11Pまた釣り遊行にでも\x01",
            "出かけたいものですねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x8,
        "#5Pふはは、楽しみだなァ。\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x101,
        (
            "#5P#0005Fあのー、すみません。\x01",
            "こちらは……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_93(0x8, 0xE1, 0x1F4)
    OP_93(0xA, 0xE1, 0x1F4)
    Sleep(300)

    #C0205
    ChrTalk(
        0x8,
        (
            "#11Pおっ、入団希望者か？\x01",
            "ふはは、歓迎してやるぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xA,
        "#11P我らが《釣公師団》へようこそ！\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xA,
        (
            "#11P嬉しいですねぇ、こんな若者たちが\x01",
            "こぞって入団してくれるなんて……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(30)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(10)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(10)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0208
    ChrTalk(
        0x104,
        "#6P#0305F《釣公師団》……入団……？\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x101,
        "#5P#0006Fあの、ここは一体……\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x8,
        (
            "#11Pおう、釣りバカどもの集まり\x01",
            "《釣公師団》のクロスベル支部だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x8,
        (
            "#11Pふむ……ジャケットの青年。\x01",
            "君は釣りの経験がありそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x8,
        (
            "#11P隠しても無駄だぜ、俺には判るんだ。\x01",
            "……どうだ、俺たちの仲間に入らんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x101,
        (
            "#5P#0005Fえ……？\x01",
            "た、確かに小さい頃に\x01",
            "やったことはありますけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0214
    ChrTalk(
        0x101,
        (
            "#5P#0011F……っていうかあの、\x01",
            "今は仕事中なので！\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x102,
        (
            "#12P#0109F（あはは……変に\x01",
            "  言い当てられちゃったみたいね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x103,
        "#6P#0203F（何だか変なおじさんたちです。）\x02",
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x101,
        (
            "#5P#0006F（はあ、調子が狂うな……）\x02\x03",

            "#0000Fあのええと……ともかく\x01",
            "ここは空家ではないんですよね？\x02\x03",

            "市役所の登録では\x01",
            "空家となっているんですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0218
    ChrTalk(
        0xA,
        (
            "#11Pいえいえ、そんなはずは\x01",
            "ありませんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xA,
        (
            "#11P見ての通り精力的に\x01",
            "活動中でありますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x8,
        "#11Pふむ、空家といえば……\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0221
    ChrTalk(
        0x8,
        (
            "#11P２軒先にアカシア荘って\x01",
            "アパートがあるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x8,
        (
            "#11P確か一室が空家になってたはずだぞ。\x01",
            "そこの事じゃねえのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x8,
        (
            "#11Pアカシア荘はウチの２軒向こう側、\x01",
            "遊撃士協会の左隣だ。\x02",
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
    Sleep(300)

    def lambda_44D9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_44D9)

    def lambda_44E6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_44E6)

    def lambda_44F3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_44F3)

    def lambda_4500():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4500)
    Sleep(500)

    #C0224
    ChrTalk(
        0x104,
        (
            "#0303F#12P２軒違いの住所……\x01",
            "市役所の書類が間違ってんのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        (
            "#5P#0000Fうーん……\x01",
            "可能性はあるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x102,
        (
            "#12P#0100Fどちらにしろ市役所の記録は\x01",
            "正しくないみたいだし……\x01",
            "確認に行った方が良さそうね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0x8, 0xFF)
    OP_4C(0xA, 0xFF)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xA, 0x10)
    SetChrPos(0x0, 4780, 0, 5260, 225)
    SetChrPos(0x1, 4780, 0, 5260, 225)
    SetChrPos(0x2, 4780, 0, 5260, 225)
    SetChrPos(0x3, 4780, 0, 5260, 225)
    OP_93(0x8, 0xB4, 0x0)
    OP_93(0xA, 0x0, 0x0)
    OP_29(0x3, 0x1, 0x4)
    SetScenarioFlags(0x0, 3)
    EventEnd(0x5)
    Return()

    # Function_9_3D97 end

    def Function_10_4651(): pass

    label("Function_10_4651")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(6970, 1400, 7010, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19720, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46D2")
    SetChrPos(0x101, 6200, 0, 6250, 0)
    SetChrPos(0xEF, 7400, 0, 6250, 0)
    SetChrPos(0x153, 6200, 0, 5050, 0)
    Jump("loc_47FA")

    label("loc_46D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4744")
    SetChrPos(0x101, 6200, 0, 6250, 0)
    SetChrPos(0x102, 7400, 0, 6250, 0)
    SetChrPos(0x103, 6200, 0, 5050, 0)
    SetChrPos(0x104, 7400, 0, 5050, 0)
    SetChrPos(0x109, 6200, 0, 3850, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_47FA")

    label("loc_4744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47B6")
    SetChrPos(0x101, 6200, 0, 6250, 0)
    SetChrPos(0x102, 7400, 0, 6250, 0)
    SetChrPos(0x103, 6200, 0, 5050, 0)
    SetChrPos(0x104, 7400, 0, 5050, 0)
    SetChrPos(0x10A, 6200, 0, 3850, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_47FA")

    label("loc_47B6")

    SetChrPos(0x101, 6200, 0, 6250, 0)
    SetChrPos(0x102, 7400, 0, 6250, 0)
    SetChrPos(0x103, 6200, 0, 5050, 0)
    SetChrPos(0x104, 7400, 0, 5050, 0)

    label("loc_47FA")

    OP_93(0x8, 0xB4, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    FadeToBright(500, 0)
    OP_0D()
    Return()

    # Function_10_4651 end

    def Function_11_481E(): pass

    label("Function_11_481E")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_483C")
    Jump("loc_4876")

    label("loc_483C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4859")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_4876")

    label("loc_4859")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4876")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_4876")

    label("loc_4876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4889")
    Jump("loc_48B9")

    label("loc_4889")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_489C")
    Jump("loc_48B9")

    label("loc_489C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_48AF")
    Jump("loc_48B9")

    label("loc_48AF")

    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)

    label("loc_48B9")

    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 5410, 0, 6840, 45)
    TurnDirection(0x8, 0x0, 0)
    EventEnd(0x5)
    TalkBegin(0x8)
    Return()

    # Function_11_481E end

    def Function_12_48DB(): pass

    label("Function_12_48DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4BE8")

    #C0227
    ChrTalk(
        0x8,
        (
            "釣公師団は、釣り文化の普及や技術向上のため\x01",
            "『段位認定試験』ってのを実施している。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x8,
        (
            "君の釣り技術を認定して\x01",
            "さまざまな称号や褒賞品などを進呈するぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x8,
        (
            "ふむ、ロイド団員は入団したばかりだから\x01",
            "現在の段位は『駆け出し釣り師』だな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4AD8")

    #C0230
    ChrTalk(
        0x8,
        (
            "次の段位へ進む条件は\x01",
            "『４種類以上の魚』を釣ることだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x8,
        (
            "釣り手帳を見れば\x01",
            "釣った事のある魚が記されているだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x8,
        "４種類以上釣れたら、ぜひ報告に来てくれ。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x8,
        (
            "フハハ、釣りは楽しいぜ？\x01",
            "工夫を凝らして挑戦してみてくれよな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BE0")

    label("loc_4AD8")


    #C0234
    ChrTalk(
        0x8,
        (
            "次の段位へ進む条件は\x01",
            "『４種類以上の魚』を釣ることだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x8,
        (
            "……と思ったら、なんだ。\x01",
            "もう４種類以上の魚を釣っているのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x8,
        (
            "まあいい、釣り手帳は\x01",
            "きちんとチェックしたいからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x8,
        (
            "もう一度俺に話しかけてくれ。\x01",
            "フハハ、次の段位を認定してやろうじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BE0")

    SetScenarioFlags(0x69, 6)
    Jump("loc_6C2E")

    label("loc_4BE8")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5037")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4F34")
    Call(0, 10)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0238
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "セルダン支部長は\x01",
            "ロイドの釣り手帳をチェックした。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0239
    ChrTalk(
        0x8,
        (
            "おっ……ロイド団員、\x01",
            "中々目覚しい釣果じゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x8,
        (
            "よくやったな。\x01",
            "今日から君は『道楽釣り師』だ！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(74, 0, 100, 0)

    #A0241
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "段位『道楽釣り師』に認められた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(17, 0, 100, 0)

    #A0242
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "褒賞として",
            scpstr(SCPSTR_CODE_ITEM, 0x5A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x5A, 1)
    OP_D0(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0243
    ChrTalk(
        0x8,
        (
            "こいつァ俺が愛用していた\x01",
            "麦わら帽子でな。\x01",
            "釣りにはもってこいだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x8,
        (
            "ロイド団員、こいつを身につけて\x01",
            "今後も釣りに励んでくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x101,
        (
            "#0002F釣りの定番アイテムですよね。\x01",
            "ありがたく受け取っておきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x8,
        (
            "うむ、『道楽釣り師』といえば\x01",
            "まだまだだが、段位が上がるにつれ\x01",
            "豪華褒章品なども用意しているぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x8,
        (
            "フフ……ついでに次の段位認定の\x01",
            "条件も伝えておくか。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x8,
        (
            "次の段位へ進むためには\x01",
            "『８種類以上の魚』を釣らねばならん。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x8,
        "工夫を凝らして挑戦してくれたまえ。\x02",
    )

    CloseMessageWindow()
    Call(0, 11)
    Jump("loc_5032")

    label("loc_4F34")


    #C0250
    ChrTalk(
        0x8,
        (
            "ロイド団員の現在の段位は\x01",
            "『駆け出し釣り師』だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        (
            "次の段位へ進むためには\x01",
            "『４種類以上の魚』を釣ることだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x8,
        (
            "釣り手帳を見れば\x01",
            "何種類釣ったか一目で確認できるはずだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x8,
        (
            "フフ……釣果が上がったら見せに来るといい。\x01",
            "俺が段位を認定してやるぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5032")

    Jump("loc_6C2E")

    label("loc_5037")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55DA")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5520")
    Call(0, 10)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0254
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "セルダン支部長は\x01",
            "ロイドの釣り手帳をチェックした。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0255
    ChrTalk(
        0x8,
        (
            "おっ……ロイド団員、\x01",
            "中々素晴らしい釣果じゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x8,
        (
            "よくやったな。\x01",
            "今日から君は『生業釣り師』だ！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(74, 0, 100, 0)

    #A0257
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "段位『生業釣り師』に認められた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(17, 0, 100, 0)

    #A0258
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "褒賞として",
            scpstr(SCPSTR_CODE_ITEM, 0x9E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x9E, 1)
    OP_D0(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0259
    ChrTalk(
        0x8,
        (
            "思い出すなァ、俺が\x01",
            "『生業釣り師』になった日の事を……\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x8,
        (
            "元々釣り好きだった俺は、\x01",
            "仕事で立ち寄ったリベール王国で\x01",
            "《釣公師団》を名乗る男と出会ってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x8,
        (
            "フハハ、それが言わずと知れた\x01",
            "あの伝説的釣師フィッシャー団長さ！\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x8,
        (
            "まァ色々あって、団長直々に\x01",
            "『生業釣り師』の段位を授かる事になった。\x01",
            "懐かしいなァ……\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x101,
        (
            "#0012Fそ、そうだったんですか。\x01",
            "（支部長の昔話か……\x01",
            "  長くなりそうだな。）\x02\x03",

            "#0000Fあれ、でも仕事でリベール王国に\x01",
            "立ち寄ったってことは……\x01",
            "以前は貿易商か何かを？\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x8,
        (
            "フハハ、いやいや。\x01",
            "俺はオヤジの代からの実業家だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x8,
        (
            "それなりにやり手で通ってたが、\x01",
            "いまは支部長の仕事が忙しくてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x101,
        (
            "#0012Fああ、なるほど……\x01",
            "（やっぱり趣味人過ぎる人だ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x8,
        (
            "おっと……忘れる所だったぜ。\x01",
            "次の段位認定の条件も\x01",
            "伝えておかねえとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x8,
        (
            "ロイド団員、次の段位へ進むためには\x01",
            "『１２種類以上の魚』を釣らねばならん。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x8,
        (
            "それなりに工夫が必要だろうが、\x01",
            "頑張ってくれよな！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 11)
    Jump("loc_55D5")

    label("loc_5520")


    #C0270
    ChrTalk(
        0x8,
        (
            "ロイド団員の段位は\x01",
            "『道楽釣り師』だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x8,
        (
            "次の段位へ進むためには\x01",
            "『８種類以上の魚』を釣ることだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x8,
        (
            "フフ……釣果が上がったら見せに来るといい。\x01",
            "俺が段位を認定してやるぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55D5")

    Jump("loc_6C2E")

    label("loc_55DA")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AD8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_5A1C")
    Call(0, 10)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0273
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "セルダン支部長は\x01",
            "ロイドの釣り手帳をチェックした。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0274
    ChrTalk(
        0x8,
        (
            "おっ……ロイド団員、\x01",
            "こいつは素晴らしい釣果じゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x8,
        (
            "よくやったな。\x01",
            "今日から君は『二級釣師』だ！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(74, 0, 100, 0)

    #A0276
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "段位『二級釣師』に認められた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(17, 0, 100, 0)

    #A0277
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x33E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sound(17, 0, 100, 0)

    #A0278
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "褒賞として",
            scpstr(SCPSTR_CODE_ITEM, 0xA4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x33E, 1)
    AddItemNumber(0xA4, 1)
    OP_D0(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0279
    ChrTalk(
        0x8,
        (
            "やるなァ、ロイド団員。\x01",
            "『二級釣師』といえば\x01",
            "俺も取るのに随分苦労したぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x8,
        (
            "フハハ、思い余った俺は\x01",
            "山奥に篭って修行することにしてなァ……\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x8,
        (
            "大自然の中で感性を研ぎ澄まし、\x01",
            "ついにあのパールグラスを釣って\x01",
            "『二級釣師』になったというわけだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x8,
        (
            "……ロイド団員も苦労しただろうが、\x01",
            "それこそが釣師の勲章のようなモンさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x8,
        (
            "ロイド団員、今後も\x01",
            "活躍を期待しているぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x101,
        (
            "#0009Fはは、ありがとうございます。\x02\x03",

            "#0000Fところで……『二級』ということは\x01",
            "『一級』もあるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x8,
        (
            "無論だぜ。\x01",
            "次なる段位が『一級釣師』だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x8,
        (
            "『一級釣師』へ進むためには\x01",
            "『１６種類以上の魚』を釣らねばならん。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x8,
        (
            "いよいよロイド団員も\x01",
            "高段位保持者の仲間入りだな。\x01",
            "フハハ、俺も期待しているぜ！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 11)
    Jump("loc_5AD3")

    label("loc_5A1C")


    #C0288
    ChrTalk(
        0x8,
        (
            "ロイド団員の段位は\x01",
            "『生業釣り師』だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x8,
        (
            "次の段位へ進むためには\x01",
            "『１２種類以上の魚』を釣ることだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x8,
        (
            "フフ……釣果が上がったら見せに来るといい。\x01",
            "俺が段位を認定してやるぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5AD3")

    Jump("loc_6C2E")

    label("loc_5AD8")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_615F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6042")
    Call(0, 10)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0291
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "セルダン支部長は\x01",
            "ロイドの釣り手帳をチェックした。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0292
    ChrTalk(
        0x8,
        (
            "おっ……どうやら\x01",
            "また釣果をあげやがったようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x8,
        (
            "ロイド団員、素晴らしいぞ。\x01",
            "今日から君は『一級釣師』だ！\x01",
            "いやァ、よくやったじゃねえか！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(74, 0, 100, 0)

    #A0294
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "段位『一級釣師』に認められた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(17, 0, 100, 0)

    #A0295
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x33F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x33F, 1)
    OP_D0(0x3, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0296
    ChrTalk(
        0x8,
        (
            "ついにロイド団員も『一級釣師』か。\x01",
            "早いもんだなァ……\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x8,
        (
            "俺も５、６年前に取ったばかりでな、\x01",
            "このクロスベル支部の立ち上げを\x01",
            "決意したきっかけでもある。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x8,
        (
            "思い出すなァ、それを進言した時の\x01",
            "フィッシャー団長の涙ぐんだ瞳を……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0299
    ChrTalk(
        0x8,
        (
            "……まあいい。\x01",
            "ロイド団員、ついでだから\x01",
            "１つ教えておこう。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x8,
        (
            "一級釣師となった者は\x01",
            "この師団支部で『練り団子ＤＸ』が\x01",
            "購入できるようになるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x8,
        (
            "こいつは俺たちが開発した\x01",
            "万能のエサでな。\x01",
            "色んな魚が食いついて来るぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x101,
        (
            "#0005F新しい釣りエサみたいですね。\x02\x03",

            "#0008F……確かにエサを変えれば\x01",
            "釣れる魚も変わってくるし、\x01",
            "別の釣りスタイルも試せる、か……\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x8,
        "フハハ、さすがはロイド団員だ。\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x8,
        (
            "その通り、通いつめた釣り場でも\x01",
            "エサを変えれば世界が変わるぜ。\x01",
            "ガンガン試してみるといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x8,
        (
            "そして……次の段位認定の\x01",
            "条件も伝えておかねえとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x8,
        (
            "次はいよいよ、あの『特級釣師』だぜ。\x01",
            "『特級釣師』になるためには\x01",
            "『２３種類以上の魚』を釣らねばならん。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x8,
        (
            "こいつはかなり厳しいだろうが……\x01",
            "ロイド団員、ぜひ挑戦してくれたまえ！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 11)
    Jump("loc_615A")

    label("loc_6042")


    #C0308
    ChrTalk(
        0x8,
        (
            "ロイド団員の段位は『二級釣師』だな。\x01",
            "これだけでも大したものだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x8,
        (
            "次の段位へ進むためには\x01",
            "『１６種類以上の魚』を釣らねばならん。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x8,
        (
            "エサや釣り場を変えたりと\x01",
            "工夫を凝らさねばならんだろうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x8,
        (
            "フフ……釣果が上がったら見せに来るといい。\x01",
            "俺が段位を認定してやるぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_615A")

    Jump("loc_6C2E")

    label("loc_615F")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66EC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6597")
    Call(0, 10)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0312
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "セルダン支部長は\x01",
            "ロイドの釣り手帳をチェックした。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0313
    ChrTalk(
        0x8,
        (
            "おっ……！？\x01",
            "あの幻の魚、ノーブルカルプと\x01",
            "ゴルドサモーナも釣りやがったか！\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x8,
        (
            "ロイド団員、素晴らしいぞ。\x01",
            "今日から君は『特級釣師』だ！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(74, 0, 100, 0)

    #A0315
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "段位『特級釣師』に認められた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(17, 0, 100, 0)

    #A0316
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x340),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)

    #A0317
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x37),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x340, 1)
    AddItemNumber(0x37, 1)
    OP_D0(0x3, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0318
    ChrTalk(
        0x8,
        (
            "ロイド団員もついに\x01",
            "俺と同じ段位に上りつめやがったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x8,
        (
            "これからはゴルドサモーナの絶妙な\x01",
            "尾びれの角度について……\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x8,
        (
            "ノーブルカルプのヒキの脈動感について\x01",
            "語り合えるということだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x8,
        (
            "フハハ、特級釣師とは\x01",
            "釣りの全てを知り尽くしたもの。\x01",
            "俺も存分に語れる友が増えて嬉しいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x8,
        (
            "……ロイド団員、もう教えることはねえ。\x01",
            "これからは己の釣魚道を貫いていくがいい！\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        (
            "#0009Fははは……\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x8,
        (
            "だがまあ……クロスベルには\x01",
            "まだあの伝説のヌシ、\x01",
            "超大物が潜んでやがるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x8,
        (
            "今回君に渡した『アクアウィザード』は、\x01",
            "ヤツを釣り上げる可能性を秘めている……\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x8,
        (
            "ロイド団員、気が向いたら\x01",
            "伝説のヌシにも挑んでみてくれよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    ClearScenarioFlags(0x0, 0)
    Call(0, 11)
    Jump("loc_66E7")

    label("loc_6597")


    #C0327
    ChrTalk(
        0x8,
        (
            "ロイド団員の段位は『一級釣師』だな。\x01",
            "この短期間で、大したもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x8,
        (
            "だが、この上にはいよいよ\x01",
            "『特級釣師』の称号が待っている。\x01",
            "条件は『２３種類以上の魚』を釣ることだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x8,
        (
            "こいつはかなり難しいぜ……\x01",
            "あのノーブルカルプやゴルドサモーナも\x01",
            "釣らなきゃいけねえからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x8,
        (
            "……ロイド団員、釣果が上がったら\x01",
            "ここへ見せに来るといい！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_66E7")

    Jump("loc_6C2E")

    label("loc_66EC")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6C2E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6B2A")
    Call(0, 10)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0331
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "セルダン支部長は\x01",
            "ロイドの釣り手帳をチェックした。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0332
    ChrTalk(
        0x8,
        (
            "なあっ……！？\x01",
            "ロイド団員、あの伝説のヌシ\x01",
            "『サーペントヘッド』を釣ったのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x8,
        (
            "信じられねえ……\x01",
            "ついにやりやがったな、\x01",
            "ふははは……！\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        (
            "#0005Fや、やっぱり\x01",
            "あれがヌシだったんですか。\x02\x03",

            "#0003F凄いサイズだったから\x01",
            "驚いてはいたんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x8,
        (
            "ヤツこそが、俺たち\x01",
            "クロスベル支部の面々が\x01",
            "長年追っていた相手だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x8,
        "そいつを釣っちまうとは……\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x8,
        (
            "よしっ、君には\x01",
            "特別な称号を与えようじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x8,
        (
            "その名も『釣聖』……\x01",
            "一支部につき１名のみが認められる\x01",
            "伝説の称号だぜ！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(74, 0, 100, 0)

    #A0339
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "称号『釣聖』に認められた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(17, 0, 100, 0)

    #A0340
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x60),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x60, 1)
    OP_D0(0x3, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0341
    ChrTalk(
        0x8,
        (
            "まさかこの俺すら抜いて\x01",
            "釣聖になっちまうとはなァ……\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x8,
        (
            "これからもよろしく頼むぜ、\x01",
            "《クロスベルの釣聖》！\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x101,
        (
            "#0012Fうっ……恥ずかしいんですが。\x02\x03",

            "#0000Fまあ色々お世話にもなりましたし。\x01",
            "こちらこそ、今後も\x01",
            "よろしくご指導願います。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x8,
        (
            "ほう、ロイド団員は\x01",
            "中々謙虚だな……\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x8,
        (
            "ふはは、さすがだぜ！\x01",
            "ふはははは……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    ClearScenarioFlags(0x0, 0)
    Call(0, 11)
    Jump("loc_6C2E")

    label("loc_6B2A")


    #C0346
    ChrTalk(
        0x8,
        "ロイド団員の段位は『特級釣師』だな。\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x8,
        (
            "釣公師団のクロスベル支部じゃ、\x01",
            "これ以上の段位認定者は出ていない。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x8,
        (
            "だがまァ、ロイド団員なら\x01",
            "さらなる大物を釣るかもしれねえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x8,
        (
            "ふはは、もしそんな事があれば\x01",
            "ぜひ見せに来てくれ。\x01",
            "俺も拝んでみたいもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C2E")

    Return()

    # Function_12_48DB end

    def Function_13_6C2F(): pass

    label("Function_13_6C2F")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C54")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C54")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C6F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C6F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C8A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C8A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CA5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6CA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CC0")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6CC0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CDB")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6CDB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6CF6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6CF6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D11")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D2C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D47")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D47")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D62")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D62")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D7D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6D98")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D98")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DB3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6DB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DCE")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6DCE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6DE9")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6DE9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E04")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6E04")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E1F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6E1F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E3A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6E3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E55")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6E55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E70")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6E70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6E8B")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6E8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6EA6")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6EA6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6EC1")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6EC1")

    Return()

    # Function_13_6C2F end

    def Function_14_6EC2(): pass

    label("Function_14_6EC2")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0350
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に『お手軽お魚料理』という本がある。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_END)), "loc_6F86")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F86")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0351
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピが書かれていた。\x02",
        )
    )

    CloseMessageWindow()

    #A0352
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピを覚えた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_B0(0x8)

    label("loc_6F86")

    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_14_6EC2 end

    SaveToFile()

Try(main)
