from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4400.bin",                # FileName
        "e4400",                    # MapName
        "e4400",                    # Location
        0x0000,                     # MapIndex
        "ed7570",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "e4400",                  # 0
        "エリィ",                 # 1
        "リーシャ",               # 2
        "神狼ツァイト",           # 3
        "グレイス",               # 4
    ))

    AddCharChip((
        "chr/ch00100.itc",                   # 00
        "chr/ch03200.itc",                   # 01
        "chr/ch02708.itc",                   # 02
        "chr/ch06000.itc",                   # 03
    ))

    DeclNpc(-2930,   0,       509,     270,  389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(2589,    0,       -29,     90,   389,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(-1549,   0,       -959,    180,  405,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-2930,   0,       509,     270,  389,  0x0, 0,   3,   0,   0,   0,   0,   9,   255,  0)

    ChipFrameInfo(324, 0)                                        # 0

    ScpFunction((
        "Function_0_144",          # 00, 0
        "Function_1_1F4",          # 01, 1
        "Function_2_2BE",          # 02, 2
        "Function_3_382",          # 03, 3
        "Function_4_577",          # 04, 4
        "Function_5_9B5",          # 05, 5
        "Function_6_D63",          # 06, 6
        "Function_7_105E",         # 07, 7
        "Function_8_1432",         # 08, 8
        "Function_9_1611",         # 09, 9
        "Function_10_1D3F",        # 0A, 10
        "Function_11_1F83",        # 0B, 11
    ))


    def Function_0_144(): pass

    label("Function_0_144")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_17C"),
        (1, "loc_188"),
        (2, "loc_194"),
        (3, "loc_1A0"),
        (4, "loc_1AC"),
        (5, "loc_1B8"),
        (6, "loc_1C4"),
        (SWITCH_DEFAULT, "loc_1D0"),
    )


    label("loc_17C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_188")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_194")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1A0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1AC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1B8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1C4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1D0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_1DC")

    label("loc_1F3")

    Return()

    # Function_0_144 end

    def Function_1_1F4(): pass

    label("Function_1_1F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_207")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_2A8")

    label("loc_207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_21A")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_2A8")

    label("loc_21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_22D")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_2A8")

    label("loc_22D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_240")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_2A8")

    label("loc_240")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_253")
    ClearChrFlags(0x8, 0x80)
    Jump("loc_2A8")

    label("loc_253")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_266")
    ClearChrFlags(0xB, 0x80)
    Jump("loc_2A8")

    label("loc_266")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_279")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_2A8")

    label("loc_279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_28C")
    ClearChrFlags(0x9, 0x80)
    Jump("loc_2A8")

    label("loc_28C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_29A")
    Jump("loc_2A8")

    label("loc_29A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2A8")
    ClearChrFlags(0xA, 0x80)

    label("loc_2A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_2BD")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 11)

    label("loc_2BD")

    Return()

    # Function_1_1F4 end

    def Function_2_2BE(): pass

    label("Function_2_2BE")

    OP_50(0x31, (scpexpr(EXPR_PUSH_LONG, 0xD0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2E4")
    Sound(132, 1, 70, 0)
    Sound(497, 1, 30, 0)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_2F0")

    label("loc_2E4")

    Sound(132, 1, 100, 0)
    Sound(497, 1, 100, 0)

    label("loc_2F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_305")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_305")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x7D0)
    SetMapFlags(0x10000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_345")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33C")
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x0)
    Jump("loc_345")

    label("loc_33C")

    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_345")

    SetMapObjFrame(0x0, "door_l1", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_l2", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_r1", 0x0, 0x1)
    SetMapObjFrame(0x0, "door_r2", 0x0, 0x1)
    Return()

    # Function_2_2BE end

    def Function_3_382(): pass

    label("Function_3_382")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_397")
    Call(0, 4)
    Jump("loc_573")

    label("loc_397")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B9")

    #C0001
    ChrTalk(
        0xFE,
        (
            "#00103F『独立国』の無効宣言……\x01",
            "それが本当に正しいのかは\x01",
            "まだ分からないけど……\x02\x03",

            "#00101Fキーアちゃんを犠牲にした上で\x01",
            "与えられた平和だなんて、\x01",
            "絶対に間違っているわよね。\x02\x03",

            "#00103Fキーアちゃんを取り戻す……\x01",
            "その第一歩を踏み出すためにも、\x01",
            "この作戦は必ず成功させなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_573")

    label("loc_4B9")


    #C0002
    ChrTalk(
        0xFE,
        (
            "#00103F『独立国』の無効宣言……\x01",
            "それが本当に正しいのかは\x01",
            "まだ分からないけど……\x02\x03",

            "#00100Fキーアちゃんを取り戻す……\x01",
            "その第一歩を踏み出すためにも、\x01",
            "この作戦は必ず成功させなくちゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_573")

    TalkEnd(0xFE)
    Return()

    # Function_3_382 end

    def Function_4_577(): pass

    label("Function_4_577")


    #C0003
    ChrTalk(
        0x8,
        (
            "#00103F『クロスベル独立国』の無効宣言……\x01",
            "あとはハッキングのタイミングを\x01",
            "計るだけみたいね。\x02\x03",

            "#00106F……ふう、なんだか緊張してきたかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#00002Fはは……無理もないさ。\x02\x03",

            "#00003Fクロスベルという地に存在する\x01",
            "仮初の平和を、俺たちの手で\x01",
            "揺るがそうっていうんだからな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #C0005
    ChrTalk(
        0x8,
        (
            "#00108F……私たちのやろうとしていることは\x01",
            "本当に正しいのかしら。\x02\x03",

            "#00103Fクロスベルに住む多くの人は、\x01",
            "おじさまたちのおかげで\x01",
            "２大国から守られて平和に過ごせてる……\x02\x03",

            "#00108F私たちはそれを、\x01",
            "奪ってしまおうとしているのよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x101,
        (
            "#00003F……ああ。\x02\x03",

            "#00001Fだけど、今の平和はキーアが\x01",
            "ディーター大統領たちに\x01",
            "利用される形で成り立っている。\x02\x03",

            "#00003Fそんな状況、ほとんどの市民は\x01",
            "知らないだろうけど……\x01",
            "俺たちにとっては大問題だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "#00108F……うん、そうね。\x02\x03",

            "#00103Fキーアちゃんを犠牲にした上で\x01",
            "与えられた平和だなんて、\x01",
            "絶対に間違っているわよね。\x02\x03",

            "#00100F……ふふ、ありがとうロイド。\x01",
            "おかげで少しは\x01",
            "迷いが消えた気がするわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        (
            "#00009Fはは、力になれたなら良かったよ。\x02\x03",

            "#00000Fキーアを取り戻す……\x01",
            "そのためにも、この作戦は\x01",
            "絶対に成功させないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        "#00100Fええ……頑張りましょう。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D6, 0)
    Return()

    # Function_4_577 end

    def Function_5_9B5(): pass

    label("Function_5_9B5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_9C6")
    Jump("loc_D5F")

    label("loc_9C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_B9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AEF")

    #C0010
    ChrTalk(
        0x9,
        (
            "#10703F《鋼の聖女》……\x02\x03",

            "#10701Fそういえば彼女には、\x01",
            "《銀》の仮面を砕かれた借りを\x01",
            "返せていないままですね。\x02\x03",

            "#10706Fあそこまでの達人相手に\x01",
            "どこまで食い下がれるかは\x01",
            "分かりませんが……\x02\x03",

            "#10701F今の私には決して譲れない、\x01",
            "果たすべき使命があります。\x01",
            "……負けられません。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_B97")

    label("loc_AEF")


    #C0011
    ChrTalk(
        0x9,
        (
            "#10703F《鋼の聖女》ほどの達人相手に\x01",
            "どこまで食い下がれるかは\x01",
            "分かりませんが……\x02\x03",

            "#10701F今の私には決して譲れない、\x01",
            "果たすべき使命があります。\x01",
            "……負けられません。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B97")

    Jump("loc_D5F")

    label("loc_B9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_D5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BB7")
    Call(0, 6)
    Jump("loc_D5F")

    label("loc_BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDB")

    #C0012
    ChrTalk(
        0x9,
        (
            "#10703Fマインツ方面の抵抗勢力の情報は、\x01",
            "古戦場に潜伏している時に\x01",
            "国防軍から得たものです。\x02\x03",

            "#10708F……思えば《黒月》にも\x01",
            "色々とお世話になっていました。\x02\x03",

            "契約をあのような形で\x01",
            "破棄させてしまいましたし……\x02\x03",

            "#10703Fツァオさんたちには、\x01",
            "いずれ借りを返さないといけませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_D5F")

    label("loc_CDB")


    #C0013
    ChrTalk(
        0x9,
        (
            "#10708F……思えば《黒月》にも\x01",
            "色々とお世話になっていました。\x02\x03",

            "#10703Fツァオさんたちには、\x01",
            "いずれ借りを返さないといけませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D5F")

    TalkEnd(0xFE)
    Return()

    # Function_5_9B5 end

    def Function_6_D63(): pass

    label("Function_6_D63")


    #C0014
    ChrTalk(
        0x9,
        (
            "#10702Fイリアさん……\x01",
            "意識が戻って本当によかったです。\x02\x03",

            "#10703F…………………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x101,
        (
            "#00003F……リーシャ、イリアさんに\x01",
            "再会したくなったら、\x01",
            "遠慮せずいつでも言ってくれ。\x02\x03",

            "#00000F絶対に合間を見つけて、\x01",
            "ウルスラ病院に向かわせるからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "#10702Fふふ、お気遣い\x01",
            "ありがとうございます。\x02\x03",

            "#10703Fでも、今はクロスベル市と\x01",
            "アルカンシェルの解放に\x01",
            "全力を注ぐと決めましたから。\x02\x03",

            "#10701Fイリアさんの前に、\x01",
            "胸を張って立てるように\x01",
            "なるためにも……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#00000F……そっか。\x01",
            "だったら、一刻も早く\x01",
            "それを達成しないとな。\x02\x03",

            "#00004Fそれでリーシャがイリアさんに\x01",
            "会えるようになるというなら、\x01",
            "俺たちももっと頑張れると思う。\x02\x03",

            "#00000Fキーア、イリアさん、そして\x01",
            "仲間たちのためにも……\x01",
            "お互い力を尽くそう、リーシャ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x9,
        (
            "#10702Fはい……！\x01",
            "よろしくおねがいします！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 3)
    Return()

    # Function_6_D63 end

    def Function_7_105E(): pass

    label("Function_7_105E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_106F")
    Jump("loc_142E")

    label("loc_106F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_1270")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11C9")

    #C0019
    ChrTalk(
        0xA,
        (
            "#01203F#3C支援課のメンバーも\x01",
            "徐々に集まってきたようだな。\x02\x03",

            "#01200Fおぬしらに直接の助力が\x01",
            "必要なくなったら、私は再び\x01",
            "後ろに下がらせてもらうつもりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00004Fああ……分かってる。\x02\x03",

            "#00000Fでも、それまでは\x01",
            "よろしく頼むよツァイト。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xA,
        (
            "#01200F#3Cフフ、もちろんだ。\x01",
            "警察犬としての責務は\x01",
            "しかと果たさせてもらおう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_126B")

    label("loc_11C9")


    #C0022
    ChrTalk(
        0xA,
        (
            "#01200F#3Cおぬしらに直接の助力が\x01",
            "必要なくなったら、私は再び\x01",
            "後ろに下がらせてもらう。\x02\x03",

            "ただ、警察犬としての責務は\x01",
            "しかと果たさせてもらうから\x01",
            "安心するがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_126B")

    Jump("loc_142E")

    label("loc_1270")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_142E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_128B")
    Call(0, 8)
    Jump("loc_142E")

    label("loc_128B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1396")

    #C0023
    ChrTalk(
        0xA,
        (
            "#01203F#3C私は、おぬしらの持つ\x01",
            "戦術オーブメントとやらは\x01",
            "使うことはできんが……\x02\x03",

            "#01200F神狼として術の心得は多少あるし、\x01",
            "戦技もこれまで通り\x01",
            "おぬしらの力になれるだろう。\x02\x03",

            "ロイド、おぬしのほうも\x01",
            "リーダーとしての手並みを\x01",
            "改めて拝見させてもらうぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_142E")

    label("loc_1396")


    #C0024
    ChrTalk(
        0xA,
        (
            "#01200F#3Cロイド、おぬしのほうも\x01",
            "リーダーとしての手並みを\x01",
            "改めて拝見させてもらうぞ。\x02\x03",

            "#01203Fフフ、神狼である私の力を\x01",
            "存分に引き出してみるがいい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_142E")

    TalkEnd(0xFE)
    Return()

    # Function_7_105E end

    def Function_8_1432(): pass

    label("Function_8_1432")


    #C0025
    ChrTalk(
        0xA,
        (
            "#01200F#3Cウルスラ病院か…………\x02\x03",

            "#01203F……………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        "#00005Fツァイト……？\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xA,
        (
            "#01203F#3Cフフ、なんでもない。\x01",
            "少々昔を思い出していてな。\x02\x03",

            "#01200Fそれにしても、これまでも何度か\x01",
            "おぬしらを助けた事はあったが……\x02\x03",

            "共に街道を往#2Rゆ#くことになるのは\x01",
            "今回が初めてだったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#00009Fはは……確かにそうだな。\x02\x03",

            "#00000Fしばらくの間、よろしくな。\x01",
            "頼りにしてるぞツァイト。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xA,
        (
            "#01200F#3Cフフ、おぬしのほうも\x01",
            "リーダーとしての手並みを\x01",
            "改めて拝見させてもらうぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1D8, 7)
    Return()

    # Function_8_1432 end

    def Function_9_1611(): pass

    label("Function_9_1611")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_17D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_162F")
    Call(0, 10)
    Jump("loc_17D1")

    label("loc_162F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_174D")

    #C0030
    ChrTalk(
        0xB,
        (
            "#02105Fまさかロイド君たちが\x01",
            "あのアリオス・マクレインを\x01",
            "倒しちゃうなんてね。\x02\x03",

            "#02102Fふふっ、\x01",
            "大きく成長してくれて\x01",
            "お姉さんは嬉しいゾ☆\x02\x03",

            "#02104Fあなたたちなら、もうなんだって\x01",
            "乗り越えていけると思うわ。\x02\x03",

            "#02109Fこのままみんなで、\x01",
            "最高のハッピーエンドを迎えましょ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_17D1")

    label("loc_174D")


    #C0031
    ChrTalk(
        0xB,
        (
            "#02104Fあなたたちなら、もうなんだって\x01",
            "乗り越えていけると思うわ。\x02\x03",

            "#02109Fこのままみんなで、\x01",
            "最高のハッピーエンドを迎えましょ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D1")

    Jump("loc_1D3B")

    label("loc_17D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 2)), scpexpr(EXPR_END)), "loc_196D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F8")

    #C0032
    ChrTalk(
        0xB,
        (
            "#02104Fあたしは《大樹》にいる間に\x01",
            "出来るだけ写真を撮っておくわ。\x02\x03",

            "#02100Fそれに、通信社に戻ったら\x01",
            "今回の事件の真実を\x01",
            "記事になくちゃならない……\x02\x03",

            "#02102Fだからロイド君たち、\x01",
            "頑張ってこの事件を解決してね！\x02\x03",

            "#02109Fあたしに最高の三面記事を\x01",
            "書かせてちょうだい！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1968")

    label("loc_18F8")


    #C0033
    ChrTalk(
        0xB,
        (
            "#02100Fロイド君たち、\x01",
            "頑張ってこの事件を解決してね！\x02\x03",

            "#02109Fあたしに最高の三面記事を\x01",
            "書かせてちょうだい！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1968")

    Jump("loc_1D3B")

    label("loc_196D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1B2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AA3")

    #C0034
    ChrTalk(
        0xB,
        (
            "#02106Fまさか湿地帯に\x01",
            "あんな《大樹》が現れるなんてね～。\x02\x03",

            "#02100Fオルキスタワーを遥かに超える\x01",
            "大きさだし、帝国や共和国からも\x01",
            "見えてるんじゃないかしら。\x02\x03",

            "#02103F今やクロスベルの同行は\x01",
            "大陸全土が注目してるはず……\x02\x03",

            "#02102Fこうなったら、あたしも命がけで\x01",
            "あなたたちを追ってくわよ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1B25")

    label("loc_1AA3")


    #C0035
    ChrTalk(
        0xB,
        (
            "#02103F今やクロスベルの同行は\x01",
            "大陸全土が注目してるはず……\x02\x03",

            "#02102Fこうなったら、あたしも命がけで\x01",
            "あなたたちを追ってくわよ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B25")

    Jump("loc_1D3B")

    label("loc_1B2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_1D3B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C94")

    #C0036
    ChrTalk(
        0xB,
        (
            "#02103F自治州代表の１人である\x01",
            "マクダエル議長を助けだし、\x01",
            "彼の言葉を国内外に発表する……\x02\x03",

            "#02100F実現すれば、少なくとも国防軍は\x01",
            "様子見の状態にならざるを\x01",
            "得なくなるでしょうね。\x02\x03",

            "#02104F議長の言葉を発表する手段は\x01",
            "また別に用意する必要があるけど……\x01",
            "最高のスクープになりそうね！\x02\x03",

            "#02102Fふふっ、がんばって\x01",
            "議長を助け出してちょうだい！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_1D3B")

    label("loc_1C94")


    #C0037
    ChrTalk(
        0xB,
        (
            "#02104Fマクダエル議長の意見の発表……\x01",
            "独立国の正当性を揺るがせるには、\x01",
            "これ以上無い手なんじゃないかしら。\x02\x03",

            "#02102Fふふっ、がんばって\x01",
            "議長を助け出してちょうだい！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D3B")

    TalkEnd(0xFE)
    Return()

    # Function_9_1611 end

    def Function_10_1D3F(): pass

    label("Function_10_1D3F")


    #C0038
    ChrTalk(
        0xB,
        (
            "#02105Fあのアリオス・マクレインを\x01",
            "倒しちゃったみたいね？\x02\x03",

            "#02106Fはあ～……\x01",
            "まさかロイド君たちが\x01",
            "そこまでやるなんて……\x02\x03",

            "#02109F《クロスベルの英雄》も\x01",
            "代替わりの時が来たってことかしら。\x01",
            "いや～、大スクープじゃないの！\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#00004Fはは……持ち上げすぎですよ。\x02\x03",

            "#00000Fそれに、クロスベルにとって\x01",
            "アリオスさんが英雄というのは\x01",
            "依然、変わらないと思いますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xB,
        (
            "#02104Fふふっ……\x01",
            "ロイド君も成長したわね。\x02\x03",

            "#02102Fアリオスさんを超えた\x01",
            "あなたたちなら、もうなんだって\x01",
            "乗り越えていけると思うわ。\x02\x03",

            "#02109Fこのままみんなで、\x01",
            "最高のハッピーエンドを迎えましょ！\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        "#00000Fはい！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DA, 0)
    Return()

    # Function_10_1D3F end

    def Function_11_1F83(): pass

    label("Function_11_1F83")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)
    AddParty(0x5, 0xFF, 0xFF)
    OP_32(0xFF, 0xFE, 0x0)
    PartySelect(1)
    RemoveParty(0x4, 0xFF)
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x5, 0xFF)
    SetChrFlags(0xB, 0x80)
    PlayBGM("ed7534", 0)
    SetChrPos(0x101, 0, 0, -2000, 180)
    SetChrPos(0x102, 1050, 0, -2950, 270)
    SetChrPos(0x103, -950, 0, -3250, 90)
    SetChrPos(0x104, 0, 0, -4250, 0)
    OP_68(1840, 1100, 14830, 0)
    MoveCamera(51, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(27300, 0)
    OP_68(0, 1100, -3000, 7000)
    MoveCamera(51, 25, 0, 7000)
    OP_6E(800, 7000)
    SetCameraDistance(18480, 7000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(0, 1100, -3000, 0)
    MoveCamera(51, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10200, 0)
    OP_0D()
    Sleep(300)

    #C0042
    ChrTalk(
        0x104,
        (
            "#00306F#12Pしっかし、思えば遠くに\x01",
            "来ちまったって感じがするな。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        (
            "#00208F#6Pそうですね……\x01",
            "狭いクロスベルの中にいるのは\x01",
            "変わらないのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#00103F#11P……多分、私たちだけじゃなくて、\x01",
            "クロスベル、ううん大陸全土が\x01",
            "動き始めてるからだと思う。\x02\x03",

            "#00108Fひょっとしたら歴史の転換点に\x01",
            "立ち会っているのかもしれない……\x02\x03",

            "…………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#00003F#5P……エリィ。\x02\x03",

            "#00008Fやっぱりマリアベルさんたちと\x01",
            "事を構えるのは抵抗があるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        (
            "#00106F#11Pそうね……私にとっては\x01",
            "馴染み深い人たちだったから。\x02\x03",

            "#00108Fそれに、政治の観点から言えば\x01",
            "彼らのやろうとしていることを\x01",
            "否定しきれない自分もいる……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x103,
        "#00208F#6P………………………………\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        "#00006F#5P……そうか……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x104,
        (
            "#00306F#12Pま、鉄血宰相じゃねえが、\x01",
            "もっとエゲつない事をしてる連中は\x01",
            "山ほどいるだろうしな……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x102,
        (
            "#00103F#11P──でも、これだけは言える。\x02\x03",

            "#00101Fどれだけ状況が変わろうと\x01",
            "私たちは『特務支援課』だわ。\x02\x03",

            "その部分だけは\x01",
            "何があっても揺るがないと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        "#00005F#5Pエリィ……\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        "#00202F#6P……エリィさん……\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x104,
        (
            "#00309F#12Pはは、何だよお嬢。\x02\x03",

            "#00302F警察なんて所詮、\x01",
            "腰掛け程度じゃなかったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x102,
        (
            "#00109F#11Pふふ、最初の頃はね。\x02\x03",

            "#00104F……でも駄目ね。\x01",
            "もう私は染まってしまった。\x02\x03",

            "多分、将来どんな道を\x01",
            "選ぶことになったとしても……\x02\x03",

            "#00102F貴方たちと過ごした日々は\x01",
            "今後も私にとっての根っこで\x01",
            "あり続けるような気がするわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#00000F#5P……そっか。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x103,
        "#00204F#6Pわたしも……同じ気持ちです。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        (
            "#00304F#12Pハハ、そういう意味じゃ\x01",
            "課長も因果な部署を\x01",
            "立ち上げたもんだよな。\x02\x03",

            "#00305Fいや、元はといえば\x01",
            "ロイドの兄貴のアイデアか。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x101,
        (
            "#00012F#5Pはは、兄貴もさすがに\x01",
            "こんな状況になるなんて\x01",
            "想像もしてなかったと思うけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0059
    ChrTalk(
        0x101,
        (
            "#00001F#5P……キーアを取り戻し、\x01",
            "今回の事件を解決すること。\x02\x03",

            "多分それは、特務支援課として\x01",
            "果たすべき使命の象徴かもしれない。\x02\x03",

            "#00004Fただ、そんな理屈を\x01",
            "無理に考えなくてもいいと思う。\x02\x03",

            "俺たちにとって\x01",
            "大切と思えるもののために……\x02\x03",

            "#00000F今はただ、前を向いて進もう。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        "#00102F#11Pええ……！\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x103,
        (
            "#00204F#6P音信不通の課長も\x01",
            "探さないといけませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x104,
        "#00309F#12Pハハ……だな。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(9200, 3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(132, 1000, 70)
    StopSound(497, 1000, 30)
    StopBGM(0xFA0)
    WaitBGM()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0063
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エリィがパーティに加入しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x1, 0x11F)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0064
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エリィがＳクラフト\x01\x07\x02",

            "『デバインクルセイド』\x07\x05",
            "を修得しました。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 52, -1, -1)

    #A0065
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "『デバインクルセイド』\x07\x05",
            "をＳブレイクに登録しますか？",
            scpstr(0x6),
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        208,
        0,
        (
            "【は  い】\x01",      # 0
            "【いいえ】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_57(0x0)
    OP_60(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29CF")
    SetChrChipPat(0x1, 0x6, 0x11F)

    label("loc_29CF")

    OP_5A()
    SetChrName("")

    #A0066
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エリィが加入したことにより、\x01",
            "パーティの定員６名がオーバーしました。\x02\x03",

            "以下のメンバーから\x01",
            "パーティに参加するメンバーを\x01",
            "改めて選択してください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PartySelect(0)
    PartySelect(2)
    Sleep(500)
    SetChrName("")

    #A0067
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "以降は、ブリッジにいる\x01",
            "アッバスに話しかけることで\x01",
            "パーティ編成を行うことができます。\x02\x03",

            "なお、ストーリーを進める場合、\x01",
            "メルカバの移動マップの東端にある\x01",
            "『ブースター地点』を選んで下さい。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    SetScenarioFlags(0x1A4, 1)
    OP_29(0xAF, 0x1, 0x14)
    SetScenarioFlags(0x31, 6)
    SetScenarioFlags(0x31, 7)
    EventEnd(0x5)
    NewScene("e3020", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_1F83 end

    SaveToFile()

Try(main)
