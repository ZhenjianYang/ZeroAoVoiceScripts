from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1120.bin",                # FileName
        "c1120",                    # MapName
        "c1120",                    # Location
        0x0017,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 23, 0, 1, 0, 2],
    )

    BuildStringList((
        "c1120",                  # 0
        "キーア",                 # 1
        "セルゲイ課長",           # 2
        "ダドリー捜査官",         # 3
        "ノエル曹長",             # 4
        "ソーニャ副司令",         # 5
        "グレイス",               # 6
        "マクダエル市長",         # 7
        "マリアベル",             # 8
        "ディーター総裁",         # 9
        "イアン弁護士",           # 10
        "ワジ",                   # 11
        "セシル",                 # 12
        "ハルトマン議長",         # 13
        "アリオス",               # 14
        "エマ捜査官",             # 15
        "カメラマン",             # 16
        "開会式客",               # 17
        "開会式客",               # 18
        "開会式客",               # 19
        "開会式客",               # 20
        "開会式客",               # 21
        "開会式客",               # 22
        "開会式客",               # 23
        "開会式客",               # 24
        "開会式客",               # 25
        "開会式客",               # 26
        "開会式客",               # 27
        "受付嬢レベッカ",         # 28
        "受付嬢フラン",           # 29
        "ドノバン警部",           # 30
        "レイモンド捜査官",       # 31
        "フランツ巡査",           # 32
        "ジョーリッジ課長",       # 33
        "ケイト巡査",             # 34
        "ヘルマー",               # 35
        "モルス会長",             # 36
        "ピエール副局長",         # 37
        "イリア",                 # 38
        "リーシャ",               # 39
        "ハロルド",               # 40
        "ウェンディ",             # 41
        "マイルズ",               # 42
        "レイテ",                 # 43
        "オスカー",               # 44
        "ヨナ",                   # 45
        "ロバーツ主任",           # 46
        "ツァイト",               # 47
        "SE制御",                 # 48
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ScpFunction((
        "Function_0_678",          # 00, 0
        "Function_1_70D",          # 01, 1
        "Function_2_75A",          # 02, 2
        "Function_3_789",          # 03, 3
        "Function_4_842",          # 04, 4
        "Function_5_8FB",          # 05, 5
        "Function_6_131F",         # 06, 6
        "Function_7_1369",         # 07, 7
        "Function_8_22F3",         # 08, 8
        "Function_9_250D",         # 09, 9
        "Function_10_251C",        # 0A, 10
    ))


    def Function_0_678(): pass

    label("Function_0_678")

    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4B), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_69B")
    Sleep(600)
    Jump("loc_6C4")

    label("loc_69B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6B2")
    Sleep(400)
    Jump("loc_6C4")

    label("loc_6B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6C4")
    Sleep(200)

    label("loc_6C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_70C")
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    Jump("loc_6C4")

    label("loc_70C")

    Return()

    # Function_0_678 end

    def Function_1_70D(): pass

    label("Function_1_70D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_721")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 7)
    Jump("loc_759")

    label("loc_721")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_735")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 5)
    Jump("loc_759")

    label("loc_735")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_759")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAD, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_759")
    Event(0, 10)

    label("loc_759")

    Return()

    # Function_1_70D end

    def Function_2_75A(): pass

    label("Function_2_75A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x86, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_776")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_788")

    label("loc_776")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE6, 4)), scpexpr(EXPR_END)), "loc_788")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_788")

    Return()

    # Function_2_75A end

    def Function_3_789(): pass

    label("Function_3_789")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_841")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7B7")
    Sleep(500)
    Jump("loc_7FF")

    label("loc_7B7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7CE")
    Sleep(200)
    Jump("loc_7FF")

    label("loc_7CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7E5")
    Sleep(300)
    Jump("loc_7FF")

    label("loc_7E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7FC")
    Sleep(400)
    Jump("loc_7FF")

    label("loc_7FC")

    Sleep(600)

    label("loc_7FF")

    PlayEffect(0x0, 0xFF, 0xFE, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 80, 0)
    Jump("Function_3_789")

    label("loc_841")

    Return()

    # Function_3_789 end

    def Function_4_842(): pass

    label("Function_4_842")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8FA")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_870")
    Sleep(500)
    Jump("loc_8B8")

    label("loc_870")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_887")
    Sleep(1000)
    Jump("loc_8B8")

    label("loc_887")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_89E")
    Sleep(1500)
    Jump("loc_8B8")

    label("loc_89E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8B5")
    Sleep(2000)
    Jump("loc_8B8")

    label("loc_8B5")

    Sleep(2500)

    label("loc_8B8")

    PlayEffect(0x0, 0xFF, 0xFE, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 80, 0)
    Jump("Function_4_842")

    label("loc_8FA")

    Return()

    # Function_4_842 end

    def Function_5_8FB(): pass

    label("Function_5_8FB")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event\\eva02_00.eff")
    LoadChrToIndex("chr/ch05800.itc", 0x1E)
    LoadChrToIndex("chr/ch06500.itc", 0x1F)
    LoadChrToIndex("chr/ch05502.itc", 0x20)
    LoadChrToIndex("chr/ch05602.itc", 0x21)
    LoadChrToIndex("chr/ch05902.itc", 0x22)
    LoadChrToIndex("chr/ch06000.itc", 0x23)
    LoadChrToIndex("apl/ch50301.itc", 0x24)
    LoadChrToIndex("apl/ch50314.itc", 0x25)
    LoadChrToIndex("chr/ch07702.itc", 0x26)
    LoadChrToIndex("chr/ch27602.itc", 0x27)
    LoadChrToIndex("chr/ch27702.itc", 0x28)
    LoadChrToIndex("chr/ch27802.itc", 0x29)
    LoadChrToIndex("chr/ch27902.itc", 0x2A)
    LoadChrToIndex("chr/ch28102.itc", 0x2B)
    LoadChrToIndex("chr/ch28202.itc", 0x2C)
    SoundLoad(883)
    SetChrFlags(0xE, 0x4)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrPos(0xE, -1460, 1100, 14620, 180)
    SetChrChipByIndex(0x14, 0x1F)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrPos(0x14, 660, 750, 16490, 183)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x22)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, -6600, 0, 9400, 55)
    SetChrFlags(0x17, 0x4)
    SetChrChipByIndex(0x17, 0x25)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrPos(0x17, -5600, 0, 9300, 55)
    OP_68(-800, 1500, 11800, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(26000, 0)
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
            "#1K創立記念祭　初日\x02",
        )
    )

    Sleep(3000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    Sleep(500)
    BeginChrThread(0x37, 0, 0, 6)
    Sleep(3000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("威厳のある声")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "──このクロスベルが\x01",
            "自治州として成立して７０年。\x02",
        )
    )

    CloseMessageWindow()

    #A0003
    AnonymousTalk(
        0xFF,
        (
            "その７０年間はまさに\x01",
            "激動の時代と共に在りました。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrChipByIndex(0x18, 0x27)
    SetChrChipByIndex(0x19, 0x28)
    SetChrChipByIndex(0x1A, 0x29)
    SetChrChipByIndex(0x1B, 0x2A)
    SetChrChipByIndex(0x1C, 0x2B)
    SetChrChipByIndex(0x1D, 0x2C)
    SetChrChipByIndex(0x1E, 0x27)
    SetChrChipByIndex(0x1F, 0x28)
    SetChrChipByIndex(0x20, 0x2A)
    SetChrChipByIndex(0x21, 0x2B)
    SetChrChipByIndex(0x22, 0x29)
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x19, 0x0)
    SetChrSubChip(0x1A, 0x0)
    SetChrSubChip(0x1B, 0x0)
    SetChrSubChip(0x1C, 0x0)
    SetChrSubChip(0x1D, 0x0)
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    SetChrSubChip(0x20, 0x0)
    SetChrSubChip(0x21, 0x0)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x8000)
    SetChrFlags(0x18, 0x4)
    SetChrFlags(0x19, 0x4)
    SetChrFlags(0x1A, 0x4)
    SetChrFlags(0x1B, 0x4)
    SetChrFlags(0x1C, 0x4)
    SetChrFlags(0x1D, 0x4)
    SetChrFlags(0x1E, 0x4)
    SetChrFlags(0x1F, 0x4)
    SetChrFlags(0x20, 0x4)
    SetChrFlags(0x21, 0x4)
    SetChrFlags(0x22, 0x4)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrChipByIndex(0x102, 0x26)
    SetChrSubChip(0x102, 0x0)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, -5800, 50, 7500, 0)
    SetChrPos(0xF, -4000, 50, 7500, 0)
    SetChrPos(0x10, -2300, 100, 7500, 0)
    SetChrPos(0x18, -500, 100, 7500, 0)
    SetChrPos(0x19, 1300, 50, 7500, 0)
    SetChrPos(0x11, 2900, 100, 7500, 0)
    SetChrPos(0x1A, -5800, 100, 5000, 0)
    SetChrPos(0x1B, -4000, 50, 5000, 0)
    SetChrPos(0x1C, -2300, 50, 5000, 0)
    SetChrPos(0x1D, -500, 50, 5000, 0)
    SetChrPos(0x1E, 1300, 100, 5000, 0)
    SetChrPos(0x1F, 2900, 100, 5000, 0)
    SetChrPos(0x20, -5800, 50, 2500, 0)
    SetChrPos(0x21, -4000, 50, 2500, 0)
    SetChrPos(0x22, -2400, 100, 2500, 0)
    OP_68(-1450, 2250, 14880, 0)
    MoveCamera(1, 11, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(18000, 0)
    OP_6E(460, 3000)
    BeginChrThread(0x17, 0, 0, 4)
    FadeToBright(2000, 0)
    Sleep(3000)
    Sleep(500)

    #C0004
    ChrTalk(
        0xE,
        (
            "#2503F#5P幾たびの戦乱、そして導力革命……\x02\x03",

            "近代化という荒波に揉まれながら\x01",
            "今やクロスベルは、大陸有数の貿易都市、\x01",
            "そして金融センターへと発展しつつあります。\x02\x03",

            "#2500Fまた、一昨年リベールにおいて締結された\x01",
            "《不戦条約》の影響もあってか\x01",
            "緊迫していた情勢も大幅に緩和されました。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(-2400, 2500, 9100, 0)
    MoveCamera(59, 14, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(15500, 0)
    OP_68(-2400, 860, 9100, 6000)
    MoveCamera(59, 19, 0, 6000)
    OP_6E(580, 6000)
    SetCameraDistance(15500, 6000)
    OP_0D()

    #C0005
    ChrTalk(
        0xE,
        (
            "#2503F#Nその一方で、急速な都市開発や\x01",
            "人口増加に起因する問題も出始めており、\x01",
            "新たな政策と法整備が求められています。\x02\x03",

            "#2501F自治州および、その周辺諸国に\x01",
            "より良き未来をもたらすためにも……\x02\x03",

            "今こそ我々は、一丸となって力を合わせ、\x01",
            "前に進む必要があるでしょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(-1550, 2080, 11590, 0)
    MoveCamera(31, 12, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(22000, 0)
    OP_68(-1550, 2080, 11590, 10000)
    MoveCamera(31, 15, 0, 10000)
    OP_6E(420, 10000)
    SetCameraDistance(23000, 10000)
    SetChrPos(0x20, -500, 0, 2400, 0)
    SetChrPos(0x21, 1300, 0, 2400, 0)
    SetChrPos(0x22, 2900, 0, 2400, 0)
    OP_0D()

    #C0006
    ChrTalk(
        0xE,
        (
            "#2509F──ですが今はただ、\x01",
            "７０年という長く大きな節目を祝い、\x01",
            "喜びを分かち合う事にしましょう。\x02\x03",

            "わずか５日間ではありますが\x01",
            "今年は例年を遥かに超える観光客が訪れ、\x01",
            "かつてない賑わいを見せております。\x02\x03",

            "かのアルカンシェルの新作を始め、\x01",
            "多くの催しやイベントも企画されており、\x01",
            "必ずや充実した５日間となるでしょう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    PlayBGM("ed7104", 0)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    BeginChrThread(0x17, 0, 0, 3)
    Sleep(1000)

    #C0007
    ChrTalk(
        0xE,
        (
            "#2503F──大いなる女神#4Rエイドス#の御名の下……\x02\x03",

            "#2507F今ここに、クロスベル自治州\x01",
            "創立７０周年記念祭の開催を宣言します！\x02",
        )
    )

    CloseMessageWindow()
    Sound(884, 0, 100, 0)
    Sleep(1000)
    OP_24(0x373)
    EndChrThread(0x37, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x17, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    Sleep(2000)
    ReplaceBGM("ed7100", "ed7106")
    ReplaceBGM("ed7101", "ed7106")
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x373)
    SetScenarioFlags(0x5C, 0)
    NewScene("c110C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_8FB end

    def Function_6_131F(): pass

    label("Function_6_131F")

    Sound(883, 2, 0, 0)
    OP_25(0x373, 0xA)
    Sleep(200)
    OP_25(0x373, 0x14)
    Sleep(200)
    OP_25(0x373, 0x1E)
    Sleep(200)
    OP_25(0x373, 0x28)
    Sleep(200)
    OP_25(0x373, 0x32)
    Sleep(200)
    OP_25(0x373, 0x3C)
    Sleep(200)
    OP_25(0x373, 0x46)
    Sleep(200)
    OP_25(0x373, 0x50)
    Sleep(200)
    OP_25(0x373, 0x5A)
    Sleep(200)
    OP_25(0x373, 0x64)
    Return()

    # Function_6_131F end

    def Function_7_1369(): pass

    label("Function_7_1369")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05800.itc", 0x1E)
    LoadChrToIndex("chr/ch08200.itc", 0x1F)
    LoadChrToIndex("chr/ch05500.itc", 0x20)
    LoadChrToIndex("chr/ch05600.itc", 0x21)
    LoadChrToIndex("chr/ch05900.itc", 0x22)
    LoadChrToIndex("chr/ch06000.itc", 0x23)
    LoadChrToIndex("chr/ch02500.itc", 0x24)
    LoadChrToIndex("chr/ch00800.itc", 0x25)
    LoadChrToIndex("chr/ch05700.itc", 0x26)
    LoadChrToIndex("chr/ch00400.itc", 0x27)
    LoadChrToIndex("chr/ch07500.itc", 0x28)
    LoadChrToIndex("apl/ch50314.itc", 0x29)
    LoadChrToIndex("chr/ch00900.itc", 0x2A)
    LoadChrToIndex("chr/ch06900.itc", 0x2B)
    LoadChrToIndex("chr/ch30200.itc", 0x2C)
    LoadChrToIndex("chr/ch30300.itc", 0x2D)
    LoadChrToIndex("chr/ch30400.itc", 0x2E)
    LoadChrToIndex("chr/ch30500.itc", 0x2F)
    LoadChrToIndex("chr/ch30000.itc", 0x30)
    LoadChrToIndex("chr/ch30100.itc", 0x31)
    LoadChrToIndex("chr/ch25800.itc", 0x32)
    LoadChrToIndex("chr/ch30600.itc", 0x33)
    LoadChrToIndex("chr/ch29300.itc", 0x34)
    LoadChrToIndex("chr/ch20200.itc", 0x35)
    LoadChrToIndex("chr/ch10300.itc", 0x36)
    LoadChrToIndex("apl/ch50560.itc", 0x37)
    LoadChrToIndex("apl/ch50562.itc", 0x38)
    LoadChrToIndex("chr/ch07000.itc", 0x39)
    LoadChrToIndex("chr/ch26100.itc", 0x3A)
    LoadChrToIndex("chr/ch06100.itc", 0x3B)
    LoadChrToIndex("chr/ch20800.itc", 0x3C)
    LoadChrToIndex("chr/ch05100.itc", 0x3D)
    LoadChrToIndex("chr/ch05200.itc", 0x3E)
    LoadChrToIndex("apl/ch50518.itc", 0x3F)
    LoadChrToIndex("chr/ch09300.itc", 0x40)
    LoadChrToIndex("chr/ch06400.itc", 0x41)
    LoadEffect(0x0, "event\\eva02_00.eff")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis106.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis107.itp")
    SetChrPos(0x101, -1500, 0, -3000, 0)
    SetChrPos(0x102, -1500, 0, -4300, 0)
    SetChrPos(0x103, -1500, 0, -5600, 0)
    SetChrPos(0x104, -1500, 0, -6900, 0)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x101, 0x40)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x103, 0x40)
    SetChrFlags(0x104, 0x40)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -1500, 750, 13700, 180)
    SetChrChipByIndex(0x2A, 0x32)
    SetChrSubChip(0x2A, 0x0)
    ClearChrFlags(0x2A, 0x80)
    ClearChrBattleFlags(0x2A, 0x8000)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, -2500, 750, 15100, 180)
    SetChrChipByIndex(0xD, 0x23)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -6200, 0, 9400, 90)

    def lambda_15B7():

        label("loc_15B7")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_15B7")

    QueueWorkItem2(0xD, 2, lambda_15B7)
    SetChrChipByIndex(0x17, 0x29)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -5200, 0, 9400, 90)

    def lambda_15F1():

        label("loc_15F1")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_15F1")

    QueueWorkItem2(0x17, 2, lambda_15F1)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    SetChrPos(0x10, 0, 0, 7000, 0)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetChrPos(0xF, 1100, 0, 7000, 0)
    SetChrChipByIndex(0x2B, 0x3C)
    SetChrSubChip(0x2B, 0x0)
    ClearChrFlags(0x2B, 0x80)
    ClearChrBattleFlags(0x2B, 0x8000)
    SetChrPos(0x2B, 2200, 0, 7000, 0)
    SetChrChipByIndex(0x9, 0x24)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, -3000, 0, 7000, 0)
    SetChrChipByIndex(0xA, 0x2A)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, -4100, 0, 7000, 0)
    SetChrChipByIndex(0x2C, 0x41)
    SetChrSubChip(0x2C, 0x0)
    ClearChrFlags(0x2C, 0x80)
    ClearChrBattleFlags(0x2C, 0x8000)
    SetChrPos(0x2C, -5200, 0, 7000, 0)
    SetChrChipByIndex(0xC, 0x26)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, 5700, 0)
    SetChrChipByIndex(0xB, 0x25)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0xB, 1100, 0, 5700, 0)
    SetChrChipByIndex(0x2D, 0x3D)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2D, 0x80)
    ClearChrBattleFlags(0x2D, 0x8000)
    SetChrPos(0x2D, 2200, 0, 5700, 0)
    SetChrChipByIndex(0x25, 0x2D)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    SetChrPos(0x25, -3000, 0, 5700, 0)
    SetChrChipByIndex(0x26, 0x2C)
    SetChrSubChip(0x26, 0x0)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrPos(0x26, -4100, 0, 5700, 0)
    SetChrChipByIndex(0x16, 0x2F)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrPos(0x16, -5200, 0, 5700, 0)
    SetChrChipByIndex(0x24, 0x2B)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrPos(0x24, 0, 0, 4400, 0)
    SetChrChipByIndex(0x23, 0x2E)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    SetChrPos(0x23, 1100, 0, 4400, 0)
    SetChrChipByIndex(0x2E, 0x3E)
    SetChrSubChip(0x2E, 0x0)
    ClearChrFlags(0x2E, 0x80)
    ClearChrBattleFlags(0x2E, 0x8000)
    SetChrPos(0x2E, 2200, 0, 4400, 0)
    SetChrChipByIndex(0x28, 0x31)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    ClearChrBattleFlags(0x28, 0x8000)
    SetChrPos(0x28, -3000, 0, 4400, 0)
    SetChrChipByIndex(0x29, 0x33)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    ClearChrBattleFlags(0x29, 0x8000)
    SetChrPos(0x29, -4100, 0, 4400, 0)
    SetChrChipByIndex(0x27, 0x30)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    SetChrPos(0x27, -5200, 0, 4400, 0)
    SetChrChipByIndex(0x11, 0x22)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    SetChrPos(0x11, 0, 0, 3100, 0)
    SetChrChipByIndex(0x2F, 0x40)
    SetChrSubChip(0x2F, 0x0)
    ClearChrFlags(0x2F, 0x80)
    ClearChrBattleFlags(0x2F, 0x8000)
    SetChrPos(0x2F, 1100, 0, 3100, 0)
    SetChrChipByIndex(0x12, 0x27)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrPos(0x12, 2200, 0, 3100, 0)
    SetChrChipByIndex(0x32, 0x36)
    SetChrSubChip(0x32, 0x0)
    ClearChrFlags(0x32, 0x80)
    ClearChrBattleFlags(0x32, 0x8000)
    SetChrPos(0x32, -3000, 0, 3100, 0)
    SetChrChipByIndex(0x31, 0x35)
    SetChrSubChip(0x31, 0x0)
    ClearChrFlags(0x31, 0x80)
    ClearChrBattleFlags(0x31, 0x8000)
    SetChrPos(0x31, -4100, 0, 3100, 0)
    SetChrChipByIndex(0x30, 0x3A)
    SetChrSubChip(0x30, 0x0)
    ClearChrFlags(0x30, 0x80)
    ClearChrBattleFlags(0x30, 0x8000)
    SetChrPos(0x30, -5200, 0, 3100, 0)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, 1800, 0)
    SetChrChipByIndex(0x13, 0x28)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrPos(0x13, 1100, 0, 1800, 0)
    SetChrChipByIndex(0x36, 0x3F)
    SetChrSubChip(0x36, 0x1)
    ClearChrFlags(0x36, 0x80)
    ClearChrBattleFlags(0x36, 0x8000)
    SetChrPos(0x36, 2200, 0, 1800, 270)
    SetChrChipByIndex(0x35, 0x34)
    SetChrSubChip(0x35, 0x0)
    ClearChrFlags(0x35, 0x80)
    ClearChrBattleFlags(0x35, 0x8000)
    SetChrPos(0x35, -3000, 0, 1800, 0)
    SetChrChipByIndex(0x34, 0x3B)
    SetChrSubChip(0x34, 0x0)
    ClearChrFlags(0x34, 0x80)
    ClearChrBattleFlags(0x34, 0x8000)
    SetChrPos(0x34, -4100, 0, 1800, 0)
    SetChrChipByIndex(0x33, 0x39)
    SetChrSubChip(0x33, 0x0)
    ClearChrFlags(0x33, 0x80)
    ClearChrBattleFlags(0x33, 0x8000)
    SetChrPos(0x33, -5200, 0, 1800, 0)
    SetMapObjFrame(0xFF, "model05", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model06", 0x0, 0x1)
    Sleep(1000)
    PlayBGM("ed7528", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x210), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_C7(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#30W──クロスベルに恐るべき混乱を\x01",
            "引き起こした《Ｄ∴Ｇ教団》の存在。\x02\x03",

            "それに利用されたマフィアと\x01",
            "薬物によって操られていた警備隊。\x02\x03",

            "そしてハルトマン議長を始めとする\x01",
            "数々の有力者たちの不始末……\x02\x03",

            "──事件の概要は、\x01",
            "クロスベルタイムズによって報じられ、\x01",
            "前代未聞の大スキャンダルへと発展した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)
    OP_C9(0x0, 0x3, 0xFFAAAAAA, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#30Wここに至ってマクダエル市長は\x01",
            "警察局長、警備隊司令両名を解任──\x02\x03",

            "各課の責任者やソーニャ副司令に\x01",
            "事件の徹底究明を命じた。\x02\x03",

            "ダドリー捜査官を始め、今まで上層部に\x01",
            "押さえつけられていた捜査官たちによって\x01",
            "帝国派議員のみならず、共和国派議員にも及ぶ\x01",
            "《教団》とのコネクションが洗い出され……\x02\x03",

            "何名もの逮捕者が出るに至って、\x01",
            "クロスベル政界に対する\x01",
            "市民の不信感は頂点へと達した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(500)
    OP_C9(0x1, 0x3, 0xFFAAAAAA, 0x320, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x0, 0x0)

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#30Wそんな中、ＩＢＣのディーター総裁が\x01",
            "次期市長選挙の出馬を電撃表明し……\x02\x03",

            "引退するマクダエル市長の理念を継いで\x01",
            "健全な政治体制の確立を公約に掲げた。\x02\x03",

            "そしてマクダエル市長もまた\x01",
            "逮捕された議員たちの\x01",
            "補欠選挙への出馬を表明し……\x02\x03",

            "早くも次の議長候補として\x01",
            "各方面から期待されているという。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(500)

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#30Wそして事件から１ヶ月後──\x02\x03",

            "そのマクダエル市長によって\x01",
            "俺たちは市庁舎のホールに呼ばれた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C7(0x1, 0x800)
    OP_68(-1500, 1300, 3000, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(12500, 0)

    def lambda_1F44():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1F44)

    def lambda_1F51():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1F51)

    def lambda_1F5E():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_1F5E)

    def lambda_1F6B():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1F6B)

    def lambda_1F78():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1F78)

    def lambda_1F85():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_1F85)

    def lambda_1F92():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1F92)

    def lambda_1F9F():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1F9F)

    def lambda_1FAC():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_1FAC)

    def lambda_1FB9():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_1FB9)

    def lambda_1FC6():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_1FC6)

    def lambda_1FD3():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_1FD3)

    def lambda_1FE0():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_1FE0)

    def lambda_1FED():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_1FED)

    def lambda_1FFA():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_1FFA)

    def lambda_2007():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_2007)

    def lambda_2014():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_2014)

    def lambda_2021():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_2021)

    def lambda_202E():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_202E)

    def lambda_203B():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x2F, 2, lambda_203B)

    def lambda_2048():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_2048)

    def lambda_2055():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x32, 2, lambda_2055)

    def lambda_2062():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_2062)

    def lambda_206F():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x30, 2, lambda_206F)

    def lambda_207C():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_207C)

    def lambda_2089():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_2089)
    BeginChrThread(0x36, 0, 0, 9)

    def lambda_209C():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x35, 2, lambda_209C)

    def lambda_20A9():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x34, 2, lambda_20A9)

    def lambda_20B6():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x33, 2, lambda_20B6)
    BeginChrThread(0x8, 3, 0, 8)

    def lambda_20C9():
        OP_96(0xFE, 0xFFFFFA24, 0x2EE, 0x2DB4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20C9)
    Sleep(50)

    def lambda_20E6():
        OP_96(0xFE, 0xFFFFFA24, 0x2EE, 0x2DB4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_20E6)
    Sleep(50)

    def lambda_2103():
        OP_96(0xFE, 0xFFFFFA24, 0x2EE, 0x2DB4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2103)
    Sleep(50)

    def lambda_2120():
        OP_96(0xFE, 0xFFFFFA24, 0x2EE, 0x2DB4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2120)
    BeginChrThread(0x17, 0, 0, 4)
    SetCameraDistance(11000, 3000)
    FadeToBright(2000, 0)
    Sleep(1500)
    OP_6F(0x10)
    Fade(1000)
    OP_68(-1500, 1000, 3000, 0)
    MoveCamera(35, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    OP_68(-1500, 1000, 7000, 6000)
    SetCameraDistance(19500, 6000)
    WaitChrThread(0x101, 1)
    OP_6F(0x79)
    Fade(1000)
    OP_68(-1500, 1450, 13100, 0)
    MoveCamera(47, 29, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, -2000, 750, 11700, 0)
    SetChrPos(0x102, -1000, 750, 11700, 0)
    SetChrPos(0x103, -3000, 750, 11700, 0)
    SetChrPos(0x104, 0, 750, 11700, 0)
    MoveCamera(42, 25, 0, 5000)
    SetCameraDistance(19000, 5000)
    OP_0D()
    Sleep(500)

    def lambda_2251():
        OP_96(0xFE, 0xFFFFFA24, 0x2EE, 0x3138, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2251)
    WaitChrThread(0x101, 1)
    Fade(250)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x38)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x37)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)
    Fade(250)
    SetChrSubChip(0xE, 0x1)
    SetChrSubChip(0x101, 0x1)
    OP_0D()
    EndChrThread(0x17, 0x0)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x40)
    ClearChrFlags(0x102, 0x40)
    ClearChrFlags(0x103, 0x40)
    ClearChrFlags(0x104, 0x40)
    OP_CA(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x210), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("t3510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1369 end

    def Function_8_22F3(): pass

    label("Function_8_22F3")

    Sleep(1000)

    def lambda_22FB():

        label("loc_22FB")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_22FB")

    QueueWorkItem2(0x8, 2, lambda_22FB)

    def lambda_230D():

        label("loc_230D")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_230D")

    QueueWorkItem2(0x13, 2, lambda_230D)

    def lambda_231F():

        label("loc_231F")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_231F")

    QueueWorkItem2(0x35, 2, lambda_231F)

    def lambda_2331():

        label("loc_2331")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_2331")

    QueueWorkItem2(0x34, 2, lambda_2331)

    def lambda_2343():

        label("loc_2343")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_2343")

    QueueWorkItem2(0x33, 2, lambda_2343)
    Sleep(50)

    def lambda_2358():

        label("loc_2358")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_2358")

    QueueWorkItem2(0x11, 2, lambda_2358)

    def lambda_236A():

        label("loc_236A")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_236A")

    QueueWorkItem2(0x2F, 2, lambda_236A)

    def lambda_237C():

        label("loc_237C")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_237C")

    QueueWorkItem2(0x12, 2, lambda_237C)

    def lambda_238E():

        label("loc_238E")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_238E")

    QueueWorkItem2(0x32, 2, lambda_238E)

    def lambda_23A0():

        label("loc_23A0")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_23A0")

    QueueWorkItem2(0x31, 2, lambda_23A0)

    def lambda_23B2():

        label("loc_23B2")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_23B2")

    QueueWorkItem2(0x30, 2, lambda_23B2)
    Sleep(50)

    def lambda_23C7():

        label("loc_23C7")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_23C7")

    QueueWorkItem2(0x24, 2, lambda_23C7)

    def lambda_23D9():

        label("loc_23D9")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_23D9")

    QueueWorkItem2(0x23, 2, lambda_23D9)

    def lambda_23EB():

        label("loc_23EB")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_23EB")

    QueueWorkItem2(0x2E, 2, lambda_23EB)

    def lambda_23FD():

        label("loc_23FD")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_23FD")

    QueueWorkItem2(0x28, 2, lambda_23FD)

    def lambda_240F():

        label("loc_240F")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_240F")

    QueueWorkItem2(0x29, 2, lambda_240F)

    def lambda_2421():

        label("loc_2421")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_2421")

    QueueWorkItem2(0x27, 2, lambda_2421)
    Sleep(50)

    def lambda_2436():

        label("loc_2436")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_2436")

    QueueWorkItem2(0xC, 2, lambda_2436)

    def lambda_2448():

        label("loc_2448")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_2448")

    QueueWorkItem2(0xB, 2, lambda_2448)

    def lambda_245A():

        label("loc_245A")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_245A")

    QueueWorkItem2(0x2D, 2, lambda_245A)

    def lambda_246C():

        label("loc_246C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_246C")

    QueueWorkItem2(0x25, 2, lambda_246C)

    def lambda_247E():

        label("loc_247E")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_247E")

    QueueWorkItem2(0x26, 2, lambda_247E)

    def lambda_2490():

        label("loc_2490")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_2490")

    QueueWorkItem2(0x16, 2, lambda_2490)
    Sleep(50)

    def lambda_24A5():

        label("loc_24A5")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_24A5")

    QueueWorkItem2(0x10, 2, lambda_24A5)

    def lambda_24B7():

        label("loc_24B7")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_24B7")

    QueueWorkItem2(0xF, 2, lambda_24B7)

    def lambda_24C9():

        label("loc_24C9")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_24C9")

    QueueWorkItem2(0x2B, 2, lambda_24C9)

    def lambda_24DB():

        label("loc_24DB")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_24DB")

    QueueWorkItem2(0x9, 2, lambda_24DB)

    def lambda_24ED():

        label("loc_24ED")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_24ED")

    QueueWorkItem2(0xA, 2, lambda_24ED)

    def lambda_24FF():

        label("loc_24FF")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_24FF")

    QueueWorkItem2(0x2C, 2, lambda_24FF)
    Return()

    # Function_8_22F3 end

    def Function_9_250D(): pass

    label("Function_9_250D")

    Sleep(4000)
    SetChrSubChip(0x36, 0x0)
    Sleep(3000)
    SetChrSubChip(0x36, 0x2)
    Return()

    # Function_9_250D end

    def Function_10_251C(): pass

    label("Function_10_251C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02400.itc", 0x1E)
    LoadChrToIndex("chr/ch00900.itc", 0x1F)
    LoadChrToIndex("chr/ch30500.itc", 0x20)
    OP_68(-1290, 2250, 12000, 0)
    MoveCamera(47, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, 5370, 4120, -7740, 325)
    SetChrPos(0x102, 4680, 4120, -6920, 325)
    SetChrPos(0x103, 6270, 4000, -6900, 325)
    SetChrPos(0x104, 7000, 4000, -7490, 325)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrPos(0x15, -8150, 0, 7500, 180)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, -8150, 0, 5500, 0)
    SetChrChipByIndex(0x16, 0x20)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrPos(0x16, -8650, 0, 4500, 0)
    OP_68(-1290, 2250, 6000, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(3380, 5620, -6500, 0)
    MoveCamera(10, 16, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(17000, 3000)
    OP_0D()
    OP_6F(0x79)

    #C0012
    ChrTalk(
        0x101,
        "#0000Fここは……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x102,
        (
            "#0100F各種式典などに使われる\x01",
            "レセプションホールね。\x02\x03",

            "今日はおじいさまの主催する\x01",
            "シンポジウムがあるはずだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0014
    ChrTalk(
        0x102,
        "#0105Fあら……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0x16, 0x8000)
    Fade(500)
    OP_68(-8150, 1500, 5000, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(15490, 0)
    OP_68(-8150, 1500, 6000, 3000)
    OP_0D()
    OP_6F(0x79)

    #C0015
    ChrTalk(
        0x15,
        (
            "#1400F──段取りは了解した。\x02\x03",

            "それでは周辺警備については\x01",
            "よろしくお願いする。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xA,
        (
            "#0600Fフン、了解だ。\x02\x03",

            "#0603F本来ならば我々一課がいれば\x01",
            "事足りるはずだったがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x15,
        (
            "#1404Fフフ……\x01",
            "まあ割り切ることだ。\x02\x03",

            "#1400Fシンポジウムの出席者は\x01",
            "諸外国の要人も多い。\x02\x03",

            "ギルドという保証が\x01",
            "対外的に欲しいだけの話だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xA,
        (
            "#0603Fフン、貴様に言われずとも\x01",
            "そのあたりは弁#2Rわきま#えている。\x02\x03",

            "#0600Fくれぐれもしくじるなよ──\x01",
            "《風の剣聖》殿。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x15,
        "#1404Fフ……承知した。\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(5370, 5620, -7740, 0)
    MoveCamera(17, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    ClearChrFlags(0x15, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0x16, 0x8000)

    #C0020
    ChrTalk(
        0x104,
        (
            "#0306F（ゲゲッ……\x01",
            "  面倒そうなのが揃い踏みかよ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#0005F（な、何だか\x01",
            "  珍しい組み合わせだな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x103,
        (
            "#0200F（どうやらシンポジウム会場の\x01",
            "  合同警備をするみたいです。）\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x102,
        (
            "#0101F（……お邪魔みたいだし、\x01",
            "  このまま出た方が良さそうね。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0xAD, 7)
    NewScene("c1110", 102, 0, 0)
    IdleLoop()
    FadeToBright(500, 0)
    OP_0D()
    Return()

    # Function_10_251C end

    SaveToFile()

Try(main)
