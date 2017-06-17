from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c153b.bin",                # FileName
        "c153b",                    # MapName
        "c153b",                    # Location
        0x00AE,                     # MapIndex
        "ed7000",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 174, 0, 0, 0, 1],
    )

    BuildStringList((
        "c153b",                  # 0
        "ディーター市長",         # 1
        "マクダエル議長",         # 2
        "ダドリー捜査官",         # 3
        "ソーニャ司令",           # 4
        "ダグラス副司令",         # 5
        "セルゲイ課長",           # 6
        "ピエール副局長",         # 7
        "局長？",                 # 8
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(384, 0)                                        # 0

    ScpFunction((
        "Function_0_180",          # 00, 0
        "Function_1_190",          # 01, 1
        "Function_2_191",          # 02, 2
    ))


    def Function_0_180(): pass

    label("Function_0_180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_18F")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_18F")

    Return()

    # Function_0_180 end

    def Function_1_190(): pass

    label("Function_1_190")

    Return()

    # Function_1_190 end

    def Function_2_191(): pass

    label("Function_2_191")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05602.itc", 0x1E)
    LoadChrToIndex("chr/ch05802.itc", 0x1F)
    LoadChrToIndex("chr/ch05702.itc", 0x20)
    LoadChrToIndex("chr/ch44902.itc", 0x21)
    LoadChrToIndex("chr/ch06402.itc", 0x22)
    LoadChrToIndex("chr/ch02502.itc", 0x23)
    LoadChrToIndex("chr/ch00902.itc", 0x24)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 272800, 100, 6950, 270)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 272800, 100, 4950, 270)
    SetChrChipByIndex(0xC, 0x21)
    SetChrSubChip(0xC, 0x2)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 269200, 100, 8950, 90)
    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 269200, 100, 6950, 90)
    SetChrChipByIndex(0xE, 0x22)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 269200, 100, 4950, 90)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x1)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, 269200, 100, 2950, 90)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x1)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 269200, 100, 900, 90)
    OP_68(271500, -1100, 5950, 0)
    MoveCamera(90, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(21000, 0)
    OP_68(271500, 900, 5950, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(271700, 800, 5950, 0)
    MoveCamera(36, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17630, 0)
    SetCameraDistance(16630, 2000)
    OP_0D()
    OP_6F(0x79)

    #C0001
    ChrTalk(
        0x9,
        (
            "#02503F#11P何たることか……\x02\x03",

            "#02501Fまさかここまで大それた事を\x01",
            "一猟兵団が引き起こすとは。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    #C0002
    ChrTalk(
        0x8,
        (
            "#5P#02803F……背後に何者かがいるのは\x01",
            "間違いないでしょう。\x02\x03",

            "#02801Fそれも通商会議の時と同じく……\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xD,
        (
            "#6P#01003Fエレボニア帝国政府……\x02\x03",

            "#01001Fいや、あえて特定するなら\x01",
            "『帝国軍情報局』ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xA,
        (
            "#12P#00606Fその可能性は高いと\x01",
            "言わざるを得ませんね……\x02\x03",

            "#00601Fこのクロスベルでも\x01",
            "情報局の将校が『赤い星座』と\x01",
            "頻繁に連絡を取り合っていました。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xE,
        (
            "#6Pこ、こうなってしまっては\x01",
            "帝国政府に泣き付いてみるしか\x01",
            "ないんじゃないでしょうか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xE,
        (
            "#6Pもしくは共和国政府に頼んで\x01",
            "味方になってもらうとか……！\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        (
            "#5P#02803Fいや、既に昼間の時点で\x01",
            "帝国政府には問い合わせている。\x02\x03",

            "#02801F返事は当然ながら……\x01",
            "『身に覚えがない』だったがね。\x02\x03",

            "#02806F……そしてこれは私の責任だが\x01",
            "独立提言以来、共和国政府にも\x01",
            "協力を頼める状況ではなくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xE,
        "#6Pそ、そんな……\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xE,
        (
            "#6P……い、いえ！\x01",
            "決して市長の責任ではっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x9,
        (
            "#02503F#11Pいずれにしても……\x01",
            "このままでは、自治州政府としても\x01",
            "正式な抗議声明を出すしかないだろう。\x02\x03",

            "#02500Fしかし……何はともあれ\x01",
            "マインツの住民の安否が気になる。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xB,
        (
            "#6P#02003F……民間の飛行艇に依頼して\x01",
            "何とか上空から確認は出来ました。\x02\x03",

            "#02001F現時点では、略奪などの行為が\x01",
            "行われている気配は無さそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xC,
        (
            "#5Pですが、マインツの住民が、\x01",
            "人質である状況は変わりません。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xC,
        (
            "#5P食料の備蓄も心配ですし、\x01",
            "グズグズはしてられませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x0)
    Sleep(150)

    #C0014
    ChrTalk(
        0x8,
        (
            "#11P#02803F無論だ、すぐに対策を打とう。\x02\x03",

            "#02801F……警備隊の被害は\x01",
            "どの程度のものだったかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xB,
        (
            "#6P#02006F……人的、物的被害共に\x01",
            "甚大と言わざるを得ません。\x02\x03",

            "#02001F現在、予備戦力の全てを\x01",
            "山道に展開している状況です。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        "#11P#02806Fそうか……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x8, 0x1)
    Sleep(300)

    #C0017
    ChrTalk(
        0x8,
        (
            "#02801F#5P──相手は戦闘のプロだが\x01",
            "あくまでミラで雇われている集団だ。\x02\x03",

            "交渉次第では、これ以上の惨事を\x01",
            "食い止められる可能性もあるだろう。\x02\x03",

            "警察の諸君には、\x01",
            "市民の不安を抑えてもらうと同時に\x01",
            "そのあたりの可能性も探って欲しい。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xA,
        "#12P#00601F了解しました！\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xE,
        "#6Pた、直ちに！\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xD,
        (
            "#6P#01003Fギルドとも連絡を取って\x01",
            "手を尽くしてみますか……\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17130, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 3)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_191 end

    SaveToFile()

Try(main)
