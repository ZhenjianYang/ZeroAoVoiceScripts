from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t2020.bin",                # FileName
        "t2020",                    # MapName
        "t2020",                    # Location
        0x0059,                     # MapIndex
        "ed7126",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 89, 0, 3, 0, 4],
    )

    BuildStringList((
        "t2020",                  # 0
        "ミレイユ准尉",           # 1
        "ブルード隊員",           # 2
    ))

    AddCharChip((
        "chr/ch32600.itc",                   # 00
        "chr/ch31200.itc",                   # 01
        "chr/ch23000.itc",                   # 02
    ))

    DeclNpc(-1309,   0,       42250,   0,    261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(40889,   0,       -30579,  315,  261,  0x0, 0,   1,   0,   0,   2,   0,   8,   255,  0)

    ScpFunction((
        "Function_0_10C",          # 00, 0
        "Function_1_1C4",          # 01, 1
        "Function_2_24D",          # 02, 2
        "Function_3_278",          # 03, 3
        "Function_4_351",          # 04, 4
        "Function_5_352",          # 05, 5
        "Function_6_502",          # 06, 6
        "Function_7_1DC1",         # 07, 7
        "Function_8_1F84",         # 08, 8
        "Function_9_22ED",         # 09, 9
        "Function_10_240C",        # 0A, 10
        "Function_11_3616",        # 0B, 11
        "Function_12_3E74",        # 0C, 12
    ))


    def Function_0_10C(): pass

    label("Function_0_10C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_14C"),
        (1, "loc_158"),
        (2, "loc_164"),
        (3, "loc_170"),
        (4, "loc_17C"),
        (5, "loc_188"),
        (6, "loc_194"),
        (SWITCH_DEFAULT, "loc_1A0"),
    )


    label("loc_14C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_158")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_164")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_170")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_17C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_188")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_194")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_1A0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_1AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1AC")

    label("loc_1C3")

    Return()

    # Function_0_10C end

    def Function_1_1C4(): pass

    label("Function_1_1C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_24C")
    OP_95(0xFE, -890, 0, 5100, 2000, 0x0)
    OP_95(0xFE, 12780, 0, 5100, 2000, 0x0)
    OP_95(0xFE, 12780, 0, 3300, 2000, 0x0)
    OP_95(0xFE, 860, 0, 3300, 2000, 0x0)
    OP_95(0xFE, 860, 0, -10930, 2000, 0x0)
    OP_95(0xFE, -890, 0, -10930, 2000, 0x0)
    Jump("Function_1_1C4")

    label("loc_24C")

    Return()

    # Function_1_1C4 end

    def Function_2_24D(): pass

    label("Function_2_24D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_277")
    OP_94(0xFE, 0x99A2, 0xFFFF838C, 0xA4BA, 0xFFFF8E40, 0x3E8)
    Sleep(300)
    Jump("Function_2_24D")

    label("loc_277")

    Return()

    # Function_2_24D end

    def Function_3_278(): pass

    label("Function_3_278")

    SetMapObjFrame(0xFF, "main03", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_29D")
    SetMapObjFrame(0xFF, "main03", 0x1, 0x1)

    label("loc_29D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2C1")
    SetChrPos(0x8, -40640, 0, 1570, 135)
    Jump("loc_322")

    label("loc_2C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_322")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2E5")
    SetChrFlags(0x8, 0x80)
    Jump("loc_31D")

    label("loc_2E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_30C")
    SetChrPos(0x8, -35130, 0, 4170, 0)
    SetChrFlags(0x8, 0x10)
    Jump("loc_31D")

    label("loc_30C")

    SetChrPos(0x8, -40640, 0, 1570, 135)

    label("loc_31D")

    Jump("loc_322")

    label("loc_322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_335")
    SetChrFlags(0x9, 0x80)

    label("loc_335")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_350")
    Event(0, 12)

    label("loc_350")

    Return()

    # Function_3_278 end

    def Function_4_351(): pass

    label("Function_4_351")

    Return()

    # Function_4_351 end

    def Function_5_352(): pass

    label("Function_5_352")

    TurnDirection(0xFE, 0x104, 0)

    #C0001
    ChrTalk(
        0xFE,
        "あ……あなた、ランディじゃないの！\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x104,
        (
            "#0300Fおお、ミレイユ曹長殿じゃねーか。\x01",
            "元気にしてたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        "あ、あいかわらず礼儀のない……\x02",
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "それに、今は昇級して准尉なの！\x01",
            "気安く呼びかけないでくれる？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#0300Fハハ、そうだったか。\x01",
            "悪い悪い。\x02\x03",

            "#0304Fでもまぁ……\x01",
            "俺はもう警備隊は抜けたし、\x01",
            "階級なんてぶっちゃけ関係ねぇよ。\x02\x03",

            "#0309Fこれからも気安く呼ばせてもらうぜ、\x01",
            "ミレイユ准尉殿。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "……もう！！\x01",
            "勝手にしなさい！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8C, 1)
    Return()

    # Function_5_352 end

    def Function_6_502(): pass

    label("Function_6_502")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_75C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_520")
    Call(0, 5)
    Jump("loc_757")

    label("loc_520")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6B0")

    #C0007
    ChrTalk(
        0xFE,
        (
            "ウルスラ医大で\x01",
            "研究が進められていた\x01",
            "栄養剤が届いたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "従来のものより\x01",
            "大幅に長い間、持続効果が得られる\x01",
            "画期的な品らしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x101,
        (
            "#0005Fさすがウルスラ医大……\x01",
            "手広くやってるなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x104,
        (
            "#0309Fなぁミレイユ。\x01",
            "せっかくだし俺らにも\x01",
            "そいつを分けてくれよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "ハイ、残念。\x01",
            "ピッタリ人数分しかなかったから\x01",
            "もう残っていないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x104,
        (
            "#0306Fぬぅ……なんだか、\x01",
            "妙に悔しい気分……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_757")

    label("loc_6B0")


    #C0013
    ChrTalk(
        0xFE,
        (
            "ウルスラ医大で研究が進められていた\x01",
            "栄養剤のサンプルが届いたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "今晩の演習はノックス大森林でやるから\x01",
            "疲労が大きいでしょうし、\x01",
            "上手く効果が現れるといいわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_757")

    Jump("loc_1DBD")

    label("loc_75C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_A44")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_777")
    Call(0, 5)
    Jump("loc_A3F")

    label("loc_777")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_96B")

    #C0015
    ChrTalk(
        0xFE,
        (
            "明日はノックス大森林を利用して、\x01",
            "標準装備を使った\x01",
            "夜戦演習を行う予定なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "警備隊の標準装備は\x01",
            "スタンハルバードとアサルトライフル。\x01",
            "隊員は両方の訓練をする義務があるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "……誰かさんはその規則に反して\x01",
            "スタンハルバードばっかり\x01",
            "扱ってたけれどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x104,
        (
            "#0309F……ハッハッハ、俺は接近戦が\x01",
            "性に合ってたんだから仕方ねぇだろ？\x02\x03",

            "#0300F何ならまた、見せてやろうか？\x01",
            "ライフルの弾より素早い\x01",
            "ランディ様のハルバード捌きを……！\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "ハァ、まったく……\x01",
            "相変わらずお調子者なんだから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_A3F")

    label("loc_96B")


    #C0020
    ChrTalk(
        0xFE,
        (
            "警備隊の標準装備は\x01",
            "スタンハルバードとアサルトライフル。\x01",
            "隊員は両方の訓練をする義務があるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "……ランディがきちんと\x01",
            "ライフルの訓練をしてくれてれば……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "……いや、やめましょう。\x01",
            "過ぎたことだものね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3F")

    Jump("loc_1DBD")

    label("loc_A44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_DD4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A5F")
    Call(0, 5)
    Jump("loc_DCF")

    label("loc_A5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D04")
    TurnDirection(0xFE, 0x109, 0)

    #C0023
    ChrTalk(
        0xFE,
        "あなたは……ノエル曹長ね。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "タングラム門に\x01",
            "誠実かつ有能な隊員がいるという\x01",
            "噂を聞いた事があるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x109,
        (
            "#0503Fいえ、私なんてまだまだです。\x02\x03",

            "#0500Fミレイユ准尉のほうこそ、\x01",
            "よくあの司令の下で\x01",
            "挫けずに職務を貫いて……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x104,
        (
            "#0300Fはは、ミレイユは昔っから\x01",
            "正義感だけは人一倍あるからなぁ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)

    #C0027
    ChrTalk(
        0xFE,
        "だ、「だけ」ってなによ「だけ」って！？\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#0006Fほ、ほらランディ。\x01",
            "からかうのもいい加減にしろって。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x104,
        "#0304Fへいへい。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        "……まったくもう。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x109, 500)

    #C0031
    ChrTalk(
        0xFE,
        (
            "ともかく、ノエル曹長のような\x01",
            "優秀な隊員がいるのは\x01",
            "上官としてとても嬉しいことです。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "いつかこの警備隊を\x01",
            "あるべき姿に正していけるよう、\x01",
            "お互いがんばりましょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x109,
        "#0501Fは、はいっ！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD8, 0)
    Jump("loc_DCF")

    label("loc_D04")


    #C0034
    ChrTalk(
        0xFE,
        (
            "本当なら例の遺跡の調査は\x01",
            "私達の手でやりたかったけど\x01",
            "司令の命令じゃ仕方ないもの……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "……ノエル曹長、特務支援課の皆さん。\x01",
            "どうかよろしく頼んだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        "#0304Fま、大船に乗ったつもりでいてくれや。\x02",
    )

    CloseMessageWindow()

    label("loc_DCF")

    Jump("loc_1DBD")

    label("loc_DD4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_FF5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DFE")
    Call(0, 7)
    TalkEnd(0xFE)
    Return()

    label("loc_DFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E10")
    Call(0, 5)
    Jump("loc_FF0")

    label("loc_E10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F61")

    #C0037
    ChrTalk(
        0xFE,
        (
            "記念祭中は私が門を指揮していたけど、\x01",
            "とりあえずそれも今日で終わりね。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "幸い大きなトラブルも起こさずに\x01",
            "終えることができたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        (
            "#0303F……だがまぁ、あの司令のことだ。\x01",
            "これからも無責任に\x01",
            "門を空けたりすんだろ。\x02\x03",

            "#0300Fミレイユ、おまえがちゃんと\x01",
            "隊員どもをリードしてかないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        "……ええ、分かってるわ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FF0")

    label("loc_F61")


    #C0041
    ChrTalk(
        0xFE,
        (
            "大きなトラブルを起こさずに\x01",
            "記念祭中の検問を終えられて\x01",
            "ほっとしているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "これからも、隊員たちが\x01",
            "道を見失わないように頑張らないと……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FF0")

    Jump("loc_1DBD")

    label("loc_FF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_12A8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_101F")
    Call(0, 7)
    TalkEnd(0xFE)
    Return()

    label("loc_101F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1031")
    Call(0, 5)
    Jump("loc_12A3")

    label("loc_1031")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11C2")

    #C0043
    ChrTalk(
        0xFE,
        (
            "司令の代理で、\x01",
            "出入国者の通行許可申請書を\x01",
            "整理していたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "……そういえばランディは、\x01",
            "今私がやっているような\x01",
            "事務的な仕事はほとんどしなかったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x104,
        (
            "#0306Fああ、めんどくさかったからな。\x02\x03",

            "大抵カーターやコナーズの奴に\x01",
            "押し付けてサボってたぜ。\x02\x03",

            "#0309Fその代わり、歓楽街で知り合った\x01",
            "女の子を紹介してやったり。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        (
            "（……あの２人は今度、\x01",
            "  問い詰める必要がありそうね……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12A3")

    label("loc_11C2")


    #C0047
    ChrTalk(
        0xFE,
        (
            "ランディ……\x01",
            "まさかあなた、特務支援課でも\x01",
            "同じことしてないでしょうね……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        (
            "#0309Fはは、まさかァ。\x01",
            "ロイドに仕事押し付けて、\x01",
            "代わりに女の子を紹介なんてことは……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#0011Fそ、そんな言い方すると\x01",
            "してるみたいだろっ！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12A3")

    Jump("loc_1DBD")

    label("loc_12A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1511")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12D2")
    Call(0, 7)
    TalkEnd(0xFE)
    Return()

    label("loc_12D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12E4")
    Call(0, 5)
    Jump("loc_150C")

    label("loc_12E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14B9")

    #C0050
    ChrTalk(
        0xFE,
        (
            "ふぅ……事務作業は嫌いじゃないけど\x01",
            "なかなか大変なものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        (
            "#0304Fああ、ミレイユ准尉殿は\x01",
            "武闘派でらっしゃるからな。\x02\x03",

            "#0300Fなんせ、武術の腕前で言えば\x01",
            "ベルガード門の男どもを抑えて\x01",
            "１、２を争うほどだ。\x02\x03",

            "椅子に座っての作業は\x01",
            "そりゃあ退屈だろうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        "んなっ……！\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "そんな言い方じゃ、\x01",
            "私が脳みそまで筋肉で\x01",
            "できているみたいじゃない！\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x104,
        (
            "#0309Fおっと失礼。\x01",
            "ウソは言ってないんだけどなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "……はぁ。\x01",
            "もういいから邪魔しないでちょうだい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_150C")

    label("loc_14B9")


    #C0056
    ChrTalk(
        0xFE,
        (
            "……はぁ、\x01",
            "私はこれでも忙しいのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        "もういいから邪魔しないでちょうだい。\x02",
    )

    CloseMessageWindow()

    label("loc_150C")

    Jump("loc_1DBD")

    label("loc_1511")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1863")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_1614")
    TurnDirection(0x8, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15C5")

    #C0058
    ChrTalk(
        0xFE,
        (
            "私は徹底的にこの司令室を\x01",
            "洗ってみるつもりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "押し付けられたとはいえ、\x01",
            "重要な仕事だもの。\x01",
            "意地でもやり通すんだから……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1608")

    label("loc_15C5")


    #C0060
    ChrTalk(
        0xFE,
        (
            "そちらの捜査はお任せします。\x01",
            "……どうかよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1608")

    OP_93(0x8, 0x0, 0x0)
    Jump("loc_185E")

    label("loc_1614")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_1628")
    Call(0, 10)
    Jump("loc_185E")

    label("loc_1628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_163A")
    Call(0, 5)
    Jump("loc_185E")

    label("loc_163A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D5")

    #C0061
    ChrTalk(
        0xFE,
        (
            "昨日から記念祭だけど……\x01",
            "司令は記念祭の間は\x01",
            "出張らしいわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "司令代理として、\x01",
            "きちんと門の警備を\x01",
            "取り仕切らないといけないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x104,
        (
            "#0300F警備隊員は精鋭揃いだから、\x01",
            "不在がちな司令の下でも\x01",
            "なんとかやっていけてんだ。\x02\x03",

            "#0304F……ま、気ぃ張りすぎて\x01",
            "昔みたいに余計な失敗を\x01",
            "するんじゃねぇぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "（このっ……\x01",
            "  い、言わなくていいことを……！）\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        "#0006F（な、なにをやったんだろう……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_185E")

    label("loc_17D5")


    #C0066
    ChrTalk(
        0xFE,
        (
            "記念祭中は交通量が増えるし、\x01",
            "トラブルの発生も予想されるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "司令代理として、\x01",
            "きちんと門の警備を\x01",
            "取り仕切らないといけないわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_185E")

    Jump("loc_1DBD")

    label("loc_1863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1CDF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_187E")
    Call(0, 5)
    Jump("loc_1CDA")

    label("loc_187E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC9")
    TurnDirection(0xFE, 0x104, 0)

    #C0068
    ChrTalk(
        0xFE,
        (
            "……ランディ、あなた……\x01",
            "あまりベルガード門を\x01",
            "うろつかない方がいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#0304Fハハッ、なんだなんだミレイユ。\x01",
            "心配してくれるなんて珍しいな。\x02\x03",

            "#0300Fそういえば俺がベルガード門を\x01",
            "クビになるとき、\x01",
            "熱心に反対してくれてたらしいな。\x02\x03",

            "#0305F……まさかお前、俺のこと……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        "バッ、バカなこと言わないでよ！\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "私はただ、あの程度のことで\x01",
            "貴重な隊員を失う事はないと……！\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        "#0005Fあの程度のことっていうと……\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x103,
        (
            "#0200F……あぁ、例の\x01",
            "女性関係のいざこざがどうとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x102,
        (
            "#0106F追い出されるほど\x01",
            "女性にかまけるなんて\x01",
            "ランディくらいのものよね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0075
    ChrTalk(
        0xFE,
        "……女性関係のいざこざ……？\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x104,
        (
            "#0309F──なんだミレイユ！\x01",
            "そんなにテレることないだろ～？\x02\x03",

            "#0304Fこのランディさまに\x01",
            "淡い恋心を抱いていた。\x01",
            "言っちまえばラクになるぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "……はぁ、もういいわ。\x01",
            "話しててもラチがあかないし……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1CDA")

    label("loc_1BC9")


    #C0078
    ChrTalk(
        0xFE,
        (
            "私は確かに、\x01",
            "ランディが解雇されるのを\x01",
            "反対していたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "けどそれは、れ……恋愛感情とか\x01",
            "そういうものではなくて、\x01",
            "あくまで合理的に考えての──\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x104,
        (
            "#0306Fまぁ、要するに\x01",
            "俺が去るのが寂しくて\x01",
            "しょうがなかったってコトか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)

    #C0081
    ChrTalk(
        0xFE,
        "……もう、勝手にそう思ってなさい！\x02",
    )

    CloseMessageWindow()

    label("loc_1CDA")

    Jump("loc_1DBD")

    label("loc_1CDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1DBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CFA")
    Call(0, 5)
    Jump("loc_1DBD")

    label("loc_1CFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D7A")

    #C0082
    ChrTalk(
        0xFE,
        (
            "はぁ、警備隊を抜けても\x01",
            "ちっとも変わってないんだから……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "あなた達もランディのお守りは\x01",
            "大変でしょう？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DBD")

    label("loc_1D7A")


    #C0084
    ChrTalk(
        0xFE,
        (
            "あなたたちも気を付けなさいよ。\x01",
            "その男は操縦が大変なんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DBD")

    TalkEnd(0xFE)
    Return()

    # Function_6_502 end

    def Function_7_1DC1(): pass

    label("Function_7_1DC1")


    #C0085
    ChrTalk(
        0xFE,
        "あ……特務支援課の皆さん。\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#0005Fミレイユ准尉……\x01",
            "え、えっと……\x02\x03",

            "#0003F先日の起動キー捜索の件……\x01",
            "途中でやめてしまってすみませんでした。\x01",
            "どうしても外せない用がありまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        "いえ、気にしないでください。\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "あの後、なんとか徹夜で探して\x01",
            "起動キーを見つけることができましたから。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x104,
        "#0303F……悪いな、マジで。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)

    #C0090
    ChrTalk(
        0xFE,
        "ふふ、らしくないじゃない。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "まぁ、あなたたちも忙しいんだし\x01",
            "仕方ないことだと思うわ。\x01",
            "本当に気にしないで。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xD8, 3)
    Return()

    # Function_7_1DC1 end

    def Function_8_1F84(): pass

    label("Function_8_1F84")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_205A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_201A")

    #C0092
    ChrTalk(
        0xFE,
        (
            "今日は街道の森林を利用した\x01",
            "夜戦演習だそうだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "相変わらずこじんまりとやるしかないのが\x01",
            "なんだか情けないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2055")

    label("loc_201A")


    #C0094
    ChrTalk(
        0xFE,
        (
            "……まぁ、やるしかないんだけどね。\x01",
            "はぁ、情けないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2055")

    Jump("loc_22E9")

    label("loc_205A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2116")

    #C0095
    ChrTalk(
        0xFE,
        (
            "タングラム門に勤めてるバレルが\x01",
            "遺跡の調査が終わったって喜んでたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "特務支援課の君たちが\x01",
            "ノエル曹長を手伝ってくれたんだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        "僕からも礼を言うよ、ありがとう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_22E9")

    label("loc_2116")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_21D1")

    #C0098
    ChrTalk(
        0xFE,
        (
            "この間、タングラム門のバレルから\x01",
            "アルカンシェルの新人リーシャ・マオの\x01",
            "ポスターをもらったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "折角だからそこに貼ってみたんだが……\x01",
            "ううむ、なかなかいいものだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22E9")

    label("loc_21D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2254")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x9C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21EC")
    Call(0, 9)
    Jump("loc_224F")

    label("loc_21EC")


    #C0100
    ChrTalk(
        0xFE,
        (
            "このベルガード門で\x01",
            "司令のもと働く俺には分かる……\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        "上司が無能ってのはなによりの不幸だよ。\x02",
    )

    CloseMessageWindow()

    label("loc_224F")

    Jump("loc_22E9")

    label("loc_2254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_22E9")

    #C0102
    ChrTalk(
        0xFE,
        (
            "司令はよく司令部を空けてるから\x01",
            "実際はミレイユ准尉の指揮下なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        (
            "准尉はちょっと頼りないけど、\x01",
            "一生懸命やってくれるいい上官だよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22E9")

    TalkEnd(0xFE)
    Return()

    # Function_8_1F84 end

    def Function_9_22ED(): pass

    label("Function_9_22ED")


    #C0104
    ChrTalk(
        0xFE,
        (
            "さぁて、休憩も終わったし\x01",
            "今日も頑張らなくちゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "司令のためじゃなくて\x01",
            "ミレイユ准尉のためだと思えば\x01",
            "仕事も苦じゃないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "そうそう、この本。\x01",
            "休憩中に読み終わっちゃったから\x01",
            "君たちにあげるよ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0107
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2CA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2CA, 1)
    SetScenarioFlags(0x9C, 4)
    Return()

    # Function_9_22ED end

    def Function_10_240C(): pass

    label("Function_10_240C")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-35280, 900, 2640, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24100, 0)
    SetChrPos(0x101, -34000, 0, 1500, 0)
    SetChrPos(0x102, -35300, 0, 1000, 0)
    SetChrPos(0x103, -34000, 0, 500, 0)
    SetChrPos(0x104, -35300, 0, 2000, 0)
    OP_93(0x8, 0x0, 0x0)
    SetChrSubChip(0x8, 0x0)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x19, 0x1, 0x1)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3595")

    #C0108
    ChrTalk(
        0x8,
        (
            "#11Pああ、もう……\x01",
            "一体どこにいったのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x8,
        "#11P早く探し出さないと……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8C, 1)), scpexpr(EXPR_END)), "loc_262F")

    #C0110
    ChrTalk(
        0x104,
        (
            "#6P#0300Fよう、ミレイユ。\x01",
            "元気にしてたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        "#0000F准尉、お疲れ様です。\x02",
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x12C)

    #C0112
    ChrTalk(
        0x8,
        (
            "#11P……ランディ？\x01",
            "それに、特務支援課の皆さん……\x01",
            "何でこんな所に……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0113
    ChrTalk(
        0x8,
        (
            "#11Pあっ、支援要請を\x01",
            "出していたんだったわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x8,
        (
            "#11Pすみません私ったら、\x01",
            "すっかり忘れてて……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_280E")

    label("loc_262F")


    #C0115
    ChrTalk(
        0x104,
        (
            "#6P#0300Fよう、ミレイユ。\x01",
            "元気にしてたか？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x12C)

    #C0116
    ChrTalk(
        0x8,
        "#11P……ランディ？\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x8,
        (
            "#11Pあ……あなた、ランディじゃないの！\x01",
            "なんでこんな所に……\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x8,
        "#11Pそれに、そちらは……？\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#12P#0005Fあ、えっと……\x01",
            "警察・特務支援課の\x01",
            "ロイド・バニングスです。\x02\x03",

            "#0000F今回は支援要請を受けて\x01",
            "こちらに伺いました。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0120
    ChrTalk(
        0x8,
        (
            "#11P……あっ……\x01",
            "そうか、ランディが今、\x01",
            "所属してるのって……\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x8,
        (
            "#11Pそれに、支援要請を出していたことを\x01",
            "すっかり忘れていたわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_280E")

    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0122
    ChrTalk(
        0x102,
        (
            "#6P#0109Fえっと……\x01",
            "よほど忙しかったんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x104,
        (
            "#6P#0304Fはは、相変わらず\x01",
            "真面目なフリして\x01",
            "どっか抜けてんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x8,
        "#11Pな、なんですって！？\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x8,
        (
            "#11Pあなたなんかに\x01",
            "言われる筋合いは……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        (
            "#12P#0006Fあ、あの、とにかく\x01",
            "落ち着いてください。\x02\x03",

            "#0001Fさっそくなんですが……\x01",
            "支援課を呼んだ理由を\x01",
            "説明していただけませんか？\x02\x03",

            "優秀な警備隊が\x01",
            "俺たちを呼ぶくらいですから、\x01",
            "なにかあったんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x8,
        (
            "#11P……こほん、そうですね。\x01",
            "少々取り乱してしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x8,
        (
            "#11P……今、ベルガード門では\x01",
            "ある重要な品物を捜索しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x8,
        (
            "#11P本来なら最重要優先事項なんですが、\x01",
            "ご覧の通り、記念祭のシーズンで\x01",
            "人手を割けない状態なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x8,
        (
            "#11Pですから、今回は私の独断で\x01",
            "皆様をお呼びした次第です。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x102,
        (
            "#6P#0103Fなるほど……事情はわかりました。\x02\x03",

            "#0105Fそれで、その重要な品物とは？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x8,
        (
            "#11Pそれは……\x01",
            "最近、警備隊に配備されたばかりの\x01",
            "新型装甲車両の起動キーなのです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0133
    ChrTalk(
        0x101,
        "#12P#0005F新型装甲車両っ……！？\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x103,
        (
            "#6P#0200F情報だけは知っていましたが……\x01",
            "すでに配備されていたのですか。\x02\x03",

            "しかしなぜ、\x01",
            "そのような大切なものを……？\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x104,
        "#6P#0301F……司令、だな？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_2D2C():
        TurnDirection(0xFE, 0x104, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D2C)

    def lambda_2D39():
        TurnDirection(0xFE, 0x104, 300)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D39)

    def lambda_2D46():
        TurnDirection(0xFE, 0x104, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2D46)
    Sleep(1000)

    #C0136
    ChrTalk(
        0x8,
        "#11P……やはり分かってしまうわね。\x02",
    )

    CloseMessageWindow()

    def lambda_2D7E():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D7E)

    def lambda_2D8B():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2D8B)

    def lambda_2D98():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D98)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x101, 1)

    #C0137
    ChrTalk(
        0x101,
        "#12P#0005Fど、どういうことなんですか？\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x8,
        (
            "#11P実は昨日……司令の接待先で、\x01",
            "記念祭の祝賀会が開かれたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x8,
        (
            "#11Pお酒をあおって\x01",
            "すっかり酔ってしまわれた司令は……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x8,
        (
            "#11P配備されたばかりの新型装甲車を\x01",
            "部下に運転させ、祝賀会の方に\x01",
            "持ち出してしまったのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x104,
        (
            "#6P#0303F大方、お偉方にお披露目して\x01",
            "ご機嫌をとろうってトコだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x103,
        "#6P#0200F……下品ですね。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x8,
        (
            "#11P……そして、帰ってきた司令は、\x01",
            "門の内部に新型装甲車を停めさせた後、\x01",
            "起動キーを部下から取り上げて……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x8,
        (
            "#11P挙句の果てに、\x01",
            "どこかに紛失してしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x8,
        (
            "#11Pキーがなければ移動できませんから\x01",
            "苦肉の策としてあのようなカバーを\x01",
            "被せてみたのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        (
            "#12P#0005Fあ……あれが新型装甲車だったのか。\x02\x03",

            "#0001Fしかし、あのカバーは逆効果では？\x01",
            "却って悪目立ちしていた気が……\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x102,
        (
            "#6P#0101Fでも、そのままにしておけば\x01",
            "色々と面倒な問題が起こってしまうわ。\x02\x03",

            "#0103F警備隊の新武装とされる装甲車を\x01",
            "国境門内部に配備する……\x02\x03",

            "#0101Fエレボニア帝国への\x01",
            "敵対行動ととられてしまっても、\x01",
            "文句は言えないもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x101,
        "#12P#0005Fそ、そんな大事になるのか……！？\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x8,
        (
            "#11P……少なくとも、悪い刺激を\x01",
            "与えてしまうでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x104,
        (
            "#6P#0303Fふむ……しかし新型ってのは\x01",
            "そんなに大したモンなのか？\x02\x03",

            "#0300F今運用されてるタイプも、\x01",
            "装甲の強度と機動力だけ見れば\x01",
            "なかなかのモンだとは思うが。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x8,
        (
            "#11P新型は、従来の装甲車を\x01",
            "より戦闘向きに改良したものなの。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x8,
        (
            "#11Pバルカン砲と小型ミサイルポッドを\x01",
            "搭載し、大幅に火力性能を高めているわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x8,
        (
            "#11P現在の警備隊の武装では\x01",
            "最強の部類にあたるでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x104,
        (
            "#6P#0301F……なるほどな。\x01",
            "さすがに門の内部に放っておいて\x01",
            "いいモンじゃなさそうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0155
    ChrTalk(
        0x104,
        (
            "#6P#0303F……で？\x01",
            "噂の司令殿は一体どこで\x01",
            "何してやがるんだ。\x02\x03",

            "#0301F確かここはヤツの部屋だよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x8,
        (
            "#11P司令は今朝、\x01",
            "キーの捜索を私たちに任せて\x01",
            "出かけてしまったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x8,
        (
            "#11P記念祭中の接待を\x01",
            "無下に出来ないと言って……\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x104,
        "#6P#0303F……ちっ、相変わらずだな。\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x103,
        (
            "#6P#0200F聞けば聞くほど\x01",
            "救いようのない人物ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x8,
        (
            "#11Pとにかく……\x01",
            "一刻も早く新型車両を\x01",
            "別の場所に移したいんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x8,
        (
            "#11P起動キーの捜索……\x01",
            "お手伝いしていただけませんか？\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x19, 0x1, 0x1)
    SetScenarioFlags(0x8C, 1)
    Jump("loc_3612")

    label("loc_3595")

    OP_93(0x8, 0xB4, 0x1F4)

    #C0162
    ChrTalk(
        0x8,
        (
            "#11P一刻も早く新型車両を\x01",
            "駐車場の方に移したいんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x8,
        (
            "#11P起動キーの捜索……\x01",
            "お手伝いしていただけませんか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3612")

    Call(0, 11)
    Return()

    # Function_10_240C end

    def Function_11_3616(): pass

    label("Function_11_3616")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【引き受ける】\x01",      # 0
            "【やめる】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_366F"),
        (1, "loc_3D3E"),
        (SWITCH_DEFAULT, "loc_3E32"),
    )


    label("loc_366F")

    OP_60(0x0)

    #C0164
    ChrTalk(
        0x101,
        "#12P#0001F分かりました、引き受けましょう。\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x8,
        (
            "#11Pあ……ありがとうございます。\x01",
            "助かります……！\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x102,
        (
            "#6P#0101Fそれでは……\x01",
            "念のため、司令の足取りを\x01",
            "お聞きしておきたいのですが。\x02\x03",

            "何か司令から\x01",
            "お聞きになっていませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x8,
        (
            "#11Pそうですね……\x01",
            "今朝までに司令に聞き出した\x01",
            "ことでよければ。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x103,
        "#6P#0203F……お願いします。\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x8,
        (
            "#11P……まず、帰ってきた司令は\x01",
            "装甲車を門内部に停車させた後、\x01",
            "部下から起動キーを取り上げました。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x8,
        (
            "#11P恐らく……祝賀会で飲んだお酒の締めに\x01",
            "ツマミが欲しかったんでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x8,
        (
            "#11Pそのまま食堂に立ち寄って\x01",
            "軽食を作らせたそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x8,
        (
            "#11Pそして、気分の赴くまま屋上に出て\x01",
            "ひとしきり歌ったあと……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x8,
        (
            "#11Pふと、起動キーがないことに\x01",
            "気づいたそうです。\x02",
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

    #C0174
    ChrTalk(
        0x103,
        (
            "#6P#0203Fそれはまた……\x01",
            "いい具合に酔っ払っていたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x101,
        (
            "#12P#0006Fな、なんというか……\x01",
            "そこまで来ると天晴れな気がするけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x104,
        "#6P#0301Fやれやれだぜ。\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x102,
        (
            "#6P#0101Fでも……その話のどこかで\x01",
            "キーを紛失したのは確かなようね。\x02\x03",

            "#0103Fだとすると、やはりベルガード門内に\x01",
            "ある可能性が高いと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            "#12P#0003Fああ、確かにそうだな。\x02\x03",

            "#0000Fよし、それじゃあ……\x01",
            "その周辺を一通り調べてみるとしよう。\x02\x03",

            "もしかしたらまた新しい事実が\x01",
            "判明するかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x103,
        (
            "#6P#0200Fミレイユ准尉は\x01",
            "わたしたちと一緒に捜索しますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x8,
        (
            "#11Pいえ……捜査方針が決まったなら、\x01",
            "私がいても邪魔になるだけです。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x8,
        (
            "#11P私は徹底的にこの司令室を\x01",
            "洗ってみます。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x104,
        (
            "#6P#0304Fま、あとは俺たちに任せて、\x01",
            "ドロ舟に乗った気持ちで\x01",
            "ドンと構えていてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x8,
        "#11Pもう……本当に頼むわよ。\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        (
            "#12P#0000Fとにかく捜査開始だ。\x02\x03",

            "まずは件の新型装甲車両を\x01",
            "調べてみよう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    Sound(80, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0185
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【重要紛失物の捜索】\x07\x00",
            "を開始した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_29(0x19, 0x1, 0x2)
    Jump("loc_3E41")

    label("loc_3D3E")

    OP_60(0x0)

    #C0186
    ChrTalk(
        0x101,
        (
            "#12P#0006Fすみません、申し訳ないのですが……\x01",
            "外せない用事が残っていまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x8,
        (
            "#11Pそう、ですか……\x01",
            "仕方ありませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x8,
        (
            "#11Pもし用事が終わったら、\x01",
            "もう一度声をかけてくれると\x01",
            "助かります。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x8,
        "#11Pどうかよろしくお願いします。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E41")

    label("loc_3E32")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E41")

    label("loc_3E41")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0x8, 0x0, 0x0)
    SetChrPos(0x0, -34470, 0, 200, 90)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_3616 end

    def Function_12_3E74(): pass

    label("Function_12_3E74")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-42850, 900, 590, 0)
    MoveCamera(294, 21, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(29780, 0)
    SetChrPos(0x101, -33410, 0, -910, 225)
    SetChrPos(0x102, -32170, 0, 1270, 315)
    SetChrPos(0x103, -33510, 0, 870, 315)
    SetChrPos(0x104, -32220, 0, -420, 270)
    Sleep(500)
    OP_68(-36150, 900, 890, 5000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)

    #C0190
    ChrTalk(
        0x101,
        "#0005Fここは……？\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x104,
        "#0301F……警備隊司令閣下殿の部屋だな。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0192
    ChrTalk(
        0x101,
        (
            "#0005F当の司令はいないみたいだけど……\x02\x03",

            "どこかに出かけてるのか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x104,
        (
            "#0306Fああ、どうせ接待か何かだろうよ。\x02\x03",

            "仕事は基本的に、部下に任せきりだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x101,
        (
            "#0000Fうーん……だとすると\x01",
            "司令に会うのは諦めた方がよさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x104,
        (
            "#0305Fああ？　会うつもりだったのか？\x02\x03",

            "#0306Fお前なぁ……俺にとっちゃ元上司だぞ。\x01",
            "気まずいなんてレベルじゃねーだろが。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x101,
        "#0000Fそ、そりゃそうだな。\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x102,
        (
            "#0106F……それにしても、\x01",
            "随分と悪趣味な部屋ね。\x02\x03",

            "#0101F棚に並んでる骨董品なんて\x01",
            "数万ミラはしそう……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x103,
        (
            "#0200F……というか、警備隊司令の部屋とは\x01",
            "とても思えないんですが。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0199
    ChrTalk(
        0x104,
        (
            "#0300Fたっぷり溜め込んだ賄賂だの\x01",
            "なんだのを使って揃えたみたいだな。\x02\x03",

            "#0306Fしかしまぁ、もったいねぇよなぁ。\x01",
            "俺がそんだけミラを持ってたら\x01",
            "歓楽街でパーッとばらまくんだが。\x02\x03",

            "キレーな姉ちゃんはべらせて、\x01",
            "一晩中カジノで遊んでよぉ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 500)

    #C0200
    ChrTalk(
        0x103,
        "#0211F……どっちもどっちです。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -32220, 0, -420, 270)
    SetScenarioFlags(0x6F, 7)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_12_3E74 end

    SaveToFile()

Try(main)
