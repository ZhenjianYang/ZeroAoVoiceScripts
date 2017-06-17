from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1050.bin",                # FileName
        "c1050",                    # MapName
        "c1050",                    # Location
        0x0001,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 3],
    )

    BuildStringList((
        "c1050",                  # 0
        "モルス老人",             # 1
        "パーラ夫人",             # 2
        "ロイ",                   # 3
        "メイリン",               # 4
    ))

    AddCharChip((
        "chr/ch20800.itc",                   # 00
        "chr/ch20900.itc",                   # 01
        "chr/ch20802.itc",                   # 02
        "chr/ch21202.itc",                   # 03
        "chr/ch21502.itc",                   # 04
        "chr/ch21200.itc",                   # 05
        "chr/ch21500.itc",                   # 06
    ))

    DeclNpc(569,     4019,    7690,    135,  261,  0x0, 0,   0,   0,   0,   1,   0,   4,   255,  0)
    DeclNpc(379,     0,       9850,    0,    261,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(889,     100,     6969,    270,  389,  0x0, 0,   3,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(-2150,   100,     7010,    90,   389,  0x0, 0,   4,   0,   255, 255, 0,   7,   255,  0)

    ChipFrameInfo(328, 0)                                        # 0

    ScpFunction((
        "Function_0_148",          # 00, 0
        "Function_1_200",          # 01, 1
        "Function_2_22B",          # 02, 2
        "Function_3_3B3",          # 03, 3
        "Function_4_43C",          # 04, 4
        "Function_5_176B",         # 05, 5
        "Function_6_2839",         # 06, 6
        "Function_7_29DC",         # 07, 7
        "Function_8_2A74",         # 08, 8
        "Function_9_3098",         # 09, 9
    ))


    def Function_0_148(): pass

    label("Function_0_148")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_188"),
        (1, "loc_194"),
        (2, "loc_1A0"),
        (3, "loc_1AC"),
        (4, "loc_1B8"),
        (5, "loc_1C4"),
        (6, "loc_1D0"),
        (SWITCH_DEFAULT, "loc_1DC"),
    )


    label("loc_188")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_194")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_1A0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_1AC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_1B8")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_1C4")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_1D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_1DC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_1E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1FF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1E8")

    label("loc_1FF")

    Return()

    # Function_0_148 end

    def Function_1_200(): pass

    label("Function_1_200")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_22A")
    OP_94(0xFE, 0x582, 0x24F4, 0xFFFFFCF4, 0x1306, 0x3E8)
    Sleep(300)
    Jump("Function_1_200")

    label("loc_22A")

    Return()

    # Function_1_200 end

    def Function_2_22B(): pass

    label("Function_2_22B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_239")
    Jump("loc_3B2")

    label("loc_239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2C8")
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x5)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrPos(0xA, 1020, 0, 3500, 270)
    SetChrPos(0x8, -800, 0, 3500, 90)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_288")
    SetChrFlags(0xA, 0x10)

    label("loc_288")

    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x6)
    BeginChrThread(0xB, 0, 0, 0)
    SetChrPos(0xB, 1040, 4019, 7540, 0)
    SetChrPos(0x9, 1040, 4019, 8540, 180)
    SetChrFlags(0x9, 0x10)
    Jump("loc_3B2")

    label("loc_2C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2D6")
    Jump("loc_3B2")

    label("loc_2D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2E9")
    SetChrFlags(0x8, 0x80)
    Jump("loc_3B2")

    label("loc_2E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2F7")
    Jump("loc_3B2")

    label("loc_2F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_305")
    Jump("loc_3B2")

    label("loc_305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_318")
    SetChrFlags(0x8, 0x80)
    Jump("loc_3B2")

    label("loc_318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_32B")
    SetChrFlags(0x8, 0x80)
    Jump("loc_3B2")

    label("loc_32B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_339")
    Jump("loc_3B2")

    label("loc_339")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_347")
    Jump("loc_3B2")

    label("loc_347")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_355")
    Jump("loc_3B2")

    label("loc_355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_363")
    Jump("loc_3B2")

    label("loc_363")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3A9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3A4")
    SetChrChipByIndex(0xA, 0x3)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xB, 0x80)

    label("loc_3A4")

    Jump("loc_3B2")

    label("loc_3A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3B2")

    label("loc_3B2")

    Return()

    # Function_2_22B end

    def Function_3_3B3(): pass

    label("Function_3_3B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3FC")
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_3FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43B")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)

    label("loc_43B")

    Return()

    # Function_3_3B3 end

    def Function_4_43C(): pass

    label("Function_4_43C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52C")

    #C0001
    ChrTalk(
        0xFE,
        (
            "クロスベルは日常を\x01",
            "取り戻しつつあるが、\x01",
            "まだ問題は山積みじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "国交を断った影響で\x01",
            "何処の商店も十分な商品を\x01",
            "揃えられてはおらぬ。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "マクダエル議長とも\x01",
            "連絡を取り合いつつ、\x01",
            "なんとか対策を考えねばな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5B8")

    label("loc_52C")


    #C0004
    ChrTalk(
        0xFE,
        (
            "クロスベルは日常を\x01",
            "取り戻しつつあるが、\x01",
            "まだ問題は山積みじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "マクダエル議長とも\x01",
            "連絡を取り合いつつ、\x01",
            "なんとか対策を考えねばな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B8")

    Jump("loc_1767")

    label("loc_5BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_70E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68C")

    #C0006
    ChrTalk(
        0xFE,
        (
            "ううむ、露店の者たちの\x01",
            "安否が気がかりじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "戒厳令下でも、どうしても\x01",
            "商売をつづけたいというから\x01",
            "許可してしまったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "もし、彼らに何かあったら\x01",
            "わしの責任じゃよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_709")

    label("loc_68C")


    #C0009
    ChrTalk(
        0xFE,
        (
            "ううむ、露店の者たちの\x01",
            "安否が気がかりじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "もし、彼らに何かあったら\x01",
            "戒厳令下の商売を許可した\x01",
            "わしの責任じゃよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_709")

    Jump("loc_1767")

    label("loc_70E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_90B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_890")

    #C0011
    ChrTalk(
        0xFE,
        (
            "例のディーター殿の演説……\x01",
            "マクダエル議長が姿を\x01",
            "見せていなかったのが気になるが。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "エリィ君、\x01",
            "何か知ってはおらぬのかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x102,
        (
            "#00103F……いえ。\x01",
            "実は私も少し気になっていまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "ふむ、そうか……\x01",
            "さぞ心配じゃろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "いずれにせよ\x01",
            "こうなってしまった以上、\x01",
            "２大国との対立は避けられまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "有事に備えておくように\x01",
            "商工会から呼びかけねばな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_906")

    label("loc_890")


    #C0017
    ChrTalk(
        0xFE,
        (
            "こうなってしまった以上、\x01",
            "２大国との対立は避けられまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "有事に備えておくように\x01",
            "商工会から呼びかけねばな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_906")

    Jump("loc_1767")

    label("loc_90B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_919")
    Jump("loc_1767")

    label("loc_919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_A8D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A0B")

    #C0019
    ChrTalk(
        0xFE,
        (
            "ふむ、住民投票も\x01",
            "間近に迫ったこの時期に、\x01",
            "かような事件が起こるとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "下手をすると、帝国や共和国に\x01",
            "付け込まれる格好の材料に\x01",
            "なってしまうかもしれん。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "なんとしても、早急な解決が\x01",
            "望まれるところじゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A88")

    label("loc_A0B")


    #C0022
    ChrTalk(
        0xFE,
        (
            "ただでさえ、\x01",
            "治安の面で帝国や共和国に\x01",
            "弱みを見せている現状じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "なんとしても、早急な解決が\x01",
            "望まれるところじゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A88")

    Jump("loc_1767")

    label("loc_A8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_C0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B6F")

    #C0024
    ChrTalk(
        0xFE,
        (
            "昨日の列車事故は\x01",
            "得体のしれない化け物の\x01",
            "仕業だったとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "ふむ、最近目撃されるという\x01",
            "不可思議な怪物と\x01",
            "同じものなのかのう？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "近頃ただでさえ事件が多い。\x01",
            "諸君らも充分気をつけるのじゃぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C08")

    label("loc_B6F")


    #C0027
    ChrTalk(
        0xFE,
        (
            "列車事故を起こした化け物が\x01",
            "最近噂される不可思議な怪物と\x01",
            "同じものかはわからんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "近頃ただでさえ事件が多い。\x01",
            "諸君らも充分気をつけるのじゃぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C08")

    Jump("loc_1767")

    label("loc_C0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_C1B")
    Jump("loc_1767")

    label("loc_C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_C29")
    Jump("loc_1767")

    label("loc_C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E6A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9D")

    #C0029
    ChrTalk(
        0xFE,
        (
            "クロスベル自治州の独立……\x01",
            "ディーター市長も思い切ったことを\x01",
            "宣言したものじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "だが、内外への発言力が\x01",
            "かつてないほどに高まっておる\x01",
            "今こそが、好機なのは間違いない。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "長い歴史で２大国に支配され続け、\x01",
            "失われつつあるクロスベルの誇り……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "色々と軋轢はあるだろうが、\x01",
            "独立の実現という結果を以って\x01",
            "何としても取り戻してほしいものじゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E65")

    label("loc_D9D")


    #C0033
    ChrTalk(
        0xFE,
        (
            "……そうそう、そんな市長の\x01",
            "最近の勢いを応援する意味でも、\x01",
            "ある企画を進めておるのじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "クロスベル通信社と共同の企画じゃ、\x01",
            "市民も活気付いてくれるじゃろう。\x01",
            "諸君も、楽しみにしておいてくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E65")

    Jump("loc_1767")

    label("loc_E6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_F73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F0C")

    #C0035
    ChrTalk(
        0xFE,
        "ついに通商会議が始まるのう。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "わしら市民は\x01",
            "クロスベルタイムズでの\x01",
            "結果を待つのみじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "さて……\x01",
            "どんな会議になるのやら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F6E")

    label("loc_F0C")


    #C0038
    ChrTalk(
        0xFE,
        (
            "本来ならば、ぜひとも\x01",
            "会議の様子を見たかったものじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "さて……\x01",
            "どんな会議になるのやら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F6E")

    Jump("loc_1767")

    label("loc_F73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_FFC")

    #C0040
    ChrTalk(
        0xFE,
        (
            "どうやら孫のロイが、\x01",
            "露店の仕事に興味を\x01",
            "持ち始めたそうじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "……わしも元は露天商でな。\x01",
            "ふむ、これも血筋かのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1767")

    label("loc_FFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_114E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 3)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1030")
    Call(0, 9)
    Jump("loc_10BF")

    label("loc_1030")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CA, 0)), scpexpr(EXPR_END)), "loc_10BF")

    #C0042
    ChrTalk(
        0x8,
        (
            "ふむ、まさか黒月の\x01",
            "長老さんのお孫さんが\x01",
            "ウチに来てくれるなんてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "何はともあれ、\x01",
            "この街を気に入ってくれると\x01",
            "私も嬉しいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10BF")

    Jump("loc_1149")

    label("loc_10C4")


    #C0044
    ChrTalk(
        0xFE,
        (
            "通商会議では、各国の代表者が\x01",
            "主に経済関係の取り決めについて\x01",
            "協議を行う。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "わしら商工会もその動向には\x01",
            "注目しているのじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1149")

    Jump("loc_1767")

    label("loc_114E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1509")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13AA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1313")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1275")

    #C0046
    ChrTalk(
        0xFE,
        (
            "おや、ロイドくんじゃないか。\x01",
            "一体どうしたね？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#00000Fえっと……\x01",
            "メイリンちゃんは\x01",
            "ご在宅でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "ん、さっき帰ってきたと\x01",
            "思っておったが……\x01",
            "またどこかに行ったかの？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "すまないが、婆さんに\x01",
            "聞いてもらえるかな？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12DC")

    label("loc_1275")


    #C0050
    ChrTalk(
        0xFE,
        (
            "仕事をしていてな。\x01",
            "孫が出かけたのに\x01",
            "気づかなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "孫については婆さんに\x01",
            "聞いてもらえるかな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12DC")

    Jump("loc_130E")

    label("loc_12E1")


    #C0052
    ChrTalk(
        0xFE,
        (
            "さて、商工会の仕事の\x01",
            "続きをせねばな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_130E")

    Jump("loc_13A6")

    label("loc_1313")


    #C0053
    ChrTalk(
        0xFE,
        (
            "ロイのやつに\x01",
            "説教のひとつでも\x01",
            "してやろうかと思うたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "メイリンのいるところで\x01",
            "やるのもなんじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        "今日のところは見逃してやるか。\x02",
    )

    CloseMessageWindow()

    label("loc_13A6")

    TalkEnd(0xFE)
    Return()

    label("loc_13AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14A4")

    #C0056
    ChrTalk(
        0xFE,
        (
            "教団事件直前に行われた\x01",
            "クロスベル予算議会は、\x01",
            "一旦仕切りなおしになってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "新市長、新議長が中心となって\x01",
            "利権が絡まない案へと\x01",
            "予算が組み直されたんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "うむ、市政もようやく\x01",
            "良い方向へと進みはじめた\x01",
            "ということかのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1504")

    label("loc_14A4")


    #C0059
    ChrTalk(
        0xFE,
        (
            "市政もようやく良い方向へと\x01",
            "進み始めたようじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "これも新市長と新議長の\x01",
            "おかげかのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1504")

    Jump("loc_1767")

    label("loc_1509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1767")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16FB")

    #C0061
    ChrTalk(
        0xFE,
        (
            "おや……ロイド君に、\x01",
            "マクダエル議長のお嬢さんか。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "久しぶりじゃのう。\x01",
            "元気そうで何よりじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        "#00000Fこんにちは、モルス会長。\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x102,
        "#00100Fご無沙汰しています。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x105,
        (
            "#10300F確か、東通りの商人をまとめる\x01",
            "商工会の会長さんだったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x109,
        (
            "#10105Fああ、こちらの方が……\x01",
            "（母さんも露天商時代に\x01",
            "  お世話になったんだっけ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "うむ、新顔もおるようだし\x01",
            "いよいよ特務支援課も\x01",
            "再始動と言ったところか。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "君たちには\x01",
            "わしら市民も期待しておる。\x01",
            "がんばってくれたまえよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 1)
    Jump("loc_1767")

    label("loc_16FB")


    #C0069
    ChrTalk(
        0xFE,
        (
            "君たち特務支援課には\x01",
            "これからも期待しておるぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "何か力になれることがあったら\x01",
            "いつでも来るといい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1767")

    TalkEnd(0xFE)
    Return()

    # Function_4_43C end

    def Function_5_176B(): pass

    label("Function_5_176B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1794")
    Call(0, 8)
    Return()

    label("loc_1794")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1915")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1871")

    #C0071
    ChrTalk(
        0xFE,
        (
            "大統領の拘束を乗り越えて、\x01",
            "これからどうするか……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "それがクロスベルに住む人々にとって\x01",
            "何より大事なことだと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "皆で話し合って、きっといい方向に\x01",
            "物事が進んでいけばいいわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1910")

    label("loc_1871")


    #C0074
    ChrTalk(
        0xFE,
        (
            "これからどうするか……\x01",
            "クロスベルに住む人々にとって\x01",
            "それが何より大事なことだと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "皆で話し合って、きっといい方向に\x01",
            "物事が進んでいけばいいわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1910")

    Jump("loc_2835")

    label("loc_1915")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_19A2")

    #C0076
    ChrTalk(
        0xFE,
        (
            "ロイとおじいさんが\x01",
            "ちゃあんと見張っているから、\x01",
            "怖いのもここにはこないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "だからメイリン、\x01",
            "心配しなくていいからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2835")

    label("loc_19A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1B37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AA8")

    #C0078
    ChrTalk(
        0xFE,
        (
            "ディーターさんの独立宣言……\x01",
            "時期尚早ではなかったかしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "この世のあらゆる物事は\x01",
            "変わっていくものだとは\x01",
            "分かっていたつもりだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "いや……クロスベルは既に\x01",
            "そうも言っていられない状況に\x01",
            "なってしまっていたのかもね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B32")

    label("loc_1AA8")


    #C0081
    ChrTalk(
        0xFE,
        (
            "物事の急激な変化は、\x01",
            "私たち年寄りにとっては\x01",
            "怖いものがあるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "クロスベルは既に\x01",
            "引き返せないところまで\x01",
            "きてしまっていたのね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B32")

    Jump("loc_2835")

    label("loc_1B37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1BD4")

    #C0083
    ChrTalk(
        0xFE,
        (
            "おじいさんなら、商工会の用事で\x01",
            "市民会館に行っているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "今回のチャリティイベントは\x01",
            "ロイも手伝ってるそうだけど……\x01",
            "どうなるかしらね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2835")

    label("loc_1BD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1C5A")

    #C0085
    ChrTalk(
        0xFE,
        (
            "今はとにかく、女神様に\x01",
            "お祈りすることしかできないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "これ以上このクロスベルで\x01",
            "無駄な血が流れませんように……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2835")

    label("loc_1C5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1CE7")

    #C0087
    ChrTalk(
        0xFE,
        (
            "最近は本当に何が起こるか\x01",
            "分からないわねえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "ロイやメイリンにも、\x01",
            "出歩くときには充分に\x01",
            "気をつけるように言わないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2835")

    label("loc_1CE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1D6C")

    #C0089
    ChrTalk(
        0xFE,
        (
            "さてと……\x01",
            "おじいさんとメイリンが\x01",
            "そろそろ帰る頃かしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "紅茶とお菓子を用意して\x01",
            "待っているとしましょうかね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2835")

    label("loc_1D6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1E1A")

    #C0091
    ChrTalk(
        0xFE,
        (
            "おじいさんなら今頃、\x01",
            "表の通りでメイリンと\x01",
            "遊んでるんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "ふふ、おじいさんったら\x01",
            "久しぶりの休みに孫と遊べて、\x01",
            "とってもうれしそうだったわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2835")

    label("loc_1E1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1E9E")

    #C0093
    ChrTalk(
        0xFE,
        (
            "住民投票については、\x01",
            "商工会でも手伝いにまわるそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "一体どうなるのかしら……\x01",
            "私にはまったく分からないわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2835")

    label("loc_1E9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1F35")

    #C0095
    ChrTalk(
        0xFE,
        (
            "おじいさん、商工会の長として\x01",
            "色々と思うところがあるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "もう年なんですから、\x01",
            "あまり無理しないように\x01",
            "してもらわないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2835")

    label("loc_1F35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_206F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FFC")

    #C0097
    ChrTalk(
        0xFE,
        (
            "以前はおじいさんも\x01",
            "ロイの無気力ぶりには\x01",
            "手を焼いていたようだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "この先ロイががんばって、\x01",
            "ゆくゆくは商工会に……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "なんてことになったら、\x01",
            "きっと喜ぶわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_206A")

    label("loc_1FFC")


    #C0100
    ChrTalk(
        0xFE,
        (
            "この先ロイががんばって、\x01",
            "ゆくゆくは商工会に……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        (
            "なんてことになったら、\x01",
            "おじいさん、きっと喜ぶわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_206A")

    Jump("loc_2835")

    label("loc_206F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2442")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 3)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_22E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_229D")

    #C0102
    ChrTalk(
        0x9,
        (
            "あらあら、あなたたち。\x01",
            "今日はまた可愛らしい子を\x01",
            "連れているのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x1A2,
        (
            "フム、ご夫人。\x01",
            "お邪魔させてもらっています。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x1A2, 500)
    Sleep(300)

    #C0104
    ChrTalk(
        0x9,
        (
            "ふふ、どういたしまして。\x01",
            "あなた随分お行儀がよろしいのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        "よければ紅茶でも飲んでいく？\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x1A2,
        (
            "ああいえ、\x01",
            "長居するつもりはないので\x01",
            "おかまいなく。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x102,
        "#00100F（ふふ、見事な社交術ね。）\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        "#00006F（なんていうか……）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_2230")

    #C0109
    ChrTalk(
        0x104,
        "#00300F（ああ、ソツがねえな。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2295")

    label("loc_2230")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_2267")

    #C0110
    ChrTalk(
        0x109,
        "#10100F（ええ、ソツがないですね。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_2295")

    label("loc_2267")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_2295")

    #C0111
    ChrTalk(
        0x105,
        "#10300F（ああ、ソツがないね。）\x02",
    )

    CloseMessageWindow()

    label("loc_2295")

    SetScenarioFlags(0x1DC, 2)
    Jump("loc_22E4")

    label("loc_229D")


    #C0112
    ChrTalk(
        0x9,
        (
            "ふふ、本当に\x01",
            "礼儀正しくて良い子ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x9,
        "ロイにも見習わせたいわ。\x02",
    )

    CloseMessageWindow()

    label("loc_22E4")

    Jump("loc_243D")

    label("loc_22E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C9")

    #C0114
    ChrTalk(
        0xFE,
        (
            "政治の話にはうるさいおじいさんも、\x01",
            "ディーター市長を\x01",
            "とても評価しているみたいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0xFE,
        (
            "なんといっても、天下のＩＢＣを\x01",
            "取り仕切ってきた人ですものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "きっと通商会議でも\x01",
            "活躍してくれることでしょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_243D")

    label("loc_23C9")


    #C0117
    ChrTalk(
        0xFE,
        (
            "おじいさんも、新しい市長さんを\x01",
            "とても評価しているみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "きっと通商会議でも\x01",
            "活躍してくれることでしょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_243D")

    Jump("loc_2835")

    label("loc_2442")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_26DA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_266F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_260F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 4)), scpexpr(EXPR_END)), "loc_260A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_255E")

    #C0119
    ChrTalk(
        0xFE,
        (
            "ロイとメイリンは、\x01",
            "この雨の中散歩に行ってしまったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "そこまで遠くには\x01",
            "行ってないと思うから、\x01",
            "近くの街区を探してみてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        (
            "ロイの緑色の傘か、\x01",
            "メイリンのピンク色の傘の\x01",
            "どちらかを探してみるといいわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_260A")

    label("loc_255E")


    #C0122
    ChrTalk(
        0xFE,
        (
            "ロイとメイリンは\x01",
            "そう遠くに行っていないと思うから、\x01",
            "近くの街区を探してみてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        (
            "ロイの緑色の傘か、\x01",
            "メイリンのピンク色の傘の\x01",
            "どちらかを探してみるといいわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_260A")

    Jump("loc_266B")

    label("loc_260F")


    #C0124
    ChrTalk(
        0xFE,
        (
            "孫が２人とも\x01",
            "帰ってきたことだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "ホットレモネードでも\x01",
            "淹れてあげましょうかね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_266B")

    TalkEnd(0xFE)
    Return()

    label("loc_266F")


    #C0126
    ChrTalk(
        0xFE,
        (
            "うーん、雨足は弱いけど\x01",
            "なかなか止まないわねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "ロイたち、どこまで\x01",
            "買い物に行ったのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2835")

    label("loc_26DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2835")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27D2")

    #C0128
    ChrTalk(
        0xFE,
        "まあまあ、あなたたちは……！\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        "#00002Fお婆さん、お久しぶりです。\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "ええ、こちらこそ。\x01",
            "元気そうでなによりだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "おじいさんには\x01",
            "もう会ったかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "上にいるから、\x01",
            "よかったら挨拶してあげて\x01",
            "ちょうだいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x12F, 2)
    Jump("loc_2835")

    label("loc_27D2")


    #C0133
    ChrTalk(
        0xFE,
        (
            "おじいさんには\x01",
            "もう会ったかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "上にいるから、\x01",
            "よかったら挨拶してあげて\x01",
            "ちょうだいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2835")

    TalkEnd(0xFE)
    Return()

    # Function_5_176B end

    def Function_6_2839(): pass

    label("Function_6_2839")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2970")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28F2")

    #C0135
    ChrTalk(
        0xFE,
        (
            "心配すんなって、じいちゃん。\x01",
            "クロンクさんたちなら\x01",
            "きっと大丈夫だからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "市民会館への問合せも\x01",
            "出来ない状態だし、\x01",
            "今は家でじっとしてようぜ。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)
    Jump("loc_296B")

    label("loc_28F2")


    #C0137
    ChrTalk(
        0xFE,
        (
            "クロンクさんたちなら\x01",
            "きっと大丈夫だからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "市民会館への問合せも\x01",
            "出来ない状態だし、\x01",
            "今は家でじっとしてようぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_296B")

    Jump("loc_29D8")

    label("loc_2970")


    #C0139
    ChrTalk(
        0xFE,
        (
            "よお、傘は無事に\x01",
            "届けてくれたみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "今度からは俺ももうちょっと\x01",
            "しっかりしないとなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29D8")

    TalkEnd(0xFE)
    Return()

    # Function_6_2839 end

    def Function_7_29DC(): pass

    label("Function_7_29DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2A40")

    #C0141
    ChrTalk(
        0xFE,
        (
            "兄たんとおじいちゃんに、\x01",
            "ここにいるように言われたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        "とっても怖いの……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A70")

    label("loc_2A40")


    #C0143
    ChrTalk(
        0xFE,
        "もくもく……\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        "兄たん、パンおいしーね！\x02",
    )

    CloseMessageWindow()

    label("loc_2A70")

    TalkEnd(0xFE)
    Return()

    # Function_7_29DC end

    def Function_8_2A74(): pass

    label("Function_8_2A74")

    EventBegin(0x0)
    Fade(500)
    OP_68(-610, 1000, 9780, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, -1400, 20, 9580, 90)
    SetChrPos(0x102, -2470, 0, 10160, 90)
    SetChrPos(0x109, -2700, 30, 8760, 90)
    SetChrPos(0x105, -3840, 30, 9080, 90)
    OP_4B(0x9, 0xFF)
    OP_0D()

    #C0145
    ChrTalk(
        0x101,
        "#6P#00000Fあの、こんにちは。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)

    #C0146
    ChrTalk(
        0x9,
        (
            "あら、こんにちは。\x01",
            "こんな雨の中、珍しいわね？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            "#6P#00003Fええ、ちょっと\x01",
            "聞きたい事がありまして。\x02\x03",

            "#00000Fこれに見覚えはありませんか？\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0148
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはメイリンの傘を\x01",
            "夫人に見せた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0149
    ChrTalk(
        0x9,
        (
            "あら、これって……\x01",
            "メイリンの傘じゃないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x9,
        "わざわざ届けてくれたの？\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0151
    ChrTalk(
        0x9,
        "あら、でも……\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x9,
        (
            "あの子がパン屋から\x01",
            "帰ったとき、ちゃんと\x01",
            "持ってたと思ったけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        "#6P#00003Fえっと、実はですね……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0154
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは\x01",
            "モモの傘探しをしている\x01",
            "事情を説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0155
    ChrTalk(
        0x9,
        (
            "あらあら、そういう\x01",
            "ことだったのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x9,
        (
            "そのモモって子には\x01",
            "悪い事をしたわねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x105,
        (
            "#6P#10305Fそれで、ご夫人。\x01",
            "お孫さんは今、どこに？\x02\x03",

            "#10300F見たところこちらには\x01",
            "いないようだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x9,
        (
            "ええ、さっきロイと一緒に\x01",
            "傘を差して散歩に行ったみたいなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x9,
        (
            "……ごめんなさい、\x01",
            "そういえば行き先を聞くのを\x01",
            "忘れてしまっていたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x109,
        (
            "#6P#10103Fうーん、どうやら入れ違いに\x01",
            "なっちゃったみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x102,
        (
            "#6P#00100Fこの雨だし、そこまで遠くには\x01",
            "行っていないんじゃないかしら。\x02\x03",

            "#00104F東通りの隣の、\x01",
            "中央広場か港湾区、旧市街……\x01",
            "その辺りだと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x9,
        "ええ、たぶんその辺りじゃないかしら。\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x9,
        (
            "ロイの緑色の傘か、\x01",
            "メイリンのピンク色の傘の\x01",
            "どちらかを探してみるといいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x109,
        (
            "#6P#10100F緑色かピンク色の傘……\x01",
            "確かに目印になりそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x101,
        (
            "#6P#00000Fああ、さっそく捜してみよう。\x02\x03",

            "#00004Fそれでは、ご協力ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x9,
        (
            "いえいえ。\x01",
            "またいつでも来てちょうだいね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -3270, 20, 8130, 225)
    OP_93(0x9, 0x0, 0x0)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x132, 4)
    OP_29(0x6B, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_8_2A74 end

    def Function_9_3098(): pass

    label("Function_9_3098")

    EventBegin(0x0)
    Fade(500)
    OP_68(630, 5020, 6780, 0)
    MoveCamera(44, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18950, 0)
    SetChrPos(0x8, 390, 4019, 5600, 0)
    SetChrPos(0x1A2, -600, 4000, 8580, 180)
    SetChrPos(0x101, 390, 4019, 6840, 180)
    SetChrPos(0x102, 390, 4019, 8320, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_3130")
    SetChrPos(0x104, 1590, 4019, 8580, 180)
    Jump("loc_3169")

    label("loc_3130")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_314F")
    SetChrPos(0x109, 1590, 4019, 8580, 180)
    Jump("loc_3169")

    label("loc_314F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_3169")
    SetChrPos(0x105, 1590, 4019, 8580, 180)

    label("loc_3169")

    OP_4B(0x8, 0xFF)
    OP_0D()

    #C0167
    ChrTalk(
        0x8,
        "#12Pふむ、ロイド君たちじゃないか。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_31B0():

        label("loc_31B0")

        TurnDirection(0xFE, 0x1A2, 500)
        Yield()
        Jump("loc_31B0")

    QueueWorkItem2(0x8, 1, lambda_31B0)
    Sleep(300)

    #C0168
    ChrTalk(
        0x8,
        (
            "#12Pそちらのお子さんは……\x01",
            "東方風の格好をしているが\x01",
            "この辺では見ない顔だね。\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x1A2, 0x0, 0x7D0, 0x7D0, 0x0)
    TurnDirection(0x1A2, 0x8, 500)
    Sleep(300)
    EndChrThread(0x8, 0x1)

    #C0169
    ChrTalk(
        0x1A2,
        (
            "#6Pなるほど、あなたが\x01",
            "クロスベル商工会の会長さんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x1A2,
        (
            "#6Pボクの名前はシン。\x01",
            "《黒月》の将来を背負うオトコです。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x8,
        (
            "#12Pふむ、《黒月》と言うと\x01",
            "最近クロスベルにも\x01",
            "進出してきた東方人街の……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x8,
        (
            "#12P今、将来を背負うと言ったが、\x01",
            "もしかして長老会の関係者なのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x1A2,
        (
            "#6Pええ、そのものズバリ\x01",
            "ボクのおじいさまが長老なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x1A2,
        (
            "#6Pもしかして、\x01",
            "モルス殿は長老たちとご面識が？\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x8,
        (
            "#12Pああいや、商売を通して\x01",
            "軽くやり取りしただけで直接\x01",
            "お会いしたことはないんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x8,
        (
            "#12Pふむ、しかし\x01",
            "長老のお孫さんとだけあって\x01",
            "随分聡明でいらっしゃる。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x8,
        (
            "#12Pだけど、どうしてまた\x01",
            "ロイド君たちと一緒に？\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            "#00009Fいやまあ、\x01",
            "色々と事情がありまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x1A2,
        (
            "#6Pフフ、この者たちが\x01",
            "どうしてもボクに市街を\x01",
            "案内したいと言うものでしてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x1A2,
        (
            "#6P仕方なく付き合ってあげている\x01",
            "トコロなんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_35EE")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_35A1():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_35A1)
    Sleep(50)

    def lambda_35B1():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_35B1)
    Sleep(50)

    def lambda_35C1():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_35C1)
    Sleep(300)

    #C0181
    ChrTalk(
        0x104,
        "#11P#00306Fおいおい……\x02",
    )

    CloseMessageWindow()
    Jump("loc_373B")

    label("loc_35EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_3692")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_3647():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3647)
    Sleep(50)

    def lambda_3657():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3657)
    Sleep(50)

    def lambda_3667():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3667)
    Sleep(300)

    #C0182
    ChrTalk(
        0x109,
        "#11P#10106Fえっと……\x02",
    )

    CloseMessageWindow()
    Jump("loc_373B")

    label("loc_3692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_373B")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_36EB():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36EB)
    Sleep(50)

    def lambda_36FB():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_36FB)
    Sleep(50)

    def lambda_370B():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_370B)
    Sleep(300)

    #C0183
    ChrTalk(
        0x105,
        "#11P#10306Fふぅ、やれやれだね。\x02",
    )

    CloseMessageWindow()

    label("loc_373B")


    #C0184
    ChrTalk(
        0x8,
        (
            "#12Pはは、何だかよく分からないが\x01",
            "仲が良さそうで結構だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x8,
        (
            "#12Pシン君と言ったかな？\x01",
            "どうかクロスベルの街を\x01",
            "気に入ってくれると嬉しいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x1A2,
        (
            "#6Pええ、ボクもそう思います。\x01",
            "ではこれにておイトマを。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 390, 4019, 8320, 0)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x1CA, 0)
    OP_29(0x73, 0x1, 0x7)
    EventEnd(0x5)
    Return()

    # Function_9_3098 end

    SaveToFile()

Try(main)
