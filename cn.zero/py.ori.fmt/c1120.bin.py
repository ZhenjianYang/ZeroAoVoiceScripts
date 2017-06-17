from ZeroScenarioHelper import *

def main():
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
        "琪雅",                   # 1
        "赛尔盖科长",             # 2
        "达德利搜查官",           # 3
        "诺艾尔上士",             # 4
        "索妮亚副司令",           # 5
        "格蕾丝",                 # 6
        "麦克道尔市长",           # 7
        "玛丽亚贝尔",             # 8
        "迪塔总裁",               # 9
        "伊安律师",               # 10
        "瓦吉",                   # 11
        "塞茜尔",                 # 12
        "哈尔特曼议长",           # 13
        "亚里欧斯",               # 14
        "艾玛搜查官",             # 15
        "摄影师",                 # 16
        "开幕式嘉宾",             # 17
        "开幕式嘉宾",             # 18
        "开幕式嘉宾",             # 19
        "开幕式嘉宾",             # 20
        "开幕式嘉宾",             # 21
        "开幕式嘉宾",             # 22
        "开幕式嘉宾",             # 23
        "开幕式嘉宾",             # 24
        "开幕式嘉宾",             # 25
        "开幕式嘉宾",             # 26
        "开幕式嘉宾",             # 27
        "接待小姐瑞贝卡",         # 28
        "接待小姐芙兰",           # 29
        "多诺邦警督",             # 30
        "雷蒙德搜查官",           # 31
        "弗兰茨巡警",             # 32
        "乔里基科长",             # 33
        "凯特巡警",               # 34
        "海尔玛",                 # 35
        "摩尔斯会长",             # 36
        "皮埃尔副局长",           # 37
        "伊莉娅",                 # 38
        "莉夏",                   # 39
        "哈罗德",                 # 40
        "温蒂",                   # 41
        "迈尔斯",                 # 42
        "雷缇",                   # 43
        "奥斯卡",                 # 44
        "约纳",                   # 45
        "罗伯兹主任",             # 46
        "蔡特",                   # 47
        "SE控制",                 # 48
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
        "Function_6_1291",         # 06, 6
        "Function_7_12DB",         # 07, 7
        "Function_8_21CD",         # 08, 8
        "Function_9_23E7",         # 09, 9
        "Function_10_23F6",        # 0A, 10
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
            "#1K创立纪念庆典　第一天\x02",
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
    SetChrName("威严的声音")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "──克洛斯贝尔自治州\x01",
            "已经成立了七十年。\x02",
        )
    )

    CloseMessageWindow()

    #A0003
    AnonymousTalk(
        0xFF,
        (
            "在这七十年间，\x01",
            "我们经历了动荡的时代。\x02",
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
            "#2503F#5P频繁的战乱，还有导力革命的到来……\x02\x03",

            "在名为近代化的时代潮流中几载沉浮，\x01",
            "现在的克洛斯贝尔，已经逐渐发展成了大陆中\x01",
            "首屈一指的贸易城市与金融中心。\x02\x03",

            "#2500F受前年在利贝尔签署的\x01",
            "《互不侵犯条约》的影响，\x01",
            "紧张的局势也得到大幅度缓和。\x02",
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
            "#2503F#N另一方面，由于急速的城市开发\x01",
            "与人口增长，某些问题也随之产生，\x01",
            "所以我们迫切需要全新的政策与法律出台。\x02\x03",

            "#2501F为了给自治州，以及周边诸国\x01",
            "带来更加美好的未来……\x02\x03",

            "如今我们应该团结一致，共同协力，\x01",
            "并肩前进。\x02",
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
            "#2509F──然而，此时此刻，\x01",
            "就先让我们高举双手，共同欢庆\x01",
            "这个拥有七十年悠久历史的盛大节日吧。\x02\x03",

            "虽然只有短短五天，\x01",
            "但今年接待的游客数量将大大超越往年，\x01",
            "整个市内呈现出盛况空前的繁荣景象。\x02\x03",

            "以彩虹剧团的新剧公演为开端，\x01",
            "我们为您准备了丰富多彩的节日活动，\x01",
            "相信一定能让各位度过充实的五天。\x02",
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
            "#2503F──以伟大女神爱德丝的名义……\x02\x03",

            "#2507F我在此宣布，克洛斯贝尔自治州\x01",
            "创立七十周年纪念庆典，正式开始！\x02",
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

    def Function_6_1291(): pass

    label("Function_6_1291")

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

    # Function_6_1291 end

    def Function_7_12DB(): pass

    label("Function_7_12DB")

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

    def lambda_1529():

        label("loc_1529")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_1529")

    QueueWorkItem2(0xD, 2, lambda_1529)
    SetChrChipByIndex(0x17, 0x29)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -5200, 0, 9400, 90)

    def lambda_1563():

        label("loc_1563")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_1563")

    QueueWorkItem2(0x17, 2, lambda_1563)
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
            "#30W──在克洛斯贝尔引起恐慌的\x01",
            "『Ｄ∴Ｇ教团』。\x02\x03",

            "以及被其利用的黑手党\x01",
            "和被药物操纵的警备队。\x02\x03",

            "此外，还有以哈尔特曼议长为首，\x01",
            "众多权势者的无能失职……\x02\x03",

            "──此次事件的概要\x01",
            "一经克洛斯贝尔时代周刊报道，\x01",
            "便演变成了前所未有的巨大丑闻。\x02",
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
            "#30W事态发展至此，麦克道尔市长\x01",
            "下令解除了警察局长和警备队司令的职务──\x02\x03",

            "并命令各科负责人与索妮亚副司令\x01",
            "彻底查明该事件。\x02\x03",

            "以达德利搜查官为首，在那些长期遭受\x01",
            "上层压制的搜查官们的共同努力下，\x01",
            "不仅是帝国派议员，甚至连一部分共和国派议员\x01",
            "都被查出与『教团』存在干系……\x02\x03",

            "直至出现多名被捕者时，\x01",
            "市民们对克洛斯贝尔政界的不信任感\x01",
            "终于达到了顶峰。\x02",
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
            "#30W就在这时，ＩＢＣ的迪塔总裁\x01",
            "突然表明要参加下一届的市长竞选……\x02\x03",

            "继承即将引退的麦克道尔市长的理念，\x01",
            "他在竞选诺言中提出要确立健全政治体系。\x02\x03",

            "此外，麦克道尔市长\x01",
            "也表明将参选因众议员被捕\x01",
            "而造成的空缺席位……\x02\x03",

            "据说，他作为下一任的议长候选人，\x01",
            "备受各界的期待。\x02",
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
            "#30W自事件发生过了一个月──\x02\x03",

            "我们被麦克道尔市长\x01",
            "叫到了市政厅。\x02",
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

    def lambda_1E1E():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_1E1E)

    def lambda_1E2B():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_1E2B)

    def lambda_1E38():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_1E38)

    def lambda_1E45():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1E45)

    def lambda_1E52():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1E52)

    def lambda_1E5F():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x2C, 2, lambda_1E5F)

    def lambda_1E6C():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1E6C)

    def lambda_1E79():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1E79)

    def lambda_1E86():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x2D, 2, lambda_1E86)

    def lambda_1E93():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_1E93)

    def lambda_1EA0():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_1EA0)

    def lambda_1EAD():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_1EAD)

    def lambda_1EBA():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_1EBA)

    def lambda_1EC7():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_1EC7)

    def lambda_1ED4():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_1ED4)

    def lambda_1EE1():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_1EE1)

    def lambda_1EEE():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_1EEE)

    def lambda_1EFB():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_1EFB)

    def lambda_1F08():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_1F08)

    def lambda_1F15():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x2F, 2, lambda_1F15)

    def lambda_1F22():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1F22)

    def lambda_1F2F():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x32, 2, lambda_1F2F)

    def lambda_1F3C():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x31, 2, lambda_1F3C)

    def lambda_1F49():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x30, 2, lambda_1F49)

    def lambda_1F56():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1F56)

    def lambda_1F63():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_1F63)
    BeginChrThread(0x36, 0, 0, 9)

    def lambda_1F76():
        TurnDirection(0xFE, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x35, 2, lambda_1F76)

    def lambda_1F83():
        TurnDirection(0xFE, 0x102, 0)
        ExitThread()

    QueueWorkItem(0x34, 2, lambda_1F83)

    def lambda_1F90():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x33, 2, lambda_1F90)
    BeginChrThread(0x8, 3, 0, 8)

    def lambda_1FA3():
        OP_96(0xFE, 0xFFFFFA24, 0x2EE, 0x2DB4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FA3)
    Sleep(50)

    def lambda_1FC0():
        OP_96(0xFE, 0xFFFFFA24, 0x2EE, 0x2DB4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1FC0)
    Sleep(50)

    def lambda_1FDD():
        OP_96(0xFE, 0xFFFFFA24, 0x2EE, 0x2DB4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1FDD)
    Sleep(50)

    def lambda_1FFA():
        OP_96(0xFE, 0xFFFFFA24, 0x2EE, 0x2DB4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1FFA)
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

    def lambda_212B():
        OP_96(0xFE, 0xFFFFFA24, 0x2EE, 0x3138, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_212B)
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

    # Function_7_12DB end

    def Function_8_21CD(): pass

    label("Function_8_21CD")

    Sleep(1000)

    def lambda_21D5():

        label("loc_21D5")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_21D5")

    QueueWorkItem2(0x8, 2, lambda_21D5)

    def lambda_21E7():

        label("loc_21E7")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_21E7")

    QueueWorkItem2(0x13, 2, lambda_21E7)

    def lambda_21F9():

        label("loc_21F9")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_21F9")

    QueueWorkItem2(0x35, 2, lambda_21F9)

    def lambda_220B():

        label("loc_220B")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_220B")

    QueueWorkItem2(0x34, 2, lambda_220B)

    def lambda_221D():

        label("loc_221D")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_221D")

    QueueWorkItem2(0x33, 2, lambda_221D)
    Sleep(50)

    def lambda_2232():

        label("loc_2232")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_2232")

    QueueWorkItem2(0x11, 2, lambda_2232)

    def lambda_2244():

        label("loc_2244")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_2244")

    QueueWorkItem2(0x2F, 2, lambda_2244)

    def lambda_2256():

        label("loc_2256")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_2256")

    QueueWorkItem2(0x12, 2, lambda_2256)

    def lambda_2268():

        label("loc_2268")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_2268")

    QueueWorkItem2(0x32, 2, lambda_2268)

    def lambda_227A():

        label("loc_227A")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_227A")

    QueueWorkItem2(0x31, 2, lambda_227A)

    def lambda_228C():

        label("loc_228C")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_228C")

    QueueWorkItem2(0x30, 2, lambda_228C)
    Sleep(50)

    def lambda_22A1():

        label("loc_22A1")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_22A1")

    QueueWorkItem2(0x24, 2, lambda_22A1)

    def lambda_22B3():

        label("loc_22B3")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_22B3")

    QueueWorkItem2(0x23, 2, lambda_22B3)

    def lambda_22C5():

        label("loc_22C5")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_22C5")

    QueueWorkItem2(0x2E, 2, lambda_22C5)

    def lambda_22D7():

        label("loc_22D7")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_22D7")

    QueueWorkItem2(0x28, 2, lambda_22D7)

    def lambda_22E9():

        label("loc_22E9")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_22E9")

    QueueWorkItem2(0x29, 2, lambda_22E9)

    def lambda_22FB():

        label("loc_22FB")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_22FB")

    QueueWorkItem2(0x27, 2, lambda_22FB)
    Sleep(50)

    def lambda_2310():

        label("loc_2310")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_2310")

    QueueWorkItem2(0xC, 2, lambda_2310)

    def lambda_2322():

        label("loc_2322")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_2322")

    QueueWorkItem2(0xB, 2, lambda_2322)

    def lambda_2334():

        label("loc_2334")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_2334")

    QueueWorkItem2(0x2D, 2, lambda_2334)

    def lambda_2346():

        label("loc_2346")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_2346")

    QueueWorkItem2(0x25, 2, lambda_2346)

    def lambda_2358():

        label("loc_2358")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_2358")

    QueueWorkItem2(0x26, 2, lambda_2358)

    def lambda_236A():

        label("loc_236A")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_236A")

    QueueWorkItem2(0x16, 2, lambda_236A)
    Sleep(50)

    def lambda_237F():

        label("loc_237F")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_237F")

    QueueWorkItem2(0x10, 2, lambda_237F)

    def lambda_2391():

        label("loc_2391")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_2391")

    QueueWorkItem2(0xF, 2, lambda_2391)

    def lambda_23A3():

        label("loc_23A3")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_23A3")

    QueueWorkItem2(0x2B, 2, lambda_23A3)

    def lambda_23B5():

        label("loc_23B5")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_23B5")

    QueueWorkItem2(0x9, 2, lambda_23B5)

    def lambda_23C7():

        label("loc_23C7")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_23C7")

    QueueWorkItem2(0xA, 2, lambda_23C7)

    def lambda_23D9():

        label("loc_23D9")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_23D9")

    QueueWorkItem2(0x2C, 2, lambda_23D9)
    Return()

    # Function_8_21CD end

    def Function_9_23E7(): pass

    label("Function_9_23E7")

    Sleep(4000)
    SetChrSubChip(0x36, 0x0)
    Sleep(3000)
    SetChrSubChip(0x36, 0x2)
    Return()

    # Function_9_23E7 end

    def Function_10_23F6(): pass

    label("Function_10_23F6")

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
        "#0000F这里是……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x102,
        (
            "#0100F举行各种仪式的\x01",
            "宴会大厅啊。\x02\x03",

            "今天应该有一场由外公\x01",
            "主办的专题研讨会……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0014
    ChrTalk(
        0x102,
        "#0105F啊……\x02",
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
            "#1400F──计划已经了解了。\x02\x03",

            "那么，周边的警备工作\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xA,
        (
            "#0600F哼，知道了。\x02\x03",

            "#0603F其实按照原定计划，有我们一科\x01",
            "就已经足够了。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x15,
        (
            "#1404F呵呵……\x01",
            "别介意，只是分工合作而已。\x02\x03",

            "#1400F在研讨会的出席者中，\x01",
            "也有很多国外要人。\x02\x03",

            "政府只是希望能有游击士协会这个保证\x01",
            "来让他们安心，仅此而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xA,
        (
            "#0603F哼，不用你说，\x01",
            "我们也明白。\x02\x03",

            "#0600F你可别搞砸工作，拖了我们的后腿──\x01",
            "『风之剑圣』先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x15,
        "#1404F呵……多谢提醒。\x02",
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
            "#0306F（呃……\x01",
            "　两个麻烦的家伙凑到一起了啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#0005F（真、真是个\x01",
            "　稀有的组合啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x103,
        (
            "#0200F（看起来，他们准备联手\x01",
            "　进行研讨会的警备工作呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x102,
        (
            "#0101F（……好像会打扰到他们呢，\x01",
            "　我们还是出去为好吧。）\x02",
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

    # Function_10_23F6 end

    SaveToFile()

Try(main)
