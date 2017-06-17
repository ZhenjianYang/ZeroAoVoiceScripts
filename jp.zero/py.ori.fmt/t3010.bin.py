from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t3010.bin",                # FileName
        "t3010",                    # MapName
        "t3010",                    # Location
        0x005B,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "t3010",                  # 0
        "レン",                   # 1
        "ヨルグ老人",             # 2
        "パテルマテル",           # 3
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_F8",           # 00, 0
        "Function_1_108",          # 01, 1
        "Function_2_109",          # 02, 2
        "Function_3_116D",         # 03, 3
    ))


    def Function_0_F8(): pass

    label("Function_0_F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_107")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 2)

    label("loc_107")

    Return()

    # Function_0_F8 end

    def Function_1_108(): pass

    label("Function_1_108")

    Return()

    # Function_1_108 end

    def Function_2_109(): pass

    label("Function_2_109")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch09500.itc", 0x1E)
    LoadChrToIndex("chr/ch06600.itc", 0x1F)
    LoadChrToIndex("apl/ch50500.itc", 0x20)
    LoadChrToIndex("chr/ch09502.itc", 0x21)
    LoadEffect(0x0, "event\\ev622_00.eff")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis162.itp")
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, -5800, 200, 6000, 0)
    SetChrFlags(0x8, 0x8000)
    BeginChrThread(0x8, 0, 0, 3)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 0, 0, 7100, 180)
    SetChrFlags(0x9, 0x8000)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_78(0x1, 0xA)
    OP_49()
    OP_74(0x1, 0xF)
    OP_70(0x1, 0x65)
    SetChrPos(0xA, 8930, 750, -140, 270)
    OP_D3(0xA, 0x0, 0x41EB0, 0x0, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03900.itp")
    Sleep(1000)
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#1K同日、１４：４０──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    Sound(850, 0, 90, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("少女の声")

    #A0002
    AnonymousTalk(
        0xFF,
        "──ふぅん、なるほど。\x02",
    )

    CloseMessageWindow()

    #A0003
    AnonymousTalk(
        0xFF,
        (
            "お兄さんたちもやっと\x01",
            "そこまで辿りついたみたいね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7304", 0)
    FadeToBright(1000, 0)
    OP_68(-960, 2500, 1000, 0)
    MoveCamera(30, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21390, 0)
    OP_68(-5320, 2500, 3850, 8000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(-7120, 1700, 5020, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(12500, 0)
    SetCameraDistance(12000, 2500)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)

    #C0004
    ChrTalk(
        0x8,
        (
            "#3302F#11P出席者も揃って\x01",
            "招待状も届けられた……\x02\x03",

            "これで宴#2Rパーティ#の準備は\x01",
            "ぜんぶ整ったのかしら？\x02\x03",

            "#3304F先に鬼さんを見つけるのは\x01",
            "エステルたち？　お兄さんたち？\x02\x03",

            "#3308Fそれとも──\x02",
        )
    )

    CloseMessageWindow()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    Sleep(250)

    #N0005
    NpcTalk(
        0x9,
        "老人の声",
        (
            "#4P……相変わらず\x01",
            "全てが見えておるらしいな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-6020, 1700, 4270, 4000)
    MoveCamera(46, 15, 0, 4000)
    OP_6E(500, 4000)
    SetCameraDistance(14300, 4000)

    def lambda_513():
        OP_9B(0x0, 0xFE, 0x0, 0x708, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_513)

    def lambda_528():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_528)
    Sleep(500)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    Sound(107, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)

    def lambda_55F():
        OP_95(0xFE, -4200, 0, 5300, 1800, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_55F)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    Sleep(300)

    #C0006
    ChrTalk(
        0x8,
        (
            "#3309F#5Pうふふ、レンはそこまで\x01",
            "自信過剰じゃないわ。\x02\x03",

            "#3300Fレンに見えるのは\x01",
            "絡まり合った因果#4Rシステム#だけ。\x02\x03",

            "お互い別々に作動する因果が\x01",
            "このクロスベルという場で\x01",
            "どんな織物を編み上げるのか……\x02\x03",

            "#3304Fそれが見えるというだけよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0007
    AnonymousTalk(
        0x9,
        (
            "ふむ……なるほどな。\x02\x03",

            "マフィアと例の教団が\x01",
            "何をするつもりかは知らんが\x01",
            "少々、騒がしくなりそうだの。\x02\x03",

            "まあ、これも自業自得──\x01",
            "いや因果応報というものか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0008
    ChrTalk(
        0x8,
        (
            "#3306F#5Pええ、あの灰色の街が\x01",
            "積み重ねてきた因果の報いと\x01",
            "言うべきかもしれないわね。\x02\x03",

            "#3300F──てっきり《結社》の関与も\x01",
            "あるかと思っていたのだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x9,
        (
            "#3903F#11Pこの地は《結社》と《教会》の\x01",
            "緩衝地帯にもなっておるからな。\x02\x03",

            "法王は騎士の活動を禁じ、\x01",
            "盟主は執行者を派遣しない。\x02\x03",

            "#3900Fま、あくまで建前としてはだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "#3309F#5Pうふふ、おじいさんの工房が\x01",
            "ある時点で怪しいものだけど……\x02\x03",

            "#3302Fまさかクロスベルの導力ネットに\x01",
            "介入できる遠隔システムまで\x01",
            "用意してるとは思わなかったわ。\x02\x03",

            "おかげでレンも\x01",
            "退屈しなくて済んでるけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x9,
        (
            "#3903F#11Pお前さんの役に立ったのなら\x01",
            "用意した甲斐があったというものだ。\x02\x03",

            "#3901Fあやつが押し付けてきた時には\x01",
            "ブチ壊してくれようと思ったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "#3302F#5Pクスクス……\x01",
            "相変わらず“博士”と仲が悪いのね。\x02\x03",

            "#3304F《十三工房》の管理者にして\x01",
            "使徒第六柱──ノバルティス博士。\x02\x03",

            "#3300F《星辰》のネットワークがあるのに\x01",
            "今さらエプスタインの試験運用に\x01",
            "何の興味があるのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x9,
        (
            "#3901F#11Pフン、あやつのことだ。\x02\x03",

            "どうせロクでもない企みのために\x01",
            "役立てようと思っとるのだろう。\x02\x03",

            "#3903Fまったく、開発途中の実験作を\x01",
            "適当にバラまきおって……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "#3304F#5Pうふふ、お兄さんたちが戦った\x01",
            "あの紅い武者さんね。\x02\x03",

            "#3300Fモニターで見た限りでは\x01",
            "なかなか優秀な子みたいだけど？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x9,
        (
            "#3903F#11Pやはり自律的な状況判断と\x01",
            "柔軟な行動選択に難アリだな。\x02\x03",

            "#3900Fなかなかお前さんの\x01",
            "“相棒”のようにはいかんさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "#3304F#5Pふふっ……\x02\x03",

            "#3305Fでも、レンがここにいるのは\x01",
            "博士も気付いてるんでしょう？\x02\x03",

            "レンはともかく彼について\x01",
            "何も言ってこないのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        (
            "#3903F#11P今のところはダンマリだな。\x02\x03",

            "どうやら新しい機体の開発に\x01",
            "熱中しておるようだが……\x02\x03",

            "#3900F──まあ、課題だった姿勢制御と\x01",
            "関節部分の構造強化も完了した。\x02\x03",

            "あやつに余計な口を\x01",
            "挟ませるスキは見せんさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "#3304F#5Pうふふ、ありがとう。\x02\x03",

            "#3308Fこれでやっと……\x01",
            "最後の賭けが始められるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x9,
        "#3900F#11P……ふむ………\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x9)
    Fade(250)
    EndChrThread(0x8, 0x0)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x10)
    SetChrChipByIndex(0x8, 0x21)
    SetChrSubChip(0x8, 0x1)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x8, 0x11)
    Sleep(300)

    #C0020
    ChrTalk(
        0x8,
        (
            "#3300F#5Pふふっ、そんな顔をしないで。\x02\x03",

            "人形繰りを教えてくれたり\x01",
            "偽者の人形さんを作ってくれたり\x01",
            "こうして匿#2Rかくま#ってくれたり……\x02\x03",

            "#3304Fおじいさんには感謝してるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x9,
        (
            "#3903F#11Pなに、大した事はしておらんさ。\x02\x03",

            "#3900Fそれよりも──\x01",
            "今日は忙しくなるのだろう？\x02\x03",

            "少々早めだが\x01",
            "午後のティータイムとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        "#3309F#5Pうふふ、そうね。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x87, 0x12C)
    Sleep(100)
    Fade(1000)
    OP_68(4730, 4900, -140, 7000)
    MoveCamera(69, 15, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(13000, 7000)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)

    #C0023
    ChrTalk(
        0x8,
        (
            "#3300F《パテル＝マテル》──\x01",
            "一緒にお茶にしましょう。\x02\x03",

            "#3304F今日は長い一日になるわ。\x02\x03",

            "#3302Fたぶん、この自治州が始まって\x01",
            "いちばん長い一日にね。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_87(0x0, 0xFF, 0x1, "pm_head:Layer1(4)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(300)
    Sound(943, 0, 100, 0)
    Sleep(1500)
    FadeToDark(3000, 0, -1)
    SetCameraDistance(12000, 4000)
    OP_0D()
    StopBGM(0x1388)
    WaitBGM()
    OP_E3(0xA)
    Sleep(1000)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_57(0x3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_E3(0xB)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x5C, 0)
    NewScene("c1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_109 end

    def Function_3_116D(): pass

    label("Function_3_116D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11BC")
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    Sleep(1000)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    Sleep(1000)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    OP_A1(0xFE, 0xBB8, 0x3, 0x0, 0x1, 0x2)
    Sleep(1000)
    Jump("Function_3_116D")

    label("loc_11BC")

    Return()

    # Function_3_116D end

    SaveToFile()

Try(main)
