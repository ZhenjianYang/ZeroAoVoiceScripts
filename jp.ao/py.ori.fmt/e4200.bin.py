from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4200.bin",                # FileName
        "e4200",                    # MapName
        "e4200",                    # Location
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
        "e4200",                  # 0
        "神狼ツァイト",           # 1
        "神狼ツァイト",           # 2
        "ロイド",                 # 3
        "ロイド",                 # 4
        "SE制御",                 # 5
    ))

    DeclNpc(0,       0,       0,       0,    228,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(20500,   4500,    0,       0,    228,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(15500,   5500,    0,       0,    228,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(16000,   4949,    0,       0,    228,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(328, 0)                                        # 0

    ScpFunction((
        "Function_0_148",          # 00, 0
        "Function_1_158",          # 01, 1
        "Function_2_16D",          # 02, 2
        "Function_3_1FC8",         # 03, 3
        "Function_4_203F",         # 04, 4
        "Function_5_2073",         # 05, 5
        "Function_6_209B",         # 06, 6
        "Function_7_20C3",         # 07, 7
        "Function_8_20E0",         # 08, 8
        "Function_9_20F6",         # 09, 9
    ))


    def Function_0_148(): pass

    label("Function_0_148")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_157")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_157")

    Return()

    # Function_0_148 end

    def Function_1_158(): pass

    label("Function_1_158")

    OP_F0(0x1, 0x4B0)
    OP_11(0x7B, 0xB4, 0xD5, 0xA, 0x190, 0x0)
    Return()

    # Function_1_158 end

    def Function_2_16D(): pass

    label("Function_2_16D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51620.itc", 0x20)
    SoundLoad(132)
    SoundLoad(962)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x0, 0x8)
    OP_49()
    SetChrPos(0x8, 16000, 0, 0, 0)
    OP_D5(0x8, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x32, 0x1, 0x20)
    SetChrFlags(0x8, 0x1)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x206C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x0, 0x97, 0xAA, 0x1, 0x20)
    OP_D3(0x101, 0x0, "Null_senaka(42)")
    SetMapObjFrame(0x0, "879mabuta:Layer1(43)", 0x0, 0x1)
    SetMapObjFrame(0x0, "879mabuta:Layer2(44)", 0x0, 0x1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x101, 0x80)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    OP_52(0x101, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x8C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x101, 0x1)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x1000)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x20)
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xC, 1, 0, 3)
    BeginChrThread(0xC, 2, 0, 4)
    Sleep(4000)
    PlayBGM("ed7304", 0)
    OP_68(32000, 5000, 0, 0)
    MoveCamera(330, 5, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(69420, 0)
    FadeToBright(1000, 0)
    OP_68(17500, 5800, 0, 6000)
    MoveCamera(320, 18, 0, 6000)
    OP_6E(500, 6000)
    SetCameraDistance(18500, 6000)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xC, 0x2)
    OP_68(17550, 6100, 0, 30000)
    MoveCamera(326, 3, 0, 30000)
    OP_6E(500, 30000)
    SetCameraDistance(15500, 30000)
    Sleep(500)

    #C0001
    ChrTalk(
        0xA,
        "#00011F#5P女神が遣#2Rつか#わした聖獣……？\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11Pうむ、そのような存在#4Rも の#と\x01",
            "考えてもらうのが早いだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11Pかつて女神から人に贈られた、\x01",
            "大いなる《七の至宝#8Rセプト＝テリオン#》……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11Pそれらの行く末を見守るために\x01",
            "在り続けているのが我らだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xA,
        (
            "#00003F#5P“我ら”ってことは……\x02\x03",

            "#00001Fひょっとしてリベールの異変で\x01",
            "現れたっていう“竜”も……？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11Pフム、さすがに聡#2Rさと#いな。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11Pかの竜レグナートも\x01",
            "確かに私の同胞#4Rはらから#だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P《空の至宝》を見守るため\x01",
            "リベールの地に残っていたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P“使命”から解かれた今は\x01",
            "どこに消えたか私にも判らぬ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xA,
        (
            "#00006F#5Pな、何がなんだか……\x02\x03",

            "#00008Fでもそれじゃあ、ツァイトも\x01",
            "大昔からクロスベルの地に……？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11Pうむ、１２００年前の\x01",
            "《大崩壊》の前からになるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11Pかつて《幻の至宝》が\x01",
            "どうして消えてしまったか……\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11Pその後、至宝を再現するため\x01",
            "どのような事が行われたか……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11Pある程度のことは識#2Rし#っている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(17150, 6100, 0, 0)
    MoveCamera(313, 3, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(12500, 0)
    Fade(500)
    OP_0D()
    BeginChrThread(0x101, 1, 0, 8)
    WaitChrThread(0x101, 1)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)
    Sleep(500)

    #C0015
    ChrTalk(
        0xA,
        (
            "#00006F#5P……正直、調べようにも\x01",
            "調べきれない部分だったんだ。\x02\x03",

            "#00008F女神の至宝……\x01",
            "それを受け継いだクロイス家……\x02\x03",

            "どうして至宝は失われ、\x01",
            "キーアがあんな役割を\x01",
            "背負わされる事になったのか……\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)

    #C0016
    ChrTalk(
        0xA,
        (
            "#00001F#5P──頼む。\x01",
            "どうか教えて欲しい。\x02\x03",

            "１２００年前の出来事を。\x02\x03",

            "そして５００年前、\x01",
            "キーアに何が起こったのかを。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(18000, 5500, 0, 2500)
    MoveCamera(310, 3, 0, 2500)
    OP_6E(500, 2500)
    SetCameraDistance(11000, 2500)
    Sleep(1000)

    #C0017
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P──よかろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11Pまあ、そのために私は\x01",
            "おぬしの前に現れたのでな。\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    Sleep(300)
    SetMapObjFrame(0x0, "879mabuta:Layer1(43)", 0x1, 0x1)
    SetMapObjFrame(0x0, "879mabuta:Layer2(44)", 0x1, 0x1)
    StopBGM(0x1770)
    StopSound(132, 4000, 100)
    StopSound(962, 4000, 60)
    Sleep(800)

    #C0019
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11Pこの地に伝わった女神の至宝……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11Pそれは“幻”を司る\x01",
            "《虚なる神#8Rデ ミ ウ ル ゴ ス#》と呼ばれた。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7573", 0)
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0021
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P“幻”は知覚と認識を司り、\x01",
            "更には《因果》をも御する属性だ。\x02\x03",

            "その力を秘めた至宝に、\x01",
            "当時のクロイス家を中心とした\x01",
            "人間の一派が望んだこと……\x02\x03",

            "それは女神#4Rエイドス#の代わり……\x01",
            "地上の《神》としての役割だった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis272.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(0, 170, -1, -1)

    #A0022
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P人を識#2Rし#り、地上の全てを識#2Rし#り、\x01",
            "因果を御することで人間を導く……\x02\x03",

            "それは一見、人の欲望を無制限に\x01",
            "叶えてしまった《空の至宝#8Rオ ー リ オ ー ル#》にも\x01",
            "通じるところがあっただろう。\x02\x03",

            "だが、《幻の至宝#8Rデ ミ ウ ル ゴ ス#》は……\x01",
            "高位の人格を与えられることで\x01",
            "同じ過ちを起こさずに済んだ。\x02\x03",

            "あくまで人を堕落させず、\x01",
            "正しく導ける叡智と判断力……\x02\x03",

            "それをもって、人という存在を\x01",
            "正しく導けるはずだったのだ。\x02\x03",

            "──至宝そのものの“心”が\x01",
            "限界に達しさえしなければ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFF000000, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis273.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(250, 160, -1, -1)

    #A0023
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11Pあらゆる人の性#2Rさが#と業#2Rごう#、\x01",
            "あらゆる世界の不条理──\x02\x03",

            "それを理解し導けるということは\x01",
            "人と同じ“情”を持つという事だ。\x02\x03",

            "そして《幻の至宝#8Rデ ミ ウ ル ゴ ス#》の“心”は\x01",
            "次第に壊れ、病んでいった。\x02\x03",

            "このままだといずれ暴走し、\x01",
            "守るべき人々を傷つけてしまう……\x02\x03",

            "そう悟った至宝は──\x01",
            "“悩んだ”末に一つの決断をした。\x02\x03",

            "自分#4R㈲　㈲#という存在の因果を解き、\x01",
            "この世から消滅させる#20R㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲#という道を。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_68(16500, 5800, 0, 0)
    MoveCamera(322, 6, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16000, 0)
    Sound(223, 0, 60, 0)
    Sound(934, 0, 70, 0)
    FadeToDark(0, 16777215, -1)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x7D0, 0x0, 0x0)
    Sleep(1000)
    Sound(934, 0, 40, 0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(700)
    Sound(132, 2, 100, 0)
    Sound(962, 2, 60, 0)
    Sleep(300)
    FadeToBright(1500, 16777215)
    OP_0D()
    SetMapObjFrame(0x0, "879mabuta:Layer1(43)", 0x0, 0x1)
    SetMapObjFrame(0x0, "879mabuta:Layer2(44)", 0x0, 0x1)
    Sleep(300)

    #C0024
    ChrTalk(
        0xA,
        (
            "#00006F#5P……そんな事が……\x02\x03",

            "#00013Fでも、それじゃあ\x01",
            "後に残された人々は……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11Pうむ──至宝の消滅に\x01",
            "ひたすら惑い、嘆き、恐れた。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11Pそして、何故そうなったのか、\x01",
            "至宝が何を思ってそうしたのかを\x01",
            "省みることなく……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P失われた至宝と同等の存在#4Rも の#を\x01",
            "生み出すことに取り憑かれたのだ。\x02",
        )
    )

    CloseMessageWindow()
    StopSound(132, 1500, 100)
    StopSound(962, 1500, 60)
    FadeToDark(1500, 0, -1)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0028
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P──もちろん最初は\x01",
            "ただの手探りだっただろう。\x02\x03",

            "しかし７００年に渡り、\x01",
            "彼らは様々な知識を集めながら\x01",
            "独自の技術を編み出していった。\x02\x03",

            "すなわち無から有を生み出すという\x01",
            "《錬金術》という魔導技術を。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis274.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(0, 170, -1, -1)

    #A0029
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11Pそして彼らは、この地で\x01",
            "途方もなく遠大な計画を立てた。\x02\x03",

            "《教団》という傀儡を用意し、\x01",
            "新たな至宝の“核”となる存在を\x01",
            "委ねて育てさせること……\x02\x03",

            "そして『錬成』という概念を\x01",
            "極限まで応用した巨大な“式”を\x01",
            "この地に用意すること……\x02\x03",

            "それが数百年前──\x01",
            "クロイス家の錬金術師たちが\x01",
            "始めた計画だったのだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFF000000, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x0, "c_vis275.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(180, 170, -1, -1)

    #A0030
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11Pそれを資金的に可能にするため、\x01",
            "彼らは『銀行家』という表の仮面を\x01",
            "被り始めることとなり……\x02\x03",

            "一方、《教団》の方は\x01",
            "信仰対象として与えられた“核”を\x01",
            "目覚めさせるべく蠢き始めた。\x02\x03",

            "そして５００年の時が過ぎ──\x01",
            "今の状況へと至ったという訳だ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFF000000, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_68(17150, 6100, 0, 0)
    MoveCamera(315, 3, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(12500, 0)
    Sound(132, 2, 100, 0)
    Sound(962, 2, 60, 0)
    SetChrSubChip(0x101, 0x2)
    FadeToBright(1500, 0)
    OP_0D()
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)

    #C0031
    ChrTalk(
        0xA,
        (
            "#00006F#5P……途方もない話だな。\x02\x03",

            "#00008Fでもやっと……事件の全貌が\x01",
            "見え始めてきた気がする。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 1, 0, 9)
    WaitChrThread(0x101, 1)
    OP_68(17500, 5800, 0, 2500)

    #C0032
    ChrTalk(
        0xA,
        (
            "#00003F#5P──ツァイト。\x01",
            "マリアベルさんはキーアを\x01",
            "《零#2Rゼロ#の至宝》と言っていた。\x02\x03",

            "#00013Fそれはどういう意味だ？\x02\x03",

            "失われた《幻の至宝》とは\x01",
            "また違うものなのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P残念ながら……\x01",
            "私もそれについては判らない。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P恐らくクロイス家は、\x01",
            "１２００年に渡る妄執の果てに\x01",
            "“何か”を掴んだのだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11Pそれによって\x01",
            "《幻の至宝#8Rデ ミ ウ ル ゴ ス#》と同等の存在を\x01",
            "再現するだけではなく……\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11Pそれを超える力を持った\x01",
            "《零の至宝》を完成させたようだ。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 1, 0, 5)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis276.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(0, 160, -1, -1)

    #A0037
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P──あの白き人形#4Rヒトガタ#の力。\x02\x03",

            "あれは人形そのもの力ではなく、\x01",
            "《至宝》の力と見るべきだろう。\x02",
        )
    )

    CloseMessageWindow()
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis277.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(300)
    SetMessageWindowPos(0, 150, -1, -1)

    #A0038
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11Pそして、《幻の至宝》には\x01",
            "あれだけの事を瞬時にやれるほどの\x01",
            "力までは備わっていなかった。\x02",
        )
    )

    CloseMessageWindow()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis278.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(300)
    SetMessageWindowPos(0, 150, -1, -1)

    #A0039
    AnonymousTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P空間を消滅させる力は\x01",
            "どちらかというと“空”の属性に\x01",
            "由来するものだからな。\x02\x03",

            "あれが全てでないとすると……\x01",
            "どれだけの潜在能力を持つのか\x01",
            "私にも想像が付かないくらいだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xC, 2, 0, 6)
    OP_68(17150, 6100, 0, 0)
    MoveCamera(315, 3, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(12500, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(300)

    #C0040
    ChrTalk(
        0xA,
        (
            "#00008F#5P……そうか……\x02\x03",

            "#00003F…………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xB)
    Sleep(500)

    #C0041
    ChrTalk(
        0xA,
        (
            "#00006F#5P──もう一つ教えてくれ。\x02\x03",

            "#00008F今までの話を聞いた限り、\x01",
            "あの子は……\x02\x03",

            "#00001F……キーアは……\x01",
            "普通の人間じゃないんだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P…………うむ。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P人にして人あらざるもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P《至宝》を再現するための\x01",
            "“核”として創られた存在──\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P恐らく錬金術の奥義をもって\x01",
            "錬成された《人造生命#8Rホ ム ン ク ル ス#》だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xA,
        "#00008F#30W#5P………………………………\x02",
    )

    CloseMessageWindow()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis279.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis280.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(300)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis281.itp")
    OP_CB(0x0, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x1, 0x0)
    Sleep(300)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis282.itp")
    OP_CB(0x1, 0x4, 0x0, 0x0, 0x0, 0x0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    OP_CC(0x1, 0x0, 0x0)
    Sleep(300)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x3E8, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(300)
    BeginChrThread(0x101, 1, 0, 8)
    WaitChrThread(0x101, 1)
    Sleep(300)

    #C0047
    ChrTalk(
        0xA,
        (
            "#00006F#5P#30W（多分……しばらく前から\x01",
            "  知っていたんだな……）\x02\x03",

            "（なのに俺たちの前では\x01",
            "  あんな風に笑って……）\x02\x03",

            "#00008F（…………キーア……………）\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 2, 0, 7)
    MoveCamera(30, 5, 0, 6000)
    OP_6E(500, 6000)
    SetCameraDistance(52000, 6000)
    Sleep(1000)
    OP_68(12000, 5000, 0, 5000)
    StopBGM(0x1770)
    Sleep(2000)
    StopSound(132, 4000, 100)
    StopSound(962, 4000, 60)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    EndChrThread(0xC, 0x1)
    EndChrThread(0xC, 0x2)
    SetScenarioFlags(0x22, 0)
    NewScene("e4100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_16D end

    def Function_3_1FC8(): pass

    label("Function_3_1FC8")

    Sound(132, 2, 20, 0)
    Sleep(200)
    OP_25(0x84, 0x19)
    Sleep(200)
    OP_25(0x84, 0x1E)
    Sleep(200)
    OP_25(0x84, 0x23)
    Sleep(200)
    OP_25(0x84, 0x28)
    Sleep(200)
    OP_25(0x84, 0x2D)
    Sleep(200)
    OP_25(0x84, 0x32)
    Sleep(200)
    OP_25(0x84, 0x37)
    Sleep(200)
    OP_25(0x84, 0x3C)
    Sleep(200)
    OP_25(0x84, 0x41)
    Sleep(200)
    OP_25(0x84, 0x46)
    Sleep(2000)
    OP_25(0x84, 0x4B)
    Sleep(200)
    OP_25(0x84, 0x50)
    Sleep(200)
    OP_25(0x84, 0x55)
    Sleep(200)
    OP_25(0x84, 0x5A)
    Sleep(200)
    OP_25(0x84, 0x5F)
    Sleep(200)
    OP_25(0x84, 0x64)
    Return()

    # Function_3_1FC8 end

    def Function_4_203F(): pass

    label("Function_4_203F")

    Sleep(200)
    Sound(962, 2, 30, 0)
    Sleep(2000)
    OP_25(0x3C2, 0x23)
    Sleep(400)
    OP_25(0x3C2, 0x28)
    Sleep(400)
    OP_25(0x3C2, 0x2D)
    Sleep(400)
    OP_25(0x3C2, 0x32)
    Sleep(400)
    OP_25(0x3C2, 0x37)
    Sleep(400)
    OP_25(0x3C2, 0x3C)
    Return()

    # Function_4_203F end

    def Function_5_2073(): pass

    label("Function_5_2073")

    OP_25(0x3C2, 0x37)
    Sleep(100)
    OP_25(0x3C2, 0x32)
    Sleep(100)
    OP_25(0x3C2, 0x2D)
    Sleep(100)
    OP_25(0x3C2, 0x28)
    Sleep(100)
    OP_25(0x3C2, 0x23)
    Sleep(100)
    OP_25(0x3C2, 0x1E)
    Return()

    # Function_5_2073 end

    def Function_6_209B(): pass

    label("Function_6_209B")

    OP_25(0x3C2, 0x23)
    Sleep(100)
    OP_25(0x3C2, 0x28)
    Sleep(100)
    OP_25(0x3C2, 0x2D)
    Sleep(100)
    OP_25(0x3C2, 0x32)
    Sleep(100)
    OP_25(0x3C2, 0x37)
    Sleep(100)
    OP_25(0x3C2, 0x3C)
    Return()

    # Function_6_209B end

    def Function_7_20C3(): pass

    label("Function_7_20C3")

    SetChrSubChip(0x101, 0x1)
    Sleep(150)
    SetChrSubChip(0x101, 0x0)
    Sleep(850)
    SetChrSubChip(0x101, 0x4)
    Sleep(1500)
    SetChrSubChip(0x101, 0x5)
    Sleep(1000)
    Return()

    # Function_7_20C3 end

    def Function_8_20E0(): pass

    label("Function_8_20E0")

    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(150)
    SetChrSubChip(0x101, 0x2)
    Sleep(200)
    Return()

    # Function_8_20E0 end

    def Function_9_20F6(): pass

    label("Function_9_20F6")

    SetChrSubChip(0x101, 0x2)
    Sleep(100)
    SetChrSubChip(0x101, 0x1)
    Sleep(150)
    SetChrSubChip(0x101, 0x0)
    Sleep(200)
    Return()

    # Function_9_20F6 end

    SaveToFile()

Try(main)
