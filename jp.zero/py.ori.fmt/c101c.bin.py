from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c101c.bin",                # FileName
        "c101c",                    # MapName
        "c101c",                    # Location
        0x0013,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 19, 0, 1, 0, 2],
    )

    BuildStringList((
        "c101c",                  # 0
        "受付ミシェル",           # 1
        "アリオス",               # 2
        "遊撃士スコット",         # 3
        "遊撃士ヴェンツェル",     # 4
        "遊撃士リン",             # 5
        "遊撃士エオリア",         # 6
    ))

    AddCharChip((
        "chr/ch09100.itc",                   # 00
        "chr/ch02400.itc",                   # 01
        "chr/ch27200.itc",                   # 02
        "chr/ch27300.itc",                   # 03
        "chr/ch32002.itc",                   # 04
        "chr/ch32102.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(1000,    0,       12819,   180,  261,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(970,     0,       10300,   0,    405,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-10729,  0,       51650,   270,  405,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-12170,  0,       51490,   90,   405,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-5929,   150,     43069,   180,  469,  0x0, 0,   4,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(-5869,   150,     40840,   0,    469,  0x0, 0,   5,   0,   255, 255, 0,   9,   255,  0)

    DeclActor(5500,    0,       6000,    1200,    5500,    1500,    6000,    0x007C, 0,  10, 0x0000)
    DeclActor(8000,    0,       6000,    1200,    8000,    1500,    6000,    0x007C, 0,  11, 0x0000)
    DeclActor(5500,    0,       2500,    1200,    5500,    1500,    2500,    0x007C, 0,  11, 0x0000)
    DeclActor(8000,    0,       2500,    1200,    8000,    1500,    2500,    0x007C, 0,  11, 0x0000)
    DeclActor(680,     0,       11370,   1700,    1000,    1500,    12820,   0x007E, 0,  3,  0x0000)

    ScpFunction((
        "Function_0_298",          # 00, 0
        "Function_1_350",          # 01, 1
        "Function_2_3B0",          # 02, 2
        "Function_3_3B1",          # 03, 3
        "Function_4_3B5",          # 04, 4
        "Function_5_E47",          # 05, 5
        "Function_6_FA1",          # 06, 6
        "Function_7_119C",         # 07, 7
        "Function_8_123A",         # 08, 8
        "Function_9_149E",         # 09, 9
        "Function_10_175E",        # 0A, 10
        "Function_11_1D7E",        # 0B, 11
    ))


    def Function_0_298(): pass

    label("Function_0_298")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2D8"),
        (1, "loc_2E4"),
        (2, "loc_2F0"),
        (3, "loc_2FC"),
        (4, "loc_308"),
        (5, "loc_314"),
        (6, "loc_320"),
        (SWITCH_DEFAULT, "loc_32C"),
    )


    label("loc_2D8")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_2E4")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_2F0")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_2FC")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_308")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_314")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_320")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_32C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_338")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_338")

    label("loc_34F")

    Return()

    # Function_0_298 end

    def Function_1_350(): pass

    label("Function_1_350")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_368")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_3AF")

    label("loc_368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_38A")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0x8, 0x10)
    Jump("loc_3AF")

    label("loc_38A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_398")
    Jump("loc_3AF")

    label("loc_398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3A6")
    Jump("loc_3AF")

    label("loc_3A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3AF")

    label("loc_3AF")

    Return()

    # Function_1_350 end

    def Function_2_3B0(): pass

    label("Function_2_3B0")

    Return()

    # Function_2_3B0 end

    def Function_3_3B1(): pass

    label("Function_3_3B1")

    Call(0, 4)
    Return()

    # Function_3_3B1 end

    def Function_4_3B5(): pass

    label("Function_4_3B5")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_5B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52F")

    #C0001
    ChrTalk(
        0x8,
        (
            "あら、坊やたちじゃない。\x01",
            "これからどこかにお出掛けかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        "#0012Fえ、ええ、仕事がてら……\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        "そう……\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "……まあいいわ。\x01",
            "警察内部の事情にまで\x01",
            "首を突っ込むつもりは無いし。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "どこに行くか知らないけど\x01",
            "自分たちの責任で頑張りなさいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        "#0001F……はい。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x103,
        "#0203F（薄々感づかれてます……）\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x104,
        "#0301F（ハン、さすがに鋭いな……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5B3")

    label("loc_52F")


    #C0009
    ChrTalk(
        0x8,
        (
            "ま、警察にも色々あるんでしょうけど\x01",
            "アタシが口を出すことじゃないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "せいぜい頑張りなさい。\x01",
            "ただし、自分たちの責任でね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B3")

    Jump("loc_E43")

    label("loc_5B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_648")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D3")
    Call(0, 5)
    Jump("loc_643")

    label("loc_5D3")


    #C0011
    ChrTalk(
        0x8,
        (
            "やれやれ、本当はアリオスに\x01",
            "お休みをあげたかったんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "……シズクちゃん、\x01",
            "寂しがっていないかしら？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_643")

    Jump("loc_E43")

    label("loc_648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_7CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70A")

    #C0013
    ChrTalk(
        0x8,
        (
            "そろそろ市外に足を伸ばす\x01",
            "観光客も出てくる頃よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "ウチもウルスラ病院の方に\x01",
            "エステルちゃんたちを回したわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "ま、アナタたちも\x01",
            "せいぜい気をつけておきなさい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_7C7")

    label("loc_70A")


    #C0016
    ChrTalk(
        0x8,
        "アリオスは手配魔獣の対処……\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "パレードへの対応は\x01",
            "リンたちに任せるとして……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "例の件はスコットに頼んで\x01",
            "ヴェンツェルは待機かしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "ああん、もう！\x01",
            "人手が倍は欲しいわねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C7")

    Jump("loc_E43")

    label("loc_7CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_CAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B23")

    #C0020
    ChrTalk(
        0x8,
        (
            "アナタたち、昨日は随分\x01",
            "活躍したみたいじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "ウチのエステルちゃんたちを\x01",
            "出し抜くなんて大金星だわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#0000Fはは……\x01",
            "それは俺たちも同感です。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x104,
        (
            "#0306Fちょいと禁じ手を\x01",
            "使っちまったからなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "ま、その調子で成長して\x01",
            "こっちを楽にしてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "そうそう……\x01",
            "アリオスが昨日の夜、\x01",
            "やっと出張から戻ってきたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "市庁舎からの要請が来てたから\x01",
            "早速、シンポジウムの\x01",
            "警備に回ってもらったわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0027
    ChrTalk(
        0x101,
        (
            "#0005Fあれ、シンポジウムの警備は\x01",
            "警察が担当していたんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x103,
        (
            "#0200Fええ、それも捜査一課が\x01",
            "受け持っていたはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        "ま、共同警備ってわけね。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "外国のＶＩＰも参加するから\x01",
            "少しでも確実な可能性を\x01",
            "追求したんじゃないかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        "#0000Fな、なるほど……\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        (
            "#0300Fそらま、《風の剣聖》がいたら\x01",
            "確実は確実だわな。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        (
            "#0100F一応、そういう場合には\x01",
            "警察とギルドも協力するんですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB3, 5)
    Jump("loc_CAA")

    label("loc_B23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C03")

    #C0034
    ChrTalk(
        0x8,
        (
            "そういえば……\x01",
            "エステルちゃんたちの方は\x01",
            "野暮用があるとか言ってたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "何でもちょっと辺鄙#4Rへんぴ#な所を\x01",
            "訪ねてみるらしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "ま、アリオスも戻ってきたし\x01",
            "少しは息抜きしてもらいましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CAA")

    label("loc_C03")


    #C0037
    ChrTalk(
        0x8,
        (
            "アリオスは市庁舎、\x01",
            "エステルちゃんたちは私用……\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            "スコットたちはＩＢＣ、\x01",
            "リンたちは大聖堂ね……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "……ふう、メンバーの行動を\x01",
            "把握するものも楽じゃないわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CAA")

    Jump("loc_E43")

    label("loc_CAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_E43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9D")

    #C0040
    ChrTalk(
        0x8,
        "あら坊やたち、ご苦労様。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "実は、本部の要請で出張してる\x01",
            "アリオスの帰国が遅れているのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "結局、記念祭の初日には\x01",
            "間に合わなかったのよねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "本部の連中にはアタシから\x01",
            "苦情を言ってやらなくちゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E43")

    label("loc_D9D")


    #C0044
    ChrTalk(
        0x8,
        (
            "記念祭の間は\x01",
            "出張は基本的にキャンセル。\x01",
            "全メンバーで乗り切るのが通例よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "まったく……よりによって\x01",
            "アリオスを独り占めするなんて\x01",
            "本部には文句言わなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E43")

    TalkEnd(0x8)
    Return()

    # Function_4_3B5 end

    def Function_5_E47(): pass

    label("Function_5_E47")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_F9D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F36")
    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0046
    ChrTalk(
        0x8,
        (
            "戻ったばかりで悪いけど\x01",
            "ちょっと時間をもらえる？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "さっきレミフェリア支部から\x01",
            "連絡があったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x9,
        (
            "#1403F例の件についてか……\x02\x03",

            "#1400F……分かった。\x01",
            "詳しい話を聞こう。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    SetScenarioFlags(0x0, 0)
    Jump("loc_F9D")

    label("loc_F36")


    #C0049
    ChrTalk(
        0x9,
        (
            "#1403F……先ほどの件は気にするな。\x02\x03",

            "#1400Fまだ仕事があるのだろう？\x01",
            "お前たちのペースで励むがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F9D")

    TalkEnd(0xFE)
    Return()

    # Function_5_E47 end

    def Function_6_FA1(): pass

    label("Function_6_FA1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1198")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FB")
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0050
    ChrTalk(
        0xA,
        (
            "今予定されている仕事をこなせば\x01",
            "来週の出張は行かなくていいと\x01",
            "ミシェルに言われたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xA,
        "ヴェンツェル、もしかしてお前……\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xB,
        (
            "たまには１人で出張に行きたい……\x01",
            "俺はそう希望を出しただけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xB,
        (
            "記念祭の忙しい時期も終わる。\x01",
            "……たまには婚約者と過ごすんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xA,
        "……ありがとう、相棒。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x0, 2)
    Jump("loc_1198")

    label("loc_10FB")


    #C0055
    ChrTalk(
        0xFE,
        (
            "来週はヴェンツェルの言うように……\x01",
            "パールと過ごすとするかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "……彼女の予定も\x01",
            "確認しておかないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "久しぶりに会うとなると\x01",
            "緊張するなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1198")

    TalkEnd(0xFE)
    Return()

    # Function_6_FA1 end

    def Function_7_119C(): pass

    label("Function_7_119C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1236")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11BA")
    Call(0, 6)
    Jump("loc_1236")

    label("loc_11BA")


    #C0058
    ChrTalk(
        0xFE,
        (
            "スコットは仕事にかまけすぎて\x01",
            "婚約者とろくすっぽ会えていない。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "たまにはこういう時間を\x01",
            "作ってやることも大事だろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1236")

    TalkEnd(0xFE)
    Return()

    # Function_7_119C end

    def Function_8_123A(): pass

    label("Function_8_123A")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_12CE")
    Jump("loc_1318")

    label("loc_12CE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_12EE")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1318")

    label("loc_12EE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_130E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1318")

    label("loc_130E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1318")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1496")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1409")

    #C0060
    ChrTalk(
        0xFE,
        (
            "ようやくパレードの警備が\x01",
            "終わったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "あの人ごみの中にいるのは\x01",
            "流石に疲れたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x104,
        "#0300Fおお……お疲れ。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "ん、どうもどうも。\x01",
            "まぁ、ゆっくり体を休めるとするよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1496")

    label("loc_1409")


    #C0064
    ChrTalk(
        0xFE,
        (
            "そういえば、人ごみの中に\x01",
            "見たことある顔がいたような……\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "ううん、気のせいかな。\x01",
            "あの人がクロスベルに来るなんて\x01",
            "連絡はなかったし……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1496")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_8_123A end

    def Function_9_149E(): pass

    label("Function_9_149E")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1532")
    Jump("loc_157C")

    label("loc_1532")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1552")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_157C")

    label("loc_1552")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1572")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_157C")

    label("loc_1572")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_157C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1756")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16CB")

    #C0066
    ChrTalk(
        0xFE,
        (
            "……あ、そこに居るのはティオちゃん！\x01",
            "やっぱり可愛い可愛い……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "お姉さん、お仕事で疲れてるの。\x01",
            "癒してもらってもいいかなぁ？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x103,
        "#0211F……具体的な方法が分かりません。\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "ぎゅ～っと抱っこさせて\x01",
            "もらえるだけでいいわ㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x103,
        "#0203Fお断りします。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        "きゃん。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1756")

    label("loc_16CB")


    #C0072
    ChrTalk(
        0xFE,
        (
            "はぁ、残念……\x01",
            "仕方ないから、食べ損ねたお昼の\x01",
            "買出しにでも行こうかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "最近は《モルジュ》のハンバーガーが\x01",
            "お気に入りなのよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1756")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_149E end

    def Function_10_175E(): pass

    label("Function_10_175E")

    TalkBegin(0xFF)
    SetChrName("")

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "遊撃士たちのシフト表が貼り付けられている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_18DD")
    SetChrName("")

    #A0075
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　 　　　　　 　 行き先\x01",
            "━━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　： レミフェリア公国\x01",
            " 　スコット　：　  《待機中》\x01",
            " ヴェンツェル：　  《待機中》\x01",
            " 　　リン　　：※休憩（龍老飯店）\x01",
            " 　エオリア　：※休憩（ベーカリー）\x01",
            " 　エステル　：　　  大聖堂\x01",
            " 　ヨシュア　：　　  大聖堂\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_1D67")

    label("loc_18DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1A08")
    SetChrName("")

    #A0076
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  行き先　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：　 《待機中》\x01",
            " 　スコット　：※休憩（龍老飯店\x01",
            " ヴェンツェル：※休憩（龍老飯店\x01",
            " 　　リン　　：　 《待機中》\x01",
            " 　エオリア　：　 《待機中》\x01",
            " 　エステル　：  ウルスラ病院\x01",
            " 　ヨシュア　：  ウルスラ病院\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_1D67")

    label("loc_1A08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1B26")
    SetChrName("")

    #A0077
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　  行き先　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：    市外巡回\x01",
            " 　スコット　：　  市外巡回\x01",
            " ヴェンツェル：　  武器商会\x01",
            " 　　リン　　：　   行政区\x01",
            " 　エオリア　：　   行政区\x01",
            " 　エステル　：  ウルスラ病院\x01",
            " 　ヨシュア　：  ウルスラ病院\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_1D67")

    label("loc_1B26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1C51")
    SetChrName("")

    #A0078
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　   行き先　　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：　　  市庁舎\x01",
            " 　スコット　：　　  ＩＢＣ\x01",
            " ヴェンツェル：　　  ＩＢＣ\x01",
            " 　　リン　　：　　  大聖堂\x01",
            " 　エオリア　：　　  大聖堂\x01",
            " 　エステル　：※私用（山道方面）\x01",
            " 　ヨシュア　：※私用（山道方面）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_1D67")

    label("loc_1C51")

    SetChrName("")

    #A0079
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "　　　　　　　　　　行き先　　\x01",
            "━━━━━━━━━━━━━━━━\x01",
            " 　アリオス　：　レマン総本部\x01",
            " 　スコット　：　タングラム門\x01",
            " ヴェンツェル：　タングラム門\x01",
            " 　　リン　　：　アルモリカ村\x01",
            " 　エオリア　：　アルモリカ村\x01",
            " 　エステル　：　　 行政区\x01",
            " 　ヨシュア　：　　 行政区\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_1D67")

    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_10_175E end

    def Function_11_1D7E(): pass

    label("Function_11_1D7E")

    TalkBegin(0xFF)
    SetChrName("")

    #A0080
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "遊撃士協会に対する依頼が\x01",
            "数多く張り出されている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_11_1D7E end

    SaveToFile()

Try(main)
