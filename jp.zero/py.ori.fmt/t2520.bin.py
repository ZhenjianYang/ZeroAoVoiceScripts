from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t2520.bin",                # FileName
        "t2520",                    # MapName
        "t2520",                    # Location
        0x005A,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 90, 0, 2, 0, 3],
    )

    BuildStringList((
        "t2520",                  # 0
        "ノエル曹長",             # 1
        "ソーニャ副司令",         # 2
        "フラミー隊員",           # 3
        "バレル隊員",             # 4
        "観光客ベルティア",       # 5
    ))

    AddCharChip((
        "chr/ch34100.itc",                   # 00
        "apl/ch50147.itc",                   # 01
        "chr/ch00800.itc",                   # 02
        "chr/ch05702.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch34500.itc",                   # 05
    ))

    DeclNpc(740,     0,       4469,    349,  257,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(6210,    150,     -150,    260,  341,  0x0, 0,   3,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(-30899,  0,       43400,   0,    257,  0x0, 0,   0,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(-70010,  449,     -32430,  90,   469,  0x0, 0,   1,   0,   255, 255, 0,   10,  255,  0)
    DeclNpc(-52060,  0,       5650,    225,  385,  0x0, 0,   5,   0,   0,   1,   0,   11,  255,  0)

    DeclActor(-28890,  10,      42110,   1200,    -28890,  1500,    42110,   0x007C, 0,  20, 0x0000)
    DeclActor(4760,    0,       -280,    1200,    6210,    1500,    -150,    0x007E, 0,  6,  0x0000)

    ScpFunction((
        "Function_0_1D4",          # 00, 0
        "Function_1_28C",          # 01, 1
        "Function_2_2B7",          # 02, 2
        "Function_3_459",          # 03, 3
        "Function_4_4EE",          # 04, 4
        "Function_5_187A",         # 05, 5
        "Function_6_1AD6",         # 06, 6
        "Function_7_1ADA",         # 07, 7
        "Function_8_3FE0",         # 08, 8
        "Function_9_420F",         # 09, 9
        "Function_10_4AAD",        # 0A, 10
        "Function_11_4BF6",        # 0B, 11
        "Function_12_4CFE",        # 0C, 12
        "Function_13_5A30",        # 0D, 13
        "Function_14_5C6B",        # 0E, 14
        "Function_15_62FA",        # 0F, 15
        "Function_16_6EC1",        # 10, 16
        "Function_17_6EE0",        # 11, 17
        "Function_18_6EFF",        # 12, 18
        "Function_19_6F1E",        # 13, 19
        "Function_20_6F3D",        # 14, 20
    ))


    def Function_0_1D4(): pass

    label("Function_0_1D4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_214"),
        (1, "loc_220"),
        (2, "loc_22C"),
        (3, "loc_238"),
        (4, "loc_244"),
        (5, "loc_250"),
        (6, "loc_25C"),
        (SWITCH_DEFAULT, "loc_268"),
    )


    label("loc_214")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_220")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_22C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_238")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_244")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_250")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_25C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_268")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_274")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_28B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_274")

    label("loc_28B")

    Return()

    # Function_0_1D4 end

    def Function_1_28C(): pass

    label("Function_1_28C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B6")
    OP_94(0xFE, 0xFFFF2E82, 0x1770, 0xFFFF3CB0, 0x170C, 0x3E8)
    Sleep(300)
    Jump("Function_1_28C")

    label("loc_2B6")

    Return()

    # Function_1_28C end

    def Function_2_2B7(): pass

    label("Function_2_2B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2CF")
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    Jump("loc_445")

    label("loc_2CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2EE")
    SetChrPos(0x8, 3980, 0, -150, 90)
    Jump("loc_445")

    label("loc_2EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_31C")
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xA, -69630, 0, -30590, 180)
    Jump("loc_445")

    label("loc_31C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_32A")
    Jump("loc_445")

    label("loc_32A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_338")
    Jump("loc_445")

    label("loc_338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3BA")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_363")
    Event(0, 15)

    label("loc_363")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_374")
    Jump("loc_3B5")

    label("loc_374")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_397")
    SetChrPos(0x8, 6080, 0, 2120, 270)
    Jump("loc_3B5")

    label("loc_397")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_3B5")
    SetChrPos(0x8, 6080, 0, 2120, 180)

    label("loc_3B5")

    Jump("loc_445")

    label("loc_3BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3C8")
    Jump("loc_445")

    label("loc_3C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3E0")
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    Jump("loc_445")

    label("loc_3E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3EE")
    Jump("loc_445")

    label("loc_3EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_445")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_406")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 14)

    label("loc_406")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_428")
    SetChrPos(0x8, 6080, 0, 2120, 270)
    Jump("loc_445")

    label("loc_428")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_445")
    SetChrPos(0x8, 6080, 0, 2120, 270)

    label("loc_445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_458")
    ClearChrFlags(0xC, 0x80)

    label("loc_458")

    Return()

    # Function_2_2B7 end

    def Function_3_459(): pass

    label("Function_3_459")

    SetMapObjFrame(0xFF, "futon00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futon01", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_485")
    Jump("loc_4AC")

    label("loc_485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4AC")
    SetMapObjFrame(0xFF, "futon00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futon01", 0x1, 0x1)

    label("loc_4AC")

    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D7")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_4D7")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4ED")
    OP_66(0x0, 0x1)

    label("loc_4ED")

    Return()

    # Function_3_459 end

    def Function_4_4EE(): pass

    label("Function_4_4EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4FF")
    Jump("loc_1876")

    label("loc_4FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_607")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_51D")
    Call(0, 5)
    SetScenarioFlags(0x0, 1)
    Jump("loc_602")

    label("loc_51D")


    #C0001
    ChrTalk(
        0xFE,
        (
            "#0502Fあっ、皆さん……\x01",
            "昨日は本当にありがとうございました。\x02\x03",

            "#0504F昨日、副司令に相談したら\x01",
            "報告は早い方がいいということで\x01",
            "大急ぎで報告書をまとめたんです。\x02\x03",

            "#0508F七耀教会の協力で\x01",
            "あの鐘のことが判明すると\x01",
            "いいんですけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_602")

    Jump("loc_1876")

    label("loc_607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_615")
    Jump("loc_1876")

    label("loc_615")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_85D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7DE")

    #C0002
    ChrTalk(
        0xFE,
        (
            "#0500F昨日、アルモリカの古戦場に\x01",
            "観光客が入り込んでしまったという\x01",
            "報告がありました。\x02\x03",

            "#0504F支援課の皆さんが先んじて\x01",
            "救出してくださったそうで……\x01",
            "ありがとうございます。\x02\x03",

            "#0508F本当ならそういう事が起きないように\x01",
            "定期巡回などをしているんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#0002Fいや、緊急要請が入っていたから\x01",
            "当然のことをしたまでだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x104,
        (
            "#0300Fそーそー。\x01",
            "あんまり気に病むことはないぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "#0504Fすみません……\x01",
            "本当にありがとうございました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_858")

    label("loc_7DE")


    #C0006
    ChrTalk(
        0xFE,
        (
            "#0504Fアルモリカの古戦場の件……\x01",
            "ありがとうございました。\x02\x03",

            "#0500F今後はもっと、徹底的に\x01",
            "巡回しないといけませんね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_858")

    Jump("loc_1876")

    label("loc_85D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_9DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93A")

    #C0007
    ChrTalk(
        0xFE,
        (
            "#0501F司令に無駄と切り捨てられて、\x01",
            "未だに調査されていない遺跡などが\x01",
            "クロスベルには多々あります。\x02\x03",

            "#0506F『星見の塔』のような\x01",
            "正体が分からないような場所は\x01",
            "いつ脅威になるか分からないのに……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_9D7")

    label("loc_93A")


    #C0008
    ChrTalk(
        0xFE,
        (
            "#0501F正式に調査の許可が下りれば、\x01",
            "『星見の塔』のような場所も\x01",
            "徹底的に調べるんですが……\x02\x03",

            "#0506F司令はあまりこういったことに\x01",
            "予算を割かせてくれません。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D7")

    Jump("loc_1876")

    label("loc_9DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_E00")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_A55")

    #C0009
    ChrTalk(
        0xFE,
        (
            "#0502F水際対策、成功したそうですね！\x02\x03",

            "私も手伝った甲斐がありました。\x01",
            "本当によかったです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DFB")

    label("loc_A55")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_AFE")

    #C0010
    ChrTalk(
        0xFE,
        (
            "#0503F偽ブランド業者については、\x01",
            "国境門でも頭を悩ませていた\x01",
            "問題なんです。\x02\x03",

            "#0501F今年は皆さんの協力もありますし、\x01",
            "何とか食い止めてみせましょう！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DFB")

    label("loc_AFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CFF")

    #C0011
    ChrTalk(
        0xFE,
        (
            "#0500F今日も警備隊員による\x01",
            "定期巡回が行なわれます。\x02\x03",

            "#0506F観光客の増えている今、\x01",
            "いつも以上の警戒が\x01",
            "必要なんですよね。\x02\x03",

            "#0501Fクロスベルにはこの間の\x01",
            "『星見の塔』のような\x01",
            "危険な場所もありますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        (
            "#0309Fハッハ、がんばれよ後輩。\x02\x03",

            "#0302Fま、何かあったら俺たちの力を\x01",
            "アテにしてもいいぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x103,
        (
            "#0202F……なるほど。\x01",
            "こういうのが先輩風を吹かす、ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x104,
        "#0310Fぐおっ……！？\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        (
            "#0104Fこーら、ティオちゃん。\x01",
            "ダメじゃない、ズバリ言っちゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#0306Fお、お嬢……\x01",
            "否定してくれよな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_DFB")

    label("loc_CFF")


    #C0017
    ChrTalk(
        0xFE,
        (
            "#0509Fえ～っと……ランディ先輩？\x01",
            "あたし、先輩風吹かされたなんて\x01",
            "全然思ってませんから……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x104,
        (
            "#0308Fハハ……\x01",
            "慰められると余計にな……\x02\x03",

            "#0306Fどーせ俺なんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "#0501Fうっ……\x01",
            "し、しっかりして下さいよ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#0006F悪ノリするなよランディ……\x02",
    )

    CloseMessageWindow()

    label("loc_DFB")

    Jump("loc_1876")

    label("loc_E00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_131C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_END)), "loc_1053")

    #C0021
    ChrTalk(
        0xFE,
        (
            "#0502Fあ……ロイドさん。\x01",
            "昨日はありがとうございました。\x02\x03",

            "#0504Fおかげでフランも\x01",
            "随分楽しんでくれたみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#0002Fいや、こっちこそ\x01",
            "誘ってくれてありがとう。\x02\x03",

            "#0004Fミニライブなんて\x01",
            "なかなか行く機会が無いし\x01",
            "楽しかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "#0509Fふふ、よかったです。\x02\x03",

            "#0500F……大丈夫、\x01",
            "チャンスはまた来ますよ。\x01",
            "めげずに頑張って下さいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#0012F（……やっぱり何か誤解されてるな……）\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x104,
        (
            "#0301F……つーか、美人姉妹と同伴かよ！\x01",
            "うらやましい奴だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x102,
        "#0106Fはぁ、うちの男どもは……\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x103,
        "#0211F……たらしばっかりです。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#0011F（……新たな誤解がっ！？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_129D")

    label("loc_1053")


    #C0029
    ChrTalk(
        0xFE,
        (
            "#0500Fあの……ロイドさん、ランディ先輩。\x01",
            "昨日、港湾区の公園で行われた\x01",
            "ミニライブに行きました？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#0005Fあれ？　なんでそれを……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "#0502Fやっぱり！\x01",
            "昨日、私も休みが取れたので\x01",
            "フランと行ってたんですよ。\x02\x03",

            "#0504Fなんだか見たような顔がいるなぁと\x01",
            "思ってたんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        (
            "#0302Fなんだなんだ、\x01",
            "声を掛けてくれりゃあよかったのによ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "#0509Fい、いやぁ……\x02\x03",

            "見たところ、女性を３人も連れて\x01",
            "楽しんでいらしたようですから\x01",
            "お邪魔かなあと……\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        "#0111Fふ～ん……？\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x103,
        "#0211F……随分お楽しみだったみたいですね。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        "#0309Fハッハッハ。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x101,
        "#0006F（な、なんか視線が痛いんだけど……）\x02",
    )

    CloseMessageWindow()

    label("loc_129D")

    SetScenarioFlags(0x0, 2)
    Jump("loc_1317")

    label("loc_12A5")


    #C0038
    ChrTalk(
        0xFE,
        (
            "#0504F昨日は久しぶりの休暇で\x01",
            "足を伸ばすことができました。\x02\x03",

            "#0502Fフランも元気にしてるみたいで\x01",
            "良かったです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1317")

    Jump("loc_1876")

    label("loc_131C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_132A")
    Jump("loc_1876")

    label("loc_132A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_13BB")

    #C0039
    ChrTalk(
        0xFE,
        (
            "#0500F今から街道の定期巡回に\x01",
            "出かける所なんです。\x02\x03",

            "#0503F危険な場所も多いですから\x01",
            "観光客が入り込まないように\x01",
            "注意しないと……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1876")

    label("loc_13BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1876")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1464")

    #C0040
    ChrTalk(
        0xFE,
        (
            "#0503F皆さんの戦いぶりをみていると、\x01",
            "私もまだまだだと思いました。\x02\x03",

            "#0501Fもっと訓練に励まないと、\x01",
            "クロスベルを守ることなど\x01",
            "できませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1876")

    label("loc_1464")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_14E4")

    #C0041
    ChrTalk(
        0xFE,
        (
            "#0500F皆さんと演習を行えば、\x01",
            "新人隊員にとっても\x01",
            "いい訓練になると思います。\x02\x03",

            "どうかよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1876")

    label("loc_14E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1582")

    #C0042
    ChrTalk(
        0xFE,
        (
            "#0500F特務支援課の皆さん……\x01",
            "どうも、お疲れ様です。\x02\x03",

            "ソーニャ副司令が\x01",
            "支援要請について\x01",
            "お話したいそうです。\x02\x03",

            "一度聞いていただけますか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1876")

    label("loc_1582")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17F0")

    #C0043
    ChrTalk(
        0xFE,
        (
            "#0508Fあっ、皆さん……\x01",
            "お疲れ様です。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#0005F……どうしたんだ？\x01",
            "なんだか元気がないみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "#0506F……先日の魔獣事件の犯人である\x01",
            "マフィアの手下たちですが……\x02\x03",

            "#0508Fついこの間、\x01",
            "保釈されてしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#0108F……そう……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x103,
        "#0203F……保釈金が支払われたんですね。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        (
            "#0306Fおいおい、あんま暗くなんなって。\x02\x03",

            "#0300Fある程度予測できてたことだし、\x01",
            "今回のことは仕方ねぇだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#0000F……そうだな。\x01",
            "きっとこんな体制も\x01",
            "徐々によくしていけるはずさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "#0503F……そう、ですね。\x01",
            "今出来ることをやっていくしか\x01",
            "ありませんよね。\x02\x03",

            "#0502Fありがとうございます。\x01",
            "少し気が楽になりました。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1876")

    label("loc_17F0")


    #C0051
    ChrTalk(
        0xFE,
        (
            "#0500Fありがとうございます。\x01",
            "少し気が楽になりました。\x02\x03",

            "#0503Fとにかく、今は警備隊の出来る範囲で\x01",
            "やれることをやっていかないと……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1876")

    TalkEnd(0xFE)
    Return()

    # Function_4_4EE end

    def Function_5_187A(): pass

    label("Function_5_187A")

    OP_4B(0x9, 0xFF)
    OP_4B(0x8, 0xFF)
    SetChrSubChip(0x9, 0x0)
    TurnDirection(0x8, 0x9, 0)

    #C0052
    ChrTalk(
        0x9,
        (
            "#2003Fなるほど……\x01",
            "これが例の遺跡での\x01",
            "調査結果というわけね。\x02\x03",

            "#2002Fよく調べてくれたわ、ノエル。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "#0504Fいえ、特務支援課の方たちの\x01",
            "協力があってこそでした。\x02\x03",

            "#0501Fそれで……\x01",
            "今後、この件はどういたしましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x9,
        (
            "#2003F……報告書に書かれている\x01",
            "この“魔物”を呼ぶ《鐘》……\x02\x03",

            "#2001Fやはり、古代遺物#8Rアーティファクト#に関わるものである\x01",
            "可能性は高そうだわ。\x02\x03",

            "クロスベル大聖堂のエラルダ大司教に\x01",
            "意見を聞いてみましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "#0503Fそうですね……分かりました。\x02\x03",

            "#0501Fでは早速、大聖堂に連絡を入れて\x01",
            "直接話を伺えないか確認します。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x9,
        "#2000Fええ、よろしくお願いするわ。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x9, 0xFF)
    OP_4C(0x8, 0xFF)
    Return()

    # Function_5_187A end

    def Function_6_1AD6(): pass

    label("Function_6_1AD6")

    Call(0, 7)
    Return()

    # Function_6_1AD6 end

    def Function_7_1ADA(): pass

    label("Function_7_1ADA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1B6E")
    Jump("loc_1BB8")

    label("loc_1B6E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1B8E")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BB8")

    label("loc_1B8E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BAE")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1BB8")

    label("loc_1BAE")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BB8")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1FF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F18")

    #C0057
    ChrTalk(
        0x9,
        (
            "#2005Fあら、あなたたち。\x02\x03",

            "#2000F今、ノエル曹長が\x01",
            "例の遺跡の資料を持って\x01",
            "大聖堂に向かっているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#0000F七耀教会と協力する事に\x01",
            "したんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        (
            "#0301F……司令のヤツに\x01",
            "許可はとらなくていいんスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "#2003F……実は、前の《星見の塔》の\x01",
            "再調査の件は蹴られてしまってね。\x02\x03",

            "#2000F似た案件であるこちらも、\x01",
            "もう大司教様に委ねた方がいいと\x01",
            "判断したの。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        "#0003Fそうでしたか……\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        (
            "#0103F……自分の目で見ていないから\x01",
            "緊急性が判断できないのか、それとも……\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x103,
        (
            "#0200F……単に警備隊の管轄にするのが\x01",
            "面倒だからか、ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        "#0301Fケッ……その両方だろ。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1E72")

    #C0065
    ChrTalk(
        0x10A,
        (
            "#0603F警備隊の腐敗もかなり進んでいると\x01",
            "いうわけですか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E72")


    #C0066
    ChrTalk(
        0x9,
        (
            "#2003F……ともかく、\x01",
            "この件は七耀教会とタングラム部隊で\x01",
            "少しずつ進めていくわ。\x02\x03",

            "#2000Fあなた達の協力で\x01",
            "ここまでこぎつける事が出来た。\x01",
            "改めて礼を言うわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1FF1")

    label("loc_1F18")


    #C0067
    ChrTalk(
        0x9,
        (
            "#2003F《星見の塔》、そして例の遺跡……\x02\x03",

            "#2000Fこの２つの件は古代遺物#8Rアーティファクト#が\x01",
            "関わっている可能性がある以上、\x01",
            "慎重に扱わなければならないわ。\x02\x03",

            "今後は七耀教会と連携して\x01",
            "調査していく事になるでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FF1")

    Jump("loc_3FD8")

    label("loc_1FF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2106")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2014")
    Call(0, 5)
    SetScenarioFlags(0x0, 1)
    Jump("loc_2101")

    label("loc_2014")


    #C0068
    ChrTalk(
        0x9,
        (
            "#2000Fあなたたち……\x01",
            "昨日はご苦労だったわね。\x02\x03",

            "#2003F遺跡の調査を遂行し、\x01",
            "原因は不明ながら魔獣が発生する現象を\x01",
            "止めることもできた。\x02\x03",

            "現時点ではこれ以上ない\x01",
            "成果と言えるでしょう。\x02\x03",

            "#2000F後の調査は、私たち警備隊に\x01",
            "任せてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2101")

    Jump("loc_3FD8")

    label("loc_2106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2529")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2447")

    #C0069
    ChrTalk(
        0x9,
        (
            "#2000Fノエル曹長……\x01",
            "首尾よく彼らの協力を得られたようね。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x109,
        "#0500Fはい、快くＯＫしていただきました。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x102,
        (
            "#0109Fも、もちろんですとも。\x01",
            "おほほ……\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#0004Fエリィ、本当に大丈夫か？\x01",
            "テンションがおかしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x102,
        (
            "#0107Fだ、大丈夫って言ってるでしょう！\x02\x03",

            "#0112Fいいから、調査に行くなら\x01",
            "さっさと行きましょう！\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x104,
        "#0305Fお嬢、すげぇ剣幕だな……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        (
            "#0203F……まぁ、エリィさんは\x01",
            "肝が据わっているほうですし、\x01",
            "この調子なら大丈夫かと。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        (
            "#2000Fふふ……相変わらず賑やかね。\x02\x03",

            "#2003F……警備隊による遺跡の調査は\x01",
            "一度、失敗してしまっているわ。\x02\x03",

            "このまま失敗を重ねると、\x01",
            "司令閣下に調査を取りやめるよう\x01",
            "指示が下る可能性は高いでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x104,
        "#0303F……そうッスね。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x9,
        (
            "#2000F……でも、もちろん\x01",
            "あなた達の安全が最優先よ。\x01",
            "重々、気を付けて行ってちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        (
            "#0001F分かりました。\x01",
            "心に留めておきます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2524")

    label("loc_2447")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9D, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2459")
    Call(0, 8)
    Jump("loc_2524")

    label("loc_2459")


    #C0080
    ChrTalk(
        0x9,
        (
            "#2000F警備隊による遺跡の調査は\x01",
            "一度、失敗してしまっているわ。\x02\x03",

            "#2003F負傷者こそ出ていないものの、\x01",
            "化け物に出会ったショックで\x01",
            "寝込んでしまった隊員もいる……\x02\x03",

            "#2000F重々、気を付けて行ってちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2524")

    Jump("loc_3FD8")

    label("loc_2529")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2820")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2736")

    #C0081
    ChrTalk(
        0x9,
        "#2006F…………………………\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#0005F……え、えっと……ソーニャ副司令？\x01",
            "俺たちがなにか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        (
            "#2003F……いいえ。\x02\x03",

            "あなた達が、\x01",
            "私のよく知る顔をしていたようだから。\x02\x03",

            "#2000F規律から外れたことをしようとしてる……\x01",
            "そんな時の顔をね。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        "#0005F（ギクッ……）\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        (
            "#0101F（競売会のこと……\x01",
            "  なんとなく気づいてるみたいね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x103,
        "#0200F（女のカンってやつでしょうか。）\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x104,
        "#0306F（い、嫌になる鋭さだぜ……）\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x9,
        (
            "#2004F……ふふ、\x01",
            "変なことを言ってしまったわね。\x01",
            "あまり気にしないでちょうだい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_281B")

    label("loc_2736")


    #C0089
    ChrTalk(
        0x9,
        (
            "#2003Fこの間の魔獣事件の時みたいに\x01",
            "無理をしてはいけないわよ。\x02\x03",

            "#2000F何か大事に当たるというなら、\x01",
            "まずはセルゲイにでも相談なさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#0001Fは、はぁ……\x02\x03",

            "#0006F（課長には止められてることだから\x01",
            "  相談できないんだよな……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_281B")

    Jump("loc_3FD8")

    label("loc_2820")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2C71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BD0")
    SetChrSubChip(0x9, 0x0)

    #C0091
    ChrTalk(
        0x9,
        "#2003F……うん、これでいいわね。\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#0005F副司令……\x01",
            "何をしてたんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0x9)
    ClearChrFlags(0x9, 0x10)
    TurnDirection(0x9, 0x0, 0)
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_291C")
    Jump("loc_2966")

    label("loc_291C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_293C")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2966")

    label("loc_293C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_295C")
    OP_52(0x9, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2966")

    label("loc_295C")

    OP_52(0x9, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x9, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2966")

    OP_52(0x9, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x10)

    #C0093
    ChrTalk(
        0x9,
        (
            "#2000Fえぇ……\x01",
            "例の《星見の塔》についての\x01",
            "書類がまとまったの。\x02\x03",

            "司令がお戻りになったら\x01",
            "この資料をもとに\x01",
            "調査隊の編成を直訴してみるつもりよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x104,
        (
            "#0301F……大丈夫ッスか？\x02\x03",

            "#0303Fあの司令のことだ、\x01",
            "どーせ突っぱねられちまうんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x9,
        (
            "#2003F……えぇ、その可能性は高いでしょうね。\x02\x03",

            "#2000Fでも、それなら別のアプローチで\x01",
            "解決策を考えてみればいい。\x02\x03",

            "前にも言ったように、\x01",
            "私達が諦めてしまえば\x01",
            "本当にダメになってしまうことがある。\x02\x03",

            "#2002Fだったらやれるだけのことは\x01",
            "やってみる必要があるでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x102,
        "#0103Fそうですね……\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        "#0000F俺たちも、今やれることをやらないとな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C6C")

    label("loc_2BD0")


    #C0098
    ChrTalk(
        0x9,
        (
            "#2000F司令がお戻りになったら\x01",
            "この資料をもとに\x01",
            "調査隊の編成を直訴してみるつもりよ。\x02\x03",

            "ダメだったら、\x01",
            "より説得力のある資料を作って\x01",
            "また突きつけるだけよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C6C")

    Jump("loc_3FD8")

    label("loc_2C71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_346B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2D3F")

    #C0099
    ChrTalk(
        0x9,
        (
            "#2000F先程、警察本部の\x01",
            "ドノバン警部という方から\x01",
            "連絡があったわ。\x02\x03",

            "無事偽ブランド業者を\x01",
            "確保できたそうね。\x02\x03",

            "#2004Fふふ……あなた達も捜査官として\x01",
            "ようやく板についてきたかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3466")

    label("loc_2D3F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_2FD4")

    #C0100
    ChrTalk(
        0x9,
        (
            "#2003F共和国からバスが来るまで\x01",
            "少し時間があるわ。\x02\x03",

            "#2000F今から門の中で待機していれば\x01",
            "休憩する時間は充分にあるでしょう。\x02\x03",

            "どうする？　よければ部屋を\x01",
            "用意させてもらうけれど。\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【まだ準備が出来ていない】\x01",          # 0
            "【共和国からの旅客バスを待つ】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2E5B"),
        (1, "loc_2EEA"),
        (SWITCH_DEFAULT, "loc_2FCF"),
    )


    label("loc_2E5B")

    OP_60(0x0)

    #C0101
    ChrTalk(
        0x101,
        (
            "#0001Fそうですね……\x01",
            "できれば少し、準備したいところです。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "#2004Fそう、了解したわ。\x02\x03",

            "#2000F準備が出来たらまた声をかけて頂戴。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FCF")

    label("loc_2EEA")

    OP_60(0x0)

    #C0103
    ChrTalk(
        0x101,
        (
            "#0000Fでは、お言葉に\x01",
            "甘えさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        (
            "#2004F了解したわ。\x02\x03",

            "#2000F共和国のバスが到着したら\x01",
            "あなた達を呼ばせるようにします。\x02\x03",

            "それまで体を休ませておきなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        "#0000Fはい！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x1B, 0x1, 0x3)
    SetScenarioFlags(0x5C, 0)
    NewScene("t2510", 0, 0, 0)
    IdleLoop()
    Jump("loc_2FCF")

    label("loc_2FCF")

    Jump("loc_3466")

    label("loc_2FD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3386")

    #C0106
    ChrTalk(
        0x9,
        (
            "#2002F……聞いたわよ。\x01",
            "不良グループと遊撃士を相手に\x01",
            "大立ち回りを演じたそうじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x104,
        "#0306Fげげっ……伝わっちまってたか。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#0006Fあ、あの。\x01",
            "昨日のはワケがありまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        (
            "#2003F言い訳は結構。\x01",
            "いくら不良グループ相手とはいえ\x01",
            "警察が一般人に手を上げるなんて……\x02\x03",

            "#2000F……と、本来なら言う所でしょうけど。\x01",
            "私からは何も無いわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x104,
        "#0305Fへ……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "#2003F本来の警察業務なら、\x01",
            "嫌が応にも対象を抑えつけることで\x01",
            "事態の収拾を図るしかない。\x02\x03",

            "#2000Fけど、『特務支援課』のあなた達は\x01",
            "警察でもイレギュラーな存在……\x01",
            "もっと色々なやり方があっていい。\x02\x03",

            "#2004Fうっ憤の溜まった不良が相手なら、\x01",
            "力を発散する場を設けて収める……\x01",
            "悪くないと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x103,
        (
            "#0200F……副司令がそんなことを言って\x01",
            "大丈夫ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x9,
        (
            "#2004Fセルゲイが何も言わない以上\x01",
            "私が偉そうに叱る理由はないでしょう？\x02\x03",

            "#2000Fふふ……これからも\x01",
            "その調子で頑張りなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        "#0005Fは……はい。\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x102,
        (
            "#0100F（……物事への柔軟な対応……\x01",
            "  ほんと、理想の上司って感じね。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3466")

    label("loc_3386")


    #C0116
    ChrTalk(
        0x9,
        (
            "#2004Fセルゲイが何も言わない以上\x01",
            "私が偉そうに叱る理由はないわ。\x01",
            "その調子で頑張りなさい。\x02\x03",

            "#2000Fだけど、普通と違うやり方は\x01",
            "得てして先が読みにくいものよ。\x02\x03",

            "選択した行動がどんな結末を呼ぶか……\x01",
            "よく考えて行動することね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3466")

    Jump("loc_3FD8")

    label("loc_346B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_36D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35DE")

    #C0117
    ChrTalk(
        0x9,
        (
            "#2000Fあら、あなた達……\x01",
            "記念祭は楽しんでいるかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x104,
        (
            "#0306Fいやいや、分かってるでしょう？\x01",
            "こっちもこっちで大忙しッスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#0000Fま、まぁまぁ。\x01",
            "初日に休暇を貰えただけでも\x01",
            "よしとしようじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x9,
        (
            "#2003F英気は充分養えたようね。\x02\x03",

            "#2000F記念祭中は色々と\x01",
            "トラブルが多いと思うけど……\x02\x03",

            "力の見せ所と思って\x01",
            "しっかり頑張るといいわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_36CF")

    label("loc_35DE")


    #C0121
    ChrTalk(
        0x9,
        (
            "#2000Fさて、中々手を付けられなかったけど……\x01",
            "先日の《星見の塔》の資料を\x01",
            "纏めるとしましょう。\x02\x03",

            "#2003Fノエル曹長の報告では、\x01",
            "あまり放置していい類のものでは\x01",
            "無かったそうだし……\x02\x03",

            "#2000F可能なら近いうちに\x01",
            "調査隊を編成する必要がありそうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36CF")

    Jump("loc_3FD8")

    label("loc_36D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_39A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3954")

    #C0122
    ChrTalk(
        0x9,
        "#2005F……あら、何か用かしら？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 1)), scpexpr(EXPR_END)), "loc_3868")

    #C0123
    ChrTalk(
        0x101,
        (
            "#0003F（そうだ、星見の塔の探索……\x01",
            "  副司令に許可を取ったほうがいいかな？）\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        (
            "#0303F（んー、とりあえず、\x01",
            "  それは黙っとこうぜ。）\x02\x03",

            "#0300F（色々と面倒そうだしよ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            "#0006F（う、うーん。\x01",
            "  本当にいいのかな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x9,
        (
            "#2005F……？\x01",
            "なにをひそひそと話しているの？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        "#0011Fな、なんでもありません。\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    Jump("loc_394C")

    label("loc_3868")


    #C0128
    ChrTalk(
        0x101,
        "#0000Fいえ、偶然近くまで来たもので。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x103,
        (
            "#0205F……そういえば、\x01",
            "ノエル曹長の姿を見かけませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x9,
        (
            "#2000F彼女なら今、\x01",
            "街道の定期巡回に行っているわ。\x02\x03",

            "戻るのは夕方以降になるでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x102,
        "#0103Fうーん、忙しそうね……\x02",
    )

    CloseMessageWindow()

    label("loc_394C")

    SetScenarioFlags(0x0, 1)
    Jump("loc_399F")

    label("loc_3954")


    #C0132
    ChrTalk(
        0x9,
        (
            "#2003F悪いけれど、今日は忙しいの。\x01",
            "用があるなら後日にしてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_399F")

    Jump("loc_3FD8")

    label("loc_39A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3B68")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3AA7")

    #C0133
    ChrTalk(
        0x9,
        (
            "#2000F少し前に、\x01",
            "この門から共和国の町の間で\x01",
            "導力車が不審な事故にあったの。\x02\x03",

            "#2003F気になって調べてみたら、\x01",
            "どうやら以前の魔獣騒動を起こした\x01",
            "ルバーチェの所有するナンバーだったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        "#0000F（……もしかして……黒月の仕業か？）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3B63")

    label("loc_3AA7")


    #C0135
    ChrTalk(
        0x9,
        (
            "#2003F少し前にこのあたりで起こった\x01",
            "マフィアの導力車の不審な事故……\x02\x03",

            "#2001F……ルバーチェが被害者である以上、\x01",
            "ただの事故とも思えないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x101,
        "#0001F（さすが副司令、するどいな……）\x02",
    )

    CloseMessageWindow()

    label("loc_3B63")

    Jump("loc_3FD8")

    label("loc_3B68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3FD8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3C1D")

    #C0137
    ChrTalk(
        0x9,
        (
            "#2000Fあなたたちも、\x01",
            "これから精進しつづけて頂戴。\x02\x03",

            "また協力が必要な時は、\x01",
            "支援要請の形で連絡を取ります。\x02\x03",

            "特務支援課の活動、\x01",
            "陰ながら応援しているわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FD8")

    label("loc_3C1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x1, 0x0)"), scpexpr(EXPR_END)), "loc_3C7A")

    #C0138
    ChrTalk(
        0x9,
        (
            "#2000Fすぐにでも演習は開始できるわ。\x02\x03",

            "戦う準備は出来ているかしら？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 13)
    Jump("loc_3FD8")

    label("loc_3C7A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_3C8E")
    Call(0, 12)
    Jump("loc_3FD8")

    label("loc_3C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EEE")

    #C0139
    ChrTalk(
        0x9,
        (
            "#2005Fあら……あなた達が\x01",
            "直接ここに来るなんて珍しいわね。\x01",
            "何かあったのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        (
            "#0000Fいえ、たまたま近くまで\x01",
            "来たものですから挨拶に伺おうかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x104,
        (
            "#0303F#2S俺はあんまり\x01",
            "来たくなかったんだけどな……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x9,
        (
            "#2004F……あら、それなのにわざわざ\x01",
            "会いに来てくれたの？\x01",
            "見かけによらず殊勝なことね。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x104,
        (
            "#0305Fどわっ！？\x01",
            "……き、聞こえてたんスか。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x9,
        (
            "#2002Fふふ、顔を見たら大体分かるわ。\x01",
            "それはともかく……\x02\x03",

            "#2003F先日の魔獣事件のように、\x01",
            "今後も何かと協力してもらうことが\x01",
            "あるでしょう。\x02\x03",

            "#2000F何かあったら頼ってちょうだい。\x01",
            "出来る限り力になるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        "#0000Fはい、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3FD8")

    label("loc_3EEE")


    #C0146
    ChrTalk(
        0x9,
        (
            "#2003Fクロスベルの抱える腐敗は\x01",
            "この警備隊にも及んでいる……\x02\x03",

            "#2000Fだけど、しがらみに囚われないあなた達なら\x01",
            "警備隊にどうしようもできない事件も\x01",
            "解決できることがあると思うわ。\x02\x03",

            "何かあったら頼ってちょうだい。\x01",
            "出来る限り力になるわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FD8")

    SetChrSubChip(0x9, 0x0)
    TalkEnd(0x9)
    Return()

    # Function_7_1ADA end

    def Function_8_3FE0(): pass

    label("Function_8_3FE0")


    #C0147
    ChrTalk(
        0x9,
        (
            "#2000Fそういえば……\x01",
            "あなた達、本は読む方かしら？\x02\x03",

            "もし良かったら\x01",
            "これを受け取って頂戴。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0148
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2D1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0149
    ChrTalk(
        0x104,
        (
            "#0300Fへぇ……副司令も\x01",
            "娯楽小説なんて読むんッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x9,
        (
            "#2003F娯楽小説だろうが啓蒙書だろうが、\x01",
            "文字を読むことは教養の面で\x01",
            "とてもいい事よ。\x02\x03",

            "#2002F少なくとも、あなたが愛読してる\x01",
            "女性のあられもない姿が載った\x01",
            "雑誌よりは何倍もマシだと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        (
            "#0306Fグラビアもいいもんだと\x01",
            "思うけどなぁ……\x02\x03",

            "#0309Fもはや切っても切り離せない\x01",
            "俺の活力の源ッスからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        "#0006F（やれやれ……）\x02",
    )

    CloseMessageWindow()
    AddItemNumber(0x2D1, 1)
    SetScenarioFlags(0x9D, 3)
    Return()

    # Function_8_3FE0 end

    def Function_9_420F(): pass

    label("Function_9_420F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_42D0")

    #C0153
    ChrTalk(
        0xFE,
        (
            "念のため、昨日のうちに\x01",
            "ノエル曹長が指揮する部隊で\x01",
            "例の遺跡の調査に行ったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "やはり、もう不気味な魔獣は\x01",
            "出現しなくなっているようですね。\x01",
            "とりあえず安心しました。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AA9")

    label("loc_42D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4470")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43C3")

    #C0155
    ChrTalk(
        0xFE,
        (
            "警備隊員だけじゃ調査できなかった\x01",
            "あの遺跡を、ノエル曹長と\x01",
            "あなたたちだけで調査できるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "あなたたちの個々のポテンシャルは\x01",
            "私たち以上ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "ソーニャ副司令の部下として、\x01",
            "負けていられません……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_446B")

    label("loc_43C3")


    #C0158
    ChrTalk(
        0xFE,
        (
            "ソーニャ副司令とノエル曹長は\x01",
            "今、副司令室で重要なことを\x01",
            "話し合っているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "副司令がお礼を言いたいと\x01",
            "仰っていました。\x01",
            "よろしければお会いになって下さい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_446B")

    Jump("loc_4AA9")

    label("loc_4470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4509")

    #C0160
    ChrTalk(
        0xFE,
        (
            "バレルさんはすっかり\x01",
            "寝込んでしまっていますが、\x01",
            "外傷などは殆どありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        (
            "しばらく休息をとれば\x01",
            "問題なく復帰できると思いますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AA9")

    label("loc_4509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4564")

    #C0162
    ChrTalk(
        0xFE,
        (
            "自分も、ここで休んでる暇はありませんね。\x01",
            "皆さんの手伝いに行かないと……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AA9")

    label("loc_4564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4629")

    #C0163
    ChrTalk(
        0xFE,
        (
            "警備隊の訓練は、\x01",
            "警察学校の警備科で受けるんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xFE,
        (
            "ノエル曹長は女性隊員としては\x01",
            "かなり優秀な成績で卒業したそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "自分も負けてはいられませんね。\x01",
            "精進しないと……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AA9")

    label("loc_4629")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_46C8")

    #C0166
    ChrTalk(
        0xFE,
        (
            "ソーニャ副司令は、\x01",
            "実力があれば女性隊員でも\x01",
            "平等に評価してくれるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xFE,
        (
            "その分、人一倍努力が必要ですけど……\x01",
            "やりがいはありますよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AA9")

    label("loc_46C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4866")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47D6")

    #C0168
    ChrTalk(
        0xFE,
        (
            "昨日はノエル曹長もソーニャ副司令も\x01",
            "非番で休みだったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        (
            "ノエル曹長は妹さんと\x01",
            "出かけたらしいんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "……ソーニャ副司令は\x01",
            "何してたんでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "興味はあるんですけど\x01",
            "あまり生活感の無い人ですから\x01",
            "想像つかないなぁ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4861")

    label("loc_47D6")


    #C0172
    ChrTalk(
        0xFE,
        (
            "ソーニャ副司令は\x01",
            "現在独身みたいですし……\x01",
            "もしかして、浮いた話が……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "仕事中に世間話すると叱られるので\x01",
            "なかなか聞けません……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4861")

    Jump("loc_4AA9")

    label("loc_4866")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_48F0")

    #C0174
    ChrTalk(
        0xFE,
        (
            "警備隊員は基本的に、\x01",
            "勤務する門に待機しなければいけません。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        (
            "普段はノエル曹長たちも\x01",
            "こちらで寝泊りしてるんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AA9")

    label("loc_48F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4AA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A16")

    #C0176
    ChrTalk(
        0xFE,
        (
            "ソーニャ副司令は、警察のセルゲイ課長と\x01",
            "以前から付き合いがあるそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "時々、導力通信で直接連絡を\x01",
            "とっているようですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "……よく考えると、\x01",
            "なんだか、アヤしい関係ですね。\x01",
            "もしかして…………？\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "……こほん、失礼しました。\x01",
            "今の話は忘れてください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4AA9")

    label("loc_4A16")


    #C0180
    ChrTalk(
        0xFE,
        "アヤしい関係であるかはさておき……\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "上司に繋がりがあると\x01",
            "組織同士の連携もしやすいと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        "お互い、今後も頑張っていきましょうね。\x02",
    )

    CloseMessageWindow()

    label("loc_4AA9")

    TalkEnd(0xFE)
    Return()

    # Function_9_420F end

    def Function_10_4AAD(): pass

    label("Function_10_4AAD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BD6")

    #C0183
    ChrTalk(
        0xFE,
        "……う～ん……ば、化け物……\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x109,
        (
            "#0503F彼は例の遺跡の調査で\x01",
            "魔獣に鉢合わせしてしまったんです。\x02\x03",

            "#0501Fあまり気の大きい方でないので\x01",
            "失神してしまって……\x01",
            "やむなく一旦退却したんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x102,
        "#0101F（ごくり……）\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x101,
        (
            "#0001F……これは、心の準備を\x01",
            "していった方がよさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4BF2")

    label("loc_4BD6")


    #C0187
    ChrTalk(
        0xFE,
        "うう……ば、化け物……\x02",
    )

    CloseMessageWindow()

    label("loc_4BF2")

    TalkEnd(0xFE)
    Return()

    # Function_10_4AAD end

    def Function_11_4BF6(): pass

    label("Function_11_4BF6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CA3")

    #C0188
    ChrTalk(
        0xFE,
        (
            "こっちは乗客の待合室じゃ\x01",
            "なかったみたいですね。\x01",
            "私ったらうっかり……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "それにしても、ここはなんだか\x01",
            "散らかってる気がします。\x01",
            "そ、掃除したい……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4CFA")

    label("loc_4CA3")


    #C0190
    ChrTalk(
        0xFE,
        (
            "せっかくの旅行中に\x01",
            "掃除したくなるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        "メイドの性というものでしょうか。\x02",
    )

    CloseMessageWindow()

    label("loc_4CFA")

    TalkEnd(0xFE)
    Return()

    # Function_11_4BF6 end

    def Function_12_4CFE(): pass

    label("Function_12_4CFE")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x8, 0xE1, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_68(3870, 1200, -590, 0)
    MoveCamera(55, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25200, 0)
    SetChrPos(0x101, 3000, 0, 0, 90)
    SetChrPos(0x102, 3000, 0, -1500, 90)
    SetChrPos(0x103, 1500, 0, -1500, 90)
    SetChrPos(0x104, 1500, 0, 0, 90)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    #C0192
    ChrTalk(
        0x9,
        (
            "#11P#2002Fフフ……ようやく来たわね。\x02\x03",

            "待っていたわ、特務支援課の諸君。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x8,
        "#5P#0500Fお疲れ様です。\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x101,
        (
            "#6P#0000Fお疲れ様です、\x01",
            "ソーニャ副司令、ノエル曹長。\x02\x03",

            "支援要請を確認して\x01",
            "こちらに伺ったのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x104,
        (
            "#6P#0300F#2S俺はあんまり\x01",
            "来たくなかったんだけどな……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x9,
        (
            "#11P#2004F……あら、それなのにわざわざ\x01",
            "会いに来てくれたの？\x02\x03",

            "見かけによらず殊勝なことね。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x104,
        (
            "#6P#0305Fどわっ！？\x01",
            "……き、聞こえてたんスか。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x9,
        (
            "#11P#2004Fふふ、顔を見たら大体分かるわ。\x02\x03",

            "#2000Fさて、要請について\x01",
            "早速話をしたいのだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        "#6P#0100Fええ、よろしくお願いします。\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x9,
        (
            "#11P#2000Fふふ、結構。\x01",
            "ではノエル曹長、お願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x8,
        (
            "#5P#0501Fハッ。\x02\x03",

            "今回、皆さんにお願いしたいのは\x01",
            "他でもありません。\x02\x03",

            "#0503F今日行なわれる、\x01",
            "警備隊の新人隊員たちの実戦演習……\x02\x03",

            "#0501Fその相手を皆さんに\x01",
            "務めていただきたいのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x101,
        "#6P#0005F警備隊員との実戦演習か……\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x102,
        (
            "#6P#0100F例え新人とはいえ、\x01",
            "相当な実力者揃いには\x01",
            "違いないですよね。\x02\x03",

            "警備隊は戦闘のエリートが\x01",
            "集まっていると聞きますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x9,
        (
            "#11P#2002Fフフ……よくご存知ね。\x02\x03",

            "#2003F彼らと訓練を行なうことで、\x01",
            "あなた達も実力を高められる……\x01",
            "悪い話ではないでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x103,
        (
            "#6P#0200F……そもそも、\x01",
            "なぜわたしたちに要請を？\x02\x03",

            "#0203Fこう言っては何ですが、\x01",
            "戦闘に秀でた人物は\x01",
            "他にいくらでもいるかと思いますが。\x02\x03",

            "#0200Fたとえば……遊撃士とか。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x101,
        "#6P#0011Fお、おいおいティオ……\x02",
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x104,
        (
            "#6P#0303F……いや！\x01",
            "俺もティオすけと同じ意見だぜ。\x02\x03",

            "訓練だって、より強い相手と\x01",
            "やった方が良いに決まってらぁ。\x02\x03",

            "#0309Fなんだったら、今からでも\x01",
            "遊撃士に依頼しなおした方が\x01",
            "よくないッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x9,
        (
            "#11P#2004Fふふ……\x01",
            "あなたの場合、理由をつけて\x01",
            "私から逃げているように聞こえるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x104,
        "#6P#0306Fぎくっ。\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x9,
        (
            "#11P#2003Fでも……否定はしないわ。\x02\x03",

            "出来て１、２ヶ月程度の支援課よりも\x01",
            "ベテランの遊撃士たちの方が\x01",
            "恐らく実力は上でしょう。\x02\x03",

            "#2000Fだけど、あなた達は\x01",
            "警備隊に片付けられなかった\x01",
            "魔獣事件を解決に導いた実績がある。\x02\x03",

            "そこには、単純な腕力だけではない\x01",
            "あなた達だけの力を感じるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x101,
        "#6P#0005F俺たちだけの……\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x8,
        (
            "#5P#0500Fランディ先輩も、\x01",
            "ベルガード門では\x01",
            "名を馳せた実力者ですし……\x02\x03",

            "決して遊撃士にも\x01",
            "見劣りしない人材だと\x01",
            "考えられるかと思います。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_55EC():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55EC)
    Sleep(100)

    def lambda_55FC():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_55FC)
    Sleep(50)

    def lambda_560C():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_560C)
    Sleep(800)

    #C0213
    ChrTalk(
        0x101,
        "#6P#0005Fそ、そうなのか！？\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x103,
        "#6P#0205F初耳です。\x02",
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x102,
        (
            "#6P#0105F本当、驚きね。\x02\x03",

            "#0100Fせっかくだから\x01",
            "教えてくれてもよかったのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x104,
        (
            "#6P#0300F……ま、昔の話だしな。\x01",
            "ペラペラ語るもんじゃねぇさ。\x02\x03",

            "#0306Fしっかしなぁ、\x01",
            "やっぱ乗り気がしねぇっつーか……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x9,
        (
            "#11P#2003F別に私は、あなただけ不参加でも\x01",
            "構わないのよ。\x02\x03",

            "#2002Fあなたを支援課に推薦してあげた私に、\x01",
            "何の恩義も感じていないなら……ね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_57AB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_57AB)
    Sleep(100)

    def lambda_57BB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_57BB)
    Sleep(50)

    def lambda_57CB():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_57CB)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0218
    ChrTalk(
        0x104,
        (
            "#6P#0306Fうぐっ……！\x01",
            "そいつを言われるとツラいッス……\x02\x03",

            "#0301Fわ、わーったよ！\x01",
            "やりゃあいいんでしょ、やりゃあ！\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x9,
        "#11P#2003F……結構。\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x101,
        (
            "#6P#0012F（この先もずっとこの調子で\x01",
            "  コキ使われそうだな……）\x02\x03",

            "#0003Fま、まぁともかく。\x01",
            "事情は大体把握しました。\x02\x03",

            "#0000F演習ですが……\x01",
            "いつ頃から開始しますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x9,
        (
            "#11P#2000F隊員たちに一声かければ、\x01",
            "すぐにでも開始できるわ。\x02\x03",

            "あなたたちも\x01",
            "戦う準備は出来ているかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0xF, 0x1, 0x0)
    Call(0, 13)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 3000, 0, 0, 90)
    SetChrPos(0x1, 3000, 0, 0, 90)
    SetChrPos(0x2, 3000, 0, 0, 90)
    SetChrPos(0x3, 3000, 0, 0, 90)
    OP_68(3000, 900, 0, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    OP_4C(0x8, 0xFF)
    OP_93(0x8, 0x10E, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_12_4CFE end

    def Function_13_5A30(): pass

    label("Function_13_5A30")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【準備が出来ていない】\x01",      # 0
            "【演習を開始する】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5A7C"),
        (1, "loc_5B18"),
        (SWITCH_DEFAULT, "loc_5C6A"),
    )


    label("loc_5A7C")

    OP_60(0x0)

    #C0222
    ChrTalk(
        0x101,
        (
            "#6P#0006Fすみません、\x01",
            "ちょっと装備が\x01",
            "心許ないというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x9,
        (
            "#11P#2004Fそう、分かったわ。\x02\x03",

            "#2000F戦う準備が出来たら\x01",
            "もう一度声をかけて頂戴。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C6A")

    label("loc_5B18")

    OP_4B(0x8, 0xFF)
    OP_60(0x0)

    #C0224
    ChrTalk(
        0x101,
        "#6P#0000Fええ、大丈夫です。\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x9,
        (
            "#11P#2004Fそう。\x02\x03",

            "#2000Fではノエル曹長。\x01",
            "彼らを駐車場まで案内しましょう。\x02\x03",

            "演習はあそこで行なうわ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 300)

    #C0226
    ChrTalk(
        0x8,
        (
            "#5P#0501F了解しました。\x02\x03",

            "#0500Fでは皆さん、\x01",
            "私についてきてください。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0227
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【警備隊演習への参加要請】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x5C, 0)
    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_5C6A")

    label("loc_5C6A")

    Return()

    # Function_13_5A30 end

    def Function_14_5C6B(): pass

    label("Function_14_5C6B")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x8, 0xE1, 0x0)
    SetChrSubChip(0x9, 0x0)
    OP_68(3870, 1200, -590, 0)
    MoveCamera(55, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(26200, 0)
    SetChrPos(0x101, 3000, 0, 0, 90)
    SetChrPos(0x102, 3000, 0, -1500, 90)
    SetChrPos(0x103, 1500, 0, -1500, 90)
    SetChrPos(0x104, 1500, 0, 0, 90)
    Sleep(500)
    SetCameraDistance(25200, 1000)
    FadeToBright(500, 0)
    OP_0D()

    #C0228
    ChrTalk(
        0x9,
        (
            "#11P#2004Fさて……改めて\x01",
            "お礼を言わせて貰うわ。\x02\x03",

            "#2000F私たちの演習に付き合ってくれて\x01",
            "本当に助かりました。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        (
            "#6P#0000Fいえ……俺たちにとっても\x01",
            "すごくいい経験になりました。\x02\x03",

            "警備隊員と戦うなんて、\x01",
            "普通は出来ませんからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x102,
        (
            "#6P#0109Fえぇ……\x01",
            "参考になる部分も多くって。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_5F09")
    OP_2C(0xF, 0x3)

    #C0231
    ChrTalk(
        0x104,
        (
            "#6P#0309F現役の警備隊員に勝てたのは\x01",
            "清々しかったよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x103,
        (
            "#6P#0203Fまぁ『胸を貸す』だのと\x01",
            "見栄を切っておいて敗北じゃ、\x01",
            "示しがつきませんからね。\x02\x03",

            "#0200Fランディさんも\x01",
            "安心したということでしょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60C3")

    label("loc_5F09")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xF, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_5FE9")
    OP_2C(0xF, 0x1)

    #C0233
    ChrTalk(
        0x104,
        (
            "#6P#0309F現役の警備隊員に勝てたのは\x01",
            "清々しかったよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x103,
        (
            "#6P#0203Fまぁ、ノエルさんが\x01",
            "指揮した時には負けたわけですが。\x02\x03",

            "#0200F普段先輩面をしていただけに、\x01",
            "ランディさんも恥ずかしかったのでは？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_60C3")

    label("loc_5FE9")


    #C0235
    ChrTalk(
        0x104,
        (
            "#6P#0300F現役の警備隊員に負けちまったのは、\x01",
            "どうも納得いかねぇけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x103,
        (
            "#6P#0203Fまぁ『胸を貸す』だのと\x01",
            "見栄を切っておいて、\x01",
            "結局は敗北ですからね。\x02\x03",

            "#0200Fランディさんは今夜、\x01",
            "一人寂しく枕を濡らすわけですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60C3")


    #C0237
    ChrTalk(
        0x104,
        "#6P#0306Fティオすけ、お前なぁ……\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x8,
        (
            "#5P#0509Fあ、あはは……\x01",
            "先輩も形無しですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x9,
        (
            "#11P#2004Fふふ……\x02\x03",

            "#2000Fあなたたちも、\x01",
            "これから精進しつづけて頂戴。\x02\x03",

            "また協力が必要な時は、\x01",
            "支援要請の形で連絡を取ります。\x02\x03",

            "特務支援課の活動、\x01",
            "陰ながら応援しているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        "#6P#0000F……はい、ありがとうございます！\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0241
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【警備隊演習への参加要請】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 3000, 0, 0, 90)
    SetChrPos(0x1, 3000, 0, 0, 90)
    SetChrPos(0x2, 3000, 0, 0, 90)
    SetChrPos(0x3, 3000, 0, 0, 90)
    OP_68(3000, 900, 0, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    OP_29(0xF, 0x1, 0x4)
    OP_29(0xF, 0x4, 0x10)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_14_5C6B end

    def Function_15_62FA(): pass

    label("Function_15_62FA")

    EventBegin(0x0)
    OP_4B(0x8, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrSubChip(0x9, 0x2)
    OP_68(6140, 900, -20, 0)
    MoveCamera(55, 17, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24460, 0)
    SetChrPos(0x101, -3000, 0, 0, 90)
    SetChrPos(0x102, -3000, 0, -1500, 90)
    SetChrPos(0x103, -4500, 0, -1500, 90)
    SetChrPos(0x104, -4500, 0, 0, 90)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)

    #C0242
    ChrTalk(
        0x101,
        "#0000F──失礼します。\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x8, 0xE1, 0x1F4)
    SetChrSubChip(0x9, 0x0)
    OP_68(3870, 1200, -590, 5000)
    MoveCamera(55, 17, 0, 5000)
    SetCameraDistance(26200, 5000)
    BeginChrThread(0x101, 3, 0, 16)
    BeginChrThread(0x102, 3, 0, 17)
    BeginChrThread(0x103, 3, 0, 18)
    BeginChrThread(0x104, 3, 0, 19)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)

    #C0243
    ChrTalk(
        0x101,
        (
            "#0000Fお疲れ様です、\x01",
            "ソーニャ副司令、ノエル曹長。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x8,
        "#5P#0500Fお疲れ様です！\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x9,
        (
            "#11P#2000Fお疲れ様。\x02\x03",

            "#2001F……あなた達のほうから\x01",
            "わざわざ出向いてくるなんて、\x01",
            "何かあったのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        (
            "#6P#0001Fええ、実は、\x01",
            "相談したいことがありまして……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0247
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは、偽ブランド業者への水際対策として\x01",
            "タングラム門に来た事を説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0248
    ChrTalk(
        0x9,
        (
            "#11P#2003F……なるほど。\x01",
            "事態は理解できたわ。\x02\x03",

            "#2000F了解しました。\x01",
            "タングラム門部隊も\x01",
            "協力しましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        "#6P#0000Fご協力感謝します。\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x104,
        (
            "#6P#0305Fしかし、大丈夫なんスか？\x02\x03",

            "記念祭中、国境門はとんでもなく\x01",
            "忙しいみたいだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        (
            "#5P#0500F気にしないでください、先輩。\x02\x03",

            "#0503F水際対策は本来、門に詰める\x01",
            "警備隊員の仕事ですから。\x02\x03",

            "#0500F多少無理してでも、\x01",
            "私たちには携わる義務が\x01",
            "あると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x9,
        (
            "#11P#2004Fええ、その通り。\x01",
            "あなた達が気に病む事は\x01",
            "一つもないわ。\x02\x03",

            "#2000F人手はあまり割けないから、\x01",
            "あなた達のサポートという形には\x01",
            "なってしまいそうだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x103,
        "#6P#0202Fそれでも充分心強いです。\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x101,
        (
            "#6P#0001Fそれで、早速なんですが……\x01",
            "共和国からの旅行者を\x01",
            "調べる機会はあるでしょうか？\x02\x03",

            "#0003F警察本部の得た情報では、\x01",
            "偽ブランド業者は本日の昼ごろに\x01",
            "到着するらしいのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x9,
        (
            "#11P#2003Fそうね、確か……\x01",
            "そろそろ共和国からの旅客バスが\x01",
            "到着する予定になっているわ。\x02\x03",

            "情報が確かなら、おそらく\x01",
            "偽ブランド業者はそのバスに\x01",
            "乗っているはずよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x8,
        (
            "#5P#0501F旅客バスからクロスベル自治州内の\x01",
            "バスへの乗り換えの間、\x01",
            "少しですが時間が空きます。\x02\x03",

            "その間なら、観光客たちは\x01",
            "恐らく食堂の方で休憩することに\x01",
            "なるかと思われます。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x104,
        (
            "#6P#0300Fんじゃ、作戦は決まりだな。\x02\x03",

            "#0303F曹長がそれとなく、乗客たちを\x01",
            "食堂のほうに誘導する。\x02\x03",

            "#0300Fその後、俺たちが\x01",
            "さりげなく食堂に入って\x01",
            "偽ブランド業者に目星をつける。\x02\x03",

            "#0309F捜査官の腕の見せ所だぜ、ロイド。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x101,
        (
            "#6P#0000Fああ、任せてくれ。\x02\x03",

            "時間としては短そうだけど、\x01",
            "乗客たちを観察して\x01",
            "当たりをつけるには充分そうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x103,
        (
            "#6P#0200F身分を明かさなければ\x01",
            "話をすることもできるかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x102,
        "#6P#0101Fな、なんだか緊張してきたわね……\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x9,
        (
            "#11P#2003F共和国からバスが来るまで\x01",
            "少し時間があるわ。\x02\x03",

            "今から門の中で待機していれば\x01",
            "休憩する時間は充分にあるでしょう。\x02\x03",

            "#2000Fどうする？　よければ部屋を\x01",
            "用意させてもらうけれど。\x02",
        )
    )

    CloseMessageWindow()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【まだ準備が出来ていない】\x01",          # 0
            "【共和国からの旅客バスを待つ】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6CA7"),
        (1, "loc_6DD1"),
        (SWITCH_DEFAULT, "loc_6EC0"),
    )


    label("loc_6CA7")

    OP_60(0x0)

    #C0262
    ChrTalk(
        0x101,
        (
            "#0003Fそうですね……\x01",
            "できれば少し、準備したいところです。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x9,
        (
            "#11P#2000Fそう、了解したわ。\x02\x03",

            "準備が出来たらまた声をかけて頂戴。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, 3000, 0, 0, 90)
    SetChrPos(0x1, 3000, 0, 0, 90)
    SetChrPos(0x2, 3000, 0, 0, 90)
    SetChrPos(0x3, 3000, 0, 0, 90)
    OP_68(3000, 900, 0, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(25500, 0)
    OP_93(0x8, 0x10E, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    OP_29(0x1B, 0x1, 0x2)
    EventEnd(0x5)
    Jump("loc_6EC0")

    label("loc_6DD1")

    OP_60(0x0)

    #C0264
    ChrTalk(
        0x101,
        (
            "#6P#0000Fでは、お言葉に\x01",
            "甘えさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x9,
        (
            "#11P#2000F了解したわ。\x02\x03",

            "共和国のバスが到着したら\x01",
            "あなた達を呼ばせるようにします。\x02\x03",

            "それまで体を休ませておきなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x101,
        "#6P#0001Fはい！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x1B, 0x1, 0x2)
    OP_29(0x1B, 0x1, 0x3)
    SetScenarioFlags(0x5C, 0)
    NewScene("t2510", 0, 0, 0)
    IdleLoop()
    Jump("loc_6EC0")

    label("loc_6EC0")

    Return()

    # Function_15_62FA end

    def Function_16_6EC1(): pass

    label("Function_16_6EC1")


    def lambda_6EC6():
        OP_95(0xFE, 3000, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6EC6)
    WaitChrThread(0x101, 1)
    Return()

    # Function_16_6EC1 end

    def Function_17_6EE0(): pass

    label("Function_17_6EE0")


    def lambda_6EE5():
        OP_95(0xFE, 3000, 0, -1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6EE5)
    WaitChrThread(0x102, 1)
    Return()

    # Function_17_6EE0 end

    def Function_18_6EFF(): pass

    label("Function_18_6EFF")


    def lambda_6F04():
        OP_95(0xFE, 1500, 0, -1500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6F04)
    WaitChrThread(0x103, 1)
    Return()

    # Function_18_6EFF end

    def Function_19_6F1E(): pass

    label("Function_19_6F1E")


    def lambda_6F23():
        OP_95(0xFE, 1500, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6F23)
    WaitChrThread(0x104, 1)
    Return()

    # Function_19_6F1E end

    def Function_20_6F3D(): pass

    label("Function_20_6F3D")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7188")

    #C0267
    ChrTalk(
        0x103,
        (
            "#0205Fこのぬいぐるみは……\x02\x03",

            "#0203F……この形、\x01",
            "どこかで見たような気が。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x109,
        (
            "#0509Fあはは……\x01",
            "これはあたしの私物でして。\x02\x03",

            "#0500Fその、実はフランが\x01",
            "寄宿舎に飾るようにと\x01",
            "プレゼントしてくれたもので。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD1, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7070")

    #C0269
    ChrTalk(
        0x101,
        (
            "#0002Fああ、そういえば……\x01",
            "フランのぬいぐるみとは\x01",
            "色違いじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70E4")

    label("loc_7070")


    #C0270
    ChrTalk(
        0x101,
        (
            "#0005Fああ、そういえば……\x02\x03",

            "#0002F前にフランの実家にお邪魔した時\x01",
            "これと色違いのぬいぐるみが\x01",
            "あった気がするよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_70E4")


    #C0271
    ChrTalk(
        0x104,
        "#0309Fはは、お揃いってワケか。\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x102,
        (
            "#0104F本当に仲のいい姉妹ですよね。\x01",
            "ちょっと羨ましいかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x109,
        (
            "#0509Fそ、そ、そうですか？\x01",
            "（何だか照れるなぁ……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD1, 2)
    Jump("loc_7222")

    label("loc_7188")

    SetChrName("")

    #A0274
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ノエルのぬいぐるみがある。\x01",
            "フランとはお揃いのようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0275
    ChrTalk(
        0x109,
        (
            "#0506F（何だか恥ずかしくなってきた……\x01",
            "  やっぱり仕舞っておけば\x01",
            "  よかったかな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7222")

    TalkEnd(0xFF)
    Return()

    # Function_20_6F3D end

    SaveToFile()

Try(main)
