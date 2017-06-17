from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e0111.bin",                # FileName
        "e0111",                    # MapName
        "e0111",                    # Location
        0x0001,                     # MapIndex
        "ed7516",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "e0111",                  # 0
        "ツァイト",               # 1
        "ディーター総裁",         # 2
        "マリアベル",             # 3
        "セルゲイ課長",           # 4
        "SE制御",                 # 5
    ))

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_1C4",          # 00, 0
        "Function_1_27C",          # 01, 1
        "Function_2_2A0",          # 02, 2
        "Function_3_2A1",          # 03, 3
        "Function_4_DC6",          # 04, 4
        "Function_5_DEB",          # 05, 5
        "Function_6_E10",          # 06, 6
        "Function_7_E41",          # 07, 7
        "Function_8_1DCC",         # 08, 8
        "Function_9_1E24",         # 09, 9
        "Function_10_2010",        # 0A, 10
    ))


    def Function_0_1C4(): pass

    label("Function_0_1C4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_204"),
        (1, "loc_210"),
        (2, "loc_21C"),
        (3, "loc_228"),
        (4, "loc_234"),
        (5, "loc_240"),
        (6, "loc_24C"),
        (SWITCH_DEFAULT, "loc_258"),
    )


    label("loc_204")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_210")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_21C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_228")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_234")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_240")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_24C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_258")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_264")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_27B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_264")

    label("loc_27B")

    Return()

    # Function_0_1C4 end

    def Function_1_27C(): pass

    label("Function_1_27C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_290")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 3)
    Jump("loc_29F")

    label("loc_290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_29F")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 7)

    label("loc_29F")

    Return()

    # Function_1_27C end

    def Function_2_2A0(): pass

    label("Function_2_2A0")

    Return()

    # Function_2_2A0 end

    def Function_3_2A1(): pass

    label("Function_3_2A1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02708.itc", 0x1E)
    LoadChrToIndex("apl/ch50511.itc", 0x1F)
    LoadChrToIndex("chr/ch05502.itc", 0x20)
    LoadChrToIndex("chr/ch00002.itc", 0x21)
    LoadChrToIndex("chr/ch00102.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    LoadChrToIndex("chr/ch00302.itc", 0x24)
    LoadChrToIndex("chr/ch08202.itc", 0x25)
    LoadChrToIndex("chr/ch08702.itc", 0x26)
    SoundLoad(460)
    OP_68(0, 1100, -5000, 0)
    MoveCamera(305, 15, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28500, 0)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x2)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x2)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x153, 0x25)
    SetChrSubChip(0x153, 0x0)
    SetChrFlags(0x153, 0x4)
    SetChrChipByIndex(0x158, 0x26)
    SetChrSubChip(0x158, 0x0)
    SetChrFlags(0x158, 0x4)
    SetChrPos(0x101, -400, 100, 600, 90)
    SetChrPos(0x102, -400, 100, 2000, 90)
    SetChrPos(0x103, -100, 100, 2600, 135)
    SetChrPos(0x104, 1300, 100, 3000, 180)
    SetChrPos(0x153, -400, 100, 1300, 90)
    SetChrPos(0x158, 500, 100, 3000, 180)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x1)
    SetChrPos(0x8, 900, 100, -600, 0)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -700, 100, -1900, 180)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 900, 100, -1900, 180)
    BeginChrThread(0x101, 3, 0, 5)
    Sound(460, 2, 80, 0)
    OP_68(0, 1100, 0, 5000)
    SetCameraDistance(26500, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x11)
    Sleep(500)

    #C0001
    ChrTalk(
        0x9,
        (
            "#2803F#5Pルバーチェのみならず\x01",
            "警備隊までもか……\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xA,
        (
            "#12P#2906F……何というか……\x01",
            "とんでもない状況ですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#11P#0006F……ええ。\x01",
            "正直、悪夢を見ている気分です。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x102,
        (
            "#11P#0105Fところで、おじさまたちは\x01",
            "どうしてあんなタイミングで？\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x9,
        (
            "#2800F#5Pああ、共和国での商談があって\x01",
            "その帰りだったんだが……\x02\x03",

            "#2803Fタングラム門を越えたあたりで\x01",
            "マフィアたちの襲撃を受けてね。\x02\x03",

            "#2801F何とか振り切って街に辿り着いたら\x01",
            "君たちが襲われていたというわけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x102,
        "#11P#0101Fそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#11P#0304Fいや～。\x01",
            "しかしマジで助かったッスよ。\x02\x03",

            "#0305Fこの車、もしかして防弾ッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x9,
        (
            "#2809F#5Pああ、特注品でね。\x02\x03",

            "#2800Fガラスも防弾だから\x01",
            "簡単には破れないはずさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x103,
        (
            "#0202F#11Pライフォルト社製の\x01",
            "最新の防弾リムジンですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x104,
        "#11P#0300Fなるほどねぇ……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xA,
        (
            "#12P#2903Fでも、さすがに砲撃までは\x01",
            "耐えられないでしょうし……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 0x2)
    Sleep(300)

    #C0012
    ChrTalk(
        0xA,
        (
            "#12P#2901F──お父様。\x01",
            "このままＩＢＣに戻っては？\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x9,
        (
            "#2804F#5Pああ、そのつもりだよ。\x02\x03",

            "#2800F彼らも疲れているだろうから\x01",
            "ゆっくりと休んでもらおう。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0014
    ChrTalk(
        0x101,
        (
            "#11P#0011Fそんな、これ以上、\x01",
            "ご迷惑をおかけする訳には……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        (
            "#11P#0108Fその、お気持ちは\x01",
            "とても嬉しいのですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xA,
        (
            "#12P#2904Fエリィ。\x01",
            "水臭いことを言わないで頂戴。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        (
            "#2800F#5PＩＢＣのゲートは特殊合金製だ。\x01",
            "簡単に破られる事はないだろう。\x02\x03",

            "#2803FそれにＩＢＣ総裁として\x01",
            "クロスベルの治安については\x01",
            "無関心でいられない……\x02\x03",

            "#2801Fできれば、詳しい事情を\x01",
            "君たちから聞かせて欲しいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        "#11P#0102Fディーターおじさま……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        (
            "#11P#0002F……分かりました。\x01",
            "ご迷惑をおかけします。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xA,
        "#12P#2902Fうふふ、決まりですわね。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x153,
        "#5P#1108F#60W…………………………\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x158,
        "#11P#6008F#60W…………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(50)
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    #C0023
    ChrTalk(
        0x101,
        (
            "#0000F#5P２人とも……\x01",
            "なんだか眠そうだな？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x153, 0x2)
    Sleep(300)

    #C0024
    ChrTalk(
        0x153,
        (
            "#11P#1101F#40Wえー……？\x01",
            "キーアねむくないよー。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x158,
        "#11P#6000F#40Wだ、大丈夫です……\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x102,
        (
            "#11P#0106F無理もないわ。\x01",
            "もう１０時近くだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#11P#0300Fあれだけの修羅場に\x01",
            "付き合わせちまったからなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xA,
        (
            "#12P#2909Fうふふ、ＩＢＣに着いたら\x01",
            "ベッドを用意しておきましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x9,
        (
            "#2800F#5Pよし、そうと決まれば\x01",
            "せいぜい飛ばすとしようか！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(0, 1100, 5000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    BeginChrThread(0xC, 1, 0, 6)
    OP_6F(0x1)
    EndChrThread(0x101, 0x3)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x153, 0x4)
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    ClearChrFlags(0x158, 0x4)
    SetChrChipByIndex(0x158, 0xFF)
    SetChrSubChip(0x158, 0x0)
    RemoveParty(0x52, 0x0)
    RemoveParty(0x57, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    WaitChrThread(0xC, 1)
    OP_24(0x1CC)
    SetScenarioFlags(0x5C, 0)
    NewScene("c130B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_2A1 end

    def Function_4_DC6(): pass

    label("Function_4_DC6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DEA")
    OP_82(0x14, 0x14, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_4_DC6")

    label("loc_DEA")

    Return()

    # Function_4_DC6 end

    def Function_5_DEB(): pass

    label("Function_5_DEB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E0F")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_5_DEB")

    label("loc_E0F")

    Return()

    # Function_5_DEB end

    def Function_6_E10(): pass

    label("Function_6_E10")

    Sleep(200)
    OP_25(0x1CC, 0x3C)
    Sleep(200)
    OP_25(0x1CC, 0x32)
    Sleep(200)
    OP_25(0x1CC, 0x28)
    Sleep(200)
    OP_25(0x1CC, 0x1E)
    Sleep(200)
    OP_25(0x1CC, 0x14)
    Sleep(200)
    OP_25(0x1CC, 0xA)
    Sleep(200)
    OP_24(0x1CC)
    Return()

    # Function_6_E10 end

    def Function_7_E41(): pass

    label("Function_7_E41")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50518.itc", 0x1E)
    LoadChrToIndex("apl/ch50519.itc", 0x1F)
    LoadChrToIndex("chr/ch00002.itc", 0x20)
    LoadChrToIndex("chr/ch00102.itc", 0x21)
    LoadChrToIndex("chr/ch00202.itc", 0x22)
    LoadChrToIndex("chr/ch00302.itc", 0x23)
    SoundLoad(492)
    OP_68(100000, 900, 5000, 0)
    MoveCamera(300, 17, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(30500, 0)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x1)
    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x102, 0x21)
    SetChrSubChip(0x102, 0x1)
    SetChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x104, 0x23)
    SetChrSubChip(0x104, 0x1)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 99600, 100, -300, 90)
    SetChrPos(0x102, 99600, 100, -1200, 90)
    SetChrPos(0x104, 99600, 100, -2200, 90)
    SetChrPos(0x103, 100900, 100, -3000, 0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 101300, -100, 900, 270)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x1F)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 101000, 100, 2250, 0)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFrame(0xFF, "wine", 0x0, 0x1)
    SetMapObjFlags(0x9, 0x4)
    LoadEffect(0x0, "battle\\cr008101.eff")
    LoadEffect(0x1, "event\\ev608_01.eff ")
    LoadEffect(0x2, "event\\eva01_00.eff")
    LoadEffect(0x3, "event\\eva03_00.eff")
    BeginChrThread(0x101, 3, 0, 4)
    Sound(492, 2, 100, 0)
    OP_68(100000, 900, 0, 5000)
    SetCameraDistance(28500, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_0D()
    OP_6F(0x11)

    #C0030
    ChrTalk(
        0x104,
        "#0309Fヒュウ！\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        "#0002F#5P課長……やりますね！\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x102,
        (
            "#0109F#5Pまさかあんな簡単に\x01",
            "突破できてしまうなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x103,
        "#6P#0202F……ちょっと驚きです。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xB,
        (
            "#1004F#5Pま、半年くらい乗ってなかったが\x01",
            "何とかなるもんだな。\x02\x03",

            "#1001Fよし、このまま飛ばして\x01",
            "アルモリカ古道に出るぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        "#0000F#5Pお願いします……！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)
    #Sound(2047, 255, 100, 0)    #voice#Zeit

    #C0036
    ChrTalk(
        0x8,
        "#11P#1201F……グルルル……\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(300)

    #C0037
    ChrTalk(
        0x101,
        "#0005F#5Pツァイト……？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x104,
        "#0301Fなんだ、何かあんのか？\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    #C0039
    ChrTalk(
        0x103,
        (
            "#6P#0207F後方から車両が接近……！\x02\x03",

            "警備隊の新型車両です……！\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xB,
        "#1005F#5Pなに……！？\x02",
    )

    CloseMessageWindow()
    OP_68(100000, 900, -2000, 2000)
    FadeToDark(2000, 0, -1)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    OP_0D()
    OP_6F(0x1)
    EndChrThread(0x101, 0x3)
    OP_24(0x1EC)
    OP_C7(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed7_ev03.pmf", 0x20F, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C7(0x1, 0x10)
    SoundLoad(492)
    OP_68(100000, 900, 0, 0)
    MoveCamera(300, 17, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28500, 0)
    Sound(492, 2, 100, 0)
    FadeToBright(1000, 0)
    ClearScenarioFlags(0x0, 0)
    BeginChrThread(0x102, 3, 0, 8)
    Sleep(1000)

    #C0041
    ChrTalk(
        0x101,
        "#0010F#5Pうおっ……！\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        "#0106F#5Pきゃあっ……！\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        "#6P#0208F……マズイです……\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#0310Fとんでもねぇモン\x01",
            "持ち出しやがって……！\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xB,
        (
            "#1007F#5Pとにかく振り切るしかない……！\x02\x03",

            "お前ら、しっかり掴まって──\x02",
        )
    )

    CloseMessageWindow()
    OP_AD(0x0)
    EndChrThread(0x101, 0x3)
    BeginChrThread(0x102, 3, 0, 9)
    Sleep(300)
    PlayEffect(0x0, 0x0, 0xB, 0x0, -200, 300, 300, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)

    def lambda_14A0():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_14A0)
    SetChrSubChip(0xB, 0x1)

    #C0046
    ChrTalk(
        0xB,
        "#1010F#4Sがっ……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 3)
    OP_68(100000, 900, 1000, 1500)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    OP_6F(0x1)

    #C0047
    ChrTalk(
        0x101,
        "#0011F#5Pか、課長！？\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x102,
        "#0101F#5P大丈夫ですか……！？\x02",
    )

    CloseMessageWindow()

    def lambda_1544():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1544)
    SetChrSubChip(0xB, 0x2)
    Sleep(800)

    #C0049
    ChrTalk(
        0xB,
        (
            "#1003F#5P#40Wし、心配ない……\x01",
            "……カスリ傷だ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#0013F#5Pし、しかし……\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        "#0307F止血しねぇとヤバイぞ！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    #C0052
    ChrTalk(
        0x103,
        (
            "#6P#0201F後方からもう一台\x01",
            "車両が接近……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)

    #C0053
    ChrTalk(
        0x102,
        "#0108F#11Pそ、そんな……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0054
    ChrTalk(
        0x101,
        (
            "#0007F#5P課長……\x01",
            "もう停車してください！\x02\x03",

            "早く手当てをしないと……！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    Sleep(300)

    #C0055
    ChrTalk(
        0xB,
        (
            "#1010F#5P#30Wいいからしっかり\x01",
            "掴まっていろ……！\x02\x03",

            "お前ら若い連中の道を拓くのが\x01",
            "俺たちオヤジどもの役目だ……\x02\x03",

            "#1007F絶対に送り届けてやる……！\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        "#0005F#5Pか、課長……\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        "#0306Fこの隠れ熱血オヤジが……\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    #C0058
    ChrTalk(
        0x103,
        (
            "#6P#0205Fあ……\x02\x03",

            "#0214F──もう一台の車両は、\x01",
            "新型車両ではありません！\x02\x03",

            "ノエルさんの警備隊車両です！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(300)

    #C0059
    ChrTalk(
        0x101,
        "#0002F#5Pあ……\x02",
    )

    CloseMessageWindow()
    OP_68(100000, 900, -2000, 3000)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_24(0x1EC)
    OP_C7(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed7_ev04.pmf", 0x20F, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C7(0x1, 0x10)
    SoundLoad(492)
    OP_68(100000, 900, 0, 0)
    MoveCamera(300, 17, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(28500, 0)
    Sound(492, 2, 100, 0)
    FadeToBright(1000, 0)
    BeginChrThread(0xC, 1, 0, 10)
    Sleep(2500)

    #C0060
    ChrTalk(
        0x101,
        "#0000F#5Pノエル曹長……！\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x102,
        "#0102F#5P来てくれたのね……！\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x104,
        (
            "#0309Fさすが警備隊若手の\x01",
            "ホープだぜ……！\x02",
        )
    )

    CloseMessageWindow()
    Sound(962, 0, 100, 0)
    Sleep(1800)
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("娘の声")

    #A0063
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──聞こえますか！\x02\x03",

            "ノエル・シーカーです！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x104, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    Sleep(150)

    #C0064
    ChrTalk(
        0x101,
        "#0002F#6Pああ、聞こえている！\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xB,
        (
            "#1004F#6P#30Wソーニャの秘蔵っ子か……\x01",
            "……正直助かったぞ……！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("ノエルの声")

    #A0066
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ふふっ、どういたしまして。\x02\x03",

            "──もう一台もこちらが\x01",
            "相手をしておきます！\x02\x03",

            "そのまま行ってください！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0067
    ChrTalk(
        0xB,
        "#1007F#6Pおお……！\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        "#0007F#6Pそちらも気をつけてくれ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0xC, 0x1)
    EndChrThread(0x101, 0x3)
    OP_82(0x96, 0x0, 0xBB8, 0x3E8)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 4)
    Fade(100)
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    PlayEffect(0x3, 0x0, 0x101, 0x40, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x1, 0x101, 0x40, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x2, 0x101, 0x40, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x3, 0x101, 0x40, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x4, 0x101, 0x40, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_68(100000, 900, -10000, 4000)
    MoveCamera(330, 13, 0, 4000)
    SetCameraDistance(32000, 4000)
    FadeToDark(4000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x101, 0x3)
    OP_24(0x1EC)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    StopEffect(0x4, 0x0)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    OP_C7(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed7_ev05.pmf", 0x20F, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C7(0x1, 0x10)
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x1EC)
    SetScenarioFlags(0x5C, 0)
    NewScene("r307B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_E41 end

    def Function_8_1DCC(): pass

    label("Function_8_1DCC")

    OP_82(0x0, 0x190, 0xBB8, 0x320)
    Sound(196, 0, 100, 0)
    Sleep(1000)
    OP_82(0x12C, 0x0, 0xBB8, 0x3E8)
    Sound(200, 0, 100, 0)
    Sleep(1200)
    OP_82(0x0, 0x190, 0xBB8, 0x320)
    Sound(834, 0, 100, 0)
    Sleep(1000)
    SetScenarioFlags(0x0, 0)
    BeginChrThread(0x101, 3, 0, 4)
    Return()

    # Function_8_1DCC end

    def Function_9_1E24(): pass

    label("Function_9_1E24")

    Sound(960, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 98500, -500, 2200, 270, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(99000, 900, 0, 100)
    OP_82(0x320, 0x0, 0x1388, 0x2BC)
    Sleep(100)
    ClearMapObjFlags(0x2, 0x4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 98500, 1600, 2200, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    ClearMapObjFlags(0x3, 0x4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 98500, 1400, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    ClearMapObjFlags(0x4, 0x4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 98500, 1700, 1800, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    ClearMapObjFlags(0x5, 0x4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 98500, 1600, 1300, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    ClearMapObjFlags(0x6, 0x4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 98500, 1400, 2900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    ClearMapObjFlags(0x7, 0x4)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 98500, 1600, 2000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    StopEffect(0x0, 0x2)
    BeginChrThread(0x101, 3, 0, 4)
    Return()

    # Function_9_1E24 end

    def Function_10_2010(): pass

    label("Function_10_2010")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_203B")
    Sound(961, 0, 100, 0)
    Sleep(1500)
    Sound(961, 0, 100, 0)
    Sleep(2500)
    Sound(961, 0, 100, 0)
    Sleep(2000)
    Jump("Function_10_2010")

    label("loc_203B")

    Return()

    # Function_10_2010 end

    SaveToFile()

Try(main)
