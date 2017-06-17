from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0580.bin",                # FileName
        "c0580",                    # MapName
        "c0580",                    # Location
        0x0028,                     # MapIndex
        "ed7117",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 40, 0, 0, 0, 1],
    )

    BuildStringList((
        "c0580",                  # 0
        "イメルダ夫人",           # 1
        "SE制御",                 # 2
    ))

    AddCharChip((
        "chr/ch09002.itc",                   # 00
    ))

    DeclNpc(-750,    100,     4800,    180,  261,  0x0, 0,   0,   0,   255, 255, 0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-750,    0,       3500,    1500,    -750,    1500,    4800,    0x007E, 0,  2,  0x0000)

    ChipFrameInfo(276, 0)                                        # 0

    ScpFunction((
        "Function_0_114",          # 00, 0
        "Function_1_126",          # 01, 1
        "Function_2_19B",          # 02, 2
        "Function_3_19F",          # 03, 3
        "Function_4_20AE",         # 04, 4
        "Function_5_2934",         # 05, 5
        "Function_6_35E7",         # 06, 6
        "Function_7_35FD",         # 07, 7
    ))


    def Function_0_114(): pass

    label("Function_0_114")

    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    Return()

    # Function_0_114 end

    def Function_1_126(): pass

    label("Function_1_126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_142")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_159")

    label("loc_142")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_159")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x7D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_17A")
    Sound(128, 1, 50, 0)

    label("loc_17A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_191")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)

    label("loc_191")

    OP_10(0x0, 0x1)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x0)
    Return()

    # Function_1_126 end

    def Function_2_19B(): pass

    label("Function_2_19B")

    Call(0, 3)
    Return()

    # Function_2_19B end

    def Function_3_19F(): pass

    label("Function_3_19F")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1")
    TalkEnd(0x8)
    Call(0, 5)
    Return()

    label("loc_1C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x139, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E4")
    TalkEnd(0x8)
    Call(0, 4)
    Return()

    label("loc_1E4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20AA")
    FadeToDark(300, 0, 100)

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24C")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_24C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_26B")
    OP_AF(0x43)
    Jump("loc_27D")

    label("loc_26B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_27B")
    OP_AF(0x44)
    Jump("loc_27D")

    label("loc_27B")

    OP_AF(0x43)

    label("loc_27D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_20A5")

    label("loc_28C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A0")
    Jump("loc_20A5")

    label("loc_2A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20A5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41C")

    #C0001
    ChrTalk(
        0x8,
        (
            "（カタカタ、カタカタ……）\x01",
            "大統領の拘束に\x01",
            "湿地帯に現れた巨大な樹か……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "特に大樹に関しては、\x01",
            "導力ネット上でも色々な憶測が\x01",
            "飛び交ってるねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "せっかくそんな物が現れたんだ、\x01",
            "この際新しい観光名所にでも\x01",
            "しちまったらどうだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "そうすりゃ、国交が再開された時に\x01",
            "アタシも大儲けできそうなんだが。\x01",
            "ヒヒャヒャヒャ……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_4CE")

    label("loc_41C")


    #C0005
    ChrTalk(
        0x8,
        (
            "世間じゃ大騒ぎだが、\x01",
            "アタシにはあの巨大な樹が\x01",
            "だんだん金のなる木に見えてきたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "いずれ国交が再開された時のために、\x01",
            "新しい物件を確保しておくかねえ。\x01",
            "ヒヒャヒャヒャ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4CE")

    Jump("loc_20A5")

    label("loc_4D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_6E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_649")

    #C0007
    ChrTalk(
        0x8,
        "おや、支援課の子達じゃないか。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "アンタたちが動いてるってことは\x01",
            "色々と面白いことになってそうだねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        "#00006F面白がられても困りますけど……\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x103,
        (
            "#00200Fとにかく、外に出ないように\x01",
            "ご注意をお願いします。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "分かった分かった。\x01",
            "ここから観戦させてもらうとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "せいぜい大統領たちを\x01",
            "引っ掻き回してやっとくれ。\x01",
            "ヒヒャヒャヒャ……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_6DC")

    label("loc_649")


    #C0013
    ChrTalk(
        0x8,
        (
            "アンタたちが動いてるってことは\x01",
            "色々と面白いことになってそうだねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "せいぜい大統領たちを\x01",
            "引っ掻き回してやっとくれ。\x01",
            "ヒヒャヒャヒャ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6DC")

    Jump("loc_20A5")

    label("loc_6E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_92C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_863")

    #C0015
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャヒャ……！\x01",
            "例の演説、なかなか面白かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "まさか帝国と共和国に\x01",
            "あそこまでの啖呵を切るとはねえ。\x01",
            "ヒヒ、さすがのアタシも予想外だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "……さあて、ディーターの小僧が\x01",
            "どうするつもりかは知らないが、\x01",
            "帝国や共和国も黙っちゃいないだろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、今のうちに\x01",
            "倉庫に保管してあるアンティークの山を\x01",
            "安全な場所に移しておくとするかねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_927")

    label("loc_863")


    #C0019
    ChrTalk(
        0x8,
        (
            "ディーターの小僧が\x01",
            "どうするつもりかは知らないが、\x01",
            "帝国や共和国も黙っちゃいないだろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、今のうちに\x01",
            "倉庫に保管してあるアンティークの山を\x01",
            "安全な場所に移しておくとするかねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_927")

    Jump("loc_20A5")

    label("loc_92C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_AC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A27")

    #C0021
    ChrTalk(
        0x8,
        (
            "あの襲撃事件で旧市街に現れた\x01",
            "巨大な化物に、アタシの所有してた\x01",
            "アパートが壊されちまってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、有様を見てきたが\x01",
            "あそこまで壊されると笑うしかないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "……ふう、やれやれ。\x01",
            "あの一帯をどうしたもんかねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_AC2")

    label("loc_A27")


    #C0024
    ChrTalk(
        0x8,
        (
            "壊されたアパートの有様を見たが、\x01",
            "あそこまで壊されると笑うしかないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "新しく建て直すにも\x01",
            "面倒でミラがかかるし……\x01",
            "いっそ土地ごと手放そうかねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AC2")

    Jump("loc_20A5")

    label("loc_AC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_CA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF7")

    #C0026
    ChrTalk(
        0x8,
        (
            "猟兵の連中、\x01",
            "まさか町一つを占領するなんて\x01",
            "大それた真似をするとはねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "山道にある人形工房にも\x01",
            "一応連絡をとってみたが、\x01",
            "結局繋がらなかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、\x01",
            "まあヨルグのことだから\x01",
            "心配ないだろうけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x8,
        (
            "案外、こんな状況でも人形制作に\x01",
            "励んでるかもしれないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_C9B")

    label("loc_BF7")


    #C0030
    ChrTalk(
        0x8,
        (
            "山道にある人形工房にも\x01",
            "一応連絡をとってみたが、\x01",
            "結局繋がらなかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "ヒヒ、まあヨルグのことだから\x01",
            "こんな状況でも人形制作に\x01",
            "励んでるかもしれないけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C9B")

    Jump("loc_20A5")

    label("loc_CA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_EA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E2A")

    #C0032
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、この雨で\x01",
            "ただでさえ少ない客足も\x01",
            "さらに減りそうだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "あんたたち、せっかくだし\x01",
            "この時間に店の棚の掃除でも\x01",
            "してってくれないかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        "#00006Fさ、さすがにお断りします。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、冗談だよ。\x01",
            "高価な品もあるのに\x01",
            "誰が棚に触らせるかね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetScenarioFlags(0x0, 0)
    Jump("loc_EA2")

    label("loc_E2A")


    #C0036
    ChrTalk(
        0x8,
        (
            "一応、導力ネットによれば\x01",
            "午後には晴れるらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、だからといって\x01",
            "店の客足は増えないだろうけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_EA2")

    Jump("loc_20A5")

    label("loc_EA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1014")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F85")

    #C0038
    ChrTalk(
        0x8,
        (
            "さっき導力ネットを見ていたら\x01",
            "速報が入ってきてねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "なんでも、西の街道で\x01",
            "列車の脱線事故があったって\x01",
            "いうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、何やら\x01",
            "キナ臭いモノを感じるのは\x01",
            "アタシだけかねえ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_100F")

    label("loc_F85")


    #C0041
    ChrTalk(
        0x8,
        (
            "導力ネットによれば、\x01",
            "西の街道で脱線事故が\x01",
            "あったそうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、何やら\x01",
            "キナ臭いモノを感じるのは\x01",
            "アタシだけかねえ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_100F")

    Jump("loc_20A5")

    label("loc_1014")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_11D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_112B")

    #C0043
    ChrTalk(
        0x8,
        (
            "さすがのアタシも\x01",
            "あのジジイについては\x01",
            "知ってる事はそう多くなくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "なんせ、普段はろくに表に出ずに\x01",
            "黙々と人形を作っているような\x01",
            "偏屈ジジイだからねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "ま、アタシはあの工房の人形で\x01",
            "一儲け出来さえすればいいんだけどね。\x01",
            "ヒヒャヒャヒャ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_11CF")

    label("loc_112B")


    #C0046
    ChrTalk(
        0x8,
        (
            "さすがのアタシも\x01",
            "あのジジイについては\x01",
            "知ってる事はそう多くなくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "ま、アタシはあの工房の人形で\x01",
            "一儲け出来さえすればいいんだけどね。\x01",
            "ヒヒャヒャヒャ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11CF")

    Jump("loc_20A5")

    label("loc_11D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1371")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12EB")

    #C0048
    ChrTalk(
        0x8,
        (
            "（カタカタカタカタ……）\x01",
            "ふむふむ、なるほどねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "導力ネット上でも\x01",
            "独立の是非については\x01",
            "賛否あるみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "ただ、今の所は\x01",
            "賛成派が多数を占めているのは\x01",
            "間違いないようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、議論は続くだろうし\x01",
            "アタシも気にかけておくかねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_136C")

    label("loc_12EB")


    #C0052
    ChrTalk(
        0x8,
        (
            "導力ネットでも\x01",
            "独立の是非については\x01",
            "賛否あるみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、議論は続くだろうし\x01",
            "アタシも気にかけておくかねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_136C")

    Jump("loc_20A5")

    label("loc_1371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_16AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_161C")

    #C0054
    ChrTalk(
        0x8,
        (
            "おや、アンタは……\x01",
            "確かエプスタインの。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        "#00200Fご無沙汰してます、お婆さん。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、特務支援課も\x01",
            "ようやくメンバーが揃い踏みだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "通商会議の警備にも立ち入るそうだし、\x01",
            "万全の体制が整ってなによりだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0058
    ChrTalk(
        0x101,
        (
            "#00006F相変わらず、色々な所に\x01",
            "通じてるみたいですね……\x02\x03",

            "#00000Fイメルダさんの場合、情報を\x01",
            "ご自分で楽しむだけに留めてるのが\x01",
            "ある意味救いですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、その点は\x01",
            "安心してくれて構わないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "警察に捕まるような\x01",
            "ヘマをしないのが、\x01",
            "アタシの信条だからねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x103,
        (
            "#00206F……それをわたしたちに\x01",
            "言うのもどうかと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 4)
    Jump("loc_16A5")

    label("loc_161C")


    #C0062
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、特務支援課も\x01",
            "ようやくメンバーが揃い踏みだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "今後ともアタシなりに、\x01",
            "アンタたちの活動を\x01",
            "楽しませてもらうとしよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A5")

    Jump("loc_20A5")

    label("loc_16AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1897")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17F0")

    #C0064
    ChrTalk(
        0x8,
        (
            "（カタカタカタカタ……）\x01",
            "ほうほう、なるほど。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "導力ネット上でも、\x01",
            "オルキスタワーについては\x01",
            "色々と騒がれてるみたいだねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        (
            "空を衝くほどの超高層ビルだ、\x01",
            "観光名所としてもかなりの\x01",
            "経済効果が期待できるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、今のうちに\x01",
            "タワーがよく見える物件を\x01",
            "押さえておくとするかねえ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1892")

    label("loc_17F0")


    #C0068
    ChrTalk(
        0x8,
        (
            "あのオルキスタワーは、\x01",
            "観光名所としてもかなりの\x01",
            "経済効果が期待できるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、今のうちに\x01",
            "タワーがよく見える物件を\x01",
            "押さえておくとするかねえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1892")

    Jump("loc_20A5")

    label("loc_1897")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1B78")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C4")

    #C0070
    ChrTalk(
        0x8,
        (
            "そういえば、最近新しく\x01",
            "続き物の小説を読み始めたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x8,
        (
            "面白いは面白いが、アタシには\x01",
            "ちょっとばかり趣味が合わなくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、この際だ。\x01",
            "あんたたちに押し付けるとしようかね。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0073
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2F0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2F0, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x188, 2)
    Jump("loc_1B73")

    label("loc_19C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AC1")

    #C0074
    ChrTalk(
        0x8,
        (
            "明日からの通商会議じゃ、\x01",
            "各国の首脳が集まるそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        (
            "他の首脳陣はともかく、\x01",
            "《鉄血宰相》と共和国大統領の\x01",
            "対面は是非見てみたいもんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "長らく対立してきた両国だ、\x01",
            "どんな顔合わせになるやら……\x01",
            "ヒヒャヒャ、これは見物だよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B73")

    label("loc_1AC1")


    #C0077
    ChrTalk(
        0x8,
        (
            "明日からの通商会議じゃ、\x01",
            "《鉄血宰相》と共和国大統領の\x01",
            "対面は是非見てみたいもんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "長らく対立してきた両国だ、\x01",
            "どんな顔合わせになるやら……\x01",
            "ヒヒャヒャ、これは見物だよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B73")

    Jump("loc_20A5")

    label("loc_1B78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_END)), "loc_1CE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C5D")

    #C0079
    ChrTalk(
        0x8,
        (
            "どうやらさっき、目立つ連中が\x01",
            "ルバーチェ跡地のほうに\x01",
            "入っていったみたいだねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x8,
        (
            "あそこは黒月の連中が\x01",
            "手にするとばかり思っていたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、なんだか面白い事に\x01",
            "なっているみたいだね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CDF")

    label("loc_1C5D")


    #C0082
    ChrTalk(
        0x8,
        (
            "ルバーチェの跡地は、黒月の連中が\x01",
            "手にするとばかり思っていたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、なんだか面白い事に\x01",
            "なっているみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CDF")

    Jump("loc_20A5")

    label("loc_1CE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1F32")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E7B")

    #C0084
    ChrTalk(
        0x8,
        (
            "そういえば、裏路地の\x01",
            "ルバーチェの跡地だが……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x8,
        (
            "このままいけば黒月のものに\x01",
            "なりそうなんだってねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、こんなことになるなら\x01",
            "アタシが前もって押さえておいて、\x01",
            "高値で売りさばけばよかったね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0087
    ChrTalk(
        0x101,
        (
            "#00006F（そういえば、この人って\x01",
            "  土地成金だったな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F2D")

    label("loc_1E7B")


    #C0088
    ChrTalk(
        0x8,
        (
            "そういえば、裏路地の\x01",
            "ルバーチェの跡地……\x01",
            "黒月が手に入れそうだってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、こんなことになるなら\x01",
            "アタシが前もって押さえておいて、\x01",
            "高値で売りさばけばよかったね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F2D")

    Jump("loc_20A5")

    label("loc_1F32")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_20A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2041")

    #C0090
    ChrTalk(
        0x8,
        (
            "再始動した支援課、\x01",
            "今後も注目させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ……\x01",
            "またホットなニュースを提供して、\x01",
            "アタシを楽しませておくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#00012Fベ、別に楽しませるために\x01",
            "やってるわけじゃないですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x105,
        "#10309Fフフ、ホント面白いお婆さんだね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_20A5")

    label("loc_2041")


    #C0094
    ChrTalk(
        0x8,
        (
            "再始動した支援課、\x01",
            "今後も注目させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "ヒヒャヒャ、またアタシを\x01",
            "楽しませておくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20A5")

    Jump("loc_1EE")

    label("loc_20AA")

    TalkEnd(0x8)
    Return()

    # Function_3_19F end

    def Function_4_20AE(): pass

    label("Function_4_20AE")

    EventBegin(0x0)
    Fade(500)
    OP_68(-730, 1150, 2860, 0)
    MoveCamera(314, 24, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24040, 0)
    SetChrPos(0x101, -1540, 0, 1900, 45)
    SetChrPos(0x102, 390, 0, 2110, 0)
    SetChrPos(0x109, -1050, 0, 800, 0)
    SetChrPos(0x105, 150, 0, 830, 0)
    OP_0D()

    #C0096
    ChrTalk(
        0x8,
        "#11Pヒヒャヒャ、いらっしゃい。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0097
    ChrTalk(
        0x8,
        (
            "#11Pおや、アンタたちは\x01",
            "特務支援課の坊やたちかい。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x8,
        "#11Pヒヒャヒャ、久しぶりだねえ。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        "#6P#00000Fお久しぶりです、イメルダさん。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        "#6P#00100F相変わらずお元気そうですね。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x8,
        (
            "#11Pフン、元気なもんかい。\x01",
            "最近は退屈な日々に\x01",
            "飽き飽きしてたくらいさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x8,
        (
            "#11Pルバーチェも潰れちまったし、\x01",
            "アンタたちもしばらく活動休止……\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "#11Pついでに、よく利用していた\x01",
            "導力ネット上の情報屋まで\x01",
            "営業を休止しちまったしねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x102,
        "#6P#00105F（導力ネット上の情報屋って……）\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#6P#00003F（ヨナのことだろうな。\x01",
            "  今は財団に出向しているし……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0106
    ChrTalk(
        0x8,
        (
            "#11Pおや、そういえば見慣れない顔が\x01",
            "一緒にいるようだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x8,
        (
            "#11Pさては、支援課の新入りってのは\x01",
            "アンタたちかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "#11P警備隊員に不良チームの頭……\x01",
            "ヒヒャヒャ、再始動にあたって\x01",
            "面白い駒が揃ったようじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0109
    ChrTalk(
        0x109,
        "#6P#10105Fな、なんでそんなことを……\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#6P#00006Fえっと、情報屋を\x01",
            "利用してない割には\x01",
            "話に通じすぎていませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x8,
        (
            "#11Pヒヒャヒャヒャ……\x01",
            "別に情報ソースは\x01",
            "一つじゃないからねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x105,
        "#6P#10309Fアハハ、面白いお婆さんだ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0113
    ChrTalk(
        0x8,
        (
            "#11Pおっとそうだ。\x01",
            "わざわざ顔を出してくれた礼に、\x01",
            "アンタたちにいいものをやろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        "#11Pほれ、受け取りな。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0115
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x321),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x321, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0116
    ChrTalk(
        0x102,
        "#6P#00105Fこれは……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        (
            "#11Pヒヒャヒャ、\x01",
            "アタシが旧市街に所有してる\x01",
            "《メゾン・イメルダ》の鍵さね。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x105,
        (
            "#6P#10302Fああ、そういえば\x01",
            "そんな名前のボロアパートが\x01",
            "あの辺りにあったっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x8,
        "#11Pコラッ、ボロとはなんだい！\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x8,
        (
            "#11Pフン、まあいいさ。\x01",
            "近頃また魔獣が沸いてるようだし、\x01",
            "気が向いたら掃除しといておくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0121
    ChrTalk(
        0x101,
        (
            "#6P#00006Fた、確かにそこには\x01",
            "手配魔獣の退治依頼も\x01",
            "入ってきてますけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x109,
        "#6P#10106F結局、押し付けられちゃいましたね。\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x8,
        (
            "#11Pヒヒャヒャ……\x01",
            "まあ気が向いたらでいいさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x8,
        "#11Pよろしく頼んだよ、坊やたち。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -750, 0, 2000, 0)
    SetScenarioFlags(0x139, 4)
    OP_29(0x67, 0x1, 0x0)
    EventEnd(0x5)
    Return()

    # Function_4_20AE end

    def Function_5_2934(): pass

    label("Function_5_2934")

    EventBegin(0x0)
    Fade(500)
    SoundLoad(841)
    OP_68(-730, 1150, 2860, 0)
    MoveCamera(314, 24, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24040, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -250, 0, 2000, 0)
    SetChrPos(0x102, -1250, 0, 1750, 0)
    SetChrPos(0x103, -250, 0, 500, 0)
    SetChrPos(0x104, -1250, 0, 250, 0)
    SetChrPos(0x109, -2840, 0, 390, 44)
    SetChrPos(0x105, -1360, 0, -710, 44)
    OP_0D()
    BeginChrThread(0x9, 1, 0, 6)
    SetChrName("")

    #A0125
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "カウンターの下にある通信器で\x01",
            "イメルダ夫人が通話している。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x9, 1)

    #C0126
    ChrTalk(
        0x8,
        (
            "#11P……チッ、あのジジイめ。\x01",
            "ちっとも出やしない！\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        (
            "#6P#00005Fイメルダさん、\x01",
            "何かあったんですか？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2C9F")

    #C0128
    ChrTalk(
        0x8,
        "#11Pああ、アンタたちか。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x8,
        (
            "#11Pいや、次の新作人形について\x01",
            "ヨルグの奴に聞いておこうと思って、\x01",
            "連絡していたところなのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x102,
        "#00105Fヨルグ老人に……？\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x8,
        (
            "#11Pああ、だけどさっきから\x01",
            "一向に繋がる気配がなくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x8,
        (
            "#11P工房には居るんだろうが……\x01",
            "チッ、仕事をしてる最中なら\x01",
            "しばらくは繋がらないかねえ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    #C0133
    ChrTalk(
        0x101,
        (
            "#6P#00003F（……以前の依頼のとき、\x01",
            "  イメルダさんはヨルグ老人と\x01",
            "  旧い付き合いだと聞いた。）\x02\x03",

            "（この際だ、人形工房のこと……\x01",
            "  何か聞いてみるかな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30C0")

    label("loc_2C9F")


    #C0134
    ChrTalk(
        0x8,
        "#11Pああ、アンタたちか。\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x8,
        (
            "#11Pいや、次の新作人形について\x01",
            "ヨルグの奴に聞いておこうと思って、\x01",
            "連絡していたところなのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x8,
        (
            "#11Pだけど、さっきから\x01",
            "一向に繋がる気配がなくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x8,
        (
            "#11P工房には居るんだろうが……\x01",
            "チッ、仕事をしてる最中なら\x01",
            "しばらくは繋がらないかねえ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)
    Sleep(50)
    OP_64(0x102)
    Sleep(50)
    OP_64(0x103)
    Sleep(50)
    OP_64(0x104)
    Sleep(50)
    OP_64(0x109)
    Sleep(50)
    OP_64(0x105)

    #C0138
    ChrTalk(
        0x101,
        (
            "#6P#00005Fヨルグ……\x01",
            "それに新作人形って……\x02",
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
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0139
    ChrTalk(
        0x101,
        (
            "#6P#00005Fも、もしかして……\x01",
            "ヨルグ・ローゼンベルク技師！？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x102,
        (
            "#00105Fイメルダさん、\x01",
            "お知り合いだったんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "#11Pああ、一応ウチは\x01",
            "あそこの人形の販売代理を\x01",
            "請け負っているんでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        (
            "#11Pただ、こいつが偏屈なジジイでね。\x01",
            "色々融通が利かなくて\x01",
            "困らされる事も多いんだよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)

    #C0143
    ChrTalk(
        0x101,
        (
            "#6P#00006F（……こんな所に\x01",
            "  知り合いがいたなんてな。）\x02\x03",

            "（この際だ、人形工房のこと……\x01",
            "  何か聞いてみるかな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30C0")


    #C0144
    ChrTalk(
        0x8,
        (
            "#11P……それにしてもアンタたち、\x01",
            "アタシに何か用かい？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x8,
        (
            "#11Pヒヒャヒャ、\x01",
            "アンティークの取引きなら\x01",
            "いつでも応じさせてもらうよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        (
            "#6P#00000Fえ、えっと、そうではなくて。\x01",
            "ちょっとお聞きしたいのですが……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0147
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはローゼンベルク工房と\x01",
            "ヨルグ老人について尋ねてみた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0148
    ChrTalk(
        0x8,
        (
            "#11P……なんでまたアンタたちが\x01",
            "そんなことを嗅ぎ回ってんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x101,
        (
            "#6P#00012Fい、いや～……\x01",
            "ちょっとした興味本位というか。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x8,
        (
            "#11Pまあいいが……さすがのアタシも、\x01",
            "ヨルグについて知ってる事は\x01",
            "そう多くなくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x8,
        (
            "#11Pなんせ、普段はろくに表に出ずに\x01",
            "黙々と人形を作っているような\x01",
            "偏屈ジジイだからねえ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3389")

    #C0152
    ChrTalk(
        0x8,
        (
            "#11Pアルカンシェルの舞台装置なんかを\x01",
            "手がけてるのは前にも言ったが、\x01",
            "それ以上のことは知らないよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33D8")

    label("loc_3389")


    #C0153
    ChrTalk(
        0x8,
        (
            "#11P確かに販売代理を請け負っちゃいるが、\x01",
            "深い事情なんかはよく知らないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33D8")


    #C0154
    ChrTalk(
        0x109,
        "#10106Fそ、そうですか……\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x8,
        (
            "#11Pま、アタシはあの工房の人形で\x01",
            "一儲け出来さえすればいいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x8,
        (
            "#11Pあのジジイのプライベートなんて\x01",
            "知ったこっちゃないのさ。\x01",
            "ヒヒャヒャヒャ……\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x104,
        (
            "#6P#00303F（な、なるほど……\x01",
            "  意外とドライな関係なんだな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x103,
        (
            "#6P#00200F（だからこそ、\x01",
            "  付き合いが保たれているとも\x01",
            "  考えられますけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x105,
        (
            "#6P#10300F（ま、そういうことなら\x01",
            "  やっぱり直接訪ねてみるしか\x01",
            "  ないんじゃない？）\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        (
            "#6P#00000F（そうだな……\x01",
            "  みんな、行くとしよう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, -750, 0, 2000, 0)
    SetScenarioFlags(0x16F, 5)
    OP_24(0x349)
    EventEnd(0x5)
    Return()

    # Function_5_2934 end

    def Function_6_35E7(): pass

    label("Function_6_35E7")

    Sound(841, 2, 50, 0)
    Sleep(1800)
    OP_24(0x349)
    Sound(813, 0, 20, 0)
    Sleep(500)
    Return()

    # Function_6_35E7 end

    def Function_7_35FD(): pass

    label("Function_7_35FD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    FadeToBright(1000, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_7_35FD end

    SaveToFile()

Try(main)
