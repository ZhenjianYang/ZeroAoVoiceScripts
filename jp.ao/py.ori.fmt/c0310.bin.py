from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0310.bin",                # FileName
        "c0310",                    # MapName
        "c0310",                    # Location
        0x002B,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 43, 0, 4, 0, 5],
    )

    BuildStringList((
        "c0310",                  # 0
        "ヘルマー",               # 1
        "ジョアンナ",             # 2
    ))

    AddCharChip((
        "chr/ch25800.itc",                   # 00
        "chr/ch25700.itc",                   # 01
    ))

    DeclNpc(0,       4059,    7760,    180,  257,  0x0, 0,   0,   0,   0,   2,   0,   6,   255,  0)
    DeclNpc(-45349,  59,      3900,    360,  257,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)

    DeclActor(-40820,  0,       40910,   1500,    -40820,  1500,    40910,   0x007C, 0,  9,  0x0000)

    ChipFrameInfo(296, 0)                                        # 0

    ScpFunction((
        "Function_0_128",          # 00, 0
        "Function_1_1E0",          # 01, 1
        "Function_2_20B",          # 02, 2
        "Function_3_236",          # 03, 3
        "Function_4_261",          # 04, 4
        "Function_5_392",          # 05, 5
        "Function_6_43B",          # 06, 6
        "Function_7_1911",         # 07, 7
        "Function_8_1B75",         # 08, 8
        "Function_9_30BB",         # 09, 9
        "Function_10_3D83",        # 0A, 10
        "Function_11_43FA",        # 0B, 11
    ))


    def Function_0_128(): pass

    label("Function_0_128")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_168"),
        (1, "loc_174"),
        (2, "loc_180"),
        (3, "loc_18C"),
        (4, "loc_198"),
        (5, "loc_1A4"),
        (6, "loc_1B0"),
        (SWITCH_DEFAULT, "loc_1BC"),
    )


    label("loc_168")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_174")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_180")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_18C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_198")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_1A4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_1B0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_1BC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_1C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1DF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1C8")

    label("loc_1DF")

    Return()

    # Function_0_128 end

    def Function_1_1E0(): pass

    label("Function_1_1E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_20A")
    OP_94(0xFE, 0xFFFFF63C, 0x0, 0x9C4, 0x73A, 0x3E8)
    Sleep(300)
    Jump("Function_1_1E0")

    label("loc_20A")

    Return()

    # Function_1_1E0 end

    def Function_2_20B(): pass

    label("Function_2_20B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_235")
    OP_94(0xFE, 0xFFFFF8B2, 0x1A36, 0x744, 0x26DE, 0x3E8)
    Sleep(300)
    Jump("Function_2_20B")

    label("loc_235")

    Return()

    # Function_2_20B end

    def Function_3_236(): pass

    label("Function_3_236")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_260")
    OP_94(0xFE, 0xA00A, 0xA05A, 0xB31A, 0xB220, 0x3E8)
    Sleep(300)
    Jump("Function_3_236")

    label("loc_260")

    Return()

    # Function_3_236 end

    def Function_4_261(): pass

    label("Function_4_261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_26F")
    Jump("loc_391")

    label("loc_26F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2A5")
    SetChrPos(0x8, 810, 0, 500, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, -810, 0, 500, 90)
    Jump("loc_391")

    label("loc_2A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2B3")
    Jump("loc_391")

    label("loc_2B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2D2")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2CD")
    SetChrFlags(0x9, 0x80)

    label("loc_2CD")

    Jump("loc_391")

    label("loc_2D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2E0")
    Jump("loc_391")

    label("loc_2E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2EE")
    Jump("loc_391")

    label("loc_2EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_301")
    SetChrFlags(0x9, 0x80)
    Jump("loc_391")

    label("loc_301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_30F")
    Jump("loc_391")

    label("loc_30F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_31D")
    Jump("loc_391")

    label("loc_31D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_32B")
    Jump("loc_391")

    label("loc_32B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_339")
    Jump("loc_391")

    label("loc_339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_347")
    Jump("loc_391")

    label("loc_347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_355")
    Jump("loc_391")

    label("loc_355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_379")
    SetChrPos(0x9, -42190, 0, 48970, 0)
    SetChrFlags(0x9, 0x10)
    Jump("loc_391")

    label("loc_379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_391")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_391")
    SetChrFlags(0x8, 0x10)

    label("loc_391")

    Return()

    # Function_4_261 end

    def Function_5_392(): pass

    label("Function_5_392")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3BA")
    OP_66(0x0, 0x1)

    label("loc_3BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3FF")
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model05_light", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_3FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43A")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "light01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model05_light", 0x0, 0x1)

    label("loc_43A")

    Return()

    # Function_5_392 end

    def Function_6_43B(): pass

    label("Function_6_43B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53D")

    #C0001
    ChrTalk(
        0xFE,
        (
            "旦那様はオルキスタワーで\x01",
            "今後の指揮を執られているようですな。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "大統領が拘束された今、\x01",
            "クロスベルを導いていけるのは\x01",
            "旦那様お一人しかおられません。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "ご負担はおありでしょうが……\x01",
            "何とかがんばっていただきたいものです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5DE")

    label("loc_53D")


    #C0004
    ChrTalk(
        0xFE,
        (
            "大統領が拘束された今、\x01",
            "クロスベルを導いていけるのは\x01",
            "旦那様お一人しかおられません。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "ご負担はおありでしょうが……\x01",
            "何とかがんばっていただきたいものです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DE")

    Jump("loc_190D")

    label("loc_5E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_692")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FE")
    Call(0, 7)
    Jump("loc_68D")

    label("loc_5FE")


    #C0006
    ChrTalk(
        0xFE,
        (
            "旦那様とお嬢様が\x01",
            "ミシュラムに拘束されて以来、\x01",
            "気が気ではありませんでしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "こうして姿をみることができて\x01",
            "本当に安心いたしました。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_68D")

    Jump("loc_190D")

    label("loc_692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_872")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EB")
    TurnDirection(0xFE, 0x102, 0)

    #C0008
    ChrTalk(
        0xFE,
        (
            "……お嬢様……\x01",
            "旦那様から、何か連絡は\x01",
            "ございましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        "#00103Fいいえ、私の方にも何も……\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "そうでございますか……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "ふむ、とにかく……\x01",
            "私も何か分かり次第、\x01",
            "ご連絡を差し上げます。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "お嬢様がたは、\x01",
            "ご自分たちの仕事に\x01",
            "専念してくださいませ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x102,
        (
            "#00100Fええ、よろしくお願いします\x01",
            "ヘルマーさん。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 2)
    Jump("loc_86D")

    label("loc_7EB")


    #C0014
    ChrTalk(
        0xFE,
        (
            "旦那様に関しましては\x01",
            "なにか分かり次第、\x01",
            "ご連絡を差し上げます。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "お嬢様がたは、\x01",
            "ご自分たちの仕事に\x01",
            "専念してくださいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_86D")

    Jump("loc_190D")

    label("loc_872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_9F2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_972")

    #C0016
    ChrTalk(
        0xFE,
        (
            "……先の襲撃事件、\x01",
            "実に痛ましい出来事でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "復旧活動には、ようやく\x01",
            "目処がついたようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "いまだ恐怖を感じている方も\x01",
            "少なくないご様子。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "再発防止のためにも、\x01",
            "旦那様や市長殿には\x01",
            "頑張って頂きたいものです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9ED")

    label("loc_972")


    #C0020
    ChrTalk(
        0xFE,
        (
            "先日の襲撃事件は、\x01",
            "実に痛ましい出来事でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "再発防止のためにも、\x01",
            "旦那様や市長殿には\x01",
            "頑張って頂きたいものです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9ED")

    Jump("loc_190D")

    label("loc_9F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_B6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE8")

    #C0022
    ChrTalk(
        0xFE,
        (
            "旦那様も、市長と共に\x01",
            "占領事件の対応に当たって\x01",
            "いらっしゃいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "噂では、武装集団には\x01",
            "警備隊ですら手も足も出ない\x01",
            "状況が続いているそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "……心配になってしまいますな。\x01",
            "早急な解決を祈るばかりです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B68")

    label("loc_AE8")


    #C0025
    ChrTalk(
        0xFE,
        (
            "武装集団の手強さに警備隊ですら\x01",
            "手も足も出ないのだとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "……心配になってしまいますな。\x01",
            "早急な解決を祈るばかりです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B68")

    Jump("loc_190D")

    label("loc_B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_CA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C34")

    #C0027
    ChrTalk(
        0xFE,
        (
            "昨日の脱線事故……\x01",
            "いやはや、驚きました。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "原因は落石、あるいは\x01",
            "巨大な化物の仕業などと\x01",
            "騒がれているようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "はて、本当の原因は\x01",
            "なんだったのでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CA0")

    label("loc_C34")


    #C0030
    ChrTalk(
        0xFE,
        "昨日の脱線事故には驚きました。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "様々な噂が流れていますが……\x01",
            "本当の原因は\x01",
            "なんだったのでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CA0")

    Jump("loc_190D")

    label("loc_CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_D06")

    #C0032
    ChrTalk(
        0xFE,
        (
            "なにやら西通りの方で\x01",
            "サイレンが聞こえたような……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "はて、空耳でしょうか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_190D")

    label("loc_D06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_DDC")

    #C0034
    ChrTalk(
        0xFE,
        (
            "国家独立の提唱がされたことで\x01",
            "各方面に影響が出ており、旦那様も\x01",
            "その対応に追われているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "今日もディーター市長と\x01",
            "オルキスタワーで会議なのだとか……\x01",
            "お体には気をつけてほしいものですな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_190D")

    label("loc_DDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EDE")

    #C0036
    ChrTalk(
        0xFE,
        (
            "独立の是非を問う住民投票が\x01",
            "近づいてきていますな。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "これに関して旦那様は、\x01",
            "慎重な姿勢をとるべきだと\x01",
            "考えておられるようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "果たしてクロスベルの住民は\x01",
            "どのような選択をするのか……\x01",
            "個人的にも興味があるところです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F73")

    label("loc_EDE")


    #C0039
    ChrTalk(
        0xFE,
        (
            "独立の是非を問う住民投票が\x01",
            "近づいてきていますな。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "果たしてクロスベルの住民は\x01",
            "どのような選択をするのか……\x01",
            "個人的にも興味があるところです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F73")

    Jump("loc_190D")

    label("loc_F78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_FFD")

    #C0041
    ChrTalk(
        0xFE,
        (
            "旦那様も、今朝早くに\x01",
            "オルキスタワーの方へと\x01",
            "向かわれました。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "今日の本会議……\x01",
            "滞りなく終わればよいのですが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_190D")

    label("loc_FFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_11A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_110A")

    #C0043
    ChrTalk(
        0xFE,
        (
            "旦那様は最近お忙しく、\x01",
            "屋敷に帰られずに市庁の方で\x01",
            "お休みになる事も多かったのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "先ほど連絡がありまして、\x01",
            "今日は久しぶりに屋敷に\x01",
            "お戻りになられるようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "明日の本会議に向けて、\x01",
            "是非とも英気を養って\x01",
            "いただきたいですな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11A1")

    label("loc_110A")


    #C0046
    ChrTalk(
        0xFE,
        (
            "今宵は旦那様のために、\x01",
            "栄養価の高いメニューを\x01",
            "用意させていただいております。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "明日の本会議に向けて、是非とも\x01",
            "英気を養っていただきたいですな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11A1")

    Jump("loc_190D")

    label("loc_11A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1366")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B6")

    #C0048
    ChrTalk(
        0xFE,
        (
            "ハルトマン議長がいた頃の議会では、\x01",
            "旦那様は帝国派と共和国派を\x01",
            "抑えるだけで精一杯のご様子でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "ですが、最近では新市長との連携で\x01",
            "ようやく互角に渡り合えるように\x01",
            "なったとの事……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "私どもも、大変喜ばしいことだと\x01",
            "思っているのですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1361")

    label("loc_12B6")


    #C0051
    ChrTalk(
        0xFE,
        (
            "ディーター殿が市長になられたことは、\x01",
            "私どもも大変喜ばしく思っております。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "明日からは本会議……\x01",
            "旦那様と市長殿には、如何なく\x01",
            "その手腕を発揮してほしいものですな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1361")

    Jump("loc_190D")

    label("loc_1366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1422")

    #C0053
    ChrTalk(
        0xFE,
        (
            "明日からの通商会議のため、\x01",
            "旦那様とディーター市長殿は\x01",
            "入念な準備を進めているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "最近はほとんどお屋敷に\x01",
            "お戻りにもなりませんし……\x01",
            "心配になってしまいますな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_190D")

    label("loc_1422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_15DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1537")

    #C0055
    ChrTalk(
        0xFE,
        (
            "近頃、お隣に\x01",
            "入居された方々ですが……\x01",
            "どうも問題がありまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "導力車で市内を走り回ったり、\x01",
            "夜中に大音量の音楽を流したり……\x01",
            "目に余る行為が目立つようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "苦情を申し上げても聞く耳を\x01",
            "持っていただけませんし……\x01",
            "どうしたらいいものやら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_15D7")

    label("loc_1537")


    #C0058
    ChrTalk(
        0xFE,
        (
            "近頃、お隣に\x01",
            "入居された方々ですが……\x01",
            "目に余る行為が目立つようでして。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "苦情を申し上げても聞く耳を\x01",
            "持っていただけませんし……\x01",
            "どうしたらいいものやら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15D7")

    Jump("loc_190D")

    label("loc_15DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_190D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1888")
    TurnDirection(0xFE, 0x102, 0)

    #C0060
    ChrTalk(
        0xFE,
        (
            "これはこれは、エリィお嬢様。\x01",
            "おかえりなさいませ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        "#00100Fただいま、ヘルマーさん。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x105,
        (
            "#10300Fなるほどね、\x01",
            "ここがエリィの実家なわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x109,
        "#10102Fほんと、大きな屋敷ですよね。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        (
            "#00004Fああ……\x01",
            "なんたって、マクダエル議長の\x01",
            "邸宅でもあるわけだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x102,
        "#00109Fふふ、そう構えないでちょうだい。\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "ええ、皆様はお嬢様の同僚で\x01",
            "あらせられますし、是非とも\x01",
            "寛#2Rくつろ#いでいただければと。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "特務支援課もいよいよ\x01",
            "再開されるということで、\x01",
            "お忙しくなられるでしょうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "今後ともエリィ様を\x01",
            "よろしくお願いいたします。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        "#00000Fええ、お任せください。\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        (
            "#00102Fふふ、ありがとうヘルマーさん。\x01",
            "これからも頑張らせてもらうわね。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xFE, 0x10)
    SetScenarioFlags(0x134, 1)
    Jump("loc_190D")

    label("loc_1888")


    #C0071
    ChrTalk(
        0xFE,
        (
            "特務支援課もいよいよ\x01",
            "再開されるということで、\x01",
            "お忙しくなられるでしょうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "今後ともエリィ様を\x01",
            "よろしくお願いいたします。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_190D")

    TalkEnd(0xFE)
    Return()

    # Function_6_43B end

    def Function_7_1911(): pass

    label("Function_7_1911")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    TurnDirection(0x8, 0x0, 0)
    TurnDirection(0x9, 0x0, 0)

    #C0073
    ChrTalk(
        0x8,
        "おお、皆様っ……！\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x9,
        (
            "お、お嬢様…………\x01",
            "……エリィお嬢様っ……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x102,
        (
            "#00100Fただいまヘルマーさん、ジョアンナ。\x01",
            "……心配をかけたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        "…………（ぶんぶんっ）\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x8,
        (
            "旦那様の無効宣言以来、\x01",
            "エリィ様たちが無事でいるかどうか、\x01",
            "それだけが気がかりでしたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "こうして姿をみることができて\x01",
            "本当に安心いたしました。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x102,
        (
            "#00100Fふふ、ありがとうございます。\x02\x03",

            "#00103F……ただ、今は行かなければ\x01",
            "ならない所があるんです。\x02\x03",

            "#00101Fもうしばらく\x01",
            "留守をお願いできますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        "ええ、もちろんですとも。\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x9,
        (
            "エリィお嬢様、皆様……\x01",
            "どうかお気をつけてくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    OP_93(0x9, 0x5A, 0x0)
    SetScenarioFlags(0x1CC, 7)
    Return()

    # Function_7_1911 end

    def Function_8_1B75(): pass

    label("Function_8_1B75")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1D1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC0")

    #C0082
    ChrTalk(
        0xFE,
        (
            "エリィお嬢様は、\x01",
            "あの不気味な大樹の元へ\x01",
            "行かれるのですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x102,
        (
            "#00104F心配しないで、ジョアンナ。\x01",
            "きっとみんなで戻ってくるから。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "……はい。\x01",
            "お嬢様は今まで絶対に\x01",
            "戻ってきてくれましたし……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "ご無事に帰られることを信じています。\x01",
            "……どうかお気をつけてください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D1A")

    label("loc_1CC0")


    #C0087
    ChrTalk(
        0xFE,
        (
            "エリィ様たちがご無事に\x01",
            "帰られることを信じています。\x01",
            "……どうかお気をつけてください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D1A")

    Jump("loc_30B7")

    label("loc_1D1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1D9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D3A")
    Call(0, 7)
    Jump("loc_1D97")

    label("loc_1D3A")


    #C0088
    ChrTalk(
        0xFE,
        "外は大変危険みたいです……\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "エリィお嬢様、皆様……\x01",
            "どうかお気をつけてくださいませ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D97")

    Jump("loc_30B7")

    label("loc_1D9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1FB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F42")

    #C0090
    ChrTalk(
        0xFE,
        (
            "旦那様……\x01",
            "一体どこへ行って\x01",
            "しまわれたのでしょうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        "私、心配で心配で……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#00003Fさっきの演説の場にも\x01",
            "姿を見せていなかったよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x102,
        "#00108Fおじいさま、本当にどこに……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 500)

    #C0094
    ChrTalk(
        0xFE,
        (
            "……ああ、すみません！\x01",
            "いたずらにお嬢様の不安を\x01",
            "煽るようなことを……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x102,
        (
            "#00103F……ううん、私は大丈夫。\x02\x03",

            "#00100Fジョアンナのほうこそ、\x01",
            "あまり心配しすぎないようにね。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        "わ、分かりました……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18C, 3)
    Jump("loc_1FB1")

    label("loc_1F42")


    #C0097
    ChrTalk(
        0xFE,
        (
            "……私としたことが、\x01",
            "いたずらにお嬢様の不安を\x01",
            "煽るようなことを……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "旦那様……\x01",
            "きっと無事ですよね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FB1")

    Jump("loc_30B7")

    label("loc_1FB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2105")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8F, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x198, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FE8")
    Call(0, 10)
    Return()

    label("loc_1FE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 6)), scpexpr(EXPR_END)), "loc_207F")

    #C0099
    ChrTalk(
        0xFE,
        (
            "……やっぱり…………\x01",
            "ミスコンに出させて\x01",
            "いただこうと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "……必要になったらお呼びください。\x01",
            "すぐに向かいますので…………\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2100")

    label("loc_207F")


    #C0101
    ChrTalk(
        0xFE,
        (
            "今日は行政区の方で\x01",
            "チャリティイベントを\x01",
            "やってるそうですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "……私も、なんらかの形で\x01",
            "お手伝いできないでしょうか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2100")

    Jump("loc_30B7")

    label("loc_2105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_217F")

    #C0103
    ChrTalk(
        0xFE,
        "鉱山町が占拠されるなんて……\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "……私、怖いです……\x01",
            "これからまた、なにかが\x01",
            "起こりそうな気がして……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30B7")

    label("loc_217F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_21D2")

    #C0105
    ChrTalk(
        0xFE,
        "最近、雨が多いですね……\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "……洗濯物が乾きません。\x01",
            "はあ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30B7")

    label("loc_21D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_21E0")
    Jump("loc_30B7")

    label("loc_21E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_23D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2358")

    #C0107
    ChrTalk(
        0xFE,
        (
            "最近特にお忙しい旦那様には、\x01",
            "精のつくお食事を用意しませんと……\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        "……どんなお料理がいいでしょうか。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x102,
        (
            "#00100Fそうねえ……\x01",
            "ラム肉なんてどうかしら。\x02\x03",

            "#00104F高タンパクで低カロリーだし、\x01",
            "おじいさまのお口にも合うと思うわ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 500)

    #C0110
    ChrTalk(
        0xFE,
        (
            "……いいかもしれませんね……\x01",
            "さすがはエリィ様です。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        (
            "#00109Fあ、あはは。\x01",
            "このくらいで褒められても……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_23CF")

    label("loc_2358")


    #C0112
    ChrTalk(
        0xFE,
        (
            "私は小食なので\x01",
            "あまり食べないのですけど、\x01",
            "お肉はいいかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "あとで百貨店に\x01",
            "買い物に行きませんと……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23CF")

    Jump("loc_30B7")

    label("loc_23D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_254C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2510")

    #C0114
    ChrTalk(
        0xFE,
        (
            "この間の通商会議で\x01",
            "テロリストの襲撃があったと聞いて……\x01",
            "私、心臓が止まりそうでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "あれ以来、エリィ様や旦那様が\x01",
            "ずっと心配でたまりません……\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        (
            "#00103Fジョアンナ……\x01",
            "あまり心配しすぎないで。\x02\x03",

            "#00100F支援課のみんなもいるし……\x01",
            "きっと大丈夫だから。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        "はい……そうですね……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2547")

    label("loc_2510")


    #C0118
    ChrTalk(
        0xFE,
        (
            "皆様、エリィ様の事……\x01",
            "よろしくおねがいしますね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2547")

    Jump("loc_30B7")

    label("loc_254C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_25A7")

    #C0119
    ChrTalk(
        0xFE,
        (
            "エリィ様……\x01",
            "今日も街は厳戒態勢みたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        "どうかお気をつけて……\x02",
    )

    CloseMessageWindow()
    Jump("loc_30B7")

    label("loc_25A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_276D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26CE")

    #C0121
    ChrTalk(
        0xFE,
        (
            "今日の晩餐は、\x01",
            "旦那様お気に入りの\x01",
            "にがトマト料理です。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xFE,
        (
            "にがトマトのサラダ、\x01",
            "にがトマトソースのスパゲッティ、\x01",
            "にがトマト１００％ジュース……\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        (
            "#00005F（う、うわあ……\x01",
            "  徹底したメニューだなあ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x102,
        (
            "#00106F（おじいさま、\x01",
            "  そこまで好きだったなんて……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2768")

    label("loc_26CE")


    #C0125
    ChrTalk(
        0xFE,
        (
            "今日は旦那様の好きな、\x01",
            "にがトマト料理です。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "健康にいいらしいですし、\x01",
            "私もガマンして\x01",
            "食べようと思います……\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x102,
        "#00105Fム、ムリしないでね……？\x02",
    )

    CloseMessageWindow()

    label("loc_2768")

    Jump("loc_30B7")

    label("loc_276D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_28FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_284F")

    #C0128
    ChrTalk(
        0xFE,
        (
            "今朝、隣に住んでいる方々と\x01",
            "玄関先で出くわしまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "突然、『一緒にドライブに行こう』\x01",
            "などと誘われてしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "もちろん丁重にお断りしましたが、\x01",
            "なんだか馴れ馴れしい方々ですね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28F6")

    label("loc_284F")


    #C0131
    ChrTalk(
        0xFE,
        (
            "今朝、隣に住んでいる方々に\x01",
            "突然、『一緒にドライブに行こう』\x01",
            "などと誘われてしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "もちろん丁重にお断りしましたが、\x01",
            "なんだか馴れ馴れしい方々ですね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28F6")

    Jump("loc_30B7")

    label("loc_28FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2982")

    #C0133
    ChrTalk(
        0xFE,
        (
            "明日、お披露目される\x01",
            "新市庁ビル……\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "垂れ幕がかかった状態でも\x01",
            "充分に迫力を感じて、\x01",
            "クラクラしてしまいますね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30B7")

    label("loc_2982")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2AC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A6F")

    #C0135
    ChrTalk(
        0xFE,
        "（きゅっきゅっきゅっ）\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x102,
        (
            "#00105Fえっと、ジョアンナ。\x01",
            "窓に何か描いてるの？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x9, 0x102, 1000)
    Sleep(1000)

    #C0137
    ChrTalk(
        0xFE,
        (
            "……ま、窓が\x01",
            "曇っていたので思わず……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "し、失礼しました。\x01",
            "お掃除に戻ります。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x9, 0x10)
    Jump("loc_2AC2")

    label("loc_2A6F")


    #C0139
    ChrTalk(
        0xFE,
        (
            "どうも雨音を聞いていると\x01",
            "気が散ってしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        "はあ、雨の日は苦手です。\x02",
    )

    CloseMessageWindow()

    label("loc_2AC2")

    Jump("loc_30B7")

    label("loc_2AC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_30B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x134, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3013")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0x9, 0x102, 0)
    Sleep(1000)

    #C0141
    ChrTalk(
        0xFE,
        "あ……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        "お帰りなさいませ、エリィ様。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x102,
        (
            "#00100Fただいまジョアンナ。\x01",
            "今日は変わりないかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        "はい……おかげさまで。\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "お嬢様が外遊から戻ってきて下さって、\x01",
            "私もようやく安心することができました。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x102,
        (
            "#00102Fふふ、ジョアンナったら……\x01",
            "そこまで心配することはないのよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "いえ、私にとってはお嬢様と\x01",
            "旦那様こそがすべてですから……\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x105,
        "#10309Fフフ、主人想いのメイドさんだね。\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0149
    ChrTalk(
        0xFE,
        (
            "……あの、エリィ様。\x01",
            "先日、若旦那様と若奥様から\x01",
            "お手紙が届いてらっしゃいましたが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0150
    ChrTalk(
        0x101,
        "#00005Fそれって……\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x102,
        (
            "#00103F……うん、共和国と帝国にいる\x01",
            "私の両親のことよ。\x02\x03",

            "#00100F今までも時々届いていたけど、\x01",
            "あの教団事件が終わってからは\x01",
            "以前よりもよく届くようになったの。\x02\x03",

            "#00104F私やおじいさまを心配してくれるような\x01",
            "内容がほとんどで、\x01",
            "最近の励みの一つになっているわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x109,
        "#10105Fそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x105,
        "#10303F（……家族、か……）\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x102,
        (
            "#00100Fジョアンナ、あとで読ませてもらうから\x01",
            "大事に保管しておいてくれるかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        "はい……ではそういたします。\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "その、特務支援課が再開されたと\x01",
            "聞きましたが……くれぐれもお体には\x01",
            "気をつけてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "旦那様も、若旦那様も、若奥様も……\x01",
            "もちろんこの私も、お嬢様のことを\x01",
            "いつでも案じておりますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x102,
        (
            "#00109Fふふ、分かってる。\x01",
            "ありがとうジョアンナ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x134, 2)
    Jump("loc_30B7")

    label("loc_3013")

    TurnDirection(0x9, 0x102, 0)

    #C0159
    ChrTalk(
        0xFE,
        (
            "エリィ様、くれぐれもお体には\x01",
            "お気をつけください。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "旦那様も、若旦那様も、若奥様も……\x01",
            "もちろんこの私も、お嬢様のことを\x01",
            "いつでも案じておりますから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30B7")

    TalkEnd(0xFE)
    Return()

    # Function_8_1B75 end

    def Function_9_30BB(): pass

    label("Function_9_30BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 5)), scpexpr(EXPR_END)), "loc_3166")
    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0161
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1Kクインシー社のパンフレットを読みますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "読む\x01",          # 0
            "読まない\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3155")
    Call(0, 11)
    TalkEnd(0xFF)
    Jump("loc_3161")

    label("loc_3155")

    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_3161")

    Jump("loc_3D82")

    label("loc_3166")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-41830, 1500, 40450, 0)
    MoveCamera(52, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(18820, 0)
    SetChrPos(0x101, -43440, 60, 40740, 90)
    SetChrPos(0x102, -41310, 0, 40520, 90)
    SetChrPos(0x103, -42890, 0, 39580, 45)
    SetChrPos(0x104, -42860, 60, 41860, 135)
    SetChrPos(0x109, -42020, 0, 38900, 0)
    SetChrPos(0x105, -41650, 0, 42460, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0162
    ChrTalk(
        0x102,
        "#00105Fええと……あったわ。\x02",
    )

    CloseMessageWindow()
    Sound(802, 0, 100, 0)
    Sleep(400)
    OP_93(0x102, 0x10E, 0x1F4)

    #C0163
    ChrTalk(
        0x102,
        (
            "#00100Fこれがクインシー社の\x01",
            "パンフレットよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x104,
        (
            "#00305Fへえ……\x01",
            "しっかりした装丁だな。\x02\x03",

            "#00300Fとても単なる資料には\x01",
            "見えないんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x103,
        (
            "#00200F大企業だからこそできる\x01",
            "力の入れ方でしょうね。\x02\x03",

            "資料の中身の情報も\x01",
            "信頼性が高そうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x102,
        "#00109Fふふ、それはよかったわ。\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        (
            "#00001Fよし……\x01",
            "とにかくざっと読んでみようか。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 11)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)

    #C0168
    ChrTalk(
        0x105,
        (
            "#10303Fふむ、ざっと目を通してみたけど……\x01",
            "あまり大した事は書いてないねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x109,
        (
            "#10105Fミンネスの発言に矛盾する内容、\x01",
            "見つかりましたか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x102,
        (
            "#00106Fう、う～ん……\x01",
            "やっぱりこんな資料からなんて\x01",
            "無理があったのかしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        "#00003Fいや……矛盾は見つかったよ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_359C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_359C)
    Sleep(50)

    def lambda_35AC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_35AC)
    Sleep(50)

    def lambda_35BC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_35BC)
    Sleep(50)

    def lambda_35CC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_35CC)

    #C0172
    ChrTalk(
        0x103,
        "#00205F……マジですか。\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x104,
        (
            "#00309Fはは、相変わらず\x01",
            "頼りになるなあオイ。\x02\x03",

            "#00300Fんで、どういう矛盾なんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        (
            "#00004F昨日のホテルでの会話を\x01",
            "よく思い出せさえすれば、\x01",
            "そこまで難しくはない答えだよ。\x02\x03",

            "#00000F一言だけ、ミンネスがこぼした言葉……\x01",
            "それと矛盾する内容が確かにあるんだ。\x02\x03",

            "それこそが、ミンネスは\x01",
            "『クインシー社の役員』ではない\x01",
            "という証拠になっている……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x109,
        (
            "#10105Fそ、そこまでのヒントが\x01",
            "この資料の中に……？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        "#00000Fああ、それは──\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x105,
        (
            "#10304F──待った、\x01",
            "それは一旦黙ってようよ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_37D1():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_37D1)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0178
    ChrTalk(
        0x101,
        "#00005Fへ……どうしてだ？\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、キミだけ分かってるってのも\x01",
            "何だかシャクじゃないか。\x02\x03",

            "#10309Fだから、実際に\x01",
            "ミンネスに突きつける時まで\x01",
            "宿題にしておかない？\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#00006Fあ、あのなあ。\x01",
            "遊びじゃないんだから……\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x103,
        (
            "#00203Fいえ、ワジさんの言うことも\x01",
            "もっともです。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_390F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_390F)
    Sleep(100)

    #C0182
    ChrTalk(
        0x103,
        (
            "#00203Fロイドさんの答えが\x01",
            "間違っている可能性もありますし、\x01",
            "ここで考えを統一するのは危険かと。\x02\x03",

            "#00211Fそれに、いつもいつも\x01",
            "ロイドさんに良い所を持って\x01",
            "いかれるのもシャクですし。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ACA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0183
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "◆ＩＢＣを（テスト用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【変更しない】\x01",                  # 0
            "【調べたことにする】\x01",            # 1
            "【調べていないことにする】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3AB5"),
        (1, "loc_3ABA"),
        (2, "loc_3AC2"),
        (SWITCH_DEFAULT, "loc_3ACA"),
    )


    label("loc_3AB5")

    Jump("loc_3ACA")

    label("loc_3ABA")

    SetScenarioFlags(0x177, 4)
    Jump("loc_3ACA")

    label("loc_3AC2")

    ClearScenarioFlags(0x177, 4)
    Jump("loc_3ACA")

    label("loc_3ACA")

    OP_29(0x87, 0x1, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x177, 4)), scpexpr(EXPR_END)), "loc_3C39")

    #C0184
    ChrTalk(
        0x101,
        (
            "#00006F（むしろ後者が本心っぽいな……）\x02\x03",

            "#00001Fわ、分かったよ。\x01",
            "それじゃあ皆にも一応、\x01",
            "考えておいてもらうとして……\x02\x03",

            "この資料については、\x01",
            "要点を手帳にメモしておくとしよう。\x02\x03",

            "#00003F……ひとまずこれで、\x01",
            "ミンネスの疑惑を追及する\x01",
            "材料が集まったはずだ。\x02\x03",

            "#00000F一旦、ハロルドさんの家に\x01",
            "戻る事にしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x102,
        "#00100Fええ、そうしましょう。\x02",
    )

    CloseMessageWindow()
    OP_29(0x87, 0x1, 0x4)
    Jump("loc_3D49")

    label("loc_3C39")


    #C0186
    ChrTalk(
        0x101,
        (
            "#00006F（むしろ後者が本心っぽいな……）\x02\x03",

            "#00001Fわ、分かったよ。\x01",
            "それじゃあ皆にも一応、\x01",
            "考えておいてもらうとして……\x02\x03",

            "この資料については、\x01",
            "要点を手帳にメモしておくとしよう。\x02\x03",

            "#00003F……残るはＩＢＣの捜査だけだな。\x01",
            "早速調べにいくとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x102,
        "#00100Fええ、了解よ。\x02",
    )

    CloseMessageWindow()

    label("loc_3D49")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x177, 5)
    SetChrPos(0x0, -43000, 60, 40720, 90)
    OP_69(0xFF, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)

    label("loc_3D82")

    Return()

    # Function_9_30BB end

    def Function_10_3D83(): pass

    label("Function_10_3D83")

    EventBegin(0x0)
    Fade(500)
    OP_68(-45700, 1560, 2610, 0)
    MoveCamera(38, 32, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(23160, 0)
    SetChrPos(0x101, -44780, 60, 2500, 0)
    SetChrPos(0x102, -45960, 0, 2500, 0)
    SetChrPos(0x103, -46730, 0, 1660, 0)
    SetChrPos(0x104, -44030, 0, 1620, 0)
    SetChrPos(0x105, -45860, 0, 980, 0)
    SetChrPos(0x109, -44820, 0, 940, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x9, 0xFF)
    OP_93(0x9, 0xB4, 0x0)
    OP_0D()

    #C0188
    ChrTalk(
        0x9,
        (
            "あ……\x01",
            "エリィお嬢様、皆さん……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x105,
        (
            "#10300F（ミスコンの『メイド』枠……\x01",
            "  彼女はどうかな？）\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x101,
        (
            "#00003F（そうだな……\x01",
            "  いいかもしれない。）\x02\x03",

            "#00000F（エリィ、\x01",
            "  頼んでみてくれないか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x102,
        (
            "#00102F（分かったわ。\x01",
            "  難しいと思うけど……）\x02\x03",

            "#00100Fねえジョアンナ、\x01",
            "あなたにお願いがあるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x9,
        (
            "はい……\x01",
            "エリィさまのお願いとあらば\x01",
            "なんなりと。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0193
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "チャリティイベントの\x01",
            "ミスコンへの参加を頼んでみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0194
    ChrTalk(
        0x9,
        (
            "……はあ……\x01",
            "ミス、コ………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0195
    ChrTalk(
        0x9,
        "#4S……えええええええ！？\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x103,
        "#00205F……すごい驚きようですね。\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x9,
        (
            "む、むむ、無理です……\x01",
            "私なんかがミスコンだなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x104,
        (
            "#00302Fいやいや、大丈夫だって。\x01",
            "お兄さんが保証しちゃうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x101,
        "#00006F何の保証だよ……\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x102,
        (
            "#00105Fえ、えっとジョアンナ？\x01",
            "気にしなくてもいいからね。\x02\x03",

            "#00103F探せばなんとか、\x01",
            "よそのメイドさんにでも\x01",
            "参加してもらえると思うし……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0201
    ChrTalk(
        0x9,
        "………………………………\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x9,
        (
            "……あの、やっぱり…………\x01",
            "出させていただきたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x109,
        (
            "#10105Fそ、それはまた急ですね。\x01",
            "助かっちゃいますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x9,
        (
            "お嬢様のメイドは……\x01",
            "……私、ですから…………\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x102,
        (
            "#00102Fふふ、ありがとうジョアンナ。\x01",
            "でも無理はしないでね？\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x9,
        (
            "……必要になったらお呼びください。\x01",
            "すぐに向かいますので…………\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x101,
        "#00000Fええ、よろしくお願いします。\x02",
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x199, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43C0")

    #C0208
    ChrTalk(
        0x101,
        (
            "#00003F──さて、これでようやく\x01",
            "参加者枠が埋まったな。\x02\x03",

            "#00000F市民会館に行って\x01",
            "ロイさんたちに報告しよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x8F, 0x1, 0x5)

    label("loc_43C0")

    SetScenarioFlags(0x199, 6)
    OP_4C(0x9, 0xFF)
    OP_93(0x9, 0x0, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -45350, 60, 2400, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_10_3D83 end

    def Function_11_43FA(): pass

    label("Function_11_43FA")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(18, 0, 100, 0)
    Sleep(300)
    SetChrName("")

    #A0209
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3S……当社は、製菓業界の第一人者として\x01",
            "製菓の未来のために、日夜研鑚を重ねています。\x01",
            "このパンフレットでは、そうした\x01",
            "当社の姿の一端を紹介したいと思います。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(18, 0, 100, 0)
    SetChrName("")

    #A0210
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3Sお菓子にとって最も重要なのは、\x01",
            "『美味しい』と思ってもらえるかどうか、\x01",
            "その一点に尽きると当社は考えています。\x01",
            "そのため当社では、\x01",
            "『お菓子のクオリティを高める』という\x01",
            "ことにおいては一切の妥協をしません。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(18, 0, 100, 0)
    SetChrName("")

    #A0211
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3S製菓工場には最新の設備が整えられ、\x01",
            "衛生面にも最大限の配慮が\x01",
            "為されているのはもちろんのこと、\x01",
            "お菓子に使用される材料の品質や\x01",
            "その産地にも強い拘りを持っています。\x01",
            "また、商品開発についても\x01",
            "厳正な基準が定められています。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(18, 0, 100, 0)
    SetChrName("")

    #A0212
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3S役員自らが開発中の商品を試食し、\x01",
            "販売に耐えうる商品かどうかを審査され、\x01",
            "それから何度もの企画会議を経て\x01",
            "ようやく製造ラインに乗るのです。\x01",
            "これは確実にお客様にお喜びしてもらえる\x01",
            "最高のお菓子をお届けしていくための、\x01",
            "社の設立当時からの伝統なのです。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(18, 0, 100, 0)
    SetChrName("")

    #A0213
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3Sそうして常に高いクオリティのお菓子を\x01",
            "提供し続けてきたからこそ、\x01",
            "現在のクインシー社の姿があるのです……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sound(18, 0, 100, 0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Return()

    # Function_11_43FA end

    SaveToFile()

Try(main)
