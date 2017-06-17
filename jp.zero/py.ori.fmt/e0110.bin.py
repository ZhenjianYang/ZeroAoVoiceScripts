from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e0110.bin",                # FileName
        "e0110",                    # MapName
        "e0110",                    # Location
        0x0001,                     # MapIndex
        "ed7102",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e0110",                  # 0
        "レクター",               # 1
        "ディーター総裁",         # 2
    ))

    DeclNpc(-449,    150,     1500,    90,   500,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(750,     150,     3150,    180,  500,  0x0, 0,   1,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_D8",           # 00, 0
        "Function_1_E8",           # 01, 1
        "Function_2_E9",           # 02, 2
    ))


    def Function_0_D8(): pass

    label("Function_0_D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_E7")
    ClearScenarioFlags(0x5C, 0)
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
    LoadChrToIndex("chr/ch07402.itc", 0x1E)
    LoadChrToIndex("chr/ch05602.itc", 0x1F)
    OP_68(0, 1000, 2650, 0)
    MoveCamera(315, 17, 0, 0)
    OP_6E(260, 0)
    SetCameraDistance(28500, 0)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x8, 0x0)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFrame(0x1, "main", 0x2, "stop")
    SetMapObjFrame(0xFF, "bg00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "bg00_y", 0x0, 0x1)
    SetMapObjFrame(0xFF, "effect00_add", 0x0, 0x1)
    VolumeBGM(0x32, 0x1F4)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD3, 7)), scpexpr(EXPR_END)), "loc_381")

    #C0001
    ChrTalk(
        0x9,
        (
            "#2801F──ズバリ言おう。\x01",
            "どうかね、ＩＢＣ#6Rウ  チ#に来ないかね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x8,
        (
            "#3510Fん～、そうだなァ。\x01",
            "……時給次第ってとこか。\x02\x03",

            "#3509Fあと残業手当と\x01",
            "危険手当も出してくれると\x01",
            "助かるぜ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x9,
        (
            "#2809Fははははは……！\x01",
            "その程度なら全然構わんよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x109,
        (
            "#0500F#3P（？？？\x01",
            "  あれはＩＢＣの総裁と……\x01",
            "  バカンスルックの観光客？）\x02\x03",

            "（変な組み合わせですね……）\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x101,
        (
            "#0006F#3P（……まあ、あんまり\x01",
            "  気にしない方がいいと思う……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_640")

    label("loc_381")


    #C0006
    ChrTalk(
        0x8,
        (
            "#3509Fいや～、そんときは焦ったんだが\x01",
            "これが後で役に立ったんだよな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x9,
        (
            "#2809Fははは、君は本当に型破りだな！\x02\x03",

            "#2803Fだがその感性、\x01",
            "捨て置くには実に惜しい。\x02\x03",

            "#2801F──ズバリ言おう。\x01",
            "どうかね、ＩＢＣ#6Rウ  チ#に来ないかね！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x8, 0x1)

    #C0008
    ChrTalk(
        0x8,
        (
            "#3505Fん～……？\x01",
            "そういや総裁んトコって……\x02\x03",

            "#3502F時給、いくらくらい？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    OP_64(0x9)

    #C0009
    ChrTalk(
        0x9,
        (
            "#2809Fははははは……！\x01",
            "君は本当に面白いなぁ！\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        "#3509Fアハハハハハ～～～♪\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x104,
        (
            "#0306F#3P（な、何やってやがんだ\x01",
            "  あいつ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        (
            "#0111F#3P（まさか……おじさまにまで\x01",
            "  取り入ってるなんて……）\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#0012F#3P（な、なんて\x01",
            "  コメントしたらいいのか……）\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x103,
        (
            "#0211F#3P（……あの人、本当に\x01",
            "  何者なんでしょうか……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_640")

    FadeToDark(1000, 0, -1)
    OP_0D()
    VolumeBGM(0x64, 0x1F4)
    SetScenarioFlags(0xD3, 7)
    SetScenarioFlags(0x5C, 0)
    NewScene("c1300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_E9 end

    SaveToFile()

Try(main)
