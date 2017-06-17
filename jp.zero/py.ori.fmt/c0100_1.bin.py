from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0100_1.bin",                # FileName
        "c0100",                    # MapName
        "c0100",                    # Location
        0x0004,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 1100, 0, -3500, 0, 0, 1, 4, 0, 5, 0, 6],
    )

    BuildStringList((
        "c0100_1",                # 0
    ))

    ScpFunction((
        "Function_0_1CC",          # 00, 0
        "Function_1_E3B",          # 01, 1
        "Function_2_1E44",         # 02, 2
        "Function_3_2A93",         # 03, 3
        "Function_4_38CC",         # 04, 4
        "Function_5_3F6D",         # 05, 5
        "Function_6_46F8",         # 06, 6
        "Function_7_516A",         # 07, 7
        "Function_8_5371",         # 08, 8
        "Function_9_686C",         # 09, 9
        "Function_10_7B84",        # 0A, 10
        "Function_11_8568",        # 0B, 11
        "Function_12_86B9",        # 0C, 12
        "Function_13_87F3",        # 0D, 13
        "Function_14_898D",        # 0E, 14
        "Function_15_8B5A",        # 0F, 15
        "Function_16_91FB",        # 10, 16
        "Function_17_950E",        # 11, 17
    ))


    def Function_0_1CC(): pass

    label("Function_0_1CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_23C")

    #C0001
    ChrTalk(
        0xFE,
        "今日はきちんと買い物も済んだわ。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "予定通りに事が進むって\x01",
            "なんて気持ちいいのかしら～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E37")

    label("loc_23C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_28A")

    #C0003
    ChrTalk(
        0xFE,
        "ふあ～……おはよー。\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        "今日も良い一日になるといいわね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E37")

    label("loc_28A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_35F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31B")

    #C0005
    ChrTalk(
        0xFE,
        "港湾区の方に人だかりが出来てたわ。\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "警察の人も来てて、\x01",
            "何だかおっかない雰囲気だったけど\x01",
            "何かあったのかな～？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_35A")

    label("loc_31B")


    #C0007
    ChrTalk(
        0xFE,
        (
            "港湾区で何かあったみたい。\x01",
            "……怖いことだったらやだな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35A")

    Jump("loc_E37")

    label("loc_35F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_36D")
    Jump("loc_E37")

    label("loc_36D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_406")

    #C0008
    ChrTalk(
        0xFE,
        (
            "なんだか、予算議会ってのが\x01",
            "遅れ気味なんですって～。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "まぁでも、毎年同じように\x01",
            "遅れてるみたいだし……\x01",
            "あんまり気にならないかなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E37")

    label("loc_406")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_547")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DF")

    #C0010
    ChrTalk(
        0xFE,
        (
            "記念祭の最終日に\x01",
            "ミシュラムで花火を見たわ。\x01",
            "綺麗だったな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "けど、あの夜はひと騒動あって\x01",
            "大変だったそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "ミシュラムに宿泊するお金がなくて\x01",
            "かえってラッキーだったかもね～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_542")

    label("loc_4DF")


    #C0013
    ChrTalk(
        0xFE,
        (
            "記念祭最終日の夜は\x01",
            "ミシュラムでひと騒動あったそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        "直前で帰れてラッキーだったかも～。\x02",
    )

    CloseMessageWindow()

    label("loc_542")

    Jump("loc_E37")

    label("loc_547")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_689")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_621")

    #C0015
    ChrTalk(
        0xFE,
        (
            "マグダエル市長って\x01",
            "しっかりした\x01",
            "おじいちゃんって感じよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "政治家なのに親しみやすいし\x01",
            "まだまだ元気、みたいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "でも……いつも\x01",
            "杖をついてるのよね。\x01",
            "やっぱり体がつらいのかなー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_684")

    label("loc_621")


    #C0018
    ChrTalk(
        0xFE,
        (
            "パパが、マグダエル市長は今年で\x01",
            "引退するかもって言ってたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        "やっぱり本当なのかなー。\x02",
    )

    CloseMessageWindow()

    label("loc_684")

    Jump("loc_E37")

    label("loc_689")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_76F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_715")

    #C0020
    ChrTalk(
        0xFE,
        (
            "今年の記念祭は\x01",
            "どんな感じになるのかなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "どこのお店も\x01",
            "何か準備してるみたいだし\x01",
            "ふふっ、楽しみよね～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_76A")

    label("loc_715")


    #C0022
    ChrTalk(
        0xFE,
        (
            "クロスベル最大のお祭り、\x01",
            "創立記念祭まであと少し……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        "ふふっ、楽しみよね～。\x02",
    )

    CloseMessageWindow()

    label("loc_76A")

    Jump("loc_E37")

    label("loc_76F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_7DA")

    #C0024
    ChrTalk(
        0xFE,
        "買い物してたら遅くなっちゃった。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "お店をのぞいてると\x01",
            "ついつい長引いちゃうのよね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E37")

    label("loc_7DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_872")

    #C0026
    ChrTalk(
        0xFE,
        "今日は警察の人が多いわね……\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        "朝から５回も６回もすれ違うの。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "事件があったわけでも\x01",
            "なさそうなのに……\x01",
            "一体何してるのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E37")

    label("loc_872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_9ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_956")

    #C0029
    ChrTalk(
        0xFE,
        (
            "はーあ、アルカンシェルのチケット\x01",
            "結局手に入らなかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "友達と２人で\x01",
            "頑張って並んだんだけどなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "あたしたちの５人くらい前で\x01",
            "全部売り切れちゃったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        "ううっ、ほんとショックだわ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_9E8")

    label("loc_956")


    #C0033
    ChrTalk(
        0xFE,
        "ああ、思い出すだけで悔しいぃ～！\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "そもそもあそこのチケット、\x01",
            "ちょっと高すぎるのよっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "お小遣いはたいても\x01",
            "なかなか買えないじゃない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9E8")

    Jump("loc_E37")

    label("loc_9ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_A67")

    #C0036
    ChrTalk(
        0xFE,
        (
            "アルモリカ村の野菜は\x01",
            "健康にいいって噂よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "お肌ツルツルになるんだって。\x01",
            "あたしも試してみようかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E37")

    label("loc_A67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_B4D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B00")

    #C0038
    ChrTalk(
        0xFE,
        (
            "今日は西通りの親戚の家に\x01",
            "遊びに行くつもりなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "でも市内には\x01",
            "バスが通ってないのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "まったく不便なんだから。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_B48")

    label("loc_B00")


    #C0041
    ChrTalk(
        0xFE,
        (
            "クロスベル市は広いんだし、\x01",
            "市内バスがあっても\x01",
            "いいと思うんだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B48")

    Jump("loc_E37")

    label("loc_B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_BC8")

    #C0042
    ChrTalk(
        0xFE,
        "さっき緑の大きな車とすれ違ったの。\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "クロスベル警備隊の紋章が入ってたわ。\x01",
            "警備隊の人だったのかな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E37")

    label("loc_BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_CF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C7C")

    #C0044
    ChrTalk(
        0xFE,
        (
            "友達とアパルトメントを\x01",
            "借りようと思ってるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "中々安い物件が\x01",
            "見つからないのよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "しばらく実家暮らしから\x01",
            "抜け出せそうにないわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CEC")

    label("loc_C7C")


    #C0047
    ChrTalk(
        0xFE,
        (
            "最近の好景気で\x01",
            "お家賃が高止まりしてるらしいの。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        (
            "はあ、ルームシェアなら\x01",
            "何とかなるかと思ったんだけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CEC")

    Jump("loc_E37")

    label("loc_CF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_E37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DC5")

    #C0049
    ChrTalk(
        0xFE,
        (
            "うちのパパね、大きな会社に\x01",
            "勤めてるんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "最近『導力ネット』ってのが\x01",
            "整備されたんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "でも使い方が判らないって\x01",
            "毎日困ってるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        "んもう、ダメダメよねぇ～。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_E37")

    label("loc_DC5")


    #C0053
    ChrTalk(
        0xFE,
        (
            "『導力ネット』って、何だか\x01",
            "スゴク便利なものらしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "使い方が判らないんじゃ\x01",
            "無いのと同じよねぇ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E37")

    TalkEnd(0xFE)
    Return()

    # Function_0_1CC end

    def Function_1_E3B(): pass

    label("Function_1_E3B")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ECF")
    Jump("loc_F19")

    label("loc_ECF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EEF")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F19")

    label("loc_EEF")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F0F")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F19")

    label("loc_F0F")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F19")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_101A")

    #C0055
    ChrTalk(
        0xFE,
        (
            "ようやっと、長引いておった\x01",
            "予算議会が片付いたそうじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "市民への発表は後日……\x01",
            "はてさて、如何なる結果になったかのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "せめて去年よりは\x01",
            "ムダの少ない予算案が\x01",
            "可決されている事を祈るばかりじゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E3C")

    label("loc_101A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1088")

    #C0058
    ChrTalk(
        0xFE,
        (
            "今日こそ予算議会に\x01",
            "決着がつくかのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "今年は例年よりさらに\x01",
            "長引いておる気がするわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E3C")

    label("loc_1088")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1150")

    #C0060
    ChrTalk(
        0xFE,
        "聞いたか、マフィアの抗争の噂……\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "嫌な感じじゃ……\x01",
            "昔はこういうことには\x01",
            "常に人死にが絡んでおった。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "クロスベルも多少は\x01",
            "平和になったかと思うたが、\x01",
            "まだまだ安心できんのう……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E3C")

    label("loc_1150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_115E")
    Jump("loc_1E3C")

    label("loc_115E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_12E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1250")

    #C0063
    ChrTalk(
        0xFE,
        (
            "鉱山町マインツへ向かうトンネルから\x01",
            "分かれた道の先に遺跡があってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "満月の夜に美しい鐘の音色を\x01",
            "鳴り響かせるという伝説があるのじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "中世の時代に建てられたらしいこと\x01",
            "以外は何もわかっていないがのう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_12E0")

    label("loc_1250")


    #C0066
    ChrTalk(
        0xFE,
        (
            "鉱山町マインツへ向かうトンネルから\x01",
            "分かれた道の先に遺跡があってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "満月の夜に美しい鐘の音色を\x01",
            "鳴り響かせるという伝説があるのじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E0")

    Jump("loc_1E3C")

    label("loc_12E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1462")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13CE")

    #C0068
    ChrTalk(
        0xFE,
        (
            "明日から、予算議会が\x01",
            "市庁舎の方で行われるのじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "クロスベルの各公共事業に回される\x01",
            "予算を決定する大事な議会なのだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "毎年、終了予定日までには\x01",
            "纏まらなくてのう。\x01",
            "今年はどうなることやら……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_145D")

    label("loc_13CE")


    #C0071
    ChrTalk(
        0xFE,
        (
            "クロスベルの予算議会は、\x01",
            "毎年なかなか纏まらなくてのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "市長と議長の対立が\x01",
            "決定を遅らせているようじゃが、\x01",
            "今年はどうなることやら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_145D")

    Jump("loc_1E3C")

    label("loc_1462")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_15CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_153C")

    #C0073
    ChrTalk(
        0xFE,
        (
            "クロスベル市の南にある\x01",
            "『星見の塔』は\x01",
            "中世に建てられたものとされておる。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "当時からクロスベルは\x01",
            "交易と戦乱の地だったという。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "時の有力者が\x01",
            "占星術を頼って\x01",
            "作らせたという話じゃよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_15C9")

    label("loc_153C")


    #C0076
    ChrTalk(
        0xFE,
        (
            "『星見の塔』は中世の頃\x01",
            "占星術のために作られたという。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "もっとも、ろくに\x01",
            "調査されたことが無いとも聞く。\x01",
            "嘘か本当かは定かではないな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C9")

    Jump("loc_1E3C")

    label("loc_15CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_16DA")

    #C0078
    ChrTalk(
        0xFE,
        (
            "ＩＢＣの総裁・ディーター殿は\x01",
            "昔からクロスベルを支えてきた\x01",
            "経済の第一人者じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "ただ儲けておるだけではなく、\x01",
            "公共事業や福祉・支援機関への寄付も\x01",
            "精力的に行っておる。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "天はニ物を与えぬというが……\x01",
            "ディーター殿にはニ物も三物も\x01",
            "感じてしまうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E3C")

    label("loc_16DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_1747")

    #C0081
    ChrTalk(
        0xFE,
        "さて、わしもそろそろ帰らねばな。\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "いつまでもこんな所にいたら\x01",
            "風邪をひいてしまうわい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E3C")

    label("loc_1747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_17F6")

    #C0083
    ChrTalk(
        0xFE,
        (
            "噂のアルカンシェルの新作は、\x01",
            "準主役に新人が起用されたそうじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "あのイリア・プラティエに\x01",
            "スカウトされたという噂が本当なら、\x01",
            "かなりの実力者じゃろうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E3C")

    label("loc_17F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_18CD")

    #C0085
    ChrTalk(
        0xFE,
        (
            "クロスベル自治州に住むものは\x01",
            "賑やかなことが大好きでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "特に祭りともなると、\x01",
            "老いも若きも沸きあがるもんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "来月開催される創立記念祭は７０周年。\x01",
            "今年はどれほどの賑わいを見せるかのう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E3C")

    label("loc_18CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_196C")

    #C0088
    ChrTalk(
        0xFE,
        (
            "劇団《アルカンシェル》は\x01",
            "クロスベルが誇る大スター集団じゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "外国の著名人にも人気でな、\x01",
            "お忍びで入国してくる者も\x01",
            "少なくないそうじゃぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E3C")

    label("loc_196C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1A8B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A15")

    #C0090
    ChrTalk(
        0xFE,
        (
            "この前裏通りの方で\x01",
            "妙なアンティークショップを\x01",
            "見つけたんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "おかしな品が並んでおってな、\x01",
            "店主の婆さんも\x01",
            "怪しい感じじゃったわい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A86")

    label("loc_1A15")


    #C0092
    ChrTalk(
        0xFE,
        (
            "この前裏通りの方で\x01",
            "妙なアンティークショップを\x01",
            "見つけたんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "はて……昔から\x01",
            "あんな店があったかのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A86")

    Jump("loc_1E3C")

    label("loc_1A8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1C00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B97")

    #C0094
    ChrTalk(
        0xFE,
        (
            "クロスベル人というやつは\x01",
            "中々に噂好きでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "毎日散歩しておるだけで\x01",
            "随分と物知りになってしまうんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "事件の裏話から\x01",
            "外国の景気の動向まで……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "クロスベルにはあらゆる情報が\x01",
            "飛び交っておるといっても\x01",
            "過言ではないじゃろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BFB")

    label("loc_1B97")


    #C0098
    ChrTalk(
        0xFE,
        (
            "クロスベル人と\x01",
            "いうやつは噂好きなんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "まあ、昔から交易を\x01",
            "しておった民じゃからかのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BFB")

    Jump("loc_1E3C")

    label("loc_1C00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1D1B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CC4")

    #C0100
    ChrTalk(
        0xFE,
        (
            "クロスベルには昔から\x01",
            "ルバーチェ商会という連中がおる。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        "……いわゆるマフィアじゃな。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "悲しいことに警察にも\x01",
            "取り締まる事ができんのじゃ。\x01",
            "関わらん方がええぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D16")

    label("loc_1CC4")


    #C0103
    ChrTalk(
        0xFE,
        (
            "ルバーチェ商会は警察も\x01",
            "ろくに取り締まる事ができん。\x01",
            "……関わらん方がええぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D16")

    Jump("loc_1E3C")

    label("loc_1D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_1E3C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DE8")

    #C0104
    ChrTalk(
        0xFE,
        (
            "百貨店の新装に\x01",
            "新しいオーバルストア……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "クロスベルの街並みは\x01",
            "どんどん新しくなっていくのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "良い事とは思うが、\x01",
            "こうも目まぐるしくては\x01",
            "迷子になってしまいそうじゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E3C")

    label("loc_1DE8")


    #C0107
    ChrTalk(
        0xFE,
        (
            "こうも街並みが変わると\x01",
            "クロスベル育ちのワシでも\x01",
            "迷子になってしまいそうじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E3C")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_1_E3B end

    def Function_2_1E44(): pass

    label("Function_2_1E44")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1ED8")

    #C0108
    ChrTalk(
        0xFE,
        (
            "さっき空港のほうから\x01",
            "警察官が引き揚げて行ったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "爆発物がどうとか\x01",
            "話していたらしいけど……\x01",
            "ううむ、やはり物騒だなぁ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A8F")

    label("loc_1ED8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1FB0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F5B")

    #C0110
    ChrTalk(
        0xFE,
        (
            "警察の車両が慌てて\x01",
            "空港のほうに向かっていったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "何かあったんだろうか。\x01",
            "いやな感じだねぇ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1FAB")

    label("loc_1F5B")


    #C0112
    ChrTalk(
        0xFE,
        (
            "警察が慌てているなんて\x01",
            "ろくな事じゃないに決まってる。\x01",
            "いやな感じだねぇ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FAB")

    Jump("loc_2A8F")

    label("loc_1FB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_206F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2026")

    #C0113
    ChrTalk(
        0xFE,
        "港湾区の事件……聞いたかい？\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "……子供をあまり遠くに\x01",
            "行かせないようにしないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_206A")

    label("loc_2026")


    #C0115
    ChrTalk(
        0xFE,
        (
            "ミミ、物騒だから\x01",
            "あまり父さんのそばから\x01",
            "離れるんじゃないぞー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_206A")

    Jump("loc_2A8F")

    label("loc_206F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_207D")
    Jump("loc_2A8F")

    label("loc_207D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2127")

    #C0116
    ChrTalk(
        0xFE,
        (
            "導力車が普及してきた今、\x01",
            "道路の整備に積極的に\x01",
            "取り組むべきだと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xFE,
        (
            "特に中央広場は人通りも多いし、\x01",
            "予算が割けるなら\x01",
            "道路の拡張をして欲しいよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A8F")

    label("loc_2127")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_225D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2204")
    TurnDirection(0xFE, 0x153, 0)

    #C0118
    ChrTalk(
        0xFE,
        (
            "おや、キミは……\x01",
            "特務支援課の子なのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "よかったらうちのミミとも\x01",
            "仲良くしてやってくれな。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x153,
        "#1109Fうん、いいよー！\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x101,
        (
            "#0002F（この馴染みの早さは\x01",
            "  天性のものだなぁ……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2258")

    label("loc_2204")

    TurnDirection(0xFE, 0x153, 0)

    #C0122
    ChrTalk(
        0xFE,
        (
            "君、ウチのミミとも歳は近いんだろう？\x01",
            "よかったら仲良くしてやってくれな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2258")

    Jump("loc_2A8F")

    label("loc_225D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_22F2")

    #C0123
    ChrTalk(
        0xFE,
        (
            "記念祭中は市内の\x01",
            "交通マナーが気がかりだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xFE,
        (
            "導力車でクロスベルに来る\x01",
            "観光客もいるだろうし、\x01",
            "迷惑行為が起きなきゃいいけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A8F")

    label("loc_22F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_23FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23A8")

    #C0125
    ChrTalk(
        0xFE,
        (
            "マスコミ関係の人って\x01",
            "アルカンシェルのプレ公演に\x01",
            "招かれるらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "一足先に新作の舞台を\x01",
            "堪能できるわけか……\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        "ちょっと羨ましいよね、ははは。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_23F6")

    label("loc_23A8")


    #C0128
    ChrTalk(
        0xFE,
        (
            "もうすぐプレ公演かあ……\x01",
            "観れないと分かっていても\x01",
            "ワクワクしちゃうねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23F6")

    Jump("loc_2A8F")

    label("loc_23FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_244A")
    TurnDirection(0xFE, 0xB, 0)

    #C0129
    ChrTalk(
        0xFE,
        (
            "おーい、ミミ。\x01",
            "暗くなってきたから\x01",
            "そろそろ帰るぞ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A8F")

    label("loc_244A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2521")

    #C0130
    ChrTalk(
        0xFE,
        (
            "アルカンシェルの新作、\x01",
            "『金の太陽、銀の月』だったっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "あのイリア・プラティエが\x01",
            "また見られるなんて、楽しみだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "まあチケットは買えなかったから……\x01",
            "写真集で楽しむ事になりそうだけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A8F")

    label("loc_2521")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2654")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25D5")

    #C0133
    ChrTalk(
        0xFE,
        (
            "アルカンシェル公演のチケット、\x01",
            "僕も手に入れられなかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "百貨店は長蛇の列だったし、\x01",
            "他の販売店ではあっという間に\x01",
            "売り切れたそうからねぇ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_264F")

    label("loc_25D5")


    #C0135
    ChrTalk(
        0xFE,
        (
            "ミミにイリア・プラティエの演技を\x01",
            "見せてあげたかったけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "仕方ない、再来月あたりに\x01",
            "もう一度当たってみようか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_264F")

    Jump("loc_2A8F")

    label("loc_2654")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_273C")

    #C0137
    ChrTalk(
        0xFE,
        (
            "導力車の運転手になるには、\x01",
            "役所で正式な手続きを踏めばいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "だけど、いまいち運転が\x01",
            "上手くない人も多くてね。\x01",
            "接触事故もたびたび起こってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "免許の交付には、もう少し\x01",
            "厳格に基準を設けるべきだと思うよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A8F")

    label("loc_273C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2865")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27DB")

    #C0140
    ChrTalk(
        0xFE,
        (
            "君たち……もしかして\x01",
            "導力車に送ってもらったのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "いや、少し羨ましいなと思ってさ。\x01",
            "ははは……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2860")

    label("loc_27DB")


    #C0143
    ChrTalk(
        0xFE,
        (
            "さっきの導力車は\x01",
            "共和国のヴェルヌ社製だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "たしか一番手ごろな値段の\x01",
            "タイプだったと思うけど……\x01",
            "やっぱり車はいいよなぁ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2860")

    Jump("loc_2A8F")

    label("loc_2865")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_29BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_294D")

    #C0145
    ChrTalk(
        0xFE,
        (
            "導力車の普及に伴って、\x01",
            "違法駐車が隠れた問題になってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "路肩に置かれたら後続の車両や\x01",
            "通行人に大変な迷惑がかかるだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "道路はみんなのものだから、\x01",
            "きちんとルールを守って使って欲しいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_29B8")

    label("loc_294D")


    #C0148
    ChrTalk(
        0xFE,
        "違法駐車が問題になってるんだ。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "道路はみんなのものだから、\x01",
            "きちんとルールを守って使って欲しいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29B8")

    Jump("loc_2A8F")

    label("loc_29BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_2A4D")

    #C0150
    ChrTalk(
        0xFE,
        (
            "僕は都市整備課にいてね、\x01",
            "交通量の調査を担当しているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        (
            "……と言っても、今日は完全オフ。\x01",
            "娘と一緒に遊びに来てるのさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A8F")

    label("loc_2A4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_2A8F")

    #C0152
    ChrTalk(
        0xFE,
        (
            "ここはクロスベルでも\x01",
            "一番人通りが多い広場なんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A8F")

    TalkEnd(0xFE)
    Return()

    # Function_2_1E44 end

    def Function_3_2A93(): pass

    label("Function_3_2A93")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2B0A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AED")

    #C0153
    ChrTalk(
        0xFE,
        "夕日がきれいだね。\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        "お父さんとおうちにかえろっと。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2B05")

    label("loc_2AED")


    #C0155
    ChrTalk(
        0xFE,
        "子供は帰る時間っ。\x02",
    )

    CloseMessageWindow()

    label("loc_2B05")

    Jump("loc_38C8")

    label("loc_2B0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2CE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CA9")

    #C0156
    ChrTalk(
        0xFE,
        "おはよー、ロイドくんたち！\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        "今日もとくむしえんかのお仕事なの？\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        (
            "#0000Fああ、ちょっとね。\x01",
            "……それにしても……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x104,
        (
            "#0300Fはは、やっと俺たちのことを\x01",
            "きちんと覚えてくれたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "えー？\x01",
            "ミミ、今まで一度だって\x01",
            "間違えたことないよー？\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x102,
        (
            "#0100Fう、うーん。\x01",
            "まぁそういうことに\x01",
            "しておきましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x103,
        "#0202F車に気をつけて遊ぶんですよ。\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        "うん！　みんなもお仕事がんばってね！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2CDC")

    label("loc_2CA9")


    #C0164
    ChrTalk(
        0xFE,
        (
            "とくむしえんかのみんな、\x01",
            "お仕事がんばってね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CDC")

    Jump("loc_38C8")

    label("loc_2CE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2D61")

    #C0165
    ChrTalk(
        0xFE,
        (
            "今日はなんだかお父さんが\x01",
            "きびしいなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xFE,
        (
            "でも、ミミのことを想ってのことだから、\x01",
            "ミミは言うこと聞くよー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C8")

    label("loc_2D61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_2D6F")
    Jump("loc_38C8")

    label("loc_2D6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2DD4")

    #C0167
    ChrTalk(
        0xFE,
        (
            "今日はキーアちゃん\x01",
            "一緒じゃないのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        "ちぇっ、遊んでもらおうとおもったのに。\x02",
    )

    CloseMessageWindow()
    Jump("loc_38C8")

    label("loc_2DD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2FDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F99")
    TurnDirection(0xFE, 0x153, 0)

    #C0169
    ChrTalk(
        0xFE,
        "あれ、しらない子だ……\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xFE,
        (
            "いいなー、ロイドくんたちに\x01",
            "遊んでもらってるのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x153,
        "#1104Fえへへ、いーでしょ！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EA4")

    #C0172
    ChrTalk(
        0x102,
        "#0106F遊んでいるわけじゃないんだけど……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F15")

    label("loc_2EA4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EE7")

    #C0173
    ChrTalk(
        0x103,
        "#0206F遊んでいるわけではないのですが……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F15")

    label("loc_2EE7")


    #C0174
    ChrTalk(
        0x104,
        "#0306F遊んでるわけじゃねえんだけどなぁ。\x02",
    )

    CloseMessageWindow()

    label("loc_2F15")


    #C0175
    ChrTalk(
        0x101,
        (
            "#0006Fうーん、でもこの１週間は確かに……\x02\x03",

            "キーアといるとつい楽しくて\x01",
            "遊んでしまってたからなぁ……\x01",
            "……気を付けないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2FD9")

    label("loc_2F99")


    #C0176
    ChrTalk(
        0xFE,
        "ね、今度あたしとも遊んでよー。\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x153,
        "#1109Fえへへ、いーよ！\x02",
    )

    CloseMessageWindow()

    label("loc_2FD9")

    Jump("loc_38C8")

    label("loc_2FDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_305E")

    #C0178
    ChrTalk(
        0xFE,
        (
            "あそこにいるお姉さん、\x01",
            "お祭りで出店を出すんだって～。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "ミミ、ポップコーン食べたことないの。\x01",
            "たのしみ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C8")

    label("loc_305E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_30F1")

    #C0180
    ChrTalk(
        0xFE,
        (
            "お父さんも街のみんなも、\x01",
            "来月のお祭りのことが気になるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "いろんな面白い事が\x01",
            "盛りだくさんだもんね！\x01",
            "ミミもたのしみ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C8")

    label("loc_30F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_3127")

    #C0182
    ChrTalk(
        0xFE,
        "え～っ、もうちょっと遊びたいよう！\x02",
    )

    CloseMessageWindow()
    Jump("loc_38C8")

    label("loc_3127")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_31C8")

    #C0183
    ChrTalk(
        0xFE,
        (
            "お父さん、アルカンシェルのチケット\x01",
            "とりそこねちゃったんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "まぁ、仕方ないよね、\x01",
            "人気のぶたいなんだし。\x01",
            "ミミ、全然気にしてないよー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C8")

    label("loc_31C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3400")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_339A")

    #C0185
    ChrTalk(
        0xFE,
        (
            "あ、ロイドくんたちだ。\x01",
            "こんにちは～！\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x101,
        (
            "#0000Fこんにちは。\x01",
            "はは、最近やっと名前を\x01",
            "覚えてくれたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "覚えてるよ～。\x01",
            "とくむしね#2R・#んかの\x01",
            "ロイドくんたち！\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x102,
        (
            "#0106Fう、うーん、\x01",
            "まだ『特務支援課』までは\x01",
            "覚えてないかぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x103,
        (
            "#0200F……と、いいますか……\x01",
            "名前もロイドさんしか\x01",
            "覚えられてないんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x104,
        (
            "#0303Fぬぅぅ……やるなロイド。\x01",
            "この俺を差し置いて\x01",
            "レディに自分を印象づけるとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x101,
        "#0011Fな、何の話をしてるんだよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_33FB")

    label("loc_339A")


    #C0192
    ChrTalk(
        0xFE,
        (
            "とくむしね#2R・#んかのみんな、\x01",
            "今日は何のお仕事？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        "ミミ、応援してるからがんばってねー。\x02",
    )

    CloseMessageWindow()

    label("loc_33FB")

    Jump("loc_38C8")

    label("loc_3400")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3452")

    #C0194
    ChrTalk(
        0xFE,
        "今日もいい天気だね～。\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        "車に気を付けていってらっしゃーい！\x02",
    )

    CloseMessageWindow()
    Jump("loc_38C8")

    label("loc_3452")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_358B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3528")

    #C0196
    ChrTalk(
        0xFE,
        (
            "あ、とくむ……\x01",
            "………ナントカのお兄ちゃんたち！\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0xFE,
        (
            "おつかれさまー！\x01",
            "お仕事がんばってね～！\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x101,
        "#0002Fはは、ありがとう。\x02",
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        (
            "#0106F（中々名前までは\x01",
            "  覚えてもらえないわねぇ……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3586")

    label("loc_3528")


    #C0200
    ChrTalk(
        0xFE,
        (
            "お父さん、\x01",
            "導力車を買うのがユメなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "よく車のカタログをみて\x01",
            "研究してるんだ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3586")

    Jump("loc_38C8")

    label("loc_358B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_373A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36FC")

    #C0202
    ChrTalk(
        0xFE,
        "あ、こんにちは！\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x101,
        "#0000Fやぁ、こんにちは。\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "え～っと……\x01",
            "とくむ……とくむ……\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x103,
        (
            "#0200F……特務支援課です。\x01",
            "まぁ、耳慣れない言葉でしょうけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "とくむしぇーんか、ね！\x01",
            "ミミ覚えた～！\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        "今日もお仕事がんばってね～。\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x102,
        "#0106Fび、微妙に違うけど……\x02",
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x104,
        (
            "#0300Fまぁ、まだ１ヶ月ちょっとだ。\x01",
            "徐々に覚えてもらえればいいだろ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3735")

    label("loc_36FC")


    #C0210
    ChrTalk(
        0xFE,
        (
            "とくむしぇーんかさん、\x01",
            "今日もお仕事がんばってね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3735")

    Jump("loc_38C8")

    label("loc_373A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_37B7")

    #C0211
    ChrTalk(
        0xFE,
        (
            "ぷっぷー、ぷっぷー……\x01",
            "車たくさん通ったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "知ってる？\x01",
            "ここってクロスベルで\x01",
            "一番よく車が通るんだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_38C8")

    label("loc_37B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_38C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_386A")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0213
    ChrTalk(
        0xFE,
        (
            "あっ、こんにちは！\x01",
            "観光客の人～？\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "えっ、違うの？\x01",
            "ざんねん～……\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "ミミがクロスベルを\x01",
            "案内してあげようと思ったのに～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_38C8")

    label("loc_386A")


    #C0216
    ChrTalk(
        0xFE,
        (
            "ミミ、将来\x01",
            "ガイドさんになるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "そのときはミミが\x01",
            "クロスベルを案内してあげるね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38C8")

    TalkEnd(0xFE)
    Return()

    # Function_3_2A93 end

    def Function_4_38CC(): pass

    label("Function_4_38CC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_395C")

    #C0218
    ChrTalk(
        0xFE,
        (
            "……あんたね……\x01",
            "せっかく走りこみしてんのに\x01",
            "今食べちゃ意味ないでしょ。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "はぁ～あ、こんなことなら\x01",
            "褒めなきゃよかった。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F69")

    label("loc_395C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_39D6")

    #C0220
    ChrTalk(
        0xFE,
        "あ……なんか顔が細くなってきたかも。\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "うんうん、ダイエット\x01",
            "よくがんばってんじゃん。\x01",
            "えらいえらい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F69")

    label("loc_39D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3A49")

    #C0222
    ChrTalk(
        0xFE,
        (
            "あー、やっぱ\x01",
            "百貨店での買い食いは\x01",
            "至福の時だわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "もぐもぐ……\x01",
            "なによ、恨めしそうな顔して。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F69")

    label("loc_3A49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3AC3")

    #C0224
    ChrTalk(
        0xFE,
        (
            "……最近太ったって言われない？\x01",
            "あんた、顔が丸いわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "ダイエットサボるから\x01",
            "こんなことになんのよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F69")

    label("loc_3AC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3B39")

    #C0226
    ChrTalk(
        0xFE,
        (
            "あれ？\x01",
            "あんたそれ何食べてんの？\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "一緒にダイエットしようって言ったのに\x01",
            "間食してちゃだめじゃん。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F69")

    label("loc_3B39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_3B8F")

    #C0228
    ChrTalk(
        0xFE,
        "あたしたちも付き合い長いよね。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        "なんか、浮いた話とかないわけ？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F69")

    label("loc_3B8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3BD7")

    #C0230
    ChrTalk(
        0xFE,
        "そういえば記念祭が近いよね。\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        "あんた予定あんの？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F69")

    label("loc_3BD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_3C64")

    #C0232
    ChrTalk(
        0xFE,
        (
            "あっ、そういえば……\x01",
            "アルカンシェルのチケットって\x01",
            "とっくに発売してたんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "完全に忘れちゃってた。\x01",
            "さいあく……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F69")

    label("loc_3C64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_3CD8")

    #C0234
    ChrTalk(
        0xFE,
        (
            "こないだ、ＩＢＣの総裁さんの\x01",
            "リムジン見たよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "あの人もすっごくダンディよね。\x01",
            "タイプだわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F69")

    label("loc_3CD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3D33")

    #C0236
    ChrTalk(
        0xFE,
        "今日どこ行く？\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "百貨店でウィンドウショッピング\x01",
            "って気分でもないし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F69")

    label("loc_3D33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_3D9F")

    #C0238
    ChrTalk(
        0xFE,
        "アリオス様、また出張らしいよ。\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0xFE,
        (
            "また少しの間\x01",
            "あのお姿を見られないのね……\x01",
            "ざんねん。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F69")

    label("loc_3D9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3E0D")

    #C0240
    ChrTalk(
        0xFE,
        (
            "導力車を持ってる人って\x01",
            "憧れちゃうよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xFE,
        (
            "どこへでも連れてって\x01",
            "もらえちゃうんだから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F69")

    label("loc_3E0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3E8B")

    #C0242
    ChrTalk(
        0xFE,
        (
            "なんか魔獣が町や村に\x01",
            "入り込む事件が起こってるんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "もー、怖いよね。\x01",
            "警備隊とかって何してんだろ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F69")

    label("loc_3E8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3F06")

    #C0244
    ChrTalk(
        0xFE,
        (
            "それにしても、\x01",
            "クロスベルタイムズの\x01",
            "あの写真見た？\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0xFE,
        (
            "アリオス様、やっぱり\x01",
            "ダンディでかっこいいよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F69")

    label("loc_3F06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_3F69")

    #C0246
    ChrTalk(
        0xFE,
        (
            "アリオス様、また\x01",
            "お手柄だったらしいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xFE,
        (
            "あたしもアリオス様に\x01",
            "助け出された～い！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F69")

    TalkEnd(0xFE)
    Return()

    # Function_4_38CC end

    def Function_5_3F6D(): pass

    label("Function_5_3F6D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4003")

    #C0248
    ChrTalk(
        0xFE,
        (
            "だ、だってだって！\x01",
            "痩せてきてるっていうから\x01",
            "ちょっとくらい、いいかな～って……\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xFE,
        (
            "あ～ん、見捨てないで～！\x01",
            "また頑張るから～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F4")

    label("loc_4003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_40B3")
    OP_4B(0xC, 0xFF)

    #C0250
    ChrTalk(
        0xFE,
        (
            "そ、そうかな～。\x01",
            "自分ではよく分からないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xFE,
        (
            "走りこみの成果は現れてるってことね！\x01",
            "よぉ～し……！\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xC,
        "（ま、やる気が出るなら嘘も方便よね。）\x02",
    )

    CloseMessageWindow()
    OP_4C(0xC, 0xFF)
    Jump("loc_46F4")

    label("loc_40B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_4158")

    #C0253
    ChrTalk(
        0xFE,
        (
            "あ～ん、ずるいずるい！\x01",
            "あたしダイエット中なのに\x01",
            "見せ付けるように……！\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0xFE,
        (
            "……ね、ちょっとだけちょうだ～い！\x01",
            "朝走りこんだごほうびってことで！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F4")

    label("loc_4158")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_4166")
    Jump("loc_46F4")

    label("loc_4166")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_41C8")

    #C0255
    ChrTalk(
        0xFE,
        (
            "ひど～い！\x01",
            "他人事みたいに……\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0xFE,
        (
            "今日からダイエットするから\x01",
            "手伝ってよ～……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F4")

    label("loc_41C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4231")

    #C0257
    ChrTalk(
        0xFE,
        (
            "もぐもぐ……だって、\x01",
            "１日２食とか無理じゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xFE,
        "大丈夫よ、明日から頑張るから～。\x02",
    )

    CloseMessageWindow()
    Jump("loc_46F4")

    label("loc_4231")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4288")

    #C0259
    ChrTalk(
        0xFE,
        (
            "そんな話あったら\x01",
            "女２人でばっかり遊んでないでしょ。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xFE,
        "……はぁ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_46F4")

    label("loc_4288")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_42CB")

    #C0261
    ChrTalk(
        0xFE,
        (
            "ん～、いつも通りブラブラ\x01",
            "出店を回るだけかな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F4")

    label("loc_42CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_4375")

    #C0262
    ChrTalk(
        0xFE,
        "ま、どーせすぐ売り切れだって。\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xFE,
        (
            "アルカンシェルのチケットって\x01",
            "いっつも即完売しちゃうんだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0xFE,
        (
            "並ぶ時間かかんなかっただけ\x01",
            "ラッキーと思おうよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F4")

    label("loc_4375")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_43F7")

    #C0265
    ChrTalk(
        0xFE,
        (
            "アリオスさんといい、\x01",
            "ディーターさんといい……\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xFE,
        (
            "あんたってばほんと、\x01",
            "かっこいいオジさんに目がないわよね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F4")

    label("loc_43F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_446E")

    #C0267
    ChrTalk(
        0xFE,
        "どっかでお茶でもする～？\x02",
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xFE,
        (
            "……と思ったけど、あたし金欠なのよね。\x01",
            "やっぱり百貨店見て回ろうよ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F4")

    label("loc_446E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_44F6")

    #C0269
    ChrTalk(
        0xFE,
        (
            "アリオスさんが人気なのは分かるけど、\x01",
            "出張ばっかよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "警察は頼りないし、\x01",
            "クロスベルにずっと居ればいいのに～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F4")

    label("loc_44F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4577")

    #C0271
    ChrTalk(
        0xFE,
        (
            "でも導力車って\x01",
            "すっごい高いんでしょ？\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xFE,
        (
            "よっぽどお金持ちの男でも\x01",
            "捕まればいいけど、\x01",
            "現実は厳しいわよね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F4")

    label("loc_4577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_4608")

    #C0273
    ChrTalk(
        0xFE,
        (
            "まぁ、クロスベル市なら\x01",
            "そんな事件起こんないだろうし、\x01",
            "安心していいんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xFE,
        (
            "何ていっても、\x01",
            "遊撃士協会があるんだし～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F4")

    label("loc_4608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_4672")

    #C0275
    ChrTalk(
        0xFE,
        "見た見た～。\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0xFE,
        (
            "後ろで立ち尽くしてる\x01",
            "警察の人がなんだか\x01",
            "オマケみたいだったわよね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46F4")

    label("loc_4672")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_46F4")

    #C0277
    ChrTalk(
        0xFE,
        (
            "なんか、警察の人も\x01",
            "アリオス様の手伝いを\x01",
            "したらしいじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "ふふ、結局お手柄を\x01",
            "横取りし損ねたみたいだけど～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46F4")

    TalkEnd(0xFE)
    Return()

    # Function_5_3F6D end

    def Function_6_46F8(): pass

    label("Function_6_46F8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4847")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47B9")

    #C0279
    ChrTalk(
        0xFE,
        (
            "風船を渡した瞬間の\x01",
            "子供の笑顔ときたら……\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0xFE,
        (
            "うん、なかなかどうして\x01",
            "やりがいのある仕事だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "将来は風船おじさんなんて呼ばれて\x01",
            "子供たちに慕われたいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4842")

    label("loc_47B9")


    #C0282
    ChrTalk(
        0xFE,
        (
            "子供たちの笑顔も見れるし、\x01",
            "なかなかどうして\x01",
            "やりがいのある仕事だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        (
            "将来は風船おじさんなんて呼ばれて\x01",
            "子供たちに慕われたいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4842")

    Jump("loc_5166")

    label("loc_4847")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4968")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48F7")

    #C0284
    ChrTalk(
        0xFE,
        "風船、風船はいかが～。\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xFE,
        (
            "風船は、人ごみに\x01",
            "無理矢理持ち込まないように\x01",
            "注意してくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        (
            "たかがゴムだから、\x01",
            "ぶつけたら簡単に割れちゃうぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4963")

    label("loc_48F7")


    #C0287
    ChrTalk(
        0xFE,
        (
            "風船は所詮ゴムだから、\x01",
            "ぶつけたら簡単に割れちゃうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        (
            "あの破裂音には\x01",
            "いまだに馴れないんだよな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4963")

    Jump("loc_5166")

    label("loc_4968")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_49F6")

    #C0289
    ChrTalk(
        0xFE,
        (
            "風船を手に取れば\x01",
            "たちまち気分が落ち着くぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        (
            "見てくれよ、この間抜けなフォルム。\x01",
            "小さいことで悩んでても笑えてくるよな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5166")

    label("loc_49F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 6)), scpexpr(EXPR_END)), "loc_4A04")
    Jump("loc_5166")

    label("loc_4A04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4A98")

    #C0291
    ChrTalk(
        0xFE,
        "風船、風船はどうだい？\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xFE,
        (
            "おっと、今日はあの元気のいい\x01",
            "女の子は一緒じゃないのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "たまに遊んでやらなきゃ\x01",
            "スネちまうぞ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5166")

    label("loc_4A98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_4BB7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B81")

    #C0294
    ChrTalk(
        0xFE,
        (
            "おっとお嬢ちゃん、\x01",
            "風船はどうだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        "ハハハ、好きだろ風船。\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x153,
        "#1111Fん～……別に？\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        "う、うそ……？\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "なんだよ、子供なんて\x01",
            "みんな風船好きだろ普通～……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        "#0006F（なんだよその偏見……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4BB2")

    label("loc_4B81")


    #C0300
    ChrTalk(
        0xFE,
        (
            "……子供なんて\x01",
            "みんな風船好きだろ普通～……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4BB2")

    Jump("loc_5166")

    label("loc_4BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4C24")

    #C0301
    ChrTalk(
        0xFE,
        (
            "風船にガスを入れるのは\x01",
            "人が見てないスキにやんないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        "じゃなきゃ、夢が壊れるだろ？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5166")

    label("loc_4C24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4D46")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CEA")

    #C0303
    ChrTalk(
        0xFE,
        (
            "ガスは空気よりも軽い。\x01",
            "だから風船は優雅に飛ぶわけだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0xFE,
        (
            "……おっと、この辺りでは\x01",
            "火気に気を付けてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0xFE,
        (
            "ガスに引火したら爆発して\x01",
            "飛んでっちゃうぜ、俺が。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4D41")

    label("loc_4CEA")


    #C0306
    ChrTalk(
        0xFE,
        "火気には充分気を付けてくれよ。\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "俺は別に風船みたいに\x01",
            "飛んだりしたくないしな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D41")

    Jump("loc_5166")

    label("loc_4D46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_END)), "loc_4D9A")

    #C0308
    ChrTalk(
        0xFE,
        "ん、今日はこんなところかね。\x02",
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0xFE,
        "このバイトもラクじゃないな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5166")

    label("loc_4D9A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4E2A")

    #C0310
    ChrTalk(
        0xFE,
        (
            "今やどこにでも導力器があるから\x01",
            "ガスを使う機器もほとんど見ない。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0xFE,
        (
            "風船配りはガスを有効に使う\x01",
            "数少ない方法だと思わないか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5166")

    label("loc_4E2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4E87")

    #C0312
    ChrTalk(
        0xFE,
        "風船、風船だよ～。\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0xFE,
        (
            "うっかり手を離して\x01",
            "飛ばさないように気をつけてな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5166")

    label("loc_4E87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4F01")

    #C0314
    ChrTalk(
        0xFE,
        (
            "うっし、今日も張り切って\x01",
            "風船配りするか。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0xFE,
        (
            "中央広場って、午前中から\x01",
            "観光客なんかで賑わうからなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5166")

    label("loc_4F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4F68")

    #C0316
    ChrTalk(
        0xFE,
        "お兄さんたちも風船はいかが？\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0xFE,
        (
            "観光客じゃなくてもいいっすよ。\x01",
            "意外と適当なんで。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5166")

    label("loc_4F68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_5005")

    #C0318
    ChrTalk(
        0xFE,
        (
            "観光業はクロスベルの\x01",
            "主要産業の１つに認められててな。\x01",
            "市から補助予算も下りてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0xFE,
        (
            "風船配りは観光を盛り上げる\x01",
            "大切な仕事なんだぜ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5166")

    label("loc_5005")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_5116")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50B3")

    #C0320
    ChrTalk(
        0xFE,
        "風船はいかが～？\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xFE,
        (
            "……ああ、別にお祭りって\x01",
            "わけじゃないんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0xFE,
        (
            "風船はいつも配ってるんだよ。\x01",
            "クロスベル人は\x01",
            "華やかなのが好きなのさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_5111")

    label("loc_50B3")


    #C0323
    ChrTalk(
        0xFE,
        (
            "クロスベル人は騒いだり\x01",
            "華やかなのが好きなのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0xFE,
        (
            "さあさあ\x01",
            "遠慮せず受け取ってくれよ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5111")

    Jump("loc_5166")

    label("loc_5116")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_5166")

    #C0325
    ChrTalk(
        0xFE,
        "風船はいかが～？\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0xFE,
        (
            "観光客の方には\x01",
            "無料でお配りしておりま～す！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5166")

    TalkEnd(0xFE)
    Return()

    # Function_6_46F8 end

    def Function_7_516A(): pass

    label("Function_7_516A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5291")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5229")

    #C0327
    ChrTalk(
        0xFE,
        (
            "さて、出店の場所の\x01",
            "下見は終わったし……\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xFE,
        (
            "折角だから、\x01",
            "少し観光して帰ろうかしらね。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0xFE,
        (
            "何しろ、記念祭が始まったら\x01",
            "観光してるヒマなんてないでしょうし。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_528C")

    label("loc_5229")


    #C0330
    ChrTalk(
        0xFE,
        "さて、どこを観光してみようかしら。\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0xFE,
        (
            "って言っても日帰りだから\x01",
            "あまり遠くにいけないけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_528C")

    Jump("loc_536D")

    label("loc_5291")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_536D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5309")

    #C0332
    ChrTalk(
        0xFE,
        (
            "来月の記念祭で、\x01",
            "ポップコーンの出店を出すのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0xFE,
        "ふふ、いい場所が取れてよかったわ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_536D")

    label("loc_5309")


    #C0334
    ChrTalk(
        0xFE,
        (
            "来月の記念祭で、\x01",
            "ポップコーンの出店を出すのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0xFE,
        (
            "今日は下見に来てたの。\x01",
            "来月はよろしくね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_536D")

    TalkEnd(0xFE)
    Return()

    # Function_7_516A end

    def Function_8_5371(): pass

    label("Function_8_5371")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_5382")
    Jump("loc_6868")

    label("loc_5382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_5481")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5428")
    OP_93(0xFE, 0xC5, 0x0)

    #C0336
    ChrTalk(
        0xFE,
        (
            "ピッピー、ピッピーッ！\x01",
            "導力車は徐行してくださ～い。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)

    #C0337
    ChrTalk(
        0xFE,
        (
            "……今日は少し\x01",
            "交通量が少ない気がするけど……\x01",
            "気のせいかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_547C")

    label("loc_5428")


    #C0338
    ChrTalk(
        0xFE,
        (
            "私、毎日交通整理してるけど\x01",
            "今日は少し街が寂しい気がするわね。\x01",
            "気のせいかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_547C")

    Jump("loc_6868")

    label("loc_5481")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_548F")
    Jump("loc_6868")

    label("loc_548F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_549D")
    Jump("loc_6868")

    label("loc_549D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_57E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_572E")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0339
    ChrTalk(
        0xFE,
        "あ……ロイド君じゃない！\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xFE,
        (
            "ねえちょっと、危ない事に\x01",
            "なってるって聞いたわよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x101,
        (
            "#0008Fすみませんケイト先輩、\x01",
            "心配を掛けまして。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_55AC")

    #C0342
    ChrTalk(
        0x102,
        (
            "#0100Fこちらはもう大丈夫です。\x02\x03",

            "それより……\x01",
            "最近の街の様子はどうですか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5668")

    label("loc_55AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_5609")

    #C0343
    ChrTalk(
        0x103,
        (
            "#0200Fこちらはもう大丈夫です。\x02\x03",

            "それより……\x01",
            "最近の街の様子はどうですか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5668")

    label("loc_5609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_5668")

    #C0344
    ChrTalk(
        0x104,
        (
            "#0300Fま、こっちは\x01",
            "もう大丈夫だけどな。\x02\x03",

            "それより……\x01",
            "最近の街の様子はどうスか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5668")


    #C0345
    ChrTalk(
        0xFE,
        (
            "街の方は静かなものね。\x01",
            "記念祭の熱が引いて\x01",
            "張り合いが無いくらい。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xFE,
        "トラブルが減ったのは嬉しいけど。\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x101,
        (
            "#0003Fそうですか……\x01",
            "（あれからルバーチェも\x01",
            "  鳴りを潜めているって事か……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB2, 0)
    Jump("loc_57E3")

    label("loc_572E")


    #C0348
    ChrTalk(
        0xFE,
        "この１週間、街の方は静かなものよ。\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0xFE,
        (
            "記念祭の熱が引いて\x01",
            "張り合いが無いくらいかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xFE,
        (
            "それより支援課の事が心配で\x01",
            "気が気じゃなかったわよ。\x01",
            "あんまり危ない真似、しないでね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57E3")

    Jump("loc_6868")

    label("loc_57E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_59A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5926")

    #C0351
    ChrTalk(
        0xFE,
        (
            "くうう……今朝も\x01",
            "違法駐車の車を見つけたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0xFE,
        (
            "もう、昨日ロイド君たちに\x01",
            "どけてもらったばかりなのに～。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x101,
        "#0000Fはは、そうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x104,
        (
            "#0300Fまあ違法駐車なんて\x01",
            "そんなもんだと思うが。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xFE,
        "でも、何か悔しくない？\x02",
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0xFE,
        (
            "私は悔しいな。\x01",
            "だから持ち主に\x01",
            "きつく言いつけてやるの！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_59A2")

    label("loc_5926")


    #C0357
    ChrTalk(
        0xFE,
        (
            "違法駐車だって犯罪だもの。\x01",
            "悪い癖は直さなくちゃいけないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0xFE,
        (
            "何事も小さな一歩から！\x01",
            "きつく言いつけてやらなくちゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_59A2")

    Jump("loc_6868")

    label("loc_59A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_5AD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A85")
    OP_93(0xFE, 0xC5, 0x0)

    #C0359
    ChrTalk(
        0xFE,
        (
            "ピッピー、ピッピーッ！\x01",
            "導力車は徐行してくださ～い。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 0)

    #C0360
    ChrTalk(
        0xFE,
        (
            "警察の仕事は\x01",
            "地道な努力の積み重ねよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xFE,
        (
            "よし、ロイド君たち。\x01",
            "今日もお互い頑張ろう！\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x101,
        "#0000Fはは、そうですね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5AD4")

    label("loc_5A85")


    #C0363
    ChrTalk(
        0xFE,
        (
            "警察の仕事は\x01",
            "地道な努力の積み重ねよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xFE,
        "よし、今日もお互い頑張ろう！\x02",
    )

    CloseMessageWindow()

    label("loc_5AD4")

    Jump("loc_6868")

    label("loc_5AD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_6245")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6115")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 0)), scpexpr(EXPR_END)), "loc_5D1E")

    #C0365
    ChrTalk(
        0xFE,
        (
            "あら、ロイド君たち。\x01",
            "また何かの捜査中なの？\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x101,
        "#0003Fええ、少し……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0367
    ChrTalk(
        0x101,
        (
            "#0000Fそうだ、ケイト先輩って\x01",
            "いつも市内を巡回してるんですよね。\x02\x03",

            "《銀》って言葉に\x01",
            "何か心当たりはありませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0xFE,
        (
            "……《銀》？\x01",
            "聞いたこと無いけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0369
    ChrTalk(
        0xFE,
        "ハッ、そういえば！\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0xFE,
        (
            "アルカンシェルの新作が\x01",
            "『金の太陽、銀の月』って\x01",
            "言うらしいわよ！\x02",
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

    #C0371
    ChrTalk(
        0x101,
        "#0006Fうーん、そうですか……\x02",
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0xFE,
        (
            "え、ええ。\x01",
            "役に立てなくてゴメンなさいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_610D")

    label("loc_5D1E")

    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0373
    ChrTalk(
        0xFE,
        "あ、ロイド君にランディさん！\x02",
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0xFE,
        (
            "さっきは交通整理の\x01",
            "手伝い、ありがとう～……\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0xFE,
        "……ではなくて。\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0xFE,
        (
            "ロイド捜査官以下\x01",
            "特務支援課殿、\x01",
            "ご協力感謝いたします！\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x101,
        (
            "#0002Fははは……\x01",
            "ケイト先輩、そんなに\x01",
            "形式張らなくても。\x02\x03",

            "こちらも時々\x01",
            "お世話になってるわけですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xFE,
        "ふふっ、それもそうね。\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xFE,
        (
            "それじゃ、また何かあったら\x01",
            "手を借りてもいいかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x104,
        (
            "#0304Fおー、何でも\x01",
            "気軽に呼びつけて下さいッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0xFE,
        "ありがとう、助かるわ。\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0xFE,
        (
            "……で、ロイド君たちは\x01",
            "また何かの捜査中なの？\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x101,
        "#0003Fええ、少し……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0384
    ChrTalk(
        0x101,
        (
            "#0000Fそうだ、ケイト先輩って\x01",
            "いつも市内を巡回してるんですよね。\x02\x03",

            "《銀》って言葉に\x01",
            "何か心当たりはありませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0xFE,
        (
            "……《銀》？\x01",
            "聞いたこと無いけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0386
    ChrTalk(
        0xFE,
        "ハッ、そういえば！\x02",
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0xFE,
        (
            "アルカンシェルの新作が\x01",
            "『金の太陽、銀の月』って\x01",
            "言うらしいわよ！\x02",
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

    #C0388
    ChrTalk(
        0x101,
        "#0006Fうーん、そうですか……\x02",
    )

    CloseMessageWindow()

    #C0389
    ChrTalk(
        0xFE,
        (
            "え、ええ。\x01",
            "役に立てなくてゴメンなさいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_610D")

    SetScenarioFlags(0x92, 1)
    Jump("loc_6240")

    label("loc_6115")


    #C0390
    ChrTalk(
        0xFE,
        (
            "《銀》……\x01",
            "特に心当たりは無いわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0xFE,
        (
            "うーん、ゴメンなさい。\x01",
            "役に立てないみたいで。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x43, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61D6")

    #C0392
    ChrTalk(
        0x101,
        (
            "#0000Fいえ、気にしないでください。\x01",
            "知り合いの弁護士を\x01",
            "訪ねてみるつもりなので。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6240")

    label("loc_61D6")


    #C0393
    ChrTalk(
        0x101,
        (
            "#0000Fいえ、こっちの方こそすみません。\x01",
            "一応手がかりみたいな物は\x01",
            "掴んだ所なので、気にしないで下さい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6240")

    Jump("loc_6868")

    label("loc_6245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_65F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x92, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6590")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_631C")

    #C0394
    ChrTalk(
        0xFE,
        (
            "あ、ロイド君にランディさん！\x01",
            "さっきは交通整理の\x01",
            "手伝い、ありがとう～……\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0xFE,
        "……ではなくて。\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xFE,
        (
            "ロイド捜査官以下\x01",
            "特務支援課殿、\x01",
            "ご協力感謝いたします！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6446")

    label("loc_631C")


    #C0397
    ChrTalk(
        0xFE,
        (
            "あ、ロイド君たち！\x01",
            "お仕事お疲れさま～。\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x101,
        (
            "#0000Fあ、ケイト先輩。\x01",
            "お疲れ様です。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x104,
        "#0300Fうっす、今朝はご指導どうもっす。\x02",
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xFE,
        (
            "そうそう、２人は今朝の\x01",
            "交通整理を手伝ってくれたのよね。\x01",
            "どうもありがとう～……\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xFE,
        "……ではなくて。\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xFE,
        (
            "ロイド捜査官以下\x01",
            "特務支援課殿、\x01",
            "ご協力感謝いたします！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6446")


    #C0403
    ChrTalk(
        0x101,
        (
            "#0002Fははは……\x01",
            "ケイト先輩、そんなに\x01",
            "形式張らなくても。\x02\x03",

            "こちらも時々\x01",
            "お世話になってるわけですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0xFE,
        "ふふっ、それもそうね。\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xFE,
        (
            "それじゃ、また何かあったら\x01",
            "手を借りてもいいかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x104,
        (
            "#0304Fおー、何でも\x01",
            "気軽に呼びつけて下さいッス。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0xFE,
        "ありがとう、助かるわ。\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0xFE,
        (
            "それじゃ、任務ご苦労様！\x01",
            "そちらも頑張ってね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x92, 0)
    Jump("loc_65EB")

    label("loc_6590")


    #C0409
    ChrTalk(
        0xFE,
        (
            "記念祭が近いせいかしら、\x01",
            "細かい事件が増えてるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xFE,
        "市内の巡回も気が抜けないわ。\x02",
    )

    CloseMessageWindow()

    label("loc_65EB")

    Jump("loc_6868")

    label("loc_65F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_6868")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_681B")
    OP_93(0xFE, 0xC5, 0x0)

    #C0411
    ChrTalk(
        0xFE,
        "ピッピー、ピッピーッ！\x02",
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xFE,
        (
            "導力車は徐行してください。\x01",
            "市民の安全に\x01",
            "ご協力をお願いしまーす！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6B, 7)), scpexpr(EXPR_END)), "loc_66E9")

    #C0413
    ChrTalk(
        0xFE,
        (
            "あらロイド君たち、\x01",
            "これから仕事？\x01",
            "導力車には気をつけてね！\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x101,
        "#0000Fはは、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    Jump("loc_6813")

    label("loc_66E9")


    #C0415
    ChrTalk(
        0xFE,
        (
            "あっ……ロイド君？\x01",
            "久しぶりね～！\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x101,
        (
            "#0000Fケイト先輩……\x01",
            "ご無沙汰しています、\x01",
            "警察学校ではお世話になりました。\x02\x03",

            "……今日はお仕事中ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xFE,
        (
            "ええ、私はよく\x01",
            "ここで交通整理をしているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xFE,
        (
            "ロイド君たちはこれから仕事？\x01",
            "導力車には気をつけてね！\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x101,
        "#0000Fはは、ありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6B, 7)

    label("loc_6813")

    SetScenarioFlags(0x1, 1)
    Jump("loc_6868")

    label("loc_681B")

    OP_93(0xFE, 0xC5, 0x0)

    #C0420
    ChrTalk(
        0xFE,
        (
            "導力車は徐行してください。\x01",
            "市民の安全に\x01",
            "ご協力をお願いしまーす！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6868")

    TalkEnd(0xFE)
    Return()

    # Function_8_5371 end

    def Function_9_686C(): pass

    label("Function_9_686C")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x1, 4)
    Call(1, 11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_68FE")

    #C0421
    ChrTalk(
        0x101,
        (
            "#0004F（そういえば……\x01",
            "  エサになりそうな物があったっけ。）\x02\x03",

            "#0000F（コッペにあげても\x01",
            "  いいかもしれないな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x52, 0)

    label("loc_68FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 0)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B7D")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6973")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B78")
    FadeToDark(300, 0, 100)
    MenuCmd(0, 1)
    MenuCmd(1, 1, "話をする")
    MenuCmd(1, 1, "エサをやる")
    MenuCmd(1, 1, "やめる")
    ClearScenarioFlags(0x1, 4)
    Call(1, 11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69C7")
    MenuCmd(3, 1, 0x1)

    label("loc_69C7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_69F9")
    FadeToBright(300, 0)
    OP_0D()

    label("loc_69F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B43")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_6A3C")
    MenuCmd(1, 1, "スノーシュラブ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6A3C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_6A63")
    MenuCmd(1, 1, "アルモリカブナ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6A63")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_6A84")
    MenuCmd(1, 1, "オロショ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6A84")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_6AA3")
    MenuCmd(1, 1, "ロック")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6AA3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_6AC2")
    MenuCmd(1, 1, "カルプ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6AC2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_6AE3")
    MenuCmd(1, 1, "レイニー")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6AE3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_6B04")
    MenuCmd(1, 1, "エーゼル")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6B04")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_6B25")
    MenuCmd(1, 1, "カサギン")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6B25")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_6B48")
    MenuCmd(1, 1, "レインボウ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6B48")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_6B69")
    MenuCmd(1, 1, "トラード")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6B69")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_6B8A")
    MenuCmd(1, 1, "サモーナ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6B8A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_6BA9")
    MenuCmd(1, 1, "イール")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6BA9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_6BCE")
    MenuCmd(1, 1, "パールグラス")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6BCE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_6BF3")
    MenuCmd(1, 1, "グラトンバス")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6BF3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_6C1A")
    MenuCmd(1, 1, "バイパーヘッド")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C1A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_6C41")
    MenuCmd(1, 1, "パイソンヘッド")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C41")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_6C62")
    MenuCmd(1, 1, "タイタン")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C62")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_6C87")
    MenuCmd(1, 1, "クインシザー")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6C87")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_6CAC")
    MenuCmd(1, 1, "エレキイール")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6CAC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_6CD3")
    MenuCmd(1, 1, "デモンタイタン")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6CD3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_6CFA")
    MenuCmd(1, 1, "アークシュラブ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6CFA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_6D21")
    MenuCmd(1, 1, "ゴルドサモーナ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D21")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_6D48")
    MenuCmd(1, 1, "ノーブルカルプ")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D48")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_END)), "loc_6D71")
    MenuCmd(1, 1, "サーペントヘッド")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D71")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D9, 0x0)"), scpexpr(EXPR_END)), "loc_6D94")
    MenuCmd(1, 1, "ねこまんま")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6D94")

    MenuCmd(1, 1, "やめる")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    FadeToBright(300, 0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_6DDE")
    Jump("loc_7B34")

    label("loc_6DDE")

    EventBegin(0x1)
    Fade(500)
    SetChrPos(0x13, -21980, 1300, -19300, 270)
    SetChrPos(0x0, -23900, 1300, -19070, 89)
    SetChrPos(0x1, -23540, 1300, -20210, 89)
    SetChrPos(0x2, -25020, 1300, -19860, 89)
    SetChrPos(0x3, -25130, 1300, -18930, 89)
    SetChrPos(0x4, -26200, 1300, -19870, 89)
    SetChrPos(0x5, -26790, 1300, -19180, 89)
    OP_68(-23130, 3900, -19610, 0)
    MoveCamera(45, 14, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    #C0422
    ChrTalk(
        0xFE,
        "にゃんにゃん……㈱\x02",
    )

    CloseMessageWindow()

    def lambda_6EA8():

        label("loc_6EA8")

        TurnDirection(0x0, 0x13, 0)
        Yield()
        Jump("loc_6EA8")

    QueueWorkItem2(0x0, 1, lambda_6EA8)

    def lambda_6EBA():

        label("loc_6EBA")

        TurnDirection(0x1, 0x13, 0)
        Yield()
        Jump("loc_6EBA")

    QueueWorkItem2(0x1, 1, lambda_6EBA)

    def lambda_6ECC():

        label("loc_6ECC")

        TurnDirection(0x2, 0x13, 0)
        Yield()
        Jump("loc_6ECC")

    QueueWorkItem2(0x2, 1, lambda_6ECC)

    def lambda_6EDE():

        label("loc_6EDE")

        TurnDirection(0x3, 0x13, 0)
        Yield()
        Jump("loc_6EDE")

    QueueWorkItem2(0x3, 1, lambda_6EDE)

    def lambda_6EF0():

        label("loc_6EF0")

        TurnDirection(0x4, 0x13, 0)
        Yield()
        Jump("loc_6EF0")

    QueueWorkItem2(0x4, 1, lambda_6EF0)

    def lambda_6F02():

        label("loc_6F02")

        TurnDirection(0x5, 0x13, 0)
        Yield()
        Jump("loc_6F02")

    QueueWorkItem2(0x5, 1, lambda_6F02)
    SetChrFlags(0x13, 0x8000)
    OP_93(0x13, 0x0, 0x1F4)
    Sleep(50)
    ClearChrFlags(0x13, 0x1)
    Sound(814, 0, 80, 0)

    def lambda_6F2E():
        OP_9D(0xFE, 0xFFFFA92A, 0x5DC, 0xFFFFC324, 0x708, 0x1F40)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6F2E)
    WaitChrThread(0x13, 1)
    Sound(814, 0, 80, 0)

    def lambda_6F55():
        OP_9D(0xFE, 0xFFFFA7CC, 0x10CC, 0xFFFFC69E, 0x1130, 0x1388)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6F55)
    WaitChrThread(0x13, 1)
    Sound(854, 0, 80, 0)

    def lambda_6F7C():
        OP_9D(0xFE, 0xFFFFA75E, 0x514, 0xFFFFDFBC, 0x708, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6F7C)
    WaitChrThread(0x13, 1)
    Sleep(2000)
    OP_93(0x13, 0xB4, 0x1F4)
    Sound(814, 0, 80, 0)

    def lambda_6FAD():
        OP_9D(0xFE, 0xFFFFA7CC, 0x10CC, 0xFFFFC69E, 0x1194, 0xFA0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6FAD)
    WaitChrThread(0x13, 1)
    Sound(814, 0, 80, 0)

    def lambda_6FD4():
        OP_9D(0xFE, 0xFFFFA92A, 0x5DC, 0xFFFFC324, 0x640, 0x1388)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6FD4)
    WaitChrThread(0x13, 1)
    Sound(854, 0, 80, 0)

    def lambda_6FFB():
        OP_9D(0xFE, 0xFFFFAA24, 0x514, 0xFFFFB49C, 0x5DC, 0x1770)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_6FFB)
    WaitChrThread(0x13, 1)
    SetChrFlags(0x13, 0x1)
    OP_93(0x13, 0x10E, 0x1F4)
    ClearChrFlags(0x13, 0x8000)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    EndChrThread(0x4, 0x1)
    EndChrThread(0x5, 0x1)

    #C0423
    ChrTalk(
        0xFE,
        "ふにゃ～……\x02",
    )

    CloseMessageWindow()
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_70CF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70C5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x15E, 1)

    #A0424
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x70),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x70, 1)

    label("loc_70C5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_70CF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_711D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7113")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x15F, 1)

    #A0425
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x79),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x79, 1)

    label("loc_7113")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_711D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_716B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7161")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x160, 1)

    #A0426
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x6A, 1)

    label("loc_7161")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_716B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_71B9")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71AF")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x161, 1)

    #A0427
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x6D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x6D, 1)

    label("loc_71AF")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_71B9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_7207")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71FD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x162, 1)

    #A0428
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x73),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x73, 1)

    label("loc_71FD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7207")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_7255")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_724B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x163, 1)

    #A0429
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x67),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x67, 1)

    label("loc_724B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7255")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_72A3")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7299")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x164, 1)

    #A0430
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x8A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x8A, 1)

    label("loc_7299")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_72A3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_72F1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72E7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x165, 1)

    #A0431
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x85),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x85, 1)

    label("loc_72E7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_72F1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_733F")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7335")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x166, 1)

    #A0432
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x99),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x99, 1)

    label("loc_7335")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_733F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_738D")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7383")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x167, 1)

    #A0433
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x82),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x82, 1)

    label("loc_7383")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_738D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_73DB")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73D1")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x168, 1)

    #A0434
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x92),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x92, 1)

    label("loc_73D1")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_73DB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_7429")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_741F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x169, 1)

    #A0435
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x7F, 1)

    label("loc_741F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7429")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_7477")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_746D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16A, 1)

    #A0436
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x76),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x76, 1)

    label("loc_746D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7477")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_74C5")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74BB")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16B, 1)

    #A0437
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x7C, 1)

    label("loc_74BB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_74C5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_7513")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7509")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16C, 1)

    #A0438
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x8B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x8B, 1)

    label("loc_7509")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7513")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_7561")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7557")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16D, 1)

    #A0439
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x8D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x8D, 1)

    label("loc_7557")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7561")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_75AF")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75A5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16E, 1)

    #A0440
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x8E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x8E, 1)

    label("loc_75A5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_75AF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_75FD")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_75F3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x16F, 1)

    #A0441
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x83),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x83, 1)

    label("loc_75F3")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_75FD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_764B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7641")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x170, 1)

    #A0442
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xA9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0xA9, 1)

    label("loc_7641")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_764B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_7699")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_768F")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x171, 1)

    #A0443
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x81),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x81, 1)

    label("loc_768F")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7699")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_76E7")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_76DD")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x172, 1)

    #A0444
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x72),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x72, 1)

    label("loc_76DD")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_76E7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_7735")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_772B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x173, 1)

    #A0445
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x9A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x9A, 1)

    label("loc_772B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7735")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_7783")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7779")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x174, 1)

    #A0446
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x95),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0x95, 1)

    label("loc_7779")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7783")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x175, 0x0)"), scpexpr(EXPR_END)), "loc_77D1")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77C7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x175, 1)

    #A0447
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xA0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0xA0, 1)

    label("loc_77C7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_77D1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D9, 0x0)"), scpexpr(EXPR_END)), "loc_7823")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7819")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D9, 1)

    #A0448
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x12D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "×３を受け取った。\x02",
        )
    )

    AddItemNumber(0x12D, 3)

    label("loc_7819")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7823")

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_784A")
    SetScenarioFlags(0x4B, 3)

    label("loc_784A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_785B")
    SetScenarioFlags(0x52, 1)

    label("loc_785B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_786C")
    SetScenarioFlags(0x52, 2)

    label("loc_786C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_787D")
    SetScenarioFlags(0x52, 3)

    label("loc_787D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_788E")
    SetScenarioFlags(0x52, 4)

    label("loc_788E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_789F")
    SetScenarioFlags(0x52, 5)

    label("loc_789F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78B0")
    SetScenarioFlags(0x52, 6)

    label("loc_78B0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 1)), scpexpr(EXPR_END)), "loc_78CD")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_78CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 2)), scpexpr(EXPR_END)), "loc_78E0")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_78E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 3)), scpexpr(EXPR_END)), "loc_78F3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_78F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 4)), scpexpr(EXPR_END)), "loc_7906")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7906")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 5)), scpexpr(EXPR_END)), "loc_7919")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_7919")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 6)), scpexpr(EXPR_END)), "loc_792C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_792C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_79A9")

    #C0449
    ChrTalk(
        0xFE,
        "にゃんにゃんにゃ～ん……♪\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0450
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xA6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    AddItemNumber(0xA6, 1)
    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_79A9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_79E9")

    #C0451
    ChrTalk(
        0x102,
        "#0105Fあら……これをくれるの？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A99")

    label("loc_79E9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7A27")

    #C0452
    ChrTalk(
        0x103,
        "#0205Fこれをくれるんですか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A99")

    label("loc_7A27")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7A99")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A75")

    #C0453
    ChrTalk(
        0x104,
        "#0305Fこれをくれるってのか？\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A99")

    label("loc_7A75")


    #C0454
    ChrTalk(
        0x101,
        "#0005Fこれをくれるのかい……？\x02",
    )

    CloseMessageWindow()

    label("loc_7A99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7AE8")

    #C0455
    ChrTalk(
        0x101,
        (
            "#0000Fはは、サンキュー。\x01",
            "ありがたく使わせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7B2E")

    label("loc_7AE8")


    #C0456
    ChrTalk(
        0x101,
        (
            "#0000Fはは、サンキュー。\x01",
            "……でもどこから\x01",
            "持って来たんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7B2E")

    TalkEnd(0xFE)
    EventEnd(0x4)
    Return()

    label("loc_7B34")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7B73")

    label("loc_7B43")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B57")
    Jump("loc_7B73")

    label("loc_7B57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B73")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 10)

    label("loc_7B73")

    Jump("loc_6973")

    label("loc_7B78")

    Jump("loc_7B80")

    label("loc_7B7D")

    Call(1, 10)

    label("loc_7B80")

    TalkEnd(0x13)
    Return()

    # Function_9_686C end

    def Function_10_7B84(): pass

    label("Function_10_7B84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7F05")

    #C0457
    ChrTalk(
        0x102,
        (
            "#0105Fあら、こんな所に猫が……\x02\x03",

            "#0109Fふふっ、可愛い！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 4)), scpexpr(EXPR_END)), "loc_7C72")

    #C0458
    ChrTalk(
        0x101,
        (
            "#0000Fああ、支援課が入る前から\x01",
            "住み着いていたみたいだ。\x02\x03",

            "#0004F確かクロスベルタイムズが\x01",
            "入っていたはずだから……\x01",
            "その頃からいたのかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7D05")

    label("loc_7C72")


    #C0459
    ChrTalk(
        0x101,
        (
            "#0000Fうーん、支援課が入る前から\x01",
            "住み着いてた猫かな。\x02\x03",

            "#0004F確かクロスベルタイムズが\x01",
            "入っていたはずだから……\x01",
            "その頃からいたのかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7D05")


    #C0460
    ChrTalk(
        0x104,
        (
            "#0309F……うりうり！\x01",
            "お前、名前は何てんだ～？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x104, 500)
    Sound(823, 0, 100, 0)
    Sleep(500)

    #C0461
    ChrTalk(
        0x103,
        (
            "#0200F…………………………\x02\x03",

            "この子の名前はコッペです。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7DA4")
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_7DA4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7DC4")
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_7DC4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7DE4")
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_7DE4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E04")
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    label("loc_7E04")

    Sleep(1000)

    #C0462
    ChrTalk(
        0x102,
        (
            "#0102Fティオちゃんが付けたの？\x01",
            "可愛い名前ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x103,
        (
            "#0203Fいえ、わたしが\x01",
            "名付けたわけではなく……\x02\x03",

            "#0202F……ともかく、この子の名前は\x01",
            "コッペでよいと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x104,
        (
            "#0304Fああ、それでいいんじゃね？\x02\x03",

            "#0300Fときどきエサでも\x01",
            "持ってきてやろうぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 3)
    Jump("loc_84C3")

    label("loc_7F05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_7F25")

    #C0465
    ChrTalk(
        0x13,
        "にゃお……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_84C3")

    label("loc_7F25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_801F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8008")

    #C0466
    ChrTalk(
        0x13,
        "にゃ～～ご。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8000")

    #C0467
    ChrTalk(
        0x10A,
        (
            "#0605F（む……確かこの猫は\x01",
            "  クロスベル通信社の\x01",
            "  飼い猫だったはずだが……）\x02\x03",

            "#0603F（現在は特務支援課に移管、か。\x01",
            "  一課の資料に\x01",
            "  追記しておかなければな……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8000")

    SetScenarioFlags(0x0, 5)
    Jump("loc_801A")

    label("loc_8008")


    #C0468
    ChrTalk(
        0x13,
        "にゃ～～ご。\x02",
    )

    CloseMessageWindow()

    label("loc_801A")

    Jump("loc_84C3")

    label("loc_801F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8041")

    #C0469
    ChrTalk(
        0x13,
        "ふみゃああ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_84C3")

    label("loc_8041")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8148")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8129")

    #C0470
    ChrTalk(
        0x13,
        "ごろごろ、にゃーご。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_80B2")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    label("loc_80B2")


    #C0471
    ChrTalk(
        0x109,
        (
            "#0502F（うーん、可愛い……）\x02\x03",

            "#0506F（屋上で猫を飼ってるなんて……\x01",
            "  はぁ、あたしも門で飼えないかなぁ。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_8143")

    label("loc_8129")


    #C0472
    ChrTalk(
        0x13,
        "ごろごろ、にゃーご。\x02",
    )

    CloseMessageWindow()

    label("loc_8143")

    Jump("loc_84C3")

    label("loc_8148")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_8346")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAE, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_82F7")

    #C0473
    ChrTalk(
        0x153,
        (
            "#1105Fあ、ネコだ～。\x02\x03",

            "#1109Fちっちゃくてかわいい！\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x101,
        (
            "#0000Fそういやキーアを\x01",
            "屋上に連れて来るのは初めてだな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_8239")

    #C0475
    ChrTalk(
        0x102,
        (
            "#0104Fまあ、通りから丸見えだもの。\x02\x03",

            "#0100Fキーアちゃんの安全を考えると\x01",
            "仕方ないわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82EC")

    label("loc_8239")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_829C")

    #C0476
    ChrTalk(
        0x103,
        (
            "#0204Fまあ、通りから丸見えですし。\x02\x03",

            "#0202Fキーアの安全を考えると\x01",
            "仕方ないかと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82EC")

    label("loc_829C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_82EC")

    #C0477
    ChrTalk(
        0x104,
        (
            "#0302Fま、通りから丸見えだし\x01",
            "キー坊の事を考えりゃあ仕方ねぇだろ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82EC")

    SetScenarioFlags(0xAE, 6)
    SetScenarioFlags(0x6A, 3)
    Jump("loc_8341")

    label("loc_82F7")


    #C0478
    ChrTalk(
        0x153,
        "#1110Fネコちゃん、こっちむいて～！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x153, 500)
    Sleep(300)

    #C0479
    ChrTalk(
        0x13,
        "にやゃゃあ～……㈱\x02",
    )

    CloseMessageWindow()

    label("loc_8341")

    Jump("loc_84C3")

    label("loc_8346")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_8368")

    #C0480
    ChrTalk(
        0x13,
        "ふみゃああ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_84C3")

    label("loc_8368")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_8386")

    #C0481
    ChrTalk(
        0x13,
        "にゃあ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_84C3")

    label("loc_8386")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_83A4")

    #C0482
    ChrTalk(
        0x13,
        "にゃーお。\x02",
    )

    CloseMessageWindow()
    Jump("loc_84C3")

    label("loc_83A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_83C0")

    #C0483
    ChrTalk(
        0x13,
        "にゃお？\x02",
    )

    CloseMessageWindow()
    Jump("loc_84C3")

    label("loc_83C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_83DE")

    #C0484
    ChrTalk(
        0x13,
        "にゃおん。\x02",
    )

    CloseMessageWindow()
    Jump("loc_84C3")

    label("loc_83DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_8400")

    #C0485
    ChrTalk(
        0x13,
        "ふみゃああ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_84C3")

    label("loc_8400")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_8420")

    #C0486
    ChrTalk(
        0x13,
        "にゃ～～ご。\x02",
    )

    CloseMessageWindow()
    Jump("loc_84C3")

    label("loc_8420")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_8466")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 3)), scpexpr(EXPR_END)), "loc_844F")

    #C0487
    ChrTalk(
        0x13,
        "にゃにやゃゃあ～㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_8461")

    label("loc_844F")


    #C0488
    ChrTalk(
        0x13,
        "にゃあ～～。\x02",
    )

    CloseMessageWindow()

    label("loc_8461")

    Jump("loc_84C3")

    label("loc_8466")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 6)), scpexpr(EXPR_END)), "loc_84C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B, 3)), scpexpr(EXPR_END)), "loc_8495")

    #C0489
    ChrTalk(
        0x13,
        "にゃにやゃゃあ～㈱\x02",
    )

    CloseMessageWindow()
    Jump("loc_84C3")

    label("loc_8495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A, 4)), scpexpr(EXPR_END)), "loc_84B3")

    #C0490
    ChrTalk(
        0x13,
        "にゃーお。\x02",
    )

    CloseMessageWindow()
    Jump("loc_84C3")

    label("loc_84B3")


    #C0491
    ChrTalk(
        0x13,
        "にゃおん？\x02",
    )

    CloseMessageWindow()

    label("loc_84C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8567")

    #C0492
    ChrTalk(
        0x101,
        (
            "#0004F（コッペはずっと支援課に\x01",
            "  住み着いてる猫なんだよな……）\x02\x03",

            "#0000F（まあ気ままな奴だし、\x01",
            "  時々エサを持ってきて\x01",
            "  やってる程度だけど。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x6A, 3)

    label("loc_8567")

    Return()

    # Function_10_7B84 end

    def Function_11_8568(): pass

    label("Function_11_8568")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15E, 0x0)"), scpexpr(EXPR_END)), "loc_8576")
    SetScenarioFlags(0x1, 4)

    label("loc_8576")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x15F, 0x0)"), scpexpr(EXPR_END)), "loc_8584")
    SetScenarioFlags(0x1, 4)

    label("loc_8584")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x160, 0x0)"), scpexpr(EXPR_END)), "loc_8592")
    SetScenarioFlags(0x1, 4)

    label("loc_8592")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x161, 0x0)"), scpexpr(EXPR_END)), "loc_85A0")
    SetScenarioFlags(0x1, 4)

    label("loc_85A0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x162, 0x0)"), scpexpr(EXPR_END)), "loc_85AE")
    SetScenarioFlags(0x1, 4)

    label("loc_85AE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x163, 0x0)"), scpexpr(EXPR_END)), "loc_85BC")
    SetScenarioFlags(0x1, 4)

    label("loc_85BC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x164, 0x0)"), scpexpr(EXPR_END)), "loc_85CA")
    SetScenarioFlags(0x1, 4)

    label("loc_85CA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x165, 0x0)"), scpexpr(EXPR_END)), "loc_85D8")
    SetScenarioFlags(0x1, 4)

    label("loc_85D8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x166, 0x0)"), scpexpr(EXPR_END)), "loc_85E6")
    SetScenarioFlags(0x1, 4)

    label("loc_85E6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x167, 0x0)"), scpexpr(EXPR_END)), "loc_85F4")
    SetScenarioFlags(0x1, 4)

    label("loc_85F4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x168, 0x0)"), scpexpr(EXPR_END)), "loc_8602")
    SetScenarioFlags(0x1, 4)

    label("loc_8602")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x169, 0x0)"), scpexpr(EXPR_END)), "loc_8610")
    SetScenarioFlags(0x1, 4)

    label("loc_8610")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16A, 0x0)"), scpexpr(EXPR_END)), "loc_861E")
    SetScenarioFlags(0x1, 4)

    label("loc_861E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16B, 0x0)"), scpexpr(EXPR_END)), "loc_862C")
    SetScenarioFlags(0x1, 4)

    label("loc_862C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16C, 0x0)"), scpexpr(EXPR_END)), "loc_863A")
    SetScenarioFlags(0x1, 4)

    label("loc_863A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16D, 0x0)"), scpexpr(EXPR_END)), "loc_8648")
    SetScenarioFlags(0x1, 4)

    label("loc_8648")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16E, 0x0)"), scpexpr(EXPR_END)), "loc_8656")
    SetScenarioFlags(0x1, 4)

    label("loc_8656")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x16F, 0x0)"), scpexpr(EXPR_END)), "loc_8664")
    SetScenarioFlags(0x1, 4)

    label("loc_8664")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x170, 0x0)"), scpexpr(EXPR_END)), "loc_8672")
    SetScenarioFlags(0x1, 4)

    label("loc_8672")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x171, 0x0)"), scpexpr(EXPR_END)), "loc_8680")
    SetScenarioFlags(0x1, 4)

    label("loc_8680")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x172, 0x0)"), scpexpr(EXPR_END)), "loc_868E")
    SetScenarioFlags(0x1, 4)

    label("loc_868E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x173, 0x0)"), scpexpr(EXPR_END)), "loc_869C")
    SetScenarioFlags(0x1, 4)

    label("loc_869C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x174, 0x0)"), scpexpr(EXPR_END)), "loc_86AA")
    SetScenarioFlags(0x1, 4)

    label("loc_86AA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D9, 0x0)"), scpexpr(EXPR_END)), "loc_86B8")
    SetScenarioFlags(0x1, 4)

    label("loc_86B8")

    Return()

    # Function_11_8568 end

    def Function_12_86B9(): pass

    label("Function_12_86B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_86CA")
    Jump("loc_87EF")

    label("loc_86CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_87EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_87D7")

    #C0493
    ChrTalk(
        0x103,
        (
            "#0202Fツァイト、キーアを\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x14,
        "#1200Fグルルル……ウォン！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8776")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    label("loc_8776")


    #C0495
    ChrTalk(
        0x109,
        (
            "#0508F（ううっ……\x01",
            "  犬はちょっと苦手かも。）\x02\x03",

            "#0505F（あ、犬じゃなくて狼だっけ。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_87EF")

    label("loc_87D7")


    #C0496
    ChrTalk(
        0x14,
        "#1200Fグルルル……\x02",
    )

    CloseMessageWindow()

    label("loc_87EF")

    TalkEnd(0xFE)
    Return()

    # Function_12_86B9 end

    def Function_13_87F3(): pass

    label("Function_13_87F3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_8804")
    Jump("loc_8989")

    label("loc_8804")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_8989")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_890D")
    OP_93(0xFE, 0x0, 0x0)

    #C0497
    ChrTalk(
        0x15,
        (
            "#1110Fうーん、ぽかぽかだぁ～！\x02\x03",

            "#1109Fツァイト、おひるねしよう～！\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x14,
        "#1200Fグルルルル……\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x109,
        (
            "#0509F（か、可愛い……！）\x02\x03",

            "#0502F（うーん、皆さんがメロメロに\x01",
            "  なってるのも分かりますねぇ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x101,
        "#0012F（はは……まあね。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_8989")

    label("loc_890D")


    #C0501
    ChrTalk(
        0x15,
        (
            "#1110Fあ、みんな。\x01",
            "いってらっしゃーい！\x02\x03",

            "#1109Fユーレイ退治、がんばってね！\x02",
        )
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x102,
        (
            "#0109Fえ、ええ……\x01",
            "頑張ってくるわね！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8989")

    TalkEnd(0xFE)
    Return()

    # Function_13_87F3 end

    def Function_14_898D(): pass

    label("Function_14_898D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_8A72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_8A02")

    #C0503
    ChrTalk(
        0xFE,
        (
            "グレイス先輩～っ！\x01",
            "原稿はどうするんですか～！？\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0xFE,
        "早く出てきて助けてくださいよ～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_8A6D")

    label("loc_8A02")


    #C0505
    ChrTalk(
        0xFE,
        (
            "参ったなー、グレイス先輩\x01",
            "ちっとも見つからないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xFE,
        (
            "先輩が居なくちゃ\x01",
            "原稿が上げられないのに……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_8A6D")

    Jump("loc_8B56")

    label("loc_8A72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_8AE7")

    #C0507
    ChrTalk(
        0xFE,
        "グレイス先輩～、どこですか～！？\x02",
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0xFE,
        (
            "……またどこかの飲み屋で\x01",
            "食べ歩いてるんじゃないだろうな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B56")

    label("loc_8AE7")


    #C0509
    ChrTalk(
        0xFE,
        (
            "まったくグレイス先輩ったら\x01",
            "どこ行っちゃったんだろ……\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0xFE,
        (
            "原稿の締め切りも近いってのに、\x01",
            "ぶつぶつ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)

    label("loc_8B56")

    TalkEnd(0xFE)
    Return()

    # Function_14_898D end

    def Function_15_8B5A(): pass

    label("Function_15_8B5A")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    SoundLoad(803)
    Sound(803, 2, 0, 0)
    BeginChrThread(0x23, 1, 0, 55)
    SetChrPos(0x101, 1420, 0, -14130, 0)
    SetChrPos(0x102, -290, 0, -16530, 45)
    SetChrPos(0x103, -700, 0, -14800, 90)
    SetChrPos(0x104, 1500, 0, -16379, 0)
    OP_68(-660, 3000, 3390, 0)
    MoveCamera(55, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16370, 0)
    MoveCamera(35, 3, 0, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-21970, 1900, 6540, 0)
    MoveCamera(351, 8, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14980, 0)
    MoveCamera(356, 8, 0, 3000)
    OP_6F(0x79)
    Fade(500)
    OP_68(19900, 3000, 6130, 0)
    MoveCamera(57, 4, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18430, 0)
    MoveCamera(55, -2, 0, 5000)
    OP_6F(0x79)
    Fade(500)
    OP_68(-60, 5700, 23250, 0)
    MoveCamera(359, 18, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(11620, 0)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    OP_6F(0x79)
    OP_68(-5540, 4000, 5000, 10000)
    MoveCamera(24, 29, 0, 10000)
    OP_6E(800, 10000)
    SetCameraDistance(35000, 10000)
    Sleep(2000)
    PlaceName2(340, 200, "c_plac02", 0x0, 1500)
    OP_6F(0x79)
    EndChrThread(0x23, 0x1)

    #C0511
    ChrTalk(
        0x104,
        (
            "#0300Fやれやれ……相変わらず\x01",
            "騒がしい通りだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x101,
        (
            "#0004Fクロスベル市の\x01",
            "中心みたいな場所だからね。\x02\x03",

            "#0000F大きな店が建ち並んでいて、\x01",
            "大抵の買い物はこの辺りで済むし……\x02\x03",

            "他の街区に向かうにも便利な場所だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x102,
        (
            "#0100F最近では導力車も増えて\x01",
            "一層賑やかになっているみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x101,
        "#0002Fはは、みたいだね。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    BeginChrThread(0x23, 1, 0, 56)
    Fade(500)
    OP_68(190, 1500, -15740, 0)
    MoveCamera(39, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    OP_0D()
    TurnDirection(0x101, 0x102, 500)

    #C0515
    ChrTalk(
        0x101,
        (
            "#0000Fそうだ、みんな。\x01",
            "《オーバルストア》にも寄ってみようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x104,
        (
            "#0305Fああ、さっきオッサンが言ってた\x01",
            "オーブメント工房のことだな？\x02\x03",

            "#0300Fなんか随分新しい内装の\x01",
            "工房だっていうのは聞いてるが。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x103,
        (
            "#0203Fより商業性を高めた\x01",
            "新しいタイプの工房ですね。\x02\x03",

            "#0200F一応、警察と契約を結んでいるので\x01",
            "戦術オーブメントの改造や\x01",
            "結晶回路#8Rク オ ー ツ#の調達も出来ると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x102,
        (
            "#0104F#6P確かにこの先、お世話になりそうね。\x02\x03",

            "#0100Fなら、他の街区に向かう前に\x01",
            "挨拶しておきましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x101,
        "#0000Fああ、そこの角にある建物のはずだ。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0520
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "中央広場には、百貨店やオーバルストア、\x01",
            "武器商会、レストランなどの施設があります。\x02",
        )
    )

    CloseMessageWindow()

    #A0521
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ほぼ全ての買い物がまかなえるため、\x01",
            "装備を整える際は\x01",
            "中央広場に立ち寄ると良いでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #A0522
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "なお、オーバルストア《ゲンテン》は\x01",
            "広場の東側に位置しています。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -290, 0, -16530, 45)
    ModifyEventFlags(0, 2, 0x80)
    SetScenarioFlags(0x44, 4)
    EndChrThread(0x23, 0x1)
    OP_24(0x323)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_15_8B5A end

    def Function_16_91FB(): pass

    label("Function_16_91FB")

    EventBegin(0x1)
    SetChrPos(0x18, -6460, -4200, -21000, 135)

    def lambda_9213():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9213)
    WaitChrThread(0x101, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_94A0")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9307")

    #C0523
    ChrTalk(
        0x101,
        (
            "#0005Fおっと……すぐそこの店が\x01",
            "武器商会みたいだな。\x02\x03",

            "#0000F課長にも言われているし、\x01",
            "先に入ってみようか。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_92AA():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_92AA)

    def lambda_92B7():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_92B7)

    def lambda_92C4():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_92C4)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0524
    ChrTalk(
        0x102,
        "#0100Fそうね、お邪魔してみましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9498")

    label("loc_9307")


    #C0525
    ChrTalk(
        0x101,
        (
            "#0005Fおっと……待ってくれ。\x01",
            "すぐそこの店が武器商会みたいだ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_934F():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_934F)

    def lambda_935C():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_935C)

    def lambda_9369():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9369)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93E7")

    #C0526
    ChrTalk(
        0x103,
        (
            "#0203Fそうみたいですね。\x02\x03",

            "#0200F了解です、まずは武器商会に\x01",
            "立ち寄ってみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9498")

    label("loc_93E7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_944F")

    #C0527
    ChrTalk(
        0x104,
        (
            "#0305Fおっと、そうみてえだな。\x02\x03",

            "#0300Fんじゃま、まずは武器商会に\x01",
            "行ってみるか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9498")

    label("loc_944F")


    #C0528
    ChrTalk(
        0x102,
        (
            "#0105Fあら、本当……\x02\x03",

            "#0100Fそれじゃあ先に\x01",
            "お邪魔してみましょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9498")

    SetScenarioFlags(0x1, 3)
    Jump("loc_94FA")

    label("loc_94A0")


    #C0529
    ChrTalk(
        0x101,
        (
            "#0000Fすぐそこの店が\x01",
            "武器商会みたいだ。\x02\x03",

            "課長にも言われているし、\x01",
            "一度入ってみよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_94FA")

    SetChrPos(0x0, -8660, -4200, -18220, 180)
    EventEnd(0x4)
    Return()

    # Function_16_91FB end

    def Function_17_950E(): pass

    label("Function_17_950E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x9E, 0xFF, 0xFF)
    OP_68(-640, 1500, 12830, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x101, 0, 0, 14500, 180)
    SetChrPos(0x19F, 750, 0, 13750, 270)
    SetChrPos(0x109, 750, 0, 12750, 315)
    SetChrPos(0x102, -1250, 0, 14250, 135)
    SetChrPos(0x103, -1500, 0, 13000, 90)
    SetChrPos(0x104, -1250, 0, 12000, 45)
    FadeToBright(1000, 0)
    OP_0D()

    #C0530
    ChrTalk(
        0x101,
        (
            "#5P#0000Fそれじゃあ、早速プレゼントを\x01",
            "見繕おうと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x104,
        (
            "#12P#0303Fつっても、そんなに時間がねぇぞ。\x02\x03",

            "#0300Fフランちゃん、\x01",
            "とっくにレストランに\x01",
            "向かってる頃じゃねぇのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x102,
        (
            "#5P#0103Fそうね……誘っておいて\x01",
            "フランさんを待たせるのは\x01",
            "気が引けるし。\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x19F,
        (
            "#11Pじゃ、じゃあ……\x01",
            "どうすればいいんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x103,
        (
            "#6P#0203F役割を分担しましょう。\x02\x03",

            "#0200Fわたしとエリィさん、ランディさんは\x01",
            "先にレストランに向かいましょう。\x02\x03",

            "待ち合わせに少し遅れることを\x01",
            "フランさんに伝えておきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x101,
        (
            "#5P#0003Fその間に俺と曹長と\x01",
            "アントンさんで\x01",
            "プレゼントを見繕う……\x02\x03",

            "#0000F……その方がよさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x19F,
        (
            "#11Pありがとう、\x01",
            "何から何まで……\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x19F,
        (
            "#11P本当に僕は運がいいよ。\x01",
            "こんなに親切な人に\x01",
            "恵まれて……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0538
    ChrTalk(
        0x109,
        "#11P#0506Fな、涙ぐまないでくださいよ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0539
    ChrTalk(
        0x101,
        (
            "#5P#0003Fと、とにかく\x01",
            "そういう分担でいこうか。\x02\x03",

            "#0000Fエリィ、ティオ、ランディ。\x01",
            "そっちはよろしく頼む。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9997():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9997)

    def lambda_99A4():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_99A4)

    def lambda_99B1():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_99B1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0540
    ChrTalk(
        0x102,
        "#5P#0100F分かったわ。\x02",
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x103,
        "#6P#0200Fでは、また。\x02",
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x104,
        (
            "#12P#0300Fせいぜいハートに\x01",
            "ビビッとくるプレゼントを\x01",
            "選んできてくれや。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9A4C():
        OP_97(0x103, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9A4C)
    Sleep(50)

    def lambda_9A69():
        OP_97(0x104, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9A69)
    Sleep(50)

    def lambda_9A86():
        OP_97(0x102, 0xFFFFE4A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9A86)

    def lambda_9AA0():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9AA0)

    def lambda_9AAD():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9AAD)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x109, 1)

    def lambda_9ACE():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9ACE)
    Sleep(50)

    def lambda_9ADE():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9ADE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x109, 1)

    #C0543
    ChrTalk(
        0x101,
        (
            "#5P#0000Fそれじゃ、俺たちも\x01",
            "百貨店に入ろう。\x02\x03",

            "曹長、フランが\x01",
            "気に入りそうなものを\x01",
            "アドバイスしてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x109,
        "#11P#0506F……ふぅ、仕方ないですね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19F, 0x109, 500)

    #C0545
    ChrTalk(
        0x19F,
        "#11Pよろしく頼むよ、お姉さん！\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-10, 2700, 26140, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 0, 800, 24000, 0)
    SetChrPos(0x109, 750, 800, 23250, 0)
    SetChrPos(0x19F, -750, 800, 22500, 0)

    def lambda_9C1A():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9C1A)
    Sleep(50)

    def lambda_9C37():
        OP_97(0x109, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9C37)
    Sleep(50)

    def lambda_9C54():
        OP_97(0x19F, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19F, 1, lambda_9C54)
    OP_0D()
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0x5, 0x0, 0x0)
    Sound(100, 0, 100, 0)
    Sleep(750)

    def lambda_9C8A():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9C8A)
    Sleep(50)

    def lambda_9C9E():
        OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9C9E)
    Sleep(50)

    def lambda_9CB2():
        OP_A7(0x19F, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x19F, 2, lambda_9CB2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x19F, 0x1)
    EndChrThread(0x19F, 0x2)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x9E, 0xFF, 0xFF)
    OP_29(0x2A, 0x1, 0x3)
    NewScene("c0170", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_950E end

    SaveToFile()

Try(main)
