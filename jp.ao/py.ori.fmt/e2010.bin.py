from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e2010.bin",                # FileName
        "e2010",                    # MapName
        "e2010",                    # Location
        0x0001,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e2010",                  # 0
        "セルゲイ課長",           # 1
        "背景",                   # 2
        "ユーリ",                 # 3
        "サイクス",               # 4
        "レジー",                 # 5
        "ミンネス",               # 6
        "黒服",                   # 7
        "黒服",                   # 8
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(440, 0)                                        # 0

    ScpFunction((
        "Function_0_1B8",          # 00, 0
        "Function_1_2C1",          # 01, 1
        "Function_2_327",          # 02, 2
        "Function_3_34C",          # 03, 3
        "Function_4_7CB",          # 04, 4
        "Function_5_BE3",          # 05, 5
        "Function_6_1143",         # 06, 6
        "Function_7_17D9",         # 07, 7
        "Function_8_26DA",         # 08, 8
        "Function_9_32E6",         # 09, 9
        "Function_10_3730",        # 0A, 10
        "Function_11_3AEE",        # 0B, 11
        "Function_12_480E",        # 0C, 12
        "Function_13_668E",        # 0D, 13
        "Function_14_6995",        # 0E, 14
        "Function_15_6B1E",        # 0F, 15
        "Function_16_6C57",        # 10, 16
    ))


    def Function_0_1B8(): pass

    label("Function_0_1B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1CF")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 3)
    Jump("loc_2C0")

    label("loc_1CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1E3")
    ClearScenarioFlags(0x22, 1)
    Event(0, 4)
    Jump("loc_2C0")

    label("loc_1E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1F7")
    ClearScenarioFlags(0x22, 2)
    Event(0, 5)
    Jump("loc_2C0")

    label("loc_1F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_20B")
    ClearScenarioFlags(0x22, 3)
    Event(0, 6)
    Jump("loc_2C0")

    label("loc_20B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_21F")
    ClearScenarioFlags(0x22, 4)
    Event(0, 7)
    Jump("loc_2C0")

    label("loc_21F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_233")
    ClearScenarioFlags(0x22, 5)
    Event(0, 8)
    Jump("loc_2C0")

    label("loc_233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_24A")
    ClearScenarioFlags(0x22, 6)
    SetScenarioFlags(0x0, 2)
    Event(0, 9)
    Jump("loc_2C0")

    label("loc_24A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_261")
    ClearScenarioFlags(0x22, 7)
    SetScenarioFlags(0x0, 3)
    Event(0, 10)
    Jump("loc_2C0")

    label("loc_261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_275")
    ClearScenarioFlags(0x23, 0)
    Event(0, 11)
    Jump("loc_2C0")

    label("loc_275")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_289")
    ClearScenarioFlags(0x23, 1)
    Event(0, 12)
    Jump("loc_2C0")

    label("loc_289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_29D")
    ClearScenarioFlags(0x23, 3)
    Event(0, 13)
    Jump("loc_2C0")

    label("loc_29D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 4)), scpexpr(EXPR_END)), "loc_2B1")
    ClearScenarioFlags(0x23, 4)
    Event(0, 14)
    Jump("loc_2C0")

    label("loc_2B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 6)), scpexpr(EXPR_END)), "loc_2C0")
    ClearScenarioFlags(0x23, 6)
    Event(0, 16)

    label("loc_2C0")

    Return()

    # Function_0_1B8 end

    def Function_1_2C1(): pass

    label("Function_1_2C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_2DB")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)
    Jump("loc_326")

    label("loc_2DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2F5")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 2)
    Jump("loc_326")

    label("loc_2F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_30F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xCD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 3)
    Jump("loc_326")

    label("loc_30F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_326")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x23D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_326")

    Return()

    # Function_1_2C1 end

    def Function_2_327(): pass

    label("Function_2_327")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34B")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_2_327")

    label("loc_34B")

    Return()

    # Function_2_327 end

    def Function_3_34C(): pass

    label("Function_3_34C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x8000000)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch02502.itc", 0x22)
    SoundLoad(460)
    OP_68(-1110, 500, 3290, 0)
    MoveCamera(323, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14280, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0x105, 0x1)
    SetChrPos(0x101, 1200, 100, -1900, 180)
    SetChrPos(0x102, -900, 100, -400, 180)
    SetChrPos(0x109, -900, 100, -1700, 180)
    SetChrPos(0x105, 1200, 100, -400, 180)
    SetChrPos(0x8, 200, 100, 1000, 180)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xFF, "effect00_add", 0x0, 0x1)
    VolumeBGM(0x3C, 0x3E8)
    FadeToBright(1000, 0)
    OP_68(-570, 500, 500, 3000)
    MoveCamera(323, 22, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(14280, 3000)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)

    #C0001
    ChrTalk(
        0x109,
        (
            "#10109F#11Pはあ……新車の薫りがする……\x02\x03",

            "#10102Fハンドル周りも使いやすそうだし\x01",
            "これは物凄くいい車ですよっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x105,
        (
            "#10304F#11Pシートの座り心地もいいし\x01",
            "内装のデザインも悪くない。\x02\x03",

            "#10302Fフフ、なかなか気に入ったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x101,
        (
            "#00012F#12Pはは……\x01",
            "確かにいい車みたいだな。\x02\x03",

            "#00002Fそれに、この広さだったら\x01",
            "８人くらいは十分乗れそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x102,
        (
            "#00109F#5Pふふ、ティオちゃんとランディが\x01",
            "戻ってきても大丈夫そうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "#01004F#11Pま、とにかく発進してみろ。\x02\x03",

            "#01002F車の良し悪しってのは\x01",
            "転がしてみてナンボだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x109,
        "#10100F#11Pはい、それでは発進します！\x02",
    )

    CloseMessageWindow()
    Sound(470, 0, 100, 0)
    OP_82(0xF, 0x23, 0xBB8, 0x1F4)
    Sleep(500)
    Sound(460, 2, 80, 0)
    BeginChrThread(0x101, 3, 0, 2)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x3)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0x109, 0x1)
    SetChrFlags(0x105, 0x1)
    StopSound(460, 1000, 80)
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    VolumeBGM(0x64, 0x64)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x235), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("t6000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_3_34C end

    def Function_4_7CB(): pass

    label("Function_4_7CB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch02502.itc", 0x22)
    SoundLoad(460)
    OP_68(-720, 500, 200, 0)
    MoveCamera(323, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0x105, 0x1)
    SetChrPos(0x101, 1200, 100, -1900, 180)
    SetChrPos(0x102, -900, 100, -400, 180)
    SetChrPos(0x109, -900, 100, -1700, 180)
    SetChrPos(0x105, 1200, 100, -400, 180)
    SetChrPos(0x8, 200, 100, 1000, 180)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    BeginChrThread(0x101, 3, 0, 2)
    Sound(460, 2, 80, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(14500, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)

    #C0007
    ChrTalk(
        0x109,
        "#10109F#5P～～～～♪\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        "#00002F#12Pこれは凄いな……\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        (
            "#00104F#11Pええ、スピードが出ているのに\x01",
            "すごく安定しているし……\x02\x03",

            "#00102Fエンジン音もとっても静かだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x105,
        (
            "#10309F#12Pそれでいて心地よい振動が\x01",
            "感じられるのもニクイよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x8,
        (
            "#01004F#11Pさすがは天下のＺＣＦだな。\x02\x03",

            "#01002F俺も個人的に一台、\x01",
            "乗り回したいくらいだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x109,
        (
            "#10108F#5Pはあ、警備隊の装甲車も\x01",
            "お気に入りなんですけど……\x02\x03",

            "#10106F浮気しちゃいそうで\x01",
            "何だか後ろめたいです……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)
    Sleep(200)

    #C0013
    ChrTalk(
        0x101,
        "#00012F#12Pはは、そんなものなんだ？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x105,
        (
            "#10302F#12Pフフ、カーマニアならではの\x01",
            "感性みたいだね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(460, 1000, 80)
    Sleep(1000)
    EndChrThread(0x101, 0x3)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0x109, 0x1)
    SetChrFlags(0x105, 0x1)
    SetScenarioFlags(0x22, 0)
    NewScene("r4000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_7CB end

    def Function_5_BE3(): pass

    label("Function_5_BE3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch02502.itc", 0x22)
    SoundLoad(460)
    OP_68(99290, 600, 1470, 0)
    MoveCamera(323, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14280, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0x105, 0x1)
    SetChrPos(0x101, 98950, 150, 1900, 0)
    SetChrPos(0x102, 101000, 150, 250, 0)
    SetChrPos(0x109, 101000, 150, 1800, 0)
    SetChrPos(0x105, 98950, 150, 250, 0)
    SetChrChipByIndex(0x8, 0x22)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 300, 100, 1100, 180)
    SetChrPos(0x8, 100000, 150, -1350, 0)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    BeginChrThread(0x101, 3, 0, 2)
    Sound(460, 2, 80, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(13280, 2000)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    Sleep(300)

    #C0015
    ChrTalk(
        0x8,
        "#01003F#6P──隻眼、赤毛の偉丈夫か。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        (
            "#00008F#5Pええ……\x01",
            "既に一課には連絡しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x105,
        (
            "#10306F#5Pま、何者かは知らないけど\x01",
            "どう考えても普通じゃないよね。\x02\x03",

            "#10301Fあんな異常な戦闘力を\x01",
            "隠そうともしてないんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "#01001F#6P……問題はそこだな。\x02\x03",

            "#01003Fテロリストや猟兵だった場合、\x01",
            "自分の戦闘力は隠すはずだ。\x02\x03",

            "#01000Fいくらクロスベルに、連中を直接、\x01",
            "取り締まれる法律が無くてもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x109,
        "#10108F#5Pですよね……\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x102,
        (
            "#00106F#12P黒月や帝国政府も\x01",
            "不穏な動きを見せていますし……\x02\x03",

            "#00101Fルバーチェ消滅後の揺れ戻しが\x01",
            "水面下で始まったみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "#01006F#6P水面下というには\x01",
            "ちと露骨すぎるみたいだがな。\x02\x03",

            "#01000F今月末には通商会議もある。\x02\x03",

            "お前らも相当、忙しくなるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#00003F#5Pええ、心得ています。\x02\x03",

            "#00001F……とりあえず、あの男の素性は\x01",
            "確かめる必要がありそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x102,
        (
            "#00108F#12Pそうね……\x01",
            "どこに滞在しているのかしら？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(12780, 2000)
    OP_6F(0x79)
    OP_0D()
    StopSound(460, 1000, 80)
    Sleep(1000)
    EndChrThread(0x101, 0x3)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0x109, 0x1)
    SetChrFlags(0x105, 0x1)
    SetScenarioFlags(0x22, 0)
    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_BE3 end

    def Function_6_1143(): pass

    label("Function_6_1143")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    SoundLoad(460)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)
    OP_68(-720, 500, 200, 0)
    MoveCamera(323, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x102, 1200, 100, -1900, 180)
    SetChrPos(0x101, -900, 100, -400, 180)
    SetChrPos(0x109, -900, 100, -1700, 180)
    SetChrPos(0x104, 1200, 100, -400, 180)
    SetChrPos(0x105, 0, 100, 1000, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0xB, 0x4)
    BeginChrThread(0x101, 3, 0, 2)
    Sound(460, 2, 80, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(14500, 2000)
    OP_6F(0x79)
    OP_0D()
    Sound(2367, 255, 80, 0)    #voice#Randy
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 4)), scpexpr(EXPR_END)), "loc_135F")

    #C0024
    ChrTalk(
        0x104,
        (
            "#00309F#11Pここに来る時にも思ったが\x01",
            "ホント良い車だよなぁ。\x02\x03",

            "#00302Fこんな車を自分で持てたら\x01",
            "ナンパし放題じゃねえか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13C2")

    label("loc_135F")


    #C0025
    ChrTalk(
        0x104,
        (
            "#00309F#11Pしっかし良い車だよなぁ。\x02\x03",

            "#00302Fこんな車を自分で持てたら\x01",
            "ナンパし放題じゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13C2")

    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0026
    ChrTalk(
        0x101,
        "#00012F#5Pあのな……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    #C0027
    ChrTalk(
        0x105,
        (
            "#10302F#5Pフフ、アシに頼るようじゃ\x01",
            "君もまだまだなんじゃないの？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(300)

    #C0028
    ChrTalk(
        0x104,
        (
            "#00301F#11Pうぐっ……\x01",
            "後輩のクセに生意気な。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x2)
    Sleep(300)

    #C0029
    ChrTalk(
        0x102,
        (
            "#00109F#6Pふふっ……\x01",
            "さすがに分#2Rぶ#が悪いわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x109,
        (
            "#10102F#5Pランディ先輩のモテ自慢も\x01",
            "ワジ君にかかれば形無しですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        (
            "#00305F#11Pこら、ノエル！\x01",
            "同じ警備隊出身なのに薄情な。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x109,
        "#10112F#5Pふふっ、すみません。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 4)), scpexpr(EXPR_END)), "loc_171D")

    #C0033
    ChrTalk(
        0x101,
        (
            "#00005F#5Pそういや、ランディ。\x02\x03",

            "#00000F課長からスペアキーを借りて\x01",
            "この車に乗って来たんだよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        (
            "#00100F#6Pいつの間に導力車の運転が\x01",
            "出来るようになったの？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        (
            "#00304F#11Pああ、訓練の合間に\x01",
            "一通り覚えちまったよ。\x02\x03",

            "#00300Fお前らも暇みて覚えろよ？\x01",
            "なかなか便利なもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#00002F#5Pはは、そうだな。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        (
            "#00104F#6P今後のことを考えると\x01",
            "覚えて損はないかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x105,
        (
            "#10306F#5Pうーん、僕はどちらかというと\x01",
            "運転してもらう方がいいけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_171D")

    Sleep(150)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0039
    ChrTalk(
        0x109,
        "#10101F#11Pあ……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x0)
    Sleep(300)
    SetCameraDistance(15000, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(460, 1000, 80)
    Sleep(1000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    SetScenarioFlags(0x22, 2)
    NewScene("r2060", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_6_1143 end

    def Function_7_17D9(): pass

    label("Function_7_17D9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    SoundLoad(460)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xCC, 0x8F, 0x85, 0x0, 0xE6, 0x0)
    OP_68(150500, 700, 250, 0)
    MoveCamera(307, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14270, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 150400, 100, -1100, 90)
    SetChrPos(0x102, 151900, 100, 900, 90)
    SetChrPos(0x109, 151900, 100, -1100, 90)
    SetChrPos(0x105, 148800, 100, -100, 90)
    SetChrPos(0x104, 150400, 100, 900, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0xB, 0x4)
    BeginChrThread(0x101, 3, 0, 2)
    Sound(460, 2, 80, 0)
    SetCameraDistance(13770, 1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0040
    ChrTalk(
        0x101,
        (
            "#00008F#5P……一体、\x01",
            "何者の仕業だったんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        (
            "#00106F#11P目的がはっきりしないのが\x01",
            "余計に不気味な気がするわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x109,
        (
            "#10108F#6Pあの爆薬も……\x01",
            "どこで調達したんでしょう？\x02\x03",

            "警備隊でもほとんど\x01",
            "使われていないものですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x105,
        (
            "#10306F#5P大方、旧鉱山に残っていた\x01",
            "発破#4Rはっぱ#を使ったとかじゃないの？\x02\x03",

            "#10300Fま、僕も火薬については\x01",
            "あんまり詳しくないけどさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        "#00303F#5Pいや、違うな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    #C0045
    ChrTalk(
        0x105,
        "#10305F#5Pへえ？\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#00105F#12P何か知っているの？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(300)

    #C0047
    ChrTalk(
        0x104,
        (
            "#00301F#11P入口のあたりに\x01",
            "漂っていた硝煙だが……\x02\x03",

            "調合されて１、２年くらいの\x01",
            "新しい爆薬の匂いだった。\x02\x03",

            "しかもかなり高性能のヤツだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        "#00001F#6Pそ、そうなのか……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x109,
        "#10105F#6Pでも、よくご存知ですね？\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x104,
        (
            "#00300F#11P火薬を使った重火器は\x01",
            "完全に廃#2Rすた#れたわけじゃない。\x02\x03",

            "正規軍じゃ滅多に使われないが\x01",
            "未だに好んで使う物好きもいる。\x02\x03",

            "#00303F……特に猟兵団#6Rイェーガー#あたりにな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0051
    ChrTalk(
        0x101,
        "#00013F#6Pまさか……\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x102,
        "#00101F#12Pそ、それって……\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x104,
        (
            "#00306F#11Pま、あくまで可能性の話さ。\x02\x03",

            "#00300Fちなみに今、火薬式の重火器が\x01",
            "一番使われてるのはエレボニアだ。\x02\x03",

            "今もラインフォルト社が\x01",
            "ラインナップを残してるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x109,
        "#10101F#6Pそうだったんですか……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x105,
        (
            "#10302F#5Pフフ、さすがに詳しいね。\x02\x03",

            "#10303Fしかしエレボニアか……\x01",
            "イヤな符合が重なるねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        (
            "#00008F#6Pああ……\x01",
            "昨日のこともあるしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        "#00305F#11Pなんだ、何かあったのか？\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        "#00108F#12Pええ、実は──\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0059
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "レクター特務大尉と再会した経緯を説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sleep(300)

    #C0060
    ChrTalk(
        0x104,
        (
            "#00301F#11P──あの遊び人、\x01",
            "エレボニアのスパイかよ。\x02\x03",

            "どう考えてもタダ者じゃ\x01",
            "無いとは思ったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#00003F#6P単なるスパイというより\x01",
            "情報将校と言うべきだろう。\x02\x03",

            "通商会議を前にして\x01",
            "情報収集をしているだけかも\x01",
            "しれないけど……\x02\x03",

            "#00008F……どうも一緒にいた\x01",
            "赤毛の子が気になるんだよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x102,
        "#00106F#12P……ふう、あの子ね……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x105,
        (
            "#10309F#5Pフフ、君にとっては\x01",
            "トラウマになったみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        (
            "#00302F#11Pなんだなんだ？\x01",
            "まさか色っぽい話かよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x109,
        "#10112F#6Pその、実は……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0066
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "レクターと一緒にいた\x01",
            "赤毛の少女について説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sleep(300)

    #C0067
    ChrTalk(
        0x104,
        (
            "#00305F#11P……へえ…………\x02\x03",

            "……………………………………\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        (
            "#00112F#12Pあ、あの子の話は止めましょう。\x02\x03",

            "#00113Fまったく、イリアさんに\x01",
            "セクハラされるリーシャさんの\x01",
            "気持ちが判った気がするわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#00012F#6Pはは、凄い説得力だな。\x02\x03",

            "#00008F……でも、いつの間にか\x01",
            "懐に入り込まれていたし……\x02\x03",

            "#00001Fただの民間人じゃないのは\x01",
            "間違いないと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x109,
        (
            "#10106F#6Pそういえば……\x01",
            "西クロスベル街道で会った人も\x01",
            "帝国方面から来たんですよね。\x02\x03",

            "#10105Fあ、そういえば、\x01",
            "あの人も赤毛だったっけ……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrSubChip(0x101, 0x0)
    Sleep(200)

    #C0071
    ChrTalk(
        0x105,
        "#10305F#5Pああ、言われてみれば。\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#00003F#5Pレクター大尉とあの子は\x01",
            "赤毛でも色合いが違ったけど……\x02\x03",

            "#00001F考えてみれば、あの子と隻眼の男は\x01",
            "そっくりな色だったかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x105, 0x1)
    Sleep(300)

    #C0073
    ChrTalk(
        0x101,
        "#00011F#6Pあれ……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x102,
        "#00108F#12Pひょ、ひょっとして……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0x1770)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    #Sound(2374, 255, 100, 0)    #voice#Randy

    #C0075
    ChrTalk(
        0x104,
        (
            "#00304F#11P#30Wはは……\x02\x03",

            "#00311F#30W──つまり、俺の赤毛も\x01",
            "そいつらに似てるってわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x109,
        "#10111F#6Pあ……\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x105,
        (
            "#10301F#5P……もしかしなくても\x01",
            "心当たりがあるみたいだね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(100)
    SetChrSubChip(0x104, 0x0)
    Sleep(200)
    Sound(2375, 255, 100, 0)    #voice#Randy
    Sleep(1300)

    #C0078
    ChrTalk(
        0x104,
        (
            "#00304F#5P#40W……参ったな。\x02\x03",

            "#00312F#40W───そう来たかよ#12R㈲　㈲　㈲　㈲　㈲　㈲#。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(13520, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(460, 1000, 80)
    Sleep(1000)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 3)
    NewScene("r2060", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_17D9 end

    def Function_8_26DA(): pass

    label("Function_8_26DA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_7D(0xBE, 0xBE, 0xBE, 0x0, 0x0)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("apl/ch50011.itc", 0x23)
    SoundLoad(460)
    SoundLoad(803)
    SoundLoad(3451)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(150500, 700, 250, 0)
    MoveCamera(307, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14270, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, 150400, 100, -1100, 90)
    SetChrPos(0x102, 151900, 100, 900, 90)
    SetChrPos(0x109, 151900, 100, -1100, 90)
    SetChrPos(0x105, 148800, 100, -100, 90)
    SetChrPos(0x104, 150400, 100, 900, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0xB, 0x4)
    BeginChrThread(0x101, 3, 0, 2)
    PlayBGM("ed7516", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x204), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(460, 2, 80, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(13770, 1000)
    OP_0D()
    SetChrSubChip(0x101, 0x1)
    Sleep(300)

    #C0079
    ChrTalk(
        0x101,
        "#00001F#6Pなあ、ランディ──\x02",
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x0)
    Sleep(200)
    SetChrSubChip(0x102, 0x2)
    Sleep(50)
    SetChrSubChip(0x104, 0x2)
    Sleep(50)
    SetChrSubChip(0x105, 0x2)
    Sleep(300)

    #C0080
    ChrTalk(
        0x101,
        "#00006F#5Pっと、こんな時に……\x02",
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    OP_24(0x323)
    Fade(250)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x9)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    #Sound(2084, 255, 100, 0)    #voice#Lloyd
    SetMessageWindowPos(90, 130, -1, -1)

    #A0081
    AnonymousTalk(
        0x101,
        (
            "#00001F#3Pはい、特務支援課、\x01",
            "ロイド・バニングスです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男の声")

    #A0082
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3451V#40W──バニングス、私だ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xD7B)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0083
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005Fああ、ダドリーさん。\x02\x03",

            "#00000F出張と聞いていましたが\x01",
            "お戻りになったんですね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0084
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、昼過ぎにな。\x02\x03",

            "エマ君から話は聞いた。\x01",
            "世話になったようだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0085
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00004Fいえ、気にしないで下さい。\x02\x03",

            "#00001Fそれよりも……\x01",
            "何かあったんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0086
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、一応お前たちにも\x01",
            "伝えておこうと思ってな。\x02\x03",

            "──ルバーチェ跡地の\x01",
            "新たな所有者が決まった。\x02\x03",

            "『クリムゾン商会』という会社だ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0087
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F『クリムゾン商会』……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0088
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011Fええっ！？\x01",
            "『黒月#4Rヘイユエ#』ではないんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0089
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "連中の裏をかくようにして\x01",
            "電撃的に契約が結ばれたらしい。\x02\x03",

            "どうやら帝国方面からの\x01",
            "裏工作もあったらしいな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0090
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011F帝国方面から……\x02\x03",

            "#00013F一体、どういう会社なんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0091
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "帝都で《ノイエ＝ブラン》という\x01",
            "高級クラブを経営している会社だ。\x02\x03",

            "クロスベル市にもその支店が\x01",
            "１年ほど前にオープンしている。\x02\x03",

            "その会社がクロスベルに\x01",
            "本格的に進出してきたわけだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0092
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001Fで、ですが当然、\x01",
            "ただの会社ではないんですよね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0093
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ……\x02\x03",

            "……オルランドはそこにいるか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0094
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005Fランディですか？\x01",
            "ええ、先ほど合流したので……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0095
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『クリムゾン商会』については\x01",
            "ヤツから話を聞くといい。\x02\x03",

            "──また夜にでも連絡する。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(813, 0, 80, 0)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0096
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011Fあ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(804, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)

    #C0097
    ChrTalk(
        0x102,
        "#00108F#11Pど、どうしたの？\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x105,
        (
            "#10301F#5P何やらキナ臭そうな\x01",
            "話をしてたみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x104,
        (
            "#00306F#5P──なるほどな。\x01",
            "ルバーチェの跡地を狙ったか。\x02\x03",

            "#00300F#11Pノエル、街に着いたら\x01",
            "歓楽街に寄ってくれねぇか？\x02\x03",

            "裏通りの手前まで頼む。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x109,
        "#10108F#6Pそ、それは構いませんけど……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrSubChip(0x101, 0x1)
    Sleep(200)
    SetChrSubChip(0x105, 0x0)

    #C0101
    ChrTalk(
        0x101,
        (
            "#00003F#6P……ランディ。\x02\x03",

            "#00013F『クリムゾン商会』っていうのは\x01",
            "どういう会社なんだ？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    SetChrSubChip(0x104, 0x0)
    Sleep(300)

    #C0102
    ChrTalk(
        0x104,
        (
            "#00306F#5P#30Wああ……\x02\x03",

            "#00303F高級クラブ《ノイエ＝ブラン》を\x01",
            "経営する帝国籍の会社……\x02\x03",

            "#00311Fしかしその実態は──\x01",
            "猟兵団《赤い星座》が持っている\x01",
            "資金調達用のダミー会社だ。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(14270, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopSound(460, 1000, 80)
    Sleep(1000)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    OP_24(0x323)
    SetScenarioFlags(0x22, 0)
    NewScene("r2030", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_26DA end

    def Function_9_32E6(): pass

    label("Function_9_32E6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, 151950, 100, 950, 90)
    SetChrPos(0x102, 150400, 100, -1050, 90)
    SetChrPos(0x109, 151750, 170, -1150, 90)
    SetChrPos(0x103, 150400, 100, 950, 90)
    SetChrPos(0x104, 148850, 100, -950, 90)
    SetChrPos(0x105, 148850, 100, 750, 90)
    SetMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x1, 0x9)
    OP_49()
    SetChrPos(0x9, 150000, 0, 0, 270)
    OP_D5(0x9, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFrame(0x1, "main", 0x2, "stop")
    SetMapObjFrame(0xFF, "effect00_add", 0x0, 0x1)
    VolumeBGM(0x46, 0x3E8)
    OP_68(150000, 750, 0, 0)
    MoveCamera(305, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(15000, 1500)
    OP_6F(0x79)
    OP_0D()

    #C0103
    ChrTalk(
        0x101,
        (
            "#00008F#5P今のは……\x01",
            "病院に向かう救急車か。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x103,
        (
            "#00201F#5Pええ、ウルスラ病院に\x01",
            "登録されている車両ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x104,
        "#00303F#5Pそいつが３台もか……\x02",
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x102,
        (
            "#00108F#5Pやっぱり脱線事故の怪我人を\x01",
            "搬送しているのかしら……？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x105,
        (
            "#10306F#5Pま、このタイミングだし\x01",
            "間違いないんじゃないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x101,
        (
            "#00006F#5P……セシル姉たちも\x01",
            "忙しい事になりそうだな。\x02\x03",

            "#00001F俺たちも現場へ急ごう。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x109,
        "#10101F#5P了解です！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x103, 0x4)
    SetScenarioFlags(0x162, 6)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1D), scpexpr(EXPR_PUSH_LONG, 0x21410100), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36E4")
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    VolumeBGM(0x64, 0x64)
    SetScenarioFlags(0x22, 1)
    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_372F")

    label("loc_36E4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1D), scpexpr(EXPR_PUSH_LONG, 0x21302000), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3709")
    VolumeBGM(0x64, 0x3E8)
    Sleep(1000)
    NewScene("c0200", 99, 0, 0)
    IdleLoop()
    Jump("loc_372F")

    label("loc_3709")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x1D), scpexpr(EXPR_PUSH_LONG, 0x21410000), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_372F")
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    VolumeBGM(0x64, 0x64)
    NewScene("r1000", 99, 0, 0)
    IdleLoop()

    label("loc_372F")

    Return()

    # Function_9_32E6 end

    def Function_10_3730(): pass

    label("Function_10_3730")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    OP_68(-440, 750, 140, 0)
    MoveCamera(317, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x2)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x2)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x2)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x103, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0x105, 0x1)
    ClearChrFlags(0x104, 0x1)
    ClearChrFlags(0x103, 0x1)
    SetChrPos(0x101, 1300, 100, -1900, 180)
    SetChrPos(0x102, -800, 100, -400, 180)
    SetChrPos(0x109, -800, 100, -1700, 180)
    SetChrPos(0x103, 1300, 100, -400, 180)
    SetChrPos(0x104, -800, 100, 1100, 180)
    SetChrPos(0x105, 1300, 100, 1100, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x4, 0x9)
    OP_49()
    SetChrPos(0x9, -8000, 0, 4000, 180)
    OP_D5(0x9, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFrame(0x4, "main", 0x2, "stop")
    SetMapObjFrame(0x4, "obj00", 0x2, "stop")
    SetMapObjFrame(0xFF, "effect00_add", 0x0, 0x1)
    VolumeBGM(0x46, 0x3E8)
    FadeToBright(1000, 0)
    SetCameraDistance(15000, 1500)
    OP_6F(0x79)
    OP_0D()

    #C0110
    ChrTalk(
        0x101,
        "#00001F#12P今のバスは……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x109,
        (
            "#10108F#11P共和国方面への行き来に\x01",
            "使われている旅客バスですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        (
            "#00103F#11P多分、列車に乗っていた乗客を\x01",
            "振替#4Rふりかえ#輸送しているんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x104,
        "#00306F#11Pやれやれ、大変だな。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x103,
        (
            "#00208F#12P……事故の規模は\x01",
            "どの程度なんでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(14500, 2000)
    OP_6F(0x79)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x103, 0x4)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0x109, 0x1)
    SetChrFlags(0x105, 0x1)
    SetChrFlags(0x104, 0x1)
    SetChrFlags(0x103, 0x1)
    SetScenarioFlags(0x162, 7)
    SetScenarioFlags(0x22, 0)
    NewScene("r1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_3730 end

    def Function_11_3AEE(): pass

    label("Function_11_3AEE")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    SoundLoad(468)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    OP_68(100040, 950, 320, 0)
    MoveCamera(317, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15750, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrPos(0x101, 98800, 100, 1700, 0)
    SetChrPos(0x102, 98800, 100, 100, 0)
    SetChrPos(0x109, 101000, 100, 1700, 0)
    SetChrPos(0x105, 101000, 100, -1400, 0)
    SetChrPos(0x104, 98800, 100, -1400, 0)
    SetChrPos(0x103, 101000, 100, 100, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    BeginChrThread(0x101, 3, 0, 2)
    VolumeBGM(0x46, 0x3E8)
    Sound(468, 2, 100, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(15000, 1500)
    OP_6F(0x79)
    OP_0D()

    #C0115
    ChrTalk(
        0x109,
        "#5P#10110Fこ、これは……\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x102,
        "#00106F#5P酷い……こんな事って……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x104,
        "#00311F#5P…………………………\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        (
            "#5P#00010Fくっ、とにかく状況が\x01",
            "どうなっているか確かめないと……\x02",
        )
    )

    CloseMessageWindow()
    Sound(867, 0, 60, 0)
    Sleep(300)
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("男の声")

    #A0119
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──セルゲイだ、聞こえるか。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x101, 0x2)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x102, 0x0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x103, 0x0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0120
    ChrTalk(
        0x101,
        "#5P#00007F課長……！？\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x102,
        "#5P#00101Fご無事ですか！？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("セルゲイの声")

    #A0122
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "おお、何とかな。\x02\x03",

            "警察本部が襲われたんで\x01",
            "支援課の方で各方面の連絡を\x01",
            "受け持っている状況だ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0123
    ChrTalk(
        0x101,
        "#5P#00013F警察本部が……！？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x109,
        "#6P#10107Fい、急いで行かないと……！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("セルゲイの声")

    #A0125
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "いや、そっちは既に\x01",
            "ソーニャの部隊が向かっている。\x02\x03",

            "できればお前たちは\x01",
            "港湾区の方に向かってくれ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0126
    ChrTalk(
        0x101,
        "#5P#00005F港湾区……ですか？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("セルゲイの声")

    #A0127
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "つい先ほど、猟兵の一部が\x01",
            "黒月の支社を爆破したそうだ。\x02\x03",

            "そのままＩＢＣビルに\x01",
            "乗り込んで行ったらしい。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("セルゲイの声")

    #A0128
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "現在、敵の主力部隊は\x01",
            "オルキスタワーを攻めている。\x02\x03",

            "アリオスやダドリーが\x01",
            "持ちこたえているようだが、\x01",
            "警備隊の助けは必要だろう。\x02\x03",

            "他の遊撃士たちは……\x01",
            "市街地に放たれた軍用魔獣を\x01",
            "片付けるので手一杯なようだ。\x02\x03",

            "駆けつけられるとしたら\x01",
            "お前たちしかいない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0129
    ChrTalk(
        0x102,
        "#5P#00108Fで、ですが……\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x103,
        (
            "#6P#00201F……支援課#6Rそちら#の方は\x01",
            "大丈夫なんですか？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("セルゲイの声")

    #A0131
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "通行人は可能な限り\x01",
            "支援課の中に避難させた。\x02\x03",

            "ツァイトが番をしているから\x01",
            "軍用魔獣も近寄って来ないしな。\x02\x03",

            "ちゃんとキーアもいるし、\x01",
            "まあ心配するな。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0132
    ChrTalk(
        0x103,
        "#6P#00206F……そうですか。\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x105,
        "#6P#10301F何とか大丈夫そうだね。\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        (
            "#5P#00013F──分かりました。\x01",
            "これより港湾区に向かいます。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(220, 20, -1, -1)
    SetChrName("セルゲイの声")

    #A0135
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ……\x01",
            "くれぐれも気をつけろ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(899, 0, 80, 0)
    Sleep(500)

    #C0136
    ChrTalk(
        0x105,
        (
            "#6P#10308FＩＢＣビル……\x01",
            "ミラ目当てってことかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#5P#00003F分からないけど……\x01",
            "とにかく急いだ方がよさそうだ。\x02\x03",

            "#00008F本当は襲撃されたっていう\x01",
            "警察本部も気になるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x109,
        (
            "#6P#10106F……はい………\x01",
            "でも、とにかく急ぎましょう。\x02\x03",

            "#10101FＩＢＣビルにも皆さんの\x01",
            "知り合いがいましたよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x102,
        (
            "#5P#00106Fそうね……\x01",
            "ベルがいる可能性は高いわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x103,
        (
            "#6P#00208Fヨナや主任も……\x01",
            "財団の事務所にいると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x104,
        (
            "#00303F#5P……とりあえず\x01",
            "港湾区に着いたところで\x01",
            "車は停めた方がいいだろう。\x02\x03",

            "#00301F下手に車で近付いたら\x01",
            "対戦車ミサイル#14Rパ ン ツァー フ ァ ウ ス ト#を\x01",
            "ぶっ放されるかもしれねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x101,
        "#5P#00011Fその危険もあるのか……\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x109,
        (
            "#6P#10101F了解しました。\x01",
            "港湾区の入口まで急ぎます。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)
    StopSound(468, 2000, 100)
    OP_68(100000, 850, -3500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    SetChrName("")

    #A0144
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、行政区に向かう\x01",
            "警備隊の車両と別れた後……\x02\x03",

            "ロイドたちを乗せた導力車は\x01",
            "戦闘を避けつつ、東通りを経由して\x01",
            "港湾区に到着した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x103, 0x4)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7150", "ed7544")
    OP_24(0x1D4)
    SetScenarioFlags(0x22, 2)
    NewScene("c120B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_3AEE end

    def Function_12_480E(): pass

    label("Function_12_480E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("chr/ch02902.itc", 0x22)
    LoadChrToIndex("chr/ch03102.itc", 0x23)
    LoadChrToIndex("chr/ch03202.itc", 0x24)
    LoadChrToIndex("chr/ch00902.itc", 0x25)
    OP_68(-610, 700, 50, 0)
    MoveCamera(321, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14400, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48BE")
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)

    label("loc_48BE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48D6")
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x0)

    label("loc_48D6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_48EE")
    SetChrChipByIndex(0x106, 0x24)
    SetChrSubChip(0x106, 0x0)

    label("loc_48EE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4906")
    SetChrChipByIndex(0x10A, 0x25)
    SetChrSubChip(0x10A, 0x0)

    label("loc_4906")

    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0xF4, 0x4)
    SetChrFlags(0xF5, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x103, 0x1)
    ClearChrFlags(0x104, 0x1)
    ClearChrFlags(0xF4, 0x1)
    ClearChrFlags(0xF5, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A31")
    SetChrPos(0x109, -800, 100, -1700, 180)
    SetChrPos(0x101, 1300, 100, -1900, 180)
    SetChrPos(0x103, 1300, 100, -400, 180)
    SetChrPos(0x102, -800, 100, -400, 180)
    SetChrPos(0x104, -700, 100, 1100, 180)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49CD")
    SetChrPos(0x105, 300, 100, 1100, 180)
    Jump("loc_4A14")

    label("loc_49CD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_49F3")
    SetChrPos(0x106, 200, 100, 1100, 180)
    Jump("loc_4A14")

    label("loc_49F3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A14")
    SetChrPos(0x10A, 300, 100, 1100, 180)

    label("loc_4A14")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0x101, 0x2)
    Jump("loc_4B16")

    label("loc_4A31")

    SetChrPos(0x101, -800, 100, -1700, 180)
    SetChrPos(0x102, 1300, 100, -1900, 180)
    SetChrPos(0x103, 1300, 100, -400, 180)
    SetChrPos(0x104, -800, 100, -400, 180)
    ClearScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4A9C")
    SetChrPos(0x10A, -700, 100, 1100, 180)
    SetScenarioFlags(0x0, 0)

    label("loc_4A9C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4ADD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ACC")
    SetChrPos(0x105, -700, 100, 1100, 180)
    Jump("loc_4ADD")

    label("loc_4ACC")

    SetChrPos(0x105, 300, 100, 1100, 180)

    label("loc_4ADD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4AFE")
    SetChrPos(0x106, 200, 100, 1100, 180)

    label("loc_4AFE")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0x102, 0x2)

    label("loc_4B16")

    SetMapObjFrame(0xFF, "effect00_add", 0x0, 0x1)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    VolumeBGM(0x3C, 0x3E8)
    FadeToBright(1000, 0)
    SetCameraDistance(13800, 2000)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58AA")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C46")

    #C0145
    ChrTalk(
        0x106,
        (
            "#10702F#11Pわぁ……初めて乗りますけど、\x01",
            "素敵な内装ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        "#12P#00009Fはは、サンキュ。\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x103,
        (
            "#12P#00202Fこの車、キーアも\x01",
            "お気に入りでしたよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C46")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4D22")

    #C0148
    ChrTalk(
        0x10A,
        (
            "#00605F#11Pふむ、ＺＣＦの最新導力車か。\x02\x03",

            "#00603F確かに使い勝手が良さそうだ。\x01",
            "一課での運用も考えたい所だが……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x102,
        (
            "#11P#00106F大陸全土の状況を考えると\x01",
            "リベールからの輸入も\x01",
            "難しいかもしれませんね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D22")

    OP_63(0x109, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x109)

    #C0150
    ChrTalk(
        0x109,
        (
            "#10104F#5Pうん、整備状況はいいし、\x01",
            "問題なく動かせますよ。\x02\x03",

            "#10100F確かにこの子なら強行突破も\x01",
            "難なくこなしてくれそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        "#12P#00000Fそうか……\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x103,
        (
            "#12P#00203Fこれで突入用の車輌は\x01",
            "確保できましたが……\x02\x03",

            "#00200Fいったん課長たちの所に\x01",
            "戻りましょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x102,
        (
            "#11P#00103Fそうね、最終的な段取りも\x01",
            "聞いておきたいし……\x02",
        )
    )

    CloseMessageWindow()
    Sound(867, 0, 80, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x109, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0154
    ChrTalk(
        0x101,
        "#12P#00013Fこれは……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F8A")

    #C0155
    ChrTalk(
        0x10A,
        (
            "#00601F#11P車載の通信器だ。\x01",
            "何処かからの連絡だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FC8")

    label("loc_4F8A")


    #C0156
    ChrTalk(
        0x104,
        (
            "#11P#00301F車載の通信器だな。\x01",
            "何処かからの連絡みてぇだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4FC8")


    #C0157
    ChrTalk(
        0x109,
        (
            "#10113F#5Pロ、ロイドさん。\x01",
            "どうしましょう……？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x101,
        (
            "#12P#00003Fああ……\x01",
            "ＯＮにしてみてくれ。\x02\x03",

            "#00001Fみんな、念のため\x01",
            "声は立てないよう頼む。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sleep(500)
    Sound(853, 0, 100, 0)
    Sleep(300)
    Sound(899, 0, 50, 0)
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("女性の声")

    #A0159
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──お久しぶりね。\x01",
            "特務支援課のみんな。\x02\x03",

            "キリカよ。\x01",
            "キリカ・ロウラン。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    #C0160
    ChrTalk(
        0x101,
        "#12P#00011Fええっ……！？\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x104,
        "#11P#00307Fキリカさんッスか！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5221")

    #C0162
    ChrTalk(
        0x106,
        "#10701F#11P（泰斗#4Rたい と #の《飛燕紅児#8R ひ えんこう じ #》……）\x02",
    )

    CloseMessageWindow()

    label("loc_5221")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_527C")

    #C0163
    ChrTalk(
        0x10A,
        (
            "#00601F#11Pロックスミス機関の室長……\x01",
            "まだクロスベルにいたのか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_52E7")

    label("loc_527C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_52E7")

    #C0164
    ChrTalk(
        0x105,
        (
            "#10403F#11Pカルバードの諜報機関の\x01",
            "お姉さんか……\x02\x03",

            "#10400Fまだクロスベルにいたとはね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_52E7")


    #C0165
    ChrTalk(
        0x109,
        (
            "#10101F#5Pで、でもどうして\x01",
            "こんな所に通信を……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x102,
        (
            "#11P#00101F……私たちの動きを\x01",
            "全て把握しているんですか？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("キリカの声")

    #A0167
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "この状況であなた達が\x01",
            "どう動くか予測しただけよ。\x02\x03",

            "忙しい中、時間を取らせて\x01",
            "申し訳ないのだけど……\x02\x03",

            "“情報交換”を\x01",
            "する気はないかしら？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0168
    ChrTalk(
        0x101,
        "#12P#00008Fそれは……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_54FB")

    #C0169
    ChrTalk(
        0x10A,
        (
            "#00603F#11P（……バニングス。\x01",
            "  お前が決めろ。）\x02\x03",

            "#00601F（我々一課は、彼女とのパイプを\x01",
            "  いまだ構築出来ていない。）\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        "#12P#00003F#11P（……分かりました。）\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Jump("loc_5513")

    label("loc_54FB")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    label("loc_5513")


    #C0171
    ChrTalk(
        0x101,
        (
            "#12P#00006F──了解です、キリカさん。\x02\x03",

            "#00001Fどちらに行けばいいんですか？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("キリカの声")

    #A0172
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クロスベル駅、３番ホームに\x01",
            "停車している列車の２番車輌に。\x02\x03",

            "駅に人気#4Rひと け #は無いから\x01",
            "安心するといいわ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0173
    ChrTalk(
        0x101,
        (
            "#12P#00004F分かりました。\x01",
            "３番ホームの列車の\x01",
            "２番車輌ですね。\x02\x03",

            "#00013Fところで……\x01",
            "レクターさんもそちらに？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("キリカの声")

    #A0174
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フフ、ご明察。\x01",
            "──それでは待ってるわ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(899, 0, 80, 0)
    Sleep(500)

    #C0175
    ChrTalk(
        0x103,
        (
            "#12P#00211F……相変わらず\x01",
            "千里眼みたいな人ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x102,
        (
            "#11P#00108Fしかもレクター大尉も\x01",
            "いるみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x104,
        "#11P#00306Fま、行ってみるしかねえだろ。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            "#12P#00001Fああ……\x01",
            "クロスベル駅に行こう。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x109,
        "#10101F#5P了解です！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5804")

    #C0180
    ChrTalk(
        0x106,
        (
            "#10701F#11P……もしもの時のために\x01",
            "備えはしておきましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58A5")

    label("loc_5804")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5857")

    #C0181
    ChrTalk(
        0x105,
        (
            "#10404F#11P念のため、備えだけは\x01",
            "しといた方がいいかもね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_58A5")

    label("loc_5857")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_58A5")

    #C0182
    ChrTalk(
        0x10A,
        (
            "#00603F#11P念のため、備えだけは\x01",
            "しておいた方がよかろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_58A5")

    Jump("loc_65E9")

    label("loc_58AA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5952")

    #C0183
    ChrTalk(
        0x106,
        (
            "#10702F#11Pわぁ……初めて乗りますけど、\x01",
            "素敵な内装ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x101,
        "#00009F#5Pはは、サンキュ。\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x103,
        (
            "#12P#00202Fこの車、キーアも\x01",
            "お気に入りでしたよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5952")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A5B")

    #C0186
    ChrTalk(
        0x10A,
        (
            "#11P#00605Fふむ、ＺＣＦの最新導力車か。\x02\x03",

            "#00603F確かに使い勝手が良さそうだ。\x01",
            "一課での運用も考えたい所だが……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x102,
        (
            "#12P#00106F大陸全土の状況を考えると\x01",
            "リベールからの輸入も\x01",
            "難しいかもしれませんね……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A5B")

    #C0188
    ChrTalk(
        0x105,
        "#10403Fふむ、確かにね。\x02",
    )

    CloseMessageWindow()

    label("loc_5A5B")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0189
    ChrTalk(
        0x101,
        (
            "#00004F#5P──整備状況もいいし、\x01",
            "問題なく動かせそうだな。\x02\x03",

            "#00000F実際の突入の時は\x01",
            "ノエルに運転してもらった方が\x01",
            "よさそうだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x104,
        "#11P#00302Fま、あっちはプロだからな。\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x103,
        (
            "#12P#00203Fこれで突入用の車輌は\x01",
            "確保できましたが……\x02\x03",

            "#00200Fいったん課長たちの所に\x01",
            "戻りましょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x102,
        (
            "#12P#00103Fそうね、最終的な段取りも\x01",
            "聞いておきたいし……\x02",
        )
    )

    CloseMessageWindow()
    Sound(867, 0, 80, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x101, 0x1)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0193
    ChrTalk(
        0x101,
        "#00005F#5Pこれは……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5CD9")

    #C0194
    ChrTalk(
        0x10A,
        (
            "#11P#00601F車載の通信器だ。\x01",
            "何処かからの連絡だな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D17")

    label("loc_5CD9")


    #C0195
    ChrTalk(
        0x104,
        (
            "#11P#00301F車載の通信器だな。\x01",
            "何処かからの連絡みてぇだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D17")


    #C0196
    ChrTalk(
        0x102,
        "#12P#00108F……ロイド、どうするの？\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#00006F#5Pああ……\x01",
            "とりあえずＯＮにしよう。\x02\x03",

            "#00013Fみんな、念のため\x01",
            "声は立てないよう頼む。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    Sleep(500)
    Sound(853, 0, 100, 0)
    Sleep(300)
    Sound(899, 0, 50, 0)
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("女性の声")

    #A0198
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──お久しぶりね。\x01",
            "特務支援課のみんな。\x02\x03",

            "キリカよ。\x01",
            "キリカ・ロウラン。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)

    #C0199
    ChrTalk(
        0x101,
        "#00011F#5Pええっ……！？\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x104,
        "#11P#00307Fキリカさんッスか！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5F66")

    #C0201
    ChrTalk(
        0x106,
        "#10701F#11P（泰斗#4Rたい と #の《飛燕紅児#8R ひ えんこう じ #》……）\x02",
    )

    CloseMessageWindow()

    label("loc_5F66")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5FC1")

    #C0202
    ChrTalk(
        0x10A,
        (
            "#11P#00601Fロックスミス機関の室長……\x01",
            "まだクロスベルにいたのか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_602C")

    label("loc_5FC1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_602C")

    #C0203
    ChrTalk(
        0x105,
        (
            "#11P#10403Fカルバードの諜報機関の\x01",
            "お姉さんか……\x02\x03",

            "#10400Fまだクロスベルにいたとはね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_602C")


    #C0204
    ChrTalk(
        0x102,
        (
            "#12P#00101F……私たちの動きを\x01",
            "全て把握しているんですか？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("キリカの声")

    #A0205
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "この状況であなた達が\x01",
            "どう動くか予測しただけよ。\x02\x03",

            "忙しい中、時間を取らせて\x01",
            "申し訳ないのだけど……\x02\x03",

            "“情報交換”を\x01",
            "する気はないかしら？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0206
    ChrTalk(
        0x101,
        "#00008F#5Pそれは……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6201")

    #C0207
    ChrTalk(
        0x10A,
        (
            "#11P#00603F（……バニングス。\x01",
            "  お前が決めろ。）\x02\x03",

            "#00601F（我々一課は、彼女とのパイプを\x01",
            "  いまだ構築出来ていない。）\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        "#00003F#5P（……分かりました。）\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Jump("loc_6219")

    label("loc_6201")

    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    label("loc_6219")


    #C0209
    ChrTalk(
        0x101,
        (
            "#00006F#5P──了解です、キリカさん。\x02\x03",

            "#00001Fどちらに行けばいいんですか？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("キリカの声")

    #A0210
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クロスベル駅、３番ホームに\x01",
            "停車している列車の２番車輌に。\x02\x03",

            "駅に人気#4Rひと け #は無いから\x01",
            "安心するといいわ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0211
    ChrTalk(
        0x101,
        (
            "#00004F#5P分かりました。\x01",
            "３番ホームの列車の\x01",
            "２番車輌ですね。\x02\x03",

            "#00013Fところで……\x01",
            "レクターさんもそちらに？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 150, -1, -1)
    SetChrName("キリカの声")

    #A0212
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フフ、ご明察。\x01",
            "──それでは待ってるわ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(899, 0, 80, 0)
    Sleep(500)

    #C0213
    ChrTalk(
        0x103,
        (
            "#12P#00211F……相変わらず\x01",
            "千里眼みたいな人ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x102,
        (
            "#12P#00108Fしかもレクター大尉も\x01",
            "いるみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x104,
        "#11P#00306Fま、行ってみるしかねえだろ。\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x101,
        (
            "#00001F#5Pああ……\x01",
            "クロスベル駅に行こう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_64C6")

    #C0217
    ChrTalk(
        0x10A,
        "#11P#00603F了解だ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_64F3")

    label("loc_64C6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_64F3")

    #C0218
    ChrTalk(
        0x105,
        "#11P#10404Fフフ、了解。\x02",
    )

    CloseMessageWindow()

    label("loc_64F3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6548")

    #C0219
    ChrTalk(
        0x106,
        (
            "#10701F#11P……もしもの時のために\x01",
            "備えはしておきましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65E9")

    label("loc_6548")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_659B")

    #C0220
    ChrTalk(
        0x105,
        (
            "#10402F#11P念のため、備えだけは\x01",
            "しといた方がいいかもね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_65E9")

    label("loc_659B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_65E9")

    #C0221
    ChrTalk(
        0x10A,
        (
            "#00601F#11P念のため、備えだけは\x01",
            "しておいた方がよかろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_65E9")

    FadeToDark(1000, 0, -1)
    SetCameraDistance(14300, 2000)
    OP_6F(0x79)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0xFF)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0xFF)
    SetChrSubChip(0xF5, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0xF4, 0x4)
    ClearChrFlags(0xF5, 0x4)
    SetChrFlags(0x101, 0x1)
    SetChrFlags(0x102, 0x1)
    SetChrFlags(0x103, 0x1)
    SetChrFlags(0x104, 0x1)
    SetChrFlags(0xF4, 0x1)
    SetChrFlags(0xF5, 0x1)
    OP_37()
    SetScenarioFlags(0x1A5, 5)
    OP_29(0xB1, 0x1, 0x8)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7573", 0)
    EventEnd(0x5)
    NewScene("c0200", 113, 0, 0)
    IdleLoop()
    Return()

    # Function_12_480E end

    def Function_13_668E(): pass

    label("Function_13_668E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 15)
    BeginChrThread(0x101, 3, 0, 2)
    SoundLoad(468)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    Sound(468, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x178, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_67E1")

    #C0222
    ChrTalk(
        0x103,
        "#00211F離されてしまいましたね……\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x102,
        (
            "#00106Fま、まあ\x01",
            "安全に越したことは\x01",
            "ないと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x109,
        "#10106F（う～…………）\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x101,
        (
            "#00003F（判断ミスだったか……？）\x02\x03",

            "#00007F……と、とにかく追跡を続けるぞ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6919")

    label("loc_67E1")


    #C0226
    ChrTalk(
        0x103,
        (
            "#00205F雨で道路の状況も悪いのに、\x01",
            "こんなスピードでカーブするなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x102,
        (
            "#00109Fで、でもちょっと\x01",
            "危なくないかしら……？\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x109,
        (
            "#10102Fフフ、この程度なら\x01",
            "朝飯前ですっ！\x02\x03",

            "#10107F暴走車……\x01",
            "絶対に逃がしませんよ！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0229
    ChrTalk(
        0x101,
        "#00012Fな、なんだかノッてるなあ……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x0)

    #C0230
    ChrTalk(
        0x101,
        (
            "#00001F……と、とにかく\x01",
            "追跡を続けるぞ！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_6919")

    Sound(494, 0, 70, 0)
    OP_68(101440, 650, -16510, 3000)
    MoveCamera(311, 29, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(11280, 3000)
    Sleep(1000)
    StopSound(468, 1000, 100)
    StopSound(494, 1000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearScenarioFlags(0x178, 5)
    SetScenarioFlags(0x22, 5)
    NewScene("r1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_13_668E end

    def Function_14_6995(): pass

    label("Function_14_6995")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 15)
    BeginChrThread(0x101, 3, 0, 2)
    SoundLoad(468)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    Sound(468, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0231
    ChrTalk(
        0x109,
        (
            "#10110Fくっ……\x01",
            "彼らもなかなかやりますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        (
            "#00003Fああ……\x02\x03",

            "#00000Fだが、このままいけば\x01",
            "西口に待機している広域防犯課と\x01",
            "うまく挟み撃ちできそうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(100)

    #C0233
    ChrTalk(
        0x105,
        (
            "#10305Fん……？\x02\x03",

            "あの車、なんだか\x01",
            "様子がおかしくない？\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x101,
        "#00005Fえ……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    StopSound(468, 500, 100)
    SetScenarioFlags(0x22, 6)
    NewScene("r1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_6995 end

    def Function_15_6B1E(): pass

    label("Function_15_6B1E")

    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    OP_68(100490, 650, -450, 0)
    MoveCamera(311, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13160, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x103, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0x105, 0x1)
    ClearChrFlags(0x104, 0x1)
    ClearChrFlags(0x103, 0x1)
    SetChrPos(0x101, 99000, 100, 1600, 0)
    SetChrPos(0x102, 99000, 100, 40, 0)
    SetChrPos(0x109, 101100, 100, 1600, 0)
    SetChrPos(0x105, 101100, 100, 40, 0)
    SetChrPos(0x104, 99000, 100, -1420, 0)
    SetChrPos(0x103, 101100, 100, -1420, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Return()

    # Function_15_6B1E end

    def Function_16_6C57(): pass

    label("Function_16_6C57")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("apl/ch51104.itc", 0x20)
    LoadChrToIndex("chr/ch03002.itc", 0x21)
    LoadChrToIndex("chr/ch00302.itc", 0x22)
    LoadChrToIndex("chr/ch00202.itc", 0x23)
    SoundLoad(468)
    SoundLoad(469)
    OP_68(-500, 650, 500, 0)
    MoveCamera(324, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13750, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    EndChrThread(0x101, 0x0)
    SetChrBattleFlags(0x101, 0x4)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    EndChrThread(0x102, 0x0)
    SetChrBattleFlags(0x102, 0x4)
    SetChrChipByIndex(0x109, 0x20)
    SetChrSubChip(0x109, 0x0)
    EndChrThread(0x109, 0x0)
    SetChrBattleFlags(0x109, 0x4)
    SetChrChipByIndex(0x105, 0x21)
    SetChrSubChip(0x105, 0x0)
    EndChrThread(0x105, 0x0)
    SetChrBattleFlags(0x105, 0x4)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    EndChrThread(0x104, 0x0)
    SetChrBattleFlags(0x104, 0x4)
    SetChrChipByIndex(0x103, 0x23)
    SetChrSubChip(0x103, 0x0)
    EndChrThread(0x103, 0x0)
    SetChrBattleFlags(0x103, 0x4)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x103, 0x4)
    ClearChrFlags(0x101, 0x1)
    ClearChrFlags(0x102, 0x1)
    ClearChrFlags(0x109, 0x1)
    ClearChrFlags(0x105, 0x1)
    ClearChrFlags(0x104, 0x1)
    ClearChrFlags(0x103, 0x1)
    SetChrPos(0x101, 1300, 100, -1900, 180)
    SetChrPos(0x102, -800, 100, -400, 180)
    SetChrPos(0x109, -800, 100, -1700, 180)
    SetChrPos(0x105, 1300, 100, -400, 180)
    SetChrPos(0x104, -800, 100, 1100, 180)
    SetChrPos(0x103, 1300, 100, 1100, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xFF, "side01", 0x0, 0x1)
    Sound(468, 2, 100, 0)
    Sound(469, 2, 60, 0)
    BeginChrThread(0x101, 3, 0, 2)
    FadeToBright(1000, 0)
    OP_0D()

    #C0235
    ChrTalk(
        0x101,
        (
            "#00010Fくそっ、手榴弾でけん制されて\x01",
            "なかなか近づけない……\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x109,
        (
            "#10106Fうう、クルマの性能では\x01",
            "負けてないんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x103,
        (
            "#00201F……このまま共和国のアルタイル市に\x01",
            "入られると面倒そうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x102,
        (
            "#00103Fそうなったら、\x01",
            "逮捕はほぼ不可能とみて\x01",
            "いいでしょうね……\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x104,
        "#00310Fちっ……マズそうだな。\x02",
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x101,
        (
            "#00001Fとにかく……\x01",
            "諦めずに追うしかない！\x02\x03",

            "#00007F頼むノエル！\x01",
            "振り切られないように\x01",
            "しっかりついていってくれ！\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x109,
        "#10107Fイエス・サー！\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0242
    ChrTalk(
        0x105,
        "#10305F……おや……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopSound(468, 300, 90)
    StopSound(469, 300, 50)
    SetScenarioFlags(0x22, 3)
    NewScene("e4101", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_6C57 end

    SaveToFile()

Try(main)
