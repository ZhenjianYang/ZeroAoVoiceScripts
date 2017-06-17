from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t116b.bin",                # FileName
        "t116b",                    # MapName
        "t116b",                    # Location
        0x004A,                     # MapIndex
        "ed7125",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 74, 0, 1, 0, 2],
    )

    BuildStringList((
        "t116b",                  # 0
        "エリィ",                 # 1
        "ティオ",                 # 2
        "ランディ",               # 3
        "ワジ",                   # 4
        "マフィア",               # 5
        "マフィア",               # 6
        "キーア",                 # 7
        "キーア",                 # 8
        "SE制御",                 # 9
    ))

    AddCharChip((
        "chr/ch07700.itc",                   # 00
        "chr/ch07800.itc",                   # 01
        "chr/ch07900.itc",                   # 02
        "chr/ch08000.itc",                   # 03
        "apl/ch50363.itc",                   # 04
        "chr/ch00000.itc",                   # 05
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

    DeclNpc(699,     0,       2500,    0,    389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(699,     0,       2500,    0,    389,  0x0, 0,   1,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(699,     0,       2500,    0,    389,  0x0, 0,   2,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(1600,    0,       -4699,   180,  389,  0x0, 0,   3,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(4000,    0,       1000,    270,  453,  0x0, 0,   4,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(4000,    0,       -1000,   270,  453,  0x0, 0,   4,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-5120,   0,       -230,    1500,    -5120,   800,     -230,    0x007C, 0,  13, 0x0000)
    DeclActor(3780,    0,       3250,    1500,    4710,    2000,    3850,    0x007C, 0,  7,  0x0000)
    DeclActor(-1380,   0,       4940,    1500,    -1380,   1800,    4940,    0x007C, 0,  8,  0x0000)
    DeclActor(-4710,   0,       3940,    1500,    -4710,   1000,    3940,    0x007C, 0,  9,  0x0000)
    DeclActor(-4030,   0,       -3730,   1500,    -4030,   1200,    -3730,   0x007C, 0,  10, 0x0000)

    ScpFunction((
        "Function_0_32C",          # 00, 0
        "Function_1_3E4",          # 01, 1
        "Function_2_3F6",          # 02, 2
        "Function_3_49B",          # 03, 3
        "Function_4_6C7",          # 04, 4
        "Function_5_8FF",          # 05, 5
        "Function_6_B31",          # 06, 6
        "Function_7_D11",          # 07, 7
        "Function_8_D72",          # 08, 8
        "Function_9_DAE",          # 09, 9
        "Function_10_DE4",         # 0A, 10
        "Function_11_E1E",         # 0B, 11
        "Function_12_E6E",         # 0C, 12
        "Function_13_12C5",        # 0D, 13
        "Function_14_3172",        # 0E, 14
        "Function_15_318F",        # 0F, 15
        "Function_16_31AE",        # 10, 16
        "Function_17_31CD",        # 11, 17
        "Function_18_3221",        # 12, 18
        "Function_19_3275",        # 13, 19
        "Function_20_333F",        # 14, 20
        "Function_21_33E9",        # 15, 21
        "Function_22_358A",        # 16, 22
        "Function_23_35C5",        # 17, 23
        "Function_24_3693",        # 18, 24
        "Function_25_3761",        # 19, 25
        "Function_26_3836",        # 1A, 26
        "Function_27_38B1",        # 1B, 27
    ))


    def Function_0_32C(): pass

    label("Function_0_32C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_36C"),
        (1, "loc_378"),
        (2, "loc_384"),
        (3, "loc_390"),
        (4, "loc_39C"),
        (5, "loc_3A8"),
        (6, "loc_3B4"),
        (SWITCH_DEFAULT, "loc_3C0"),
    )


    label("loc_36C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_378")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_384")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_390")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_39C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_3A8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_3B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_3C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_3CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3E3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3CC")

    label("loc_3E3")

    Return()

    # Function_0_32C end

    def Function_1_3E4(): pass

    label("Function_1_3E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F5")
    Event(0, 12)

    label("loc_3F5")

    Return()

    # Function_1_3E4 end

    def Function_2_3F6(): pass

    label("Function_2_3F6")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40C")
    OP_66(0x0, 0x1)

    label("loc_40C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_41E")
    OP_70(0x4, 0x78)
    Jump("loc_42A")

    label("loc_41E")

    SetMapObjFrame(0x4, "CA01", 0x1, 0x2)

    label("loc_42A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_436")
    Call(0, 26)

    label("loc_436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_END)), "loc_43F")

    label("loc_43F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA6, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_465")
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    Jump("loc_490")

    label("loc_465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_47D")
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    Jump("loc_490")

    label("loc_47D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_490")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)

    label("loc_490")

    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)

    label("loc_49A")

    Return()

    # Function_2_3F6 end

    def Function_3_49B(): pass

    label("Function_3_49B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63B")

    #C0001
    ChrTalk(
        0xFE,
        (
            "#5308Fそれにしても……\x01",
            "どこかで見た美術品や名画ばかり。\x02\x03",

            "一体どんなルートを使えば\x01",
            "こんな商品を集めてこれるのかしら。\x02\x03",

            "#5303Fさっき《銀》が言っていた\x01",
            "“爆弾”というのも気になるし……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0002
    ChrTalk(
        0xFE,
        (
            "#5305F……ロイド、どうしたの？\x02\x03",

            "なんだか顔色が悪いみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#5112F……いや、なんでもないんだ。\x02\x03",

            "#5108F（やっぱりさっきの声、\x01",
            "  エリィたちには\x01",
            "  聞こえてないのか……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_6C3")

    label("loc_63B")


    #C0004
    ChrTalk(
        0xFE,
        (
            "#5308F一体どんなルートを使えば\x01",
            "こんな商品を集めて来れるのかしら。\x02\x03",

            "#5306Fルバーチェのコネクション……\x01",
            "思った以上に手広いみたいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6C3")

    TalkEnd(0xFE)
    Return()

    # Function_3_49B end

    def Function_4_6C7(): pass

    label("Function_4_6C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_889")

    #C0005
    ChrTalk(
        0xFE,
        (
            "#5400Fどれも高価なものみたいですけど\x01",
            "悪趣味な出品物も多そうですね。\x02\x03",

            "#5403Fやっぱり、主催者の品性が\x01",
            "にじみ出てしまうのでしょうか……\x02\x03",

            "#5408F……そういえば、《銀》さんの言った\x01",
            "“爆弾”とやらは何を指すのでしょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0006
    ChrTalk(
        0xFE,
        (
            "#5400F……ロイドさん、どうかしました？\x02\x03",

            "さっきから様子が変ですよ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#5112F……いや、なんでもないんだ。\x02\x03",

            "#5108F（やっぱりさっきの声、\x01",
            "  ティオたちには\x01",
            "  聞こえてないのか……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_8FB")

    label("loc_889")


    #C0008
    ChrTalk(
        0xFE,
        (
            "#5403F……個人的に\x01",
            "目を引く出品物はありませんね。\x02\x03",

            "#5408F純金のみっしぃとか出てないかと\x01",
            "期待したんですが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8FB")

    TalkEnd(0xFE)
    Return()

    # Function_4_6C7 end

    def Function_5_8FF(): pass

    label("Function_5_8FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD2")

    #C0009
    ChrTalk(
        0xFE,
        (
            "#5602Fありゃ、戦乙女を模した石膏像か？\x01",
            "なかなかのナイスバディじゃねぇか。\x02\x03",

            "#5606F……ってか、それ以外の絵とかは\x01",
            "いまいち楽しみ方がわかんねぇなぁ。\x02\x03",

            "#5601Fそういや、《銀》の野郎が言ってた\x01",
            "“爆弾”ってのも何のことやら……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0010
    ChrTalk(
        0xFE,
        (
            "#5605F……おい、どうした？\x02\x03",

            "#5609F腹でも痛いなら\x01",
            "お兄さんがさすってやろうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        (
            "#5112F……いや、なんでもないんだ。\x02\x03",

            "#5108F（やっぱりさっきの声、\x01",
            "  ランディたちには\x01",
            "  聞こえてないのか……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_B2D")

    label("loc_AD2")


    #C0012
    ChrTalk(
        0xFE,
        (
            "#5601F……爆弾ねぇ……\x02\x03",

            "#5603Fヤツの話し振りからするに\x01",
            "本物ってわけじゃなさそうだが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2D")

    TalkEnd(0xFE)
    Return()

    # Function_5_8FF end

    def Function_6_B31(): pass

    label("Function_6_B31")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C7D")

    #C0013
    ChrTalk(
        0xFE,
        (
            "#5705Fふうん……\x01",
            "なかなか高価そうなものが揃ってるね。\x02\x03",

            "#5704F面倒に巻き込まれたついでに、\x01",
            "何かひとつ、いただいちゃおうかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#5113Fあのな……\x01",
            "流石に見過ごすわけないだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "#5702Fふふ……冗談さ。\x01",
            "物盗りをするほど腐っちゃいない。\x02\x03",

            "#5704F……ま、ここにある商品が\x01",
            "まっとうなものだとも思えないけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_D0D")

    label("loc_C7D")


    #C0016
    ChrTalk(
        0xFE,
        (
            "#5702Fふふ……不良グループの頭だからって、\x01",
            "物盗りをするほど腐っちゃいないさ。\x02\x03",

            "#5704Fここにある商品が\x01",
            "まっとうなものだとも思えないけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D0D")

    TalkEnd(0xFE)
    Return()

    # Function_6_B31 end

    def Function_7_D11(): pass

    label("Function_7_D11")

    TalkBegin(0xFF)
    SetChrName("")

    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "戦乙女を象った石膏像や古い陶磁器、\x01",
            "不気味な仮面のようなものが置かれている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_7_D11 end

    def Function_8_D72(): pass

    label("Function_8_D72")

    TalkBegin(0xFF)
    SetChrName("")

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "禁猟指定された動物の剥製が置いてある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_8_D72 end

    def Function_9_DAE(): pass

    label("Function_9_DAE")

    TalkBegin(0xFF)
    SetChrName("")

    #A0019
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "美しい絵画が立てかけられている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_9_DAE end

    def Function_10_DE4(): pass

    label("Function_10_DE4")

    TalkBegin(0xFF)
    SetChrName("")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "古びた書物などが乱雑に置かれている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_10_DE4 end

    def Function_11_E1E(): pass

    label("Function_11_E1E")

    TalkBegin(0xFE)

    #C0021
    ChrTalk(
        0xFE,
        "………………………………\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "完全に気を失っているようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_11_E1E end

    def Function_12_E6E(): pass

    label("Function_12_E6E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-3350, 1200, 0, 0)
    MoveCamera(43, 12, 0, 0)
    MoveCamera(46, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18330, 0)
    SetChrPos(0x101, 6000, 0, 0, 270)
    SetChrPos(0xEF, 7350, 0, 600, 270)
    SetChrPos(0x151, 7000, 0, -600, 270)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis064.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis065.itp")
    FadeToBright(1000, 0)
    OP_68(5940, 1200, 0, 6000)
    OP_6F(0x1)
    Sleep(300)

    #C0023
    ChrTalk(
        0x101,
        "#5105F#11Pここは……\x02",
    )

    CloseMessageWindow()
    OP_C7(0x0, 0x800)
    VolumeBGM(0x28, 0x1F4)
    FadeToDark(500, 0, -1)
    Sound(915, 0, 100, 0)
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    Sleep(200)
    Sound(2179, 255, 75, 0)    #voice#KeA
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    Sleep(200)
    Sound(2044, 255, 75, 0)    #voice#KeA
    OP_CA(0x0, 0x1, 0x3)
    Sleep(1000)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    FadeToBright(500, 0)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    OP_C7(0x1, 0x800)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_109B")

    #C0024
    ChrTalk(
        0x102,
        (
            "#5301F#11P……どうやら競売会の\x01",
            "後半に出品される物みたいね。\x02\x03",

            "まだ結構あるみたいだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1174")

    label("loc_109B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_110C")

    #C0025
    ChrTalk(
        0x103,
        (
            "#5401F#11P……どうやら競売会の\x01",
            "後半に出品される物みたいですね。\x02\x03",

            "まだ結構あるみたいですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1174")

    label("loc_110C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1174")

    #C0026
    ChrTalk(
        0x104,
        (
            "#5601F#11P……どうやら競売会の\x01",
            "後半に出品される物みたいだな。\x02\x03",

            "まだ結構あるみたいだが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1174")


    #C0027
    ChrTalk(
        0x151,
        (
            "#5704F#11Pふふ、後半に出るってことは\x01",
            "取っておきの品ばかりだろうね。\x02\x03",

            "#5702F時間もないことだし、\x01",
            "手分けして調べてみようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#5103F#11P……ああ。\x02\x03",

            "#5108Fどうやら……\x01",
            "本当に何かありそうだ。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 5130, 0, -200, 270)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    RemoveParty(0x50, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1281")
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    RemoveParty(0x1, 0x0)
    Jump("loc_12B2")

    label("loc_1281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_129C")
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    RemoveParty(0x2, 0x0)
    Jump("loc_12B2")

    label("loc_129C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_12B2")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    RemoveParty(0x3, 0x0)

    label("loc_12B2")

    OP_66(0x0, 0x1)
    SetScenarioFlags(0xA6, 4)
    OP_29(0x47, 0x1, 0xE)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_12_E6E end

    def Function_13_12C5(): pass

    label("Function_13_12C5")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    SetChrChipPat(0x0, 0x1, 0x4C)
    LoadChrChipPat()
    OP_49()
    LoadChrToIndex("chr/ch31050.itc", 0x1E)
    LoadChrToIndex("chr/ch31051.itc", 0x1F)
    LoadChrToIndex("chr/ch31150.itc", 0x20)
    LoadChrToIndex("chr/ch31151.itc", 0x21)
    LoadChrToIndex("chr/ch08100.itc", 0x23)
    LoadChrToIndex("apl/ch50364.itc", 0x24)
    LoadChrToIndex("apl/ch50365.itc", 0x25)
    LoadChrToIndex("apl/ch50368.itc", 0x26)
    LoadChrToIndex("apl/ch50369.itc", 0x27)
    LoadChrToIndex("chr/ch10800.itc", 0x29)
    LoadChrToIndex("chr/ch31053.itc", 0x2A)
    LoadChrToIndex("chr/ch31153.itc", 0x2B)
    LoadChrToIndex("chr/ch31052.itc", 0x2C)
    LoadChrToIndex("chr/ch31152.itc", 0x2D)
    LoadChrToIndex("chr/ch00000.itc", 0x2E)
    SoundLoad(924)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x25)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x2)
    SetChrFlags(0xE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1382")
    AddParty(0x1, 0xEF, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    Jump("loc_13B5")

    label("loc_1382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_139E")
    AddParty(0x2, 0xEF, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    Jump("loc_13B5")

    label("loc_139E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_13B5")
    AddParty(0x3, 0xEF, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)

    label("loc_13B5")

    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x0)
    OP_4B(0xB, 0xFF)
    FadeToBright(1000, 0)
    OP_68(-3840, 1000, -210, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19330, 0)
    SetCameraDistance(18330, 2000)
    SetChrPos(0x101, -3600, 0, 0, 270)
    SetChrPos(0xEF, 700, 0, 2500, 0)
    SetChrPos(0xB, 1600, 0, -4700, 180)
    SetChrFlags(0x101, 0x8000)
    SetChrFlags(0xEF, 0x8000)
    SetChrFlags(0xB, 0x8000)
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu05800.itp")
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_263C")
    OP_6F(0x10)

    #C0029
    ChrTalk(
        0x101,
        (
            "#5105F#11P（このトランクは……）\x02\x03",

            "#5101F（ずいぶん大きいけど\x01",
            "  何が入っているんだ……？）\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(882, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0030
    ChrTalk(
        0x101,
        (
            "#5000F#11P（……鍵がかかっているけど\x01",
            "  このくらいだったら何とか……）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0031
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは捜査官用のツールボックスから\x01",
            "ピッキング用のツールを取り出した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    SetCameraDistance(18030, 1500)
    Fade(250)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x2)
    Sound(804, 0, 100, 0)
    OP_6F(0x10)

    #C0032
    ChrTalk(
        0x101,
        (
            "#5003F#11P（捜査官研修で習った\x01",
            "  ピッキング対策用の技術……）\x02\x03",

            "#5001F（まさかこんな所で使うなんてな……）\x02",
        )
    )

    CloseMessageWindow()
    Sound(833, 0, 100, 0)
    SetCameraDistance(17000, 3000)
    OP_A1(0x101, 0x3E8, 0x4, 0x3, 0x4, 0x3, 0x4)
    Sleep(100)
    OP_A1(0x101, 0x3E8, 0x6, 0x3, 0x4, 0x3, 0x4, 0x3, 0x4)
    Sleep(50)
    Sound(833, 0, 100, 0)
    OP_A1(0x101, 0x3E8, 0x4, 0x3, 0x4, 0x3, 0x4)
    OP_6F(0x10)
    Sound(809, 0, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0033
    ChrTalk(
        0x101,
        "#5002F#11P（──やった。）\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    OP_71(0x4, 0x0, 0x28, 0x0, 0x0)
    Sound(922, 0, 100, 0)
    OP_79(0x4)
    Sleep(300)
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    StopBGM(0x1770)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(2000)
    OP_64(0x101)

    #C0034
    ChrTalk(
        0x101,
        "#5005F#11P……………………え。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-4500, 1000, 79640, 0)
    MoveCamera(315, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(14860, 2500)
    SetChrPos(0x101, -3600, 0, 80000, 270)
    SetChrPos(0xEF, 700, 0, 82500, 0)
    SetChrPos(0xB, 1600, 0, 76700, 180)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x190), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x101, 0x8)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrPos(0xE, -5000, -200, 79750, 90)
    SetChrPos(0xF, -5000, -800, 79750, 90)
    OP_A7(0xE, 0x40, 0x40, 0x40, 0xFF, 0x0)
    SetChrFlags(0xF, 0x8)
    BeginChrThread(0xE, 0, 0, 14)
    OP_70(0x5, 0x28)
    OP_71(0x5, 0x28, 0x78, 0x0, 0x0)
    Sound(923, 0, 100, 0)

    def lambda_1843():
        OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1843)
    WaitChrThread(0xE, 1)
    OP_79(0x5)
    OP_6F(0x10)
    OP_0D()
    SetChrSubChip(0x101, 0x9)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0035
    ChrTalk(
        0x101,
        "#5011F#11P…………ぁ………………\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrPos(0xE, -5000, 50, 79750, 90)
    ClearChrFlags(0xE, 0x1)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x230), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x230), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x230), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 0x25)
    SetChrSubChip(0x101, 0x16)
    OP_68(-4260, 1000, 79730, 0)
    MoveCamera(311, 34, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(9670, 0)
    SetCameraDistance(8670, 10000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7304", 0)
    Sleep(2000)

    #C0036
    ChrTalk(
        0x101,
        (
            "#5005F#30W#11P（もしかして……\x01",
            "  これがローゼンベルク工房の？）\x02\x03",

            "#5008F（ま、まるで本当に\x01",
            "  生きているみたいだけど……）\x02\x03",

            "（で、でもこれは……）\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 50, -1, -1)
    #Sound(2026, 255, 70, 0)    #voice#KeA
    Sleep(300)
    SetChrName("声")

    #A0037
    AnonymousTalk(
        0xFF,
        "#2S#80W………ん…………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sleep(150)
    EndChrThread(0xE, 0x0)
    OP_A1(0xE, 0x3E8, 0x4, 0x0, 0x5, 0x6, 0x7)
    Sound(820, 0, 100, 0)
    OP_A1(0xE, 0x3E8, 0x2, 0x9, 0xA)
    OP_A1(0xE, 0x3E8, 0x4, 0xB, 0xC, 0xD, 0xC)
    OP_A1(0xE, 0x3E8, 0x4, 0xB, 0xC, 0xD, 0xC)
    OP_A1(0xE, 0x3E8, 0x3, 0xD, 0xE, 0xF)
    BeginChrThread(0xE, 0, 0, 15)
    Sleep(1000)

    #N0038
    NpcTalk(
        0xF,
        "人形？",
        "#80W#5P………………………………\x02",
    )

    CloseMessageWindow()
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    #Sound(2027, 255, 80, 0)    #voice#KeA
    Sleep(500)
    SetChrName("人形？")

    #A0039
    AnonymousTalk(
        0xFF,
        "#50W……おにいちゃん、だれ？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Sleep(150)
    Fade(500)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x1)
    BeginChrThread(0xE, 0, 0, 16)
    SetChrPos(0xE, -5000, -200, 79750, 90)
    SetChrFlags(0xE, 0x1)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(2000)
    SetCameraDistance(14000, 0)
    SetCameraDistance(19000, 800)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0040
    ChrTalk(
        0x101,
        "#5007F#4S#11P#16Aなあああっ！？\x02",
    )
    #Auto

    OP_6F(0x10)
    Sleep(500)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1C36():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1C36)

    def lambda_1C43():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1C43)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0xB, 1)
    OP_68(-4260, 1000, 79730, 2000)
    MoveCamera(311, 22, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(14360, 2000)

    def lambda_1C86():
        OP_95(0xFE, -3250, 0, 81490, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1C86)

    def lambda_1CA0():
        OP_95(0xFE, -2080, 0, 79080, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1CA0)
    WaitChrThread(0xEF, 1)

    def lambda_1CBE():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1CBE)
    WaitChrThread(0xEF, 1)

    def lambda_1CCF():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1CCF)
    WaitChrThread(0xB, 1)
    OP_6F(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_1D1C")

    #C0041
    ChrTalk(
        0x102,
        (
            "#5301F#2Pど、どうしたの……？\x02\x03",

            "#5305F！！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D99")

    label("loc_1D1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_1D5D")

    #C0042
    ChrTalk(
        0x103,
        (
            "#5401F#2P……どうしたんですか？\x02\x03",

            "#5405F！！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D99")

    label("loc_1D5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_1D99")

    #C0043
    ChrTalk(
        0x104,
        (
            "#5605F#2Pなんだ、どうした……？\x02\x03",

            "#5601F！！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D99")


    #C0044
    ChrTalk(
        0xB,
        "#5705F#12P……その子は………\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#5011F#11P#30Wき、君は……\x02\x03",

            "どうしてこんな所に……\x02",
        )
    )

    CloseMessageWindow()

    #N0046
    NpcTalk(
        0xF,
        "女の子",
        (
            "#5805F#5P#30Wどーしたの？\x01",
            "目をまんまるにして。\x02\x03",

            "#5809Fあはは！\x01",
            "おにいちゃん、面白い～！\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#5006F#11Pい、いや、面白いって……\x02\x03",

            "#5008Fもしかして偶然、\x01",
            "中に紛れ込んだのか……\x02\x03",

            "#5013Fお父さんとお母さんは\x01",
            "どこにいるか分かるかい！？\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xF, -4850, -400, 79950, 135)
    OP_63(0xF, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #N0048
    NpcTalk(
        0xE,
        "女の子",
        (
            "#5805F#5P#30W？？？\x02\x03",

            "おとうさん？　おかあさん？\x02\x03",

            "キーア、そんなの知らないよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#5003F#11Pキーア……\x01",
            "君の名前はキーアっていうのか。\x02\x03",

            "#5008Fでも、いったい誰の……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2038")

    #C0050
    ChrTalk(
        0x102,
        (
            "#5306F#2Pね、ねえ、ロイド……\x02\x03",

            "#5308Fその子の格好、どう考えても\x01",
            "招待客の子には見えないんだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2111")

    label("loc_2038")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_20A6")

    #C0051
    ChrTalk(
        0x103,
        (
            "#5406F#2P……ロイドさん。\x02\x03",

            "#5411Fその子の格好、どう考えても\x01",
            "招待客の子には見えませんが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2111")

    label("loc_20A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2111")

    #C0052
    ChrTalk(
        0x104,
        (
            "#5606F#2Pおい、ロイド……\x02\x03",

            "#5601Fその子の格好、どう考えても\x01",
            "招待客の子じゃねえんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2111")

    OP_63(0x101, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0053
    ChrTalk(
        0x101,
        (
            "#5006F#11Pああもう……\x01",
            "もちろん分かってるけどさ！\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xB,
        (
            "#5704F#12Pフフ……なるほどね。\x02\x03",

            "どうやらその子が……\x01",
            "“爆弾”だったわけだ。\x02\x03",

            "#5702Fローゼンベルク工房の人形が\x01",
            "仕舞われているトランク……\x02\x03",

            "もしこのまま会場に運ばれて\x01",
            "その蓋が開かれていたら……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0055
    ChrTalk(
        0x101,
        "#5013F#11Pあ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_22A3")

    #C0056
    ChrTalk(
        0x102,
        "#5301F#2Pな、なるほど……\x02",
    )

    CloseMessageWindow()
    Jump("loc_22FC")

    label("loc_22A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_22D0")

    #C0057
    ChrTalk(
        0x103,
        "#5401F#2P……なるほど……\x02",
    )

    CloseMessageWindow()
    Jump("loc_22FC")

    label("loc_22D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_22FC")

    #C0058
    ChrTalk(
        0x104,
        "#5603F#2P……そういう事か……\x02",
    )

    CloseMessageWindow()

    label("loc_22FC")


    #N0059
    NpcTalk(
        0xF,
        "キーア",
        (
            "#5800F#5P#30Wへー、おにいちゃん、\x01",
            "ロイドっていうんだ。\x02\x03",

            "#5803F……ロイド、ロイド……\x02\x03",

            "#5809Fえへへっ……いい名前だね！\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#5012F#11Pど、どうも……\x02\x03",

            "#5011F──って、そうじゃなくて！\x02\x03",

            "#5013Fキーア！\x01",
            "他に覚えてることはないか！？\x02\x03",

            "知ってる人とか\x01",
            "住んでいた場所とか！？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    #Sound(2028, 255, 85, 0)    #voice#KeA
    Sleep(300)

    #N0061
    NpcTalk(
        0xF,
        "キーア",
        "#5811F#5P……えーと。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xF, -4850, -400, 79950, 135)
    OP_63(0xF, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xF)

    #N0062
    NpcTalk(
        0xF,
        "キーア",
        (
            "#5809F#5Pえへへ……\x01",
            "なんにも思い出せないや。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#5006F#11Pガクッ……\x02\x03",

            "#5013F──と、とにかく君を\x01",
            "このままにはしておけない。\x02\x03",

            "いったんここを出て──\x02",
        )
    )

    CloseMessageWindow()
    Sound(924, 2, 100, 0)
    Sleep(500)
    StopBGM(0xFA0)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0064
    ChrTalk(
        0x101,
        "#5010F#11Pくっ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_25AE")

    #C0065
    ChrTalk(
        0x102,
        "#5307F#2Pいけない……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2605")

    label("loc_25AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_25DF")

    #C0066
    ChrTalk(
        0x103,
        "#5407F#2P……マズイです……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2605")

    label("loc_25DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2605")

    #C0067
    ChrTalk(
        0x104,
        "#5607F#2Pやべえぞ……！\x02",
    )

    CloseMessageWindow()

    label("loc_2605")


    #C0068
    ChrTalk(
        0xB,
        (
            "#5703F#12Pやれやれ……\x01",
            "タイムオーバーみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_263C")

    Sound(103, 0, 70, 0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xC, 10000, 0, 80000, 270)
    SetChrPos(0xD, 10000, 0, 80000, 270)

    #N0069
    NpcTalk(
        0xC,
        "男の声",
        "#2Sなっ……！\x02",
    )

    CloseMessageWindow()

    #N0070
    NpcTalk(
        0xC,
        "男の声",
        "#2S馬鹿な、侵入者だと！？\x02",
    )

    CloseMessageWindow()

    #N0071
    NpcTalk(
        0xD,
        "男の声",
        "#2Sしゅ、出品物を確かめろ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(103, 0, 100, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7509", 0)
    ReplaceBGM("ed7000", "ed7000")
    ReplaceBGM("ed7513", "ed7509")
    ReplaceBGM("ed7125", "ed7509")
    OP_68(-2500, 1100, 0, 0)
    MoveCamera(40, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18330, 0)
    OP_68(0, 1100, 0, 2000)
    SetChrPos(0x101, -3600, 0, 0, 270)
    SetChrPos(0xEF, -3250, 0, 1490, 0)
    SetChrPos(0xB, -2080, 0, -1080, 180)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0xC, 10000, 0, 0, 270)
    SetChrPos(0xD, 10000, 0, 0, 270)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    EndChrThread(0xE, 0x0)
    SetChrPos(0xE, -4850, -200, -250, 90)
    SetChrSubChip(0xE, 0x1C)
    SetChrPos(0xF, -4850, -800, -250, 90)
    OP_70(0x4, 0x78)
    SetMapObjFrame(0x4, "CA01", 0x0, 0x2)
    ClearMapObjFlags(0x1, 0x10)
    OP_70(0x1, 0x5)

    def lambda_280A():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_280A)

    def lambda_2817():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2817)

    def lambda_2824():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2824)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0xB, 1)
    BeginChrThread(0xC, 3, 0, 17)
    Sleep(500)
    BeginChrThread(0xD, 3, 0, 18)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    OP_6F(0x1)
    OP_0D()
    BeginChrThread(0x10, 1, 0, 27)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_29A7")

    #C0072
    ChrTalk(
        0x104,
        "#5611F#5P……ハッ……！\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xB,
        "#5707F#6Pひゅっ……！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xB, 3, 0, 19)
    BeginChrThread(0x104, 3, 0, 20)
    WaitChrThread(0xB, 3)
    WaitChrThread(0x104, 3)
    Sleep(850)
    OP_68(-1350, 1400, 0, 2000)
    MoveCamera(45, 16, 0, 2000)
    SetCameraDistance(17350, 2000)
    OP_93(0xB, 0x10E, 0x12C)
    OP_93(0x104, 0x10E, 0x1F4)
    OP_6F(0x79)

    #N0074
    NpcTalk(
        0xF,
        "キーア",
        "#5805F#5Pほえ～っ……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        "#5001F#5Pランディ、ワジ……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xB,
        (
            "#5702F#11P──どうやら覚悟を\x01",
            "決めた方がいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x104,
        (
            "#5601F#11Pああ、このままだと\x01",
            "確実に捕まることになるぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AFF")

    label("loc_29A7")


    #C0078
    ChrTalk(
        0xB,
        "#5707F#5Pひゅっ……！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0xB, 3, 0, 21)
    WaitChrThread(0xB, 3)
    Sleep(500)
    OP_68(-1350, 1400, 0, 2000)
    MoveCamera(45, 16, 0, 2000)
    SetCameraDistance(17350, 2000)
    OP_93(0xB, 0x10E, 0x12C)
    OP_6F(0x79)

    #N0079
    NpcTalk(
        0xF,
        "キーア",
        "#5805F#5Pほえ～っ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2A4E")

    #C0080
    ChrTalk(
        0x102,
        "#5305F#5Pで、電光石火ね……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A76")

    label("loc_2A4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2A76")

    #C0081
    ChrTalk(
        0x103,
        "#5405F#5P電光石火です……\x02",
    )

    CloseMessageWindow()

    label("loc_2A76")


    #C0082
    ChrTalk(
        0x101,
        "#5013F#5Pワジ……\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xB,
        (
            "#5706F#11P──どうやら覚悟を\x01",
            "決めた方がいいんじゃない？\x02\x03",

            "#5702Fこのままだと確実に\x01",
            "連中に捕まることになるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AFF")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0084
    ChrTalk(
        0x101,
        "#5003F#5P……分かった。\x02",
    )

    CloseMessageWindow()

    def lambda_2B39():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B39)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B5B")
    Sleep(100)

    def lambda_2B53():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_2B53)

    label("loc_2B5B")

    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    Sleep(300)
    OP_68(-3650, 1400, 0, 1500)
    SetCameraDistance(15060, 1500)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x7)
    Sleep(500)
    Sound(534, 0, 90, 0)
    Sound(804, 0, 100, 0)
    Fade(500)
    OP_A1(0x101, 0x7D0, 0x4, 0x7, 0x0, 0x1, 0x2)
    SetChrChipByIndex(0x101, 0x2E)
    SetChrSubChip(0x101, 0x0)
    OP_A1(0x101, 0x7D0, 0x5, 0x3, 0x4, 0x5, 0x6, 0x7)
    OP_6F(0x79)
    Sleep(500)
    OP_68(-4100, 1200, 0, 1500)
    SetCameraDistance(14300, 1500)
    Sleep(100)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x5)
    Sound(804, 0, 100, 0)
    OP_6F(0x79)
    OP_A1(0x101, 0x3E8, 0x4, 0x6, 0x7, 0x6, 0x5)

    #C0085
    ChrTalk(
        0x101,
        (
            "#0000F#11Pキーア。\x01",
            "俺たちと一緒に来てくれるか？\x02\x03",

            "君のことは絶対に守るから。\x02",
        )
    )

    CloseMessageWindow()

    #N0086
    NpcTalk(
        0xF,
        "キーア",
        (
            "#5800F#5P？？？\x02\x03",

            "#5810Fよくわかんないけど\x01",
            "べつにいいよ～。\x02\x03",

            "#5809Fキーア、ロイドたちと一緒にいく！\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        "#0002F#11P……いい子だ。\x02",
    )

    CloseMessageWindow()
    OP_68(-4300, 1200, 0, 1000)
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(-3650, 1400, 0, 1000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x0)
    Sound(910, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_6F(0x79)
    OP_0D()

    #N0088
    NpcTalk(
        0x101,
        "キーア",
        "#5810F#5Pわぁ……！\x02",
    )

    CloseMessageWindow()
    OP_68(-920, 1400, 210, 1200)
    SetCameraDistance(16270, 1200)

    def lambda_2D73():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D73)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_2E57")

    #C0089
    ChrTalk(
        0x101,
        (
            "#0001F#5P──２人とも。\x01",
            "動きやすい格好に戻ってくれ。\x02\x03",

            "#0003Fそれと、外で待機している\x01",
            "ランディたちに連絡を──\x02\x03",

            "#0007Fこれより、この子を連れて\x01",
            "議長邸から脱出する……！\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x102,
        "#5307F……分かったわ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FFB")

    label("loc_2E57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_2F29")

    #C0091
    ChrTalk(
        0x101,
        (
            "#0001F#5P──２人とも。\x01",
            "動きやすい格好に戻ってくれ。\x02\x03",

            "#0003Fそれと、外で待機している\x01",
            "エリィたちに連絡を──\x02\x03",

            "#0007Fこれより、この子を連れて\x01",
            "議長邸から脱出する……！\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x103,
        "#5401F了解です……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2FFB")

    label("loc_2F29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_2FFB")

    #C0093
    ChrTalk(
        0x101,
        (
            "#0001F#5P──２人とも。\x01",
            "動きやすい格好に戻ってくれ。\x02\x03",

            "#0003Fそれと、外で待機している\x01",
            "エリィたちに連絡を──\x02\x03",

            "#0007Fこれより、この子を連れて\x01",
            "議長邸から脱出する……！\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x104,
        "#5607F#2Pアイアイ・サー！\x02",
    )

    CloseMessageWindow()

    label("loc_2FFB")


    #C0095
    ChrTalk(
        0xB,
        (
            "#5702F#11Pフフ……\x01",
            "楽しくなってきたじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16600, 1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x10, 0x1)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x32, 0xFF, 0xFF)
    Call(0, 26)
    OP_32(0x4, 0x0, 0x1D)
    RemoveCraft(0x4, 0xFFFF)
    OP_38(0x4, 0x80, 0x2)
    OP_38(0x4, 0x81, 0x1)
    OP_38(0x4, 0x82, 0x2)
    OP_38(0x4, 0x83, 0x2)
    OP_38(0x4, 0x84, 0x2)
    OP_38(0x4, 0x85, 0x2)
    OP_38(0x4, 0x86, 0x1)
    OP_42(0x4, 0x439, 0xFF)
    OP_42(0x4, 0x5E7, 0xFF)
    OP_42(0x4, 0x64B, 0xFF)
    AddCraft(0x4, 0xBE)
    AddCraft(0x4, 0xBF)
    AddCraft(0x4, 0xC0)
    AddCraft(0x4, 0x10E)
    SetChrChipPat(0x4, 0x6, 0x10E)
    AddCraft(0x4, 0x138)
    OP_42(0x4, 0x86, 0x0)
    OP_42(0x4, 0x77, 0x3)
    OP_42(0x4, 0x65, 0x4)
    OP_42(0x4, 0x6B, 0x5)
    OP_42(0x4, 0x7D, 0x6)
    OP_42(0x4, 0x71, 0x1)
    OP_42(0x4, 0x80, 0x2)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    OP_D5(0x2C)
    OP_D5(0x2D)
    OP_D5(0x2E)
    SetChrChipPat(0x0, 0x1, 0x9A)
    LoadChrChipPat()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_311A")
    SetChrChipPat(0x1, 0x1, 0x1)
    LoadChrChipPat()
    Jump("loc_3141")

    label("loc_311A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_3130")
    SetChrChipPat(0x2, 0x1, 0x2)
    LoadChrChipPat()
    Jump("loc_3141")

    label("loc_3130")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_3141")
    SetChrChipPat(0x3, 0x1, 0x3)
    LoadChrChipPat()

    label("loc_3141")

    SetChrPos(0x0, -2520, 0, -200, 90)
    OP_70(0x1, 0x5)
    SetMapObjFlags(0x1, 0x10)
    OP_65(0x0, 0x1)
    SetScenarioFlags(0xA6, 5)
    OP_29(0x47, 0x1, 0xF)
    OP_24(0x39C)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_13_12C5 end

    def Function_14_3172(): pass

    label("Function_14_3172")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_318E")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x2, 0x1)
    Jump("Function_14_3172")

    label("loc_318E")

    Return()

    # Function_14_3172 end

    def Function_15_318F(): pass

    label("Function_15_318F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31AD")
    OP_A1(0xFE, 0x3E8, 0x5, 0x10, 0x11, 0x12, 0x11, 0x10)
    Sleep(3000)
    Jump("Function_15_318F")

    label("loc_31AD")

    Return()

    # Function_15_318F end

    def Function_16_31AE(): pass

    label("Function_16_31AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_31CC")
    OP_A1(0xFE, 0x3E8, 0x5, 0x18, 0x19, 0x1A, 0x19, 0x18)
    Sleep(3000)
    Jump("Function_16_31AE")

    label("loc_31CC")

    Return()

    # Function_16_31AE end

    def Function_17_31CD(): pass

    label("Function_17_31CD")

    SetChrPos(0xFE, 9650, 0, 0, 270)

    def lambda_31E3():
        OP_95(0xFE, 4570, 0, 800, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_31E3)

    def lambda_31FD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_31FD)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_17_31CD end

    def Function_18_3221(): pass

    label("Function_18_3221")

    SetChrPos(0xFE, 9650, 0, 0, 270)

    def lambda_3237():
        OP_95(0xFE, 4570, 0, -800, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3237)

    def lambda_3251():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3251)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_18_3221 end

    def Function_19_3275(): pass

    label("Function_19_3275")

    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    OP_68(3130, 1400, 0, 800)
    MoveCamera(60, 16, 0, 800)
    SetCameraDistance(15330, 800)
    Sound(2091, 255, 100, 0)    #voice#Lazy
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    SetChrSubChip(0xFE, 0x3)

    def lambda_32C8():
        OP_9D(0xFE, 0xD02, 0x0, 0xFFFFFCCC, 0x640, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_32C8)
    Sound(814, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_82(0x1F4, 0x0, 0x1770, 0x190)
    Sound(2093, 255, 100, 0)    #voice#Lazy
    Sound(534, 0, 100, 0)
    OP_A1(0xFE, 0xDAC, 0x2, 0x14, 0x13)
    BeginChrThread(0xD, 3, 0, 24)
    Sleep(350)
    SetChrSubChip(0xFE, 0xE)
    Sleep(50)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x10)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_19_3275 end

    def Function_20_333F(): pass

    label("Function_20_333F")

    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    Sound(1294, 255, 100, 0)    #voice#Randy
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)

    def lambda_336C():
        OP_9D(0xFE, 0xDDE, 0x0, 0x35C, 0x4B0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_336C)
    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Sleep(200)
    OP_82(0x1F4, 0x0, 0x1770, 0x190)
    OP_68(5430, 1400, 0, 200)
    SetCameraDistance(16900, 200)
    SetChrSubChip(0xFE, 0x1)
    Sound(532, 0, 100, 0)
    BeginChrThread(0xC, 3, 0, 25)
    Sleep(500)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x10)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_20_333F end

    def Function_21_33E9(): pass

    label("Function_21_33E9")

    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    OP_68(3130, 1400, 0, 800)
    MoveCamera(60, 16, 0, 800)
    SetCameraDistance(15330, 800)
    Sound(2091, 255, 100, 0)    #voice#Lazy
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    SetChrSubChip(0xFE, 0x3)

    def lambda_343C():
        OP_9D(0xFE, 0xD02, 0x0, 0xFFFFFCCC, 0x640, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_343C)
    Sound(814, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Sleep(200)
    OP_82(0x1F4, 0x0, 0x1770, 0x190)
    Sound(2094, 255, 100, 0)    #voice#Lazy
    Sound(541, 0, 100, 0)
    OP_A1(0xFE, 0xDAC, 0x2, 0xE, 0xC)
    BeginChrThread(0xD, 3, 0, 24)
    OP_A1(0xFE, 0xDAC, 0x3, 0xA, 0x8, 0xC)
    Sleep(350)
    BeginChrThread(0xC, 3, 0, 22)
    OP_A1(0xFE, 0x9C4, 0x2, 0xD, 0x1)
    OP_6F(0x79)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    SetChrSubChip(0xFE, 0x1)

    def lambda_34C1():
        OP_9D(0xFE, 0xA0A, 0x0, 0xFFFFF8B2, 0x320, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_34C1)
    Sound(804, 0, 100, 0)
    WaitChrThread(0xFE, 1)

    def lambda_34E8():
        OP_9D(0xFE, 0xC3A, 0x0, 0xFFFFFC90, 0x320, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_34E8)
    Sound(534, 0, 100, 0)
    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_68(4300, 1400, 670, 150)
    OP_82(0x1F4, 0x0, 0x1770, 0x190)
    Sound(2093, 255, 100, 0)    #voice#Lazy
    SetChrSubChip(0xFE, 0x11)
    BeginChrThread(0xC, 3, 0, 23)
    OP_6F(0x79)
    OP_68(3130, 1400, 0, 1000)
    Sleep(500)
    OP_A1(0xFE, 0x3E8, 0x1, 0xD)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x10)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x3)
    SetChrSubChip(0xFE, 0x0)
    TurnDirection(0xFE, 0xC, 0)
    OP_6F(0x79)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xD, 1)
    Return()

    # Function_21_33E9 end

    def Function_22_358A(): pass

    label("Function_22_358A")

    OP_93(0xFE, 0xE1, 0x1F4)
    SetChrChipByIndex(0xFE, 0x2C)
    OP_A1(0xFE, 0xDAC, 0x2, 0x0, 0x1)
    SetChrFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x3)

    def lambda_35AB():
        OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_35AB)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_22_358A end

    def Function_23_35C5(): pass

    label("Function_23_35C5")

    PlayEffect(0xA, 0xFF, 0xFF, 0x0, 4570, 800, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)

    def lambda_360E():
        OP_96(0xFE, 0x1CAC, 0x3E8, 0x9B0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_360E)
    WaitChrThread(0xFE, 1)
    PlayEffect(0xA, 0xFF, 0xFE, 0x40, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(400)

    def lambda_366A():
        OP_96(0xFE, 0x1CAC, 0x0, 0x9B0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_366A)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Sound(514, 0, 100, 0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_23_35C5 end

    def Function_24_3693(): pass

    label("Function_24_3693")

    PlayEffect(0xA, 0xFF, 0xFF, 0x0, 4570, 800, -800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)

    def lambda_36DC():
        OP_96(0xFE, 0x1E1E, 0x3E8, 0xFFFFF70E, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_36DC)
    WaitChrThread(0xFE, 1)
    PlayEffect(0xA, 0xFF, 0xFE, 0x40, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(400)

    def lambda_3738():
        OP_96(0xFE, 0x1E1E, 0x0, 0xFFFFF70E, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3738)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Sound(514, 0, 100, 0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_24_3693 end

    def Function_25_3761(): pass

    label("Function_25_3761")

    PlayEffect(0xA, 0xFF, 0xFF, 0x0, 4570, 800, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x0)

    def lambda_37B1():
        OP_96(0xFE, 0x2094, 0x3E8, 0x62C, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_37B1)
    WaitChrThread(0xFE, 1)
    PlayEffect(0xA, 0xFF, 0xFE, 0x40, 0, 800, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(400)

    def lambda_380D():
        OP_96(0xFE, 0x2094, 0x0, 0x62C, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_380D)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Sound(514, 0, 100, 0)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_25_3761 end

    def Function_26_3836(): pass

    label("Function_26_3836")

    SetChrChipByIndex(0xC, 0x4)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x4)
    SetChrSubChip(0xD, 0x1)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x1)
    ClearChrFlags(0xD, 0x40)
    ClearChrFlags(0xD, 0x1)
    SetChrPos(0xC, 7340, 0, 2480, 225)
    SetChrPos(0xD, 7590, 0, -1830, 315)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xD, 0x10)
    Return()

    # Function_26_3836 end

    def Function_27_38B1(): pass

    label("Function_27_38B1")

    OP_25(0x39C, 0x5A)
    Sleep(1000)
    OP_25(0x39C, 0x50)
    Sleep(1000)
    OP_25(0x39C, 0x46)
    Sleep(1000)
    OP_25(0x39C, 0x3C)
    Sleep(1000)
    OP_25(0x39C, 0x32)
    Sleep(1000)
    OP_25(0x39C, 0x28)
    Sleep(1000)
    OP_25(0x39C, 0x1E)
    Sleep(1000)
    OP_25(0x39C, 0x14)
    Sleep(1000)
    OP_25(0x39C, 0xA)
    Sleep(1000)
    OP_24(0x39C)
    Return()

    # Function_27_38B1 end

    SaveToFile()

Try(main)
