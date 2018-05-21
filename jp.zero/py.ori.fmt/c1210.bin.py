from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1210.bin",                # FileName
        "c1210",                    # MapName
        "c1210",                    # Location
        0x0021,                     # MapIndex
        "ed7114",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 33, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1210",                  # 0
        "ツァオ",                 # 1
        "黒月社員",               # 2
        "ラウ",                   # 3
        "銀",                     # 4
        "エマ捜査官",             # 5
        "ダドリー捜査官",         # 6
    ))

    AddCharChip((
        "chr/ch31500.itc",                   # 00
        "chr/ch06300.itc",                   # 01
        "chr/ch31400.itc",                   # 02
        "chr/ch06302.itc",                   # 03
        "chr/ch00000.itc",                   # 04
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

    DeclNpc(6000,    0,       0,       270,  261,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-34979,  0,       1870,    270,  389,  0x0, 0,   0,   0,   0,   0,   0,   3,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   2,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-72300,  0,       1900,    2000,    -72300,  1500,    1900,    0x007C, 0,  8,  0x0000)
    DeclActor(-37230,  0,       7940,    2000,    -37230,  1500,    7940,    0x007C, 0,  8,  0x0000)

    ScpFunction((
        "Function_0_220",          # 00, 0
        "Function_1_2D8",          # 01, 1
        "Function_2_334",          # 02, 2
        "Function_3_3E4",          # 03, 3
        "Function_4_43C",          # 04, 4
        "Function_5_209F",         # 05, 5
        "Function_6_277C",         # 06, 6
        "Function_7_539E",         # 07, 7
        "Function_8_53EF",         # 08, 8
    ))


    def Function_0_220(): pass

    label("Function_0_220")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_260"),
        (1, "loc_26C"),
        (2, "loc_278"),
        (3, "loc_284"),
        (4, "loc_290"),
        (5, "loc_29C"),
        (6, "loc_2A8"),
        (SWITCH_DEFAULT, "loc_2B4"),
    )


    label("loc_260")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_26C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_278")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_284")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_290")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_29C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_2A8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_2B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_2C0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2C0")

    label("loc_2D7")

    Return()

    # Function_0_220 end

    def Function_1_2D8(): pass

    label("Function_1_2D8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F7")
    Event(0, 4)
    Jump("loc_311")

    label("loc_2F7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_311")
    Event(0, 6)

    label("loc_311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_320")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 5)

    label("loc_320")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_333")
    ClearChrFlags(0x9, 0x80)

    label("loc_333")

    Return()

    # Function_1_2D8 end

    def Function_2_334(): pass

    label("Function_2_334")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A4")
    SetMapObjFrame(0xFF, "c122_tesri02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tama00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tama01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kuro01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ato", 0x0, 0x1)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x4, 0x2)
    ClearMapObjFlags(0x5, 0x2)
    Jump("loc_3E3")

    label("loc_3A4")

    SetMapObjFrame(0xFF, "c122_tesri01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "mae", 0x0, 0x1)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x1, 0x2)
    ClearMapObjFlags(0x2, 0x2)
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)

    label("loc_3E3")

    Return()

    # Function_2_334 end

    def Function_3_3E4(): pass

    label("Function_3_3E4")

    TalkBegin(0xFE)

    #N0001
    NpcTalk(
        0xFE,
        "男",
        "お待ちしておりました。\x02",
    )

    CloseMessageWindow()

    #N0002
    NpcTalk(
        0xFE,
        "男",
        (
            "──どうぞ。\x01",
            "こちらが支社長室になります。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_3_3E4 end

    def Function_4_43C(): pass

    label("Function_4_43C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    OP_68(-2500, 900, 0, 0)
    MoveCamera(47, 33, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -1900, 0, -600, 90)
    SetChrPos(0x102, -1900, 0, 500, 90)
    SetChrPos(0x103, -3000, 0, -600, 90)
    SetChrPos(0x104, -3000, 0, 500, 90)
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 5600, 50, 0, 270)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03200.itp")
    FadeToBright(1000, 0)
    OP_0D()

    #N0003
    NpcTalk(
        0x8,
        "青年の声",
        "#6Pやあ、よくいらっしゃいましたね。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(4500, 900, 0, 2000)
    SetCameraDistance(23500, 2000)
    MoveCamera(47, 27, 0, 2000)
    OP_6F(0x11)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 5700, 0, -1600, 270)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_92(0x8, 0x125C, 0xFFFFF5D8, 0x1F4)

    def lambda_62E():
        OP_95(0xFE, 4700, 0, -2600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_62E)
    WaitChrThread(0x8, 1)

    def lambda_64C():
        OP_95(0xFE, 200, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_64C)
    Sleep(1300)
    Fade(500)
    OP_68(-530, 1000, 80, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(21000, 0)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x10E, 0x0)

    #C0004
    ChrTalk(
        0x101,
        (
            "#6P#0003F初めまして……\x02\x03",

            "#0000Fクロスベル警察・特務支援課の\x01",
            "ロイド・バニングスといいます。\x02",
        )
    )

    CloseMessageWindow()

    #N0005
    NpcTalk(
        0x8,
        "東方風の青年",
        (
            "#3204F#11Pふふ……\x01",
            "こちらこそ、初めまして。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("東方風の青年")

    #A0006
    AnonymousTalk(
        0xFF,
        (
            "《黒月貿易公司》\x01",
            "クロスベル支社を任されている\x01",
            "ツァオ・リーといいます。\x02\x03",

            "ロイドさんに……\x01",
            "エリィさん、ランディさん、\x01",
            "ティオさんでよろしかったですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0007
    ChrTalk(
        0x101,
        "#6P#0011Fな……\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#0105Fど、どうして\x01",
            "私たちの名前まで……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "#3204F#11Pふふ、タネを明かしますと\x01",
            "クロスベルタイムズを愛読していまして。\x02\x03",

            "#3200Fあなた方の記事を読んで\x01",
            "ファンになってしまったんです。\x02\x03",

            "#3209Fそれで失礼ながら、色々ツテを使って\x01",
            "お名前を調べさせてもらったんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        "#6P#0003Fそ、そうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x104,
        (
            "#0306F#6P（おいおい……\x01",
            "  いきなり先制パンチかよ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x103,
        "#3P#0201F（頭脳派のキレ者……納得です。）\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#3209F#11Pいや～、私としては皆さんに\x01",
            "お会いできて光栄なんですが……\x02\x03",

            "#3200F本日はどのようなご用件で？\x02\x03",

            "もしや、当社の営業活動に\x01",
            "何か問題でもあったのでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        (
            "#6P#0006F……いえ、\x01",
            "そういう訳ではないんです。\x02\x03",

            "#0001F実は、自分たちは現在、\x01",
            "《アルカンシェル》に関係する\x01",
            "事件を調べていまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "#3205F#11P《アルカンシェル》……\x01",
            "ああ、あの有名な劇団の事ですね！\x02\x03",

            "#3206Fいや～、クロスベルに来たからには\x01",
            "私も一度は見ておきたいんですが\x01",
            "忙しくてなかなか時間が取れなくて。\x02\x03",

            "#3200Fそういえば今度、\x01",
            "新作が発表されるそうですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        "#6P#0000Fえ、ええ……\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x102,
        (
            "#0103F……実は、その新作の公演について\x01",
            "ちょっとした問題が起きていまして。\x02\x03",

            "#0100Fその捜査の一環として\x01",
            "こちらに伺わせてもらったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "#3203F#11Pふむふむ……\x01",
            "何か事情がありそうですね。\x02\x03",

            "#3200F分かりました、詳しい話を\x01",
            "聞かせていただきましょう。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21300, 1500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_6F(0x10)
    Sleep(500)
    OP_68(270, 800, 4510, 0)
    MoveCamera(69, 21, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrPos(0x101, -2600, 50, 4000, 90)
    SetChrPos(0x102, -2600, 50, 5000, 90)
    SetChrPos(0x103, -2600, 0, 2200, 45)
    SetChrPos(0x104, -2300, 0, 1400, 45)
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 750, 50, 4500, 270)
    SetCameraDistance(20500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(300)

    #C0019
    ChrTalk(
        0x8,
        "#5P#3203Fふむ……《銀#2Rイン#》ですか。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#6P#0000Fこちらの貿易会社は、\x01",
            "カルバード共和国の東方人街に\x01",
            "本社がおありだとか……\x02\x03",

            "もしかしたら、名前くらい\x01",
            "ご存知ではないかと思いまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "#5P#3204Fふふ……なるほど。\x02\x03",

            "#3200Fまるで私どもが、\x01",
            "その《銀》なる犯罪者と関わりが\x01",
            "あるかのような仰られようですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#6P#0003Fいえ、とんでもない。\x02\x03",

            "#0000F正直情報が少なくて……\x01",
            "こうして藁にもすがる思いで\x01",
            "お訪ねしたというだけなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "#5P#3204Fふふ、いいでしょう。\x02\x03",

            "#3200Fあくまで一般的な情報ですが……\x01",
            "《銀》についての、もう少し詳しい\x01",
            "伝説についてご披露しましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        "#6P#0001F……お願いします。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "#5P#3200F──《銀》という名前は、\x01",
            "共和国の東方人街では非常に有名です。\x02\x03",

            "#3203F仮面と黒衣で身を包み\x01",
            "素顔を見せない謎の凶手#4Rきょうしゅ#……\x02\x03",

            "影のように現れ、影のように消え、\x01",
            "狙った獲物は決して逃がさない……\x02\x03",

            "#3201Fそして……ここが肝心ですが、\x01",
            "どうやら不老不死という話なのです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0026
    ChrTalk(
        0x101,
        "#6P#0005Fふ、不老不死？\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        "#0101F#6Pそれはどういう……\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x8,
        (
            "#5P#3203Fどうやら《銀》は、百年以上前から\x01",
            "凶手として活動を続けているそうです。\x02\x03",

            "百年前といえば、カルバード共和国が\x01",
            "民主化された直後くらいの事ですね。\x02\x03",

            "#3201Fそして、その時の記録を調べると\x01",
            "確かに《銀》の名前が頻出するそうです。\x02\x03",

            "動乱期の最中、要人を次々と葬#2Rほうむ#った\x01",
            "黒衣に身を包んだ謎の魔人としてね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0029
    ChrTalk(
        0x101,
        (
            "#6P#0003F……ますますもって\x01",
            "荒唐無稽な話ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x104,
        (
            "#0300F#4Pやっぱり、ただの言い伝えで\x01",
            "実在はしてないんじゃねえのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        "#5P#3209Fいえ──実在しますよ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0032
    ChrTalk(
        0x101,
        "#6P#0013Fっ……！？\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x104,
        "#0301F#4Pなにぃ……？\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20300, 60000)

    #C0034
    ChrTalk(
        0x8,
        (
            "#5P#3202F東方人街の裏側においては\x01",
            "《銀》はただの伝説ではありません。\x02\x03",

            "正体不明ではありますが\x01",
            "条件さえ合えばミラで雇える\x01",
            "最高の刺客にして暗殺者……\x02\x03",

            "あらゆる暗器と符術を使いこなす、\x01",
            "神速の迅#2Rはや#さを秘めた闇の武術家……\x02\x03",

            "そんな存在として認知されています。\x02\x03",

            "#3204F噂では、とある組織に重宝され、\x01",
            "よく仕事を任されているのだとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x102,
        "#0101F#6P………………………………\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x103,
        "#0201F#12P……その組織というのは……\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#5P#3205Fああ、そうそう。\x01",
            "その《銀》ですが……\x02\x03",

            "噂では最近、東方人街から\x01",
            "姿を消してしまったそうですねぇ。\x02\x03",

            "#3204F何でも、その組織から\x01",
            "大きな仕事が入ったらしく……\x02\x03",

            "#3202Fとある自治州に向かったのだとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#6P#0013Fあんた……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "#5P#3202Fふふ、どうしました？\x02\x03",

            "その組織が何という名前なのか、\x01",
            "私はまだ申し上げていませんよ？\x02\x03",

            "#3209Fその自治州が何処なのかもね。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#6P#0010Fくっ……\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        (
            "#0103F#6P……どうやら貴方がたも\x01",
            "《ルバーチェ》と同じようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "#5P#3204Fふふ、たかが地方組織ごときと\x01",
            "同じにしないで頂きたい……\x01",
            "と言いたいところですが。\x02\x03",

            "彼らは彼らで、この特異な街に\x01",
            "抜け目なく適応しているだけはある。\x02\x03",

            "#3200Fなかなかに手強く、\x01",
            "私も手こずらせてもらっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x104,
        "#0301F#4Pおいおい……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x103,
        "#0211F#12P……ぶっちゃけましたね。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "#5P#3209Fふふ、あくまで“ビジネス”の\x01",
            "競争相手としての話ですよ。\x02\x03",

            "#3200Fクロスベルは自由な競争が\x01",
            "法によって保障されている場所……\x02\x03",

            "何か問題でもありますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        "#6P#0008F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x101)
    Sleep(300)

    #C0047
    ChrTalk(
        0x101,
        (
            "#6P#0003F……一つ、聞かせてください。\x02\x03",

            "#0001Fそのルバーチェとの競争の中に\x01",
            "アルカンシェルは入っていますか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0048
    ChrTalk(
        0x8,
        "#5P#3205Fほう……？\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#6P#0001F以前、ルバーチェの会長は、\x01",
            "アルカンシェルに対して\x01",
            "帝都興行を持ちかけたそうです。\x02\x03",

            "同じようなことを\x01",
            "お考えになってらっしゃるとか？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "#5P#3204Fふふ、確かに共和国の方では\x01",
            "そういった動きもあるようですが……\x02\x03",

            "あいにく、私どもの会社は\x01",
            "芸能方面には関わっておりません。\x02\x03",

            "#3201F──私としても不思議なのですよ。\x02\x03",

            "どうして、その脅迫状の最後に\x01",
            "そんな名前が書かれていたのかがね。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        "#6P#0006F……なるほど。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, -2300, 0, 4000, 90)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0052
    ChrTalk(
        0x101,
        (
            "#6P#0003F──色々と参考になりました。\x01",
            "どうも、ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1D98():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1D98)
    Sleep(100)

    def lambda_1DA8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1DA8)
    Sleep(300)

    #C0053
    ChrTalk(
        0x103,
        "#0205F#11Pロイドさん……？\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x104,
        "#0301F#11Pおい、いいのかよ？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(300)

    #C0055
    ChrTalk(
        0x101,
        (
            "#0006F#5Pこれ以上、ここにいても\x01",
            "得られるものは無さそうだ。\x02\x03",

            "#0000F色々と忙しいみたいだし、\x01",
            "そろそろ失礼させてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x102,
        "#0108F#5P……そうね。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x8,
        (
            "#5P#3204Fふふ、お気遣い感謝します。\x02\x03",

            "#3205F──ああそう、ロイドさん。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 500)

    def lambda_1F03():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1F03)

    #C0058
    ChrTalk(
        0x101,
        "#6P#0013F……なんでしょうか？\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x8,
        (
            "#5P#3200Fふふ……\x01",
            "そう恐い顔をしないでください。\x02\x03",

            "先ほども言ったように……\x01",
            "私があなた方のファンというのは\x01",
            "本当のことなんですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        "#6P#0011Fえ……\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x8,
        (
            "#5P#3204F今回の一件……\x01",
            "なかなかに興味深い。\x02\x03",

            "いちファンとして、あなた方が\x01",
            "どのように解決してくれるか……\x02\x03",

            "#3202F楽しみにさせて頂きますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    SetScenarioFlags(0x5C, 0)
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_43C end

    def Function_5_209F(): pass

    label("Function_5_209F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00500.itc", 0x1E)
    LoadChrToIndex("apl/ch50237.itc", 0x1F)
    LoadEffect(0x0, "event\\ev202_00.eff")
    OP_68(6280, 900, 1830, 0)
    MoveCamera(50, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21760, 0)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 5800, 0, 3300, 180)
    SetChrChipByIndex(0x8, 0x3)
    SetChrSubChip(0x8, 0x2)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 5600, 50, 0, 270)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("青年の声")

    #A0062
    AnonymousTalk(
        0xFF,
        "いやはや、助かりましたよ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetCameraDistance(20760, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)

    #C0063
    ChrTalk(
        0x8,
        (
            "#11P#3206Fあのまま事が運ばれていたら\x01",
            "どうなっていたことか……\x02\x03",

            "危うく、市長暗殺の容疑を\x01",
            "こちらに掛けられる所でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#0700Fフン……共和国派の議員どもと\x01",
            "繋がりを持ったりするからだ。\x02\x03",

            "私の名を、あの秘書に囁いたのは\x01",
            "ハルトマンという帝国派の議長……\x02\x03",

            "恐らくルバーチェの\x01",
            "会長あたりから聞いたのだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#11P#3204Fええ、そうでしょうね。\x02\x03",

            "秘書が暗殺まで企てるとは\x01",
            "思っていなかったでしょうが……\x02\x03",

            "#3200Fそれでも私たちを通じて\x01",
            "共和国派にダメージを与えるのが\x01",
            "目的だったに違いありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#0702Fフン、つくづく因果な街だ。\x02\x03",

            "#0700Fそれはともかく……\x01",
            "『私たち』など一緒にするな。\x02\x03",

            "こちらはいい迷惑だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#11P#3206Fやれやれ、つれないですねぇ。\x02\x03",

            "#3200Fまあ、議員との繋がりなど\x01",
            "その気になればいつでも切れます。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 5630, 0, -1610, 180)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_93(0x8, 0x2D, 0x190)
    OP_68(7110, 900, 1620, 1500)
    SetChrFlags(0x8, 0x4)

    def lambda_24D6():
        OP_96(0xFE, 0x1C84, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_24D6)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x5A, 0x190)
    OP_6F(0x1)
    Sleep(500)

    #C0068
    ChrTalk(
        0x8,
        (
            "#5P#3204F──お伝えしている通り、\x01",
            "こちらの攻勢は記念祭以降……\x02\x03",

            "#3210F最終日の仕掛けは\x01",
            "よろしく頼みますよ、《銀》殿。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#5Pフ……いいだろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0x5A, 0x190)
    Sound(1569, 255, 100, 0)    #voice#Yin
    Sleep(1000)

    #C0070
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#5P時間だ──行くぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayEffect(0x0, 0xFF, 0xB, 0x40, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(859, 0, 100, 0)
    SetChrChip(0x0, 0xB, 0x1E, 0x12C)

    def lambda_2619():
        OP_95(0xFE, 7300, 0, 3300, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2619)

    def lambda_2633():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2633)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xB, 2)
    SetChrChip(0x1, 0xB, 0x0, 0x0)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    Sleep(1000)
    OP_68(7300, 900, 1000, 2000)
    MoveCamera(40, 17, 0, 2000)
    SetCameraDistance(18500, 2000)
    OP_6F(0x79)
    Sleep(300)

    #C0071
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#5P#3209Fはは……\x01",
            "相変わらず神出鬼没な方だ。\x02\x03",

            "#3210Fしかし『時間』ですか……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x190)
    Sleep(300)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(130)
    SetChrSubChip(0x8, 0x1)
    Sleep(130)
    SetChrSubChip(0x8, 0x2)
    Sleep(130)
    SetChrSubChip(0x8, 0x3)
    Sound(882, 0, 100, 0)
    Sleep(500)
    OP_6F(0x10)

    #C0072
    ChrTalk(
        0x8,
        (
            "#11P#3204Fフフ……\x01",
            "一体何の『時間』なのやら。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    SetScenarioFlags(0x5C, 2)
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_209F end

    def Function_6_277C(): pass

    label("Function_6_277C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30500.itc", 0x1E)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    LoadChrToIndex("apl/ch50237.itc", 0x20)
    OP_68(1100, 1100, 0, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -4300, 0, 0, 90)
    SetChrPos(0x102, -4300, 0, 0, 90)
    SetChrPos(0x103, -4300, 0, 0, 90)
    SetChrPos(0x104, -4300, 0, 0, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 2200, 0, 0, 270)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, 2800, 0, -1000, 270)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xC, -200, 0, 900, 90)
    SetChrChipByIndex(0xD, 0x1F)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, 300, 0, 0, 90)
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00600.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03200.itp")
    FadeToBright(1000, 0)
    OP_0D()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0073
    AnonymousTalk(
        0xD,
        (
            "──ツァオさん。\x01",
            "今日の所はこれで失礼します。\x02\x03",

            "できればもう少し、\x01",
            "詳しい話を伺う事ができれば\x01",
            "こちらも協力できるのですが。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    #C0074
    ChrTalk(
        0x8,
        (
            "#3204F#11Pフフ、これは失礼。\x01",
            "何しろ深夜の事でしたからね。\x02\x03",

            "#3200F襲撃者が何者だったのか、\x01",
            "どうして当社が狙われたのか\x01",
            "皆目見当が付かないのですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xD,
        (
            "#6P#0603F……それにしては随分と\x01",
            "手際よく防戦されたようですね。\x02\x03",

            "#0600F１階と２階は酷い状況でしたが、\x01",
            "この部屋など綺麗なものだ。\x02\x03",

            "重機関銃で武装した相手に\x01",
            "一体どのように対処したのやら。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x8,
        (
            "#3209F#11Pはは、恐れ入ります。\x02\x03",

            "#3200Fただまあ、結局襲撃者には\x01",
            "逃げられてしまいましたからね。\x02\x03",

            "#3206Fこちらは何人も病院送り……\x01",
            "やれやれ、とんだ災難です。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xD,
        (
            "#6P#0603Fお悔やみ申し上げます。\x01",
            "それでは──\x02",
        )
    )

    CloseMessageWindow()
    Sound(811, 0, 100, 0)
    Sleep(500)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrPos(0x101, -4800, -1000, 0, 90)

    #N0078
    NpcTalk(
        0x101,
        "ロイドの声",
        "#2P──失礼します。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(103, 0, 100, 0)
    OP_68(-500, 1100, 0, 1500)
    SetCameraDistance(24000, 1500)
    SetChrPos(0x101, -4300, 0, 0, 90)

    def lambda_2CD6():
        OP_96(0xFE, 0xFFFFF894, 0x0, 0xFFFFFDA8, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2CD6)

    def lambda_2CF0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2CF0)

    def lambda_2D01():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2D01)
    Sleep(50)

    def lambda_2D11():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2D11)

    def lambda_2D1E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2D1E)
    Sleep(50)

    def lambda_2D2E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2D2E)
    Sleep(150)

    def lambda_2D3E():
        OP_96(0xFE, 0xFFFFF894, 0x0, 0x1F4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D3E)

    def lambda_2D58():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2D58)
    Sleep(400)

    def lambda_2D6C():
        OP_96(0xFE, 0xFFFFF448, 0x0, 0xFFFFFDA8, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2D6C)

    def lambda_2D86():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2D86)
    Sleep(350)

    def lambda_2D9A():
        OP_96(0xFE, 0xFFFFF448, 0x0, 0x1F4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2D9A)

    def lambda_2DB4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2DB4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0079
    ChrTalk(
        0xD,
        "#11P#0605Fお前たち……！？\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xC,
        "#5Pと、特務支援課……\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x8,
        (
            "#11P#3205Fおお、ロイドさん。\x01",
            "それに支援課の皆さんですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#6P#0003F失礼します、ツァオさん。\x02\x03",

            "#0000Fお忙しいかとは思いますが、\x01",
            "少々、話を伺っても構いませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x8,
        (
            "#11P#3204Fええ、もちろん構いませんとも。\x02\x03",

            "#3210F──それではダドリーさん。\x01",
            "事情聴取、お疲れさまでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xD,
        "#11P#0610Fくっ……失礼する！\x02",
    )

    CloseMessageWindow()

    def lambda_2F76():

        label("loc_2F76")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2F76")

    QueueWorkItem2(0x101, 2, lambda_2F76)

    def lambda_2F88():

        label("loc_2F88")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2F88")

    QueueWorkItem2(0x102, 2, lambda_2F88)

    def lambda_2F9A():

        label("loc_2F9A")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2F9A")

    QueueWorkItem2(0x103, 2, lambda_2F9A)

    def lambda_2FAC():

        label("loc_2FAC")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2FAC")

    QueueWorkItem2(0x104, 2, lambda_2FAC)

    def lambda_2FBE():
        OP_98(0xFE, 0x0, 0x0, 0x640, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2FBE)

    def lambda_2FD8():
        OP_98(0xFE, 0x0, 0x0, 0x640, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2FD8)
    Sleep(200)

    def lambda_2FF5():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2FF5)

    def lambda_3002():
        OP_98(0xFE, 0x0, 0x0, 0x640, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3002)

    def lambda_301C():
        OP_98(0xFE, 0x0, 0x0, 0x640, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_301C)
    Sleep(500)
    OP_68(-820, 1100, 110, 1000)

    def lambda_304A():
        OP_96(0xFE, 0xFFFFF768, 0x0, 0x0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_304A)
    WaitChrThread(0xD, 1)
    WaitChrThread(0x101, 1)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xD)
    Sleep(300)

    #C0085
    ChrTalk(
        0xD,
        (
            "#12P#0603F（腹立たしいが……\x01",
            "  ヤツの相手はお前たちに任せる。）\x02\x03",

            "#0600F（せいぜい情報を\x01",
            "  引き出してくるがいい。）\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        "#0005F#5P（あ……はい！）\x02",
    )

    CloseMessageWindow()

    def lambda_311E():
        OP_95(0xFE, -4800, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_311E)
    Sleep(600)
    BeginChrThread(0xC, 3, 0, 7)
    Sleep(100)

    def lambda_3144():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_3144)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xD, 2)
    WaitChrThread(0xC, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    Sound(104, 0, 100, 0)
    OP_68(1100, 1000, 0, 1500)
    SetCameraDistance(22500, 1500)
    OP_92(0x101, 0xFFFFFF38, 0xFFFFFDA8, 0x1F4)

    def lambda_31B2():
        OP_95(0xFE, -200, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_31B2)
    OP_92(0x102, 0xFFFFFF38, 0x1F4, 0x1F4)

    def lambda_31D9():
        OP_95(0xFE, -200, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_31D9)
    OP_92(0x103, 0xFFFFFA88, 0xFFFFFDA8, 0x1F4)

    def lambda_3200():
        OP_95(0xFE, -1400, 0, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3200)
    OP_92(0x104, 0xFFFFFA88, 0x1F4, 0x1F4)

    def lambda_3227():
        OP_95(0xFE, -1400, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3227)
    WaitChrThread(0x101, 1)

    def lambda_3245():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3245)
    WaitChrThread(0x102, 1)

    def lambda_3256():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3256)
    WaitChrThread(0x103, 1)

    def lambda_3267():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_3267)
    WaitChrThread(0x104, 1)

    def lambda_3278():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3278)
    WaitChrThread(0x104, 2)
    OP_6F(0x11)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0087
    AnonymousTalk(
        0x8,
        (
            "フフ、お久しぶりですね。\x01",
            "ロイドさん、それに皆さん。\x02\x03",

            "記念祭の最終日は、なかなかの\x01",
            "ご活躍ぶりだったそうですね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x2, 0x0)

    #C0088
    ChrTalk(
        0x101,
        (
            "#6P#0003F《銀#2Rイン#》からの情報ですか……\x02\x03",

            "#0001F──俺たち《特務支援課》は\x01",
            "通常の捜査体制から外れています。\x02\x03",

            "それを踏まえて、率直な本音で\x01",
            "話をさせてもらってもいいですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_349A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_349A)
    Sleep(50)

    def lambda_34AA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_34AA)
    WaitChrThread(0x104, 2)

    #C0089
    ChrTalk(
        0x8,
        "#3210F#11Pほう……？\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x102,
        "#0105F#5Pロ、ロイド……？\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#5P#0006Fこの人相手に、肚#2Rハラ#の読み合いは\x01",
            "時間の無駄だろうからね。\x02\x03",

            "#0000F他にも色々聞きたい事もあるし\x01",
            "今回は単刀直入に行かせてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x104,
        (
            "#6P#0306Fおいおい……\x01",
            "ぶっちゃけたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x103,
        (
            "#6P#0202Fロイドさん……\x01",
            "たまに大胆ですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        "#3202F#11Pフフ……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #C0095
    ChrTalk(
        0x8,
        "#11P#3209F#4Sハハハハハハハッ！\x02",
    )

    CloseMessageWindow()

    def lambda_3636():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3636)

    def lambda_3643():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3643)

    def lambda_3650():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_3650)
    WaitChrThread(0x101, 2)
    Sleep(300)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sound(820, 0, 100, 0)
    Sleep(130)
    SetChrSubChip(0x8, 0x1)
    Sleep(130)
    SetChrSubChip(0x8, 0x2)
    Sleep(130)
    SetChrSubChip(0x8, 0x3)
    Sound(882, 0, 100, 0)
    Sleep(500)

    #C0096
    ChrTalk(
        0x8,
        (
            "#3204F#11P──さすがはロイドさん。\x01",
            "私が見込んだだけはありますね。\x02\x03",

            "#3210Fいいでしょう。\x01",
            "私も無意味なやり取りは\x01",
            "あまり好きではありません。\x02\x03",

            "答えられる範囲であれば\x01",
            "一通り答えさせて頂きますよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#6P#0004F──感謝します。\x02\x03",

            "#0001Fお聞きしたいのは\x01",
            "以下の３点についてです。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x8, 0x1)
    SetChrSubChip(0x8, 0x0)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x0, 1)
    ClearScenarioFlags(0x0, 2)

    label("loc_37BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3858")
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【襲撃者の正体について】\x01",      # 0
            "【今後の対応について】\x01",        # 1
            "【キーアの素性について】\x01",      # 2
            "【質問をやめる】\x01",              # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_38C5")

    label("loc_3858")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【襲撃者の正体について】\x01",      # 0
            "【今後の対応について】\x01",        # 1
            "【キーアの素性について】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_38C5")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_38E7"),
        (1, "loc_40AE"),
        (2, "loc_4716"),
        (3, "loc_4EE9"),
        (SWITCH_DEFAULT, "loc_4EF1"),
    )


    label("loc_38E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FC3")

    #C0098
    ChrTalk(
        0x101,
        (
            "#6P#0001F昨晩の襲撃者ですが……\x01",
            "ルバーチェで間違いありませんか？\x02\x03",

            "全く関係ない連中が\x01",
            "襲ってきたという可能性は？\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x8,
        (
            "#3200F#11Pフフ……\x01",
            "まずその可能性を疑いますか。\x02\x03",

            "#3204F──ラウ。\x01",
            "答えてあげてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xA,
        "#11Pは。\x02",
    )

    CloseMessageWindow()

    def lambda_39D7():
        OP_96(0xFE, 0x834, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_39D7)
    WaitChrThread(0xA, 1)
    Sleep(300)

    #C0101
    ChrTalk(
        0xA,
        (
            "#11P……襲撃者たちは\x01",
            "覆面で正体を隠していましたが\x01",
            "間違いなくルバーチェの配下でしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xA,
        (
            "#11P武装が同じでしたし、\x01",
            "何よりもクセが似ていました。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "#11Pそういうものは簡単に\x01",
            "偽装できるものではありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x101,
        "#6P#0005Fなるほど……\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x104,
        (
            "#6P#0306Fしかし、そうなると\x01",
            "少々解せなくなってくるな。\x02\x03",

            "#0301Fアンタら《黒月》の構成員は\x01",
            "相当な武術家揃いと聞いている。\x02\x03",

            "#0300Fそっちの兄さんも\x01",
            "かなりの腕みたいだしな？\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xA,
        "#11P……恐れ入ります。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x104,
        (
            "#6P#0303F一方ルバーチェの方は\x01",
            "戦闘のプロではあるんだろうが\x01",
            "一人一人はアンタら程じゃねえ。\x02\x03",

            "なのにどうしてここまで\x01",
            "遅れを取っちまったのか……\x02\x03",

            "#0301Fあの《キリングベア》の\x01",
            "オッサンでも襲ってきたかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x8,
        (
            "#3204F#11Pいや、かの営業本部長殿は\x01",
            "参加していなかったようですね。\x02\x03",

            "#3200F彼の右腕を務める元猟兵たちも\x01",
            "参加はしていなかったようです。\x02\x03",

            "ルバーチェの中でも平均的な\x01",
            "戦闘能力の者たちだけでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x101,
        "#6P#0013Fだったらどうして……\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        (
            "#11P──戦闘技術は並み程度ですが\x01",
            "力とスピードが段違いでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xA,
        (
            "#11P重機関銃を片手で軽々と振り回して\x01",
            "力任せに突入してきたのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xA,
        (
            "#11Pおかげでこちらの守りを崩され\x01",
            "２階まで制圧されてしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x104,
        "#6P#0301Fそいつは……\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x103,
        "#6P#0201F………………………………\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x8,
        (
            "#3200F#11P力とスピードだけでなく、\x01",
            "タフさも大したものでしたね。\x02\x03",

            "#3204Fおかげで少々、危険な技を\x01",
            "使う事になってしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        "#0101Fき、危険な技……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#6P#0001F……どうやら貴方自身も\x01",
            "かなりの使い手のようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x8,
        (
            "#3210F#11Pフフ、《銀》殿に比べれば\x01",
            "素人同然ではありますがね。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_3F9F():
        OP_96(0xFE, 0xAF0, 0x0, 0xFFFFFC18, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3F9F)
    WaitChrThread(0xA, 1)
    Sleep(300)
    SetScenarioFlags(0x0, 0)
    Jump("loc_40A9")

    label("loc_3FC3")


    #C0119
    ChrTalk(
        0x8,
        (
            "#3204F#11P覆面で正体を隠していましたが\x01",
            "ルバーチェの一般的な\x01",
            "構成員で間違いないでしょう。\x02\x03",

            "#3200F戦闘技術は並み程度でしたが……\x01",
            "異常なほどの力とスピード、\x01",
            "そしてタフさを持っていました。\x02\x03",

            "#3209Fフフ、どういう事なのでしょうね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40A9")

    Jump("loc_4EF1")

    label("loc_40AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_464C")

    #C0120
    ChrTalk(
        0x101,
        (
            "#6P#0003F率直にお聞きします。\x02\x03",

            "#0001F──今回の事件を受けて\x01",
            "どう対処されるおつもりですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x8,
        (
            "#3210F#11Pフフ……\x01",
            "何を聞かれるかと思えば。\x02\x03",

            "我々がどういう存在であるかを\x01",
            "考えれば訊ねるまでもないのでは？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        "#6P#0013F………………………………\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x102,
        "#0103F報復──というわけですか。\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x8,
        (
            "#3204F#11Pフフ、人聞きの悪いことを\x01",
            "言わないでください。\x02\x03",

            "我々はあくまで営利会社……\x01",
            "危機管理の話をしているだけです。\x02\x03",

            "#3210F自社の利益を損ねる状況があれば\x01",
            "妥当な方法でそれを改善する……\x02\x03",

            "何かおかしいことがありますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x104,
        "#6P#0301Fハン……\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x103,
        (
            "#6P#0211F……本当に\x01",
            "物は言いようですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0127
    ChrTalk(
        0x101,
        (
            "#6P#0001Fその“妥当な方法”の中に\x01",
            "“本社”の援助を要請されるご予定は？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0128
    ChrTalk(
        0x102,
        "#0108Fあ……\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x104,
        "#6P#0301F《黒月》本体からの増援か……\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x8,
        (
            "#3209F#11Pハハ、本当に率直な人だ。\x02\x03",

            "#3204F──私にも面子があるのでね。\x01",
            "今の所、その予定はありません。\x02\x03",

            "#3210Fもっとも状況次第では\x01",
            "“本社”が無理矢理介入してくる\x01",
            "可能性もあるでしょうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        "#6P#0013F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x8,
        (
            "#3200F#11Pフフ、まあしばらくの間は\x01",
            "直接介入は抑えられるでしょう。\x02\x03",

            "#3204F──いずれにせよ、\x01",
            "先方#4Rルバーチェ#の状況が掴めない事には\x01",
            "こちらも対処しようがありません。\x02\x03",

            "ちょうど今、そのあたりを\x01",
            "探ってもらっている最中ですよ。\x02\x03",

            "#3200F我らの頼もしい協力者に、ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x103,
        "#6P#0205F《銀#2Rイン#》さんに……\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x104,
        (
            "#6P#0306Fま、こういう状況には\x01",
            "打ってつけのヤツだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_4711")

    label("loc_464C")


    #C0135
    ChrTalk(
        0x8,
        (
            "#3204F#11P“本社”の介入はあり得ますが\x01",
            "今の所はクロスベル支社だけで\x01",
            "対処してみるつもりです。\x02\x03",

            "#3200Fちょうど今、ルバーチェの状況を\x01",
            "探ってもらっている最中ですよ。\x02\x03",

            "我らの頼もしい協力者に、ね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4711")

    Jump("loc_4EF1")

    label("loc_4716")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E0A")

    #C0136
    ChrTalk(
        0x101,
        (
            "#6P#0003F今回の件とは\x01",
            "直接関係ない話なんですが、\x01",
            "せっかくなのでお聞きします。\x02\x03",

            "#0001F──あなた方は本当に、\x01",
            "キーアをご存知ないんですか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_47B3():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_47B3)
    Sleep(50)

    def lambda_47C3():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_47C3)
    Sleep(300)

    #C0137
    ChrTalk(
        0x103,
        "#6P#0205Fあ……\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x102,
        "#0101F#5Pロイド、それは……\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x8,
        (
            "#3205F#11Pふむ、キーア……ですか？\x02\x03",

            "#3209Fそれは人名ですか？\x01",
            "それとも暗号か何か？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x101,
        "#6P#0013F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x8,
        (
            "#3206F#11P失礼──\x01",
            "どうやら本気のようですね。\x02\x03",

            "#3200F一応、例の競売会で\x01",
            "あなた方が保護した少女の\x01",
            "名前である事は存じています。\x02\x03",

            "我らの協力者が、あなた方に\x01",
            "ちょっとした助言をした事もね。\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x3C, 0x1F4)
    FadeToDark(500, 0, -1)
    OP_0D()
    Sleep(500)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0142
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "そちらの奥の部屋には\x01",
            "競売会後半の出品物がある……\x02\x03",

            "《黒月》に流れた情報によると\x01",
            "面白い“爆弾”があるらしいぞ？\x02\x03",

            "その目で確かめてみるといい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)

    def lambda_4A1B():
        OP_93(0xFE, 0x5A, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4A1B)

    def lambda_4A28():
        OP_93(0xFE, 0x5A, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4A28)
    FadeToBright(500, 0)
    OP_0D()
    VolumeBGM(0x64, 0x1F4)
    Sleep(500)

    #C0143
    ChrTalk(
        0x8,
        (
            "#3203F#11P『競売会の最後に出品される\x01",
            "  革張りの大きなトランク……』\x02\x03",

            "『その中にはルバーチェの立場を\x01",
            "  危うくする“爆弾”が仕込まれている』\x02\x03",

            "#3201F──その情報は我々の元に\x01",
            "複雑なルートで届けられました。\x02\x03",

            "情報提供者は不明……\x01",
            "結局掴む事はできませんでしたが\x01",
            "逆にそれが信憑性を高めました。\x02\x03",

            "#3204Fそこで念のため、我らの協力者に\x01",
            "確かめに行くよう頼んだのです。\x02\x03",

            "#3210Fまさか“爆弾”の正体が\x01",
            "そのようなものであるとは\x01",
            "夢にも思っていませんでしたがね。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x104,
        (
            "#6P#0301Fったく、どいつもこいつも\x01",
            "知らぬ存ぜぬの一点張りかよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x102,
        (
            "#0106F仮にその話が本当だとして……\x02\x03",

            "#0101F情報提供者について、\x01",
            "何か心当たりはないんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x8,
        (
            "#3204F#11Pさて、順当に考えるならば\x01",
            "ルバーチェ側の関係者による\x01",
            "裏切りが考えられそうですが……\x02\x03",

            "こちらに情報を届けた手並みといい、\x01",
            "抜け目のない相手ではありそうですね。\x02\x03",

            "#3200F──いずれにせよ、キーアさんについて\x01",
            "我々が知っている事実はそれだけです。\x02\x03",

            "どうか信じて頂けませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            "#6P#0006F……分かりました。\x01",
            "正直に答えて下さって感謝します。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4EE4")

    label("loc_4E0A")


    #C0148
    ChrTalk(
        0x8,
        (
            "#3203F#11Pキーアさんの素性については\x01",
            "残念ながら我々も一切知りません。\x02\x03",

            "#3200Fもし我々の情報網に\x01",
            "それらしき人物が引っかかったら\x01",
            "そちらにもお伝えしますよ。\x02\x03",

            "#3209F──こちらの不手際で\x01",
            "誤解させてしまったお詫びにね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EE4")

    Jump("loc_4EF1")

    label("loc_4EE9")

    SetScenarioFlags(0x0, 3)
    Jump("loc_4EF1")

    label("loc_4EF1")

    Jump("loc_37BA")

    label("loc_4EF6")


    #C0149
    ChrTalk(
        0x8,
        (
            "#3200F#11Pさて……\x01",
            "ご質問はそれだけですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#6P#0003Fええ、色々と\x01",
            "答えていただけて感謝します。\x02\x03",

            "#0001F概要については、警察本部にも\x01",
            "伝えても構いませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x8,
        (
            "#3204F#11Pフフ、ご随意に……\x02\x03",

            "#3200F──ねえ、ロイドさん。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        "#6P#0005Fはい……？\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x8,
        (
            "#3200F#11P正直、今回の襲撃は\x01",
            "少々想定外の出来事でした。\x02\x03",

            "彼らの戦力とコネクション、\x01",
            "そして思考パターンは読み切った\x01",
            "つもりだったからです。\x02\x03",

            "#3204Fそして、現状で彼らが\x01",
            "思い切った事をするはずがない……\x02\x03",

            "#3210Fその予想が見事、覆#2Rくつがえ#されました。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x101,
        "#6P#0001F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x8,
        (
            "#3209F#11Pフフ、ですから私は今、\x01",
            "非常にワクワクしているんですよ。\x02\x03",

            "ここ数年、私の見込みどおりに\x01",
            "事が運ばなかったことなど\x01",
            "久しくありませんでしたから。\x02\x03",

            "#3202Fこれでようやく、思う存分、\x01",
            "力と知恵を振るうことが出来る……\x02\x03",

            "そんな悦びすら感じている所です。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x101,
        "#6P#0013F！？\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x104,
        "#6P#0310Fおいおい……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x102,
        "#0110F……貴方は……\x02",
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x103,
        "#6P#0206Fとんでもないです……\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x8,
        (
            "#3204F#11Pフフ、警察ごときに私の楽しみを\x01",
            "邪魔されるつもりはありませんが……\x02\x03",

            "あなた方にだけは\x01",
            "特別に“機会”を与えましょう。\x02\x03",

            "#3202F我々が本格的に動き始める前に\x01",
            "何らかの解決方法を提示できるか……\x02\x03",

            "興味深く拝見させて頂きますよ？\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(23000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x5C, 3)
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_277C end

    def Function_7_539E(): pass

    label("Function_7_539E")


    def lambda_53A3():
        OP_95(0xFE, -1600, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_53A3)
    WaitChrThread(0xC, 1)

    def lambda_53C1():
        OP_95(0xFE, -4800, 0, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_53C1)
    Sleep(900)

    def lambda_53DE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_53DE)
    WaitChrThread(0xC, 1)
    Return()

    # Function_7_539E end

    def Function_8_53EF(): pass

    label("Function_8_53EF")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0161
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉は固く閉ざされている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_8_53EF end

    SaveToFile()

Try(main)
