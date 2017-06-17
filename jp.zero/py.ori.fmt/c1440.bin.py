from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1440.bin",                # FileName
        "c1440",                    # MapName
        "c1440",                    # Location
        0x0031,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 49, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1440",                  # 0
        "アシュリー",             # 1
        "ジンゴ",                 # 2
        "シスター・ハティナ",     # 3
        "遊撃士リン",             # 4
        "遊撃士エオリア",         # 5
        "ガルシア",               # 6
    ))

    AddCharChip((
        "chr/ch09200.itc",                   # 00
        "chr/ch23900.itc",                   # 01
        "chr/ch25500.itc",                   # 02
        "chr/ch32000.itc",                   # 03
        "chr/ch32100.itc",                   # 04
    ))

    DeclNpc(-2859,   0,       13750,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(5670,    29,      8649,    225,  261,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(2930,    0,       7659,    315,  389,  0x0, 0,   2,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-2170,   19,      5400,    180,  389,  0x0, 0,   3,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-2170,   29,      4110,    0,    389,  0x0, 0,   4,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 17,  9.899999618530273,     14.0,                  -0.5,                  16.0,                  [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -2.4749999046325684,   -7.0,                  0.10000000149011612,   1.0])

    DeclActor(4590,    0,       7540,    1000,    5670,    1500,    8650,    0x007E, 0,  9,  0x0000)

    ScpFunction((
        "Function_0_21C",          # 00, 0
        "Function_1_2D4",          # 01, 1
        "Function_2_3FE",          # 02, 2
        "Function_3_451",          # 03, 3
        "Function_4_25CB",         # 04, 4
        "Function_5_2A19",         # 05, 5
        "Function_6_2BFC",         # 06, 6
        "Function_7_2E98",         # 07, 7
        "Function_8_30D7",         # 08, 8
        "Function_9_378F",         # 09, 9
        "Function_10_3793",        # 0A, 10
        "Function_11_4F97",        # 0B, 11
        "Function_12_5353",        # 0C, 12
        "Function_13_5897",        # 0D, 13
        "Function_14_5998",        # 0E, 14
        "Function_15_5AB0",        # 0F, 15
        "Function_16_5CC5",        # 10, 16
        "Function_17_63F9",        # 11, 17
    ))


    def Function_0_21C(): pass

    label("Function_0_21C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_25C"),
        (1, "loc_268"),
        (2, "loc_274"),
        (3, "loc_280"),
        (4, "loc_28C"),
        (5, "loc_298"),
        (6, "loc_2A4"),
        (SWITCH_DEFAULT, "loc_2B0"),
    )


    label("loc_25C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_268")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_274")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_280")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_28C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_298")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_2A4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_2B0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_2BC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2BC")

    label("loc_2D3")

    Return()

    # Function_0_21C end

    def Function_1_2D4(): pass

    label("Function_1_2D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EA")
    Event(0, 16)

    label("loc_2EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2F8")
    Jump("loc_3FD")

    label("loc_2F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_310")
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jump("loc_3FD")

    label("loc_310")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_31E")
    Jump("loc_3FD")

    label("loc_31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_351")
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x8, 1850, 0, 8750, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34C")
    SetChrFlags(0x8, 0x10)

    label("loc_34C")

    Jump("loc_3FD")

    label("loc_351")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_364")
    SetChrFlags(0x8, 0x80)
    Jump("loc_3FD")

    label("loc_364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_372")
    Jump("loc_3FD")

    label("loc_372")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_391")
    SetChrPos(0x8, 1810, 0, 10210, 135)
    Jump("loc_3FD")

    label("loc_391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_39F")
    Jump("loc_3FD")

    label("loc_39F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3B2")
    SetChrFlags(0x8, 0x80)
    Jump("loc_3FD")

    label("loc_3B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3C0")
    Jump("loc_3FD")

    label("loc_3C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3EE")
    SetChrPos(0x8, -1940, 30, 10250, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E9")
    SetChrFlags(0x8, 0x10)

    label("loc_3E9")

    Jump("loc_3FD")

    label("loc_3EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FD")
    SetChrFlags(0x8, 0x10)

    label("loc_3FD")

    Return()

    # Function_1_2D4 end

    def Function_2_3FE(): pass

    label("Function_2_3FE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_417")
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x1)
    Jump("loc_41D")

    label("loc_417")

    OP_10(0x0, 0x1)
    OP_10(0x3, 0x0)

    label("loc_41D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_439")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_450")

    label("loc_439")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_450")
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    Jump("loc_450")

    label("loc_450")

    Return()

    # Function_2_3FE end

    def Function_3_451(): pass

    label("Function_3_451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E7")
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_491")
    Call(0, 7)
    SetScenarioFlags(0x6B, 3)
    Jump("loc_5DF")

    label("loc_491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_4A2")
    Call(0, 4)
    Jump("loc_5DF")

    label("loc_4A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4B6")
    Call(0, 7)
    SetScenarioFlags(0x6B, 3)
    Jump("loc_5DF")

    label("loc_4B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_537")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_52F")

    #C0001
    ChrTalk(
        0x8,
        (
            "最近シスターが\x01",
            "しつこく訪ねてきやがるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "ったく煩い女だな。\x01",
            "舌引っこ抜いてやろうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_532")

    label("loc_52F")

    Call(0, 5)

    label("loc_532")

    Jump("loc_5DF")

    label("loc_537")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_545")
    Jump("loc_5DF")

    label("loc_545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_559")
    Call(0, 7)
    SetScenarioFlags(0x6B, 3)
    Jump("loc_5DF")

    label("loc_559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_590")

    #C0003
    ChrTalk(
        0x8,
        (
            "さてと、例のブツの\x01",
            "在庫整理はと……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5DF")

    label("loc_590")


    #C0004
    ChrTalk(
        0x8,
        "やれやれ、また新商品かい。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "チッ……商品管理の\x01",
            "手間が増えちまうねェ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5DF")

    TalkEnd(0xFE)
    Jump("loc_25CA")

    label("loc_5E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_602")
    Call(0, 7)
    Jump("loc_6CD")

    label("loc_602")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_613")
    Call(0, 4)
    Jump("loc_6CD")

    label("loc_613")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_624")
    Call(0, 7)
    Jump("loc_6CD")

    label("loc_624")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_6AB")
    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_6A0")

    #C0006
    ChrTalk(
        0x8,
        (
            "最近シスターが\x01",
            "しつこく訪ねてきやがるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "ったく煩い女だな。\x01",
            "舌引っこ抜いてやろうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6A3")

    label("loc_6A0")

    Call(0, 5)

    label("loc_6A3")

    TalkEnd(0xFE)
    Jump("loc_6CD")

    label("loc_6AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_6B9")
    Jump("loc_6CD")

    label("loc_6B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_6CA")
    Call(0, 7)
    Jump("loc_6CD")

    label("loc_6CA")

    Call(0, 8)

    label("loc_6CD")

    Jump("loc_25CA")

    label("loc_6D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6F4")
    Call(0, 6)
    Jump("loc_25CA")

    label("loc_6F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_87A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_775")

    #C0008
    ChrTalk(
        0x8,
        "空港に爆破予告が届いてるんだって？\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "クク、どこの誰だか知らないが\x01",
            "派手にぶち上げるじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_875")

    label("loc_775")


    #C0010
    ChrTalk(
        0x8,
        "空港に爆破予告が届いてるんだって？\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "空港を爆破してもらっちゃ\x01",
            "あたしも困る……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "ここはひとつクロスベル警察の\x01",
            "活躍に期待させてもらおうかねェ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x104,
        (
            "#0305F（闇ブローカーが\x01",
            "  抜け抜けと言うよなぁ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        "#0106F（皮肉にしか聞こえないわ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_875")

    Jump("loc_25C7")

    label("loc_87A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_END)), "loc_88B")
    Call(0, 4)
    Jump("loc_25C7")

    label("loc_88B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_C1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_99E")

    #C0015
    ChrTalk(
        0xFE,
        (
            "最近娘がナントカとかいう\x01",
            "ぬいぐるみを欲しがっててね。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "あんたら、ヒマなら\x01",
            "相手してやってくれないかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "アタシが忙しくしてる所為で\x01",
            "退屈してるみたいなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#0003Fは、はあ……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x104,
        (
            "#0300F（ブローカーは\x01",
            "  景気も良さそうだなぁ……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD3, 5)
    Jump("loc_C19")

    label("loc_99E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A72")

    #C0020
    ChrTalk(
        0x8,
        (
            "そういや、その件で\x01",
            "ダドリーが訪ねてくるんじゃ\x01",
            "ないかと思ってたんだがねェ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "おかしいね、いつもなら\x01",
            "先陣切って調べまわるくせに。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#0001F（ダドリーさんは……\x01",
            "  いま動けないんだよな……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C19")

    label("loc_A72")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0023
    ChrTalk(
        0x101,
        (
            "#0005Fそうだ……\x02\x03",

            "#0001Fあの、ここってもしかして\x01",
            "危ないクスリとか扱ってますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        "危ないクスリ……？\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "ああ、もしかして\x01",
            "『幸せを運ぶ青い薬』……\x01",
            "とかいう噂かい？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "生憎置いてないねェ。\x01",
            "まあうちからは完全に外れた\x01",
            "流通ルートって所だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x103,
        "#0203F……そうですか。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#0101Fでも噂は\x01",
            "確実にあるみたいね……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x104,
        (
            "#0301F火の無い所に煙は立たず……\x02\x03",

            "もしかして\x01",
            "結構出回ってんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_C19")

    Jump("loc_25C7")

    label("loc_C1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_E89")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_CA3")

    #C0030
    ChrTalk(
        0x8,
        (
            "にしても……\x01",
            "ガルシアの奴も苦労するねェ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "あいつ、ルバーチェに移ってから\x01",
            "白髪増えたんじゃないかい？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E84")

    label("loc_CA3")


    #C0032
    ChrTalk(
        0x8,
        "やれやれ、やっちまったか。\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "ツァオの奴がブチ切れれば\x01",
            "クロスベルで市街戦ができるねェ。\x02",
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
    Sleep(1000)

    #C0034
    ChrTalk(
        0x101,
        (
            "#0003F……物騒な事\x01",
            "言わないで下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        (
            "#0301Fストレートにマジな事を\x01",
            "言いやがって……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x103,
        (
            "#0200Fあの、もしかして\x01",
            "こちらで何か\x01",
            "情報を掴んでいたりは？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "さあね、襲撃は\x01",
            "ルバーチェの連中だとしか。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "あたしは情報屋じゃないし興味も無い。\x01",
            "調べたいなら当人達の所へ行っとくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_E84")

    Jump("loc_25C7")

    label("loc_E89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_F0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F02")

    #C0039
    ChrTalk(
        0x8,
        (
            "最近シスターが\x01",
            "しつこく訪ねてきやがるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "ったく煩い女だな。\x01",
            "舌引っこ抜いてやろうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F05")

    label("loc_F02")

    Call(0, 5)

    label("loc_F05")

    Jump("loc_25C7")

    label("loc_F0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_10FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F8A")

    #C0041
    ChrTalk(
        0x8,
        "あんたらも出歩くなら気を付けな。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "『今日から祭りを見に来た』\x01",
            "なんて連中は、かなり眉唾もんだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10FA")

    label("loc_F8A")


    #C0043
    ChrTalk(
        0x8,
        (
            "チッ……今日はどことなし\x01",
            "キナ臭い感じだねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "大方ルバーチェの\x01",
            "アレのせいだろうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#0005Fアレって……\x01",
            "もしかして《黒の競売会》ですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0046
    ChrTalk(
        0x8,
        (
            "なんだ、あんたたちも\x01",
            "知っていたのかい。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "あれは７～８年前から\x01",
            "マルコーニが始めた事業でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "お陰で当日はどこかしら\x01",
            "キナ臭い客がうろついてやがる……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        "チッ、気に食わないねえ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_10FA")

    Jump("loc_25C7")

    label("loc_10FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_11D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_115C")

    #C0050
    ChrTalk(
        0x8,
        (
            "さて、店はジンゴに任せて\x01",
            "トリニティで\x01",
            "一杯引っ掛けるとするかね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11D0")

    label("loc_115C")


    #C0051
    ChrTalk(
        0x8,
        "ようやく在庫整理が終わったよ。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x8,
        "ふー、働いた働いた。\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "記念祭の間は仕入れが多くて\x01",
            "困っちまうねェ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_11D0")

    Jump("loc_25C7")

    label("loc_11D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_13DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_12A7")

    #C0054
    ChrTalk(
        0x8,
        (
            "クロスベルじゃ爆弾テロなんて\x01",
            "珍しくもなかったがねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#0003Fその割に……俺は一度も\x01",
            "聞いた事がなかったんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "捜査一課がもみ消してるのさ。\x01",
            "大抵は未然に防いじまうしねェ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13DA")

    label("loc_12A7")


    #C0057
    ChrTalk(
        0x8,
        "今日はパレードらしいねェ。\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "クック……そういや\x01",
            "１０年ほど前だったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "パレードのミコシに\x01",
            "爆弾を仕掛けたテロ事件があったねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        "クク、今年は何もなきゃいいんだが。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x104,
        (
            "#0301F怖いこと言うなよ……\x01",
            "不安になるじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x8,
        (
            "ま、捜査一課も働いてんだろ。\x01",
            "あんたらがそう心配する事はないさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_13DA")

    Jump("loc_25C7")

    label("loc_13DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_15C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_145B")

    #C0063
    ChrTalk(
        0x8,
        (
            "すぱー……\x01",
            "ガルシアの奴も\x01",
            "苦労してるようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x8,
        (
            "ルバーチェなんざに\x01",
            "入るからだよ、まったく。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15BE")

    label("loc_145B")

    OP_93(0x8, 0xB4, 0x0)

    #C0065
    ChrTalk(
        0x8,
        (
            "すぱー……\x01",
            "ガルシアの奴、何か焦ってるね。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "自分トコのルートが\x01",
            "潰されちまったからって\x01",
            "泣きついてきやがったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#0003Fいや……そういう話じゃ\x01",
            "全然無かった気がしますが。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x104,
        (
            "#0300Fあの野郎とは\x01",
            "親しかったりするのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "昔、奴がルバーチェに入る前に\x01",
            "何度か取引があってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "ま、馴染み客って所か。\x01",
            "近頃はデカイツラして来やがるが。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_15BE")

    Jump("loc_25C7")

    label("loc_15C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_16BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_161D")

    #C0071
    ChrTalk(
        0x8,
        (
            "今日はいい品を仕入れたよ。\x01",
            "クック、見たきゃジンゴに声かけな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16B9")

    label("loc_161D")


    #C0072
    ChrTalk(
        0x8,
        (
            "今日はいい品を仕入れたよ。\x01",
            "クック、それも破格の仕入れ値だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "記念祭の前後は\x01",
            "取引が活発でいいねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#0006F警察としちゃ\x01",
            "良くないんですが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_16B9")

    Jump("loc_25C7")

    label("loc_16BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_18F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1733")

    #C0075
    ChrTalk(
        0x8,
        (
            "捜査一課の連中、何かを\x01",
            "調べまわってるようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "まあアタシの\x01",
            "知ったこっちゃないが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18EF")

    label("loc_1733")


    #C0077
    ChrTalk(
        0x8,
        "さっき捜査一課の連中が来たよ。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        "連中何か調べまわってるようだね。\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        "#0000Fはは、まあ……\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x102,
        (
            "#0105Fこの店では裏の情報も\x01",
            "扱っているんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "いいや？\x01",
            "アタシが扱うのはブツだけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x8,
        (
            "だがまあ、噂話くらいは\x01",
            "耳に入るからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "ルバーチェの噂、黒月の噂、\x01",
            "クロスベルを取り巻く裏社会の噂……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x8,
        (
            "買い物のついでに\x01",
            "ポロッとこぼしちまうことも\x01",
            "あるかもしれないねェ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        (
            "#0003F（一課にとっても\x01",
            "  情報源になってるみたいだな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_18EF")

    Jump("loc_25C7")

    label("loc_18F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1D71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x90, 7)), scpexpr(EXPR_END)), "loc_1ACF")

    #C0086
    ChrTalk(
        0x8,
        (
            "黒月のツァオは\x01",
            "スマートなやり方を使うって話だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x8,
        (
            "クック……抗争のやり口にしても\x01",
            "可愛げが無いくらい堅実だねェ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x8,
        (
            "あたしもちょいと\x01",
            "興味が出てきたよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ACA")

    #C0089
    ChrTalk(
        0x102,
        (
            "#0101Fあのう……双方に武器を\x01",
            "提供するような事はやめて下さいね？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "クック……約束はしないが\x01",
            "まあその必要はないだろうさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "双方、もうたっぷりと\x01",
            "持ってるはずだからねェ。\x02",
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
    Sleep(1000)
    SetScenarioFlags(0x0, 0)

    label("loc_1ACA")

    Jump("loc_1D6C")

    label("loc_1ACF")


    #C0092
    ChrTalk(
        0x8,
        "ツァオ、面白いことを始めたねェ。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x8,
        (
            "あのルバーチェ相手に\x01",
            "中々見事な切り崩しじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0094
    ChrTalk(
        0x101,
        (
            "#0005Fツァオ……？\x02\x03",

            "もしかしてそれは\x01",
            "黒月のボスの名前ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "ん、ああ……\x01",
            "あたしも会ったことはないがね。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x8,
        (
            "クロスベルに来ている＂支社長”だよ。\x01",
            "抗争するにも支配するにも\x01",
            "スマートなやり方を使うって話だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        (
            "クロスベルでの足場も固めたんで\x01",
            "攻勢に移ってきたんじゃないかい？\x01",
            "マフィアにしちゃ堅実なやり口だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x102,
        (
            "#0101Fもしかして……\x01",
            "最近事故の話が多いのは\x01",
            "そのせいかしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x104,
        (
            "#0303Fこの一ヶ月、\x01",
            "事件が多いとは思ってたが……\x02\x03",

            "#0301Fあくまで目に付かない所で\x01",
            "抗争してるってワケか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x90, 7)

    label("loc_1D6C")

    Jump("loc_25C7")

    label("loc_1D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2081")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1EF3")

    #C0100
    ChrTalk(
        0x8,
        (
            "この新型重機関銃は\x01",
            "先週から流通が始まってねェ。\x01",
            "ウチもすぐに仕入れたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "……ルバーチェの連中も\x01",
            "買い漁ったらしいから、\x01",
            "あんたらも気を付けなよ？\x02",
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
    Sleep(1000)

    #C0102
    ChrTalk(
        0x101,
        (
            "#0003F確かにあんな物を\x01",
            "ぶっ放されたくは無いな。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x104,
        (
            "#0306F生身の人間相手じゃ\x01",
            "あっという間にミンチだぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_207C")

    label("loc_1EF3")


    #C0104
    ChrTalk(
        0x104,
        (
            "#0305Fん、そいつは\x01",
            "ラインフォルト社製の重機関銃……？\x02\x03",

            "新型みたいだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x8,
        "ああ、先週から仕入れ始めたブツだ。\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x8,
        (
            "クック……装填弾数を増やした上に\x01",
            "威力が２割増しになってるらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        "赤毛、あんた持ってみるかい？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0108
    ChrTalk(
        0x104,
        (
            "#0305Fいや、いい……\x02\x03",

            "#0306Fつーか警察に\x01",
            "密輸品を見せびらかすなよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x102,
        "#0106Fふう、まったくです……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_207C")

    Jump("loc_25C7")

    label("loc_2081")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_21F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_20EB")

    #C0110
    ChrTalk(
        0x8,
        "やれやれ、仕方ねえ……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "店はジンゴに任せて\x01",
            "ちょっくら出かけてくるかねェ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21EB")

    label("loc_20EB")


    #C0112
    ChrTalk(
        0x8,
        (
            "これから帝国の方で\x01",
            "外せない商談があるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        (
            "チッ、アタシは低血圧なんだ。\x01",
            "朝から呼び出すなと\x01",
            "言ってあるんだがねェ……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        (
            "#0005F（商談って……\x01",
            "  武器の仕入れとかかな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x104,
        (
            "#0301F（だろうなぁ……帝国には\x01",
            "  デカイメーカーもあるわけだし。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_21EB")

    Jump("loc_25C7")

    label("loc_21F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2409")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2297")

    #C0116
    ChrTalk(
        0x8,
        (
            "警備隊も新規格のオーブメントに\x01",
            "鞍替えしたらしくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        (
            "旧式の備品のほか\x01",
            "新型クオーツも流れ始めてるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x8,
        "まだまだ数は少ないがねェ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2404")

    label("loc_2297")

    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0119
    ChrTalk(
        0x103,
        (
            "#0205Fあ……\x02\x03",

            "それはエニグマ用の\x01",
            "新型クオーツですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        "ああ、らしいね。\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x8,
        "こいつは警備隊からの横流し品だよ。\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x8,
        (
            "チッ、新型オーブメントなんざ\x01",
            "まだまだ普及してねぇし、\x01",
            "流されても困るんだがねェ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x101,
        (
            "#0003F警備隊……\x01",
            "そんなものなのか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        (
            "#0300Fそういう事もあるんだよ。\x01",
            "お偉いさんの中には\x01",
            "腐ってる連中もいてなぁ……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)

    label("loc_2404")

    Jump("loc_25C7")

    label("loc_2409")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_24B2")

    #C0125
    ChrTalk(
        0x8,
        (
            "ま、連中の抗争なんざ\x01",
            "あたしの知ったことじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "ブツが売れりゃあ\x01",
            "それでいいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x104,
        (
            "#0306F（いかにもブローカーの\x01",
            "  セリフだな、オイ……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_25C7")

    label("loc_24B2")


    #C0128
    ChrTalk(
        0x8,
        (
            "さて、こいつは黒月に卸す分だ。\x01",
            "そろそろ運び出しておくか。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#0005F黒月って……\x01",
            "あの東方マフィアの？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)

    #C0130
    ChrTalk(
        0x8,
        "ああ、知ってたのかい。\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x8,
        (
            "連中は新商品を出すたびに\x01",
            "少量だけ買っていくんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x8,
        (
            "クク……ルバーチェに流れる前に\x01",
            "性能を確かめてるんじゃないかね。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)

    label("loc_25C7")

    TalkEnd(0xFE)

    label("loc_25CA")

    Return()

    # Function_3_451 end

    def Function_4_25CB(): pass

    label("Function_4_25CB")

    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    TurnDirection(0x8, 0x10A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 1)), scpexpr(EXPR_END)), "loc_26E1")

    #C0133
    ChrTalk(
        0x8,
        (
            "またアングラ情報が\x01",
            "欲しくなったら来な。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x8,
        (
            "クク、あんたもお得意さんだからねェ。\x01",
            "サービスさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x103,
        "#0205F（ダドリーさん、常連なんですか。）\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x10A,
        (
            "#0603F（有力な情報源と\x01",
            "  持ちつ持たれつの関係になる……\x01",
            "  これも捜査の一環だ。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A00")

    label("loc_26E1")


    #C0137
    ChrTalk(
        0x8,
        "よう、ダドリーじゃないか。\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x8,
        (
            "今日は拳銃のメンテかい？\x01",
            "それともまた情報集めか？\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x10A,
        (
            "#0603F……アシュリーさん、\x01",
            "つかぬ事を聞くが……\x02\x03",

            "#0600Fこの店で違法薬物の類は\x01",
            "取り扱ってはいないだろうな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0140
    ChrTalk(
        0x101,
        "#0001F（ダドリーさん……直球だ……）\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "クク……『幸せを運ぶ青い薬』\x01",
            "……とかいう噂の件かい。\x01",
            "訪ねてくる頃だと思ってたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        (
            "生憎扱ってないが、\x01",
            "噂はちょくちょく耳にするねェ。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x8,
        "ここ２～３週間の事だ。\x02",
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x10A,
        (
            "#0603Fそうですか……\x02\x03",

            "#0600F失礼した。\x01",
            "今の発言は忘れていただきたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x8,
        (
            "了解。\x01",
            "代わりに何か買っていきな。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x8,
        (
            "あんたの銃に合う\x01",
            "新型の徹甲弾を仕入れておいたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x10A,
        "#0603F……かたじけない。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x102,
        "#0101F（この２人……もしかして……）\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x104,
        "#0301F（いつもこんな関係なのかねえ？）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCE, 1)

    label("loc_2A00")

    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0x8)
    Return()

    # Function_4_25CB end

    def Function_5_2A19(): pass

    label("Function_5_2A19")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)

    #C0150
    ChrTalk(
        0x8,
        "ったく、何度言えば判るんだい……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    #C0151
    ChrTalk(
        0x8,
        (
            "ジンゴ、お前だって\x01",
            "算術くらいできるよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x8,
        (
            "ラインフォルト社製のライフルを\x01",
            "１挺１万５千ミラで売り出しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x8,
        "一週間で４０挺売れました。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x8,
        "売り上げはいくらでしょう。\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x9,
        "ん～……\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x9,
        "……６０万ミラだな！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0xA, 500)

    #C0157
    ChrTalk(
        0x8,
        "カンペキじゃねーか。\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xA,
        (
            "……カンペキじゃありません。\x01",
            "まったくもう……\x02",
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
    Sleep(1000)
    ClearChrFlags(0x8, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 0)
    Return()

    # Function_5_2A19 end

    def Function_6_2BFC(): pass

    label("Function_6_2BFC")

    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    TurnDirection(0x8, 0x104, 500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C5C")

    #C0159
    ChrTalk(
        0x8,
        (
            "そういや、赤毛。\x01",
            "アンタ中々軍備品に詳しいようだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C9D")

    label("loc_2C5C")


    #C0160
    ChrTalk(
        0x8,
        (
            "そういや、そっちの赤毛。\x01",
            "アンタ中々軍備品に詳しいようだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C9D")


    #C0161
    ChrTalk(
        0x8,
        "軍人かい？\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0162
    ChrTalk(
        0x104,
        (
            "#0305Fへ……？\x02\x03",

            "#0300Fハハ、まあ……\x01",
            "確かに警備隊にはいたけどな。\x02\x03",

            "警備隊も建前上は\x01",
            "軍隊じゃないことになってるし、\x01",
            "別に軍人ってワケじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x8,
        (
            "赤毛の長髪……\x01",
            "戦闘経験のありそうな面構え……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    #C0164
    ChrTalk(
        0x8,
        "ふーん……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0165
    ChrTalk(
        0x104,
        "#0305F……あの、俺に何か用スか？\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x8,
        "いいや、なんでもないさ。\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x8,
        (
            "邪魔したねェ。\x01",
            "また入用なものがあれば\x01",
            "立ち寄ってくんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        (
            "#0005Fは、はあ……\x01",
            "（何だったんだ……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6B, 2)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0xFE)
    Return()

    # Function_6_2BFC end

    def Function_7_2E98(): pass

    label("Function_7_2E98")

    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    TurnDirection(0x8, 0x0, 0)

    #C0169
    ChrTalk(
        0x8,
        (
            "……警察のナントカ課じゃないか。\x01",
            "クック、元気してるようだねェ。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x8,
        (
            "何か見ていくかい？\x01",
            "最近はいい品を仕入れてるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        (
            "#0006Fいえ、あの……\x01",
            "闇ブローカーの人に\x01",
            "そんな事を言われても……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x104,
        (
            "#0306F相変わらずキナ臭ぇ店だな。\x01",
            "密輸品ばっかじゃねえか……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x8,
        (
            "オモテじゃ酒だの\x01",
            "食料品だのを扱ってる。\x01",
            "ククク……文句あるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x103,
        (
            "#0200Fまあ、主に外国の\x01",
            "軍や猟兵団相手の商売と\x01",
            "聞いていますし……\x02\x03",

            "ルバーチェのような脅威がない分\x01",
            "黙認のしようもあるのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x102,
        (
            "#0106Fこんなお店が堂々とある辺り、\x01",
            "ため息が出てしまうわね……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6B, 1)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0x8)
    Return()

    # Function_7_2E98 end

    def Function_8_30D7(): pass

    label("Function_8_30D7")

    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x8)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0176
    ChrTalk(
        0x8,
        (
            "ラインフォルトの\x01",
            "２４口径が６０、と……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x102,
        (
            "#0101F（ねえ、ロイド……）\x02\x03",

            "（そこの木箱から\x01",
            "  拳銃がのぞいているんだけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x103,
        (
            "#0201F（……あっちの木箱は\x01",
            "  すべて弾薬のようです。）\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x104,
        (
            "#0301F（爆薬に手榴弾……\x01",
            "  あっちは防弾チョッキに\x01",
            "  カスタムグレネード……）\x02\x03",

            "#0306F（うはあ、あのドラム缶は\x01",
            "  警備隊で使ってた\x01",
            "  液体燃料じゃねえか？）\x02",
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
    Sleep(1000)

    #C0180
    ChrTalk(
        0x101,
        (
            "#0001Fあ、あのう……すみません。\x02\x03",

            "失礼ですが、ここは\x01",
            "どういった店なんでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    TurnDirection(0x8, 0x0, 500)

    #C0181
    ChrTalk(
        0x8,
        (
            "……ああン？\x01",
            "なんだい客かい。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x8,
        "うちはブローカーだよ。\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x8,
        (
            "あちこちから流れてくる\x01",
            "色んなブツを扱わせてもらっている。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x8,
        (
            "あんたらは警察の新入りかい？\x01",
            "クック、見ない顔だねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x101,
        "#0005Fブ、ブローカー……\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x104,
        (
            "#0303F……“闇”が付く方だな。\x02\x03",

            "#0301Fそういやクロスベルには\x01",
            "手広くやってる店があるって噂を\x01",
            "聞いたことがあるが……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x102,
        (
            "#0101F武器や横流し品の密貿易……\x01",
            "まさかルバーチェの関係の……？\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x8,
        (
            "やれやれ……\x01",
            "ちんけなマフィアなんかと\x01",
            "一緒にしないでおくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x8,
        (
            "あたしは真っ当なブローカーでねえ。\x01",
            "十数カ国の、軍だの猟兵団やらを\x01",
            "相手に商売させてもらっている。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x8,
        (
            "所構わずぶっ放すようなジャリは\x01",
            "相手にしねえし、ケジメが付けられんなら\x01",
            "警察相手だろうが構わないさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x8,
        (
            "……実際、クロスベル警察の\x01",
            "捜査一課は定期的に顔を出しやがるね。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x8,
        (
            "ま、買い物半分\x01",
            "密貿易のトレンド調査半分って\x01",
            "腹積もりらしいが。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x103,
        (
            "#0200F警察にとっても\x01",
            "利用価値アリ、ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x101,
        (
            "#0003Fなんというか\x01",
            "きな臭さが抜けないんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x8,
        (
            "クク、あんたらも\x01",
            "何か買っていくかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x8,
        (
            "……ただし、信用のない奴に\x01",
            "武器は売れない。\x01",
            "こっちにもルールがあるんでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x8,
        (
            "それでもいいってんなら\x01",
            "カウンターにいる\x01",
            "娘に声を掛けるんだね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6B, 1)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkEnd(0x8)
    Return()

    # Function_8_30D7 end

    def Function_9_378F(): pass

    label("Function_9_378F")

    Call(0, 10)
    Return()

    # Function_9_378F end

    def Function_10_3793(): pass

    label("Function_10_3793")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_37B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37AD")
    Call(0, 11)
    SetScenarioFlags(0x6B, 3)
    Return()

    label("loc_37AD")

    Jump("loc_37C0")

    label("loc_37B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37C0")
    Call(0, 12)
    Return()

    label("loc_37C0")

    TalkBegin(0x9)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_37CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F93")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",                # 0
            "交換する(装備)\x01",          # 1
            "交換する(クオーツ)\x01",      # 2
            "交換する(その他)\x01",        # 3
            "やめる\x01",                  # 4
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_385B")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_385B")

    RunExpression(0x4, (scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D3, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3884")
    OP_AF(0x90)
    Jump("loc_38B6")

    label("loc_3884")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3894")
    OP_AF(0x8F)
    Jump("loc_38B6")

    label("loc_3894")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_38A4")
    OP_AF(0x8E)
    Jump("loc_38B6")

    label("loc_38A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_38B4")
    OP_AF(0x8D)
    Jump("loc_38B6")

    label("loc_38B4")

    OP_AF(0x8C)

    label("loc_38B6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4F8E")

    label("loc_38C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3925")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_38E4")
    OP_AF(0x9A)
    Jump("loc_3916")

    label("loc_38E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_38F4")
    OP_AF(0x99)
    Jump("loc_3916")

    label("loc_38F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3904")
    OP_AF(0x98)
    Jump("loc_3916")

    label("loc_3904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3914")
    OP_AF(0x97)
    Jump("loc_3916")

    label("loc_3914")

    OP_AF(0x96)

    label("loc_3916")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4F8E")

    label("loc_3925")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3944")
    OP_AF(0xA4)
    Jump("loc_3986")

    label("loc_3944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3954")
    OP_AF(0xA5)
    Jump("loc_3986")

    label("loc_3954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3964")
    OP_AF(0xA3)
    Jump("loc_3986")

    label("loc_3964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3974")
    OP_AF(0xA2)
    Jump("loc_3986")

    label("loc_3974")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3984")
    OP_AF(0xA1)
    Jump("loc_3986")

    label("loc_3984")

    OP_AF(0xA0)

    label("loc_3986")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x2D3, 0x0)"), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_39A2")
    SetScenarioFlags(0x9D, 5)

    label("loc_39A2")

    Jump("loc_4F8E")

    label("loc_39A7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_39BB")
    Jump("loc_4F8E")

    label("loc_39BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F8E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_3A1C")

    #C0198
    ChrTalk(
        0x9,
        "お客、そろそろ店閉めっぞー。\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x9,
        "買うなら早くしろ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F8E")

    label("loc_3A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3D04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9D, 5)), scpexpr(EXPR_END)), "loc_3B9F")

    #C0200
    ChrTalk(
        0x9,
        (
            "みっしぃが１匹……\x01",
            "みっしぃが２匹……\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x9,
        (
            "『……大佐、これより\x01",
            "  雪中行軍を開始するであります！』\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x9,
        (
            "あー、やっぱ\x01",
            "みっしぃごっこは最高だなー！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B97")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0203
    ChrTalk(
        0x101,
        "#0006F（何ておままごとだ……）\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x103,
        (
            "#0200F（あの《みっしぃ》たちは\x01",
            "  今幸せなのでしょうか……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B97")

    SetScenarioFlags(0x0, 1)
    Jump("loc_3CFF")

    label("loc_3B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CB4")

    #C0205
    ChrTalk(
        0x9,
        "ん～、なんか買ってくか？\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x9,
        (
            "常連ならな、\x01",
            "サービスしてやってもいいぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x9,
        "はい、弾一個おまけな。\x02",
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
    Sleep(1000)

    #C0208
    ChrTalk(
        0x102,
        (
            "#0106F（子供がこんな事してて\x01",
            "  いいのかしら……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3CFF")

    label("loc_3CB4")


    #C0209
    ChrTalk(
        0x9,
        "あー、今日はヒマだなー。\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x9,
        (
            "ママもさいきん\x01",
            "すげーいそがしいしなー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CFF")

    Jump("loc_4F8E")

    label("loc_3D04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3EA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3D93")

    #C0211
    ChrTalk(
        0x9,
        (
            "ママなー、ジンゴが生まれる前は\x01",
            "ふんそー地域で店やっててなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x9,
        (
            "客とぶっ放しあいとか、\x01",
            "よくしたって言ってたぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E9C")

    label("loc_3D93")


    #C0213
    ChrTalk(
        0x9,
        "あんなー、あんなー……\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x9,
        "ウチはしゅーげきされても平気だぞ。\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x9,
        (
            "ママ、慣れてっからなー。\x01",
            "すぐに返り討ちだなー。\x02",
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
    Sleep(1000)

    #C0216
    ChrTalk(
        0x104,
        "#0306F（確かにここの店ならなぁ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3E9C")

    Jump("loc_4F8E")

    label("loc_3EA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3F13")

    #C0217
    ChrTalk(
        0x9,
        (
            "あんなー、シスターのことは\x01",
            "気にせず買い物しろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x9,
        (
            "ジンゴ、算術くらい\x01",
            "らくしょーだからなー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F8E")

    label("loc_3F13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4324")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB0, 3)), scpexpr(EXPR_END)), "loc_3FF4")

    #C0219
    ChrTalk(
        0x9,
        (
            "あんなー、ウチは\x01",
            "ガキンチョお断りだからなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x9,
        (
            "来るときはちゃんと\x01",
            "『遊びっ』って言えなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x153,
        "#1109Fうん、わかった～！\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x101,
        (
            "#0003Fキーア……その前に\x01",
            "俺たちに一言相談してくれ。\x01",
            "お願いだから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_431F")

    label("loc_3FF4")


    #C0223
    ChrTalk(
        0x153,
        (
            "#1110Fねえねえ、ここで何してるの？\x01",
            "なんだか変わったおミセだね～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x9)

    #C0224
    ChrTalk(
        0x9,
        "な、なんだお前ー、お客か？\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x9,
        "ウチはガキンチョお断りだぞっ！！\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x153,
        (
            "#1105Fえー、そうなのー！？\x02\x03",

            "#1108Fううっ、モノがたくさんあって\x01",
            "楽しそうなのに……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0227
    ChrTalk(
        0x9,
        (
            "ん～、なんだお前ー、\x01",
            "よく分かってんじゃねーか。\x01",
            "見込みあるなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x9,
        (
            "……ジンゴと遊ぶか？\x01",
            "それならいいぞー。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x153,
        "#1109Fほんと？　わーい！\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x9,
        (
            "あんなー、こっちが１８口径でな、\x01",
            "こっちは２４口径でなー……\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x153,
        "#1109Fうんうん♪\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        (
            "#0003Fストップ、ストップ……\x02\x03",

            "キーア、危ない遊びはやめような。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4283")

    #C0233
    ChrTalk(
        0x102,
        (
            "#0103Fどうしてこんな場所で\x01",
            "気が合ってしまうのかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_431C")

    label("loc_4283")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_42D1")

    #C0234
    ChrTalk(
        0x103,
        (
            "#0206Fこんな場所でキーアと\x01",
            "気が合ってしまうとは……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_431C")

    label("loc_42D1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_431C")

    #C0235
    ChrTalk(
        0x104,
        (
            "#0306Fどうしてこういう場所で\x01",
            "気が合っちまうかねぇ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_431C")

    SetScenarioFlags(0xB0, 3)

    label("loc_431F")

    Jump("loc_4F8E")

    label("loc_4324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_43FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_438E")

    #C0236
    ChrTalk(
        0x9,
        (
            "……ママ、あとで\x01",
            "祭りに連れてってくんねーかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x9,
        "きげん悪ぃし無理かなー。\x02",
    )

    CloseMessageWindow()
    Jump("loc_43F7")

    label("loc_438E")


    #C0238
    ChrTalk(
        0x9,
        (
            "あー、祭りなー……\x01",
            "ジンゴも出かけたかったんだけどなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x9,
        (
            "店あっからなー。\x01",
            "しょうがないなー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_43F7")

    Jump("loc_4F8E")

    label("loc_43FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_445E")

    #C0240
    ChrTalk(
        0x9,
        "……お客、なんか疲れてねえ？\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x9,
        "何か買ってけ！\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x9,
        "ぱーっと買って元気出せ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4F8E")

    label("loc_445E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_45F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_44B5")

    #C0243
    ChrTalk(
        0x9,
        (
            "このカメラ、\x01",
            "フツーの写真もとれっし\x01",
            "ちょーお得なのになー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45EF")

    label("loc_44B5")


    #C0244
    ChrTalk(
        0x9,
        (
            "さっき観光客が来てな、\x01",
            "導力カメラくれって言うからな……\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x9,
        (
            "中に小型銃入ってるヤツ\x01",
            "勧めたら、慌てて帰ってったぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x9,
        (
            "残念だなー、\x01",
            "これ、すげー使えっぞ？\x02",
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
    Sleep(1000)

    #C0247
    ChrTalk(
        0x101,
        (
            "#0006Fこの店には\x01",
            "危ないものしかないのか……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_45EF")

    Jump("loc_4F8E")

    label("loc_45F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_46C2")

    #C0248
    ChrTalk(
        0x9,
        (
            "ニシシ……\x01",
            "猟兵のオヤジ、ざまーみろ！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46BD")

    #C0249
    ChrTalk(
        0x104,
        (
            "#0306Fつーか、危ないだろ。\x01",
            "こっちがヒヤッとしたぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x103,
        "#0200F……まったくです。\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        (
            "#0006Fこの親子、\x01",
            "いつもこの調子なのか……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_46BD")

    Jump("loc_4F8E")

    label("loc_46C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4792")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4715")

    #C0252
    ChrTalk(
        0x9,
        "お客、金目のもん見ていくか？\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x9,
        "高いけどガマンしろ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_478D")

    label("loc_4715")


    #C0254
    ChrTalk(
        0x9,
        "お客、新しい品はいったぞ。\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x9,
        "今度のは金目のもんだぞ。\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x9,
        (
            "とーぜん高いけどなー。\x01",
            "そんくらいガマンしろなー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_478D")

    Jump("loc_4F8E")

    label("loc_4792")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_485B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_47E5")

    #C0257
    ChrTalk(
        0x9,
        "……お客、なんか買ってけ！\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x9,
        "夕方には店閉めっぞー！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4856")

    label("loc_47E5")


    #C0259
    ChrTalk(
        0x9,
        (
            "今日はママの仕入れに\x01",
            "ついてっていいってさー。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x9,
        (
            "夕方には店閉めっから。\x01",
            "お客、買うなら早めにしとけー！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4856")

    Jump("loc_4F8E")

    label("loc_485B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4AA4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_49ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_48DC")

    #C0261
    ChrTalk(
        0x9,
        "ママ、まだ帰ってこねーの。\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0262
    ChrTalk(
        0x9,
        (
            "おせーなー。\x01",
            "何やってんだろ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49E8")

    label("loc_48DC")


    #C0263
    ChrTalk(
        0x9,
        "……あー、おい、お客ら？\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x9,
        "#4S表でうっせーぞ、こら！！\x02",
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
    Sleep(1000)

    #C0265
    ChrTalk(
        0x101,
        "#0006F……スミマセン。\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x9,
        (
            "しょーばいの邪魔ンなんだろ？\x01",
            "な？　な！？\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x9,
        "遊ぶならしずかにしろ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_49E8")

    Jump("loc_4A9F")

    label("loc_49ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4A59")

    #C0268
    ChrTalk(
        0x9,
        "ママ、まだ帰ってこねーの。\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0269
    ChrTalk(
        0x9,
        (
            "おせーなー。\x01",
            "何やってんだろ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A9F")

    label("loc_4A59")


    #C0270
    ChrTalk(
        0x9,
        (
            "おもてのガキンチョども、\x01",
            "うっせーなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x9,
        "しめっぞコラー！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4A9F")

    Jump("loc_4F8E")

    label("loc_4AA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4B7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4AFE")

    #C0272
    ChrTalk(
        0x9,
        (
            "ママ、今日は\x01",
            "飲みに行く日だぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x9,
        "話あんなら早めにしとけ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4B78")

    label("loc_4AFE")


    #C0274
    ChrTalk(
        0x9,
        "んー、ママに用かー？\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x9,
        "話あんなら早めにしとけ。\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x9,
        (
            "ママ、在庫整理終わったら\x01",
            "飲みに行くっていってたからなー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4B78")

    Jump("loc_4F8E")

    label("loc_4B7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4CA5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4BE7")

    #C0277
    ChrTalk(
        0x9,
        (
            "最近ママが\x01",
            "取引に連れてってくんなくてなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x9,
        "うー、毎日店番つまんねーの。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4CA0")

    label("loc_4BE7")


    #C0279
    ChrTalk(
        0x9,
        "最近なー、取引あぶねーらしいぞ？\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x9,
        (
            "ルバーチェの取引場所、\x01",
            "襲われたりしてんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x9,
        (
            "ママもあぶねーからって\x01",
            "最近取引に連れてってくんなくてなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x9,
        "うー、つまんねーの。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4CA0")

    Jump("loc_4F8E")

    label("loc_4CA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4EC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4D13")

    #C0283
    ChrTalk(
        0x9,
        (
            "こっちのタマ、\x01",
            "１８口径で人気ないのなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x9,
        "んー、ＳＡＬＥとか貼っとくかなー。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4EBD")

    label("loc_4D13")


    #C0285
    ChrTalk(
        0x9,
        (
            "ふつーのタマはこっちなー。\x01",
            "炸薬多めはこっちでー……\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x9,
        (
            "んー……やっぱ\x01",
            "あっちのケースにいれっかな。\x01",
            "見やすいかもしんねーし……\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x9,
        "お客、どう思う～？\x02",
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
    Sleep(1000)

    #C0288
    ChrTalk(
        0x101,
        "#0006Fどうって言われても……\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x102,
        (
            "#0105Fあ、危ないから触らない方が\x01",
            "いいんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0290
    ChrTalk(
        0x9,
        (
            "ブツ並べねーと\x01",
            "客、買ってくんねーだろ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_4EBD")

    Jump("loc_4F8E")

    label("loc_4EC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4F35")

    #C0291
    ChrTalk(
        0x9,
        "ママは猟兵とも付き合いあんだー。\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x9,
        (
            "猟兵のオヤジ、ごっついぞ。\x01",
            "前に店に来たことあっからなー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F8E")

    label("loc_4F35")


    #C0293
    ChrTalk(
        0x9,
        "お客、なんか買ってくか？\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x9,
        (
            "現ミラは足付くからダメー。\x01",
            "お支払いは適当なブツなー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F8E")

    Jump("loc_37CD")

    label("loc_4F93")

    TalkEnd(0x9)
    Return()

    # Function_10_3793 end

    def Function_11_4F97(): pass

    label("Function_11_4F97")

    TalkBegin(0x9)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0295
    ChrTalk(
        0x9,
        (
            "あ、客だ～。\x01",
            "今日は何か買ってくか？\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x9,
        (
            "あんなー、最近\x01",
            "ちょー強力なグレネード仕入れたぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x9,
        "これで一個小隊もイチコロなー。\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x101,
        "#0006Fあ、相変わらず怪しい店だなぁ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_50DA")

    #C0299
    ChrTalk(
        0x102,
        (
            "#0103F表向きは物々交換の店って事に\x01",
            "なっているけど……\x02\x03",

            "限りなく黒に近い\x01",
            "灰色のお店、だものね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51CF")

    label("loc_50DA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5157")

    #C0300
    ChrTalk(
        0x103,
        (
            "#0203F表向きは物々交換の店って事に\x01",
            "なっていますが……\x02\x03",

            "限りなく黒に近い\x01",
            "灰色のお店、ですからね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_51CF")

    label("loc_5157")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_51CF")

    #C0301
    ChrTalk(
        0x104,
        (
            "#0303F表向きは物々交換の店って事に\x01",
            "なっちゃいるが……\x02\x03",

            "限りなく黒に近い\x01",
            "灰色のお店、だからなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51CF")

    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)
    SetChrName("")

    #A0302
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ジンゴに話しかけて『交換する』を選択すると、\x01",
            "  交換可能な商品が一覧表示されます。\x01",
            "  必要なアイテムを所持していれば、交換を行えます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0303
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ここに置いている装備やクオーツは\x01",
            "  他では入手できない希少価値の高いものです。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0304
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ミラがかからない代わりに相応の品が\x01",
            "  必要になるため、本当に交換していいか\x01",
            "  よく考えてから実行しましょう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetScenarioFlags(0xB3, 4)
    TalkEnd(0x9)
    Return()

    # Function_11_4F97 end

    def Function_12_5353(): pass

    label("Function_12_5353")

    TalkBegin(0x9)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0305
    ChrTalk(
        0x9,
        "あ、客だ～。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    #C0306
    ChrTalk(
        0x9,
        "#4Sママー、知らない客が来た～！\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x9,
        "#4Sこいつらにブキ売っていい～？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_546E")
    Sleep(1500)

    #C0308
    ChrTalk(
        0x9,
        "………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x0, 500)

    #C0309
    ChrTalk(
        0x9,
        (
            "あ、わりー。\x01",
            "今ママいないんだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x9,
        (
            "まあいいやー。\x01",
            "なんか買ってくか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_54E5")

    label("loc_546E")


    #C0311
    ChrTalk(
        0x8,
        "#4Pハァ？　知らねえ客？\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x8,
        "#4P足の付かねえモンにしときな！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x0, 500)

    #C0313
    ChrTalk(
        0x9,
        "……だってさー。\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x9,
        "なんか買ってくか？\x02",
    )

    CloseMessageWindow()

    label("loc_54E5")

    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0315
    ChrTalk(
        0x101,
        "#0005Fあの、えっと……\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x102,
        "#0100Fここは何のお店なのかしら？\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x9,
        (
            "ブツ。\x01",
            "なんでもあるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x9,
        (
            "でも今は\x01",
            "お薬とクオーツくらいだなー。\x01",
            "んー、これとこれとー……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0319
    ChrTalk(
        0x9,
        (
            "あ、あと現ミラは足付くからダメー。\x01",
            "お支払いも適当なブツなー。\x02",
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
    Sleep(1000)

    #C0320
    ChrTalk(
        0x103,
        "#0203Fあ、怪しい匂いがプンプンです。\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x104,
        (
            "#0306Fとりあえず……\x01",
            "物々交換の店ってことで\x01",
            "いいのかねえ？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(828, 0, 100, 0)
    SetChrName("")

    #A0322
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ジンゴに話しかけて『交換する』を選択すると、\x01",
            "  交換可能な商品が一覧表示されます。\x01",
            "  必要なアイテムを所持していれば、交換を行えます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0323
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ここに置いている装備やクオーツは\x01",
            "  他では入手できない希少価値の高いものです。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0324
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※ミラがかからない代わりに相応の品が\x01",
            "  必要になるため、本当に交換していいか\x01",
            "  よく考えてから実行しましょう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetScenarioFlags(0x6B, 3)
    SetScenarioFlags(0xB3, 4)
    TalkEnd(0x9)
    Return()

    # Function_12_5353 end

    def Function_13_5897(): pass

    label("Function_13_5897")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_58F0")

    #C0325
    ChrTalk(
        0xA,
        (
            "ふう……\x01",
            "旧市街の子供たちに教えるのは\x01",
            "いつも一筋縄ではいきません。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5994")

    label("loc_58F0")


    #C0326
    ChrTalk(
        0xA,
        (
            "ジンゴちゃんにも日曜学校に\x01",
            "参加してもらいたいのですが、\x01",
            "いつも追い返されてしまうのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xA,
        (
            "なんとかアシュリーさんにも\x01",
            "ご理解頂ければいいのですけれど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_5994")

    TalkEnd(0xFE)
    Return()

    # Function_13_5897 end

    def Function_14_5998(): pass

    label("Function_14_5998")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5AAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A51")

    #C0328
    ChrTalk(
        0xFE,
        (
            "昨日の襲撃事件について\x01",
            "聞き込みに来たんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        (
            "ここの店主さんは\x01",
            "どうもとっつきづらいんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xFE,
        (
            "常連でもない私は\x01",
            "なんだか居心地が悪いよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_5AAC")

    label("loc_5A51")


    #C0331
    ChrTalk(
        0xFE,
        (
            "私はどっちかって言うと\x01",
            "自分の拳に頼るタイプだからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xFE,
        "こういう店には縁がないよ。\x02",
    )

    CloseMessageWindow()

    label("loc_5AAC")

    TalkEnd(0xFE)
    Return()

    # Function_14_5998 end

    def Function_15_5AB0(): pass

    label("Function_15_5AB0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5CC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C33")

    #C0333
    ChrTalk(
        0xFE,
        (
            "ヴェンツェルたちは\x01",
            "ベルガード門のほうに調査に行ったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xFE,
        (
            "マフィアの目撃情報が\x01",
            "あったらしくって。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x101,
        (
            "#0005Fマフィアが警備隊の詰め所に……\x01",
            "なんでまた？\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xFE,
        (
            "目撃情報自体は\x01",
            "今までにも何度かあるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0xFE,
        (
            "警備隊の司令と繋がっているって\x01",
            "噂は前々から囁かれているしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x104,
        (
            "#0301Fまた賄賂がどうとかいう話だろ。\x02\x03",

            "#0306Fったく、あの司令も懲りねえな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5CC1")

    label("loc_5C33")


    #C0339
    ChrTalk(
        0xFE,
        (
            "ベルガード門の方の調査はまぁ、\x01",
            "大したことないだろうけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "あんな襲撃事件があったばかりだし、\x01",
            "念の為裏は取ってきてもらわないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CC1")

    TalkEnd(0xFE)
    Return()

    # Function_15_5AB0 end

    def Function_16_5CC5(): pass

    label("Function_16_5CC5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    LoadChrToIndex("chr/ch02200.itc", 0x1E)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    OP_68(2670, 1200, 7100, 0)
    MoveCamera(63, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, -270, 0, 1360, 45)
    SetChrPos(0x102, 860, 0, 1510, 0)
    SetChrPos(0x103, -810, 0, 500, 45)
    SetChrPos(0x104, 1130, 0, 760, 0)
    SetChrPos(0xD, 2330, 0, 6050, 0)
    SetChrPos(0x8, 2920, 0, 7720, 180)
    SetChrPos(0x9, 4380, -1920, 14500, 270)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetCameraDistance(17000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0341
    ChrTalk(
        0xD,
        (
            "#3104F……これは親切で\x01",
            "言ってやってるんだぜ？\x02\x03",

            "#3100Fアシュリー、悪い事は言わねえ。\x01",
            "ルバーチェの傘下に入れや。\x02\x03",

            "テメエの商売は\x01",
            "微妙にうちと被ってやがるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x8,
        (
            "その話は何度も\x01",
            "断ってるはずだがねェ……\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0xD,
        (
            "#3104F……分かってねえな。\x02\x03",

            "#3101Fお前には一目置いているから\x01",
            "潰さずに済ましてやってるんだ。\x01",
            "勘違いしてんじゃねえッ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x8,
        (
            "カハッ……面白ェよ\x01",
            "やってみな！\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x8,
        (
            "アタシはクロスベルから\x01",
            "大陸東部まで手広くやってんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x8,
        (
            "一国のチンケなマフィアの\x01",
            "手に負えるルートじゃねェんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x8,
        (
            "分かったらそこに直れや、\x01",
            "若頭さんよォ。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xD,
        (
            "#3107F……誰が直るか。\x01",
            "調子こくんじゃねえぞボケがァ！！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(3790, 1200, 8640, 3000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    OP_95(0x9, 9740, 0, 14440, 2000, 0x0)
    OP_95(0x9, 9740, 0, 12440, 2000, 0x0)
    TurnDirection(0x9, 0xD, 500)

    #C0349
    ChrTalk(
        0x9,
        "おいお客、うっせーぞ。\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x9,
        "ハナシは黙ってしろ！\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0xD,
        (
            "#3103F……チッ………\x01",
            "テメエんとこのガキも\x01",
            "相変わらずだな。\x02\x03",

            "#3100Fまあいい、よく考えとけよ。\x01",
            "クロスベルで店を\x01",
            "続けるつもりならな。\x02",
        )
    )

    CloseMessageWindow()
    Fade(300)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    OP_93(0x8, 0xE1, 0x0)
    OP_68(1500, 500, 4580, 0)
    OP_68(40, 1200, 2580, 2000)
    MoveCamera(41, 17, 0, 0)
    SetCameraDistance(17000, 0)
    OP_95(0xD, 730, 20, 3170, 2000, 0x0)

    #C0352
    ChrTalk(
        0xD,
        "#3101F……邪魔だ、どけ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x103, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_621D():
        OP_96(0x101, 0xFFFFFD6C, 0x0, 0x6E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_621D)

    def lambda_6237():
        OP_96(0x102, 0x532, 0x0, 0x6E0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6237)

    def lambda_6251():
        OP_96(0x103, 0xFFFFF9E8, 0x0, 0x460, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6251)
    OP_95(0xD, -110, 0, 70, 2000, 0x0)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)

    def lambda_6288():
        TurnDirection(0x101, 0xD, 350)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6288)

    def lambda_6295():
        TurnDirection(0x102, 0xD, 350)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6295)

    def lambda_62A2():
        TurnDirection(0x103, 0xD, 350)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_62A2)

    def lambda_62AF():
        TurnDirection(0x104, 0xD, 350)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_62AF)

    def lambda_62BC():
        OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_62BC)
    OP_95(0xD, -320, 0, -2350, 2000, 0x0)

    #C0353
    ChrTalk(
        0x104,
        (
            "#0301Fガルシア・ロッシ……\x01",
            "こんな所に来てやがったのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x103,
        "#0200F揉めていたみたいですね……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    Sleep(1000)
    OP_D5(0x1E)
    OP_68(130, 1200, 1760, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x0, 130, 0, 1760, 45)
    SetChrPos(0x1, 130, 0, 1760, 45)
    SetChrPos(0x2, 130, 0, 1760, 45)
    SetChrPos(0x3, 130, 0, 1760, 45)
    SetChrPos(0x9, 5670, 30, 8650, 225)
    SetScenarioFlags(0xB5, 0)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_16_5CC5 end

    def Function_17_63F9(): pass

    label("Function_17_63F9")

    EventBegin(0x1)
    OP_4B(0x9, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_647C")

    #C0355
    ChrTalk(
        0x9,
        (
            "お？\x01",
            "……客、ちょっと待て。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x9,
        (
            "そっちな、地下倉庫だから\x01",
            "入ったらダメなー。\x01",
            "買い物なら、ここでしろ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_64E2")

    label("loc_647C")


    #C0357
    ChrTalk(
        0x9,
        (
            "おいお客？\x01",
            "ハナシ聞いてたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x9,
        (
            "地下倉庫はいんなっつってるだろ！！\x01",
            "買い物なら、ここでしろ！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_64E2")

    Sleep(50)
    SetChrPos(0x0, 9940, 0, 11910, 180)
    OP_4C(0x9, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_17_63F9 end

    SaveToFile()

Try(main)
