from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4020.bin",                # FileName
        "e4020",                    # MapName
        "e4020",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, -123000, 0, 106000, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4020",                  # 0
        "クローディア姫",         # 1
        "レクター書記官",         # 2
        "ロックスミス大統領",     # 3
        "キーア",                 # 4
        "シズク",                 # 5
        "椅子",                   # 6
        "椅子",                   # 7
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(388, 0)                                        # 0

    ScpFunction((
        "Function_0_184",          # 00, 0
        "Function_1_1B9",          # 01, 1
        "Function_2_1BA",          # 02, 2
        "Function_3_1361",         # 03, 3
        "Function_4_13B6",         # 04, 4
        "Function_5_140B",         # 05, 5
        "Function_6_1460",         # 06, 6
        "Function_7_14B5",         # 07, 7
        "Function_8_150A",         # 08, 8
        "Function_9_155F",         # 09, 9
        "Function_10_26BA",        # 0A, 10
    ))


    def Function_0_184(): pass

    label("Function_0_184")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_198")
    ClearScenarioFlags(0x22, 0)
    Event(0, 9)
    Jump("loc_1A7")

    label("loc_198")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1A7")
    ClearScenarioFlags(0x22, 1)
    Event(0, 10)

    label("loc_1A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B8")
    Event(0, 2)

    label("loc_1B8")

    Return()

    # Function_0_184 end

    def Function_1_1B9(): pass

    label("Function_1_1B9")

    Return()

    # Function_1_1B9 end

    def Function_2_1BA(): pass

    label("Function_2_1BA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11000.itc", 0x1E)
    LoadChrToIndex("chr/ch12400.itc", 0x1F)
    SetChrPos(0x0, -55750, 0, 113000, 180)
    SetChrPos(0x1, -55100, 0, 114400, 180)
    SetChrPos(0x2, -53700, 0, 114400, 180)
    SetChrPos(0x3, -53000, 0, 113300, 270)
    SetChrPos(0x4, -52300, 0, 114700, 270)
    SetChrPos(0x5, -51200, 0, 114200, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -53000, 0, -2900, 270)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -55000, 0, -2900, 90)
    OP_68(-54000, 1100, 113000, 0)
    MoveCamera(51, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15820, 0)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_318")

    #C0001
    ChrTalk(
        0x101,
        "#00005F#5P（あれは……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_412")

    label("loc_318")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B")

    #C0002
    ChrTalk(
        0x102,
        "#00105F#5P（あれって……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_412")

    label("loc_34B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_380")

    #C0003
    ChrTalk(
        0x103,
        "#00205F#5P（……あれは……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_412")

    label("loc_380")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B3")

    #C0004
    ChrTalk(
        0x104,
        "#00301F#5P（なんだ……？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_412")

    label("loc_3B3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E6")

    #C0005
    ChrTalk(
        0x109,
        "#10105F#5P（あれれ……？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_412")

    label("loc_3E6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_412")

    #C0006
    ChrTalk(
        0x105,
        "#10302F#5P（へえ……？）\x02",
    )

    CloseMessageWindow()

    label("loc_412")

    StopBGM(0xFA0)
    OP_68(-54000, 1100, 100000, 3000)
    Sleep(1500)
    Fade(1000)
    OP_68(-54000, 1100, 3100, 0)
    MoveCamera(125, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_68(-54000, 1100, -2900, 3000)
    OP_0D()
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)
    Sleep(300)
    OP_68(-53970, 1100, -3250, 2000)
    MoveCamera(129, 16, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(14000, 2000)
    OP_6F(0x79)
    MoveCamera(133, 18, 0, 50000)
    SetCameraDistance(13270, 50000)
    Sleep(300)

    #C0007
    ChrTalk(
        0x8,
        (
            "#5P#07004Fそうですか……\x01",
            "ルーシー先輩と。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        (
            "#12P#11506Fああ、この前レミフェリアに\x01",
            "出張した時にバッタリとな。\x02\x03",

            "何とか逃げようとしたんだが\x01",
            "フン捕まっちまったよ。\x02\x03",

            "#11501F何発殴られたと思う？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "#5P#07002F……一発も。\x02\x03",

            "#07009F代わりに、しがみ付かれて\x01",
            "泣かれてしまったんじゃないですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x9,
        "#12P#11501F……む。\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "#5P#07004Fふふっ……\x01",
            "ルーシー先輩の気持ちは\x01",
            "分かりますから。\x02\x03",

            "#07001F多分、先輩が普段、\x01",
            "どれだけ危険な事をしているのか\x01",
            "気付いたんじゃないかと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x9,
        (
            "#12P#11506Fあー、女ってのはたまに\x01",
            "恐ろしく鋭くなるからなァ。\x02\x03",

            "#11510Fやりにくくて仕方ねぇぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "#5P#07004Fふふ、自業自得ですね。\x02\x03",

            "#07008F……懐かしいな。\x02\x01",

            "#07002Fレオ先輩とも会っていませんし、\x01",
            "いずれ同窓会とかしたいですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        "#12P#11501F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "#5P#07003F……先輩、駄目ですよ？\x02\x03",

            "#07002Fそこは『おお、ミシュラムあたりで\x01",
            "パーッっと豪勢にやるか！』\x01",
            "──とか言ってくれないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "#12P#11504Fハハ……一本取られたな。\x02\x03",

            "#11500F──約束はできんが\x01",
            "まあ、努力はしてみるさ。\x02\x03",

            "期待しないで待っててくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "#5P#07009F分かりました。\x01",
            "楽しみに待っています。\x02\x03",

            "#07002Fそれでは、私はこれで。\x01",
            "──失礼します。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x9,
        (
            "#12P#11509Fおお、ジークのやつにも\x01",
            "よろしく言っといてくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x8, 0xFFFF379C, 0xFFFFFC18, 0x15E)
    Sleep(300)
    OP_68(-52720, 1100, -2590, 3500)
    MoveCamera(133, 18, 0, 3500)
    SetCameraDistance(13270, 3500)

    def lambda_993():
        OP_95(0xFE, -51300, 0, -1000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_993)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0x5A, 0x1F4)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x1)

    def lambda_9D3():
        OP_95(0xFE, -48300, 0, -1000, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9D3)
    Sleep(1000)

    def lambda_9F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_9F0)
    WaitChrThread(0x8, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x1)
    Sleep(300)

    #C0019
    ChrTalk(
        0x9,
        (
            "#11P#11506Fやれやれ……\x01",
            "ホント成長してやがんなァ。\x02\x03",

            "#11500Fさすがは次期女王陛下。\x01",
            "──アンタらもそう思わないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#00011F……！\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x105,
        "#10302Fフフ、気付かれてたか。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-55530, 1100, -1440, 3000)
    MoveCamera(125, 21, 0, 3000)
    OP_6E(550, 3000)
    SetCameraDistance(16650, 3000)

    def lambda_AFA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_AFA)
    SetChrPos(0x101, -56200, 0, 7600, 180)
    SetChrPos(0x102, -54900, 0, 7600, 180)
    SetChrPos(0x103, -55900, 0, 8700, 180)
    SetChrPos(0x104, -54600, 0, 8700, 180)
    SetChrPos(0x109, -56200, 0, 9800, 180)
    SetChrPos(0x105, -54900, 0, 9800, 180)

    def lambda_B6D():
        OP_97(0x101, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B6D)
    Sleep(50)

    def lambda_B8A():
        OP_97(0x102, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B8A)
    Sleep(50)

    def lambda_BA7():
        OP_97(0x103, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BA7)
    Sleep(50)

    def lambda_BC4():
        OP_97(0x104, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BC4)
    Sleep(50)

    def lambda_BE1():
        OP_97(0x109, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BE1)
    Sleep(50)

    def lambda_BFE():
        OP_97(0x105, 0x0, 0x0, 0xFFFFE0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BFE)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    #C0022
    ChrTalk(
        0x101,
        (
            "#6P#00006F……すみません。\x01",
            "立ち聞きするつもりは\x01",
            "なかったんですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x102,
        (
            "#00103F#6Pその……\x01",
            "つい聞こえてしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x103,
        (
            "#6P#00202Fでも、エリィさん。\x01",
            "すごく興味津々でしたね？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    #C0025
    ChrTalk(
        0x102,
        "#5P#00112Fティ、ティオちゃん。\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x104,
        (
            "#00309F#6Pいや～、でも気になるぜ。\x02\x03",

            "#00302F一国のお姫様相手に\x01",
            "随分お安くないじゃねえの？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        (
            "#11503F#11Pあー、学校の後輩ってだけだ。\x02\x03",

            "#11500Fといっても日曜学校じゃなくて\x01",
            "ジェニス王立学園って所だが。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x105,
        (
            "#10305F#6Pジェニス王立学園……\x01",
            "たしかリベールにある\x01",
            "有名な高等学校だったかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        (
            "#00108F#6Pええ、確かに留学生も\x01",
            "多く受け入れているけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x109,
        (
            "#6P#10105Fそれじゃあ国費で\x01",
            "留学されていたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x9,
        (
            "#11504F#11Pいや、ポケットマネーさ。\x01",
            "──ギリアスのオッサンのな。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        "#6P#00013F！\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x9,
        (
            "#11504F#11Pそんじゃオレも\x01",
            "これで失礼させてもらうぜ。\x02\x03",

            "#11505Fああ、そういやアンタら\x01",
            "狸どもに呼ばれてるんだってな？\x02\x03",

            "#11509Fどちらも一筋縄じゃいかないから\x01",
            "せいぜい気をつけとけよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        "#6P#00011Fあ……\x02",
    )

    CloseMessageWindow()

    def lambda_FDB():

        label("loc_FDB")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_FDB")

    QueueWorkItem2(0x101, 2, lambda_FDB)

    def lambda_FED():

        label("loc_FED")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_FED")

    QueueWorkItem2(0x102, 2, lambda_FED)

    def lambda_FFF():

        label("loc_FFF")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_FFF")

    QueueWorkItem2(0x103, 2, lambda_FFF)

    def lambda_1011():

        label("loc_1011")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1011")

    QueueWorkItem2(0x109, 2, lambda_1011)

    def lambda_1023():

        label("loc_1023")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1023")

    QueueWorkItem2(0x105, 2, lambda_1023)

    def lambda_1035():

        label("loc_1035")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1035")

    QueueWorkItem2(0x104, 2, lambda_1035)

    def lambda_1047():
        OP_95(0xFE, -57100, 0, -1400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1047)
    WaitChrThread(0x9, 1)

    def lambda_1065():
        OP_95(0xFE, -57100, 0, 1900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1065)
    WaitChrThread(0x9, 1)
    StopBGM(0x1770)
    Fade(500)
    OP_68(-54000, 1100, 103000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, -56200, 0, 98800, 0)
    SetChrPos(0x102, -54900, 0, 98800, 0)
    SetChrPos(0x103, -55900, 0, 99900, 0)
    SetChrPos(0x104, -54600, 0, 99900, 0)
    SetChrPos(0x109, -56200, 0, 101000, 0)
    SetChrPos(0x105, -54900, 0, 101000, 0)
    SetChrPos(0x9, -55500, 0, 103000, 0)
    ClearChrFlags(0x9, 0x4)
    OP_68(-54000, 1100, 113000, 5000)
    SetCameraDistance(17500, 5000)

    def lambda_1151():
        OP_95(0xFE, -55500, 0, 112500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1151)
    WaitChrThread(0x9, 1)

    def lambda_116F():
        OP_95(0xFE, -51500, 0, 112500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_116F)
    WaitChrThread(0x9, 1)

    def lambda_118D():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_118D)
    Sleep(500)

    def lambda_11AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_11AA)
    WaitChrThread(0x9, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0x9, 0x80)
    OP_6F(0x79)
    Fade(500)
    OP_68(-55640, 1100, 100200, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_0D()

    #C0035
    ChrTalk(
        0x103,
        (
            "#12P#00211F……相変わらず\x01",
            "怪しさてんこ盛りな人ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x105,
        (
            "#10304F#11Pリベールの次期女王の\x01",
            "先輩にあたる情報将校か……\x02\x03",

            "#10302Fフフ、ますます興味深いね。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x101,
        (
            "#12P#00003F……いずれにしても\x01",
            "彼が《鉄血宰相》の配下として\x01",
            "動いているのは確かだ。\x02\x03",

            "#00001F何を狙っているのか……\x01",
            "見極める必要がありそうだな。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)
    SetScenarioFlags(0x142, 2)
    EventEnd(0x5)
    NewScene("c1550", 126, 0, 0)
    IdleLoop()
    Return()

    # Function_2_1BA end

    def Function_3_1361(): pass

    label("Function_3_1361")


    def lambda_1366():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1366)

    def lambda_1380():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1380)
    WaitChrThread(0xFE, 1)

    def lambda_1395():
        OP_95(0xFE, -122600, 0, 205400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1395)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_3_1361 end

    def Function_4_13B6(): pass

    label("Function_4_13B6")


    def lambda_13BB():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13BB)

    def lambda_13D5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13D5)
    WaitChrThread(0xFE, 1)

    def lambda_13EA():
        OP_95(0xFE, -122600, 0, 206600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13EA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_4_13B6 end

    def Function_5_140B(): pass

    label("Function_5_140B")


    def lambda_1410():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1410)

    def lambda_142A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_142A)
    WaitChrThread(0xFE, 1)

    def lambda_143F():
        OP_95(0xFE, -121500, 0, 204600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_143F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_5_140B end

    def Function_6_1460(): pass

    label("Function_6_1460")


    def lambda_1465():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1465)

    def lambda_147F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_147F)
    WaitChrThread(0xFE, 1)

    def lambda_1494():
        OP_95(0xFE, -121500, 0, 207400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1494)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_6_1460 end

    def Function_7_14B5(): pass

    label("Function_7_14B5")


    def lambda_14BA():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14BA)

    def lambda_14D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14D4)
    WaitChrThread(0xFE, 1)

    def lambda_14E9():
        OP_95(0xFE, -120800, 0, 205400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14E9)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_7_14B5 end

    def Function_8_150A(): pass

    label("Function_8_150A")


    def lambda_150F():
        OP_96(0xFE, 0xFFFE2C08, 0x0, 0x324B0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_150F)

    def lambda_1529():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1529)
    WaitChrThread(0xFE, 1)

    def lambda_153E():
        OP_95(0xFE, -120800, 0, 206600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_153E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_8_150A end

    def Function_9_155F(): pass

    label("Function_9_155F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11712.itc", 0x1E)
    LoadChrToIndex("chr/ch00002.itc", 0x1F)
    LoadChrToIndex("chr/ch00102.itc", 0x20)
    LoadChrToIndex("chr/ch00202.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch02902.itc", 0x23)
    LoadChrToIndex("chr/ch03002.itc", 0x24)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07500.itp")
    SetChrPos(0x101, -117500, 0, 206000, 270)
    SetChrPos(0x102, -117500, 0, 206000, 270)
    SetChrPos(0x103, -117500, 0, 206000, 270)
    SetChrPos(0x104, -117500, 0, 206000, 270)
    SetChrPos(0x109, -117500, 0, 206000, 270)
    SetChrPos(0x105, -117500, 0, 206000, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -130000, 50, 206000, 90)
    OP_68(-120300, 1100, 206000, 0)
    MoveCamera(55, 13, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    FadeToBright(1000, 0)
    StopBGM(0x1388)
    ClearMapObjFlags(0x7, 0x10)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x7)
    OP_68(-126300, 1100, 206000, 5000)
    SetCameraDistance(18500, 5000)
    BeginChrThread(0x101, 3, 0, 3)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 4)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 5)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 6)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 7)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 8)
    Sleep(1700)
    Sound(104, 0, 100, 0)
    OP_71(0x7, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x7)
    WaitChrThread(0x105, 3)

    #C0038
    ChrTalk(
        0x101,
        (
            "#00003F#11P──失礼します、閣下。\x02\x03",

            "#00001Fクロスベル警察、特務支援課、\x01",
            "お招きにより参上しました。\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7583", 0)

    #C0039
    ChrTalk(
        0xA,
        (
            "#6P#07509Fおお、よく来てくれたなぁ。\x02\x03",

            "#07500F遠慮はいらんよ。\x01",
            "さあ、座ってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#00000F#11Pは、はい。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        "#00104F#11Pそれではお言葉に甘えて……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-128500, 2700, 105900, 0)
    MoveCamera(303, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_68(-128500, 900, 105900, 3000)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x1)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x109, 0x23)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x105, 0x24)
    SetChrSubChip(0x105, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrPos(0x101, -128400, 50, 103900, 0)
    SetChrPos(0x102, -128199, 50, 107200, 200)
    SetChrPos(0x103, -127500, 50, 103900, 0)
    SetChrPos(0x104, -126700, 50, 107200, 200)
    SetChrPos(0x109, -126600, 50, 103900, 0)
    SetChrPos(0x105, -125700, 50, 103900, 0)
    SetChrPos(0xA, -130000, 50, 105900, 90)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xD, 0x80)
    OP_78(0xA, 0xD)
    ClearChrFlags(0xE, 0x80)
    OP_78(0xB, 0xE)
    OP_49()
    SetChrPos(0xD, -128100, 0, 107500, 20)
    OP_D5(0xD, 0x0, 0x4E20, 0x0, 0x0)
    SetChrPos(0xE, -126600, 0, 107500, 20)
    OP_D5(0xE, 0x0, 0x4E20, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    SetCameraDistance(15500, 80000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0042
    AnonymousTalk(
        0xA,
        (
            "わっはっは、\x01",
            "いきなり驚いただろう？\x02\x03",

            "いや～、こんな時でもないと\x01",
            "時間が取れんと思ったもんでな。\x02\x03",

            "忙しいだろうにスマンなぁ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0043
    ChrTalk(
        0x101,
        "#6P#00011Fい、いえ、そんな。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        "#00102Fお気遣いいただき恐縮です。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x1)
    Sleep(300)

    #C0045
    ChrTalk(
        0xA,
        (
            "#07505F#5Pたしか君は、マクダエル市長の\x01",
            "お孫さんだったかな？\x02\x03",

            "確か前に、祝賀会か何かで\x01",
            "お目にかかったことはないかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        (
            "#00104Fはい、祖父の付き添いで共和国を\x01",
            "訪ねた折にお目にかかっています。\x02\x03",

            "#00100F一昨年のことになりますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xA,
        (
            "#07509F#5Pおお、確かにそうだった。\x02\x03",

            "#07500Fしかし、あのマクダエル市長が\x01",
            "今は退#2Rしりぞ#かれて自治州議長とは……\x02\x03",

            "#07504Fあのお年にして、あの情熱。\x01",
            "まさに政治家の鑑#2Rかがみ#というものだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x102,
        (
            "#00109Fふふ、祖父が聞いたら\x01",
            "きっと喜ぶと思います。\x02\x03",

            "#00108Fところで閣下──\x01",
            "今日はどのような御用で？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x0)
    Sleep(300)

    #C0049
    ChrTalk(
        0xA,
        (
            "#07509F#5Pハハハ、君たちの話は\x01",
            "キリカ君から聞いていたのでな。\x02\x03",

            "#07500F《黒の競売会》の顛末も、\x01",
            "痛快だったそうじゃないかね？\x02\x03",

            "#07503Fこう言っちゃなんだが、\x01",
            "前のハルトマンという議長は\x01",
            "鼻持ちならない男だったからな。\x02\x03",

            "#07500Fその失脚のきっかけを作った\x01",
            "功労者たちの顔触れは\x01",
            "一度見ておきたかったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#6P#00002Fきょ、恐縮です。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        (
            "#12P#00306Fま、どっちかというと勝手に\x01",
            "自滅しただけみたいッスけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x103,
        (
            "#6P#00208F……そうですね。\x01",
            "あんな教団と関わっていた時点で\x01",
            "アウトではないかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xA,
        (
            "#07505F#5Pそうそう、それとその教団だ。\x02\x03",

            "#07503F《Ｄ∴Ｇ教団》──\x01",
            "大陸各地で悪さをしていたが、\x01",
            "最大の被害者は我が国でな。\x02\x03",

            "#07501F連中に止めを刺してくれた事も\x01",
            "改めて礼を言いたかったのだよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#6P#00011Fい、いえ……\x01",
            "当然の事をしただけですから。\x02\x03",

            "#00004Fそれに自分たちの貢献など\x01",
            "ほんの些細なもので──\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xA,
        (
            "#07509F#5Pわっはっはっ、謙遜は止めたまえ。\x02\x03",

            "何でも警備隊すら操られていた\x01",
            "危機的状況だったそうじゃないか？\x02\x03",

            "#07502Fそんな中、一人の少女を守って\x01",
            "邪悪な教団に立ち向かった……\x02\x03",

            "いやはや、中々できる事じゃない！\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#6P#00012Fいや……本当に恐縮です。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        "#00103F過分なお言葉、痛み入ります。\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xA,
        (
            "#07506F#5P実際、あの事件が下手に転んだら\x01",
            "大変なことになっていただろう。\x02\x03",

            "ＩＢＣも邪悪な教団に占拠され、\x01",
            "国際貿易と金融がストップする……\x02\x03",

            "#07501F──そうすれば共和国経済にも\x01",
            "深刻なダメージだったに違いない。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        "#6P#00001F……！\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        "#00108F……それは。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xA,
        (
            "#07505F#5Pふーむ、そうなると\x01",
            "君たちには勲章でも贈らないと\x01",
            "格好がつかんかもしれんなぁ。\x02\x03",

            "#07509Fよし、帰ったらすぐにでも\x01",
            "豪勢なのを手配させてもらおう！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#6P#00011Fい、いや……！\x01",
            "ちょっとお待ちください。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x103,
        (
            "#6P#00211F自治州での事件なのに\x01",
            "共和国政府から勲章をもらうのは\x01",
            "ちょっとおかしいような……\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        (
            "#12P#00306Fマクダエルのじーさまからも\x01",
            "既に表彰状を貰ってるしなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xA,
        (
            "#07504F#5Pなに、何もおかしい事はない。\x02\x03",

            "#07502F──クロスベルの問題は即ち、\x01",
            "宗主国である我が国の問題だからなぁ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0066
    ChrTalk(
        0x101,
        "#6P#00013F……っ。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x102,
        "#00108F……閣下………\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xA,
        (
            "#07509F#5Pハッハッハッ。\x01",
            "そんな顔をするもんじゃない。\x02\x03",

            "#07502F《鉄血宰相》にも\x01",
            "呼ばれておるのだろう？\x02\x03",

            "もう少し話したいところだが\x01",
            "そろそろ行くといいだろう。\x02\x03",

            "#07504F──ああ、勲章は必ず手配するから\x01",
            "楽しみに待っててくれたまえよ？\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x23, 1)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_9_155F end

    def Function_10_26BA(): pass

    label("Function_10_26BA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11600.itc", 0x1E)
    LoadChrToIndex("chr/ch05410.itc", 0x1F)
    LoadChrToIndex("apl/ch51603.itc", 0x20)
    LoadChrToIndex("apl/ch51604.itc", 0x21)
    LoadEffect(0x0, "event\\ev500_00.eff")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis412.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12300.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11202.itp")
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 26500, 0, 26800, 0)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 26500, 0, 19000, 0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x0, 31000, 0, 23000, 0)
    PlayEffect(0x0, 0xFF, 0xB, 0x1, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetMapObjFrame(0xFF, "wlight_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "toreru", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back_pano", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ent01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ent02", 0x0, 0x1)
    OP_68(26500, 1000, 26800, 0)
    MoveCamera(41, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16340, 0)
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    SetCameraDistance(15340, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)
    OP_64(0xB)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0069
    AnonymousTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#40W…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #N0070
    NpcTalk(
        0xC,
        "少女の声",
        "キーアちゃん……\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xB, 0xB4, 0x1F4)
    Fade(500)
    OP_68(26500, 1000, 24400, 0)
    MoveCamera(137, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "toreru", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back_pano", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ent01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ent02", 0x1, 0x1)
    OP_68(26500, 1000, 23450, 1500)
    OP_0D()
    OP_6F(0x79)

    #C0071
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12302F#5Pあ、シズク……\x02\x03",

            "もう目の調子はいいのー？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_68(26500, 1000, 25480, 3000)
    SetCameraDistance(14500, 3000)

    def lambda_2A7F():
        OP_95(0xFE, 26500, 0, 24900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2A7F)
    WaitChrThread(0xC, 1)
    OP_6F(0x79)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0072
    AnonymousTalk(
        0xC,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#30Wうん……もう眩暈#4Rめまい#もしないし、\x01",
            "色も見えるようになったし……\x02\x03",

            "全部……\x01",
            "キーアちゃんのおかげだよ。\x02\x03",

            "……本当にありがとう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    #C0073
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#5P#12309Fえへへ……よかった。\x02\x03",

            "#12302Fでも、シズクと病院の人たちが\x01",
            "ずっと頑張ってきたからだよ？\x02\x03",

            "キーアはあくまで\x01",
            "最後の一押しをしただけだし。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xC,
        "#11P#11226Fそうなんだ……\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#5P#12304Fそれにせっかくの“力”は\x01",
            "有効活用しないと勿体ないし。\x02\x03",

            "#12314Fえへへ、シズクの目が治せたなら\x01",
            "こうなった甲斐があったなって──\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(14000, 500)
    Fade(250)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x20)
    OP_0D()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0xC8)

    #C0076
    ChrTalk(
        0xC,
        "#11P#11232F#4S───でも！\x02",
    )

    CloseMessageWindow()

    def lambda_2D40():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2D40)
    WaitChrThread(0xC, 2)
    Sleep(300)

    #C0077
    ChrTalk(
        0xC,
        (
            "#11P#11226F#30W……わ、わたしは嬉しいよ……？\x02\x03",

            "ずっと目が見えなくて不安で……\x01",
            "……お父さんのお荷物になってて……\x02\x03",

            "#11228Fキーアちゃんと友だちになれたのに\x01",
            "どんな顔かもわからなくって……！\x02\x03",

            "#11227Fこうして顔が見られるのは\x01",
            "涙が出るほど嬉しいけど……っ！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(26500, 1000, 25870, 600)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xC, 0x2)
    ClearChrFlags(0xC, 0x20)

    def lambda_2E88():
        OP_95(0xFE, 26500, 0, 25400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2E88)
    WaitChrThread(0xC, 1)
    Sound(812, 0, 100, 0)
    OP_6F(0x79)
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0078
    ChrTalk(
        0xC,
        (
            "#11P#11232F#4Sでも……キーアちゃんは\x01",
            "本当にこのままでいいの！？\x02\x03",

            "#3Sロイドさんたちと別れて\x01",
            "大変なことをさせられて……！\x02\x03",

            "#11227Fわたし……こんなの\x01",
            "絶対に間違っていると思う！\x02\x03",

            "マリアベルさんも、ディーターさんも！\x02\x03",

            "#11232F#40W……それに…#500W…#40Wお父さんも……っ！\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#5P#12312F#30Wシズク……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_68(26500, 1000, 25400, 1000)

    def lambda_3007():
        OP_95(0xFE, 26500, 0, 26000, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3007)
    WaitChrThread(0xB, 1)
    Sleep(300)
    Fade(500)
    OP_68(26500, 1000, 25800, 0)
    MoveCamera(41, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    SetMapObjFrame(0xFF, "wlight_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "toreru", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back_pano", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ent01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "ent02", 0x0, 0x1)
    SetCameraDistance(13000, 13000)
    Sleep(300)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xB, 0x2)
    SetChrFlags(0xB, 0x20)
    SetChrChipByIndex(0xC, 0x21)
    SetChrSubChip(0xC, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x20)
    OP_0D()
    Sound(898, 0, 100, 0)
    Sleep(100)
    SetChrSubChip(0xB, 0x1)
    SetChrSubChip(0xC, 0x11)
    Sleep(100)
    SetChrSubChip(0xB, 0x2)
    SetChrSubChip(0xC, 0x12)
    Sleep(100)
    SetChrSubChip(0xB, 0x3)
    SetChrSubChip(0xC, 0x13)
    Sleep(100)
    SetChrSubChip(0xB, 0x4)
    SetChrSubChip(0xC, 0x14)
    Sleep(100)
    SetChrSubChip(0xB, 0x5)
    SetChrSubChip(0xC, 0x15)
    Sleep(100)
    SetChrSubChip(0xB, 0x6)
    SetChrSubChip(0xC, 0x16)
    Sleep(500)

    #C0080
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#5P#12304F#40Wありがとう……\x01",
            "大好きだよ、シズク。\x02\x03",

            "#12302Fでも……大丈夫だから。\x02\x03",

            "ぜんぶ分かった上で\x01",
            "自分で決めたことだから……\x02\x03",

            "#12309Fだからね……？\x01",
            "そんなに心配しないで──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(13500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E5(0xA)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_E5(0xB)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("t6050", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_26BA end

    SaveToFile()

Try(main)
