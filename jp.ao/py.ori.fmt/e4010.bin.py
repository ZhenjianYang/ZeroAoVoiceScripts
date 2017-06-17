from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4010.bin",                # FileName
        "e4010",                    # MapName
        "e4010",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4010",                  # 0
        "金髪の青年",             # 1
        "黒髪の軍人",             # 2
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(216, 0)                                        # 0

    ScpFunction((
        "Function_0_D8",           # 00, 0
        "Function_1_E8",           # 01, 1
        "Function_2_E9",           # 02, 2
    ))


    def Function_0_D8(): pass

    label("Function_0_D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_E7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_E7")

    Return()

    # Function_0_D8 end

    def Function_1_E8(): pass

    label("Function_1_E8")

    Return()

    # Function_1_E8 end

    def Function_2_E9(): pass

    label("Function_2_E9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11102.itc", 0x1E)
    LoadChrToIndex("chr/ch11300.itc", 0x1F)
    LoadChrToIndex("apl/ch51205.itc", 0x20)
    CreatePortrait(0, 16, 20, 528, 84, 0, 0, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis503.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07300.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07200.itp")
    SetChrPos(0x0, -7000, 0, 2000, 0)
    SetChrPos(0x1, -7000, 0, 2000, 0)
    SetChrPos(0x2, -7000, 0, 2000, 0)
    SetChrPos(0x3, -7000, 0, 2000, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 50, 7100, 180)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -7500, 0, -3000, 90)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sleep(500)
    Sound(103, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("青年の声")

    #A0001
    AnonymousTalk(
        0xFF,
        "──まだ起きていたのか。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapObjFlags(0x3, 0x10)
    OP_70(0x3, 0x5)
    OP_68(-6000, 1000, -3000, 0)
    MoveCamera(309, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    PlayBGM("ed7515", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_68(0, 1000, 5900, 8000)
    MoveCamera(315, 21, 0, 8000)
    SetCameraDistance(18500, 8000)

    def lambda_2D6():
        OP_95(0xFE, -4000, 0, -3000, 1800, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2D6)

    def lambda_2F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2F0)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    WaitChrThread(0x9, 1)

    def lambda_31B():
        OP_95(0xFE, 0, 0, 4300, 1800, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_31B)
    Sound(104, 0, 100, 0)
    OP_71(0x3, 0x5, 0x0, 0x0, 0x0)
    Sleep(3500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    WaitChrThread(0x9, 1)
    TurnDirection(0x9, 0x8, 500)
    OP_6F(0x79)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0002
    AnonymousTalk(
        0x9,
        (
            "明日の出発は早い。\x01",
            "いい加減、寝たらどうだ？\x02",
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

    #C0003
    ChrTalk(
        0x8,
        (
            "#11P#07208F#30Wあー……うん……\x02\x03",

            "#07203F一応、こちらの報告にも\x01",
            "目を通しておきたいからねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x9,
        (
            "#6P#07303F士官学校か……\x02\x03",

            "#07302Fまさかお前がそこまで\x01",
            "真面目に職務に励むとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "#11P#07204Fフフ、あくまで\x01",
            "名目上の理事でしかないけどね。\x02\x03",

            "#07200Fあの子たちも頑張ってるみたいだし、\x01",
            "このくらいはさせてもらわないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x9,
        (
            "#6P#07304Fフ……まあいいだろう。\x02\x03",

            "#07300F──しかしどうやら\x01",
            "例の話は確かなようだな。\x02\x03",

            "カイエン公の手の者が\x01",
            "密かに手を回しているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "#11P#07206Fあのヒトか……\x01",
            "そんな所じゃないかと思ったけど。\x02\x03",

            "#07200F規模の方は掴めているのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        (
            "#6P#07303Fいや、そちらは不明のままだ。\x02\x03",

            "#07300F情報局もその辺りは\x01",
            "掴み損ねているようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x8,
        (
            "#11P#07209Fアハハ、自業自得とはいえ\x01",
            "宰相殿も災難だねぇ。\x02\x03",

            "#07202Fフフ、意外とボクもまとめて\x01",
            "ターゲットにするつもりかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x9,
        (
            "#6P#07306F……洒落になっていないぞ。\x02\x03",

            "#07301Fやはり第七師団からの護衛を\x01",
            "増員した方がいいのではないか？\x02\x03",

            "今からねじ込む事も可能だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "#11P#07204Fいや、それには及ばない。\x02\x03",

            "宰相殿ならともかく、\x01",
            "ボクのキャラでそれをやったら\x01",
            "築いたイメージも台無しだろう。\x02\x03",

            "#07202Fそれに──\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(400)
    Sound(822, 0, 100, 0)
    OP_63(0x8, 0x12C, 1300, 0x36, 0x39, 0xFA, 0x0)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x20)
    SetCameraDistance(18200, 400)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    Sleep(100)
    SetChrSubChip(0x8, 0x1)
    Sleep(800)

    #C0012
    ChrTalk(
        0x8,
        (
            "#11P#07209Fボクにはキミがいるからね㈱\x02\x03",

            "#07212Fキミの腕の中で守ってもらえれば\x01",
            "もうそれだけで十分さっ！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x8)
    OP_63(0x8, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1200)
    OP_93(0x9, 0xB4, 0x1F4)

    #C0013
    ChrTalk(
        0x9,
        "#11P#07303F──さて、俺も早く寝るか。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x20)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(100)

    #C0014
    ChrTalk(
        0x8,
        (
            "#11P#07206Fスミマセン、調子に乗りました。\x02\x03",

            "#07200Fいずれにしても、明日のうちに\x01",
            "姫殿下と話をしておきたいかな。\x02\x03",

            "そちらの段取りはどうだい？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x0, 0x1F4)

    #C0015
    ChrTalk(
        0x9,
        (
            "#6P#07304Fああ、准佐殿と連絡は取れている。\x02\x03",

            "#07302F明日の昼食会の後──\x01",
            "夕方くらいの時間になるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "#11P#07202Fそうか……\x01",
            "フフ、１年ぶりくらいかな。\x02\x03",

            "#07206Fエステル君たちが残っていたら\x01",
            "同窓会が開けたんだけどねぇ。\x02\x03",

            "#07208Fシェラ君も忙しそうだから\x01",
            "出張できる余裕はなさそうだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        "#6P#07303F……そうだな。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "#11P#07204Fま、せいぜいボクは\x01",
            "最先端のアーバンリゾートを\x01",
            "満喫させてもらうとするさ。\x02\x03",

            "#07212Fあ、キミと准佐殿の逢引を\x01",
            "邪魔するつもりはないから\x01",
            "安心してくれたまえ㈱\x02\x03",

            "#07209F何だったら噂のテーマパークで\x01",
            "デートしてきたらどうだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x9,
        (
            "#6P#07306F──余計なお世話だ、阿呆。\x02\x03",

            "#07303Fしかし、いつも以上に\x01",
            "下らん戯言が多いようだが。\x02\x03",

            "#07301F……まさか良からぬことを\x01",
            "考えてるんじゃないだろうな？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "#11P#07211Fギクッ……\x02\x03",

            "#07209Fハハハ、ヤダナア。\x01",
            "ソンナワケナイジャナイカ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x9,
        (
            "#6P#07308F（……明日は首に\x01",
            "  縄でも付けておくか。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0022
    AnonymousTalk(
        0x8,
        (
            "──まあ多分、\x01",
            "これが最後の外遊になるだろう。\x02\x03",

            "宰相殿の狙いを探りつつ、\x01",
            "大陸全土の動向も見極める……\x02\x03",

            "相変わらず苦労をかけるけど\x01",
            "よろしく頼むよ──親友。\x02",
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

    #C0023
    ChrTalk(
        0x9,
        "#6P#07304Fフッ、無論だ。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18700, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("e430B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_E9 end

    SaveToFile()

Try(main)
