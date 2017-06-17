from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1050.bin",                # FileName
        "c1050",                    # MapName
        "c1050",                    # Location
        0x0001,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 2, 0, 3],
    )

    BuildStringList((
        "c1050",                  # 0
        "モルス老人",             # 1
        "モルス老人",             # 2
        "パーラ夫人",             # 3
    ))

    AddCharChip((
        "chr/ch20800.itc",                   # 00
        "chr/ch20900.itc",                   # 01
        "chr/ch20802.itc",                   # 02
    ))

    DeclNpc(569,     4019,    7690,    135,  261,  0x0, 0,   0,   0,   0,   1,   0,   4,   255,  0)
    DeclNpc(-2160,   100,     6829,    90,   389,  0x0, 0,   2,   0,   255, 255, 0,   5,   255,  0)
    DeclNpc(379,     0,       9850,    0,    261,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)

    ScpFunction((
        "Function_0_110",          # 00, 0
        "Function_1_1C8",          # 01, 1
        "Function_2_1F3",          # 02, 2
        "Function_3_346",          # 03, 3
        "Function_4_399",          # 04, 4
        "Function_5_1EAB",         # 05, 5
        "Function_6_2285",         # 06, 6
    ))


    def Function_0_110(): pass

    label("Function_0_110")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_150"),
        (1, "loc_15C"),
        (2, "loc_168"),
        (3, "loc_174"),
        (4, "loc_180"),
        (5, "loc_18C"),
        (6, "loc_198"),
        (SWITCH_DEFAULT, "loc_1A4"),
    )


    label("loc_150")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_15C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_168")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_174")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_180")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_18C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_198")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_1A4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_1B0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1B0")

    label("loc_1C7")

    Return()

    # Function_0_110 end

    def Function_1_1C8(): pass

    label("Function_1_1C8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F2")
    OP_94(0xFE, 0x582, 0x24F4, 0xFFFFFCF4, 0x1306, 0x3E8)
    Sleep(300)
    Jump("Function_1_1C8")

    label("loc_1F2")

    Return()

    # Function_1_1C8 end

    def Function_2_1F3(): pass

    label("Function_2_1F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_221")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, -2200, 30, 8350, 135)
    SetChrFlags(0xA, 0x10)
    Jump("loc_345")

    label("loc_221")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_22F")
    Jump("loc_345")

    label("loc_22F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_23D")
    Jump("loc_345")

    label("loc_23D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_24B")
    Jump("loc_345")

    label("loc_24B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_259")
    Jump("loc_345")

    label("loc_259")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_26C")
    SetChrFlags(0x8, 0x80)
    Jump("loc_345")

    label("loc_26C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_27F")
    SetChrFlags(0x8, 0x80)
    Jump("loc_345")

    label("loc_27F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_292")
    SetChrFlags(0x8, 0x80)
    Jump("loc_345")

    label("loc_292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2A5")
    SetChrFlags(0x8, 0x80)
    Jump("loc_345")

    label("loc_2A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2BD")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    Jump("loc_345")

    label("loc_2BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2D0")
    SetChrFlags(0x8, 0x80)
    Jump("loc_345")

    label("loc_2D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2E8")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    Jump("loc_345")

    label("loc_2E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2F6")
    Jump("loc_345")

    label("loc_2F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_304")
    Jump("loc_345")

    label("loc_304")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_312")
    Jump("loc_345")

    label("loc_312")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_320")
    Jump("loc_345")

    label("loc_320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_32E")
    Jump("loc_345")

    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_33C")
    Jump("loc_345")

    label("loc_33C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_345")

    label("loc_345")

    Return()

    # Function_2_1F3 end

    def Function_3_346(): pass

    label("Function_3_346")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35F")
    OP_10(0x0, 0x0)
    OP_10(0x1, 0x1)
    Jump("loc_365")

    label("loc_35F")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)

    label("loc_365")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_381")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_398")

    label("loc_381")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_398")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_398")

    label("loc_398")

    Return()

    # Function_3_346 end

    def Function_4_399(): pass

    label("Function_4_399")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9F4")
    TurnDirection(0x8, 0x101, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4E7")

    #C0001
    ChrTalk(
        0xFE,
        (
            "……おお、君はたしか\x01",
            "一度鉄道で同じの席になったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        (
            "#0002Fああ、あの時のお爺さん！\x01",
            "……ハハ、久し振りだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        "うむうむ、かれこれ二ヶ月になるか。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "そういえばあの時は\x01",
            "初出勤に行くと言っておったが。\x01",
            "仕事の方は順調かね？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        (
            "#0000Fうん、何とか。\x01",
            "最近ようやく慣れてきた所だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_699")

    label("loc_4E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_616")

    #C0006
    ChrTalk(
        0xFE,
        (
            "……おお、君はたしか\x01",
            "一度鉄道で同じの席になったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#0002Fああ、あの時のお爺さん！\x01",
            "……ハハ、久し振りだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "うむうむ、かれこれ一ヶ月ぶりか。\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "そういえばあの時は\x01",
            "初出勤に行くと言っておったが。\x01",
            "仕事の方は順調かね？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#0000Fうん、何とか。\x01",
            "最近ようやく慣れてきた所だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_699")

    label("loc_616")


    #C0011
    ChrTalk(
        0xFE,
        "……おお、君はあの時の。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "初出勤はどうじゃったかね？\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#0012Fええ、まあ、ははは……\x01",
            "ようやく本番開始ってカンジかな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_699")


    #C0014
    ChrTalk(
        0xFE,
        (
            "ほっほ、どうやら\x01",
            "同期の仲間と一緒のようじゃな。\x01",
            "若い者が揃って、中々壮観じゃわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "まあわしにできる事も少なかろうが\x01",
            "何かあれば相談に来てくれい。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "わしも若い頃は商売をしておってな、\x01",
            "それなりの人脈はあるんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#0005Fへえ、そうだったんだ。\x02\x03",

            "#0000Fちなみにお知り合いって、\x01",
            "具体的にはどんな人が……？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        "ふむ、そうじゃな。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "クロスベル市長とか\x01",
            "貿易商組合の取り纏めとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "あとはウルスラ医科大学の\x01",
            "理事長なんかも親友じゃな。\x02",
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

    #C0021
    ChrTalk(
        0x104,
        (
            "#0303F……ロイド、何だか\x01",
            "大物臭い人なんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        "#0006Fあのう、お爺さんは一体……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "ふふ、わしは\x01",
            "クロスベル商工会の\x01",
            "会長をやっておる。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "まあ堅くならんでも良いぞ。\x01",
            "大した仕事ではないからのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        "#0200F（そうは見えないですが……）\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x102,
        (
            "#0104F（商工会のモルス会長……\x01",
            "  そう、この人が。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4F, 4)
    Jump("loc_1EA7")

    label("loc_9F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_A02")
    Jump("loc_1EA7")

    label("loc_A02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B0D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AAA")

    #C0027
    ChrTalk(
        0xFE,
        (
            "昨日の事件に続き、\x01",
            "空港の方でも\x01",
            "トラブルがあったそうじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "ふむ、ここの所\x01",
            "事件が続くのう……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "議会どころではないかもしれんぞ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B08")

    label("loc_AAA")


    #C0030
    ChrTalk(
        0xFE,
        (
            "商人というのは\x01",
            "街の空気に敏感なものじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "……どうも近頃は\x01",
            "気になる事件が多いわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B08")

    Jump("loc_1EA7")

    label("loc_B0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_BB1")

    #C0032
    ChrTalk(
        0xFE,
        (
            "今朝発売の\x01",
            "クロスベルタイムズ最新刊が\x01",
            "届いておらんのじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "婆さんに聞いても\x01",
            "知らぬというが……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "はて、臨時休刊でも\x01",
            "しておるのかのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EA7")

    label("loc_BB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_CE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C7A")

    #C0035
    ChrTalk(
        0xFE,
        (
            "自治州議会は案の定\x01",
            "会期延長となったのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "このまま纏まらねば\x01",
            "予算が執行できん……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "むむむ、やってくれるのう。\x01",
            "このままでは市民の生活にも\x01",
            "悪影響が出てしまうぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CDE")

    label("loc_C7A")


    #C0038
    ChrTalk(
        0xFE,
        (
            "むむむ、やはり\x01",
            "ハルトマン議長は妥協せんか……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "そうなると議会は\x01",
            "さらに長引くじゃろうな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CDE")

    Jump("loc_1EA7")

    label("loc_CE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1526")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11C9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1011")

    #C0040
    ChrTalk(
        0xFE,
        (
            "おや……ロイド君たちか。\x01",
            "記念祭では世話になったのう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xE)"), scpexpr(EXPR_END)), "loc_E91")

    #C0041
    ChrTalk(
        0x101,
        (
            "#0000Fいえ、大したことじゃ。\x01",
            "警察官としては当然の事ですから。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_DD9")

    #C0042
    ChrTalk(
        0x102,
        "#0100Fともかく解決できて良かったです。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E5B")

    label("loc_DD9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E23")

    #C0043
    ChrTalk(
        0x103,
        (
            "#0204Fまあわたしたちの\x01",
            "実力という奴でしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5B")

    label("loc_E23")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E5B")

    #C0044
    ChrTalk(
        0x104,
        "#0304Fま、噂の特務支援課ッスから。\x02",
    )

    CloseMessageWindow()

    label("loc_E5B")


    #C0045
    ChrTalk(
        0xFE,
        (
            "ふふ、相変わらず\x01",
            "元気にやっとるようじゃな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_FB1")

    label("loc_E91")


    #C0046
    ChrTalk(
        0x101,
        (
            "#0006Fあの時は\x01",
            "あんまりお役に立てなくって。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EFB")

    #C0047
    ChrTalk(
        0x102,
        "#0103Fご心配をお掛けしました。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F62")

    label("loc_EFB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F38")

    #C0048
    ChrTalk(
        0x103,
        "#0203F……ご心配をお掛けしました。\x02",
    )

    CloseMessageWindow()
    Jump("loc_F62")

    label("loc_F38")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F62")

    #C0049
    ChrTalk(
        0x104,
        "#0306F面目ねえッス。\x02",
    )

    CloseMessageWindow()

    label("loc_F62")


    #C0050
    ChrTalk(
        0xFE,
        (
            "いやいや、全力で捜査してくれただけでも\x01",
            "市民の身としては嬉しいものじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB1")


    #C0051
    ChrTalk(
        0xFE,
        (
            "ところで……ふむ。\x01",
            "今日は小さい子を連れておるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        "これから交番にでも行くのかね？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1092")

    label("loc_1011")


    #C0053
    ChrTalk(
        0xFE,
        (
            "おや……ロイド君か。\x01",
            "久し振りじゃのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "ふむ……今日は小さい子を\x01",
            "連れておるようじゃな。\x01",
            "これから交番にでも行くのかね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1092")


    #C0055
    ChrTalk(
        0x101,
        (
            "#0000Fええとまあ、そんな所です。\x01",
            "この子の身元を当たってみようかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        "そうかそうか。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x153, 500)
    Sleep(300)

    #C0057
    ChrTalk(
        0xFE,
        (
            "お嬢ちゃん、大通りでは\x01",
            "導力車に気を付けるんじゃぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        "飛び出し厳禁じゃ。\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x153,
        (
            "#1111Fトビダシゲンキン……\x02\x03",

            "#1109Fうん、わかったー。\x01",
            "トビダシゲンキンだねー！\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        "ほっほ、覚えのよい子じゃのう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBF, 7)
    Jump("loc_1521")

    label("loc_11C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_149C")

    #C0061
    ChrTalk(
        0xFE,
        (
            "さて明日からは\x01",
            "自治州議会が始まるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "ふむ、また帝国派と共和国派で\x01",
            "揉めることになろうな……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "マクダエル市長の心労は\x01",
            "察してあまりあるわい。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1494")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1352")

    #C0064
    ChrTalk(
        0x101,
        (
            "#0003F（会長さん……エリィのお祖父さんの事を\x01",
            "  心配してるみたいだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x102,
        (
            "#0100F（お２人は以前から\x01",
            "  ちょっとした親交があるのよ。）\x02\x03",

            "#0108F（……私も…………\x01",
            "  議会の事は少し心配ね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1494")

    label("loc_1352")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13FC")

    #C0066
    ChrTalk(
        0x103,
        (
            "#0203F（会長さん、エリィさんの\x01",
            "  お祖父様のことを\x01",
            "  心配しているようですね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#0000F（エリィによると\x01",
            "  お２人は親交があるらしいからね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1494")

    label("loc_13FC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1494")

    #C0068
    ChrTalk(
        0x104,
        (
            "#0303F（会長さん、お嬢のジイ様のことを\x01",
            "  心配してるみてえだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#0000F（エリィによると\x01",
            "  お２人は親交があるらしいからね。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1494")

    SetScenarioFlags(0x0, 0)
    Jump("loc_1521")

    label("loc_149C")


    #C0070
    ChrTalk(
        0xFE,
        (
            "まともな政治家は\x01",
            "あのマクダエル市長しか\x01",
            "おらんという状況じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "議会は荒れるじゃろうが……\x01",
            "わしらは見守るしかないんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1521")

    Jump("loc_1EA7")

    label("loc_1526")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_1534")
    Jump("loc_1EA7")

    label("loc_1534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1542")
    Jump("loc_1EA7")

    label("loc_1542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_16BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_162A")

    #C0072
    ChrTalk(
        0xFE,
        (
            "来月には\x01",
            "めでたい記念祭があるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "しかし、忘れてはいかんのは\x01",
            "その１週間後にある\x01",
            "自治州議会じゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "州政１年の計を決める大切な議会……\x01",
            "議員どもが私物化せんように\x01",
            "わしらも見守ってやらんとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16B9")

    label("loc_162A")


    #C0075
    ChrTalk(
        0xFE,
        (
            "記念祭の後には\x01",
            "予算議会が控えておる。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "ふむ……中立派の市長にとっては\x01",
            "まさに正念場になるじゃろう。\x01",
            "わしらもしっかり見守ってやらねば。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16B9")

    Jump("loc_1EA7")

    label("loc_16BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_17D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1771")

    #C0077
    ChrTalk(
        0xFE,
        (
            "ルバーチェの連中は\x01",
            "保釈されてしまったか……\x01",
            "相変わらず腹の立つ話じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "わしは政治には踏み込まんと\x01",
            "決めておるんじゃが、\x01",
            "それだけに歯痒いわい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17D3")

    label("loc_1771")


    #C0079
    ChrTalk(
        0xFE,
        (
            "クロスベルの政治は\x01",
            "ミラと権力に塗れておる。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "やれやれ……毎度毎度\x01",
            "失望させてくれるわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D3")

    Jump("loc_1EA7")

    label("loc_17D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1934")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C5")

    #C0081
    ChrTalk(
        0xFE,
        (
            "露店街にディンズ君という\x01",
            "野菜売りがおるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "以前世話をしてやった事があってな、\x01",
            "それ以来顔を出してくれるんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "ふふ、変わらず誠実な\x01",
            "商売を続けているとみえる。\x01",
            "若い者には頑張って欲しいのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_192F")

    label("loc_18C5")


    #C0084
    ChrTalk(
        0xFE,
        (
            "若い商人を育てるのも\x01",
            "わしら年寄りの仕事じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "ふふ、誠実な商売を\x01",
            "続けているようで何よりじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_192F")

    Jump("loc_1EA7")

    label("loc_1934")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1A9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A58")

    #C0086
    ChrTalk(
        0xFE,
        "さて、今晩は会合に出ねばならん。\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "総会を取りまとめて\x01",
            "決算書を出して。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "創立記念祭も近づいておるし\x01",
            "後日市長ともお話をせねばのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#0000Fはは……やっぱり会長だと\x01",
            "何かと忙しいみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "そうなんじゃ。\x01",
            "この歳になっても\x01",
            "毎日仕事で一杯じゃわい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A95")

    label("loc_1A58")


    #C0091
    ChrTalk(
        0xFE,
        (
            "今晩は商工会の会合があってな。\x01",
            "何かと準備に忙しいわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A95")

    Jump("loc_1EA7")

    label("loc_1A9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1C17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B92")

    #C0092
    ChrTalk(
        0xFE,
        (
            "クロスベルの商人は\x01",
            "いがみ合ってきたばかりではないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "この東通りには昔から商人同士の\x01",
            "ネットワークがあって、\x01",
            "助け合ってきたんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "ま、いつの間にか\x01",
            "『クロスベル商工会』という\x01",
            "名前になってしまったがのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C12")

    label("loc_1B92")


    #C0095
    ChrTalk(
        0xFE,
        (
            "クロスベル商工会は\x01",
            "東通りの露店から生まれたんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "今ではクロスベル全体に広がったが\x01",
            "その心は受け継いでおるんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C12")

    Jump("loc_1EA7")

    label("loc_1C17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1D29")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CDE")

    #C0097
    ChrTalk(
        0xFE,
        (
            "今日は古い友人と\x01",
            "会う約束があるんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "昔の商人仲間の付き合いでな。\x01",
            "引退した今でも\x01",
            "親しくやり取りしておるんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "ふふ、東通りの商人は\x01",
            "情に厚いからのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D24")

    label("loc_1CDE")


    #C0100
    ChrTalk(
        0xFE,
        (
            "今日は古い友人と\x01",
            "会う約束があるんじゃ。\x01",
            "そろそろ支度をせんとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D24")

    Jump("loc_1EA7")

    label("loc_1D29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1EA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E2F")

    #C0101
    ChrTalk(
        0xFE,
        (
            "今では商工会なんぞに\x01",
            "収まっているが、わしも若い頃は\x01",
            "表の市場に露店を出しておってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "ふふ、露天商時代の人脈が\x01",
            "いまでも役に立っておるだけなんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "ま、何かあれば相談に来てくれい。\x01",
            "わしも話し相手が\x01",
            "できて嬉しいからのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1EA7")

    label("loc_1E2F")


    #C0104
    ChrTalk(
        0xFE,
        (
            "君らと知り合ったのも何かの縁、\x01",
            "困ったことがあったら相談に来てくれい。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "わしも話し相手が\x01",
            "できて嬉しいからのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EA7")

    TalkEnd(0xFE)
    Return()

    # Function_4_399 end

    def Function_5_1EAB(): pass

    label("Function_5_1EAB")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F3F")
    Jump("loc_1F89")

    label("loc_1F3F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1F5F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F89")

    label("loc_1F5F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1F7F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1F89")

    label("loc_1F7F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F89")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_20EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_207A")

    #C0106
    ChrTalk(
        0xFE,
        (
            "自治州議会が\x01",
            "ようやく終わったそうじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "ふむ……速報しか聞いておらんが\x01",
            "まずまず、といった所か。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "帝国派、共和国派に阻まれつつも\x01",
            "マクダエル市長は健闘なさったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20E6")

    label("loc_207A")


    #C0109
    ChrTalk(
        0xFE,
        (
            "自治州議会が\x01",
            "ようやく終わったそうじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "いまの派閥政治を考えれば\x01",
            "市長も健闘なさった方じゃろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20E6")

    Jump("loc_227D")

    label("loc_20EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_227D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_221E")

    #C0111
    ChrTalk(
        0xFE,
        (
            "ＩＢＣといえば\x01",
            "クロスベルが誇る\x01",
            "世界最大の国際銀行じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "ふふ、優秀なクロスベル商人の中でも\x01",
            "ＩＢＣの成功は最たるものじゃろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "歴代優秀な総裁が任につき、\x01",
            "巧みな舵取りによって\x01",
            "激動の時代すら乗り越えてきた銀行。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "ＩＢＣはわしらにとっても\x01",
            "一つの誇りなんじゃよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_227D")

    label("loc_221E")


    #C0115
    ChrTalk(
        0xFE,
        "ＩＢＣは世界最大の国際銀行じゃ。\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "クロスベル市民にとって\x01",
            "誇りと言って良いじゃろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_227D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_5_1EAB end

    def Function_6_2285(): pass

    label("Function_6_2285")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2402")
    TurnDirection(0xFE, 0x101, 0)
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0117
    ChrTalk(
        0xFE,
        (
            "あら、あなた。\x01",
            "確か鉄道で同じ席になった……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#0005Fあ、あの時のお婆さん……！？\x02\x03",

            "そっか、家は東通りって\x01",
            "言っていたけど……\x01",
            "ここだったんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "ふふ、あの時は\x01",
            "荷物を運んでくれたのよね。\x01",
            "若いのに感心な人だこと。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "そうそう、\x01",
            "おじいさんなら上にいますよ。\x01",
            "良かったら会ってらっしゃい。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        "#0000Fええ、喜んで。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x4F, 5)
    Jump("loc_3B5E")

    label("loc_2402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2462")

    #C0122
    ChrTalk(
        0xFE,
        (
            "ほらほらおじいさん、\x01",
            "政治のお話ばかりしてないで\x01",
            "早く召し上がってくださいな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B5E")

    label("loc_2462")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2590")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_251B")

    #C0123
    ChrTalk(
        0xFE,
        (
            "商人さんたちの噂では、\x01",
            "取引していた貿易商の方が\x01",
            "何人か行方不明だと聞きましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "どうしたのかしらね、\x01",
            "そろって外国に商談にでも\x01",
            "行っているのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_258B")

    label("loc_251B")


    #C0125
    ChrTalk(
        0xFE,
        (
            "商人さんたちの噂は\x01",
            "早いし正確なのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "朝から何人か行方不明だなんて\x01",
            "少しおかしな話だとは思うけれど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_258B")

    Jump("loc_3B5E")

    label("loc_2590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2617")

    #C0127
    ChrTalk(
        0xFE,
        (
            "おじいさんはいつも\x01",
            "議会の動向を気にしているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "だからクロスベルタイムズが\x01",
            "届いていないと\x01",
            "落ち着かないのよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B5E")

    label("loc_2617")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2759")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26EB")

    #C0129
    ChrTalk(
        0xFE,
        (
            "おじいさんったら\x01",
            "今日もクロスベルタイムズと\x01",
            "睨めっこしているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "議会が開かれている間は\x01",
            "毎年こうなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "難しいお話を\x01",
            "聞かされたくなかったら\x01",
            "近づかない方がいいですよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2754")

    label("loc_26EB")


    #C0132
    ChrTalk(
        0xFE,
        (
            "おじいさんは\x01",
            "毎年こうなのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "難しいお話を\x01",
            "聞かされたくなかったら\x01",
            "近づかない方がいいですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2754")

    Jump("loc_3B5E")

    label("loc_2759")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2E32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 7)), scpexpr(EXPR_END)), "loc_2C61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A6C")

    #C0134
    ChrTalk(
        0xFE,
        (
            "あら……？\x01",
            "今日は可愛らしいお客さんが\x01",
            "一緒みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x153,
        "#1110Fこんにちはー！\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        "うふふ、元気な挨拶だこと。\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#0000Fキーアといって、しばらく\x01",
            "支援課で預かっている子なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "そうだったの。\x01",
            "何か事情があるみたいねぇ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0139
    ChrTalk(
        0xFE,
        (
            "そうだわ、キーアちゃん。\x01",
            "今日はこれを\x01",
            "持って行きなさいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        (
            "うちは酒屋だったから\x01",
            "ジュースは少ないんだけど……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0141
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1CF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を貰った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1CF, 1)

    #C0142
    ChrTalk(
        0x153,
        "#1105Fわー、いいのー？\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "ええ、もちろんよ。\x01",
            "疲れた時におあがりなさいな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_29CE")

    #C0144
    ChrTalk(
        0x102,
        (
            "#0100Fすみません、\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A40")

    label("loc_29CE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A12")

    #C0145
    ChrTalk(
        0x103,
        (
            "#0200Fすみません、\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A40")

    label("loc_2A12")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A40")

    #C0146
    ChrTalk(
        0x104,
        "#0300Fはは、悪いっすね。\x02",
    )

    CloseMessageWindow()

    label("loc_2A40")


    #C0147
    ChrTalk(
        0x153,
        "#1109Fありがと、おばーちゃん！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBF, 5)
    Jump("loc_2C5C")

    label("loc_2A6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BF0")

    #C0148
    ChrTalk(
        0xFE,
        (
            "そういえば……あなたたちなら\x01",
            "聞いた事があるかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "記念祭の最後の日に\x01",
            "ミシュラムで\x01",
            "事件があったそうなんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "アーケード街に\x01",
            "魔獣が出たという話だったけど……\x01",
            "その後の噂をとんと聞かないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "怪我人は出なかったのかしら。\x01",
            "何だか心配してしまうわねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x153,
        "#1111F………………？？？\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x101,
        (
            "#0000Fははは……\x01",
            "（一通り報道規制が\x01",
            "  掛かったみたいだしな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C5C")

    label("loc_2BF0")


    #C0154
    ChrTalk(
        0xFE,
        (
            "ミシュラムに魔獣が出るなんて\x01",
            "大きく報道されそうだけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "やっぱりただの\x01",
            "噂だったのかしらねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C5C")

    Jump("loc_2E2D")

    label("loc_2C61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CF6")

    #C0156
    ChrTalk(
        0xFE,
        (
            "あら……？\x01",
            "可愛らしいお客さんが\x01",
            "一緒みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "ふふ、ゆっくりしていきなさいな。\x01",
            "今日はお爺さんも帰っていますからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBF, 5)
    Jump("loc_2E2D")

    label("loc_2CF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DC1")

    #C0158
    ChrTalk(
        0xFE,
        (
            "記念祭の最後の日に\x01",
            "ミシュラムで\x01",
            "事件があったそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "アーケード街に\x01",
            "魔獣が出たという話だったけど……\x01",
            "怪我人は出なかったのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "あまり事件の噂を\x01",
            "聞かないわねえ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2E2D")

    label("loc_2DC1")


    #C0161
    ChrTalk(
        0xFE,
        (
            "ミシュラムに魔獣が出るなんて\x01",
            "大きく報道されそうだけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "やっぱりただの\x01",
            "噂だったのかしらねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E2D")

    Jump("loc_3B5E")

    label("loc_2E32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2EA4")

    #C0163
    ChrTalk(
        0xFE,
        (
            "あらあら、\x01",
            "あなたたちもお出掛け？\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "気を付けるんですよ。\x01",
            "今日はどこも混雑していますからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B5E")

    label("loc_2EA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2F86")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F1F")

    #C0165
    ChrTalk(
        0xFE,
        (
            "ロイ君とメイリンちゃん\x01",
            "随分大きくなったのねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "今日はうちに\x01",
            "泊まっていけばいいのに。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F81")

    label("loc_2F1F")


    #C0167
    ChrTalk(
        0xFE,
        (
            "久々に孫の顔を見ると\x01",
            "ほっとするわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "今日はお婆ちゃんのおうちに\x01",
            "泊めてあげましょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F81")

    Jump("loc_3B5E")

    label("loc_2F86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3067")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FF6")

    #C0169
    ChrTalk(
        0xFE,
        "今日はパレードがあるでしょう？\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "何か飲み物でも\x01",
            "用意しておこうかとおもって。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3062")

    label("loc_2FF6")


    #C0171
    ChrTalk(
        0xFE,
        (
            "ふふ、商工会の皆さんの分も\x01",
            "用意しておきましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xFE,
        (
            "皆さんいつまでたっても\x01",
            "甘えん坊なんですから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3062")

    Jump("loc_3B5E")

    label("loc_3067")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_315C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30F3")

    #C0173
    ChrTalk(
        0xFE,
        (
            "お爺さんは今日も\x01",
            "商工会のテントに行っているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "後輩達の事が\x01",
            "気になるみたいよ。\x01",
            "ふふ、仕方がない人ね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3157")

    label("loc_30F3")


    #C0175
    ChrTalk(
        0xFE,
        (
            "あとでお弁当でも\x01",
            "持って行ってあげましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "きっとお喋りに夢中に\x01",
            "なってるでしょうから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3157")

    Jump("loc_3B5E")

    label("loc_315C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_31FD")

    #C0177
    ChrTalk(
        0xFE,
        (
            "おじいさんなら\x01",
            "出かけてしまっていますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "商工会の寄り合いでね、\x01",
            "記念祭の準備を進めているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "ふふ、年甲斐もなく\x01",
            "張り切っていたわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B5E")

    label("loc_31FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3380")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32F5")

    #C0180
    ChrTalk(
        0xFE,
        "ふふ、ＩＢＣといえば……\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "たしかクロイス総裁は\x01",
            "マクダエル市長の息子さんと\x01",
            "ご親友だったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "市長の息子さんは\x01",
            "以前政治家をしていたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "２人とも娘さんがいて……\x01",
            "娘さん同士も\x01",
            "ご親友じゃなかったかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_337B")

    label("loc_32F5")


    #C0184
    ChrTalk(
        0xFE,
        (
            "クロイス総裁は\x01",
            "マクダエル市長の息子さんと\x01",
            "ご親友だったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "２人とも娘さんがいて、\x01",
            "娘さん同士も\x01",
            "ご親友じゃなかったかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_337B")

    Jump("loc_3B5E")

    label("loc_3380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_34B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3462")

    #C0186
    ChrTalk(
        0xFE,
        (
            "クロスベルにやってきた\x01",
            "新しい遊撃士さんたち、\x01",
            "とても頑張っているみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "エステルさんと\x01",
            "ヨシュアさんだったかしら。\x01",
            "東通りではもう有名人なのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "若い人の活躍を\x01",
            "見るのは楽しいものね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_34B2")

    label("loc_3462")


    #C0189
    ChrTalk(
        0xFE,
        (
            "新しい遊撃士さんたちも\x01",
            "活躍しているみたいね。\x01",
            "確か雑誌にも載っていたのよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34B2")

    Jump("loc_3B5E")

    label("loc_34B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_35D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_356C")

    #C0190
    ChrTalk(
        0xFE,
        (
            "記念祭が近づくと\x01",
            "街が華やかになっていくわねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "どのお店もお祭りの準備を始めて、\x01",
            "私たちもそれを楽しみにして。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        "まるで心が躍りだすようだわ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_35CC")

    label("loc_356C")


    #C0193
    ChrTalk(
        0xFE,
        (
            "記念祭が近づくと\x01",
            "街が徐々に華やいでいくの。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "ふふ、毎年この時期は\x01",
            "本当に楽しいわねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35CC")

    Jump("loc_3B5E")

    label("loc_35D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3666")

    #C0195
    ChrTalk(
        0xFE,
        (
            "今朝は腰痛が酷くって。\x01",
            "食材は馴染みの商人さんに頼んで\x01",
            "届けてもらったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "ふふ、おじいさんの人脈も\x01",
            "たまには役に立つのねえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B5E")

    label("loc_3666")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_379F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3752")

    #C0197
    ChrTalk(
        0xFE,
        (
            "あらあなた達……\x01",
            "疲れた顔をしてるけど大丈夫？\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x102,
        "#0100Fあはは……平気です。\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x103,
        (
            "#0200Fええ、同じく……\x01",
            "少し休みましたから。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 7)), scpexpr(EXPR_END)), "loc_374A")

    #C0200
    ChrTalk(
        0x101,
        (
            "#0000Fおばさん、\x01",
            "レモネードありがとう。\x01",
            "とっても役に立ったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_374A")

    SetScenarioFlags(0x0, 1)
    Jump("loc_379A")

    label("loc_3752")


    #C0201
    ChrTalk(
        0xFE,
        (
            "疲れたのなら言って頂戴ね。\x01",
            "またレモネードを\x01",
            "振舞ってあげますから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_379A")

    Jump("loc_3B5E")

    label("loc_379F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_39DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3992")

    #C0202
    ChrTalk(
        0xFE,
        (
            "あらあら、\x01",
            "若い人たちがたくさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "どうしたの、\x01",
            "みんなしてお出掛け？\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x101,
        (
            "#0000Fええ、ちょっと仕事で。\x01",
            "アルモリカ村の方に\x01",
            "行ってくる所なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xFE,
        "あらあら、大変ねえ。\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0206
    ChrTalk(
        0xFE,
        (
            "そうだ、それだったら\x01",
            "これを持って行きなさいな。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0207
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x336),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を貰った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x336, 1)

    #C0208
    ChrTalk(
        0x101,
        (
            "#0000F凍らせたレモネード……\x01",
            "確か前に飲ませてくれたヤツだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0xFE,
        (
            "飲むと元気になるから\x01",
            "途中でお上がりなさいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x104,
        "#0300Fはは、了解っす。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6C, 7)
    Jump("loc_39D5")

    label("loc_3992")


    #C0211
    ChrTalk(
        0xFE,
        (
            "ささ、早く行ってらっしゃいな。\x01",
            "日が暮れてしまわないうちにね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39D5")

    Jump("loc_3B5E")

    label("loc_39DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3AD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A87")

    #C0212
    ChrTalk(
        0xFE,
        (
            "この辺りの通りは\x01",
            "いつも騒がしいでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "でも慣れてしまうと、喧騒がないと\x01",
            "寂しい気がしてしまうものなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        "ふふ、困ったものねえ……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3AD1")

    label("loc_3A87")


    #C0215
    ChrTalk(
        0xFE,
        (
            "表の喧騒も、ないと\x01",
            "寂しい気がしてしまうの。\x01",
            "ふふ、困ったものねえ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AD1")

    Jump("loc_3B5E")

    label("loc_3AD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_3B5E")

    #C0216
    ChrTalk(
        0xFE,
        (
            "ふふ、若い人と知り合うと\x01",
            "何だか楽しいものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "よかったらまた寄って頂戴。\x01",
            "何かおいしい物でも\x01",
            "用意しておきますからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B5E")

    TalkEnd(0xFE)
    Return()

    # Function_6_2285 end

    SaveToFile()

Try(main)
