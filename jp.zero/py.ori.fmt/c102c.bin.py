from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c102c.bin",                # FileName
        "c102c",                    # MapName
        "c102c",                    # Location
        0x0014,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 20, 0, 1, 0, 2],
    )

    BuildStringList((
        "c102c",                  # 0
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
    DeclNpc(-519,    0,       43310,   90,   389,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(7230,    0,       6780,    0,    389,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)

    DeclActor(6580,    0,       7980,    1500,    7230,    1500,    9070,    0x007E, 0,  3,  0x0000)
    DeclActor(-3170,   0,       51750,   1200,    -2860,   1500,    52600,   0x007C, 0,  9,  0x0000)
    DeclActor(470,     0,       43660,   1200,    470,     1500,    43360,   0x007C, 0,  15, 0x0000)

    ScpFunction((
        "Function_0_1A0",          # 00, 0
        "Function_1_258",          # 01, 1
        "Function_2_2D9",          # 02, 2
        "Function_3_316",          # 03, 3
        "Function_4_31A",          # 04, 4
        "Function_5_E91",          # 05, 5
        "Function_6_1835",         # 06, 6
        "Function_7_1A8A",         # 07, 7
        "Function_8_1C4F",         # 08, 8
        "Function_9_2819",         # 09, 9
        "Function_10_325C",        # 0A, 10
        "Function_11_3278",        # 0B, 11
        "Function_12_3445",        # 0C, 12
        "Function_13_34EF",        # 0D, 13
        "Function_14_5841",        # 0E, 14
        "Function_15_5AD4",        # 0F, 15
    ))


    def Function_0_1A0(): pass

    label("Function_0_1A0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1E0"),
        (1, "loc_1EC"),
        (2, "loc_1F8"),
        (3, "loc_204"),
        (4, "loc_210"),
        (5, "loc_21C"),
        (6, "loc_228"),
        (SWITCH_DEFAULT, "loc_234"),
    )


    label("loc_1E0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_1EC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_1F8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_204")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_210")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_21C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_228")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_234")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_240")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_257")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_240")

    label("loc_257")

    Return()

    # Function_0_1A0 end

    def Function_1_258(): pass

    label("Function_1_258")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_26B")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_2BF")

    label("loc_26B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_279")
    Jump("loc_2BF")

    label("loc_279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_287")
    Jump("loc_2BF")

    label("loc_287")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_295")
    Jump("loc_2BF")

    label("loc_295")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_2AC")
    SetChrFlags(0x8, 0x80)
    Jump("loc_2BF")

    label("loc_2AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2BF")
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xA, 0x80)

    label("loc_2BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D8")
    Event(0, 8)

    label("loc_2D8")

    Return()

    # Function_1_258 end

    def Function_2_2D9(): pass

    label("Function_2_2D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x16, 0x1, 0x0)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EF")
    OP_65(0x0, 0x1)

    label("loc_2EF")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_315")
    OP_66(0x1, 0x1)

    label("loc_315")

    Return()

    # Function_2_2D9 end

    def Function_3_316(): pass

    label("Function_3_316")

    Call(0, 4)
    Return()

    # Function_3_316 end

    def Function_4_31A(): pass

    label("Function_4_31A")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_C29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_461")

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

    label("loc_461")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_7D3")

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

    label("loc_7D3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C29")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x3, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_915")

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
    Jump("loc_A46")

    label("loc_915")


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

    label("loc_A46")


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

    label("loc_C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 1)), scpexpr(EXPR_END)), "loc_E83")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E7E")
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFD")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CA8")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_CA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC8")
    OP_AF(0x37)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CF8")

    label("loc_CC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CDC")
    Jump("loc_CF8")

    label("loc_CDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_CF8")

    Jump("loc_E79")

    label("loc_CFD")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DED")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D5F")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_D5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D83")
    Call(0, 14)
    Call(0, 13)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DE8")

    label("loc_D83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DB8")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DA7")
    OP_AF(0x36)
    Jump("loc_DA9")

    label("loc_DA7")

    OP_AF(0x37)

    label("loc_DA9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DE8")

    label("loc_DB8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DCC")
    Jump("loc_DE8")

    label("loc_DCC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_DE8")

    Jump("loc_E79")

    label("loc_DED")


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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E49")
    Call(0, 14)
    Call(0, 13)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E79")

    label("loc_E49")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E5D")
    Jump("loc_E79")

    label("loc_E5D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E79")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 5)

    label("loc_E79")

    Jump("loc_C3C")

    label("loc_E7E")

    Jump("loc_E86")

    label("loc_E83")

    Call(0, 5)

    label("loc_E86")

    TalkEnd(0x8)
    OP_93(0x8, 0xB4, 0x0)
    Return()

    # Function_4_31A end

    def Function_5_E91(): pass

    label("Function_5_E91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_12D1")
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF5")

    #C0029
    ChrTalk(
        0x8,
        "ロイド団員はこんな話を知っているか？\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "クロスベルには、伝説のヌシ\x01",
            "『サーペントヘッド』って奴がいるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "エルム湖を根城にしている\x01",
            "それはもう凶暴な奴でな、\x01",
            "昔は漁師にも恐れられていたらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "だが、奴はここ十数年\x01",
            "まったく目撃されてねえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "もしこいつを釣り上げられたら\x01",
            "勲章モノなんだがなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_10B1")

    label("loc_FF5")


    #C0034
    ChrTalk(
        0x8,
        (
            "『サーペントヘッド』はまさに\x01",
            "ヌシの中のヌシ……\x01",
            "奴を釣り上げるのは俺たち釣公師団の夢だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "ここ十数年は目撃されてねえが、\x01",
            "『特級釣師』になったお前さんなら\x01",
            "可能性はあるかもなァ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B1")

    Jump("loc_12CC")

    label("loc_10B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_124C")

    #C0036
    ChrTalk(
        0x8,
        (
            "さすがロイド団員だ、\x01",
            "《釣聖》になっても謙虚だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "ふはは、気に入ったぜ！\x01",
            "今夜あたり夜釣りにいかねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "うちの支部は親睦会を兼ねて\x01",
            "よく行くんだよなァ、夜釣り！\x02",
        )
    )

    CloseMessageWindow()

    #C0039
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

    #C0040
    ChrTalk(
        0x8,
        "ふははは、断り方まで謙虚だな！\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "よし、都合のいい日に声を掛けてくれ。\x01",
            "祝いを兼ねて釣り大会と行こうじゃねえか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12CC")

    label("loc_124C")


    #C0042
    ChrTalk(
        0x8,
        (
            "ロイド団員の\x01",
            "《釣聖》認定祝いをしねえとなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "サーペントヘッドを釣り上げた武勇伝も\x01",
            "ゆっくり聞かせてくれよ、ふははは！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12CC")

    Jump("loc_1834")

    label("loc_12D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_134F")

    #C0044
    ChrTalk(
        0x8,
        (
            "さて、今日は\x01",
            "俺も釣りに出かけるとするか。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "市内は騒がしくなりそうだ。\x01",
            "マインツ辺りに行ってみるかなァ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1834")

    label("loc_134F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1494")

    #C0046
    ChrTalk(
        0x8,
        (
            "クロスベルのどこかには\x01",
            "ヌシと呼ばれる超大物が\x01",
            "潜んでいると言われているが……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "それ以外にも、エレキイールや\x01",
            "デモンタイタンといった\x01",
            "かなりの大型魚がいるんだ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1450")

    #C0048
    ChrTalk(
        0x8,
        (
            "……ロイド団員、興味があれば\x01",
            "ぜひ挑戦してみてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_148F")

    label("loc_1450")


    #C0049
    ChrTalk(
        0x8,
        (
            "……ロイド団員、興味があれば\x01",
            "また挑戦してみてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_148F")

    Jump("loc_1834")

    label("loc_1494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_15DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1555")

    #C0050
    ChrTalk(
        0x8,
        (
            "釣公師団の団長は\x01",
            "フィッシャー男爵というお方なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "記念祭に合わせて\x01",
            "お呼びしたかったんだが、\x01",
            "日程が取れなくてな……\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        (
            "あの方も今は\x01",
            "中々お忙しいんだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15D8")

    label("loc_1555")


    #C0053
    ChrTalk(
        0x8,
        (
            "フィッシャー男爵は今\x01",
            "各国に釣公師団支部を作るため\x01",
            "飛び回っておられるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x8,
        (
            "中々お忙しくて\x01",
            "お呼びできなかったんだよなァ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15D8")

    Jump("loc_1834")

    label("loc_15DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_16CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1647")

    #C0055
    ChrTalk(
        0x8,
        "昨日の釣果は見事だった！\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "ロイド団員、この調子で\x01",
            "頑張ってくれたまえ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16C6")

    label("loc_1647")


    #C0057
    ChrTalk(
        0x8,
        (
            "記念祭だからと言って\x01",
            "釣りを怠けてちゃアいけねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "ロッド捌きは\x01",
            "放っておくと腕が落ちる。\x01",
            "１日１釣は嗜むことだなァ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16C6")

    Jump("loc_1834")

    label("loc_16CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1834")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17CE")

    #C0059
    ChrTalk(
        0x8,
        (
            "……ロイド団員、\x01",
            "警察の仕事は忙しいのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#0000Fええ、それはもう……\x01",
            "記念祭の真っ只中ですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "そうかい……\x01",
            "いや、妙な事を聞いちまったなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "気にしねえで本職に励んでくれ。\x01",
            "合間に釣果を上げることも忘れずにな！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1834")

    label("loc_17CE")


    #C0063
    ChrTalk(
        0x8,
        (
            "ロイド団員、俺たちのことは気にせず\x01",
            "本職に励んでくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "合間に釣果を上げることも\x01",
            "忘れずにな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1834")

    Return()

    # Function_5_E91 end

    def Function_6_1835(): pass

    label("Function_6_1835")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1A86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A1B")
    OP_4B(0x8, 0xFF)

    #C0065
    ChrTalk(
        0xFE,
        (
            "ええ、遊撃士のエステルさんにも\x01",
            "お声を掛けてみたんですけどねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "やはり本職持ちの団員は\x01",
            "皆忙しいみてえだなァ……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "本職を妨げぬよう楽しむのが\x01",
            "俺たちの流儀だ、\x01",
            "口惜しいが連中は誘わねえでおくか。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "うふふ、でもあの方は\x01",
            "ぜひとも参加したいと仰ってましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        "本職の方はお休みを取るから、とか……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0070
    ChrTalk(
        0x8,
        (
            "ほほう、そいつは楽しみだ。\x01",
            "久々に盛り上がりそうじゃねえか！\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        (
            "#0005F（？？？\x01",
            "  ……何の話だろう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A86")

    label("loc_1A1B")


    #C0072
    ChrTalk(
        0xFE,
        "うふふ、楽しみですねえ。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "先月から温めてきた一大イベント……\x01",
            "皆さんと盛り上げていきましょうねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A86")

    TalkEnd(0xFE)
    Return()

    # Function_6_1835 end

    def Function_7_1A8A(): pass

    label("Function_7_1A8A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1C4B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x22, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B30")

    #C0074
    ChrTalk(
        0xFE,
        (
            "ペーターさんとあの特級釣師の人、\x01",
            "ミシュラムに行ってるらしいっすよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "……ちぇ～、\x01",
            "もう一度釣り勝負を\x01",
            "仕掛ける予定だったのに。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C4B")

    label("loc_1B30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BD1")

    #C0076
    ChrTalk(
        0xFE,
        (
            "何だか知らないっすけど\x01",
            "警察も大変っすねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "あ、オレの事は\x01",
            "気にしなくていいんで。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "ついでだし、この足で\x01",
            "釣りに出ちまおっかなー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1C4B")

    label("loc_1BD1")


    #C0079
    ChrTalk(
        0xFE,
        (
            "ペーターさんとあの特級釣師の人、\x01",
            "ミシュラムに行ってるらしいっすよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "オレも暇なんで\x01",
            "どこか出かけちまおっかなー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C4B")

    TalkEnd(0xFE)
    Return()

    # Function_7_1A8A end

    def Function_8_1C4F(): pass

    label("Function_8_1C4F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(1500, 1400, 700, 0)
    MoveCamera(45, 22, 0, 0)
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
    SetChrPos(0x9, 11910, 1670, 7920, 180)
    ClearChrFlags(0x9, 0x80)
    OP_4B(0x9, 0xFF)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(2100, 1400, 1510, 3000)
    MoveCamera(45, 22, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(22440, 3000)

    def lambda_1D50():
        OP_95(0xFE, 1310, 0, 2330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D50)

    def lambda_1D6A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D6A)
    Sleep(300)

    def lambda_1D7E():
        OP_95(0xFE, 2310, 0, 1130, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1D7E)

    def lambda_1D98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1D98)
    Sleep(300)

    def lambda_1DAC():
        OP_95(0xFE, 110, 0, 1130, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1DAC)

    def lambda_1DC6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1DC6)
    Sleep(300)

    def lambda_1DDA():
        OP_95(0xFE, 1310, 0, 130, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1DDA)

    def lambda_1DF4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1DF4)
    Sleep(3000)

    #C0081
    ChrTalk(
        0x101,
        "#5P#0000Fごめんくださーい……\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x12C)
    Sleep(300)
    OP_93(0x101, 0x0, 0x12C)
    Sleep(300)
    OP_93(0x101, 0x2D, 0x12C)

    #C0082
    ChrTalk(
        0x101,
        (
            "#5P#0003F……誰もいないみたいだ。\x02\x03",

            "#0001Fヨアヒム先生の手がかり、\x01",
            "ここなら見つけられそうな\x01",
            "気がしてたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#12P#0300Fもう例の釣り大会とやらに\x01",
            "行っちまったんじゃねぇか？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x102,
        (
            "#11P#0106F……だとすると、手がかりが\x01",
            "なくなってしまうわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x103,
        (
            "#6P#0200F……待ってください。\x01",
            "建物内にまだ誰かいるようです。\x02",
        )
    )

    CloseMessageWindow()

    #N0086
    NpcTalk(
        0x9,
        "青年の声",
        "……ち、ちこくっす～！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1FF5():

        label("loc_1FF5")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1FF5")

    QueueWorkItem2(0x0, 1, lambda_1FF5)

    def lambda_2007():

        label("loc_2007")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2007")

    QueueWorkItem2(0x1, 1, lambda_2007)

    def lambda_2019():

        label("loc_2019")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_2019")

    QueueWorkItem2(0x2, 1, lambda_2019)

    def lambda_202B():

        label("loc_202B")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_202B")

    QueueWorkItem2(0x3, 1, lambda_202B)
    Fade(500)
    OP_68(9180, 1400, 3560, 0)
    OP_0D()

    def lambda_2054():
        OP_95(0xFE, 11480, 0, 3930, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2054)
    Sleep(100)
    OP_68(2630, 1400, 2250, 2700)
    WaitChrThread(0x9, 1)

    def lambda_2086():
        OP_95(0xFE, 3740, 0, 3740, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2086)
    WaitChrThread(0x9, 1)
    OP_93(0x9, 0xE1, 0x1F4)
    Sleep(300)

    #C0087
    ChrTalk(
        0x9,
        (
            "#11P……あれ？\x01",
            "警察のロイドさんじゃないすか。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        (
            "#6P#0000Fコパンさん、丁度よかった。\x01",
            "ちょっと聞きたいことが\x01",
            "あるんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "#11Pだめっす。\x01",
            "オレは急いでるんす。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "#11P今からウルスラ間道の中州で\x01",
            "開かれてる『フィッシャー杯』に\x01",
            "行かなければならないんす。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        "#12P#0105Fフィッシャー杯……？\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x104,
        "#12P#0305F例の釣りの大会ってヤツか？\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "#11Pご存知だったっすか。\x01",
            "やっぱ釣り人なら外せないっすよねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "#11Pフィッシャー杯とは、\x01",
            "釣公師団の名誉会長である\x01",
            "フィッシャー氏の功績を讃えて……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x9,
        (
            "#11P……って、こんなこと\x01",
            "してるヒマはないっす！\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "#11P早くしないと、先輩たちに\x01",
            "いいポイントをとられちゃうっす～！\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#6P#0011Fひ、一つ！　もう一つだけ！\x02\x03",

            "#0000F釣り大会に向かった人に、\x01",
            "青い髪で眼鏡をかけた\x01",
            "白衣の男性はいませんでしたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        "#11Pんんんん？\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x9,
        (
            "#11Pもしかして、\x01",
            "ヨアヒムさんのことっすか？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        "#11Pたしか今日は来ていたはずっすよ。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x104,
        "#12P#0301F……ビンゴだな。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        "#6P#0001F……ああ。\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "#11P……もしかして、皆さんも\x01",
            "大会に参加するっすか？\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        "#11Pだったら、これをあげるっす。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0105
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x34),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x34, 1)

    #C0106
    ChrTalk(
        0x101,
        "#6P#0005Fえ！　こ、これは……？\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        (
            "#12P#11Pフィッシャー杯の参加者には\x01",
            "無料で差し上げてるっす。\x01",
            "いわば参加賞っすね。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#6P#0006F（まだ参加するなんて一言も……\x01",
            "  いいのかなぁ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        (
            "#11P……っとぉ、遅刻していたのを\x01",
            "忘れていたっす！\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x9,
        (
            "#11Pオレは急ぐんで、これで！\x01",
            "皆さんも急ぐっすよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(940, 1400, 910, 1000)
    OP_95(0x9, -1250, 0, -1260, 7000, 0x0)

    def lambda_263C():
        OP_95(0xFE, -3050, 0, -3060, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_263C)

    def lambda_2656():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2656)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    SetChrFlags(0x9, 0x80)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    Sleep(500)

    #C0111
    ChrTalk(
        0x102,
        (
            "#11P#0105F……なんだかせわしなく\x01",
            "出て行っちゃったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x101,
        (
            "#5P#0003Fとにかく……\x02\x03",

            "#0000Fヨアヒム先生は\x01",
            "どうやらウルスラ間道の\x01",
            "中州に向かったらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x103,
        "#6P#0200F早速急ぐとするっす。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x104,
        "#12P#0309F……言葉が移ってるぞ、ティオすけ。\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x103,
        "#6P#0203F…………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 1210, 0, 1210, 45)
    SetChrPos(0x1, 1210, 0, 1210, 45)
    SetChrPos(0x2, 1210, 0, 1210, 45)
    SetChrPos(0x3, 1210, 0, 1210, 45)
    OP_4C(0x9, 0xFF)
    OP_49()
    OP_68(1210, 1400, 1210, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    OP_29(0x16, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_8_1C4F end

    def Function_9_2819(): pass

    label("Function_9_2819")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x9, 0xFF)
    OP_68(-2830, 1100, 51870, 0)
    MoveCamera(41, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18470, 0)
    SetChrPos(0x101, -3450, 0, 51000, 0)
    SetChrPos(0x102, -3450, 0, 49640, 0)
    SetChrPos(0x103, -2510, 0, 51000, 0)
    SetChrPos(0x104, -2510, 0, 49640, 0)
    SetChrPos(0x9, -1490, 0, 45300, 315)
    SetChrFlags(0x9, 0x40)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis030.itp")
    LoadEffect(0x7, "event\\eva00_00.eff")
    FadeToBright(1000, 0)
    OP_0D()

    #C0116
    ChrTalk(
        0x102,
        "#6P#0105Fこれは……大きな水槽ね。\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x103,
        "#11P#0202F魚が平和そうに泳いでいます。\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#6P#0003Fそういえば、魚のうろこは\x01",
            "光を反射して輝くよな。\x02\x03",

            "#0000F『暖かき水の小楽園』……\x01",
            "もしかしてここの事かな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Sound(860, 0, 100, 0)
    PlayEffect(0x7, 0x7, 0xFF, 0x0, -3230, 1000, 53150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    StopEffect(0x7, 0x2)
    Sleep(500)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0119
    ChrTalk(
        0x101,
        "#6P#0005Fあっ……\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x104,
        "#12P#0305F中に何か落ちてるぞ！？\x02",
    )

    CloseMessageWindow()

    #N0121
    NpcTalk(
        0x9,
        "青年の声",
        "あの、どうかしたっすか？\x02",
    )

    CloseMessageWindow()
    OP_68(-3020, 1400, 49800, 1800)
    BeginChrThread(0x9, 1, 0, 10)
    Sleep(300)

    def lambda_2AF6():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_2AF6)

    def lambda_2B03():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2B03)

    def lambda_2B10():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2B10)

    def lambda_2B1D():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2B1D)
    WaitChrThread(0x9, 1)

    #C0122
    ChrTalk(
        0x102,
        (
            "#5P#0100Fすみません、お邪魔して。\x01",
            "話せば長くなるんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        (
            "#5P#0000Fこの水槽の中に\x01",
            "落ちてるカード、\x01",
            "何とか取り出せませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x9,
        "#12Pへ……？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_63(0x9, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0125
    ChrTalk(
        0x9,
        "#12Pそれは大変と思うっす。\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x9,
        (
            "#12Pなんとか釣り針をひっかけて\x01",
            "釣り上げるしかないっすねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x9,
        "#12P水槽の中に入るわけにもいかないんで。\x02",
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

    #C0128
    ChrTalk(
        0x103,
        "#11P#0200Fやはりそうですか……\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x104,
        "#11P#0306Fそりゃ、かなりのスキルが必要だな……\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x9,
        (
            "#12Pうーん、仕方ないっすねー。\x01",
            "オレが釣り上げてやるっすよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-3150, 1200, 49570, 0)
    MoveCamera(41, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18470, 0)
    SetChrPos(0x101, -3080, 0, 49720, 0)
    SetChrPos(0x102, -3880, 0, 47530, 0)
    SetChrPos(0x103, -2670, 0, 48590, 0)
    SetChrPos(0x104, -2670, 0, 47530, 0)
    SetChrPos(0x9, -3010, 0, 51090, 180)
    Sleep(1200)
    Sound(11, 0, 100, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0131
    ChrTalk(
        0x9,
        "#5P釣れたっす。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        (
            "#6P#0012Fさ、さすが釣公師団……\x02\x03",

            "#0000F手間をかけさせてすみません。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x9,
        (
            "#5P別にいいっすよ。\x01",
            "こんなもん、朝飯前っすから。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x9,
        (
            "#5Pそれより……何なんすか\x01",
            "このカードは。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#6P#0006Fえ、えーっと……\x01",
            "諸事情ありまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        (
            "#5P……ふーん？\x01",
            "まぁ、いいっすけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x104,
        (
            "#6P#0301Fおうロイド、\x01",
            "さっそく見てみようぜ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2F68():

        label("loc_2F68")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_2F68")

    QueueWorkItem2(0x102, 1, lambda_2F68)

    def lambda_2F7A():

        label("loc_2F7A")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_2F7A")

    QueueWorkItem2(0x104, 1, lambda_2F7A)

    def lambda_2F8C():

        label("loc_2F8C")

        TurnDirection(0xFE, 0x101, 300)
        Yield()
        Jump("loc_2F8C")

    QueueWorkItem2(0x103, 1, lambda_2F8C)
    OP_95(0x101, -3920, 0, 48810, 1000, 0x0)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x103, 0x1)

    def lambda_2FBE():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FBE)

    def lambda_2FCB():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2FCB)

    def lambda_2FD8():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2FD8)

    def lambda_2FE5():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2FE5)
    Sleep(300)

    #C0138
    ChrTalk(
        0x102,
        "#6P#0105Fええと、なになに……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    Sleep(600)
    SetMessageWindowPos(-1, 90, -1, 3)
    SetChrName("")

    #A0139
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "９－７－１４－９－１９\x01",
            " 粗野なる調べ響かせる \x01",
            "　　中央の箱を見よ　　\x02",
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

    #C0140
    ChrTalk(
        0x104,
        (
            "#12P#0301Fイミが判らん。\x01",
            "先頭の数字はどういう事だ？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x103,
        (
            "#11P#0200F暗号の一種かもしれませんね。\x02\x03",

            "#0203Fたとえば……数字と見せかけて\x01",
            "文字を指しているとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        (
            "#6P#0003Fそうだな……\x01",
            "色々考えながら探してみよう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -2910, 0, 49460, 0)
    SetChrPos(0x9, -520, 0, 43310, 90)
    ClearChrFlags(0x9, 0x40)
    OP_4C(0x9, 0xFF)
    OP_CA(0x1, 0xFF, 0x0)
    OP_65(0x1, 0x1)
    OP_29(0x22, 0x1, 0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_9_2819 end

    def Function_10_325C(): pass

    label("Function_10_325C")

    OP_95(0x9, -3370, 0, 47470, 1500, 0x0)
    OP_93(0x9, 0x0, 0x1F4)
    Return()

    # Function_10_325C end

    def Function_11_3278(): pass

    label("Function_11_3278")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(6970, 1400, 7010, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(19720, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32F9")
    SetChrPos(0x101, 6200, 0, 6250, 0)
    SetChrPos(0xEF, 7400, 0, 6250, 0)
    SetChrPos(0x153, 6200, 0, 5050, 0)
    Jump("loc_3421")

    label("loc_32F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_336B")
    SetChrPos(0x101, 6200, 0, 6250, 0)
    SetChrPos(0x102, 7400, 0, 6250, 0)
    SetChrPos(0x103, 6200, 0, 5050, 0)
    SetChrPos(0x104, 7400, 0, 5050, 0)
    SetChrPos(0x109, 6200, 0, 3850, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_3421")

    label("loc_336B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33DD")
    SetChrPos(0x101, 6200, 0, 6250, 0)
    SetChrPos(0x102, 7400, 0, 6250, 0)
    SetChrPos(0x103, 6200, 0, 5050, 0)
    SetChrPos(0x104, 7400, 0, 5050, 0)
    SetChrPos(0x10A, 6200, 0, 3850, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_3421")

    label("loc_33DD")

    SetChrPos(0x101, 6200, 0, 6250, 0)
    SetChrPos(0x102, 7400, 0, 6250, 0)
    SetChrPos(0x103, 6200, 0, 5050, 0)
    SetChrPos(0x104, 7400, 0, 5050, 0)

    label("loc_3421")

    OP_93(0x8, 0xB4, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    FadeToBright(500, 0)
    OP_0D()
    Return()

    # Function_11_3278 end

    def Function_12_3445(): pass

    label("Function_12_3445")

    FadeToDark(500, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3463")
    Jump("loc_349D")

    label("loc_3463")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3480")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_349D")

    label("loc_3480")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_349D")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_349D")

    label("loc_349D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34B0")
    Jump("loc_34CD")

    label("loc_34B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34C3")
    Jump("loc_34CD")

    label("loc_34C3")

    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)

    label("loc_34CD")

    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 5410, 0, 6840, 45)
    TurnDirection(0x8, 0x0, 0)
    EventEnd(0x5)
    TalkBegin(0x8)
    Return()

    # Function_12_3445 end

    def Function_13_34EF(): pass

    label("Function_13_34EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_37FC")

    #C0143
    ChrTalk(
        0x8,
        (
            "釣公師団は、釣り文化の普及や技術向上のため\x01",
            "『段位認定試験』ってのを実施している。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x8,
        (
            "君の釣り技術を認定して\x01",
            "さまざまな称号や褒賞品などを進呈するぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x8,
        (
            "ふむ、ロイド団員は入団したばかりだから\x01",
            "現在の段位は『駆け出し釣り師』だな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_36EC")

    #C0146
    ChrTalk(
        0x8,
        (
            "次の段位へ進む条件は\x01",
            "『４種類以上の魚』を釣ることだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x8,
        (
            "釣り手帳を見れば\x01",
            "釣った事のある魚が記されているだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x8,
        "４種類以上釣れたら、ぜひ報告に来てくれ。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x8,
        (
            "フハハ、釣りは楽しいぜ？\x01",
            "工夫を凝らして挑戦してみてくれよな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37F4")

    label("loc_36EC")


    #C0150
    ChrTalk(
        0x8,
        (
            "次の段位へ進む条件は\x01",
            "『４種類以上の魚』を釣ることだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x8,
        (
            "……と思ったら、なんだ。\x01",
            "もう４種類以上の魚を釣っているのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x8,
        (
            "まあいい、釣り手帳は\x01",
            "きちんとチェックしたいからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x8,
        (
            "もう一度俺に話しかけてくれ。\x01",
            "フハハ、次の段位を認定してやろうじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37F4")

    SetScenarioFlags(0x69, 6)
    Jump("loc_5840")

    label("loc_37FC")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C4B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_3B48")
    Call(0, 11)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0154
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

    #C0155
    ChrTalk(
        0x8,
        (
            "おっ……ロイド団員、\x01",
            "中々目覚しい釣果じゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
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

    #A0157
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

    #A0158
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

    #C0159
    ChrTalk(
        0x8,
        (
            "こいつァ俺が愛用していた\x01",
            "麦わら帽子でな。\x01",
            "釣りにはもってこいだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x8,
        (
            "ロイド団員、こいつを身につけて\x01",
            "今後も釣りに励んでくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x101,
        (
            "#0002F釣りの定番アイテムですよね。\x01",
            "ありがたく受け取っておきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x8,
        (
            "うむ、『道楽釣り師』といえば\x01",
            "まだまだだが、段位が上がるにつれ\x01",
            "豪華褒章品なども用意しているぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x8,
        (
            "フフ……ついでに次の段位認定の\x01",
            "条件も伝えておくか。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x8,
        (
            "次の段位へ進むためには\x01",
            "『８種類以上の魚』を釣らねばならん。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x8,
        "工夫を凝らして挑戦してくれたまえ。\x02",
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_3C46")

    label("loc_3B48")


    #C0166
    ChrTalk(
        0x8,
        (
            "ロイド団員の現在の段位は\x01",
            "『駆け出し釣り師』だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x8,
        (
            "次の段位へ進むためには\x01",
            "『４種類以上の魚』を釣ることだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x8,
        (
            "釣り手帳を見れば\x01",
            "何種類釣ったか一目で確認できるはずだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x8,
        (
            "フフ……釣果が上がったら見せに来るといい。\x01",
            "俺が段位を認定してやるぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C46")

    Jump("loc_5840")

    label("loc_3C4B")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41EE")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4134")
    Call(0, 11)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0170
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

    #C0171
    ChrTalk(
        0x8,
        (
            "おっ……ロイド団員、\x01",
            "中々素晴らしい釣果じゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
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

    #A0173
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

    #A0174
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

    #C0175
    ChrTalk(
        0x8,
        (
            "思い出すなァ、俺が\x01",
            "『生業釣り師』になった日の事を……\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x8,
        (
            "元々釣り好きだった俺は、\x01",
            "仕事で立ち寄ったリベール王国で\x01",
            "《釣公師団》を名乗る男と出会ってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x8,
        (
            "フハハ、それが言わずと知れた\x01",
            "あの伝説的釣師フィッシャー団長さ！\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x8,
        (
            "まァ色々あって、団長直々に\x01",
            "『生業釣り師』の段位を授かる事になった。\x01",
            "懐かしいなァ……\x02",
        )
    )

    CloseMessageWindow()

    #C0179
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

    #C0180
    ChrTalk(
        0x8,
        (
            "フハハ、いやいや。\x01",
            "俺はオヤジの代からの実業家だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x8,
        (
            "それなりにやり手で通ってたが、\x01",
            "いまは支部長の仕事が忙しくてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x101,
        (
            "#0012Fああ、なるほど……\x01",
            "（やっぱり趣味人過ぎる人だ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x8,
        (
            "おっと……忘れる所だったぜ。\x01",
            "次の段位認定の条件も\x01",
            "伝えておかねえとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x8,
        (
            "ロイド団員、次の段位へ進むためには\x01",
            "『１２種類以上の魚』を釣らねばならん。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x8,
        (
            "それなりに工夫が必要だろうが、\x01",
            "頑張ってくれよな！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_41E9")

    label("loc_4134")


    #C0186
    ChrTalk(
        0x8,
        (
            "ロイド団員の段位は\x01",
            "『道楽釣り師』だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x8,
        (
            "次の段位へ進むためには\x01",
            "『８種類以上の魚』を釣ることだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x8,
        (
            "フフ……釣果が上がったら見せに来るといい。\x01",
            "俺が段位を認定してやるぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41E9")

    Jump("loc_5840")

    label("loc_41EE")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_46EC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4630")
    Call(0, 11)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0189
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

    #C0190
    ChrTalk(
        0x8,
        (
            "おっ……ロイド団員、\x01",
            "こいつは素晴らしい釣果じゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
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

    #A0192
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

    #A0193
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

    #A0194
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

    #C0195
    ChrTalk(
        0x8,
        (
            "やるなァ、ロイド団員。\x01",
            "『二級釣師』といえば\x01",
            "俺も取るのに随分苦労したぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x8,
        (
            "フハハ、思い余った俺は\x01",
            "山奥に篭って修行することにしてなァ……\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x8,
        (
            "大自然の中で感性を研ぎ澄まし、\x01",
            "ついにあのパールグラスを釣って\x01",
            "『二級釣師』になったというわけだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x8,
        (
            "……ロイド団員も苦労しただろうが、\x01",
            "それこそが釣師の勲章のようなモンさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x8,
        (
            "ロイド団員、今後も\x01",
            "活躍を期待しているぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        (
            "#0009Fはは、ありがとうございます。\x02\x03",

            "#0000Fところで……『二級』ということは\x01",
            "『一級』もあるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x8,
        (
            "無論だぜ。\x01",
            "次なる段位が『一級釣師』だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x8,
        (
            "『一級釣師』へ進むためには\x01",
            "『１６種類以上の魚』を釣らねばならん。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x8,
        (
            "いよいよロイド団員も\x01",
            "高段位保持者の仲間入りだな。\x01",
            "フハハ、俺も期待しているぜ！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_46E7")

    label("loc_4630")


    #C0204
    ChrTalk(
        0x8,
        (
            "ロイド団員の段位は\x01",
            "『生業釣り師』だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x8,
        (
            "次の段位へ進むためには\x01",
            "『１２種類以上の魚』を釣ることだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x8,
        (
            "フフ……釣果が上がったら見せに来るといい。\x01",
            "俺が段位を認定してやるぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46E7")

    Jump("loc_5840")

    label("loc_46EC")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D73")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_4C56")
    Call(0, 11)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0207
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

    #C0208
    ChrTalk(
        0x8,
        (
            "おっ……どうやら\x01",
            "また釣果をあげやがったようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
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

    #A0210
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

    #A0211
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

    #C0212
    ChrTalk(
        0x8,
        (
            "ついにロイド団員も『一級釣師』か。\x01",
            "早いもんだなァ……\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x8,
        (
            "俺も５、６年前に取ったばかりでな、\x01",
            "このクロスベル支部の立ち上げを\x01",
            "決意したきっかけでもある。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
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

    #C0215
    ChrTalk(
        0x8,
        (
            "……まあいい。\x01",
            "ロイド団員、ついでだから\x01",
            "１つ教えておこう。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x8,
        (
            "一級釣師となった者は\x01",
            "この師団支部で『練り団子ＤＸ』が\x01",
            "購入できるようになるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x8,
        (
            "こいつは俺たちが開発した\x01",
            "万能のエサでな。\x01",
            "色んな魚が食いついて来るぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
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

    #C0219
    ChrTalk(
        0x8,
        "フハハ、さすがはロイド団員だ。\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x8,
        (
            "その通り、通いつめた釣り場でも\x01",
            "エサを変えれば世界が変わるぜ。\x01",
            "ガンガン試してみるといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x8,
        (
            "そして……次の段位認定の\x01",
            "条件も伝えておかねえとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x8,
        (
            "次はいよいよ、あの『特級釣師』だぜ。\x01",
            "『特級釣師』になるためには\x01",
            "『２３種類以上の魚』を釣らねばならん。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x8,
        (
            "こいつはかなり厳しいだろうが……\x01",
            "ロイド団員、ぜひ挑戦してくれたまえ！\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_4D6E")

    label("loc_4C56")


    #C0224
    ChrTalk(
        0x8,
        (
            "ロイド団員の段位は『二級釣師』だな。\x01",
            "これだけでも大したものだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x8,
        (
            "次の段位へ進むためには\x01",
            "『１６種類以上の魚』を釣らねばならん。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x8,
        (
            "エサや釣り場を変えたりと\x01",
            "工夫を凝らさねばならんだろうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x8,
        (
            "フフ……釣果が上がったら見せに来るといい。\x01",
            "俺が段位を認定してやるぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D6E")

    Jump("loc_5840")

    label("loc_4D73")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52FE")
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_51A9")
    Call(0, 11)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0228
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

    #C0229
    ChrTalk(
        0x8,
        (
            "おっ……！？\x01",
            "あの幻の魚、ノーブルカルプと\x01",
            "ゴルドサモーナも釣りやがったか！\x02",
        )
    )

    CloseMessageWindow()

    #C0230
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

    #A0231
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

    #A0232
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

    #A0233
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

    #C0234
    ChrTalk(
        0x8,
        (
            "ロイド団員もついに\x01",
            "俺と同じ段位に上りつめやがったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x8,
        (
            "これからはゴルドサモーナの絶妙な\x01",
            "尾びれの角度について……\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x8,
        (
            "ノーブルカルプのヒキの脈動感について\x01",
            "語り合えるということだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x8,
        (
            "フハハ、特級釣師とは\x01",
            "釣りの全てを知り尽くしたもの。\x01",
            "俺も存分に語れる友が増えて嬉しいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x8,
        (
            "……ロイド団員、もう教えることはねえ。\x01",
            "これからは己の釣魚道を貫いていくがいい！\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x101,
        (
            "#0009Fははは……\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x8,
        (
            "だがまあ、クロスベルには\x01",
            "まだあの伝説のヌシ、\x01",
            "超大物が潜んでやがるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x8,
        (
            "今回君に渡した『アクアウィザード』は、\x01",
            "ヤツを釣り上げる可能性を秘めている……\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x8,
        (
            "ロイド団員、気が向いたら\x01",
            "伝説のヌシにも挑んでみてくれよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 0)
    Call(0, 12)
    Jump("loc_52F9")

    label("loc_51A9")


    #C0243
    ChrTalk(
        0x8,
        (
            "ロイド団員の段位は『一級釣師』だな。\x01",
            "この短期間で、大したもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x8,
        (
            "だが、この上にはいよいよ\x01",
            "『特級釣師』の称号が待っている。\x01",
            "条件は『２３種類以上の魚』を釣ることだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x8,
        (
            "こいつはかなり難しいぜ……\x01",
            "あのノーブルカルプやゴルドサモーナも\x01",
            "釣らなきゃいけねえからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x8,
        (
            "……ロイド団員、釣果が上がったら\x01",
            "ここへ見せに来るといい！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52F9")

    Jump("loc_5840")

    label("loc_52FE")

    Jc((scpexpr(EXPR_23, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5840")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_573C")
    Call(0, 11)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0247
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

    #C0248
    ChrTalk(
        0x8,
        (
            "なあっ……！？\x01",
            "ロイド団員、あの伝説のヌシ\x01",
            "『サーペントヘッド』を釣ったのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x8,
        (
            "信じられねえ……\x01",
            "ついにやりやがったな、\x01",
            "ふははは……！\x02",
        )
    )

    CloseMessageWindow()

    #C0250
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

    #C0251
    ChrTalk(
        0x8,
        (
            "ヤツこそが、俺たち\x01",
            "クロスベル支部の面々が\x01",
            "長年追っていた相手だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x8,
        "そいつを釣っちまうとは……\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x8,
        (
            "よしっ、君には\x01",
            "特別な称号を与えようじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
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

    #A0255
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

    #A0256
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

    #C0257
    ChrTalk(
        0x8,
        (
            "まさかこの俺すら抜いて\x01",
            "釣聖になっちまうとはなァ……\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x8,
        (
            "これからもよろしく頼むぜ、\x01",
            "《クロスベルの釣聖》！\x02",
        )
    )

    CloseMessageWindow()

    #C0259
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

    #C0260
    ChrTalk(
        0x8,
        (
            "ほう、ロイド団員は\x01",
            "中々謙虚だな……\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x8,
        (
            "ふはは、さすがだぜ！\x01",
            "ふはははは……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 0)
    Call(0, 12)
    Jump("loc_5840")

    label("loc_573C")


    #C0262
    ChrTalk(
        0x8,
        "ロイド団員の段位は『特級釣師』だな。\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x8,
        (
            "釣公師団のクロスベル支部じゃ、\x01",
            "これ以上の段位認定者は出ていない。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x8,
        (
            "だがまァ、ロイド団員なら\x01",
            "さらなる大物を釣るかもしれねえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x8,
        (
            "ふはは、もしそんな事があれば\x01",
            "ぜひ見せに来てくれ。\x01",
            "俺も拝んでみたいもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5840")

    Return()

    # Function_13_34EF end

    def Function_14_5841(): pass

    label("Function_14_5841")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5866")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5866")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5881")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5881")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_589C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_589C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58B7")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_58B7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58D2")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_58D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x5, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58ED")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_58ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x6, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5908")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5908")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5923")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5923")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x8, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_593E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_593E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5959")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5959")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xA, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5974")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5974")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_598F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_598F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xC, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_59AA")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_59AA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xD, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_59C5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_59C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xE, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_59E0")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_59E0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0xF, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_59FB")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_59FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x10, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A16")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5A16")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A31")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5A31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x12, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A4C")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5A4C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x13, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A67")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5A67")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x14, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A82")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5A82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A9D")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5A9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5AB8")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5AB8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x17, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5AD3")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_5AD3")

    Return()

    # Function_14_5841 end

    def Function_15_5AD4(): pass

    label("Function_15_5AD4")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)

    #A0266
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "本棚に『お手軽お魚料理』という本がある。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_END)), "loc_5B98")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_B0(0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B98")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0267
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "のレシピが書かれていた。\x02",
        )
    )

    CloseMessageWindow()

    #A0268
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

    label("loc_5B98")

    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    OP_0D()
    TalkEnd(0xFF)
    Return()

    # Function_15_5AD4 end

    SaveToFile()

Try(main)
