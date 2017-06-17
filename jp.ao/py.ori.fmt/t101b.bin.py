from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t101b.bin",                # FileName
        "t101b",                    # MapName
        "t101b",                    # Location
        0x0045,                     # MapIndex
        "ed7513",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 69, 0, 2, 0, 3],
    )

    BuildStringList((
        "t101b",                  # 0
        "エミー",                 # 1
        "ゼル",                   # 2
        "カビラン",               # 3
        "ルーグマン",             # 4
        "ツァイト",               # 5
        "セシル",                 # 6
        "イリア",                 # 7
        "迎賓館方面",             # 8
        "ホテル・デルフィニア方面",# 9
    ))

    AddCharChip((
        "chr/ch22300.itc",                   # 00
        "chr/ch22200.itc",                   # 01
        "chr/ch33100.itc",                   # 02
        "chr/ch33000.itc",                   # 03
        "chr/ch02708.itc",                   # 04
        "chr/ch07502.itc",                   # 05
    ))

    DeclNpc(-2750,   -2000,   33099,   180,  389,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-2750,   -2000,   31899,   0,    389,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(26860,   -2000,   2200,    270,  385,  0x0, 0,   2,   0,   0,   1,   0,   9,   255,  0)
    DeclNpc(-6929,   -1799,   52110,   45,   389,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-3170,   -3799,   -13359,  135,  405,  0x0, 0,   4,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-1919,   -3700,   -12430,  180,  389,  0x0, 0,   5,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    PlaceName(-5.0, 0.0, 81.0, 0x0000, 0x0000, "迎賓館方面")
    PlaceName(65.0, 0.0, 0.0, 0x0000, 0x0000, "ホテル・デルフィニア方面")

    ChipFrameInfo(456, 0)                                        # 0

    ScpFunction((
        "Function_0_1C8",          # 00, 0
        "Function_1_280",          # 01, 1
        "Function_2_2E1",          # 02, 2
        "Function_3_39E",          # 03, 3
        "Function_4_3C6",          # 04, 4
        "Function_5_44B",          # 05, 5
        "Function_6_504",          # 06, 6
        "Function_7_5BB",          # 07, 7
        "Function_8_6B5",          # 08, 8
        "Function_9_765",          # 09, 9
        "Function_10_911",         # 0A, 10
        "Function_11_A70",         # 0B, 11
    ))


    def Function_0_1C8(): pass

    label("Function_0_1C8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_208"),
        (1, "loc_214"),
        (2, "loc_220"),
        (3, "loc_22C"),
        (4, "loc_238"),
        (5, "loc_244"),
        (6, "loc_250"),
        (SWITCH_DEFAULT, "loc_25C"),
    )


    label("loc_208")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_214")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_220")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_22C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_238")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_244")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_250")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_25C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_268")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_268")

    label("loc_27F")

    Return()

    # Function_0_1C8 end

    def Function_1_280(): pass

    label("Function_1_280")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E0")
    OP_95(0xFE, 26860, -2000, 2200, 2000, 0x0)
    OP_95(0xFE, -4019, -1800, 2200, 2000, 0x0)
    OP_95(0xFE, -3510, -1800, -1500, 2000, 0x0)
    OP_95(0xFE, 26860, -2000, -2060, 2000, 0x0)
    Jump("Function_1_280")

    label("loc_2E0")

    Return()

    # Function_1_280 end

    def Function_2_2E1(): pass

    label("Function_2_2E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_2EF")
    Jump("loc_39D")

    label("loc_2EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_2FD")
    Jump("loc_39D")

    label("loc_2FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_34E")
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32B")
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    EndChrThread(0xD, 0x0)
    SetChrBattleFlags(0xD, 0x4)

    label("loc_32B")

    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_39D")

    label("loc_34E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_35C")
    Jump("loc_39D")

    label("loc_35C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_36A")
    Jump("loc_39D")

    label("loc_36A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_378")
    Jump("loc_39D")

    label("loc_378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_386")
    Jump("loc_39D")

    label("loc_386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_394")
    Jump("loc_39D")

    label("loc_394")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_39D")

    label("loc_39D")

    Return()

    # Function_2_2E1 end

    def Function_3_39E(): pass

    label("Function_3_39E")

    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(126, 1, 80, 0)
    Return()

    # Function_3_39E end

    def Function_4_3C6(): pass

    label("Function_4_3C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DD")
    Call(0, 11)
    Return()

    label("loc_3DD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_3EE")
    Jump("loc_447")

    label("loc_3EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_406")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_401")

    label("loc_401")

    Jump("loc_447")

    label("loc_406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_414")
    Jump("loc_447")

    label("loc_414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_422")
    Jump("loc_447")

    label("loc_422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_430")
    Jump("loc_447")

    label("loc_430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_43E")
    Jump("loc_447")

    label("loc_43E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_447")

    label("loc_447")

    TalkEnd(0xFE)
    Return()

    # Function_4_3C6 end

    def Function_5_44B(): pass

    label("Function_5_44B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_462")
    Call(0, 11)
    Return()

    label("loc_462")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_473")
    Jump("loc_500")

    label("loc_473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_4B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48B")
    Jump("loc_4AC")

    label("loc_48B")


    #C0001
    ChrTalk(
        0xC,
        "#01200Fグルルル……ウォン。\x02",
    )

    CloseMessageWindow()

    label("loc_4AC")

    Jump("loc_500")

    label("loc_4B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_4BF")
    Jump("loc_500")

    label("loc_4BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_4CD")
    Jump("loc_500")

    label("loc_4CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_4DB")
    Jump("loc_500")

    label("loc_4DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_4E9")
    Jump("loc_500")

    label("loc_4E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_4F7")
    Jump("loc_500")

    label("loc_4F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_500")

    label("loc_500")

    TalkEnd(0xFE)
    Return()

    # Function_5_44B end

    def Function_6_504(): pass

    label("Function_6_504")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_5A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_522")
    Call(0, 7)
    Jump("loc_59B")

    label("loc_522")


    #C0002
    ChrTalk(
        0x8,
        (
            "ゼルったら……\x01",
            "紳士的振る舞いだけは一級ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "で、でもだからといって\x01",
            "まだまだ素敵な旦那様には\x01",
            "程遠いんだからっ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59B")

    Jump("loc_5B7")

    label("loc_5A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_5AE")
    Jump("loc_5B7")

    label("loc_5AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_5B7")

    label("loc_5B7")

    TalkEnd(0xFE)
    Return()

    # Function_6_504 end

    def Function_7_5BB(): pass

    label("Function_7_5BB")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0004
    ChrTalk(
        0x8,
        "いいこと、ゼル？\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "昼間言ったとおり、\x01",
            "これから勉強も運動もがんばるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x9,
        (
            "わ、分かってるってば。\x01",
            "僕はエミーの許婚だからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x9,
        (
            "まだどうなるか分からないけど、\x01",
            "それなりに努力はさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        "…………ぽっ。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_7_5BB end

    def Function_8_6B5(): pass

    label("Function_8_6B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_74A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6D3")
    Call(0, 7)
    Jump("loc_745")

    label("loc_6D3")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0009
    ChrTalk(
        0x9,
        (
            "それじゃあね、エミー。\x01",
            "夜中は冷えるから\x01",
            "暖かくしてないとダメだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        "わ、分かってるもん。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)

    label("loc_745")

    Jump("loc_761")

    label("loc_74A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_758")
    Jump("loc_761")

    label("loc_758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_761")

    label("loc_761")

    TalkEnd(0xFE)
    Return()

    # Function_8_6B5 end

    def Function_9_765(): pass

    label("Function_9_765")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_8E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85F")

    #C0011
    ChrTalk(
        0xA,
        (
            "最近、暗くなったらできるだけ\x01",
            "出歩かないようにしているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xA,
        (
            "以前、夜中に散歩していたら\x01",
            "突然マフィアの軍用犬が現れて、\x01",
            "怖い思いをしたことがあるんでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xA,
        (
            "君達も、用があるなら\x01",
            "さっさと済まして家に帰りたまえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_8E3")

    label("loc_85F")


    #C0014
    ChrTalk(
        0xA,
        (
            "最近、暗くなったら\x01",
            "さっさと家に帰ることにしているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xA,
        (
            "……突然軍用犬とかが現れた場合に\x01",
            "あたふたしなくてもいいようにね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E3")

    Jump("loc_90D")

    label("loc_8E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_8F6")
    Jump("loc_90D")

    label("loc_8F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_904")
    Jump("loc_90D")

    label("loc_904")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_90D")

    label("loc_90D")

    TalkEnd(0xFE)
    Return()

    # Function_9_765 end

    def Function_10_911(): pass

    label("Function_10_911")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_A55")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9D6")

    #C0016
    ChrTalk(
        0xB,
        (
            "今夜は迎賓館に\x01",
            "ディーター市長が訪れるらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xB,
        (
            "独立提唱からあの方も\x01",
            "相当に忙しくしていると聞くが……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xB,
        (
            "果たして、実現に向けての\x01",
            "首尾はどうなのだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_A50")

    label("loc_9D6")


    #C0019
    ChrTalk(
        0xB,
        (
            "ディーター市長は独立提唱から\x01",
            "相当に忙しくしていると聞くが……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xB,
        (
            "果たして、実現に向けての\x01",
            "首尾はどうなのだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A50")

    Jump("loc_A6C")

    label("loc_A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_A63")
    Jump("loc_A6C")

    label("loc_A63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_A6C")

    label("loc_A6C")

    TalkEnd(0xFE)
    Return()

    # Function_10_911 end

    def Function_11_A70(): pass

    label("Function_11_A70")

    EventBegin(0x0)
    Fade(500)
    LoadChrToIndex("chr/ch05100.itc", 0x1E)
    LoadChrToIndex("chr/ch07500.itc", 0x1F)
    OP_68(-1560, -2000, -14560, 0)
    MoveCamera(351, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20110, 0)
    SetChrPos(0x101, -1020, -3800, -14130, 315)
    SetChrPos(0xEF, 0, -3800, -13600, 315)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xC, 0x8000)
    OP_4B(0xC, 0xFF)
    SetChrSubChip(0xD, 0x1)
    OP_0D()

    #C0021
    ChrTalk(
        0xD,
        "#5P#05902Fあら、ロイド。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xC,
        "#5P#01200Fグルル……ウォン。\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#12P#00000Fセシル姉、それにツァイト。\x01",
            "こんなところに居たのか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_BC4")

    #C0024
    ChrTalk(
        0x102,
        (
            "#12P#00100F珍しい組み合わせですね。\x02\x03",

            "迎賓館には\x01",
            "まだ行かないんですか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D29")

    label("loc_BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_C24")

    #C0025
    ChrTalk(
        0x103,
        (
            "#12P#00200F珍しい組み合わせですね。\x02\x03",

            "迎賓館のほうには\x01",
            "まだ行かないんですか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D29")

    label("loc_C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_C7E")

    #C0026
    ChrTalk(
        0x104,
        (
            "#12P#00300F珍しい組み合わせッスね。\x02\x03",

            "迎賓館には\x01",
            "まだ行かないんッスか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D29")

    label("loc_C7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_CD8")

    #C0027
    ChrTalk(
        0x109,
        (
            "#12P#10100F珍しい組み合わせですね。\x02\x03",

            "迎賓館には\x01",
            "まだ行かないんですか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D29")

    label("loc_CD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_D29")

    #C0028
    ChrTalk(
        0x105,
        (
            "#12P#10300F珍しい組み合わせだね。\x02\x03",

            "迎賓館には\x01",
            "まだ行かないのかい？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D29")


    #C0029
    ChrTalk(
        0xD,
        (
            "#5P#05909Fええ、さっきツァイト君が\x01",
            "ここに連れてきてくれてね。\x02\x03",

            "#05904Fテーマパークから離れて静かだし、\x01",
            "ちょっと涼んでいこうと思って。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xD)

    #C0030
    ChrTalk(
        0x101,
        (
            "#12P#00003Fセシル姉……\x01",
            "何か悩み事でもあるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xD,
        (
            "#5P#05904F……ふふ、いいえ。\x01",
            "そういうわけじゃないんだけど……\x02\x03",

            "#05901Fそうね、ロイドたちには\x01",
            "話したほうがいいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0032
    ChrTalk(
        0xD,
        (
            "#5P#05903F実は今度、シズクちゃんが\x01",
            "手術を受ける事になったの。\x02\x03",

            "#05901Fセイランド教授による、\x01",
            "視力回復をかけた手術をね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0033
    ChrTalk(
        0x101,
        "#12P#0005Fシズクちゃんが……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xD,
        (
            "#5P#05908Fもともと、シズクちゃんは\x01",
            "今までにも何度か視力回復のために\x01",
            "手術を受けていたんだけど……\x02\x03",

            "#05903F彼女の症状は内科と外科、\x01",
            "神経科の問題が複雑に絡んでいて、\x01",
            "完治が難しかったの。\x02\x03",

            "#05900Fそこで、セイランド教授が\x01",
            "前々から研究していた新しい術式を\x01",
            "試してみることになったらしいわ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_10D9")

    #C0035
    ChrTalk(
        0x102,
        "#12P#00105F新しい術式、ですか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1198")

    label("loc_10D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_1106")

    #C0036
    ChrTalk(
        0x103,
        "#12P#00205F新しい術式……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1198")

    label("loc_1106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_1139")

    #C0037
    ChrTalk(
        0x104,
        "#12P#00305F新しい術式、ッスか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1198")

    label("loc_1139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_1168")

    #C0038
    ChrTalk(
        0x109,
        "#12P#10105F新しい術式……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_1198")

    label("loc_1168")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_1198")

    #C0039
    ChrTalk(
        0x105,
        "#12P#10305Fふむ、新しい術式ねえ。\x02",
    )

    CloseMessageWindow()

    label("loc_1198")


    #C0040
    ChrTalk(
        0xD,
        (
            "#5P#05903F私もそこまで詳しくはないけど……\x02\x03",

            "#05902F神経科の権威で、外科手術の心得もある\x01",
            "教授だからこそとれる術式らしくてね。\x02\x03",

            "#05903F万全の準備が必要らしくて、\x01",
            "この間もレミフェリアから最新式の\x01",
            "医療機器を取り寄せていたみたい。\x02\x03",

            "#05908F……セイランド教授によれば、\x01",
            "それでも確率は五分五分だろうという\x01",
            "話だったけれど。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        "#12P#00003Fそこまでしても五分五分なのか……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_133E")

    #C0042
    ChrTalk(
        0x102,
        "#12P#00108F……それは心配ですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1410")

    label("loc_133E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_136F")

    #C0043
    ChrTalk(
        0x103,
        "#12P#00208F……心配、ですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1410")

    label("loc_136F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_13A4")

    #C0044
    ChrTalk(
        0x104,
        "#12P#00303F……それは心配ッスね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1410")

    label("loc_13A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_13D7")

    #C0045
    ChrTalk(
        0x109,
        "#12P#10108Fそれは心配ですね……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1410")

    label("loc_13D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_1410")

    #C0046
    ChrTalk(
        0x105,
        (
            "#12P#10308Fなるほど。\x01",
            "……それは心配だね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1410")


    #C0047
    ChrTalk(
        0xD,
        (
            "#5P#05903F今までの失敗を考えると\x01",
            "かなり希望があるのには\x01",
            "間違いないらしいんだけどね。\x02\x03",

            "#05908F本当に、成功してくれると\x01",
            "いいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#12P#00003Fそうだな……\x01",
            "アリオスさんにも随分と\x01",
            "お世話になっているし。\x02\x03",

            "#00000F俺たちも、手術の成功を\x01",
            "女神に祈っているよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xD,
        (
            "#5P#05909Fふふ、ありがとう。\x01",
            "シズクちゃんにも伝えておくわね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x4)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 250, -1800, -440, 180)

    #N0050
    NpcTalk(
        0xE,
        "女性の声",
        (
            "#Nあら、セシル。\x01",
            "まだここにいたんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-860, -2000, -14160, 3000)
    MoveCamera(344, 18, 0, 3000)
    OP_6E(400, 3000)
    SetCameraDistance(20110, 3000)

    def lambda_162C():

        label("loc_162C")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_162C")

    QueueWorkItem2(0x101, 2, lambda_162C)

    def lambda_163E():

        label("loc_163E")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_163E")

    QueueWorkItem2(0xEF, 2, lambda_163E)

    def lambda_1650():
        OP_95(0xFE, 250, -3800, -12220, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1650)
    WaitChrThread(0xE, 1)
    OP_93(0xE, 0x10E, 0x1F4)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0xEF, 0xFF)

    #C0051
    ChrTalk(
        0xD,
        "#5P#05905Fイリア、どうしたの？\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xE,
        (
            "#01706Fどうしたもこうしたも……\x02\x03",

            "#01700F後で来るって言って\x01",
            "いつまでたっても来ないから\x01",
            "わざわざ迎えに来たんじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xD,
        (
            "#5P#05902Fふふ、ごめんごめん、\x01",
            "すぐに行くから。\x02\x03",

            "#05904Fうん、ロイドたちに話したおかげで\x01",
            "大分気持ちも整理できたし……\x01",
            "私もそろそろ行くとするかな。\x02\x03",

            "#05900Fあなたたちも色々と大変だろうけど……\x01",
            "私もシズクちゃんも応援してるわ。\x02\x03",

            "#05909Fだから、どんなことがあっても\x01",
            "くじけずにがんばってね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_183F():
        TurnDirection(0x101, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_183F)
    Sleep(50)

    def lambda_184F():
        TurnDirection(0xEF, 0xD, 500)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_184F)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)

    #C0054
    ChrTalk(
        0x101,
        "#12P#00000Fああ、ありがとうセシル姉。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x4)
    SetChrFlags(0xD, 0x40)
    SetChrPos(0xD, -1920, -3800, -13130, 180)
    OP_0D()
    Sleep(300)
    OP_93(0xD, 0x5A, 0x1F4)

    def lambda_18C6():
        OP_95(0xFE, -580, -3800, -12220, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_18C6)
    WaitChrThread(0xD, 1)

    #C0055
    ChrTalk(
        0xD,
        "#5P#05900Fそれじゃあ、行きましょ。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xE,
        (
            "#01705Fなになに、弟君たちと\x01",
            "色っぽい話でもしてたの？\x02\x03",

            "#01709Fあたしにも聞かせてよ～。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    OP_93(0xEF, 0x0, 0x1F4)

    def lambda_1975():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_1975)
    OP_93(0xD, 0x0, 0x1F4)

    def lambda_1989():
        OP_95(0xFE, 250, -1800, -440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1989)

    def lambda_19A3():
        OP_95(0xFE, -580, -1800, -440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_19A3)
    OP_68(-20, -2000, -16100, 5000)
    MoveCamera(344, 18, 0, 5000)
    OP_6E(400, 5000)
    SetCameraDistance(20110, 5000)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)

    def lambda_19FD():
        TurnDirection(0xFE, 0xEF, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_19FD)
    TurnDirection(0xEF, 0x101, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_1A5E")

    #C0057
    ChrTalk(
        0x102,
        (
            "#12P#00102Fふふ、元気付けるつもりが\x01",
            "逆に励まされちゃったわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAD")

    label("loc_1A5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_1AAE")

    #C0058
    ChrTalk(
        0x103,
        (
            "#12P#00202F元気付けるつもりが\x01",
            "逆に励まされてしまいましたね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAD")

    label("loc_1AAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_1B04")

    #C0059
    ChrTalk(
        0x104,
        (
            "#12P#00302Fハハ、元気付けるつもりだったが\x01",
            "逆に励まされちまったな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAD")

    label("loc_1B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_1B58")

    #C0060
    ChrTalk(
        0x109,
        (
            "#12P#10102Fふふ、元気付けるつもりが\x01",
            "逆に励まされちゃいましたね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BAD")

    label("loc_1B58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_1BAD")

    #C0061
    ChrTalk(
        0x105,
        (
            "#12P#10302Fフフ、元気付けていたのが\x01",
            "どっちだか分からなくなっちゃうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BAD")


    #C0062
    ChrTalk(
        0x101,
        (
            "#6P#00004Fああ、セシル姉らしいよ。\x02\x03",

            "#00000F……よし、俺たちもそろそろ\x01",
            "迎賓館に行くとしようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xC,
        "#5P#01200Fグルル……ウォン。\x02",
    )

    CloseMessageWindow()

    def lambda_1C38():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1C38)
    Sleep(50)

    def lambda_1C48():
        TurnDirection(0xEF, 0xC, 500)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1C48)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_1C94")

    #C0064
    ChrTalk(
        0x102,
        "#12P#00100F行ってくるわね、ツァイト。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D93")

    label("loc_1C94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_1CD6")

    #C0065
    ChrTalk(
        0x103,
        (
            "#12P#00200Fええ……\x01",
            "行ってきますね、ツァイト。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D93")

    label("loc_1CD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_1D0D")

    #C0066
    ChrTalk(
        0x104,
        "#12P#00300F行ってくるぜ、ツァイト。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D93")

    label("loc_1D0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_1D46")

    #C0067
    ChrTalk(
        0x109,
        "#12P#10100F行ってくるね、ツァイト君。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D93")

    label("loc_1D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_1D93")

    #C0068
    ChrTalk(
        0x105,
        (
            "#12P#10300Fフフ、見送ってくれてるのかな？\x01",
            "また後で、ツァイト。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D93")

    OP_5A()
    SetScenarioFlags(0x15A, 2)
    ClearChrFlags(0xC, 0x8000)
    OP_4C(0xC, 0xFF)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -1020, -3800, -14130, 0)
    EventEnd(0x5)
    Return()

    # Function_11_A70 end

    SaveToFile()

Try(main)
