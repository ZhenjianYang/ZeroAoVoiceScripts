from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t113b.bin",                # FileName
        "t113b",                    # MapName
        "t113b",                    # Location
        0x0049,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 73, 0, 0, 0, 1],
    )

    BuildStringList((
        "t113b",                  # 0
        "キーア",                 # 1
        "フラン",                 # 2
        "セシル",                 # 3
        "イリア",                 # 4
        "リーシャ",               # 5
        "シュリ",                 # 6
        "マリアベル",             # 7
        "ディーター市長",         # 8
        "エリィ",                 # 9
        "ティオ",                 # 10
        "ランディ",               # 11
        "ノエル",                 # 12
        "ワジ",                   # 13
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(524, 0)                                        # 0

    ScpFunction((
        "Function_0_20C",          # 00, 0
        "Function_1_21C",          # 01, 1
        "Function_2_21D",          # 02, 2
    ))


    def Function_0_20C(): pass

    label("Function_0_20C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_21B")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_21B")

    Return()

    # Function_0_20C end

    def Function_1_21C(): pass

    label("Function_1_21C")

    Return()

    # Function_1_21C end

    def Function_2_21D(): pass

    label("Function_2_21D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 2)), scpexpr(EXPR_END)), "loc_23A")
    RemoveParty(0x1, 0xFF)
    Jump("loc_279")

    label("loc_23A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 3)), scpexpr(EXPR_END)), "loc_24B")
    RemoveParty(0x2, 0xFF)
    Jump("loc_279")

    label("loc_24B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 4)), scpexpr(EXPR_END)), "loc_25C")
    RemoveParty(0x3, 0xFF)
    Jump("loc_279")

    label("loc_25C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 5)), scpexpr(EXPR_END)), "loc_26D")
    RemoveParty(0x8, 0xFF)
    Jump("loc_279")

    label("loc_26D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x147, 6)), scpexpr(EXPR_END)), "loc_279")
    RemoveParty(0x4, 0xFF)

    label("loc_279")

    LoadChrToIndex("chr/ch08202.itc", 0x1E)
    LoadChrToIndex("chr/ch08502.itc", 0x1F)
    LoadChrToIndex("chr/ch05202.itc", 0x20)
    LoadChrToIndex("chr/ch05102.itc", 0x21)
    LoadChrToIndex("chr/ch07502.itc", 0x22)
    LoadChrToIndex("chr/ch10002.itc", 0x23)
    LoadChrToIndex("chr/ch05502.itc", 0x24)
    LoadChrToIndex("chr/ch05602.itc", 0x25)
    LoadChrToIndex("chr/ch00102.itc", 0x26)
    LoadChrToIndex("chr/ch00202.itc", 0x27)
    LoadChrToIndex("chr/ch00302.itc", 0x28)
    LoadChrToIndex("chr/ch02902.itc", 0x29)
    LoadChrToIndex("chr/ch03002.itc", 0x2A)
    LoadChrToIndex("chr/ch00002.itc", 0x2B)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02800.itp")
    OP_68(2100, 3100, -8280, 0)
    MoveCamera(28, 11, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(26140, 0)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x1)
    SetChrPos(0x101, -2000, 180, -4900, 90)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x1)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -2000, 180, -8900, 90)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x2)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 2000, 180, -16900, 270)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x2)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 2000, 180, -8900, 270)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x2)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 2000, 180, -6900, 270)
    SetChrChipByIndex(0xA, 0x22)
    SetChrSubChip(0xA, 0x2)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 2000, 180, -12900, 270)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x2)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 2000, 180, -10900, 270)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x2)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 2000, 180, -4900, 270)
    SetChrChipByIndex(0xF, 0x25)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 0, 180, -1500, 180)
    SetChrChipByIndex(0x10, 0x26)
    SetChrSubChip(0x10, 0x1)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -2000, 180, -6900, 90)
    SetChrChipByIndex(0x11, 0x27)
    SetChrSubChip(0x11, 0x1)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -2000, 180, -10900, 90)
    SetChrChipByIndex(0x12, 0x28)
    SetChrSubChip(0x12, 0x1)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -2000, 180, -12900, 90)
    SetChrChipByIndex(0x13, 0x29)
    SetChrSubChip(0x13, 0x2)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 2000, 180, -14900, 270)
    SetChrChipByIndex(0x14, 0x2A)
    SetChrSubChip(0x14, 0x1)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -2000, 180, -14900, 90)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "やがてロイドたちは全員、\x01",
            "迎賓館の《饗応#4Rきょうおう#の間》に集まり……\x02\x03",

            "程なくしてディーター市長と\x01",
            "娘のマリアベルも到着した。\x02\x03",

            "そして、到着が遅れたのを詫びる\x01",
            "ディーター市長の挨拶を合図に……\x02\x03",

            "豪華ながらも居心地のいい\x01",
            "晩餐会が始まるのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7162", 0)
    OP_68(2100, 1100, -8280, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    MoveCamera(32, 11, 0, 100000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0002
    AnonymousTalk(
        0xF,
        (
            "いやいや、本当に\x01",
            "遅れて申しわけなかった。\x02\x03",

            "招待した側が遅れるなど\x01",
            "本来あってはならないんだが。\x02",
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

    #C0003
    ChrTalk(
        0x101,
        (
            "#00004F#6Pいえ、市長がお忙しいのは\x01",
            "さすがに分かっていますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x11,
        "#00202F#6Pどうもお疲れさまです。\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xE,
        (
            "#02904F#11Pまあ、お父様の場合、\x01",
            "忙しいのは自業自得ですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xF,
        (
            "#02809F#5Pハッハッハッ。\x01",
            "まあその通りなんだがね。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x10,
        "#00106F#6Pもう、ベルったら……\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xB,
        (
            "#01703F#11Pしかし練習と公演ばかりで\x01",
            "詳しくは知らないんですけど……\x02\x03",

            "#01700Fまたずいぶん思い切った\x01",
            "提案をなさったみたいね？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xF,
        (
            "#02804F#5Pハハ、実は就任当初から\x01",
            "考えていたアイデアでね。\x02\x03",

            "本当はあのタイミングで\x01",
            "出すつもりはなかったが……\x01",
            "そうも言ってられなくなった。\x02\x03",

            "#02800Fなので思い切って\x01",
            "サイを投げさせてもらったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xB,
        (
            "#01704F#11Pフフ、なるほど。\x02\x03",

            "#01702Fそして幕が上がったステージは\x01",
            "最後まで踊り続ける必要がある……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xF,
        (
            "#02803F#5Pその通り。\x02\x03",

            "#02800F聞けばアルカンシェルは\x01",
            "『金の太陽、銀の月』の\x01",
            "リニューアルに挑戦するとか。\x02\x03",

            "実は、その初公演の翌週に\x01",
            "国家独立の是非を問う住民投票を\x01",
            "実施することが決定してね。\x02\x03",

            "#02804Fそれで、これも縁かと思い、\x01",
            "招待させていただいた次第だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        "#00005F#6Pそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xB,
        (
            "#01709F#11Pふふっ、おかげさまで\x01",
            "楽しい休暇が過ごせたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xC,
        "#01804F#11Pどうも有難うございます。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xD,
        "#04203F#11P……ども。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xA,
        (
            "#05902F#11Pふふ、私は部外者なので\x01",
            "申し訳ないくらいですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xF,
        (
            "#02805F#5Pいやいや、とんでもない。\x02\x03",

            "#02800Fウルスラ病院の関係者から\x01",
            "貴女の噂は常々聞いている。\x02\x03",

            "何でも聖女ウルスラの再来と\x01",
            "言われるくらいの働き者だとか。\x02\x03",

            "#02809Fお会いできて光栄だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xA,
        (
            "#05905F#11Pさ、さすがにそれは\x01",
            "大げさかと思いますけど……\x02\x03",

            "#05904Fそう言って頂けると光栄です。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xE,
        (
            "#02906F#11Pもう、お父さまったら。\x01",
            "先ほどから妙齢の女性ばかり\x01",
            "誉めそやして……\x02\x03",

            "#02900F少しはロイドさんたちも\x01",
            "労#2Rねぎら#ってはいかがですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xF,
        (
            "#02805F#5Pおっと、これは失礼。\x02\x03",

            "#02809Fいやはや、美しいお嬢さんばかりで\x01",
            "年甲斐もなく舞い上がっているようだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        "#00012F#6Pはは……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x12,
        (
            "#00309F#6Pま、でも招待してくれて\x01",
            "本当に有り難かったッスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x14,
        (
            "#10304F#6P#Nそうだね。\x01",
            "いい気分転換になったし。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0024
    ChrTalk(
        0x13,
        "#10109F#11P市長、有難うございました。\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x9,
        "#06409F#11Pすっごく楽しかったです！\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        "#01109F#6Pキーアも楽しかったー。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xF,
        "#02804F#5Pはは、それは何よりだ。\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xF)

    #C0028
    ChrTalk(
        0xF,
        (
            "#02803F#5P──蒸し返すようで悪いが\x01",
            "あれは本当に不幸な事件だった。\x02\x03",

            "#02801Fいくらタワーの爆破まで\x01",
            "しようとした犯罪者#6Rテロリスト#とはいえ……\x02\x03",

            "あんな形で命を\x01",
            "落とさなくてはならないほど\x01",
            "罪深かったとは思えない。\x02\x03",

            "#02803F二度と、あんな事件が\x01",
            "起きないよう尽力するつもりだ。\x02\x03",

            "#02800Fこの世に《正義》が実在すると\x01",
            "皆に信じてもらうためにもね。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x13,
        "#10108F#11Pあ……\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#00008F#6Pディーター市長……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x10,
        (
            "#00104F#6P……そう言っていただけると\x01",
            "胸のつかえが取れた気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x11,
        (
            "#00203F#6Pしかし、その独立の是非を問う\x01",
            "住民投票ですが……\x02\x03",

            "#00200Fもし賛成が上回った場合、\x01",
            "本当に独立できるものなんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xF,
        (
            "#02806F#5Pいや、住民投票自体に\x01",
            "独立を可能にする決定力はない。\x02\x03",

            "#02804Fただ、その結果は必ずや\x01",
            "諸外国への意思表示となるはずだ。\x02\x03",

            "そうして徐々に国際世論を形成し、\x01",
            "２大国から何とかして\x01",
            "『独立』をもぎ取っていく……\x02\x03",

            "#02800Fそれが私のシナリオだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x12,
        "#00303F#6Pなるほどねぇ……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x14,
        (
            "#10302F#6P#Nこう言っちゃなんだけど\x01",
            "相当、険しい道のりだよね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0036
    ChrTalk(
        0x13,
        "#10101F#11Pワ、ワジ君……！\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xF,
        (
            "#02803F#5Pいや、君の指摘通りだ。\x02\x03",

            "#02801F地政学的な観点から言っても\x01",
            "クロスベルの国家独立というのは\x01",
            "かなり困難な状況にある……\x02\x03",

            "#02800Fだが、人間というのは\x01",
            "ただ情勢に流されるだけの\x01",
            "生き物ではないと思うのだ。\x02\x03",

            "苦境にあっても理想を追求し、\x01",
            "誇り高くあらんと指向する……\x02\x03",

            "#02804Fそんな力と可能性を\x01",
            "秘めているように思えるのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x10,
        "#00102F#6P……おじさま……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#00003F#6P誇り高くあるための\x01",
            "力と可能性、ですか……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xC,
        "#01808F#11P…………………………\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xB,
        "#01704F#11Pふむ……なるほどね。\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xF,
        (
            "#02803F#5P今後、クロスベルが歩く道は\x01",
            "困難なものになるだろう……\x02\x03",

            "むろん我々大人たちは\x01",
            "粉骨砕身の覚悟と努力で\x01",
            "その道を切り拓くつもりだ。\x02\x03",

            "#02800Fだが、それに続いて\x01",
            "高みを目指していくのは\x01",
            "君たち若者の役目だと思うのだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0043
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ディーター市長は席を見渡して\x01",
            "深々と頭を下げた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    #C0044
    ChrTalk(
        0xF,
        (
            "#02804F#5Pどうか君たちも──\x01",
            "君たちならではのやり方で\x01",
            "クロスベルの明日に尽くして欲しい。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2100, 1350, -8280, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、晩餐会が終わり、\x01",
            "ホテルの３Ｆまで戻った後……\x02\x03",

            "不思議な高揚感に包まれながらも\x01",
            "遊び疲れていたロイドたちは\x01",
            "それぞれ早めに休むことにした。\x02\x03",

            "そして──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x22, 1)
    NewScene("e430B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_21D end

    SaveToFile()

Try(main)
