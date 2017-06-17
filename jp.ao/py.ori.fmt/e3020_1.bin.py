from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e3020_1.bin",                # FileName
        "e3020",                    # MapName
        "e3020",                    # Location
        0x0000,                     # MapIndex
        "ed7570",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [312, 2211, 3054, 7510, 8130, 9138, 9791, 13175, 14343, 0, 14961, 0, 15811, 16579, 17348, 20335, 0, 21233, 0, 80, 85, 0, 0],
    )

    BuildStringList((
        "e3020_1",                # 0
    ))

    ChipFrameInfo(312, 0)                                        # 0

    ScpFunction((
        "Function_0_138",          # 00, 0
        "Function_1_8A3",          # 01, 1
        "Function_2_BEE",          # 02, 2
        "Function_3_1D56",         # 03, 3
        "Function_4_1FC2",         # 04, 4
        "Function_5_23B2",         # 05, 5
        "Function_6_263F",         # 06, 6
        "Function_7_3377",         # 07, 7
        "Function_8_3807",         # 08, 8
        "Function_9_3A71",         # 09, 9
        "Function_10_3DC3",        # 0A, 10
        "Function_11_40C3",        # 0B, 11
        "Function_12_43C4",        # 0C, 12
        "Function_13_4F6F",        # 0D, 13
        "Function_14_52F1",        # 0E, 14
        "Function_15_5550",        # 0F, 15
        "Function_16_6D48",        # 10, 16
        "Function_17_6EFC",        # 11, 17
        "Function_18_736F",        # 12, 18
        "Function_19_7764",        # 13, 19
        "Function_20_8582",        # 14, 20
        "Function_21_8943",        # 15, 21
        "Function_22_8C72",        # 16, 22
        "Function_23_9AC5",        # 17, 23
        "Function_24_9D9D",        # 18, 24
        "Function_25_A444",        # 19, 25
        "Function_26_A778",        # 1A, 26
        "Function_27_C3C6",        # 1B, 27
        "Function_28_C67F",        # 1C, 28
        "Function_29_C776",        # 1D, 29
        "Function_30_CA1D",        # 1E, 30
        "Function_31_CD63",        # 1F, 31
        "Function_32_E6CD",        # 20, 32
        "Function_33_EB4B",        # 21, 33
        "Function_34_EDD0",        # 22, 34
        "Function_35_F74C",        # 23, 35
        "Function_36_F99A",        # 24, 36
        "Function_37_FBC0",        # 25, 37
        "Function_38_100B9",       # 26, 38
        "Function_39_10764",       # 27, 39
        "Function_40_10B7F",       # 28, 40
        "Function_41_10DFC",       # 29, 41
        "Function_42_111B4",       # 2A, 42
        "Function_43_111B8",       # 2B, 43
        "Function_44_12200",       # 2C, 44
        "Function_45_12537",       # 2D, 45
        "Function_46_1253B",       # 2E, 46
        "Function_47_13461",       # 2F, 47
        "Function_48_13657",       # 30, 48
        "Function_49_137AA",       # 31, 49
        "Function_50_13D4E",       # 32, 50
        "Function_51_13E89",       # 33, 51
        "Function_52_1442B",       # 34, 52
        "Function_53_14E4B",       # 35, 53
        "Function_54_157CA",       # 36, 54
        "Function_55_15B0D",       # 37, 55
        "Function_56_15CE5",       # 38, 56
    ))


    def Function_0_138(): pass

    label("Function_0_138")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_38A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_156")
    Call(1, 1)
    Jump("loc_385")

    label("loc_156")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D2")

    #C0001
    ChrTalk(
        0x11,
        (
            "#00101Fベルは、おそらく自分自身の為に\x01",
            "今回の計画に参加してるんだと思う。\x02\x03",

            "#00108Fベルのそういう性格には\x01",
            "私も戸惑うことが多かったけど、\x01",
            "それが彼女の魅力なんだと感じてた……\x02\x03",

            "#00103F……でも、どんな理由があっても、\x01",
            "誰かを犠牲にするようなやり方は、\x01",
            "決して許されてはいけないと思う。\x02\x03",

            "#00100Fベルの幼い頃からの親友として……\x01",
            "きっと彼女の間違いを正してみせるわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_385")

    label("loc_2D2")


    #C0002
    ChrTalk(
        0x11,
        (
            "#00103Fどんな理由があっても、\x01",
            "誰かを犠牲にするようなやり方は、\x01",
            "決して許されてはいけないと思う。\x02\x03",

            "#00100Fベルの幼い頃からの親友として……\x01",
            "きっと彼女の間違いを正してみせるわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_385")

    Jump("loc_89F")

    label("loc_38A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_52D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_494")

    #C0003
    ChrTalk(
        0x11,
        (
            "#00103Fベルはクロイス家の末裔として、\x01",
            "今回の計画にもかなり根深い所で\x01",
            "関わっているはずよ。\x02\x03",

            "#00108Fきっと、私たちの求める真実は、\x01",
            "彼女とイアン先生が持っているはず……\x02\x03",

            "#00101F……行きましょう、ロイド。\x01",
            "キーアちゃんを取り戻す為に……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_528")

    label("loc_494")


    #C0004
    ChrTalk(
        0x11,
        (
            "#00108Fきっと、私たちの求める真実は、\x01",
            "ベルとイアン先生が持っているはず……\x02\x03",

            "#00101F……行きましょう、ロイド。\x01",
            "キーアちゃんを取り戻す為に……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_528")

    Jump("loc_89F")

    label("loc_52D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_6CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64C")

    #C0005
    ChrTalk(
        0x11,
        (
            "#00108Fベル……最初からおじさまを\x01",
            "見捨てるつもりだったのかしら。\x02\x03",

            "それに、まさかイアン先生が\x01",
            "黒幕だったなんて……\x02\x03",

            "#00106F……ダメだわ、\x01",
            "私も混乱しているみたい……\x01",
            "上手く考えがまとまらないわ。\x02\x03",

            "#00100Fとにかく、行くしかないわよね。\x01",
            "あの《碧の大樹》へ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_6CA")

    label("loc_64C")


    #C0006
    ChrTalk(
        0x11,
        (
            "#00108F……色々と起こりすぎて\x01",
            "混乱してしまっているけど……\x02\x03",

            "#00100Fとにかく、行くしかないわよね。\x01",
            "あの《碧の大樹》へ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6CA")

    Jump("loc_89F")

    label("loc_6CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_89F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F4")

    #C0007
    ChrTalk(
        0x11,
        (
            "#00103Fおじいさまによって\x01",
            "独立国の無効宣言が出されたことで、\x01",
            "各地にかなりの影響が出たみたい。\x02\x03",

            "#00108F国防軍も一旦撤退しているようだし、\x01",
            "様々な乱れが出ているかもしれない……\x02\x03",

            "#00100F《大鐘》を止めにいく合間に、\x01",
            "もう一度各地を見て回っても\x01",
            "いいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_89F")

    label("loc_7F4")


    #C0008
    ChrTalk(
        0x11,
        (
            "#00103F独立国の無効宣言が出されたことで、\x01",
            "様々な乱れが出ているかもしれない……\x02\x03",

            "#00100F《大鐘》を止めにいく合間に、\x01",
            "もう一度各地を見て回っても\x01",
            "いいかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_89F")

    TalkEnd(0xFE)
    Return()

    # Function_0_138 end

    def Function_1_8A3(): pass

    label("Function_1_8A3")


    #C0009
    ChrTalk(
        0x11,
        (
            "#00100Fいよいよ……\x01",
            "キーアちゃんが待つ場所への\x01",
            "道が拓かれたわね。\x02\x03",

            "#00108Fそこには、黒幕のイアン先生、\x01",
            "そしてベルもいる………………\x02\x03",

            "#00103F……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        "#00001Fエリィ…………\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x11,
        (
            "#00103F……ベルは、おそらく自分自身の為に\x01",
            "今回の計画に参加してるんだと思う。\x02\x03",

            "#00108Fベルのそういう性格には\x01",
            "私も戸惑うことが多かったけど、\x01",
            "それが彼女の魅力なんだと感じてた……\x02\x03",

            "#00101F……でも、どんな理由があっても、\x01",
            "誰かを犠牲にするようなやり方は、\x01",
            "決して許されてはいけないと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#00003F……ああ、そうだな。\x02\x03",

            "#00001Fマリアベルさんとイアン先生の計画が\x01",
            "どんなものであろうと、これ以上\x01",
            "キーアを利用させるわけにはいかない。\x02\x03",

            "#00003Fエリィ、彼女と戦うことになるのは\x01",
            "辛いかもしれないけど……\x01",
            "どうか力を貸してくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x11,
        (
            "#00103F……ええ、覚悟は出来てる。\x02\x03",

            "#00101Fベルの幼い頃からの親友として……\x01",
            "きっと彼女の間違いを正してみせるわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 1)
    Return()

    # Function_1_8A3 end

    def Function_2_BEE(): pass

    label("Function_2_BEE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C12")
    Call(1, 56)
    Jump("loc_DEA")

    label("loc_C12")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C32")
    RunExpression(0xA, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0xB, 0x101, 0)

    label("loc_C32")


    #C0014
    ChrTalk(
        0xB,
        (
            "#00200Fロイドさん、\x01",
            "よろしければこれを\x01",
            "受け取って下さい。\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『ティオのアカウント』\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x28, 1)
    OP_E4(0x3)

    #C0016
    ChrTalk(
        0x101,
        "#00005F『ポムっと！』のアカウント……？\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xB,
        (
            "#00204Fこんな状況だからこそ、\x01",
            "息抜きも大事になるかと。\x02\x03",

            "#00202Fいつでもお相手になりますので\x01",
            "気軽に勝負を仕掛けてきてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#00009Fはは、分かった。\x02\x03",

            "#00004F（ティオはかなりの\x01",
            "　強敵だと思うけど……\x01",
            "　何とか頑張ってみるか。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DEA")
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DEA")

    Jump("loc_1D52")

    label("loc_DEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_F6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E0A")
    Call(1, 5)
    Jump("loc_F69")

    label("loc_E0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EED")

    #C0019
    ChrTalk(
        0xB,
        (
            "#00208Fイアン先生は、ガイさんですら\x01",
            "届かなかった相手……\x01",
            "その覚悟は計り知れません。\x02\x03",

            "#00203Fならば、わたしたちは\x01",
            "それをさらに超える\x01",
            "最大限の覚悟を示さなければ……\x02\x03",

            "#00202F……頑張りましょう、ロイドさん。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_F69")

    label("loc_EED")


    #C0020
    ChrTalk(
        0xB,
        (
            "#00203Fわたしたちは、\x01",
            "イアン先生をさらに超える\x01",
            "最大限の覚悟を示さなければ……\x02\x03",

            "#00202F……頑張りましょう、ロイドさん。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F69")

    Jump("loc_1D52")

    label("loc_F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_1172")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10A7")

    #C0021
    ChrTalk(
        0xB,
        (
            "#00200F《碧の大樹》の中には、\x01",
            "不可思議な空間が形成されています。\x02\x03",

            "#00203F大鐘の共鳴によって《僧院》や《塔》に\x01",
            "作られていた“場”を遥かに超える、\x01",
            "物理法則を完全に無視した世界……\x02\x03",

            "#00201Fわたしたちが培ってきた\x01",
            "あらゆる常識が通用しないはず……\x01",
            "用心しながら進んだほうがいいでしょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_116D")

    label("loc_10A7")


    #C0022
    ChrTalk(
        0xB,
        (
            "#00203F《碧の大樹》の中には、\x01",
            "物理法則を完全に無視した\x01",
            "不可思議な空間が形成されています。\x02\x03",

            "#00201Fわたしたちが培ってきた\x01",
            "あらゆる常識が通用しないはず……\x01",
            "用心しながら進んだほうがいいでしょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_116D")

    Jump("loc_1D52")

    label("loc_1172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_131B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_126E")

    #C0023
    ChrTalk(
        0xB,
        (
            "#00200F確かに、あの《大樹》からは\x01",
            "キーアに似た波動を感じます。\x02\x03",

            "マリアベルさんは、\x01",
            "《大樹》がキーアそのものだと\x01",
            "仰っていましたが……\x02\x03",

            "#00206F……理解できません。\x01",
            "あのような物を出現させて、\x01",
            "一体何を企んでいるんでしょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1316")

    label("loc_126E")


    #C0024
    ChrTalk(
        0xB,
        (
            "#00200Fマリアベルさんは、\x01",
            "《大樹》がキーアそのものだと\x01",
            "仰っていましたが……\x02\x03",

            "#00206F……理解できません。\x01",
            "あのような物を出現させて、\x01",
            "一体何を企んでいるんでしょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1316")

    Jump("loc_1D52")

    label("loc_131B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_14F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1448")

    #C0025
    ChrTalk(
        0xB,
        (
            "#00200F今回は新たな《隙間》の探知が\x01",
            "必要なさそうなので、ヨナに全面的に\x01",
            "艦の仕事を引き継いでもらいました。\x02\x03",

            "#00203F相手はあの《結社》……\x01",
            "どんな手を講じてくるか、\x01",
            "分かったものではありませんから。\x02\x03",

            "#00200F魔導杖も含めて、常に万全の体勢を\x01",
            "整えておかなくてはいけませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_14EB")

    label("loc_1448")


    #C0026
    ChrTalk(
        0xB,
        (
            "#00203F相手はあの《結社》……\x01",
            "どんな手を講じてくるか、\x01",
            "分かったものではありません。\x02\x03",

            "#00200F魔導杖も含めて、常に万全の体勢を\x01",
            "整えておかなくてはいけませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14EB")

    Jump("loc_1D52")

    label("loc_14F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_1657")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_150B")
    Call(1, 4)
    Jump("loc_1652")

    label("loc_150B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15BB")

    #C0027
    ChrTalk(
        0xB,
        (
            "#00204F短い間でしたけど……\x01",
            "ツァイトと一緒に歩けたのは\x01",
            "素直に嬉しかったです。\x02\x03",

            "#00202F彼の庇護に報いる為にも、\x01",
            "これからは一層\x01",
            "頑張らないといけませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1652")

    label("loc_15BB")


    #C0028
    ChrTalk(
        0xB,
        (
            "#00204Fさて、わたしも後で\x01",
            "ハッキングの最終準備を\x01",
            "手伝いに行くとしましょう。\x02\x03",

            "#00211Fヨナの力は信用していますが、\x01",
            "多少ツメが甘いのは否めませんし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1652")

    Jump("loc_1D52")

    label("loc_1657")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_1818")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1765")

    #C0029
    ChrTalk(
        0xB,
        (
            "#00200Fエリィさんを取り戻せば、\x01",
            "支援課のメンバーは一通り\x01",
            "揃うことになりますね。\x02\x03",

            "#00203Fマクダエル議長が\x01",
            "監禁されている以上、\x01",
            "警備も相当に厳しいでしょうが……\x02\x03",

            "#00202Fツァイトも危険な役を\x01",
            "買って出てくれましたし、\x01",
            "絶対に成功させましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1813")

    label("loc_1765")


    #C0030
    ChrTalk(
        0xB,
        (
            "#00203Fエリィさんとマクダエル議長が\x01",
            "監禁されている以上、\x01",
            "警備も相当に厳しいでしょうが……\x02\x03",

            "#00200Fツァイトも危険な役を\x01",
            "買って出てくれましたし、\x01",
            "絶対に成功させましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1813")

    Jump("loc_1D52")

    label("loc_1818")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_1993")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F9")

    #C0031
    ChrTalk(
        0xB,
        (
            "#00200F西クロスベル街道から行けるのは、\x01",
            "ベルガード門、警察学校……\x02\x03",

            "#00206Fふう、難儀な位置に\x01",
            "《隙間》を見つけてしまいました。\x02\x03",

            "#00200F……でも、今はとにかく\x01",
            "行ける場所に行くしかないですよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_198E")

    label("loc_18F9")


    #C0032
    ChrTalk(
        0xB,
        (
            "#00206F西クロスベル街道から行けるのは、\x01",
            "ベルガード門、警察学校……\x02\x03",

            "#00200F難儀な位置ですが……\x01",
            "今はとにかく行ける場所に\x01",
            "行くしかないですよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_198E")

    Jump("loc_1D52")

    label("loc_1993")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_1A31")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19AE")
    Call(1, 3)
    Jump("loc_1A2C")

    label("loc_19AE")


    #C0033
    ChrTalk(
        0xB,
        (
            "#00208Fツァイトの部下の狼さんたち……\x01",
            "今は何をしているのでしょうね。\x02\x03",

            "#00203F彼らの助力も得られるなら\x01",
            "心強いのですが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A2C")

    Jump("loc_1D52")

    label("loc_1A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1D52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A4C")
    Call(1, 56)
    Jump("loc_1D52")

    label("loc_1A4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC1")
    EndChrThread(0x8, 0x0)

    #C0034
    ChrTalk(
        0xB,
        (
            "#00203F財団と教会が協力関係にあった……\x01",
            "噂くらいは聞いたことがありましたが、\x01",
            "ようやく確証が持てました。\x02\x03",

            "#00202Fとにかく、これなら違和感なく\x01",
            "端末を扱っていく事が出来そうです。\x02\x03",

            "エイオンシステムも併用すれば、\x01",
            "《隙間》の策的範囲も格段に広がるかと。\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x8, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BE7")
    Jump("loc_1C31")

    label("loc_1BE7")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1C07")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C31")

    label("loc_1C07")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C27")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1C31")

    label("loc_1C27")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C31")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    #C0035
    ChrTalk(
        0xB,
        (
            "#00200Fアッバスさん、引き続き\x01",
            "使い方をご教授願います。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        "#12100Fうむ、分かった。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xB, 0x0)
    BeginChrThread(0x8, 0, 0, 0)
    SetScenarioFlags(0x0, 4)
    Jump("loc_1D52")

    label("loc_1CC1")


    #C0037
    ChrTalk(
        0xB,
        (
            "#00203Fエイオンシステムも併用すれば、\x01",
            "《隙間》の索敵範囲も\x01",
            "格段に広がりそうです。\x02\x03",

            "#00200Fこちらはわたしとフランさんに\x01",
            "任せていただけると。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D52")

    TalkEnd(0xFE)
    Return()

    # Function_2_BEE end

    def Function_3_1D56(): pass

    label("Function_3_1D56")

    OP_4B(0xB, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0038
    ChrTalk(
        0xB,
        (
            "#00205Fそういえば……\x01",
            "山道にはツァイトの部下たちが\x01",
            "群れを作っていましたね。\x02\x03",

            "#00200F彼らもツァイトと同じく、\x01",
            "『神狼』だったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x13,
        (
            "#01203F#3Cいや、彼らはあくまで普通の狼だ。\x02\x03",

            "#01200Fただ、ウルスラが生きていた時代より\x01",
            "代替わりをしながら付き従っている、\x01",
            "私の眷属たちと言えるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xB,
        (
            "#00203F神狼の眷属……ルバーチェの事件で\x01",
            "軍用犬たちを容易く威圧できたのも、\x01",
            "当然といえば当然ですね。\x02\x03",

            "#00208F彼らも無事だといいのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x13,
        (
            "#01203F#3Cそれに関しては、群れを離れる前に\x01",
            "しかと言い含めておいたから\x01",
            "心配することはあるまい。\x02\x03",

            "#01200F今はどこぞでこの状況を\x01",
            "見守っているだろうな。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x0, 4)
    SetScenarioFlags(0x1, 1)
    Return()

    # Function_3_1D56 end

    def Function_4_1FC2(): pass

    label("Function_4_1FC2")

    OP_4B(0xB, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0042
    ChrTalk(
        0xB,
        (
            "#00203F……よし、と。\x01",
            "これで治療は一通り終わりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x13,
        "#01200F#3Cうむ、恩に着るぞティオ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x13, 500)

    #C0044
    ChrTalk(
        0x101,
        (
            "#00005Fツァイト……\x01",
            "さっきの戦闘で怪我を？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x13,
        (
            "#01203F#3Cうむ、あの《赤い星座》とやらにな。\x02\x03",

            "#01200F怪我自体はすぐに完治するだろうが……\x01",
            "やはり、彼奴らは国防軍とは\x01",
            "比べ物にならない練度のようだ。\x02\x03",

            "今回は奇襲をかけたおかげで\x01",
            "陽動が上手くいったが、\x01",
            "同じ手は２度通用するまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#00003Fそうか……\x02\x03",

            "#00002Fでも、本当に助かったよ。\x01",
            "ありがとうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x13,
        (
            "#01203F#3Cフフ、礼には及ばぬ。\x02\x03",

            "#01200F……さて、戦力の整った\x01",
            "おぬしらに付き添う必要も、\x01",
            "もはや無くなっただろう。\x02\x03",

            "以前と同様、後ろに控えているから\x01",
            "必要な時だけ呼び出すがいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xB,
        (
            "#00200F以前のように魔導杖で\x01",
            "導力波を送るんですね。\x01",
            "……了解しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x13,
        (
            "#01200F#3Cそれと、これからは\x01",
            "元の姿に戻った状態で\x01",
            "戦線に駆けつけるとしよう。\x02\x03",

            "#01203Fそこいらの魔獣程度なら\x01",
            "一飲みにしてやれるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#00009Fはは、あの姿で\x01",
            "駆けつけてもらえるなら\x01",
            "かなり心強いよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xB,
        (
            "#00202Fそれじゃあ、ツァイト。\x01",
            "改めてよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xB, 0xFF)
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x1D7, 0)
    Return()

    # Function_4_1FC2 end

    def Function_5_23B2(): pass

    label("Function_5_23B2")


    #C0052
    ChrTalk(
        0xB,
        (
            "#00203F……イアン先生が、親しかったはずの\x01",
            "ガイさんを手に掛けたと聞いて……\x01",
            "わたしは少しだけ不安になりました。\x02\x03",

            "#00208Fそこまでしなくてはならないほどの\x01",
            "『碧き零の計画』とは、一体……\x02\x03",

            "#00206Fなにより、ガイさんですら\x01",
            "届かなかった相手に、\x01",
            "わたしたちが届くのかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#00003F……そうだな、\x01",
            "確かに不安かもしれない。\x02\x03",

            "#00008Fイアン先生の覚悟は多分、\x01",
            "あのアリオスさん以上だろう。\x02\x03",

            "#00001Fだけど……だからこそ、\x01",
            "俺たちはイアン先生以上の覚悟を\x01",
            "示さなきゃいけないんだと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xB,
        (
            "#00208Fイアン先生以上の覚悟……\x01",
            "……そうですね。\x02\x03",

            "#00201F頑張りましょう、ロイドさん。\x01",
            "今こそが、ガイさんを超えるとき\x01",
            "なんだと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#00000Fああ……もちろんだ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 2)
    Return()

    # Function_5_23B2 end

    def Function_6_263F(): pass

    label("Function_6_263F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_2850")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_265D")
    Call(1, 11)
    Jump("loc_284B")

    label("loc_265D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27B0")

    #C0056
    ChrTalk(
        0xE,
        (
            "#00300F最後の相手は、底の知れない\x01",
            "マリアベルお嬢さんと\x01",
            "全ての黒幕であるイアン先生だ。\x02\x03",

            "#00303F《零の至宝》である\x01",
            "キー坊を利用してるとなると、\x01",
            "相当厄介なのは間違いねえだろう。\x02\x03",

            "#00302Fだが、もちろん一歩だって\x01",
            "退いてやるつもりはねえ。\x02\x03",

            "#00309F俺らの可愛い愛娘が\x01",
            "パパたちを待ってるんだ。\x01",
            "とっとと迎えに行ってやろうぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_284B")

    label("loc_27B0")


    #C0057
    ChrTalk(
        0xE,
        (
            "#00302F相手がどんな奴だろうと、\x01",
            "一歩だって退いてやるつもりはねえ。\x02\x03",

            "#00309F俺らの可愛い愛娘が\x01",
            "パパたちを待ってるんだ。\x01",
            "とっとと迎えに行ってやろうぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_284B")

    Jump("loc_3373")

    label("loc_2850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 0)), scpexpr(EXPR_END)), "loc_291F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_286B")
    Call(1, 10)
    Jump("loc_291A")

    label("loc_286B")


    #C0058
    ChrTalk(
        0xE,
        (
            "#00303Fこれからは、俺が見出した足場を\x01",
            "証明し続けなくちゃならねえ。\x02\x03",

            "#00302Fそれが、曲がりなりにも世話になった\x01",
            "死んだ親父や叔父貴への、\x01",
            "俺が出来る最大の義理立てだろうさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_291A")

    Jump("loc_3373")

    label("loc_291F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_END)), "loc_29C4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_293A")
    Call(1, 9)
    Jump("loc_29BF")

    label("loc_293A")


    #C0059
    ChrTalk(
        0xE,
        (
            "#00303F俺もこの先、\x01",
            "叔父貴っつう正真正銘の化物と\x01",
            "決着をつけなくちゃなんねえ。\x02\x03",

            "#00301F今のうちに、\x01",
            "頭を切り替えておかないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29BF")

    Jump("loc_3373")

    label("loc_29C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_2B6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ACF")

    #C0060
    ChrTalk(
        0xE,
        (
            "#00301F《赤い星座》の飛行艇は退けたが、\x01",
            "奴らににとっちゃ\x01",
            "小手調べみたいなもんだろう。\x02\x03",

            "#00303Fこの先には叔父貴やシャーリィが\x01",
            "手ぐすねひいて待ってるはず……\x02\x03",

            "#00301F何を仕掛けてくるか\x01",
            "分かったもんじゃねえ。\x01",
            "絶対に油断するんじゃねえぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2B68")

    label("loc_2ACF")


    #C0061
    ChrTalk(
        0xE,
        (
            "#00303Fこの先には叔父貴やシャーリィが\x01",
            "手ぐすねひいて待ってるはず……\x02\x03",

            "#00301F何を仕掛けてくるか\x01",
            "分かったもんじゃねえ。\x01",
            "絶対に油断するんじゃねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B68")

    Jump("loc_3373")

    label("loc_2B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2CE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C65")

    #C0062
    ChrTalk(
        0xE,
        (
            "#00300Fあの《大樹》がなんだろうが、\x01",
            "俺たちにとっちゃ小さい事だ。\x01",
            "……そうだろ、ロイド？\x02\x03",

            "#00304Fキー坊を俺たちの元に取り戻す。\x01",
            "それさえ忘れなきゃ万事ＯＫだ。\x02\x03",

            "#00300F考えてる暇があったら\x01",
            "とっとと突入するとしようぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2CDB")

    label("loc_2C65")


    #C0063
    ChrTalk(
        0xE,
        (
            "#00304Fハルバードも《ベルゼルガー》も\x01",
            "整備は万全にしてある。\x02\x03",

            "#00300Fとっととキー坊を取り戻しに\x01",
            "行くとしようぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CDB")

    Jump("loc_3373")

    label("loc_2CE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2EEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E2F")

    #C0064
    ChrTalk(
        0xE,
        (
            "#00303F総合的な戦闘力だけで見るなら、\x01",
            "《赤い星座》の方が上だろうが……\x02\x03",

            "#00301F《結社》の奴らには人形兵器もあるし、\x01",
            "あのとんでもねえ槍の達人もいる。\x02\x03",

            "純粋に力だけで立ち向かっても、\x01",
            "簡単には勝たしちゃくれねえだろう。\x02\x03",

            "#00303F……とにかく、\x01",
            "決して侮れねえ奴らだってことだ。\x01",
            "お前も心に留めておけ、ロイド。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2EE5")

    label("loc_2E2F")


    #C0065
    ChrTalk(
        0xE,
        (
            "#00303F《結社》の奴らに\x01",
            "純粋に力だけで立ち向かっても、\x01",
            "簡単には勝たしちゃくれねえだろう。\x02\x03",

            "#00301F……とにかく、\x01",
            "決して侮れねえ奴らだってことだ。\x01",
            "お前も心に留めておけ、ロイド。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EE5")

    Jump("loc_3373")

    label("loc_2EEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_30E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_302D")

    #C0066
    ChrTalk(
        0xE,
        (
            "#00300F『無効宣言』が出されれば、\x01",
            "少なくとも国防軍は\x01",
            "様子見の状態になるだろうが……\x02\x03",

            "#00303F大統領が独自に雇ってる\x01",
            "《赤い星座》の連中は、\x01",
            "今まで通りに襲ってくるだろう。\x02\x03",

            "#00308Fいや……むしろ今まで以上に\x01",
            "なりふり構わねえ手段を\x01",
            "とってくるかもしれねえな。\x02\x03",

            "#00300Fとにかく、警戒は怠れねえな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_30DB")

    label("loc_302D")


    #C0067
    ChrTalk(
        0xE,
        (
            "#00303F無効宣言が出されても、\x01",
            "《赤い星座》の連中は、\x01",
            "今まで通りに襲ってくるだろう。\x02\x03",

            "#00301Fなりふり構わねえ手段を\x01",
            "とってくる可能性もある。\x01",
            "これからも警戒は怠れねえな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30DB")

    Jump("loc_3373")

    label("loc_30E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_31B3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30FB")
    Call(1, 8)
    Jump("loc_31AE")

    label("loc_30FB")


    #C0068
    ChrTalk(
        0xE,
        (
            "#00300Fミシュラムを警備している部隊に、\x01",
            "叔父貴やシャーリィはいねえだろうが……\x02\x03",

            "#00303Fガレスみてえな幹部クラスが\x01",
            "指揮をとってるのは間違いねえ。\x01",
            "……万全に準備をしねえとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31AE")

    Jump("loc_3373")

    label("loc_31B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_3373")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31CE")
    Call(1, 7)
    Jump("loc_3373")

    label("loc_31CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32DB")

    #C0069
    ChrTalk(
        0xE,
        (
            "#00304Fミレイユたちのほうは\x01",
            "マインツの連中も協力してくれてるし、\x01",
            "とりあえずは心配いらねえだろう。\x02\x03",

            "#00300F俺たちも色々やる事はあるが、\x01",
            "まずは目の前の事を片付けるしかねえ。\x02\x03",

            "#00309Fこっからはガンガン頼ってくれ。\x01",
            "お兄さんが暴れまくってやっからよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_3373")

    label("loc_32DB")


    #C0070
    ChrTalk(
        0xE,
        (
            "#00303F俺たちも色々やる事はあるが、\x01",
            "まずは目の前の事を片付けるしかねえ。\x02\x03",

            "#00300Fこっからはガンガン頼ってくれ。\x01",
            "お兄さんが暴れまくってやっからよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3373")

    TalkEnd(0xFE)
    Return()

    # Function_6_263F end

    def Function_7_3377(): pass

    label("Function_7_3377")


    #C0071
    ChrTalk(
        0xE,
        (
            "#00309Fまさか工房まであるたあ……\x01",
            "いや～、メルカバってのは\x01",
            "至れり尽くせりだねえ。\x02\x03",

            "#00300Fこれで《ベルゼルガー》の\x01",
            "定期的なメンテナンスも\x01",
            "欠かさずに済みそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#00000Fそういえばギヨーム親方に\x01",
            "直してもらったんだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xE,
        (
            "#00304Fおう、そん時のアドバイスもあって\x01",
            "使い時を制限してるってわけだ。\x02\x03",

            "#00300Fせっかくダグラスの兄さんに\x01",
            "教えてもらったハルバードも、\x01",
            "腐らせたくはねぇし……\x02\x03",

            "#00300F今後はコイツとハルバードの\x01",
            "二股で行かせてもらうとするぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#00009Fはは、言い方はどうかと思うけど……\x01",
            "それでこそランディっていうか。\x02\x03",

            "#00003Fでも、ダグラス副司令か……\x01",
            "今はどうしてるんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xE,
        (
            "#00303Fあの兄さんのことだから、\x01",
            "今まで通り律儀に副司令の仕事を\x01",
            "全うしてんだろうが……\x02\x03",

            "#00301F司令も含めて、本当に現状に\x01",
            "納得してんのかは分からねえ。\x02\x03",

            "#00303F例え納得がいってないにしても、\x01",
            "ミレイユたちみたいに先陣を切って\x01",
            "反旗を翻すわけにはいかねえだろうしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#00001Fそうだな……\x01",
            "なんとかして司令たちの真意が\x01",
            "確かめられるといいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xE,
        (
            "#00304Fま、色々やらなきゃいけねえだろうが、\x01",
            "まずは目の前の事を片付けるしかねえ。\x02\x03",

            "#00300Fこっからはガンガン頼ってくれ。\x01",
            "お兄さんが暴れまくってやっからよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#00009Fはは……分かった。\x01",
            "頼りにしてるよ、ランディ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 1)
    Return()

    # Function_7_3377 end

    def Function_8_3807(): pass

    label("Function_8_3807")


    #C0079
    ChrTalk(
        0xD,
        (
            "#10703Fミシュラムに陣取っているという\x01",
            "《赤い星座》の部隊……\x02\x03",

            "#10708F……《血染めの#8Rブ ラ ッ デ ィ#シャーリィ》も\x01",
            "いるのでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xE,
        (
            "#00303F……いや、重要人物の監禁場所を\x01",
            "警備するなんてのが、\x01",
            "あいつの性に合ってるとは思えねえ。\x02\x03",

            "#00300F幹部クラスがいるにしても、\x01",
            "恐らく他のヤツが当てられてるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xD,
        "#10703F……そうですか。\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xE,
        (
            "#00303Fリーシャちゃん……\x01",
            "今はお嬢たちを助け出すことに\x01",
            "集中しようぜ。\x02\x03",

            "#00300F叔父貴やシャーリィたちとは、\x01",
            "いずれイヤでも対峙するハメに\x01",
            "なるだろうしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xD,
        (
            "#10708F……ええ、そうですね。\x01",
            "すみません、ランディさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xE,
        "#00309Fハハ、謝るこたあねえけどよ。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xE, 0x10)
    ClearChrFlags(0xD, 0x10)
    SetScenarioFlags(0x0, 5)
    SetScenarioFlags(0x1, 0)
    Return()

    # Function_8_3807 end

    def Function_9_3A71(): pass

    label("Function_9_3A71")


    #C0085
    ChrTalk(
        0xE,
        (
            "#00303Fシャーリィは、物心ついたときから\x01",
            "戦うことにしか喜びを見出せない\x01",
            "正真正銘の人喰い虎だった。\x02\x03",

            "アイツを満たしてやれるのは\x01",
            "殺るか殺られるかの戦場のみ……\x02\x03",

            "#00302Fそんなアイツが、リーシャちゃんに\x01",
            "“殺られる”以外の敗北を喫した……\x01",
            "さぞ、面食らったことだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#00003Fそうだな……\x01",
            "気を失う直前まで\x01",
            "物足りないみたいだったし。\x02\x03",

            "#00002Fでも、ランディは少し\x01",
            "安心してるみたいだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xE,
        (
            "#00302F……ハハ、まあな。\x01",
            "あんなのでも従妹には違いねえし。\x02\x03",

            "#00303F正直、あいつがやった事を考えると\x01",
            "復讐されても仕方ねえとは思ってたが……\x02\x03",

            "#00300Fそうしなかったリーシャちゃんには\x01",
            "改めて感謝しなくちゃいけねえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        "#00002Fはは……そっか。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xE,
        (
            "#00303F……俺もこの先、\x01",
            "叔父貴っつう正真正銘の化物と\x01",
            "決着をつけなくちゃなんねえ。\x02\x03",

            "#00300Fそん時は、是非力を貸してもらうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#00000Fああ、もちろんだ。\x01",
            "みんなで力をあわせて\x01",
            "きっと乗り越えてみせよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 2)
    Return()

    # Function_9_3A71 end

    def Function_10_3DC3(): pass

    label("Function_10_3DC3")


    #C0091
    ChrTalk(
        0xE,
        "#00303Fふう……………………\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#00001Fランディの叔父さん……\x01",
            "やっぱりとんでもない\x01",
            "強さだったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xE,
        (
            "#00302Fああ……お前らが\x01",
            "力を貸してくれたおかげで\x01",
            "なんとか踏ん張れたけどな。\x02\x03",

            "#00306F正直、もう一度やれって言われたら\x01",
            "また勝てるかは怪しいだろう。\x02\x03",

            "#00300F最強の猟兵、《赤の戦鬼》の名は\x01",
            "伊達じゃねえってことだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#00004F……俺たちが力を合わせれば、\x01",
            "きっと何度でも乗り越えられるさ。\x02\x03",

            "#00000Fランディには俺たちがついてるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xE,
        (
            "#00304F……ハハ、そうだな。\x01",
            "それこそが俺の手に入れた強さだ。\x02\x03",

            "#00300Fこれからは、俺が見出した足場を\x01",
            "証明し続けていかねえとな。\x02\x03",

            "#00303Fそれが、曲がりなりにも世話になった\x01",
            "死んだ親父や叔父貴への、\x01",
            "俺が出来る最大の義理立てだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        (
            "#00002Fああ……俺たちも精一杯\x01",
            "それに協力させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xE,
        "#00309Fハハ、ありがとよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 3)
    Return()

    # Function_10_3DC3 end

    def Function_11_40C3(): pass

    label("Function_11_40C3")


    #C0098
    ChrTalk(
        0xE,
        (
            "#00301F最後の相手は、底の知れない\x01",
            "マリアベルお嬢さんと\x01",
            "全ての黒幕であるイアン先生だ。\x02\x03",

            "#00303F単純な戦闘力だけでいうなら\x01",
            "叔父貴やアリオスのオッサンの方が\x01",
            "十分に脅威だろうが……\x02\x03",

            "#00301F《零の至宝》である\x01",
            "キー坊を利用してるとなると、\x01",
            "相当厄介なのは間違いねえだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        (
            "#00008Fああ……アリオスさん以上に\x01",
            "厳しい戦いになるかもしれない。\x02\x03",

            "#00001Fだけど──\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xE,
        (
            "#00304Fそこには全ての真実がある──\x01",
            "絶対に引くわけにはいかない、だろ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0101
    ChrTalk(
        0x101,
        "#00006Fさ、先に言うなよ。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xE,
        (
            "#00309Fハハ、長い付き合いだし\x01",
            "お前の言いそうなことは\x01",
            "大体分かるってこった。\x02\x03",

            "#00304Fもちろん、一歩だって\x01",
            "退いてやるつもりはねえ。\x02\x03",

            "#00302Fなんたって、俺らの可愛い愛娘が\x01",
            "パパたちを待ってるはずだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        (
            "#00000Fああ……そうだな。\x01",
            "みんなでキーアを向かえにいこう！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 4)
    Return()

    # Function_11_40C3 end

    def Function_12_43C4(): pass

    label("Function_12_43C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_4559")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_43E2")
    Call(1, 14)
    Jump("loc_4554")

    label("loc_43E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_44CB")

    #C0104
    ChrTalk(
        0x10,
        (
            "#10100Fここまで来たら、\x01",
            "あとは自分を信じて\x01",
            "飛び込むだけだと思います。\x02\x03",

            "#10104Fこれからクロスベルを守るために……\x01",
            "頑張りましょう、ロイドさん。\x02\x03",

            "#10102F警察や警備隊員である前に\x01",
            "共にこの地に生きる仲間として……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4554")

    label("loc_44CB")


    #C0105
    ChrTalk(
        0x10,
        (
            "#10100Fこれからクロスベルを守るために……\x01",
            "頑張りましょう、ロイドさん。\x02\x03",

            "警察や警備隊員である前に\x01",
            "共にこの地に生きる仲間として……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4554")

    Jump("loc_4F6B")

    label("loc_4559")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_46C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4650")

    #C0106
    ChrTalk(
        0x10,
        (
            "#10106F強襲揚陸艦の出現には\x01",
            "驚きましたけど……\x02\x03",

            "#10100Fなんとか無事に《大樹》に\x01",
            "到着できて良かったですね。\x02\x03",

            "#10103Fただ、今後もあれが\x01",
            "現れないとは限りません。\x02\x03",

            "#10101F待機メンバーは十分に\x01",
            "注意しないといけませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_46C0")

    label("loc_4650")


    #C0107
    ChrTalk(
        0x10,
        (
            "#10103F今後も強襲揚陸艦が\x01",
            "現れないとは限りません。\x02\x03",

            "#10101F待機メンバーは十分に\x01",
            "注意しないといけませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46C0")

    Jump("loc_4F6B")

    label("loc_46C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_48CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4836")

    #C0108
    ChrTalk(
        0x10,
        (
            "#10103Fアリオスさんが失踪した事で、\x01",
            "国防軍全体の指揮権が\x01",
            "ソーニャ司令に移ったみたいです。\x02\x03",

            "#10100Fしばらくは《大樹》の出現で\x01",
            "混乱が起こってしまっている\x01",
            "各地の対応に追われるみたいですね。\x02\x03",

            "#10104F大変だと思いますが……\x01",
            "ソーニャ司令にお任せすれば\x01",
            "きっと大丈夫だと思います。\x02\x03",

            "#10100Fあたしたちは、\x01",
            "眼の前の目標に向かって\x01",
            "突き進みましょう！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_48CA")

    label("loc_4836")


    #C0109
    ChrTalk(
        0x10,
        (
            "#10104F国防軍のことは、\x01",
            "ソーニャ司令にお任せすれば\x01",
            "きっと大丈夫だと思います。\x02\x03",

            "#10100Fあたしたちは、\x01",
            "眼の前の目標に向かって\x01",
            "突き進みましょう！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48CA")

    Jump("loc_4F6B")

    label("loc_48CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_4AA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_49EB")

    #C0110
    ChrTalk(
        0x10,
        (
            "#10101F《月の僧院》も《星見の塔》も、\x01",
            "もとは警備隊の管理下にあった遺跡です。\x02\x03",

            "#10106Fなんとか鐘の正体を掴んでさえいれば、\x01",
            "ここまでの事態には\x01",
            "ならなかったのかもしれません……\x02\x03",

            "#10103F……後悔しても始まりませんよね。\x01",
            "とにかく、今は前を向いていかないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4A9C")

    label("loc_49EB")


    #C0111
    ChrTalk(
        0x10,
        (
            "#10108F事前に鐘の正体を掴んでさえいれば、\x01",
            "ここまでの事態には\x01",
            "ならなかったのかもしれません……\x02\x03",

            "#10103F……後悔しても始まりませんよね。\x01",
            "とにかく、今は前を向いていかないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A9C")

    Jump("loc_4F6B")

    label("loc_4AA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_4C9E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BDC")

    #C0112
    ChrTalk(
        0x10,
        (
            "#10103F独立国の正当性が揺らぐ事……\x02\x03",

            "#10101Fそれは国防軍という組織そのものの\x01",
            "正当性が揺らぐ事に他なりません。\x02\x03",

            "#10108Fソーニャ司令が上手くまとめて\x01",
            "くれるとは思いますが、\x01",
            "相当な混乱は免れないでしょうね。\x02\x03",

            "#10103F……２大国が内戦や恐慌で動けないのは、\x01",
            "ある意味救いなのかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4C99")

    label("loc_4BDC")


    #C0113
    ChrTalk(
        0x10,
        (
            "#10101Fいざ無効宣言が出されれば、\x01",
            "ベルカード門、タングラム門……\x01",
            "どの部隊にも相当な混乱が訪れるはず……\x02\x03",

            "#10103F……２大国が内戦や恐慌で動けないのは、\x01",
            "ある意味救いなのかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C99")

    Jump("loc_4F6B")

    label("loc_4C9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_4F6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CB9")
    Call(1, 13)
    Jump("loc_4F6B")

    label("loc_4CB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ECC")

    #C0114
    ChrTalk(
        0x10,
        (
            "#10105Fあ、ロ、ロイドさん……\x02\x03",

            "#10111Fあのっ、あたし……\x01",
            "“君をもらう”なんて言われて\x01",
            "確かにびっくりしましたけど……\x02\x03",

            "#10106Fその、ロイドさんが\x01",
            "そういう意味で言ったんじゃないって\x01",
            "ちゃんと分かってますから！！\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#00005Fえっと、『そういう意味』って\x01",
            "どういう意味なのか、\x01",
            "いまいち分かんないんだが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0116
    ChrTalk(
        0x10,
        (
            "#10106F（ほ、本気で言ってるのかな……）\x02\x03",

            "#10100F……コホン、とにかく。\x01",
            "今はミシュラムの攻略を\x01",
            "第一に考えていきましょう！\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#00000Fああ、もちろんだ。\x01",
            "頼りにしてるぞ、ノエル。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_4F6B")

    label("loc_4ECC")


    #C0118
    ChrTalk(
        0x10,
        (
            "#10100F……コホン、とにかく。\x01",
            "今はミシュラムの攻略を\x01",
            "第一に考えていきましょう！\x02\x03",

            "あたしもエリィさんと\x01",
            "マクダエル議長のために、\x01",
            "力を尽くさせてもらいます！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F6B")

    TalkEnd(0xFE)
    Return()

    # Function_12_43C4 end

    def Function_13_4F6F(): pass

    label("Function_13_4F6F")

    OP_4B(0x10, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0119
    ChrTalk(
        0xC,
        (
            "#01912Fはぁあ……\x01",
            "お姉ちゃんと再会できて\x01",
            "ほんとによかったよ～。\x02\x03",

            "#01911Fううっ、なんだかまた\x01",
            "泣けてきちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x10,
        (
            "#10112Fもう、フランったら……\x02\x03",

            "#10104F……でも、あたしも\x01",
            "フランの怪我がすっかり治ってて\x01",
            "本当に安心しちゃった。\x02\x03",

            "#10109Fそれにロイドさんやワジ君のもとで\x01",
            "しっかりと働いてたみたいだし。\x01",
            "ふふ、えらいえらい。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xC,
        (
            "#01906Fも、もうお姉ちゃんったら、\x01",
            "いつまでも子供扱いして～……\x02\x03",

            "#01905F……あ、そっか。\x01",
            "お姉ちゃんはロイドさんに\x01",
            "“もらわれて”来たんだもんね～。\x02\x03",

            "#01906F大人への階段を３段飛ばしくらいで\x01",
            "上ったんだから、そりゃわたしも\x01",
            "子供にみえて仕方ないっていうか……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x10)

    #C0122
    ChrTalk(
        0x10,
        (
            "#10111Fば、ばかっ……！\x01",
            "何言ってるのよ、フランってば！\x02\x03",

            "#10106Fロイドさんもそういう意味で\x01",
            "言ったんじゃ……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xC,
        (
            "#01909Fわわっ、お姉ちゃんったら\x01",
            "思い出して照れてる～。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        (
            "#00004F（……何の話か分からないけど……\x01",
            "  微妙に会話に入りづらい雰囲気だな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 5)
    OP_4C(0x10, 0xFF)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0x10, 0x10)
    ClearChrFlags(0xC, 0x10)
    Return()

    # Function_13_4F6F end

    def Function_14_52F1(): pass

    label("Function_14_52F1")


    #C0125
    ChrTalk(
        0x10,
        (
            "#10101Fいよいよ大詰めですね……\x02\x03",

            "#10103Fここまで来たら、\x01",
            "あとは自分を信じて\x01",
            "飛び込むだけだと思います。\x02\x03",

            "#10108Fこの事件が終わっても、\x01",
            "クロスベルには多くの苦難が\x01",
            "待ち受けていると思いますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        (
            "#00004Fああ……だけど、\x01",
            "結局は目の前のことを\x01",
            "一つ一つ片付けていくしかないんだ。\x02\x03",

            "#00000Fこの事件を解決する事こそが、\x01",
            "これからクロスベルを守っていくための\x01",
            "第一歩になるんじゃないかと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x10,
        (
            "#10109Fふふ、きっと父が生きていたら\x01",
            "同じ事を言ってくれたと思います。\x02\x03",

            "#10103Fこれからクロスベルを守るために……\x01",
            "頑張りましょう、ロイドさん。\x02\x03",

            "#10102F警察や警備隊員である前に\x01",
            "共にこの地に生きる仲間として……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 6)
    Return()

    # Function_14_52F1 end

    def Function_15_5550(): pass

    label("Function_15_5550")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_572D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_556E")
    Call(1, 18)
    Jump("loc_5728")

    label("loc_556E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5678")

    #C0128
    ChrTalk(
        0xA,
        (
            "#10404Fしばらく一緒にいて感じたけど、\x01",
            "君たちとキーアの“絆”は本物だ。\x02\x03",

            "#10402F例え何があろうと、\x01",
            "君たちが求め続ける限りは\x01",
            "希望があるんじゃないかと思うよ。\x02\x03",

            "#10409Fま、こうなったら僕も\x01",
            "とことん付き合わせてもらうよ。\x01",
            "可愛いキーアのためにもね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5728")

    label("loc_5678")


    #C0129
    ChrTalk(
        0xA,
        (
            "#10404F例え何があろうと、\x01",
            "君たちが求め続ける限りは\x01",
            "希望があるんじゃないかと思うよ。\x02\x03",

            "#10409Fま、こうなったら僕も\x01",
            "とことん付き合わせてもらうよ。\x01",
            "可愛いキーアのためにもね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5728")

    Jump("loc_6D44")

    label("loc_572D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_END)), "loc_5805")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5748")
    Call(1, 17)
    Jump("loc_5800")

    label("loc_5748")


    #C0130
    ChrTalk(
        0xA,
        (
            "#10404Fようやく彼に、僕なりの\x01",
            "けじめを付けることができた。\x01",
            "……礼を言わせてもらうよ。\x02\x03",

            "#10402Fここからは星杯騎士として、\x01",
            "特務支援課のメンバーとして、\x01",
            "君たちを手伝わせてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5800")

    Jump("loc_6D44")

    label("loc_5805")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 4)), scpexpr(EXPR_END)), "loc_591F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5825")
    Call(1, 55)
    Jump("loc_591A")

    label("loc_5825")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_7B(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_58A4")

    #C0131
    ChrTalk(
        0xA,
        (
            "#10403Fどうやら“彼”は\x01",
            "僕との決着をお望みらしい。\x02\x03",

            "#10400F準備が出来たら、\x01",
            "さっそく障壁へ向かおう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_591A")

    label("loc_58A4")


    #C0132
    ChrTalk(
        0xA,
        (
            "#10403Fどうやら“彼”は\x01",
            "僕との決着をお望みらしい。\x02\x03",

            "#10400F僕を探索メンバーに入れてくれ。\x01",
            "一緒に障壁へ向かおう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_591A")

    Jump("loc_6D44")

    label("loc_591F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_5A88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_59FE")

    #C0133
    ChrTalk(
        0xA,
        (
            "#10404Fさてと、いよいよ探索開始だね。\x02\x03",

            "#10401Fメルカバで進めないのは残念だけど……\x01",
            "この先には“彼”も待っている。\x02\x03",

            "#10403F付け損ねたけじめを\x01",
            "改めて付けるためにも、\x01",
            "地道に進んでいかなきゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5A83")

    label("loc_59FE")


    #C0134
    ChrTalk(
        0xA,
        (
            "#10401F《大樹》を進んだ先には\x01",
            "“彼”も待っている。\x02\x03",

            "#10403F付け損ねたけじめを\x01",
            "改めて付けるためにも、\x01",
            "地道に進んでいかなきゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A83")

    Jump("loc_6D44")

    label("loc_5A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5CF5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5C3A")

    #C0135
    ChrTalk(
        0xA,
        (
            "#10403Fあの《大樹》の出現に、\x01",
            "アルテリア法国のほうも\x01",
            "大騒ぎになっているみたいだ。\x02\x03",

            "#10400F何せ、教会のどの聖典にも\x01",
            "記されていないだろう\x01",
            "“予定外の奇蹟”だからね。\x02\x03",

            "#10408F《塩の杭》の一件もあるし、\x01",
            "上層部も慎重にならざるを\x01",
            "得ないだろうな……\x02\x03",

            "#10400Fでも、あそこにキーアがいる以上、\x01",
            "のんびりともしてられないだろう。\x02\x03",

            "責任は僕が持たせてもらうから、\x01",
            "《大樹》に向かうなら遠慮なく\x01",
            "アッバスに指示してくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5CF0")

    label("loc_5C3A")


    #C0136
    ChrTalk(
        0xA,
        (
            "#10404Fあそこにキーアがいる以上、\x01",
            "アルテリア法国の指示を\x01",
            "悠長に待っている暇もない。\x02\x03",

            "#10400F責任は僕が持たせてもらうから、\x01",
            "《大樹》に向かうなら遠慮なく\x01",
            "アッバスに指示してくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5CF0")

    Jump("loc_6D44")

    label("loc_5CF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_5F4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E7A")

    #C0137
    ChrTalk(
        0xA,
        (
            "#10400F《結社》と僕たち騎士団は、\x01",
            "歴史の裏で幾度となく対立してきた。\x01",
            "いわば宿命の相手ってことさ。\x02\x03",

            "#10403F彼らの事は騎士団でも調べてるけど、\x01",
            "《道化師》と《鋼の聖女》に関しては\x01",
            "特に情報が少なくてね。\x02\x03",

            "有効な対抗手段がないまま\x01",
            "戦いに臨むことになっちゃうけど……\x02\x03",

            "#10402F虎穴に入らずんば虎児を得ずとも言うし、\x01",
            "とにかく飛び込んで\x01",
            "勝機を窺ってみようじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_5F48")

    label("loc_5E7A")


    #C0138
    ChrTalk(
        0xA,
        (
            "#10403F《結社》の事は騎士団でも調べてるけど、\x01",
            "《道化師》と《鋼の聖女》に関しては\x01",
            "特に情報が少なくてね。\x02\x03",

            "#10402F虎穴に入らずんば虎児を得ずとも言うし、\x01",
            "とにかく飛び込んで\x01",
            "勝機を窺ってみようじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5F48")

    Jump("loc_6D44")

    label("loc_5F4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_60FC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6082")

    #C0139
    ChrTalk(
        0xA,
        (
            "#10402Fブースター地点の周辺なら、\x01",
            "特に警戒もされていないみたいだね。\x02\x03",

            "#10404F国防軍や猟兵も警備範囲外だし、\x01",
            "これならメルカバで向かっても\x01",
            "邪魔が入らずにすみそうだ。\x02\x03",

            "#10408Fこの『無効宣言』によって\x01",
            "これからの因果がどう変わりゆくか……\x02\x03",

            "#10409Fフフ、あとは女神のみぞ知るってね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_60F7")

    label("loc_6082")


    #C0140
    ChrTalk(
        0xA,
        (
            "#10404Fこの『無効宣言』によって\x01",
            "これからの因果がどう変わりゆくか……\x02\x03",

            "#10409Fフフ、あとは女神のみぞ知るってね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_60F7")

    Jump("loc_6D44")

    label("loc_60FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_6366")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62BC")

    #C0141
    ChrTalk(
        0xA,
        (
            "#10402Fミシュラムのビーチか……\x01",
            "こんな形で行くことになるとはね。\x02\x03",

            "#10406Fできればまた、みんなでのんびりと\x01",
            "休暇に行きたかった所だけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        (
            "#00004Fキーアを取り戻して……\x01",
            "……何もかも終わったら、\x01",
            "きっとみんなでまた来よう。\x02\x03",

            "#00000F今度は課長やアッバス、\x01",
            "ソーニャ司令なんかも\x01",
            "誘ってみてもいいかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        (
            "#10409Fアハハ、それはいいね！\x02\x03",

            "#10400Fそんな日をこの手に掴むためにも、\x01",
            "せいぜい努力させてもらうとするよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6361")

    label("loc_62BC")


    #C0144
    ChrTalk(
        0xA,
        (
            "#10404Fミシュラムのビーチ……\x01",
            "今回は休暇どころか厳しい戦いが\x01",
            "待っているだろうね。\x02\x03",

            "#10400F平穏な日々をこの手に掴むためにも、\x01",
            "せいぜい努力させてもらうとするよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6361")

    Jump("loc_6D44")

    label("loc_6366")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_66D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_65D8")

    #C0145
    ChrTalk(
        0xA,
        (
            "#10404Fやれやれ、グレイスさんにかかると\x01",
            "なんでもインタビューになっちゃうね。\x02\x03",

            "アッバスが怒るから\x01",
            "あんまり大した事は言えないんだけど……\x02\x03",

            "#10409Fこの勢いに押されたら、\x01",
            "あることないこと喋っちゃいそうだよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xF, 0x10)
    TurnDirection(0xF, 0xA, 0)
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_64DB")
    Jump("loc_6525")

    label("loc_64DB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_64FB")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6525")

    label("loc_64FB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_651B")
    OP_52(0xF, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6525")

    label("loc_651B")

    OP_52(0xF, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6525")

    OP_52(0xF, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xF, 0x10)

    #C0146
    ChrTalk(
        0xF,
        (
            "#02109Fあ、ダメよワジ君～。\x01",
            "『あること』に限定してよね！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0147
    ChrTalk(
        0x101,
        "#00006F（アッバスも苦労するな……）\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0x0)
    SetScenarioFlags(0x0, 7)
    Jump("loc_66CD")

    label("loc_65D8")


    #C0148
    ChrTalk(
        0xA,
        (
            "#10404F要するに、テスタメンツってのは\x01",
            "僕の渾名から『聖典#4Rテスタメント#』を\x01",
            "適当にもじった名前だったわけさ。\x02\x03",

            "#10409Fボクは正直、何でもよかったんだけど\x01",
            "アッバスがうるさくてね。\x01",
            "彼、形から入りたがるタイプだから。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_66CD")

    Jump("loc_6D44")

    label("loc_66D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_69EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6949")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_682E")

    #C0149
    ChrTalk(
        0xA,
        (
            "#10403Fリーシャ、甲板に立って\x01",
            "物思いに耽ってるみたいだね。\x02\x03",

            "アルカンシェル、黒月、\x01",
            "そして《銀》の使命……\x01",
            "思い悩む事が多いんだろうな。\x02\x03",

            "#10402Fフフ、良かったら\x01",
            "君が相談に乗ったらどうだい？\x02\x03",

            "#10409Fもしかしたら、何らかのフラグが\x01",
            "立つかもしれないよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#00003Fそ、そんな下心満載で\x01",
            "相談になんて乗らないから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6941")

    label("loc_682E")


    #C0151
    ChrTalk(
        0xA,
        (
            "#10403Fリーシャ、甲板に立って\x01",
            "物思いに耽ってるみたいだね。\x02\x03",

            "アルカンシェル、黒月、\x01",
            "そして《銀》の使命……\x01",
            "思い悩む事が多いんだろうな。\x02\x03",

            "#10402Fフフ、それで……\x01",
            "相談に乗ってたみたいだけど、\x01",
            "何かフラグは立ったかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        (
            "#00006Fそ、そんなのを立てに\x01",
            "行ったんじゃないから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6941")

    SetScenarioFlags(0x0, 7)
    Jump("loc_69EA")

    label("loc_6949")


    #C0153
    ChrTalk(
        0xA,
        (
            "#10404Fそれにしてもリーシャって、\x01",
            "今の服装を抜きにすれば\x01",
            "とても《銀》には見えないよね。\x02\x03",

            "#10400Fフフ、あの性格が素だからこその\x01",
            "天然の隠遁術ってところかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69EA")

    Jump("loc_6D44")

    label("loc_69EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_6B7E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AF9")

    #C0154
    ChrTalk(
        0xA,
        (
            "#10400Fティオたちが入ってきたおかげで、\x01",
            "艦の運用効率が大幅に上がりそうだ。\x02\x03",

            "#10404F《隙間》を見つけるにしても、\x01",
            "僕たちだけじゃ限界があったからね。\x01",
            "これは大きな前進と言えるよ。\x02\x03",

            "#10400Fフフ、これも女神の巡りあわせ\x01",
            "なのかもしれないね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6B79")

    label("loc_6AF9")


    #C0155
    ChrTalk(
        0xA,
        (
            "#10404F最初に行ったウルスラ病院で\x01",
            "ティオたちと合流できたこと……\x02\x03",

            "#10400Fフフ、これも女神の巡りあわせ\x01",
            "なのかもしれないね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B79")

    Jump("loc_6D44")

    label("loc_6B7E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_6D44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B99")
    Call(1, 16)
    Jump("loc_6D44")

    label("loc_6B99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CC2")

    #C0156
    ChrTalk(
        0xA,
        (
            "#10406Fなかなかに前途多難だけど……\x01",
            "とりあえず地道にやってかないとね。\x02\x03",

            "#10400F……そうそう、メルカバ内の施設は\x01",
            "自由に使ってくれて構わないからね。\x02\x03",

            "装備・備品・工房機能──\x01",
            "上の廊下に出れば仮眠室も利用できる。\x02\x03",

            "#10409Fクルーへの目通しも兼ねて\x01",
            "一通り確認してきたらどうだい？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_6D44")

    label("loc_6CC2")


    #C0157
    ChrTalk(
        0xA,
        (
            "#10400Fメルカバ内の施設は\x01",
            "自由に使ってくれて構わないからね。\x02\x03",

            "#10409Fクルーへの目通しも兼ねて\x01",
            "一通り確認してきたらどうだい？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6D44")

    TalkEnd(0xFE)
    Return()

    # Function_15_5550 end

    def Function_16_6D48(): pass

    label("Function_16_6D48")


    #C0158
    ChrTalk(
        0xA,
        (
            "#10403Fとりあえず、異変が起きる前に\x01",
            "ウルスラ間道の中洲の先に\x01",
            "《隙間》は見つけておいたけど……\x02\x03",

            "#10400F今後は着陸できそうな《隙間》を\x01",
            "探知・発見していく必要がある。\x02\x03",

            "#10406Fメルカバも人手不足だし、\x01",
            "なかなかに前途多難だねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x101,
        (
            "#00003F……それでも、一歩ずつ\x01",
            "進んでいくしかない。\x02\x03",

            "#00001F仲間とキーアを取り戻す……\x01",
            "それが簡単にいかないのは\x01",
            "百も承知だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xA,
        (
            "#10402Fフフ、分かってるさ。\x01",
            "とりあえず地道にやってかないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D7, 7)
    Return()

    # Function_16_6D48 end

    def Function_17_6EFC(): pass

    label("Function_17_6EFC")


    #C0161
    ChrTalk(
        0xA,
        "#10402Fやあ、お疲れだったね。\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x101,
        (
            "#00005Fワジのほうこそ……\x01",
            "体の方は大丈夫なのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xA,
        (
            "#10404Fああ、もう心配ないよ。\x01",
            "一休みしたらご覧の通りさ。\x02\x03",

            "#10408F反動が大きいから、\x01",
            "普段は出来るだけ力を\x01",
            "抑えるようにしてるんだけど……\x02\x03",

            "#10404Fフフ、僕も久しぶりに\x01",
            "熱くなってしまったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        (
            "#00000F全力を出して\x01",
            "ヴァルドを叩き伏せる……\x02\x03",

            "それが必要だったんだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xA,
        (
            "#10404Fああ、その通りだ。\x02\x03",

            "#10408F……最初から全力を出していれば、\x01",
            "彼があそこまで思いつめることも\x01",
            "無かったのかもしれないけどね。\x02\x03",

            "#10403Fその点に関しては、\x01",
            "全面的に僕に責任があるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        "#00005Fそんなことは……\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xA,
        (
            "#10402Fフフ、いいんだ。\x01",
            "後悔しているわけじゃないけど、\x01",
            "今後の教訓にはしなきゃね。\x02\x03",

            "#10404Fとにかく……\x01",
            "ようやく彼に、僕なりの\x01",
            "けじめを付けることができた。\x02\x03",

            "テスタメンツのリーダー、\x01",
            "ワジ・ヘミスフィアの使命は\x01",
            "これで一通り済んだだろう。\x02\x03",

            "#10402F見届けてくれた君たちには、\x01",
            "礼を言わせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        (
            "#00009Fはは……どういたしまして。\x02\x03",

            "#00000Fこの先も相当な強敵が\x01",
            "待ち構えているだろうけど……\x01",
            "改めてよろしくお願いするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xA,
        (
            "#10402Fフフ、了解だリーダー。\x02\x03",

            "#10404Fここからは星杯騎士として、\x01",
            "特務支援課のメンバーとして、\x01",
            "君たちを手伝わせてもらおう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 1)
    Return()

    # Function_17_6EFC end

    def Function_18_736F(): pass

    label("Function_18_736F")


    #C0170
    ChrTalk(
        0xA,
        (
            "#10400F《風の剣聖》から\x01",
            "色々な情報は得られたけど、\x01",
            "いくつかはまだ謎のままだ。\x02\x03",

            "#10403F《碧#2Rあお#き零#2Rゼロ#の計画》……\x01",
            "熊ヒゲ先生の計画したその全容。\x02\x03",

            "#10408Fマリアベル嬢が知っているはずの\x01",
            "《零の至宝》キーアの潜在能力と、\x01",
            "それをどう計画に利用しているか。\x02\x03",

            "#10406Fこの辺りは直接問いただしてみるしか\x01",
            "方法はなさそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        (
            "#00001Fああ……彼らの元に辿り着いたら\x01",
            "きっと分かるはずだ。\x02\x03",

            "#00008Fキーアがなぜ、\x01",
            "彼らに付き従っているかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xA,
        (
            "#10404F……まあ、心配しなくても大丈夫さ。\x02\x03",

            "#10402Fしばらく一緒にいて感じたけど、\x01",
            "君たちとキーアの“絆”は本物だ。\x02\x03",

            "#10409F例え何があろうと、\x01",
            "君たちが求め続ける限りは\x01",
            "希望があるんじゃないかと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x101,
        (
            "#00000F……そうだな。\x01",
            "きっと何もかも上手くいくはずだ。\x02\x03",

            "#00005Fでも、他人事みたいに言ってるけど\x01",
            "ワジもその“絆”の中にいるんだからな？\x02\x03",

            "#00004Fキーアだってきっとそう思ってる……\x01",
            "みんな一緒にあの子を迎えにいこう。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xA,
        (
            "#10404F……フフ、嬉しいことを\x01",
            "言ってくれるじゃないか。\x02\x03",

            "#10402Fこうなったら僕も\x01",
            "とことん付き合わせてもらうよ。\x01",
            "可愛いキーアのためにもね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 2)
    Return()

    # Function_18_736F end

    def Function_19_7764(): pass

    label("Function_19_7764")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_796A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7782")
    Call(1, 21)
    Jump("loc_7965")

    label("loc_7782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78AB")

    #C0175
    ChrTalk(
        0xD,
        (
            "#10708F《銀》とアーティストの道……\x01",
            "まだこの先どうしていくか\x01",
            "具体的には決めていませんが……\x02\x03",

            "#10704F今の私には、クロスベルを……\x01",
            "イリアさんたちのいるこの地を\x01",
            "守りたい気持ちが確かにあります。\x02\x03",

            "#10702F“大切なもの”を守るために……\x01",
            "皆さんと一緒に力を尽くさせて\x01",
            "いただきます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7965")

    label("loc_78AB")


    #C0176
    ChrTalk(
        0xD,
        (
            "#10704F今の私には、クロスベルを……\x01",
            "イリアさんたちのいるこの地を\x01",
            "守りたい気持ちが確かにあります。\x02\x03",

            "#10702F“大切なもの”を守るために……\x01",
            "皆さんと一緒に力を尽くさせて\x01",
            "いただきます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7965")

    Jump("loc_857E")

    label("loc_796A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A8, 3)), scpexpr(EXPR_END)), "loc_7A30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7985")
    Call(1, 20)
    Jump("loc_7A2B")

    label("loc_7985")


    #C0177
    ChrTalk(
        0xD,
        (
            "#10703Fみなさんのおかげで、\x01",
            "ようやく彼女とのけじめを\x01",
            "付けることが出来ました。\x02\x03",

            "#10702Fそのご恩を返す為にも……\x01",
            "この事件には最後まで\x01",
            "関わらせて頂こうと思います。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A2B")

    Jump("loc_857E")

    label("loc_7A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 5)), scpexpr(EXPR_END)), "loc_7B8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A50")
    Call(1, 54)
    Jump("loc_7B87")

    label("loc_7A50")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_7B(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7AF6")

    #C0178
    ChrTalk(
        0xD,
        (
            "#10703F……準備は出来ています。\x01",
            "すぐに障壁へ向かいましょう。\x02\x03",

            "#10701F私自身が、この先の道を\x01",
            "見出すためにも……\x01",
            "彼女ともう一度見えなくては。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B87")

    label("loc_7AF6")


    #C0179
    ChrTalk(
        0xD,
        (
            "#10703F……準備は出来ています。\x01",
            "私を探索班に加えてください。\x02\x03",

            "#10701F私自身が、この先の道を\x01",
            "見出すためにも……\x01",
            "彼女ともう一度見えなくては。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B87")

    Jump("loc_857E")

    label("loc_7B8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_7D06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C64")

    #C0180
    ChrTalk(
        0xD,
        (
            "#10703F……ついにここまで来ましたね。\x02\x03",

            "“彼女”も含めて、この先には\x01",
            "かなりの使い手が揃っている……\x02\x03",

            "#10701F心を引き締めて掛かりましょう。\x01",
            "私たちの大切なものを、\x01",
            "この手に掴む為にも……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7D01")

    label("loc_7C64")


    #C0181
    ChrTalk(
        0xD,
        (
            "#10703F“彼女”も含めて、この先には\x01",
            "かなりの使い手が揃っている……\x02\x03",

            "#10701F心を引き締めて掛かりましょう。\x01",
            "私たちの大切なものを、\x01",
            "この手に掴む為にも……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D01")

    Jump("loc_857E")

    label("loc_7D06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_807C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F06")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E60")

    #C0182
    ChrTalk(
        0xD,
        (
            "#10703F私自身のけじめのためにも……\x01",
            "《大樹》で待つ“彼女”と\x01",
            "決着を付ける必要があります。\x02\x03",

            "#10701F……覚悟は出来ています。\x01",
            "準備が整い次第、出発しましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        (
            "#00003F（アルカンシェルを解放した\x01",
            "  今なら、もしかして……）\x02\x03",

            "（《大樹》に向かう前に、\x01",
            "  リーシャを“あの人”の所へ\x01",
            "  連れて行こうかな……？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_7F01")

    label("loc_7E60")


    #C0184
    ChrTalk(
        0xD,
        (
            "#10703F私自身のけじめのためにも……\x01",
            "《大樹》で待つ“彼女”と\x01",
            "決着を付ける必要があります。\x02\x03",

            "#10701F……覚悟は出来ています。\x01",
            "準備が整い次第、出発しましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7F01")

    Jump("loc_8077")

    label("loc_7F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FF9")

    #C0185
    ChrTalk(
        0xD,
        (
            "#10704Fイリアさんに勇気をもらった\x01",
            "今の私に、怖いものはありません。\x02\x03",

            "#10701Fあとは、私自身のけじめのためにも\x01",
            "“彼女”と決着を付けなければ……\x02\x03",

            "#10702F……覚悟は出来ています。\x01",
            "準備が整い次第、\x01",
            "《大樹》へと向かいましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8077")

    label("loc_7FF9")


    #C0186
    ChrTalk(
        0xD,
        (
            "#10704Fイリアさんに勇気をもらった\x01",
            "今の私に、怖いものはありません。\x02\x03",

            "#10702F準備が整い次第、\x01",
            "《大樹》へと向かいましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8077")

    Jump("loc_857E")

    label("loc_807C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_8259")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8192")

    #C0187
    ChrTalk(
        0xD,
        (
            "#10708F《銀》である私が、クロスベルを救う\x01",
            "お手伝いをしているなんて……\x02\x03",

            "#10703F今更ながら、なんだか身に余る\x01",
            "役であるような気がしてきました。\x02\x03",

            "#10701F……でも、これもクロスベル市と\x01",
            "アルカンシェルを解放するため……\x01",
            "精一杯やらせていただきたいです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8254")

    label("loc_8192")


    #C0188
    ChrTalk(
        0xD,
        (
            "#10708F《銀》である私が、クロスベルを救う\x01",
            "お手伝いをしているなんて、\x01",
            "身に余る役な気もしますけど……\x02\x03",

            "#10701Fクロスベル市と\x01",
            "アルカンシェルを解放するため……\x01",
            "精一杯やらせていただきたいです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8254")

    Jump("loc_857E")

    label("loc_8259")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_8301")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8274")
    Call(1, 8)
    Jump("loc_82FC")

    label("loc_8274")


    #C0189
    ChrTalk(
        0xD,
        (
            "#10708F《血染めのシャーリィ》……\x01",
            "彼女の動向は気になりますけど……\x02\x03",

            "#10703F……今はエリィさんたちを\x01",
            "助け出すことに集中しましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82FC")

    Jump("loc_857E")

    label("loc_8301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_857E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_84C2")

    #C0190
    ChrTalk(
        0xD,
        (
            "#10705Fほ、本当に《銀》のことを\x01",
            "記事にしないでもらえるんでしょうか。\x02\x03",

            "#10706Fなんだか心配になってきました……\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xF,
        (
            "#02103Fみんなの気になる劇団の裏話！\x01",
            "伝説の《銀》の歴史と舞台裏！\x01",
            "リーシャ・マオのスリーサイズ！\x02\x03",

            "#02109Fせっかくの機会ですもの、\x01",
            "洗いざらい喋ってもらうわよ～♪\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0192
    ChrTalk(
        0xD,
        "#10706Fううう、ロイドさ～ん……\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x101,
        (
            "#00012Fな、なんとか、\x01",
            "上手くかわしてくれ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xF, 0x0)
    SetScenarioFlags(0x1, 0)
    Jump("loc_857E")

    label("loc_84C2")


    #C0194
    ChrTalk(
        0xD,
        (
            "#10706Fいつもは劇団長が適当な所で\x01",
            "切り上げてくれてたんですが……\x01",
            "こ、こんなにしつこかったなんて。\x02\x03",

            "#10709F本当に記事にしないで\x01",
            "もらえるんでしょうか……\x01",
            "なんだか心配になってきました。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_857E")

    TalkEnd(0xFE)
    Return()

    # Function_19_7764 end

    def Function_20_8582(): pass

    label("Function_20_8582")


    #C0195
    ChrTalk(
        0xD,
        (
            "#10703F《血染めのシャーリィ》……\x02\x03",

            "その呼び名の通り、彼女の道は\x01",
            "血に塗れていたのでしょう。\x02\x03",

            "それを生き甲斐とし、\x01",
            "戦場に喜びを見出したからこそ\x01",
            "現在の彼女がある……\x02\x03",

            "#10708F《銀》である私にとって、\x01",
            "それは決して他人事ではありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x101,
        "#00001Fリーシャ……\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xD,
        (
            "#10704Fだけど……私はようやく、\x01",
            "本当の意味で変われた気がします。\x02\x03",

            "#10702Fイリアさんやロイドさんたち……\x01",
            "沢山の人々との出会いが\x01",
            "私を変えてくれたんだと思います。\x02\x03",

            "#10703F似た者同士であるはずの私と彼女が、\x01",
            "全く別の道を歩むことになるくらいに……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x101,
        (
            "#00004F人が人と出会うこと……\x02\x03",

            "#00000F考えてみれば、これほどまでに\x01",
            "因果なことは無いのかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xD,
        (
            "#10702Fええ……本当にそう思います。\x02\x03",

            "#10704F……みなさんのおかげで、\x01",
            "ようやく彼女とのけじめを\x01",
            "付けることが出来ました。\x02\x03",

            "#10702Fそのご恩を返す為にも……\x01",
            "この事件には最後まで\x01",
            "関わらせて頂こうと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        (
            "#00000Fああ、よろしく頼むよリーシャ。\x02\x03",

            "一緒にキーアを助け出して……\x01",
            "イリアさんたちの所に笑顔で帰ろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xD,
        "#10709Fふふ、はいっ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 5)
    Return()

    # Function_20_8582 end

    def Function_21_8943(): pass

    label("Function_21_8943")


    #C0202
    ChrTalk(
        0xD,
        (
            "#10708F……旅の終わりが\x01",
            "近づいてきましたね。\x02\x03",

            "#10703Fあのマリアベルさんに、\x01",
            "《銀》としての力がどこまで\x01",
            "通用するか分かりませんが……\x02\x03",

            "#10701Fとにかく、皆さんと一緒に\x01",
            "力を尽くさせてもらうだけです。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        (
            "#00000Fああ……よろしく頼むよ。\x02\x03",

            "#00009Fはは、今更だけど……\x01",
            "戦ったり力を合わせたり、\x01",
            "俺たちも色々あったよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xD,
        (
            "#10709Fあ、あはは……\x01",
            "その説はすみませんでした。\x02\x03",

            "#10703F《銀》とアーティストの道……\x01",
            "まだこの先どうしていくか\x01",
            "具体的には決めていませんが……\x02\x03",

            "#10702F今の私には、クロスベルを……\x01",
            "イリアさんたちのいるこの地を\x01",
            "守りたい気持ちが確かにあります。\x02\x03",

            "#10704F培ってきた《銀》としての力が\x01",
            "それに役立つというのなら……\x01",
            "私は迷いなく力を振るえるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x101,
        (
            "#00004Fありがとう、リーシャ……\x01",
            "頼りにさせてもらうよ。\x02\x03",

            "#00000F俺たちの“大切なもの”を\x01",
            "守るために、一緒に頑張ろう！\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xD,
        "#10702Fはいっ……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 6)
    Return()

    # Function_21_8943 end

    def Function_22_8C72(): pass

    label("Function_22_8C72")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_8E4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C90")
    Call(1, 23)
    Jump("loc_8E45")

    label("loc_8C90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D88")

    #C0207
    ChrTalk(
        0x13,
        (
            "#01203F#3Cかつて《幻の至宝#8Rデ ミ ウ ル ゴ ス#》は\x01",
            "自らを消滅させることを選んだ……\x02\x03",

            "#01200Fキーアが同じ結論に\x01",
            "辿り着いてしまう可能性は、\x01",
            "ないとは言えんだろう。\x02\x03",

            "人の子よ、見事キーアを取り戻し、\x01",
            "それを阻止して見せるがいい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8E45")

    label("loc_8D88")


    #C0208
    ChrTalk(
        0x13,
        (
            "#01203F#3Cキーアが《幻の至宝#8Rデ ミ ウ ル ゴ ス#》と\x01",
            "同じ結論に辿り着いてしまう可能性は、\x01",
            "ないとは言えんだろう。\x02\x03",

            "#01200F人の子よ、見事キーアを取り戻し、\x01",
            "それを阻止して見せるがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8E45")

    Jump("loc_9AC1")

    label("loc_8E4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_8FB6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F34")

    #C0209
    ChrTalk(
        0x13,
        (
            "#01203F#3C《大樹》のどこかに\x01",
            "キーアがいるのは間違いあるまい。\x02\x03",

            "#01200Fおそらくは最も深き場所……\x01",
            "あのクロイス家の娘、そして\x01",
            "黒幕である弁護士と共にな。\x02\x03",

            "私の助けが必要になったら\x01",
            "いつでも呼び出すがいい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_8FB1")

    label("loc_8F34")


    #C0210
    ChrTalk(
        0x13,
        (
            "#01203F#3C《大樹》のどこかに\x01",
            "キーアがいるのは間違いあるまい。\x02\x03",

            "#01200F私の助けが必要になったら\x01",
            "いつでも呼び出すがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FB1")

    Jump("loc_9AC1")

    label("loc_8FB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_9147")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90A2")

    #C0211
    ChrTalk(
        0x13,
        (
            "#01200F#3Cあの《大樹》に\x01",
            "どこまでの事が出来るのか、\x01",
            "私にも見当がつかぬ。\x02\x03",

            "女神に匹敵する力を有している……\x01",
            "そう言っても過言ではなかろう。\x02\x03",

            "#01203F人の子が妄執の果てに\x01",
            "ここまでの境地に辿り着こうとはな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_9142")

    label("loc_90A2")


    #C0212
    ChrTalk(
        0x13,
        (
            "#01200F#3Cあの《大樹》に\x01",
            "女神に匹敵する力を有している……\x01",
            "そう言っても過言ではなかろう。\x02\x03",

            "#01203F人の子が妄執の果てに\x01",
            "ここまでの境地に辿り着こうとはな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9142")

    Jump("loc_9AC1")

    label("loc_9147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_938C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92C7")

    #C0213
    ChrTalk(
        0x13,
        (
            "#01203F#3Cクロスベルに点在していた鐘は\x01",
            "《至宝》の力を増幅させる“場”を\x01",
            "生み出すためのもの……\x02\x03",

            "#01200F現状と照らし合わせても、\x01",
            "ヨルグの調査結果は信用していいだろう。\x02\x03",

            "#01203Fしかし、例の教団の揺籃#4Rゆりかご#を\x01",
            "生み出したことといい……\x01",
            "人の子の手でここまでの所業を成すとはな。\x02\x03",

            "#01200F改めて、クロイス家の錬金術師たちの\x01",
            "途方もない妄執が窺えるようだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_9387")

    label("loc_92C7")


    #C0214
    ChrTalk(
        0x13,
        (
            "#01203F#3Cしかし、例の教団の揺籃#4Rゆりかご#を\x01",
            "生み出したことといい……\x01",
            "人の子の手でここまでの所業を成すとはな。\x02\x03",

            "#01200F改めて、クロイス家の錬金術師たちの\x01",
            "途方もない妄執が窺えるようだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9387")

    Jump("loc_9AC1")

    label("loc_938C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_9554")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_93A7")
    Call(1, 4)
    Jump("loc_954F")

    label("loc_93A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94AF")

    #C0215
    ChrTalk(
        0x13,
        (
            "#01203F#3C今のおぬしらなら、\x01",
            "私のお守りなど必要あるまい。\x02\x03",

            "#01200F以前と同様、後ろに控えているから\x01",
            "必要な時は呼び出すがいい。\x02\x03",

            "これからは元の姿に戻った状態で\x01",
            "戦線に駆けつけよう。\x02\x03",

            "#01203Fフフ、そこいらの魔獣程度なら\x01",
            "一飲みにしてくれようぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_954F")

    label("loc_94AF")


    #C0216
    ChrTalk(
        0x13,
        (
            "#01200F#3C必要な時に呼び出してくれれば、\x01",
            "これからは元の姿に戻った状態で\x01",
            "戦線に駆けつけよう。\x02\x03",

            "#01203Fフフ、そこいらの魔獣程度なら\x01",
            "一飲みにしてくれようぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_954F")

    Jump("loc_9AC1")

    label("loc_9554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_97A2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9704")

    #C0217
    ChrTalk(
        0x13,
        (
            "#01200F#3C猟兵たちの陽動は任せるがいい。\x01",
            "元の姿に戻れば、かなりの戦力を\x01",
            "引きつけられるはずだ。\x02\x03",

            "その間に分散した部隊を退けつつ、\x01",
            "エリィたちのもとへ向かうといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x101,
        (
            "#00003F相手は猟兵だ、ツァイトも\x01",
            "相当危険があると思うけど……\x02\x03",

            "#00001Fどうか、気をつけてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x13,
        (
            "#01203F#3Cフフ、案ずるな。\x01",
            "私とて易々とやられるつもりはない。\x02\x03",

            "#01200F神狼としての誇りを掛けて、\x01",
            "存分に敵を翻弄させてもらうとしよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_979D")

    label("loc_9704")


    #C0220
    ChrTalk(
        0x13,
        (
            "#01203F#3C元の姿に戻れば、猟兵といえど\x01",
            "かなりの戦力を引きつけられるはずだ。\x02\x03",

            "#01200F神狼としての誇りを掛けて、\x01",
            "存分に敵を翻弄させてもらうとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_979D")

    Jump("loc_9AC1")

    label("loc_97A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_985D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_97BD")
    Call(1, 3)
    Jump("loc_9858")

    label("loc_97BD")


    #C0221
    ChrTalk(
        0x13,
        (
            "#01200F#3Cウルスラが生きていた時代より\x01",
            "代々クロスベルを見てきた我が眷属だ。\x02\x03",

            "今はどこぞでこの状況を\x01",
            "見守っているだろうし、\x01",
            "心配をすることもあるまい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9858")

    Jump("loc_9AC1")

    label("loc_985D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_9AC1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A2D")

    #C0222
    ChrTalk(
        0x13,
        "#01200F#3C……あの看護師の娘は……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0223
    ChrTalk(
        0x101,
        (
            "#00005Fえっと……\x01",
            "セシル姉がどうかしたのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x13,
        (
            "#01203F#3C……フフ、いやなに。\x01",
            "まさに因果だと思ってな。\x02\x03",

            "大したことではないから\x01",
            "気にせずともよかろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        "#00000Fへ……？\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x13,
        (
            "#01200F#3Cともかく、ティオとの\x01",
            "再会を果たせたのは\x01",
            "僥倖と言えるだろう。\x02\x03",

            "この調子で支援課の仲間を\x01",
            "取り戻していくがいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#00000Fあ、ああ、よく分からないけど……\x01",
            "そうさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_9AC1")

    label("loc_9A2D")


    #C0228
    ChrTalk(
        0x13,
        (
            "#01200F#3Cともかく、ティオとの\x01",
            "再会を果たせたのは\x01",
            "僥倖と言えるだろう。\x02\x03",

            "今は何やら忙しそうだが……\x01",
            "フフ、あとで様子を\x01",
            "見に行ってやるとするか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AC1")

    TalkEnd(0xFE)
    Return()

    # Function_22_8C72 end

    def Function_23_9AC5(): pass

    label("Function_23_9AC5")


    #C0229
    ChrTalk(
        0x13,
        (
            "#01200F#3Cかつて《幻の至宝#8Rデ ミ ウ ル ゴ ス#》は\x01",
            "自らを消滅させることを選んだ……\x02\x03",

            "ロイド、おぬしにはそう話したな。\x02",
        )
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x101,
        (
            "#00001F暴走して、守るべき人々を\x01",
            "傷つけてしまうのを防ぐため……\x01",
            "そういう話だったな。\x02\x03",

            "#00003F……《零の至宝》であるキーアも、\x01",
            "そうなってしまうのか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x13,
        (
            "#01200F#3C……それは分からぬ。\x02\x03",

            "だが、キーアは《零の至宝》となり\x01",
            "ついには女神に匹敵する力を持つ\x01",
            "《大樹》をも生み出した。\x02\x03",

            "それほどまでの大いなる力を、\x01",
            "この先、制御していける保証は\x01",
            "今のところどこにもない。\x02\x03",

            "#01203F《幻の至宝#8Rデ ミ ウ ル ゴ ス#》と同じ結論に\x01",
            "辿り着いてしまう可能性は、\x01",
            "ないとは言えんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        (
            "#00003Fそうか……\x02\x03",

            "#00001Fいや、絶対にさせるもんか。\x01",
            "俺たちがいる限り……！\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x13,
        "#01200F#3C……フフ、それでこそおぬしだ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 0)
    Return()

    # Function_23_9AC5 end

    def Function_24_9D9D(): pass

    label("Function_24_9D9D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9DC4")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x7F), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_9DC4")
    OP_50(0x6B, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    SetScenarioFlags(0x1DE, 3)

    label("loc_9DC4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6B), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9DDF")
    Call(1, 53)
    Jump("loc_A440")

    label("loc_9DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_9E90")

    #C0234
    ChrTalk(
        0x14,
        (
            "#00603Fお前にはお前の素質がある。\x01",
            "そこを伸ばしていくことで\x01",
            "優秀な捜査官へと近づけるだろう。\x02\x03",

            "#00602F自分なりの捜査官を目指し、\x01",
            "今後も一層精進していくがいい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A440")

    label("loc_9E90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_A00E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9EAB")
    Call(1, 25)
    Jump("loc_A009")

    label("loc_9EAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F8B")

    #C0235
    ChrTalk(
        0x14,
        (
            "#00603Fガイ・バニングスの死……\x01",
            "３年の時を越えて、ようやく\x01",
            "その真相が明らかになった。\x02\x03",

            "あとは、この事件を\x01",
            "真の意味で解決させるだけだ。\x02\x03",

            "#00602F行くぞ、バニングス。\x01",
            "今こそお前の兄を越えてみせるがいい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_A009")

    label("loc_9F8B")


    #C0236
    ChrTalk(
        0x14,
        (
            "#00603Fあとは、この事件を\x01",
            "真の意味で解決させるだけだ。\x02\x03",

            "#00602F行くぞ、バニングス。\x01",
            "今こそお前の兄を越えてみせるがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A009")

    Jump("loc_A440")

    label("loc_A00E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_A225")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A154")

    #C0237
    ChrTalk(
        0x14,
        (
            "#00600F足を止めるな、バニングス。\x01",
            "真実に近づくためには\x01",
            "一歩ずつ歩みを進めるしかない。\x02\x03",

            "#00603F何より、《大樹》がクロスベルに\x01",
            "どんな影響を及ぼすか分からない以上、\x01",
            "この事件は早急に片付ける必要がある。\x02\x03",

            "#00608Fイアン先生、マクレイン……\x01",
            "一筋縄ではいかない相手たちだが、\x01",
            "必ずや乗り越えてみせるぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_A220")

    label("loc_A154")


    #C0238
    ChrTalk(
        0x14,
        (
            "#00600F《大樹》がクロスベルに\x01",
            "どんな影響を及ぼすか分からない以上、\x01",
            "この事件は早急に片付ける必要がある。\x02\x03",

            "#00608Fイアン先生、マクレイン……\x01",
            "一筋縄ではいかない相手たちだが、\x01",
            "必ずや乗り越えてみせるぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A220")

    Jump("loc_A440")

    label("loc_A225")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A440")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A393")

    #C0239
    ChrTalk(
        0x14,
        (
            "#00608Fまさか、イアン先生が\x01",
            "黒幕だったとはな……\x02\x03",

            "#00610Fクッ、事務所に足繁く\x01",
            "通っていながら何てザマだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        "#00003Fダドリーさん……\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x14,
        (
            "#00603F……とにかく、こうなった以上は\x01",
            "先生やマクレインに直接会って\x01",
            "真意を問いただすしかないだろう。\x02\x03",

            "#00601Fもはや支援課だけの問題ではない。\x01",
            "なんとしても真実を掴みとるぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x101,
        "#00000Fはい……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_A440")

    label("loc_A393")


    #C0243
    ChrTalk(
        0x14,
        (
            "#00603Fとにかく、こうなった以上は\x01",
            "先生やマクレインに直接会って\x01",
            "真意を問いただすしかないだろう。\x02\x03",

            "#00600Fもはや支援課だけの問題ではない。\x01",
            "なんとしても真実を掴みとるぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A440")

    TalkEnd(0xFE)
    Return()

    # Function_24_9D9D end

    def Function_25_A444(): pass

    label("Function_25_A444")


    #C0244
    ChrTalk(
        0x14,
        (
            "#00600Fガイ・バニングスの死……\x01",
            "３年の時を経て、ようやく\x01",
            "その真相が明らかになったか。\x02\x03",

            "#00603Fマクレインは、そんな重荷を\x01",
            "今まで背負っていたのだな。\x02\x03",

            "#00608F……どこまでも不器用な奴だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x101,
        (
            "#00003Fすべてを自らの戒めとし、\x01",
            "逃げ道を断つ事で\x01",
            "前へと進んでいく……\x02\x03",

            "#00008Fだからこそアリオスさんは\x01",
            "強かったのかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x14,
        (
            "#00603F……だが、それは間違った強さだ。\x02\x03",

            "#00608Fそれはヤツにも分かっていた筈……\x01",
            "だからこそお前たちに道をあけたのだろう。\x02\x03",

            "#00600Fとにかく、バニングス。\x01",
            "これでお前もガイの死を\x01",
            "乗り超えられるはずだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        (
            "#00004F……はい。\x01",
            "改めて整理は必要でしょうが、\x01",
            "もう大丈夫です。\x02\x03",

            "#00001F今は最後の《壁》……\x01",
            "イアン先生とマリアベルさんを\x01",
            "乗り越えることに目を向けないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x14,
        (
            "#00604Fそれでいい。\x02\x03",

            "#00602Fこの事件を真の意味で\x01",
            "解決させるためにも……\x01",
            "今はただ前進あるのみだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        "#00000Fはい……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 2)
    Return()

    # Function_25_A444 end

    def Function_26_A778(): pass

    label("Function_26_A778")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A786")
    Call(0, 11)
    Return()

    label("loc_A786")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A7A8")
    Call(1, 56)
    TalkEnd(0xFE)
    Return()

    label("loc_A7A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A936")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A7D6")
    RunExpression(0xA, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0x8, 0x0, 0)

    label("loc_A7D6")


    #C0250
    ChrTalk(
        0x8,
        (
            "#12100F……そうだ、せっかくだから\x01",
            "お前たちにこれを渡しておこう。\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0251
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『アッバスのアカウント』\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x28, 0)
    OP_E4(0x3)

    #C0252
    ChrTalk(
        0x101,
        (
            "#00000F『ポムっと！』のアカウント……？\x01",
            "アッバスもやってるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x8,
        (
            "#12102F時間が空いたときだけだがな。\x02\x03",

            "#12100F気が向いたら相手をしてやるから、\x01",
            "勝負を申し込んでくるがいい。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x8, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A931")
    OP_52(0x8, 0x4, (scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A931")

    Jump("loc_A973")

    label("loc_A936")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A94C")
    Call(1, 28)
    Jump("loc_A973")

    label("loc_A94C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A962")
    Call(1, 29)
    Jump("loc_A973")

    label("loc_A962")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A973")
    Call(1, 30)

    label("loc_A973")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A984")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C3BF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_A9DD")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",                # 0
            "メルカバで移動する\x01",      # 1
            "パーティ編成\x01",            # 2
            "やめる\x01",                  # 3
        )
    )

    MenuEnd(0x0)
    Jump("loc_AA25")

    label("loc_A9DD")


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",                # 0
            "メルカバで移動する\x01",      # 1
            "やめる\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AA25")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_AA25")

    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_AA44"),
        (1, "loc_C050"),
        (2, "loc_C394"),
        (SWITCH_DEFAULT, "loc_C3B0"),
    )


    label("loc_AA44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_AB6F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB03")

    #C0254
    ChrTalk(
        0x8,
        (
            "#12100F《赤い星座》とは今後も\x01",
            "関わる事があるかもしれんが……\x02\x03",

            "今はこの事件を解決する事が\x01",
            "なによりも重要だろう。\x02\x03",

            "最後の戦いに向けて\x01",
            "万全の準備を整えるがいい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_AB6A")

    label("loc_AB03")


    #C0255
    ChrTalk(
        0x8,
        (
            "#12100F我々も星杯騎士として、\x01",
            "最後まで使命を全うしよう。\x02\x03",

            "お前たちも、\x01",
            "万全の準備を整えるがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB6A")

    Jump("loc_C04B")

    label("loc_AB6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 7)), scpexpr(EXPR_END)), "loc_ABFF")

    #C0256
    ChrTalk(
        0x8,
        (
            "#12100F……バイパーの連中も\x01",
            "さぞ、ヴァルドのことを\x01",
            "心配していることだろう。\x02\x03",

            "クロスベルの危機が去ったら\x01",
            "回収してやらねばな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C04B")

    label("loc_ABFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_AE79")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ACDD")

    #C0257
    ChrTalk(
        0x8,
        (
            "#12100F機体に受けたダメージは軽微だ。\x01",
            "飛行には一切問題あるまい。\x02\x03",

            "我々は、いつでも\x01",
            "《大樹》を離脱できるよう\x01",
            "艦内に待機している。\x02\x03",

            "《大樹》を離脱する場合は\x01",
            "そう指示するがいい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_AD48")

    label("loc_ACDD")


    #C0258
    ChrTalk(
        0x8,
        (
            "#12100Fメルカバもとりあえずは\x01",
            "大した損傷がないようだ。\x02\x03",

            "《大樹》を離脱する場合は\x01",
            "そう指示するがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AD48")

    Jump("loc_AE74")

    label("loc_AD4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE07")

    #C0259
    ChrTalk(
        0x8,
        (
            "#12100F機体に受けたダメージは軽微だ。\x01",
            "飛行には一切問題あるまい。\x02\x03",

            "《碧の大樹》内部への\x01",
            "安全なルートも確保できた。\x02\x03",

            "再び《大樹》を目指す場合は\x01",
            "そう指示するがいい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_AE74")

    label("loc_AE07")


    #C0260
    ChrTalk(
        0x8,
        (
            "#12100Fメルカバもとりあえずは\x01",
            "大した損傷がないようだ。\x02\x03",

            "再び《大樹》を目指す場合は\x01",
            "そう指示するがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE74")

    Jump("loc_C04B")

    label("loc_AE79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B035")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AFA0")

    #C0261
    ChrTalk(
        0x8,
        (
            "#12100F《碧の大樹》の出現が\x01",
            "何を意味するか、教会も\x01",
            "いまだに掴めていない状況だ。\x02\x03",

            "いざ、あそこに乗り込めば、\x01",
            "どんな事態が起こっても\x01",
            "おかしくはあるまい。\x02\x03",

            "今ならクロスベルの各地に\x01",
            "降りることも可能だが……\x02\x03",

            "やるべき事があるなら\x01",
            "そちらを優先しても\x01",
            "いいかもしれんな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_B030")

    label("loc_AFA0")


    #C0262
    ChrTalk(
        0x8,
        (
            "#12100F《碧の大樹》の出現が\x01",
            "何を意味するか、教会も\x01",
            "いまだに掴めていない状況だ。\x02\x03",

            "いずれにせよ、乗り込む前に\x01",
            "しっかりと準備しておくことだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B030")

    Jump("loc_C04B")

    label("loc_B035")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_B477")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_END)), "loc_B256")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1A7")

    #C0263
    ChrTalk(
        0x8,
        (
            "#12100F止めるべき鐘はあと一つ……\x01",
            "ウルスラ間道はずれの《星見の塔》だ。\x02\x03",

            "だが、使徒の一柱である\x01",
            "《鋼の聖女》アリアンロードと\x01",
            "部下の戦乙女たちが待ち構えている。\x02\x03",

            "乗り越えるのは至難の業だろうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x101,
        (
            "#00001F……とにかく、やるしかない。\x01",
            "なんとかして勝機を見出そう。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x8,
        (
            "#12102Fうむ、よく言った。\x01",
            "覚悟が決まったら向かうとしよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_B251")

    label("loc_B1A7")


    #C0266
    ChrTalk(
        0x8,
        (
            "#12100F《星見の塔》には、\x01",
            "使徒の一柱である《鋼の聖女》と\x01",
            "部下の戦乙女たちが待ち構えている。\x02\x03",

            "乗り越えるのは至難の業だろうが……\x01",
            "覚悟を決めて乗り越えてみせるがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B251")

    Jump("loc_B472")

    label("loc_B256")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3C1")

    #C0267
    ChrTalk(
        0x8,
        (
            "#12100F最初の目的地は《月の僧院》……\x01",
            "マインツ方面にある、\x01",
            "中世の遺跡の一つだな。\x02\x03",

            "ヨルグ老人によれば、\x01",
            "待ち受けているのは執行者の１人\x01",
            "《道化師》カンパネルラ……\x02\x03",

            "普段は裏方に徹しているようで、\x01",
            "こちらも情報はほとんどない。\x01",
            "……かなり不気味な人物だ。\x02\x03",

            "何を仕掛けてくるか分からん。\x01",
            "あらゆる状況に対応できるよう\x01",
            "十二分な備えをしておくがいい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_B472")

    label("loc_B3C1")


    #C0268
    ChrTalk(
        0x8,
        (
            "#12100F《月の僧院》に\x01",
            "待ち受けているのは執行者の１人、\x01",
            "《道化師》カンパネルラ……\x02\x03",

            "何を仕掛けてくるか分からん。\x01",
            "あらゆる状況に対応できるよう\x01",
            "十二分な備えをしておくがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B472")

    Jump("loc_C04B")

    label("loc_B477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_B6CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5ED")

    #C0269
    ChrTalk(
        0x8,
        (
            "#12100Fマクダエル議長が奪われたことで、\x01",
            "地上は国防軍と猟兵によって\x01",
            "厳戒態勢になったようだ。\x02\x03",

            "この状況では、メルカバを各地に\x01",
            "着陸させることはできないだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x101,
        (
            "#00001Fそうか……だとすると、\x01",
            "今はブースター地点での作戦に\x01",
            "集中した方がよさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x8,
        (
            "#12100Fうむ、あとは開始のタイミングを\x01",
            "見計らうだけだ。\x02\x03",

            "準備が出来たら声をかけるがいい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_B6C6")

    label("loc_B5ED")


    #C0272
    ChrTalk(
        0x8,
        (
            "#12100Fこの厳戒態勢下では、メルカバを各地に\x01",
            "着陸させることはできまい。\x02\x03",

            "今はブースター地点に向かい\x01",
            "作戦を成功させることに\x01",
            "集中したほうがいいだろう。\x02\x03",

            "こちらの段取りはついている。\x01",
            "準備が出来たら声をかけるがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B6C6")

    Jump("loc_C04B")

    label("loc_B6CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_B92C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B856")

    #C0273
    ChrTalk(
        0x8,
        (
            "#12100Fミシュラムに到着したら、\x01",
            "すぐにでも猟兵の迎撃が\x01",
            "始まる事が予想される。\x02\x03",

            "対空兵器による撃墜を防ぐためにも\x01",
            "メルカバはしばらく\x01",
            "上空に身を隠すつもりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x101,
        (
            "#00006F一度降りたら、エリィたちを\x01",
            "助け出すまでは戻れない……か。\x01",
            "やっぱり厳しい戦いになりそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x8,
        (
            "#12100Fうむ、恐らく想像以上にな。\x02\x03",

            "装備、オーブメント、回復薬……\x01",
            "全てを万全に整えておくがいい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_B927")

    label("loc_B856")


    #C0276
    ChrTalk(
        0x8,
        (
            "#12100Fミシュラムで戦闘が始まったら\x01",
            "対空兵器による撃墜を防ぐためにも\x01",
            "艦はしばらく上空に身を隠すつもりだ。\x02\x03",

            "その間、お前たちも艦には戻れない。\x01",
            "装備、オーブメント、回復薬……\x01",
            "全てを万全に整えておくがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B927")

    Jump("loc_C04B")

    label("loc_B92C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_BB45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BAC0")

    #C0277
    ChrTalk(
        0x8,
        (
            "#12100Fあの記者はこのメルカバやワジの事を\x01",
            "細かく調べているようだな。\x02\x03",

            "……やれやれ、報道に携わる者を\x01",
            "乗せてしまうなど、前代未聞なのだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x101,
        (
            "#00012Fま、まあ……さすがに\x01",
            "ただの好奇心だと思うし、\x01",
            "大丈夫じゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x8,
        (
            "#12100F……まあいい。\x01",
            "ワジが許可したことだしな。\x02\x03",

            "もしものことがあれば、\x01",
            "バニングス、お前にも責任を\x01",
            "取ってもらうぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x101,
        "#00006F（な、なんで俺が……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_BB40")

    label("loc_BAC0")


    #C0281
    ChrTalk(
        0x8,
        (
            "#12100Fやれやれ、報道に携わる者を\x01",
            "乗せてしまうなど、\x01",
            "前代未聞なのだが……\x02\x03",

            "まあ、ワジが許可したことだし\x01",
            "仕方があるまいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB40")

    Jump("loc_C04B")

    label("loc_BB45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_BCAB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC0D")

    #C0282
    ChrTalk(
        0x8,
        (
            "#12100F《黒月》とは別の信念の元に動く\x01",
            "警備隊のレジスタンスか……\x02\x03",

            "どちらにせよ、反旗を翻した以上は\x01",
            "大統領サイドも放っておくまい。\x02\x03",

            "行くなら急いだ方がいいかもしれんな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_BCA6")

    label("loc_BC0D")


    #C0283
    ChrTalk(
        0x8,
        (
            "#12100Fいくら警備隊のレジスタンスとはいえ、\x01",
            "国防軍と猟兵という戦力を相手に\x01",
            "長く持ちこたえるのは難しいだろう。\x02\x03",

            "行くなら急いだ方がいいかもしれんな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCA6")

    Jump("loc_C04B")

    label("loc_BCAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_BEAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BDFF")

    #C0284
    ChrTalk(
        0x8,
        (
            "#12100Fメルカバの機関部に使われている\x01",
            "《天の車》は、元は飛翔機能をもつ\x01",
            "アーティファクトの乗り物だったが……\x02\x03",

            "導力革命以降、財団の協力で\x01",
            "現在の形に改修されたのだ。\x02\x03",

            "それ以外にも、戦術オーブメントの\x01",
            "開発などにも一部協力している。\x02\x03",

            "……だが、あくまで\x01",
            "世俗には非公式の事柄だ。\x01",
            "くれぐれも外部に漏らさぬようにな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_BEA7")

    label("loc_BDFF")


    #C0285
    ChrTalk(
        0x8,
        (
            "#12100Fメルカバや戦術オーブメントは\x01",
            "財団と教会が協力があって\x01",
            "はじめて生まれたものだが……\x02\x03",

            "……あくまで世俗には非公式の事柄だ。\x01",
            "くれぐれも外部に漏らさぬようにな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BEA7")

    Jump("loc_C04B")

    label("loc_BEAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_C04B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEC7")
    Call(1, 27)
    Jump("loc_C04B")

    label("loc_BEC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BFC5")

    #C0286
    ChrTalk(
        0x8,
        (
            "#12100F新たな場所に移動するときには\x01",
            "ワジの指揮と《神機》への警戒が必要だが、\x01",
            "現状ならこの体制で十分だろう。\x02\x03",

            "こちらの心配はいらないから、\x01",
            "装備やオーブメントの準備を\x01",
            "十分に整えておけ。\x02\x03",

            "地上に降りる準備が出来たら\x01",
            "声をかけるがいい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_C04B")

    label("loc_BFC5")


    #C0287
    ChrTalk(
        0x8,
        (
            "#12100Fこちらの心配はいらないから、\x01",
            "装備やオーブメントの準備を\x01",
            "十分に整えておけ。\x02\x03",

            "地上に降りる準備が出来たら\x01",
            "声をかけるがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C04B")

    Jump("loc_C3BA")

    label("loc_C050")

    FadeToDark(300, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)), "loc_C385")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C173")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C0A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C16E")
    Call(0, 39)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C169")
    OP_50(0x1E, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C169")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)), "loc_C15A")
    FadeToDark(500, 0, -1)
    Sleep(500)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C14A")
    Call(0, 6)
    Jump("loc_C14D")

    label("loc_C14A")

    Call(0, 5)

    label("loc_C14D")

    Call(0, 7)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Jump("loc_C169")

    label("loc_C15A")

    FadeToBright(0, 0)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Return()

    label("loc_C169")

    Jump("loc_C0A9")

    label("loc_C16E")

    Jump("loc_C37F")

    label("loc_C173")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C25A")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C190")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C255")
    Call(0, 23)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C250")
    OP_50(0x1E, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C250")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)), "loc_C241")
    FadeToDark(500, 0, -1)
    Sleep(500)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C231")
    Call(0, 6)
    Jump("loc_C234")

    label("loc_C231")

    Call(0, 5)

    label("loc_C234")

    Call(0, 7)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Jump("loc_C250")

    label("loc_C241")

    FadeToBright(0, 0)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Return()

    label("loc_C250")

    Jump("loc_C190")

    label("loc_C255")

    Jump("loc_C37F")

    label("loc_C25A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C341")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C277")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C33C")
    Call(0, 21)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C337")
    OP_50(0x1E, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C337")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)), "loc_C328")
    FadeToDark(500, 0, -1)
    Sleep(500)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C318")
    Call(0, 6)
    Jump("loc_C31B")

    label("loc_C318")

    Call(0, 5)

    label("loc_C31B")

    Call(0, 7)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Jump("loc_C337")

    label("loc_C328")

    FadeToBright(0, 0)
    TalkEnd(0xFE)
    EventEnd(0x6)
    Return()

    label("loc_C337")

    Jump("loc_C277")

    label("loc_C33C")

    Jump("loc_C37F")

    label("loc_C341")

    FadeToDark(500, 0, -1)
    Sleep(500)
    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C35D")
    Call(0, 12)

    label("loc_C35D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C374")
    Call(0, 6)
    Jump("loc_C377")

    label("loc_C374")

    Call(0, 5)

    label("loc_C377")

    Call(0, 7)
    TalkEnd(0xFE)
    EventEnd(0x6)

    label("loc_C37F")

    Return()

    label("loc_C385")

    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_C3BA")

    label("loc_C394")

    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(0)
    Fade(500)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C3BA")

    label("loc_C3B0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C3BA")

    Jump("loc_A984")

    label("loc_C3BF")

    OP_60(0x0)
    TalkEnd(0xFE)
    Return()

    # Function_26_A778 end

    def Function_27_C3C6(): pass

    label("Function_27_C3C6")


    #C0288
    ChrTalk(
        0x8,
        (
            "#12100F先ほど、連絡が入ってな。\x01",
            "メルカバ伍号機が無事に\x01",
            "《神機》を振り切ったようだ。\x02\x03",

            "グラハム卿たちクルーに\x01",
            "ひとまず被害はないらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x101,
        (
            "#00004Fそうか……安心したよ。\x02\x03",

            "#00005F……そういえば、アッバス。\x01",
            "操縦席から離れて大丈夫なのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x8,
        (
            "#12100F心配は無用だ……\x01",
            "この席で《メルカバ》の殆どの機能を\x01",
            "掌握することができるからな。\x02\x03",

            "それに、今は自動操縦モードにして\x01",
            "《隙間》上空に滞空しているから、\x01",
            "操縦席に座る必要もない。\x02\x03",

            "新たな場所に移動するときには\x01",
            "ワジの指揮と《神機》への警戒が必要だが、\x01",
            "現状ならこの体制で十分だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x101,
        (
            "#00003Fなるほど……\x01",
            "やっぱり相当な高性能みたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x8,
        (
            "#12100Fとにかく、艦にいる間は\x01",
            "準備を十分に整えておけ。\x02\x03",

            "地上に降りる準備が出来たら\x01",
            "声をかけるがいい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 3)
    Return()

    # Function_27_C3C6 end

    def Function_28_C67F(): pass

    label("Function_28_C67F")


    #C0293
    ChrTalk(
        0x8,
        (
            "#12100F機体の鏡面装甲と\x01",
            "対衝撃フィールドに任せて\x01",
            "強行突破したが……\x02\x03",

            "機体に受けたダメージは軽微だ。\x01",
            "飛行には一切問題あるまい。\x02\x03",

            "我々は、いつでも\x01",
            "《大樹》を離脱できるよう\x01",
            "艦内に待機している。\x02\x03",

            "《大樹》を離脱する場合は\x01",
            "そう指示するがいい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 5)
    Return()

    # Function_28_C67F end

    def Function_29_C776(): pass

    label("Function_29_C776")


    #C0294
    ChrTalk(
        0x8,
        (
            "#12100Fヴァルドを退けたそうだな。\x02\x03",

            "……奴とは、２年前に\x01",
            "ワジと共にクロスベルに潜入して\x01",
            "以来の付き合いだが……\x02\x03",

            "カモフラージュとして\x01",
            "テスタメンツを結成してから、\x01",
            "ワジはどこか楽しそうだった。\x02\x03",

            "一時期、ルバーチェが\x01",
            "陰謀を働いた事件のときは\x01",
            "若干険悪になりはしたが……\x02\x03",

            "ワジにとって、ヴァルドは\x01",
            "良き喧嘩仲間であり、\x01",
            "親友でもあったのだろう。\x02\x03",

            "#12102F無論、ヴァルドにとってのワジもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x101,
        "#00005Fた、確かに結構息はあってたけど……\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x8,
        (
            "#12100F奴に本気を出さなかったのは、\x01",
            "そういう要素が一因として\x01",
            "あったからかもしれない。\x02\x03",

            "まあ、ワジは言葉には出さぬから\x01",
            "本当のところは分からないが……\x02\x03",

            "……無駄な話をしてしまった。\x01",
            "くれぐれも他言せぬようにな。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x101,
        "#00000Fあ、ああ分かった。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 6)
    Return()

    # Function_29_C776 end

    def Function_30_CA1D(): pass

    label("Function_30_CA1D")


    #C0298
    ChrTalk(
        0x8,
        (
            "#12100F……先ほど、お前たちが\x01",
            "《剣聖》と戦っていた時だが……\x02\x03",

            "この《神域》に\x01",
            "飛行物体が侵入したのを\x01",
            "艦のレーダーが感知した。\x02\x03",

            "どうやら、赤い星座の\x01",
            "《ベイオウルフ号》のようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0299
    ChrTalk(
        0x101,
        "#00005Fえっ……大丈夫だったのか！？\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x8,
        (
            "#12100Fうむ、こちらには目もくれず\x01",
            "別の地点に降り立ち、しばらくして\x01",
            "《大樹》の外に離脱したようだ。\x02\x03",

            "おそらく、《赤の戦鬼》と\x01",
            "《血染めのシャーリィ》を\x01",
            "回収していったのだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        (
            "#00003Fそうか……\x01",
            "警察としては彼らにも\x01",
            "事情聴取をしたかったけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x8,
        (
            "#12100Fまあ、仕方があるまい。\x01",
            "待機班だけでは阻止しようも\x01",
            "なかったからな。\x02\x03",

            "あの引き際のよさも、\x01",
            "猟兵団ならではだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x101,
        (
            "#00003Fまたいつか出会うことも\x01",
            "あるかもしれないな……\x02\x03",

            "#00001F……だけど今は、\x01",
            "この事件を解決する事に\x01",
            "集中したほうがよさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x8,
        (
            "#12100Fうむ、その通りだ。\x02\x03",

            "最後の戦いに向けて\x01",
            "万全の準備を整えるがいい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 7)
    Return()

    # Function_30_CA1D end

    def Function_31_CD63(): pass

    label("Function_31_CD63")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_CE13")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6E), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD8E")
    Call(1, 52)
    TalkEnd(0xC)
    Return()

    label("loc_CD8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_CE13")

    #C0305
    ChrTalk(
        0xC,
        (
            "#01909Fそのお守り、\x01",
            "大事にしてくださいね～。\x02\x03",

            "皆さんの無事を祈って\x01",
            "作ったものですから、\x01",
            "きっと効き目は抜群ですよ！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xC)
    Return()

    label("loc_CE13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D067")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF32")
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x0, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CEBE")
    Jump("loc_CF08")

    label("loc_CEBE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CEDE")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CF08")

    label("loc_CEDE")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CEFE")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CF08")

    label("loc_CEFE")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CF08")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)
    Jump("loc_CF42")

    label("loc_CF32")

    RunExpression(0xA, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TurnDirection(0xC, 0x0, 0)

    label("loc_CF42")


    #C0306
    ChrTalk(
        0xC,
        (
            "#01900F皆さんは、『ポムっと！』っていう\x01",
            "導力ゲームをご存知ですか～？\x02\x03",

            "#01909Fふふ、実はわたしも始めてみたんです。\x01",
            "よかったらアカウントを交換して下さい～。\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0307
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『フランのアカウント』\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 4)
    OP_E4(0x3)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D059")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D050")
    ClearChrFlags(0xC, 0x10)

    label("loc_D050")

    SetChrSubChip(0xC, 0x0)
    Jump("loc_D062")

    label("loc_D059")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_RESULT, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D062")

    Jump("loc_E6C9")

    label("loc_D067")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_D22E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D082")
    Call(1, 33)
    Jump("loc_D229")

    label("loc_D082")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D19F")

    #C0308
    ChrTalk(
        0xC,
        (
            "#01904F不安に耐えて待つことも、\x01",
            "みなさんと一緒に戦ってるって\x01",
            "ことなんですよね……\x02\x03",

            "#01902Fだったら、\x01",
            "私のやるべき事は一つです。\x02\x03",

            "#01909F不肖、フラン・シーカー……\x01",
            "ここでお姉ちゃんや皆さんの\x01",
            "無事をお祈りしています！\x02\x03",

            "絶対に、絶対に、\x01",
            "無事に帰ってきてくださいね！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_D229")

    label("loc_D19F")


    #C0309
    ChrTalk(
        0xC,
        (
            "#01909F不肖、フラン・シーカー……\x01",
            "ここでお姉ちゃんや皆さんの\x01",
            "無事をお祈りしています！\x02\x03",

            "絶対に、絶対に、\x01",
            "無事に帰ってきてくださいね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D229")

    Jump("loc_E6C9")

    label("loc_D22E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_D3F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D369")

    #C0310
    ChrTalk(
        0xC,
        (
            "#01900F《大樹》の内部が\x01",
            "あんなにキレイだとは\x01",
            "思いもよりませんでしたよ～。\x02\x03",

            "#01904Fこんな時じゃなければ、\x01",
            "いつまでも景色を\x01",
            "楽しんでいたいくらいですね～。\x02\x03",

            "#01905F……っと、いけないいけない。\x01",
            "油断してちゃダメですよね。\x02\x03",

            "#01909Fとにかく、頑張って下さい！\x01",
            "わたしはここで応援してます～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_D3F3")

    label("loc_D369")


    #C0311
    ChrTalk(
        0xC,
        (
            "#01906F《大樹》の内部はキレイですけど、\x01",
            "油断してちゃダメですよね。\x02\x03",

            "#01909Fとにかく、頑張って下さい！\x01",
            "わたしはここで応援してます～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3F3")

    Jump("loc_E6C9")

    label("loc_D3F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D548")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D4CB")

    #C0312
    ChrTalk(
        0xC,
        (
            "#01905Fあの《大樹》に突入していくのは\x01",
            "ちょっと怖いですけど……\x02\x03",

            "#01901F……わたしも警察官です。\x01",
            "こんな時こそ度胸を見せないと\x01",
            "いけませんよね！\x02\x03",

            "#01909Fロイドさん、頑張りましょう！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_D543")

    label("loc_D4CB")


    #C0313
    ChrTalk(
        0xC,
        (
            "#01901F……わたしも警察官です。\x01",
            "こんな時こそ度胸を見せないと\x01",
            "いけませんよね！\x02\x03",

            "#01909Fロイドさん、頑張りましょう！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D543")

    Jump("loc_E6C9")

    label("loc_D548")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_D725")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D677")

    #C0314
    ChrTalk(
        0xC,
        (
            "#01900F結界と白い《神機》さえ\x01",
            "なんとかすれば、市内に侵入する\x01",
            "算段がつけられそうですね～。\x02\x03",

            "#01904F市内にいるセルゲイ課長たちにも\x01",
            "『無効宣言』は届いたでしょうし、\x01",
            "そっちも動き出したかもしれません。\x02\x03",

            "#01909Fとにかく、もうひと頑張りです！\x01",
            "ロイドさんたち、頑張ってください！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_D720")

    label("loc_D677")


    #C0315
    ChrTalk(
        0xC,
        (
            "#01900F結界と白い《神機》さえ\x01",
            "なんとかすれば、市内に侵入する\x01",
            "算段がつけられそうですね～。\x02\x03",

            "#01909Fとにかく、もうひと頑張りです！\x01",
            "ロイドさんたち、頑張ってください！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D720")

    Jump("loc_E6C9")

    label("loc_D725")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_DAD6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DA09")

    #C0316
    ChrTalk(
        0xC,
        (
            "#01904F（カタカタカタカタ……）\x02\x03",

            "あーあー、テステス……\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x101,
        "#00005Fフラン、何してるんだ？\x02",
    )

    CloseMessageWindow()
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x101, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D829")
    Jump("loc_D873")

    label("loc_D829")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D849")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D873")

    label("loc_D849")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D869")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D873")

    label("loc_D869")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D873")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    #C0318
    ChrTalk(
        0xC,
        (
            "#01902Fああ、ロイドさん。\x01",
            "マイクとカメラのテストを\x01",
            "しているんですよ～。\x02\x03",

            "メルカバのモニタシステムから\x01",
            "導力ネットを経由して、各地に\x01",
            "映像と音声を送る予定なんです。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0x0)

    #C0319
    ChrTalk(
        0xC,
        (
            "#01904F『わたしはフラン・シーカーです。\x01",
            "  お姉ちゃんが大好きです！』\x02\x03",

            "#01909F……うん、音声認識は良好ですね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        (
            "#00009F（はは、こんな状況でも\x01",
            "  フランには和まされるなあ……）\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x1, 4)
    Jump("loc_DAD1")

    label("loc_DA09")


    #C0321
    ChrTalk(
        0xC,
        (
            "#01902Fメルカバのモニタシステムから\x01",
            "導力ネットを経由して、各地に\x01",
            "映像と音声を送る予定なんです。\x02\x03",

            "#01909Fマクダエル議長のお声が\x01",
            "市民の皆さんによく聞こえるように、\x01",
            "入念にチェックしないとですね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DAD1")

    Jump("loc_E6C9")

    label("loc_DAD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_DC6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D7, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DAF1")
    Call(1, 13)
    Jump("loc_DC68")

    label("loc_DAF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBFC")

    #C0322
    ChrTalk(
        0xC,
        (
            "#01912Fふふ、お姉ちゃんが戻ってきて\x01",
            "本当にうれしかったです。\x02\x03",

            "#01901Fロイドさん……\x01",
            "お姉ちゃんのこと、\x01",
            "よろしくお願いしますね！\x02\x03",

            "#01909Fわたしも陰ながら\x01",
            "応援させてもらいますから！\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        (
            "#00006F（う、うーん……\x01",
            "  なにか誤解してる気がするなあ。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_DC68")

    label("loc_DBFC")


    #C0324
    ChrTalk(
        0xC,
        (
            "#01901Fお姉ちゃんのこと、\x01",
            "よろしくお願いしますね！\x02\x03",

            "#01909Fわたしも陰ながら\x01",
            "応援させてもらいますから！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DC68")

    Jump("loc_E6C9")

    label("loc_DC6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_DDF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD93")

    #C0325
    ChrTalk(
        0xC,
        (
            "#01908F西クロスベル街道……\x01",
            "ベルガード門があるんですよね。\x02\x03",

            "#01903Fあそこには多分、お姉ちゃんが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    #C0326
    ChrTalk(
        0xC,
        (
            "#01906Fふう、こんなことじゃいけませんね。\x01",
            "わたしもしっかりしないと～。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x101,
        (
            "#00003F（フラン、やっぱり\x01",
            "  ノエルの事は心配だよな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_DDF1")

    label("loc_DD93")


    #C0328
    ChrTalk(
        0xC,
        (
            "#01908Fベルガード門には多分、お姉ちゃんが……\x02\x03",

            "#01906F……今、どうしているんでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DDF1")

    Jump("loc_E6C9")

    label("loc_DDF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_E4E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E322")

    #C0329
    ChrTalk(
        0xC,
        (
            "#01908F……お姉ちゃんは、わたしたちと\x01",
            "対立してしまうことさえも受け入れて、\x01",
            "今の道を選んだんですよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x101,
        (
            "#00001Fああ……正直言って、\x01",
            "並大抵の覚悟じゃないと思う。\x02\x03",

            "#00003Fノエルにあそこまでの\x01",
            "決意をさせたのが何なのか……\x02\x03",

            "#00008F今回の一連の事件だけが\x01",
            "きっかけじゃないような気がするけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xC,
        (
            "#01903F……たぶんですけど……\x02\x03",

            "#01901Fわたしたちが小さい頃に、\x01",
            "お父さんが亡くなったことが\x01",
            "根っこにあるんだと思います。\x02\x03",

            "#01908F……共和国軍の行った演習中の、\x01",
            "ライフルの“誤射”によって。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x101,
        (
            "#00005Fえ……！？\x02\x03",

            "君たちのお父さんは、\x01",
            "１０年ほど前の“事故”で\x01",
            "亡くなったって話じゃ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xC,
        (
            "#01906Fわたしはまだ小さかったので、\x01",
            "詳しくは覚えてないんですけど……\x02\x03",

            "#01908F共和国軍が演習中に誤って発砲して、\x01",
            "それがたまたま警備中のお父さんに……\x01",
            "ということだったらしいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x101,
        "#00003F……そうだったのか……\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xC,
        (
            "#01903Fだけどクロスベルの立場では、\x01",
            "それを大事にすることなんて\x01",
            "当然できなくて……\x02\x03",

            "#01908Fそれで、あくまでただの“事故”として、\x01",
            "処理されてしまったみたいです。\x02\x03",

            "お母さんも悲しんだそうですけど、\x01",
            "もともと危険なお仕事だからって\x01",
            "受け入れるしかなかったみたいで……\x02\x03",

            "#01903F……でも多分、お姉ちゃんはそのことに、\x01",
            "ずっと納得がいってなかったんですよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x101,
        (
            "#00008F……そうかもしれないな。\x02\x03",

            "#00003F（ノエルがクロスベルを守りたいと\x01",
            "  強く願う理由……なんとなく\x01",
            "  分かったような気がするな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DB, 7)
    Jump("loc_E4E1")

    label("loc_E322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E467")

    #C0337
    ChrTalk(
        0xC,
        (
            "#01908F……すみません。\x01",
            "なんだかしんみりしてしまって。\x02\x03",

            "#01903F国防軍の現状に異議を唱えた\x01",
            "元警備隊メンバー……\x02\x03",

            "#01900F今はその人たちと合流するのを\x01",
            "第一に考えないといけませんよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x101,
        (
            "#00003Fああ……そうだな。\x02\x03",

            "#00000Fフラン、バックアップはよろしく頼む。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0xC,
        "#01909Fはい、尽力させていただきます～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_E4E1")

    label("loc_E467")


    #C0340
    ChrTalk(
        0xC,
        (
            "#01903F国防軍の現状に異議を唱えた\x01",
            "元警備隊メンバー……\x02\x03",

            "#01900Fお姉ちゃんじゃないとしたら、\x01",
            "一体誰なんでしょうね～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4E1")

    Jump("loc_E6C9")

    label("loc_E4E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_E6C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E501")
    Call(1, 32)
    Jump("loc_E6C9")

    label("loc_E501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E613")

    #C0341
    ChrTalk(
        0xC,
        (
            "#01900F《隙間》を探すついでに\x01",
            "危険な魔獣の反応も\x01",
            "探知しているみたいですね～。\x02\x03",

            "これからはわたしが責任を持って、\x01",
            "正式な支援要請として\x01",
            "端末に情報を送りますから～。\x02\x03",

            "#01909F魔獣を退治したら、\x01",
            "キャビンにある端末で忘れずに\x01",
            "報告をよろしくお願いしますね～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_E6C9")

    label("loc_E613")


    #C0342
    ChrTalk(
        0xC,
        (
            "#01900Fまだまだ未熟ですけど、\x01",
            "メルカバでのお手伝いは\x01",
            "精一杯やらせていただきます！\x02\x03",

            "#01909Fみなさんも、手配魔獣を退治したら\x01",
            "キャビンにある端末で\x01",
            "報告をよろしくお願いしますね～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E6C9")

    TalkEnd(0xC)
    Return()

    # Function_31_CD63 end

    def Function_32_E6CD(): pass

    label("Function_32_E6CD")


    #C0343
    ChrTalk(
        0xC,
        (
            "#01900Fこのメルカバには、支援課にあったような\x01",
            "報告用の端末が備え付けられていますけど……\x02\x03",

            "#01909Fこれからは、わたしが責任を持って\x01",
            "支援要請の情報を送らせて\x01",
            "いただくことになったんです～！\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x101,
        (
            "#00005Fへえ、そうなのか。\x01",
            "確かにキャビンに\x01",
            "そんな端末があったけど……\x02\x03",

            "#00003Fそういえば、どこからあんな情報が\x01",
            "入ってきてるんだろうな？\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0xC,
        (
            "#01905Fわたしも気になって、\x01",
            "アッバスさんに聞いてみたんですけど……\x02\x03",

            "#01904Fどうやら《隙間》を探すついでに、\x01",
            "危険な魔獣の反応も\x01",
            "探知しているみたいですね～。\x02\x03",

            "#01902Fメルカバが作戦行動をする際の\x01",
            "障害となりうるものを早期に発見して、\x01",
            "対処するための機能、だそうです～。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x101,
        (
            "#00000Fなるほど……\x01",
            "確かに、放っておくのも危険だし\x01",
            "合間に退治しに行ってもいいかもな。\x02\x03",

            "#00009Fでも、フランへの報告か……\x01",
            "久しぶりでなんだか懐かしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0xC,
        (
            "#01909Fふふ、本当ですよね～！\x01",
            "わたしもなんだか感慨深いです～。\x02\x03",

            "#01906Fキャビンの端末から報告するのは\x01",
            "ちょっと手間かもしれませんけど……\x02\x03",

            "#01900Fいずれ警察に戻った時に\x01",
            "正当な評価をしてもらうためにも、\x01",
            "今までどおりの手順でお願いしますね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        (
            "#00004F……ああ、そうだな。\x02\x03",

            "#00000Fそれじゃあ、改めて前みたいに\x01",
            "オペレーターをよろしく頼む、フラン。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xC,
        "#01909Fはいっ、こちらこそ～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 3)
    Return()

    # Function_32_E6CD end

    def Function_33_EB4B(): pass

    label("Function_33_EB4B")


    #C0350
    ChrTalk(
        0xC,
        (
            "#01903F本当の本当に、これが最後の\x01",
            "山場なんですね～……\x02\x03",

            "#01908Fこういう時、安全な場所で\x01",
            "待っていることしかできないのは\x01",
            "やっぱり不甲斐ないです……\x02\x03",

            "#01906Fわたしも皆さんと同じ場所で\x01",
            "戦えたらなって、何度思ったことか。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x101,
        (
            "#00003F……なにも、敵との戦闘だけが\x01",
            "『戦う』ってことじゃないさ。\x02\x03",

            "#00000Fフランや他のみんなが\x01",
            "待っててくれるからこそ、\x01",
            "俺たちは頑張れるんだ。\x02\x03",

            "どんなに辛くても、\x01",
            "絶対にあの場所に帰る……\x01",
            "そう心から思えるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xC,
        (
            "#01900Fロイドさん……\x01",
            "……分かりました。\x02\x03",

            "#01909F不肖、フラン・シーカー……\x01",
            "ここでお姉ちゃんや皆さんの\x01",
            "無事をお祈りしています！\x02\x03",

            "絶対に、絶対に、\x01",
            "無事に帰ってきてくださいね！\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x101,
        "#00002Fああ……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 3)
    Return()

    # Function_33_EB4B end

    def Function_34_EDD0(): pass

    label("Function_34_EDD0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF08")

    #C0354
    ChrTalk(
        0x9,
        (
            "#02305Fそういえばアンタら……\x01",
            "『ポムっと！』のアカウントを\x01",
            "持ってるんだって？\x02\x03",

            "#02304Fフフン、折角だからこのヨナ様の\x01",
            "アカウントをプレゼントしてやるぜ。\x02\x03",

            "#02309F開発段階から関わってたオレに\x01",
            "勝てるもんなら勝ってみろよな～。\x02",
        )
    )

    CloseMessageWindow()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0355
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『ヨナのアカウント』\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x27, 7)
    OP_E4(0x3)
    Jump("loc_F748")

    label("loc_EF08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_F08C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF23")
    Call(1, 36)
    Jump("loc_F087")

    label("loc_EF23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F007")

    #C0356
    ChrTalk(
        0x9,
        (
            "#02306Fちぇっ、なんだよ。\x01",
            "人がせっかく心配してやってる\x01",
            "っつーのによ……\x02\x03",

            "#02300Fフン、まあ……\x01",
            "せいぜい頑張ってこいよ。\x02\x03",

            "#02309Fさっさとボクに、前みたいな\x01",
            "ダラけた導力ネットライフを\x01",
            "取り戻させてくれよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_F087")

    label("loc_F007")


    #C0357
    ChrTalk(
        0x9,
        (
            "#02300Fまあ、せいぜい頑張ってこいよ。\x02\x03",

            "#02309Fさっさとボクに、前みたいな\x01",
            "ダラけた導力ネットライフを\x01",
            "取り戻させてくれよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F087")

    Jump("loc_F748")

    label("loc_F08C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_F254")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F1CF")

    #C0358
    ChrTalk(
        0x9,
        (
            "#02301Fあの無数の光が\x01",
            "樹に吸い込まれていくカンジ……\x01",
            "導力ネットの概念イメージっぽいぜ。\x02\x03",

            "#02303F考えてみりゃ、クロイス家の奴らって\x01",
            "導力ネットも陰謀に利用してたんだよな。\x02\x03",

            "あの《大樹》の姿自体が、\x01",
            "奴らの『計画』に関係があったりして。\x02\x03",

            "#02302F……ま、その辺の分析は\x01",
            "アンタたちにお任せするぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_F24F")

    label("loc_F1CF")


    #C0359
    ChrTalk(
        0x9,
        (
            "#02303Fあの《大樹》の姿自体が、\x01",
            "奴らの『計画』に関係があるのかもな。\x02\x03",

            "#02302Fま、その辺の分析は\x01",
            "アンタたちにお任せするぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F24F")

    Jump("loc_F748")

    label("loc_F254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_F39E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F325")

    #C0360
    ChrTalk(
        0x9,
        (
            "#02303Fボクはジオフロントのベースに\x01",
            "戻ってもよかったんだけど……\x02\x03",

            "#02302F今はこっちの方が面白そうだし、\x01",
            "せっかくだから最後まで\x01",
            "付き合ってやるぜ。\x02\x03",

            "#02304Fへへっ、感謝しろよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_F399")

    label("loc_F325")


    #C0361
    ChrTalk(
        0x9,
        (
            "#02302F今はこっちの方が面白そうだし、\x01",
            "せっかくだから最後まで\x01",
            "付き合ってやるぜ。\x02\x03",

            "#02304Fへへっ、感謝しろよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F399")

    Jump("loc_F748")

    label("loc_F39E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_F5A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F50C")

    #C0362
    ChrTalk(
        0x9,
        (
            "#02302F導力ネットへのハッキングは\x01",
            "思った以上に上手くいったぜ。\x02\x03",

            "#02306Fただ、無線ブースターからの経路は\x01",
            "完全に遮断されちまったから、\x01",
            "もう一度やるのはムリだろうな。\x02\x03",

            "#02309F……へへ、まあいいや。\x01",
            "とりあえずタワーのヤツらには\x01",
            "一泡吹かせてやれただろうし。\x02\x03",

            "#02302Fあとはとっとと\x01",
            "クロスベル市を解放して、\x01",
            "ボクのベースを取り返さないとな！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_F5A2")

    label("loc_F50C")


    #C0363
    ChrTalk(
        0x9,
        (
            "#02300Fなんだか強い相手がいるみたいだけど、\x01",
            "そっちはよろしく頼んだぜ。\x02\x03",

            "#02309Fとっととクロスベル市を解放して、\x01",
            "ボクのベースを取り返さないとな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F5A2")

    Jump("loc_F748")

    label("loc_F5A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_F748")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5C2")
    Call(1, 35)
    Jump("loc_F748")

    label("loc_F5C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6BC")

    #C0364
    ChrTalk(
        0x9,
        (
            "#02306Fとにかく、ボクを端末もない場所に\x01",
            "押し込んでくれやがった奴らに、\x01",
            "バッチリ借りを返してやらなくちゃな。\x02\x03",

            "#02310F特にあのマリアベルとかいう女！\x01",
            "あのアクマに思い知らせてやるぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x101,
        "#00006F（相当な私怨があるみたいだな……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_F748")

    label("loc_F6BC")


    #C0366
    ChrTalk(
        0x9,
        (
            "#02302Fこっちはいつでもハッキングを\x01",
            "開始できる準備が整ってるぜ～！\x02\x03",

            "#02309F見てろよ、クロスベル中の端末に\x01",
            "無効宣言を届けてやるからさ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F748")

    TalkEnd(0xFE)
    Return()

    # Function_34_EDD0 end

    def Function_35_F74C(): pass

    label("Function_35_F74C")


    #C0367
    ChrTalk(
        0x9,
        (
            "#02305Fよー、まだ作戦を始めねーの？\x02\x03",

            "こっちはいつでもハッキングを\x01",
            "開始できる準備が整ってるぜ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x101,
        "#00006Fなんだかノリノリだなあ……\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x9,
        (
            "#02304Fヘヘ、ボクをネット環境のない所に\x01",
            "押し込んでくれやがった奴らに、\x01",
            "ようやく借りを返してやれるからな。\x02\x03",

            "#02302F見てろよ、クロスベル中の端末に\x01",
            "あの議長のオッサンの顔と声を\x01",
            "バッチリ届けてやるからさ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0370
    ChrTalk(
        0x101,
        (
            "#00003Fマクダエル議長、だろ。\x02\x03",

            "#00001Fヨナ、こういうときでも\x01",
            "礼儀くらいはちゃんと\x01",
            "しないとだめだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x9,
        (
            "#02306Fあーもう、アンタは\x01",
            "相変わらずウルセーなあ。\x02\x03",

            "#02302Fいいからとっとと作戦を\x01",
            "開始してくれよな！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 6)
    Return()

    # Function_35_F74C end

    def Function_36_F99A(): pass

    label("Function_36_F99A")


    #C0372
    ChrTalk(
        0x9,
        (
            "#02300Fなんだか、ついにラストが\x01",
            "近づいてるみてーだな。\x02\x03",

            "#02303F……その、大丈夫なのか？\x01",
            "あのマリアベルとかいう女が\x01",
            "待ってるみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x101,
        (
            "#00005Fへえ、珍しいな……\x01",
            "俺たちを心配してくれるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x9,
        (
            "#02305Fあ、あたりめーじゃん！\x01",
            "こんなトンでもねー状況なら\x01",
            "誰だって心配するっつーの！\x02\x03",

            "#02306Fちぇっ、なんだよ。\x01",
            "人がせっかく……\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x101,
        (
            "#00009Fはは、ゴメンゴメン。\x02\x03",

            "#00000F……ありがとう、ヨナ。\x01",
            "俺たちはきっと無事に戻るよ。\x02\x03",

            "いつでも外に離脱できるように\x01",
            "しっかり準備を頼んだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x9,
        (
            "#02303Fフン、分かってるっつの。\x01",
            "せいぜい頑張ってこいよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 6)
    Return()

    # Function_36_F99A end

    def Function_37_FBC0(): pass

    label("Function_37_FBC0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_FBD1")
    Jump("loc_100B5")

    label("loc_FBD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_FBDF")
    Jump("loc_100B5")

    label("loc_FBDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_FBED")
    Jump("loc_100B5")

    label("loc_FBED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_FD70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FD02")

    #C0377
    ChrTalk(
        0xF,
        (
            "#02103F謎の結社《身喰らう蛇#10Rウ ロ ボ ロ ス#》……\x01",
            "リベールで起こった異変でも\x01",
            "暗躍してたって話よね。\x02\x03",

            "#02101F今回の事件ではあまり前には\x01",
            "出てきてなかったけど、\x01",
            "重要な場所はキッチリと守ってるし……\x02\x03",

            "#02106F……一体、彼らの目的は何なのかしらね？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_FD6B")

    label("loc_FD02")


    #C0378
    ChrTalk(
        0xF,
        (
            "#02103F結社《身喰らう蛇》……\x02\x03",

            "#02101F謎ばかりが膨らんでいくけど、\x01",
            "彼らの真の目的は何なのかしらね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FD6B")

    Jump("loc_100B5")

    label("loc_FD70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_FF13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE63")

    #C0379
    ChrTalk(
        0xF,
        (
            "#02102F『無効宣言』の段取りも\x01",
            "ようやく固まったわ。\x02\x03",

            "マクダエル議長にも\x01",
            "宣言の声明文を作っていただいたし、\x01",
            "あとは実行に移すだけ……\x02\x03",

            "#02106F……う～、なんだか緊張してきた～！\x01",
            "甲板で発声練習でもしてこようかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_FF0E")

    label("loc_FE63")


    #C0380
    ChrTalk(
        0xF,
        (
            "#02102Fマクダエル議長にも\x01",
            "宣言の声明文を作っていただいたし、\x01",
            "あとは実行に移すだけ……\x02\x03",

            "#02106F……う～、なんだか緊張してきた～！\x01",
            "甲板で発声練習でもしてこようかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FF0E")

    Jump("loc_100B5")

    label("loc_FF13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_100B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF2E")
    Call(1, 38)
    Jump("loc_100B5")

    label("loc_FF2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10054")

    #C0381
    ChrTalk(
        0xF,
        (
            "#02109Fさ～て、ワジ君にリーシャさん。\x01",
            "インタビューを続行するわよ～！\x02\x03",

            "あたしが気になるってだけだし、\x01",
            "もちろん記事にはしないから\x01",
            "安心して色々話してちょうだい！\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xD,
        "#10706Fは、はあ……\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0xA,
        (
            "#10409Fやれやれ、\x01",
            "とんだゴシップ好きだねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x101,
        "#00006F（だ、大丈夫かなあ……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_100B5")

    label("loc_10054")


    #C0385
    ChrTalk(
        0xF,
        (
            "#02105F……へ～、そうなんだ～！\x02\x03",

            "#02109Fいや～、そういう裏話って\x01",
            "あたしの大好物なのよね～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_100B5")

    TalkEnd(0xFE)
    Return()

    # Function_37_FBC0 end

    def Function_38_100B9(): pass

    label("Function_38_100B9")


    #C0386
    ChrTalk(
        0xF,
        (
            "#02104Fこんなすごい飛行艇で、\x01",
            "こんなすごいメンツに\x01",
            "インタビューできるなんて……\x02\x03",

            "#02109Fああっ、ジャーナリスト魂が\x01",
            "くすぐられちゃうわね～！\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x101,
        (
            "#00006Fグ、グレイスさん……\x01",
            "記事にはしないんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0xF,
        (
            "#02102Fやだなあ、心配しないでってば。\x01",
            "あくまで好奇心ってやつだから。\x02\x03",

            "#02104Fレジスタンスについてってる時に\x01",
            "掴んだネタもまとめなきゃいけないし、\x01",
            "記事にはしないから安心してよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0x101,
        (
            "#00006Fは、はあ……\x02\x03",

            "#00005F……そういえばグレイスさんが\x01",
            "レジスタンスに押しかけた経緯#4Rいきさつ#って……？\x02\x03",

            "#00003F確か、クロスベル市で何か問題を\x01",
            "起こしたとか言ってましたっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xF,
        (
            "#02106Fん～、まあねえ。\x01",
            "ちょっと話は長くなるんだけど……\x02\x03",

            "#02101F……実は、あの独立宣言の日から\x01",
            "ウチの記事に政府の検閲が\x01",
            "入るようになっちゃってね。\x02\x03",

            "大統領を批判するような\x01",
            "反対派のインタビュー記事なんかは\x01",
            "絶対に書けなくなっちゃったし……\x02\x03",

            "#02106Fはては、通信器の使用や\x01",
            "取材行為そのものまでが\x01",
            "規制されちゃったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x101,
        (
            "#00001F徹底されてますね……\x02\x03",

            "#00003F……いや、ディーター大統領なら\x01",
            "やりかねないのかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0xF,
        (
            "#02103Fまあ、そんなのはあたしの求める\x01",
            "ジャーナリズムからかけ離れてるし、\x01",
            "さすがに納得いかなくてね。\x02\x03",

            "#02102F通告を無視して取材を続けてたら、\x01",
            "ついに国防軍に目をつけられちゃって。\x02\x03",

            "#02104Fいよいよクロスベル市に居辛くなって、\x01",
            "レジスタンスに流れ着いたってワケ。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x101,
        (
            "#00000Fそうだったんですか……\x01",
            "よくご無事でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0xF,
        (
            "#02109Fそれが、レインズ君が機転を利かして\x01",
            "脱出ルートを手配してくれてさ～。\x01",
            "いい後輩を持って幸せだわ。\x02\x03",

            "#02100F……とにかく、こうなったからには\x01",
            "あたしもあたしなりに、\x01",
            "クロスベル市の解放に協力するからね！\x02\x03",

            "#02109F『ペンは剣よりも強し』って言うし、\x01",
            "国防軍や猟兵には負けないんだから！\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x101,
        (
            "#00012Fはは……協力してもらえることが\x01",
            "あるかもしれませんし、\x01",
            "その時はよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D9, 7)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x10)
    Return()

    # Function_38_100B9 end

    def Function_39_10764(): pass

    label("Function_39_10764")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_10946")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10782")
    Call(1, 41)
    Jump("loc_10941")

    label("loc_10782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1088B")

    #C0396
    ChrTalk(
        0x12,
        (
            "#02503Fこれ以上、私が君たちの\x01",
            "お役に立てる事はないだろうが……\x02\x03",

            "#02500Fせめて、無効宣言を出した者として\x01",
            "クロスベルの未来に与える影響、\x01",
            "その対策を考え続けているとしよう。\x02\x03",

            "自治州議会の長として……\x01",
            "何より、クロスベルに住む\x01",
            "１人の住民としてね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_10941")

    label("loc_1088B")


    #C0397
    ChrTalk(
        0x12,
        (
            "#02503F無効宣言を出した者として\x01",
            "クロスベルの未来に与える影響、\x01",
            "その対策を考え続けているとしよう。\x02\x03",

            "#02500F自治州議会の長として……\x01",
            "何より、クロスベルに住む\x01",
            "１人の住民としてね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10941")

    Jump("loc_10B7B")

    label("loc_10946")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_10B7B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10961")
    Call(1, 40)
    Jump("loc_10B7B")

    label("loc_10961")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10AD0")

    #C0398
    ChrTalk(
        0x12,
        (
            "#02500F私の方は、いつでも\x01",
            "『独立国の無効宣言』を\x01",
            "出す準備が整っている。\x02\x03",

            "#02503F後は、クロスベルの住民たちに\x01",
            "この宣言がどう届くか……\x01",
            "それに懸かっているだろう。\x02\x03",

            "#02500Fディーター君ほどの\x01",
            "パフォーマンスは出来ないが、\x01",
            "私なりに懸命に伝えてみせるつもりだ。\x02\x03",

            "クロスベルに住む一人一人に\x01",
            "この地の未来を考えてもらう為にも、\x01",
            "必ずやり遂げねばなるまい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_10B7B")

    label("loc_10AD0")


    #C0399
    ChrTalk(
        0x12,
        (
            "#02503F『独立国の無効宣言』……\x01",
            "私なりに懸命に伝えてみせるつもりだ。\x02\x03",

            "#02500Fクロスベルに住む一人一人に\x01",
            "この地の未来を考えてもらう為にも、\x01",
            "必ずやり遂げねばなるまい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10B7B")

    TalkEnd(0xFE)
    Return()

    # Function_39_10764 end

    def Function_40_10B7F(): pass

    label("Function_40_10B7F")


    #C0400
    ChrTalk(
        0x101,
        (
            "#00000Fマクダエル議長……\x01",
            "そちらの準備はいかがですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x12,
        (
            "#02500Fうむ、いつでも\x01",
            "『独立国の無効宣言』を\x01",
            "出す準備が整っている。\x02\x03",

            "宣言の内容も、申し分のない\x01",
            "ものを作ったつもりだ。\x02\x03",

            "#02503F無論、例のディーター君の言葉を\x01",
            "反映した上でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x101,
        "#00003F……ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x12,
        (
            "#02503Fいや……礼には及ばない。\x02\x03",

            "#02501F後は、クロスベルの住民たちに\x01",
            "この宣言がどう届くか……\x01",
            "それに懸かっているはずだ。\x02\x03",

            "私にはディーター君ほどの\x01",
            "パフォーマンスは出来ないが、\x01",
            "一言一句を懸命に伝えてみせよう。\x02\x03",

            "#02503Fクロスベルに住む一人一人に\x01",
            "この地の未来を考えてもらう為にも、\x01",
            "必ずやり遂げねばなるまい。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x101,
        "#00000Fええ……よろしくお願いします。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 1)
    Return()

    # Function_40_10B7F end

    def Function_41_10DFC(): pass

    label("Function_41_10DFC")


    #C0405
    ChrTalk(
        0x12,
        "#02503F………………………………\x02",
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x101,
        "#00005Fマクダエル議長……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x12, 0x10)
    TurnDirection(0x12, 0x101, 0)
    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_10EE8")
    Jump("loc_10F32")

    label("loc_10EE8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_10F08")
    OP_52(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10F32")

    label("loc_10F08")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10F28")
    OP_52(0x12, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10F32")

    label("loc_10F28")

    OP_52(0x12, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x12, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10F32")

    OP_52(0x12, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x10)

    #C0407
    ChrTalk(
        0x12,
        (
            "#02505F……ああ、すまない。\x01",
            "少し考え事をしていてね。\x02\x03",

            "#02503Fクロスベル独立国の無効宣言……\x01",
            "現状を打開する為とはいえ、\x01",
            "本当にこれが正しかったのかとね。\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x101,
        "#00008F…………………………\x02",
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x12,
        (
            "#02503F……おそらくこの問題に\x01",
            "正しい答えというものはないのだろう。\x02\x03",

            "#02500Fだが、正しい答えを求める事こそが\x01",
            "大事なことだと思うのだ。\x02\x03",

            "自治州議会の長として……\x01",
            "何より、クロスベルに住む\x01",
            "１人の住民としてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x101,
        (
            "#00003F……ありがとうございます。\x02\x03",

            "#00000F事件にひと段落ついたら、\x01",
            "きっと俺たちも議長を\x01",
            "お手伝いさせて頂きます。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x12,
        (
            "#02509Fフフ、それはありがたい。\x01",
            "その時はどうかよろしくお願いしよう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x1DA, 2)
    Return()

    # Function_41_10DFC end

    def Function_42_111B4(): pass

    label("Function_42_111B4")

    Call(1, 43)
    Return()

    # Function_42_111B4 end

    def Function_43_111B8(): pass

    label("Function_43_111B8")

    TalkBegin(0x15)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_111C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_121FC")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "装備品を買う\x01",      # 1
            "消耗品を買う\x01",      # 2
            "やめる\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11230")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_11230")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_112B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1124F")
    OP_AF(0xD8)
    Jump("loc_112A1")

    label("loc_1124F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_1125F")
    OP_AF(0xD7)
    Jump("loc_112A1")

    label("loc_1125F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_1126F")
    OP_AF(0xD6)
    Jump("loc_112A1")

    label("loc_1126F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_1127F")
    OP_AF(0xD5)
    Jump("loc_112A1")

    label("loc_1127F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_1128F")
    OP_AF(0xD4)
    Jump("loc_112A1")

    label("loc_1128F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1129F")
    OP_AF(0xD3)
    Jump("loc_112A1")

    label("loc_1129F")

    OP_AF(0xD2)

    label("loc_112A1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_121F7")

    label("loc_112B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_112D0")
    OP_AF(0xDC)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_121F7")

    label("loc_112D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_112E4")
    Jump("loc_121F7")

    label("loc_112E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_121F7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_11491")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1141A")

    #C0412
    ChrTalk(
        0x15,
        (
            "クロスベルの因果を巡る戦いに\x01",
            "ようやく決着が付く時が来たんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x15,
        (
            "最初は教会の人員も集まらなくて\x01",
            "どうなる事かと思ったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x15,
        (
            "何とかしてここまで辿りついたんだ。\x01",
            "君たちなら絶対に大丈夫さ。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x15,
        (
            "さあ、最後に向けて\x01",
            "しっかり準備を整えていってくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_1148C")

    label("loc_1141A")


    #C0416
    ChrTalk(
        0x15,
        (
            "ここまで辿りついたんだ。\x01",
            "君たちなら絶対に大丈夫さ。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x15,
        (
            "さあ、最後に向けて\x01",
            "しっかり準備を整えていってくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1148C")

    Jump("loc_121F7")

    label("loc_11491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_115E6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11565")

    #C0418
    ChrTalk(
        0x15,
        (
            "《大樹》の道はかなり深い所まで\x01",
            "続いているみたいだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x15,
        (
            "危なくなったら、\x01",
            "ときどき補給に戻るのも大事だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x15,
        (
            "事件の解決は君たちにかかってる。\x01",
            "できるだけ慎重に進むようにね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_115E1")

    label("loc_11565")


    #C0421
    ChrTalk(
        0x15,
        (
            "危なくなったら、\x01",
            "ときどき補給に戻るのも大事だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x15,
        (
            "事件の解決は君たちにかかってる。\x01",
            "できるだけ慎重に進むようにね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_115E1")

    Jump("loc_121F7")

    label("loc_115E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_117C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11714")

    #C0423
    ChrTalk(
        0x15,
        (
            "《大樹》に向かう前に\x01",
            "あらゆる準備を済ませておきたいけど、\x01",
            "ここで揃えられるものには限界がある。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x15,
        (
            "一旦クロスベルの各地に下りて\x01",
            "色々な施設を訪ねてたり、親しい人に\x01",
            "挨拶をしてくるのもアリじゃないかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x15,
        (
            "何が起こるか分からないし……\x01",
            "悔いのないようにしておかないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_117C3")

    label("loc_11714")


    #C0426
    ChrTalk(
        0x15,
        (
            "一旦クロスベルの各地に下りて\x01",
            "色々な施設を訪ねてたり、親しい人に\x01",
            "挨拶をしてくるのもアリじゃないかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x15,
        (
            "何が起こるか分からないし……\x01",
            "悔いのないようにしておかないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_117C3")

    Jump("loc_121F7")

    label("loc_117C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_11944")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_118B6")

    #C0428
    ChrTalk(
        0x15,
        (
            "ヨルグ・ローゼンベルク……\x01",
            "《結社》の人間が僕たちに\x01",
            "有益な情報をくれるとはね。\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x15,
        (
            "星杯騎士としては\x01",
            "簡単に信じていいか疑問だけど、\x01",
            "情報に嘘はなさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x15,
        (
            "きっと結社にも色々な人間が\x01",
            "いるんだろうな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_1193F")

    label("loc_118B6")


    #C0431
    ChrTalk(
        0x15,
        (
            "ヨルグ・ローゼンベルク……\x01",
            "簡単に信じていいか疑問だけど、\x01",
            "情報に嘘はなさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x15,
        (
            "きっと結社にも色々な人間が\x01",
            "いるんだろうな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1193F")

    Jump("loc_121F7")

    label("loc_11944")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_11AB5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A2A")

    #C0433
    ChrTalk(
        0x15,
        (
            "マクダエル議長によって\x01",
            "独立国の無効が宣言されれば、\x01",
            "クロスベル各地に影響が現れるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x15,
        (
            "各地に潜伏しているレジスタンスも\x01",
            "かなり動きやすくなると思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x15,
        "……山場が近づいて来た気がするね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_11AB0")

    label("loc_11A2A")


    #C0436
    ChrTalk(
        0x15,
        (
            "マクダエル議長によって\x01",
            "独立国の無効が宣言されれば、\x01",
            "クロスベル各地に影響が現れるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x15,
        "……山場が近づいて来た気がするね。\x02",
    )

    CloseMessageWindow()

    label("loc_11AB0")

    Jump("loc_121F7")

    label("loc_11AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_11C3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11BAF")

    #C0438
    ChrTalk(
        0x15,
        (
            "マクダエル議長の救出作戦……\x01",
            "自分が出撃するわけでもないのに\x01",
            "かなり緊張してきたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x15,
        (
            "相手は《赤い星座》の一個中隊……\x01",
            "これまでに比べても厳しい戦いが\x01",
            "待っているはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x15,
        (
            "君たち、どうか\x01",
            "無事に戻ってきてくれよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_11C36")

    label("loc_11BAF")


    #C0441
    ChrTalk(
        0x15,
        (
            "相手は《赤い星座》の一個中隊……\x01",
            "これまでに比べても厳しい戦いが\x01",
            "待っているはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x15,
        (
            "君たち、どうか\x01",
            "無事に戻ってきてくれよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11C36")

    Jump("loc_121F7")

    label("loc_11C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_11D96")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11D14")

    #C0443
    ChrTalk(
        0x15,
        (
            "メルカバ内部も随分と\x01",
            "賑やかになってきたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x15,
        (
            "普段なら騎士団関係者くらいで、\x01",
            "世俗の人間が入ること自体が\x01",
            "珍しいことだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x15,
        (
            "ここだけの話、こういうのも\x01",
            "案外悪くないと思えるよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_11D91")

    label("loc_11D14")


    #C0446
    ChrTalk(
        0x15,
        (
            "メルカバ内部に\x01",
            "世俗の人間が入ること自体が\x01",
            "珍しいことだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x15,
        (
            "ここだけの話、こういうのも\x01",
            "案外悪くないと思えるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D91")

    Jump("loc_121F7")

    label("loc_11D96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_11EFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E98")

    #C0448
    ChrTalk(
        0x15,
        (
            "伝説の凶手《銀》……\x01",
            "その噂は僕も聞いたことがあるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x15,
        (
            "しかし、それが\x01",
            "あんな少女だったとは……\x01",
            "世の中分からないものだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0450
    ChrTalk(
        0x15,
        (
            "……まあ、君たちにとっては\x01",
            "ヘミスフィア卿が聖職者というのも、\x01",
            "かなりの衝撃だったとは思うけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_11EF7")

    label("loc_11E98")


    #C0451
    ChrTalk(
        0x15,
        (
            "伝説の凶手《銀》……\x01",
            "それがあんな少女だったとはね。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x15,
        "はは、世の中分からないものだよ。\x02",
    )

    CloseMessageWindow()

    label("loc_11EF7")

    Jump("loc_121F7")

    label("loc_11EFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_12069")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11FAE")

    #C0453
    ChrTalk(
        0x15,
        (
            "仲間と合流できたか……\x01",
            "どうやら出だしは上々のようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x15,
        (
            "とはいえ、準備を整えておくに\x01",
            "越したことはないからね。\x01",
            "この先も気をつけていってくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_12064")

    label("loc_11FAE")


    #C0455
    ChrTalk(
        0x15,
        (
            "ヘミスフィア卿の法術のおかげで\x01",
            "しばらくは国防軍とも接触せずに\x01",
            "病院に出入りできるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x15,
        (
            "ただ、出だしがいいからと言って\x01",
            "油断は禁物だからね。\x01",
            "この先も気をつけていってくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12064")

    Jump("loc_121F7")

    label("loc_12069")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_121F7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12084")
    Call(1, 44)
    Jump("loc_121F7")

    label("loc_12084")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1217A")

    #C0457
    ChrTalk(
        0x15,
        (
            "ともかく、装備や備品は\x01",
            "沢山調達してきたから、\x01",
            "必要な場合は声を掛けてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x15,
        (
            "……ふう、それにしても\x01",
            "ヘミスフィア卿には\x01",
            "昔から振り回されっぱなしさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x15,
        (
            "僕たちのいない間、\x01",
            "アッバスさんは本当によく\x01",
            "ついていったと思うよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_121F7")

    label("loc_1217A")


    #C0460
    ChrTalk(
        0x15,
        (
            "ヘミスフィア卿には\x01",
            "昔から振り回されっぱなしさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x15,
        (
            "僕たちのいない間、\x01",
            "アッバスさんは本当によく\x01",
            "ついていったと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_121F7")

    Jump("loc_111C5")

    label("loc_121FC")

    TalkEnd(0x15)
    Return()

    # Function_43_111B8 end

    def Function_44_12200(): pass

    label("Function_44_12200")


    #C0462
    ChrTalk(
        0x15,
        (
            "僕は従騎士のヴェントス。\x01",
            "艦内設備の管理を\x01",
            "一任されてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x15,
        (
            "作戦前に装備や備品を\x01",
            "沢山調達してきたから、\x01",
            "必要な場合は声を掛けてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x101,
        (
            "#00005F一任って……\x01",
            "人手も足りないのに、\x01",
            "結構大変そうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x15,
        (
            "まあ、今回ヘミスフィア卿が\x01",
            "急に活動を再開されたからねえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x15,
        (
            "艦内の人員も最低限しか\x01",
            "揃えられなかったんだよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x15, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xA, 0x10)
    TurnDirection(0xA, 0x15, 0)
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_123DA")
    Jump("loc_12424")

    label("loc_123DA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_123FA")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12424")

    label("loc_123FA")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1241A")
    OP_52(0xA, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12424")

    label("loc_1241A")

    OP_52(0xA, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xA, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12424")

    OP_52(0xA, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x15, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x10)

    #C0467
    ChrTalk(
        0xA,
        (
            "#10404Fフフ、なにせ\x01",
            "緊急を要する事態だったからね。\x02\x03",

            "#10409Fヴェントスたちとも２年ぶりだけど、\x01",
            "またしばらくはよろしく頼むよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x15,
        "……ふう、とにかく頑張らないとね。\x02",
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x101,
        (
            "#00006F（うーん、色々と\x01",
            "  苦労させられてそうだな……）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    SetScenarioFlags(0x1DA, 3)
    Return()

    # Function_44_12200 end

    def Function_45_12537(): pass

    label("Function_45_12537")

    Call(1, 46)
    Return()

    # Function_45_12537 end

    def Function_46_1253B(): pass

    label("Function_46_1253B")

    TalkBegin(0x16)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12548")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1345D")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",            # 0
            "改造・合成する\x01",      # 1
            "やめる\x01",              # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_125A8")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_125A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_125C8")
    OP_AF(0xDD)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13458")

    label("loc_125C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_125DC")
    Jump("loc_13458")

    label("loc_125DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13458")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_12768")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_126D6")

    #C0470
    ChrTalk(
        0x16,
        (
            "ここまで来たら、もはや自分に\x01",
            "言える事はありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x16,
        (
            "立ちはだかる敵は強大ですが、\x01",
            "空の女神がきっと皆さんを\x01",
            "導いてくださるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x16,
        (
            "どうか、お気をつけて。\x01",
            "女神の加護がありますよう……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_12763")

    label("loc_126D6")


    #C0473
    ChrTalk(
        0x16,
        (
            "立ちはだかる敵は強大ですが、\x01",
            "空の女神がきっと皆さんを\x01",
            "導いてくださるでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x16,
        (
            "どうか、お気をつけて。\x01",
            "女神の加護がありますよう……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12763")

    Jump("loc_13458")

    label("loc_12768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_1292C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1287B")

    #C0475
    ChrTalk(
        0x16,
        (
            "《零の至宝》……\x01",
            "あんな空間を生み出すとは、\x01",
            "まさに女神の所業です。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x16,
        (
            "……ここまで同行しましたし、\x01",
            "この艦の命運は皆さんに\x01",
            "預けさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x16,
        (
            "自分は大した事は出来ませんが、\x01",
            "オーブメントの準備が必要なら\x01",
            "いつでも声を掛けてください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_12927")

    label("loc_1287B")


    #C0478
    ChrTalk(
        0x16,
        (
            "ここまで同行しましたし、\x01",
            "この艦の命運は皆さんに\x01",
            "預けさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x16,
        (
            "自分は大した事は出来ませんが、\x01",
            "オーブメントの準備が必要なら\x01",
            "いつでも声を掛けてください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12927")

    Jump("loc_13458")

    label("loc_1292C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_12A16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_129D4")

    #C0480
    ChrTalk(
        0x16,
        (
            "……艦内の緊張感が\x01",
            "クロスベル市解放作戦の時より\x01",
            "さらに増したのを感じます。\x02",
        )
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x16,
        (
            "いよいよ訪れた最終局面……\x01",
            "女神の加護を祈るばかりです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_12A11")

    label("loc_129D4")


    #C0482
    ChrTalk(
        0x16,
        (
            "いよいよ訪れた最終局面……\x01",
            "女神の加護を祈るばかりです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A11")

    Jump("loc_13458")

    label("loc_12A16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_12BCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B25")

    #C0483
    ChrTalk(
        0x16,
        (
            "現在、無効宣言を受けて\x01",
            "クロスベル外にいる伍号機とも\x01",
            "連絡をとりあっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x16,
        (
            "クロスベル市解放に向けて、\x01",
            "グラハム卿たちも色々と\x01",
            "準備を進めているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x16,
        (
            "彼らの助力を得るためにも、\x01",
            "白い《神機》と《結界》は\x01",
            "何とかしたい所ですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_12BC7")

    label("loc_12B25")


    #C0486
    ChrTalk(
        0x16,
        (
            "クロスベル市解放に向けて、\x01",
            "グラハム卿たちも色々と\x01",
            "準備を進めているようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x16,
        (
            "彼らの助力を得るためにも、\x01",
            "白い《神機》と《結界》は\x01",
            "何とかしたい所ですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12BC7")

    Jump("loc_13458")

    label("loc_12BCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_12D62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12CC4")

    #C0488
    ChrTalk(
        0x16,
        (
            "ハッキングの際には、\x01",
            "自分もそこの端末から\x01",
            "お手伝いさせてもらいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0489
    ChrTalk(
        0x16,
        (
            "導力ネットは専門外なので\x01",
            "メルカバのシステム面でしか\x01",
            "力にはなれませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x16,
        (
            "騎士団としての使命のためにも、\x01",
            "全力を尽くさせていただきます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_12D5D")

    label("loc_12CC4")


    #C0491
    ChrTalk(
        0x16,
        (
            "自分は導力ネットは専門外なので\x01",
            "メルカバのシステム面でしか\x01",
            "力にはなれませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x16,
        (
            "騎士団としての使命のためにも、\x01",
            "全力を尽くさせていただきます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12D5D")

    Jump("loc_13458")

    label("loc_12D62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_12EAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E1A")

    #C0493
    ChrTalk(
        0x16,
        (
            "ミシュラムに国防軍の部隊は\x01",
            "いないようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x16,
        (
            "猟兵だけでも危険なことに\x01",
            "変わりはありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x16,
        (
            "オーブメントの準備も\x01",
            "万全にしていってください。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_12EA7")

    label("loc_12E1A")


    #C0496
    ChrTalk(
        0x16,
        (
            "ミシュラムに国防軍の部隊は\x01",
            "いないようですが、猟兵だけでも\x01",
            "危険に変わりありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x16,
        (
            "オーブメントの準備も\x01",
            "万全にしていってください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12EA7")

    Jump("loc_13458")

    label("loc_12EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_1307D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12FC8")

    #C0498
    ChrTalk(
        0x16,
        (
            "ランディさんの持っている\x01",
            "《ベルゼルガー》というライフル……\x01",
            "相当な火力を秘めているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x16,
        (
            "大陸最強の猟兵団の一つである\x01",
            "《赤い星座》を相手に立ち回るなんて\x01",
            "相当に厳しいはずですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x16,
        (
            "あの武器をみると、なんだか\x01",
            "納得がいってしまいましたよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_13078")

    label("loc_12FC8")


    #C0501
    ChrTalk(
        0x16,
        (
            "ランディさんの持っている\x01",
            "《ベルゼルガー》というライフル……\x01",
            "相当な火力を秘めているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x16,
        (
            "《赤い星座》を\x01",
            "相手に立ち回ったというのも\x01",
            "納得がいってしまいましたよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13078")

    Jump("loc_13458")

    label("loc_1307D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_13244")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_131AA")

    #C0503
    ChrTalk(
        0x16,
        (
            "国防軍という大組織に逆らって\x01",
            "抵抗活動をするというのは、\x01",
            "相当な信念が必要になるはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x16,
        (
            "満足な補給もできないでしょうし、\x01",
            "曲がりなりにも仲間を\x01",
            "裏切ってしまう行為なのですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x16,
        (
            "どんな方がリーダーかは\x01",
            "分かりませんが、気骨のある\x01",
            "芯の強い人なのは確かでしょうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_1323F")

    label("loc_131AA")


    #C0506
    ChrTalk(
        0x16,
        (
            "抵抗活動をするというのは、\x01",
            "相当な信念が必要なはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x16,
        (
            "どんな方がリーダーかは\x01",
            "分かりませんが、気骨のある\x01",
            "芯の強い人なのは確かでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1323F")

    Jump("loc_13458")

    label("loc_13244")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_133CF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1336A")

    #C0508
    ChrTalk(
        0x16,
        (
            "そこの機関室には\x01",
            "何があっても入らないように\x01",
            "お願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x16,
        (
            "世俗の人間には見せられない\x01",
            "重要なものがありますから。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 4)), scpexpr(EXPR_END)), "loc_1333B")

    #C0510
    ChrTalk(
        0x101,
        (
            "#00005F（さっきアッバスが話してた\x01",
            "  《天の車》とかいう\x01",
            "  アーティファクト……かな？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13362")

    label("loc_1333B")


    #C0511
    ChrTalk(
        0x101,
        "#00005F（何があるんだろう……？）\x02",
    )

    CloseMessageWindow()

    label("loc_13362")

    SetScenarioFlags(0x2, 2)
    Jump("loc_133CA")

    label("loc_1336A")


    #C0512
    ChrTalk(
        0x16,
        (
            "そろそろ機関室内部の\x01",
            "メンテナンスを\x01",
            "しなくちゃいけません。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x16,
        "……覗かないでくださいね？\x02",
    )

    CloseMessageWindow()

    label("loc_133CA")

    Jump("loc_13458")

    label("loc_133CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_13458")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_133EA")
    Call(1, 47)
    Jump("loc_13458")

    label("loc_133EA")


    #C0514
    ChrTalk(
        0x16,
        (
            "……結社が出張っている以上、\x01",
            "騎士団も今回の件を\x01",
            "見過ごすことはできません。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x16,
        "お互い、頑張りましょう。\x02",
    )

    CloseMessageWindow()

    label("loc_13458")

    Jump("loc_12548")

    label("loc_1345D")

    TalkEnd(0x16)
    Return()

    # Function_46_1253B end

    def Function_47_13461(): pass

    label("Function_47_13461")


    #C0516
    ChrTalk(
        0x16,
        (
            "あなたがクロスベル警察の\x01",
            "特務支援課の方ですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x16,
        (
            "自分はこの機関部の\x01",
            "管理を任されている\x01",
            "ジュノー、と申します。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x16,
        (
            "クオーツの合成や\x01",
            "戦術オーブメントの改造は\x01",
            "自分に任せて下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x101,
        (
            "#00005Fへえ……従騎士っていうのは\x01",
            "そんなことまで出来るんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x16,
        (
            "ふふ、私は特別、\x01",
            "手先の器用さにかけては\x01",
            "自信がありまして。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0521
    ChrTalk(
        0x16,
        (
            "……結社が出張っている以上、\x01",
            "騎士団も今回の件を\x01",
            "見過ごすことはできません。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x16,
        "お互い、頑張りましょう。\x02",
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x101,
        "#00000Fええ……よろしくお願いします。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 4)
    Return()

    # Function_47_13461 end

    def Function_48_13657(): pass

    label("Function_48_13657")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0524
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K 仮眠室 \x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "休憩する\x01",      # 0
            "やめる\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_137A6")
    EventBegin(0x2)
    Fade(500)
    OP_68(2040, 1000, -91940, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 1300, 0, -92030, 90)
    OP_0D()
    Sound(100, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0xA, 0x1, 0x8)
    Sleep(500)

    def lambda_13711():
        OP_95(0xFE, 4300, 0, -92030, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13711)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFF, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    OP_70(0x3, 0x0)
    OP_68(1300, 1000, -92030, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 1300, 0, -92030, 270)
    SetChrSubChip(0x101, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x3)

    label("loc_137A6")

    TalkEnd(0xFF)
    Return()

    # Function_48_13657 end

    def Function_49_137AA(): pass

    label("Function_49_137AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_137C0")
    OP_C9(0x0, 0x4)
    OP_C9(0x0, 0x100)

    label("loc_137C0")

    OP_E5(0xA)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E5(0x5)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_137D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13D01")
    RunExpression(0x5, (scpexpr(EXPR_EXEC_OP, "OP_E5(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_13812"),
        (1, "loc_13841"),
        (2, "loc_13CE5"),
        (3, "loc_13CED"),
        (SWITCH_DEFAULT, "loc_13CFC"),
    )


    label("loc_13812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_13831")
    OP_2B(0x9A, 0x9B, 0x9C, 0x96, 0x97, 0x98, 0x99, 0xFFFF)
    Jump("loc_1383C")

    label("loc_13831")

    OP_2B(0x96, 0x97, 0x98, 0x99, 0xFFFF)

    label("loc_1383C")

    Jump("loc_13CFC")

    label("loc_13841")

    SetMapFlags(0x40000000)
    OP_E5(0x7)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1391A")
    SetChrName("自動アナウンス")

    #A0525
    AnonymousTalk(
        0xFF,
        "こちらはクロスベル警察です。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_138F3")

    #A0526
    AnonymousTalk(
        0xFF,
        "報告を承ります。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    SetChrName("自動アナウンス")

    #A0527
    AnonymousTalk(
        0xFF,
        (
            "報告処理を終了します。\x01",
            "お疲れ様でした。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13915")

    label("loc_138F3")


    #A0528
    AnonymousTalk(
        0xFF,
        "報告可能な依頼はありません。\x02",
    )

    CloseMessageWindow()

    label("loc_13915")

    Jump("loc_13CD7")

    label("loc_1391A")

    SetChrName("受付嬢フラン")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1396E")
    Sound(3062, 255, 100, 0)    #voice#Fran

    #A0529
    AnonymousTalk(
        0xFF,
        "#26Aはい、こちらクロスベル警察です～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1399A")

    label("loc_1396E")

    Sound(3061, 255, 100, 0)    #voice#Fran

    #A0530
    AnonymousTalk(
        0xFF,
        "#29A皆さん、どうもお疲れさまですー。\x02",
    )

    CloseMessageWindow()

    label("loc_1399A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E5(0x4)"), scpexpr(EXPR_END)), "loc_13BE3")
    Sound(3067, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0531
    AnonymousTalk(
        0xFF,
        "#27Aそれでは報告を承りますね～。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    RunExpression(0x8, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x8), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13B6E")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (14, "loc_13A0B"),
        (13, "loc_13A55"),
        (12, "loc_13A9D"),
        (SWITCH_DEFAULT, "loc_13AE7"),
    )


    label("loc_13A0B")

    Sound(3075, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0532
    AnonymousTalk(
        0xFF,
        (
            "#39Aクラス１ｓｔ――\x01",
            "ロイドさん、スゴすぎです！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13AE7")

    label("loc_13A55")

    Sound(3074, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0533
    AnonymousTalk(
        0xFF,
        (
            "#38Aクラス２ｎｄ──\x01",
            "ロイドさん、すごいです！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13AE7")

    label("loc_13A9D")

    Sound(3073, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0534
    AnonymousTalk(
        0xFF,
        (
            "#33Aクラス３ｒｄ──\x01",
            "ロイドさん、やりましたね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13AE7")

    label("loc_13AE7")

    Sound(3076, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0535
    AnonymousTalk(
        0xFF,
        (
            "#33A特典の品もすぐに\x01",
            "そちらにお届けしますね～！\x02",
        )
    )

    CloseMessageWindow()
    Sound(3077, 255, 100, 0)    #voice#Fran

    #A0536
    AnonymousTalk(
        0xFF,
        (
            "#33Aお疲れさまでした～！\x01",
            "またよろしくお願いしますー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13BDB")

    label("loc_13B6E")

    Sound(3078, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0537
    AnonymousTalk(
        0xFF,
        "#17A報告は以上ですね～。\x02",
    )

    CloseMessageWindow()
    Sound(3079, 255, 100, 0)    #voice#Fran

    #A0538
    AnonymousTalk(
        0xFF,
        (
            "#38Aでは、また依頼を達成したら\x01",
            "よろしくお願いしますー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13BDB")

    SetScenarioFlags(0x2, 4)
    Jump("loc_13CD7")

    label("loc_13BE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_END)), "loc_13C68")
    Sound(3063, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0539
    AnonymousTalk(
        0xFF,
        (
            "#31Aあれっ……\x01",
            "先ほど報告されたばかりですよ？\x02",
        )
    )

    CloseMessageWindow()
    Sound(3064, 255, 100, 0)    #voice#Fran

    #A0540
    AnonymousTalk(
        0xFF,
        "#35Aまた依頼を達成されたらお願いしますね～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_13CD7")

    label("loc_13C68")

    Sound(3065, 255, 100, 0)    #voice#Fran
    SetChrName("受付嬢フラン")

    #A0541
    AnonymousTalk(
        0xFF,
        (
            "#38Aあれっ、報告可能な\x01",
            "依頼は無いみたいですね～。\x02",
        )
    )

    CloseMessageWindow()
    Sound(3066, 255, 100, 0)    #voice#Fran

    #A0542
    AnonymousTalk(
        0xFF,
        "#20Aまたよろしくお願いしますー。\x02",
    )

    CloseMessageWindow()

    label("loc_13CD7")

    OP_57(0x0)
    OP_E5(0x8)
    ClearMapFlags(0x40000000)
    Jump("loc_13CFC")

    label("loc_13CE5")

    Call(1, 50)
    Jump("loc_13CFC")

    label("loc_13CED")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_13CFC")

    label("loc_13CFC")

    Jump("loc_137D9")

    label("loc_13D01")

    OP_E5(0x6)
    OP_C9(0x1, 0x4)
    OP_C9(0x1, 0x100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13D3E")
    OP_E5(0xB)
    TalkEnd(0xFF)
    Call(1, 51)
    Return()

    label("loc_13D3E")

    FadeToBright(1000, 0)
    OP_0D()
    OP_E5(0xB)
    TalkEnd(0xFF)
    Return()

    # Function_49_137AA end

    def Function_50_13D4E(): pass

    label("Function_50_13D4E")

    OP_E5(0x6)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 3)), scpexpr(EXPR_END)), "loc_13D70")
    SetScenarioFlags(0x2A, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13D70")
    ClearScenarioFlags(0x2A, 0)

    label("loc_13D70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 4)), scpexpr(EXPR_END)), "loc_13D8D")
    SetScenarioFlags(0x2A, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13D8D")
    ClearScenarioFlags(0x2A, 1)

    label("loc_13D8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 5)), scpexpr(EXPR_END)), "loc_13DAA")
    SetScenarioFlags(0x2A, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13DAA")
    ClearScenarioFlags(0x2A, 2)

    label("loc_13DAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 6)), scpexpr(EXPR_END)), "loc_13DC7")
    SetScenarioFlags(0x2A, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13DC7")
    ClearScenarioFlags(0x2A, 3)

    label("loc_13DC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x27, 7)), scpexpr(EXPR_END)), "loc_13DE4")
    SetScenarioFlags(0x2A, 4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13DE4")
    ClearScenarioFlags(0x2A, 4)

    label("loc_13DE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 0)), scpexpr(EXPR_END)), "loc_13E01")
    SetScenarioFlags(0x2A, 5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13E01")
    ClearScenarioFlags(0x2A, 5)

    label("loc_13E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 1)), scpexpr(EXPR_END)), "loc_13E0D")
    SetScenarioFlags(0x2A, 6)

    label("loc_13E0D")

    OP_24(0x1F2)
    RunExpression(0x9, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_1F()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1E), scpexpr(EXPR_PUSH_LONG, 0x2A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E52")
    Sound(498, 1, 50, 0)
    Jump("loc_13E58")

    label("loc_13E52")

    Sound(498, 1, 100, 0)

    label("loc_13E58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x28, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2A, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13E88")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13E88")

    Return()

    # Function_50_13D4E end

    def Function_51_13E89(): pass

    label("Function_51_13E89")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0xB, 0x12)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0x8, 0x1A)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0xC, 0x1B)
    SetChrSubChip(0xC, 0x0)
    OP_4B(0xB, 0xFF)
    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_END)), "loc_13EF2")
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, 102700, 0, -102930, 180)

    label("loc_13EF2")

    OP_68(102970, 1000, -104740, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14560, 0)
    SetChrPos(0x101, 103020, 100, -105800, 90)
    SetChrPos(0xB, 101590, 0, -105440, 90)
    SetChrPos(0xC, 101470, 0, -104110, 135)
    SetChrPos(0x8, 103000, 0, -104100, 180)
    FadeToBright(1000, 0)
    OP_0D()

    #C0543
    ChrTalk(
        0xB,
        (
            "#00205Fおや……\x02\x03",

            "#00204Fどうやらロイドさんは、\x01",
            "『ポムっと！』で全員から\x01",
            "勝利を収めたみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0xC,
        (
            "#01905Fええっ、本当ですか～！？\x02\x03",

            "#01909Fさすがロイドさん……\x01",
            "スゴすぎますよ～！！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 0)), scpexpr(EXPR_END)), "loc_14070")

    #C0545
    ChrTalk(
        0x9,
        (
            "#02302Fへっ、そうだな。\x01",
            "アンタもなかなかやるじゃん。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14070")

    SetChrSubChip(0x101, 0x1)

    #C0546
    ChrTalk(
        0x101,
        (
            "#00009Fはは、ありがとう。\x01",
            "運がよかっただけかもしれないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x8,
        (
            "#12100Fいや、このパズルゲームにおいては\x01",
            "運だけが勝利の要因たりえまい。\x02\x03",

            "#12102Fバニングス、お前こそが\x01",
            "真の『ポムっと！マスター』だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x101,
        "#00012F……そ、そりゃどうも。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xF0, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14315")

    #C0549
    ChrTalk(
        0x8,
        (
            "#12100Fふむ……そうだな。\x02\x03",

            "よければこれを受け取るがいい。\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x8, 0x0, 0x1F4, 0x5DC, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0550
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xF0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xF0, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0551
    ChrTalk(
        0x8,
        (
            "#12100F教会とエプスタイン財団が\x01",
            "古代の術をもとにして共同開発した、\x01",
            "禁断のマスタークオーツだ。\x02\x03",

            "強力すぎて扱いが難しく、\x01",
            "運用に踏み切れなかったものだが……\x02\x03",

            "#12102Fお前ならば正しく扱えるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x101,
        (
            "#00000Fああ、分かった。\x01",
            "是非とも役立たせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_143F9")

    label("loc_14315")


    #C0553
    ChrTalk(
        0x8,
        (
            "#12100Fふむ……そうだな。\x02\x03",

            "#12102F褒賞としてお前にこれをやろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x8, 0x0, 0x1F4, 0x5DC, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0554
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x67),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x67, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)

    #C0555
    ChrTalk(
        0x101,
        (
            "#00000Fはは、ありがとう。\x01",
            "是非とも役立たせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_143F9")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x2A, 7)
    OP_E0(0x35, 0x0)
    OP_E0(0x80, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x4)
    OP_D7(0x1E)
    EventEnd(0x5)
    SetScenarioFlags(0x24, 3)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_51_13E89 end

    def Function_52_1442B(): pass

    label("Function_52_1442B")

    EventBegin(0x0)
    Fade(500)
    OP_68(4130, -1100, 7060, 0)
    MoveCamera(47, 40, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(14590, 0)
    SetChrPos(0x101, 4000, -1500, 5730, 315)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x101, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14502")
    Jump("loc_1454C")

    label("loc_14502")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_14522")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1454C")

    label("loc_14522")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14542")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1454C")

    label("loc_14542")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1454C")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)
    OP_0D()

    #C0556
    ChrTalk(
        0xC,
        (
            "#6P#01905Fロイドさん……\x01",
            "なんだかお疲れみたいですね。\x02\x03",

            "大丈夫ですか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x101,
        (
            "#11P#00005Fああ……言われてみれば。\x02\x03",

            "#00003F色々なことがあったから、\x01",
            "疲れが出てるのかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0xC,
        (
            "#6P#01906Fえっと、絶対に無理は\x01",
            "しないでくださいね～。\x02\x03",

            "#01908Fもしロイドさんたちやお姉ちゃんが\x01",
            "倒れたりしたらと思うと……\x01",
            "わたし、とっても心配ですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x101,
        (
            "#11P#00000Fああ、ありがとう。\x01",
            "十分に気をつけさせて……\x02",
        )
    )

    CloseMessageWindow()

    #C0560
    ChrTalk(
        0xC,
        (
            "#6P#01901F気をつけるだけじゃダメですよ～！\x01",
            "こういうときはしっかり休まないと！\x02\x03",

            "#01902Fなんでしたら、わたしが\x01",
            "マッサージして差し上げましょうか？\x02\x03",

            "#01909F疲れに効くツボをゴリッと押せば、\x01",
            "一発で元気になれますよ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0561
    ChrTalk(
        0x101,
        (
            "#11P#00006F（な、なんだかすごく痛そうだ……）\x02\x03",

            "#00002Fえ、えっと……\x01",
            "気持ちはありがたいけど大丈夫だよ。\x02\x03",

            "#00009Fフランと話してるだけで\x01",
            "なんだかリフレッシュできた気がするし。\x02",
        )
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0xC,
        (
            "#6P#01905Fえ……そ、そうですか～？\x02\x03",

            "#01909Fえへへ……\x01",
            "そう言ってもらえると嬉しいです～。\x02\x03",

            "#01904Fオペレーターとして、\x01",
            "皆さんに元気を与えるのが\x01",
            "わたしの使命だと思ってますから。\x02",
        )
    )

    CloseMessageWindow()

    #C0563
    ChrTalk(
        0x101,
        (
            "#11P#00009Fはは、だとしたら\x01",
            "本当に天職だと思うよ。\x02\x03",

            "#00004F実際、端末に映る君の笑顔に、\x01",
            "何度癒されたことか分からないし……\x02\x03",

            "#00000F警察本部を出入りする人たちにも、\x01",
            "君目当ての人が結構多いと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0564
    ChrTalk(
        0xC,
        (
            "#6P#01906Fうう、そこまで言われると\x01",
            "ちょっと恥ずかしいですけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xC)

    #C0565
    ChrTalk(
        0xC,
        (
            "#6P#01904Fでも、そうですね～。\x01",
            "ロイドさんには今後とも\x01",
            "頑張ってほしいですし～……\x02\x03",

            "#01902Fよかったら、これを\x01",
            "受け取ってもらえませんか？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0566
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x39E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x39E, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0567
    ChrTalk(
        0x101,
        "#11P#00005Fこれは……もらってもいいのか？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 4)), scpexpr(EXPR_END)), "loc_14D34")

    #C0568
    ChrTalk(
        0xC,
        (
            "#6P#01909Fはいっ、是非とも\x01",
            "持っておいてください。\x02\x03",

            "#01904Fなにせ、ロイドさんは将来\x01",
            "わたしのお義兄ちゃんに\x01",
            "なるかもしれない人ですし……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0569
    ChrTalk(
        0x101,
        "#11P#00011Fえ……ええっ！？\x02",
    )

    CloseMessageWindow()

    #C0570
    ChrTalk(
        0xC,
        (
            "#6P#01909Fむふふ……\x01",
            "わたしはお姉ちゃんのことなら\x01",
            "なんでも分かるんですよ～。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0571
    ChrTalk(
        0x101,
        (
            "#11P#00012F（は、はは……参ったな。\x01",
            "  さすがにお見通しか……）\x02\x03",

            "#00000F……えっと、それじゃあ\x01",
            "ありがたく使わせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14DF1")

    label("loc_14D34")


    #C0572
    ChrTalk(
        0xC,
        (
            "#6P#01909Fはいっ、是非とも\x01",
            "持っておいてください。\x02\x03",

            "皆さんの無事を祈って\x01",
            "作ったものですから、\x01",
            "きっと効き目は抜群ですよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0573
    ChrTalk(
        0x101,
        (
            "#11P#00009Fはは、それじゃあ、\x01",
            "ありがたく使わせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14DF1")


    #C0574
    ChrTalk(
        0xC,
        "#6P#01909Fえへへ、大事にしてくださいね～。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1D9, 4)
    SetScenarioFlags(0x1, 5)
    SetChrSubChip(0xC, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14E48")
    OP_E0(0x34, 0x0)

    label("loc_14E48")

    EventEnd(0x5)
    Return()

    # Function_52_1442B end

    def Function_53_14E4B(): pass

    label("Function_53_14E4B")

    EventBegin(0x0)
    Fade(500)
    OP_68(97920, 1000, 600, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15320, 0)
    SetChrPos(0x101, 97510, 0, -530, 0)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x14, 0x10)
    TurnDirection(0x14, 0x101, 0)
    OP_52(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14F22")
    Jump("loc_14F6C")

    label("loc_14F22")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_14F42")
    OP_52(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14F6C")

    label("loc_14F42")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14F62")
    OP_52(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_14F6C")

    label("loc_14F62")

    OP_52(0x14, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x14, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14F6C")

    OP_52(0x14, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x14, 0x10)
    OP_0D()

    #C0575
    ChrTalk(
        0x14,
        (
            "#5P#00603Fふむ……\x02\x03",

            "#00600F……バニングス、お前も\x01",
            "少しは成長したようだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0576
    ChrTalk(
        0x101,
        "#12P#00005Fえっ……？\x02",
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0x14,
        (
            "#5P#00603Fお前たちにここまで\x01",
            "同行させてもらったが……\x02\x03",

            "捜査や推理の腕も確かだし、\x01",
            "以前のような青臭さは\x01",
            "もう完全に抜けたと言っていい。\x02\x03",

            "ガイやマクレインの現役時代には\x01",
            "まだまだと言ったところだが……\x02\x03",

            "#00602Fフ、捜査一課で面倒を見た\x01",
            "甲斐があったというものだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0578
    ChrTalk(
        0x101,
        (
            "#12P#00012Fえ、えっと……\x01",
            "突然、どうしたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0579
    ChrTalk(
        0x14,
        "#5P#00603Fいいから黙って聞くがいい。\x02",
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x101,
        "#12P#00006Fハ、ハイ。\x02",
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x14,
        (
            "#5P#00600F……先ほどガイやマクレインの\x01",
            "話をしたが、奴らと同じタイプの\x01",
            "捜査官を目指せとは言わん。\x02\x03",

            "お前にはお前の素質がある。\x01",
            "そこを伸ばしていくことで\x01",
            "優秀な捜査官へと近づけるだろう。\x02\x03",

            "#00604F自分なりの捜査官を目指し、\x01",
            "今後も一層精進していくがいい。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0582
    ChrTalk(
        0x14,
        "#5P#00605F……何だ、何か文句でもあるのか？\x02",
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x101,
        (
            "#12P#00011Fい、いえ……\x01",
            "なんだか驚いてしまって。\x02\x03",

            "#00006Fそこまで評価してくれるなんて\x01",
            "ダドリーさんらしくないというか……\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x14,
        (
            "#5P#00603F……国防軍がどうなるかは\x01",
            "今後の動向次第だろうが、\x01",
            "それでも警察は存続するだろう。\x02\x03",

            "#00600Fこの一連の事件が収束すれば、\x01",
            "少なくともお前は警察に戻る\x01",
            "ことになるはずだ。\x02\x03",

            "それに備えて、一課の主任捜査官として\x01",
            "今のうちからアドバイスを\x01",
            "くれてやろうと思ってな。\x02\x03",

            "#00603Fただ、それだけのことだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x101,
        (
            "#12P#00000Fそうですか……\x02\x03",

            "#00004F……ありがとうございます。\x02\x03",

            "#00002Fダドリーさんの期待に応えられるよう、\x01",
            "今後も精進させていただこうと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x14,
        (
            "#5P#00606Fフン、勘違いするんじゃないぞ。\x02\x03",

            "あくまでここまでのお前を分析して\x01",
            "客観的事実を言ったまでだ。\x02\x03",

            "#00600F何はなくとも、この事件を解決し\x01",
            "全ての真実を掴まないことには\x01",
            "次へと進む事はできんのだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0x101,
        (
            "#12P#00012F（はは、相変わらず素直じゃ\x01",
            "  ないっていうか……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0588
    ChrTalk(
        0x14,
        "#5P#00601F……何をニヤついている？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0589
    ChrTalk(
        0x101,
        "#12P#00011Fい、いえ、何でもありません！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_156EF")
    Jump("loc_157B7")

    label("loc_156EF")

    Sleep(500)
    Sound(517, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0590
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "ロイドとダドリーは\x01",
            "ハーツオブアイアンⅡを習得した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0591
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドとダドリーのコンビクラフト、\x01",
            "《ハーツオブアイアン》が強化されました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddCraft(0x9, 0x1AA)
    AddCraft(0x0, 0x1AA)

    label("loc_157B7")

    OP_E0(0x24, 0x0)
    OP_E0(0x80, 0x0)
    SetScenarioFlags(0x1D9, 1)
    SetScenarioFlags(0x1, 3)
    SetChrSubChip(0x14, 0x0)
    EventEnd(0x5)
    Return()

    # Function_53_14E4B end

    def Function_54_157CA(): pass

    label("Function_54_157CA")

    EventBegin(0x0)
    Fade(500)
    OP_68(96790, 1200, -101940, 0)
    MoveCamera(48, 33, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16250, 0)
    SetChrPos(0x101, 96960, 0, -100830, 180)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xD, 0x10)
    TurnDirection(0xD, 0x101, 0)
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_158A1")
    Jump("loc_158EB")

    label("loc_158A1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_158C1")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_158EB")

    label("loc_158C1")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_158E1")
    OP_52(0xD, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_158EB")

    label("loc_158E1")

    OP_52(0xD, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_158EB")

    OP_52(0xD, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x10)
    OP_0D()
    SetChrName("")

    #A0592
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはリーシャに障壁のことを説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0593
    ChrTalk(
        0xD,
        (
            "#12P#10704F……どうやら私が行く必要が\x01",
            "あるみたいですね。\x02\x03",

            "#10701F“彼女”と因果のある者として……\x02",
        )
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x101,
        (
            "#00003F……なあ、リーシャ。\x02\x03",

            "#00001Fできれば彼女のことは\x01",
            "俺たちに任せて……\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0xD,
        (
            "#12P#10706F───いいえ。\x02\x03",

            "#10708F私と彼女はある意味、\x01",
            "似たような境遇の存在です。\x02\x03",

            "私自身が、この先の道を\x01",
            "見出すためにも……\x02\x03",

            "#10701F私は彼女ともう一度、\x01",
            "見#2Rまみ#えなくてはなりません。\x02",
        )
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0x101,
        (
            "#00006F………分かった。\x02\x03",

            "#00001F準備ができたら行くとしよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1D8, 4)
    SetChrSubChip(0xD, 0x0)
    EventEnd(0x5)
    Return()

    # Function_54_157CA end

    def Function_55_15B0D(): pass

    label("Function_55_15B0D")

    EventBegin(0x0)
    Fade(500)
    OP_68(101090, 1000, -93870, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16290, 0)
    SetChrPos(0x101, 100220, 0, -93940, 90)
    SetChrPos(0xA, 101370, 150, -94090, 270)
    SetChrSubChip(0xA, 0x0)
    OP_0D()
    SetChrName("")

    #A0597
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはワジに障壁のことを説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0598
    ChrTalk(
        0xA,
        (
            "#10404Fふうん……なるほどね。\x02\x03",

            "#10408F……まったく。\x01",
            "どうして僕みたいな\x01",
            "半端者にこだわるんだか。\x02",
        )
    )

    CloseMessageWindow()

    #C0599
    ChrTalk(
        0x101,
        "#6P#00008Fワジ……\x02",
    )

    CloseMessageWindow()

    #C0600
    ChrTalk(
        0xA,
        (
            "#10401Fどうやら“彼”は\x01",
            "僕との決着をお望みらしい。\x02\x03",

            "#10403Fロイド、僕を探索メンバーに\x01",
            "入れてくれるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0601
    ChrTalk(
        0x101,
        (
            "#6P#00003Fああ、分かった。\x02\x03",

            "#00000F準備ができたら行くとしよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1D8, 0)
    SetChrPos(0xA, 101790, 150, -93960, 90)
    EventEnd(0x5)
    Return()

    # Function_55_15B0D end

    def Function_56_15CE5(): pass

    label("Function_56_15CE5")

    EventBegin(0x0)
    Fade(500)
    OP_68(-3010, -500, 6090, 0)
    MoveCamera(46, 33, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16290, 0)
    SetChrPos(0x101, -3520, -1500, 5560, 0)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x101, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15DBC")
    Jump("loc_15E06")

    label("loc_15DBC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_15DDC")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15E06")

    label("loc_15DDC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15DFC")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_15E06")

    label("loc_15DFC")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15E06")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    OP_93(0x8, 0x104, 0x0)
    EndChrThread(0x8, 0x0)
    OP_0D()

    #C0602
    ChrTalk(
        0xB,
        (
            "#00200F先ほどからアッバスさんに\x01",
            "端末の使い方を教えてもらって\x01",
            "いるのですが……\x02\x03",

            "#00203Fどうやら、《メルカバ》のシステムは\x01",
            "エプスタイン財団製のようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x101,
        "#00005Fえっ……そうなのか！？\x02",
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0xB,
        (
            "#00200Fええ、間違いないと思います。\x02\x03",

            "#00203F昔、教会の人間が財団本部にいたのを\x01",
            "見かけたことがありましたが……\x02",
        )
    )

    CloseMessageWindow()
    OP_52(0x8, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x8, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15FFD")
    Jump("loc_16047")

    label("loc_15FFD")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1601D")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16047")

    label("loc_1601D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1603D")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_16047")

    label("loc_1603D")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_16047")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x8, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)

    #C0605
    ChrTalk(
        0xB,
        (
            "#00200Fもしかして、財団と教会は\x01",
            "以前から協力関係にあるのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0606
    ChrTalk(
        0x8,
        (
            "#12100F……非公式ではあるがな。\x02\x03",

            "このメルカバは、もとは\x01",
            "《天の車》という飛翔機能を持つ\x01",
            "アーティファクトの乗り物だったが……\x02\x03",

            "導力革命以降、財団の協力を受けて、\x01",
            "《天の車》を機関部に利用した\x01",
            "現在の形に改修されたのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x101,
        (
            "#00005F《天の車》……\x01",
            "ツァイトがメルカバを見たときに\x01",
            "呟いていた名前だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x8,
        (
            "#12100Fついでに言えば、教会の方も\x01",
            "戦術オーブメントの開発などに\x01",
            "一部協力している。\x02\x03",

            "お前たちが使っている\x01",
            "『導力魔法』も、もとはといえば\x01",
            "《法術》の技術を応用したものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0609
    ChrTalk(
        0xB,
        "#00203Fなるほど……\x02",
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x8,
        (
            "#12100F……分かっているとは思うが、\x01",
            "あくまで非公式の事柄だ。\x01",
            "くれぐれも外部には漏らさぬようにな。\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x101,
        "#00000Fああ、もちろん分かってるさ。\x02",
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0xB,
        "#00200Fわたしも了解しました。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 4)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0xB, 0x10)
    SetChrSubChip(0xB, 0x0)
    OP_93(0x8, 0x13B, 0x0)
    BeginChrThread(0x8, 0, 0, 0)
    EventEnd(0x5)
    Return()

    # Function_56_15CE5 end

    SaveToFile()

Try(main)
