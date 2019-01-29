from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t3000.bin",                # FileName
        "t3000",                    # MapName
        "t3000",                    # Location
        0x005B,                     # MapIndex
        "ed7202",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x1E,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 91, 0, 1, 0, 2],
    )

    BuildStringList((
        "t3000",                  # 0
        "案内人形",               # 1
        "白衣の男",               # 2
        "少年",                   # 3
        "ヨルグ老人",             # 4
        "ハインツ",               # 5
        "車",                     # 6
        "SE制御",                 # 7
        "マインツ山道",           # 8
    ))

    AddCharChip((
        "chr/ch47400.itc",                   # 00
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 22,  2.0,                   40.0,                  -0.5,                  900.0,                 [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   0.0,                   -0.1666666716337204,   -8.0,                  0.05000000074505806,   1.0])

    DeclActor(-7090,   0,       24320,   1200,    -7090,   2500,    24320,   0x007C, 0,  3,  0x0000)
    DeclActor(2070,    250,     26860,   1200,    2070,    1500,    26860,   0x007C, 0,  4,  0x0000)
    DeclActor(2000,    2500,    47300,   1200,    2000,    4000,    47300,   0x007C, 0,  5,  0x0000)

    PlaceName(-1.6100000143051147, 0.0, -23.0, 0x0000, 0x0000, "マインツ山道")

    ChipFrameInfo(844, 0)                                        # 0

    ScpFunction((
        "Function_0_34C",          # 00, 0
        "Function_1_404",          # 01, 1
        "Function_2_4E4",          # 02, 2
        "Function_3_6F1",          # 03, 3
        "Function_4_762",          # 04, 4
        "Function_5_7A0",          # 05, 5
        "Function_6_7AD",          # 06, 6
        "Function_7_1BF8",         # 07, 7
        "Function_8_1C1A",         # 08, 8
        "Function_9_1C3C",         # 09, 9
        "Function_10_1C5E",        # 0A, 10
        "Function_11_1C80",        # 0B, 11
        "Function_12_1C97",        # 0C, 12
        "Function_13_1CB1",        # 0D, 13
        "Function_14_1CCB",        # 0E, 14
        "Function_15_1CE5",        # 0F, 15
        "Function_16_1D0E",        # 10, 16
        "Function_17_1D37",        # 11, 17
        "Function_18_1D97",        # 12, 18
        "Function_19_3194",        # 13, 19
        "Function_20_31C9",        # 14, 20
        "Function_21_3252",        # 15, 21
        "Function_22_3DC3",        # 16, 22
        "Function_23_3DF9",        # 17, 23
        "Function_24_3E63",        # 18, 24
        "Function_25_3E86",        # 19, 25
        "Function_26_4ECE",        # 1A, 26
        "Function_27_4F40",        # 1B, 27
        "Function_28_4FE9",        # 1C, 28
        "Function_29_5021",        # 1D, 29
        "Function_30_5059",        # 1E, 30
        "Function_31_5091",        # 1F, 31
        "Function_32_50C9",        # 20, 32
        "Function_33_5101",        # 21, 33
        "Function_34_5139",        # 22, 34
        "Function_35_583C",        # 23, 35
        "Function_36_58A6",        # 24, 36
        "Function_37_5D78",        # 25, 37
        "Function_38_5DCF",        # 26, 38
    ))


    def Function_0_34C(): pass

    label("Function_0_34C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_38C"),
        (1, "loc_398"),
        (2, "loc_3A4"),
        (3, "loc_3B0"),
        (4, "loc_3BC"),
        (5, "loc_3C8"),
        (6, "loc_3D4"),
        (SWITCH_DEFAULT, "loc_3E0"),
    )


    label("loc_38C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_398")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3A4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3B0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3BC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3C8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3D4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3E0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_3EC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_403")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_3EC")

    label("loc_403")

    Return()

    # Function_0_34C end

    def Function_1_404(): pass

    label("Function_1_404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 7)), scpexpr(EXPR_END)), "loc_412")
    Jump("loc_46F")

    label("loc_412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 1)), scpexpr(EXPR_END)), "loc_43C")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 2000, 2500, 46450, 180)
    BeginChrThread(0x8, 0, 0, 0)
    Jump("loc_46F")

    label("loc_43C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 0)), scpexpr(EXPR_END)), "loc_44A")
    Jump("loc_46F")

    label("loc_44A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_END)), "loc_46F")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 2000, 2500, 46450, 180)
    BeginChrThread(0x8, 0, 0, 0)

    label("loc_46F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_483")
    ClearScenarioFlags(0x22, 0)
    Event(0, 25)
    Jump("loc_492")

    label("loc_483")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_492")
    ClearScenarioFlags(0x22, 1)
    Event(0, 36)

    label("loc_492")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B2")
    SetMapFlags(0x10000000)
    Event(0, 6)
    Jump("loc_4E3")

    label("loc_4B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4CD")
    SetMapFlags(0x10000000)
    Event(0, 18)
    Jump("loc_4E3")

    label("loc_4CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4E3")
    SetMapFlags(0x10000000)
    Event(0, 34)

    label("loc_4E3")

    Return()

    # Function_1_404 end

    def Function_2_4E4(): pass

    label("Function_2_4E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_4F6")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56D")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x6E, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_56D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_584")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_584")

    label("loc_584")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 7)), scpexpr(EXPR_END)), "loc_597")
    Jump("loc_61C")

    label("loc_597")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 1)), scpexpr(EXPR_END)), "loc_5D5")
    SetChrFlags(0x8, 0x8000)
    ModifyEventFlags(1, 0, 0x80)
    ClearMapObjFlags(0x1, 0x10)
    OP_10(0x1, 0x0)
    SetBarrier(0x0, 0x0, 0x1, 0x0, 2000, 2000, 46450, 5000, 2000, 0)
    Jump("loc_61C")

    label("loc_5D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 0)), scpexpr(EXPR_END)), "loc_5E3")
    Jump("loc_61C")

    label("loc_5E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_END)), "loc_61C")
    SetChrFlags(0x8, 0x8000)
    ModifyEventFlags(1, 0, 0x80)
    ClearMapObjFlags(0x1, 0x10)
    OP_10(0x1, 0x0)
    SetBarrier(0x0, 0x0, 0x1, 0x0, 2000, 2000, 46450, 5000, 2000, 0)

    label("loc_61C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62F")
    OP_1B(0x0, 0x0, 0x26)

    label("loc_62F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 2)), scpexpr(EXPR_END)), "loc_63D")
    Jump("loc_67E")

    label("loc_63D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 7)), scpexpr(EXPR_END)), "loc_659")
    EndChrThread(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    Jump("loc_67E")

    label("loc_659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 4)), scpexpr(EXPR_END)), "loc_667")
    Jump("loc_67E")

    label("loc_667")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 0)), scpexpr(EXPR_END)), "loc_67E")
    EndChrThread(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)

    label("loc_67E")

    ClearMapObjFlags(0x0, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 2)), scpexpr(EXPR_END)), "loc_692")
    Jump("loc_6CB")

    label("loc_692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 1)), scpexpr(EXPR_END)), "loc_6AA")
    SetMapObjFlags(0x0, 0x10)
    OP_65(0x1, 0x1)
    Jump("loc_6CB")

    label("loc_6AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 4)), scpexpr(EXPR_END)), "loc_6B8")
    Jump("loc_6CB")

    label("loc_6B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_END)), "loc_6CB")
    SetMapObjFlags(0x0, 0x10)
    OP_65(0x1, 0x1)

    label("loc_6CB")

    OP_65(0x2, 0x1)
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x226), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x226), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x226), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_2_4E4 end

    def Function_3_6F1(): pass

    label("Function_3_6F1")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "   『ローゼンベルク工房』\x01",
            "関係者以外の立ち入りを禁ずる。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_3_6F1 end

    def Function_4_762(): pass

    label("Function_4_762")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_774")
    Call(0, 21)
    Return()

    label("loc_774")

    TalkBegin(0xFF)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉は固く閉ざされている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_4_762 end

    def Function_5_7A0(): pass

    label("Function_5_7A0")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    TalkEnd(0xFF)
    Return()

    # Function_5_7A0 end

    def Function_6_7AD(): pass

    label("Function_6_7AD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    LoadChrToIndex("chr/ch13400.itc", 0x1E)
    LoadChrToIndex("chr/ch03600.itc", 0x1F)
    LoadChrToIndex("chr/ch06600.itc", 0x20)
    SoundLoad(3701)
    SoundLoad(3702)
    SoundLoad(3703)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03900.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04801.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04700.itp")
    OP_68(2000, 600, 24500, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 230, 0, 3850, 0)
    SetChrPos(0x102, 900, 0, 2310, 0)
    SetChrPos(0x109, -430, 0, 1790, 0)
    SetChrPos(0x105, 440, 0, 740, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrPos(0x9, 2600, 0, 22100, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrPos(0xA, 1400, 0, 22100, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x20)
    SetChrPos(0xB, 2000, 0, 24300, 180)
    ClearChrFlags(0xB, 0x4)
    OP_70(0x0, 0xA)
    OP_68(2250, 6700, 42650, 0)
    MoveCamera(25, 11, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(84820, 0)
    FadeToBright(1000, 0)
    OP_68(2250, 6700, 42650, 6000)
    MoveCamera(17, 11, 0, 6000)
    OP_6E(510, 6000)
    SetCameraDistance(93510, 6000)
    Sleep(1000)
    PlaceName2(100, 200, "c_plac16", 0x0, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(2000, 3600, 23000, 0)
    MoveCamera(42, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20150, 0)
    OP_68(2000, 1000, 23000, 3000)
    OP_0D()
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0003
    AnonymousTalk(
        0xB,
        (
            "──くどい。\x01",
            "おぬしを入れるつもりはない。\x02\x03",

            "いかに《十三工房》の統括者といえ、\x01",
            "立ち入る権利は無いはずだ。\x02",
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
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0004
    AnonymousTalk(
        0x9,
        (
            "……フフ、まあいいだろう。\x02\x03",

            "アレはＮｏ．ⅩⅤの所有物。\x01",
            "元より取り上げるつもりはないさ。\x02\x03",

            "しかし、マイスター？\x01",
            "データは一通り渡してもらうよ？\x02\x03",

            "それが“あの御方”の\x01",
            "御意志でもあるのだからねぇ。\x02",
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

    #C0005
    ChrTalk(
        0xB,
        (
            "#03903F#5P……フン。\x01",
            "おぬしに言われるまでもない。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #A0006
    AnonymousTalk(
        0xA,
        (
            "#3701V#30Wウフフ、本当に仲が悪いなぁ。\x02\x03",

            "#3702V博士も嫌われていると判ってて\x01",
            "わざわざ訪ねなきゃいいのに。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE76)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_C9(0x1, 0x80000000)

    #C0007
    ChrTalk(
        0x9,
        (
            "#04709F#11Pハハ、何を言ってるのかね？\x02\x03",

            "#04702F私とマイスターは旧知の仲。\x02\x03",

            "特に人形作りに関しては\x01",
            "固い師弟の絆で\x01",
            "結ばれているんだからねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xB,
        (
            "#03903F#5Pフン、戯言#4Rざれごと#は止めるがいい。\x02\x03",

            "#03900F所詮わしの技術など\x01",
            "結社にしてみれば古臭いもの。\x02\x03",

            "おぬしの《統合理論》があれば\x01",
            "わしに頼る必要などあるまい？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x9,
        (
            "#04704F#11Pフフ、ご謙遜を。\x02\x03",

            "こと人形の調整にかけて\x01",
            "マイスターの右に出る人間なんて\x01",
            "この世に存在しないさ。\x02\x03",

            "#04705Fあ、でも《パテル＝マテル》に付けた\x01",
            "あの回路だけはいただけないねぇ？\x02\x03",

            "#04703Fあれじゃあ、せっかくの\x01",
            "《殲滅#4Rせんめつ#天使》のポテンシャルが\x01",
            "無駄になってしまうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xB,
        "#03901F#5P……この外道が。\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        "#5Pえっと、すみません。\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x109, 0x8)
    ClearChrFlags(0x105, 0x8)
    OP_68(920, 300, 9760, 0)
    MoveCamera(33, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(32049, 0)
    Fade(500)
    BeginChrThread(0x101, 0, 0, 7)
    BeginChrThread(0x102, 0, 0, 8)
    BeginChrThread(0x109, 0, 0, 9)
    BeginChrThread(0x105, 0, 0, 10)
    OP_68(2000, 1000, 23000, 8000)
    MoveCamera(42, 15, 0, 8000)
    OP_6E(510, 8000)
    SetCameraDistance(25150, 8000)

    def lambda_10AB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_10AB)
    Sleep(50)

    def lambda_10BB():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_10BB)
    Sleep(3000)
    OP_0D()
    OP_68(2000, 1000, 23000, 0)
    MoveCamera(42, 15, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20150, 0)
    Fade(500)
    OP_0D()
    OP_4B(0x101, 0xFF)
    OP_4B(0x102, 0xFF)
    OP_4B(0x109, 0xFF)
    OP_4B(0x105, 0xFF)

    #C0012
    ChrTalk(
        0x9,
        "#04705F#5Pおや……？\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xA,
        (
            "#04805F#5Pあれ？\x01",
            "お客さんみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xB,
        (
            "#03903F#5P……カンパネルラ。\x01",
            "用件は済んだだろう。\x02\x03",

            "#03900Fその不快な男を連れて\x01",
            "とっとと立ち去るがいい。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11C2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_11C2)
    Sleep(50)

    def lambda_11D2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_11D2)
    Sleep(300)

    #C0015
    ChrTalk(
        0xA,
        (
            "#04804F#12Pウフフ、了解。\x02\x03",

            "#04802Fほらほら博士。\x01",
            "さっさと次に行かないと。\x02\x03",

            "今日中に用を済ませて\x01",
            "ラボに戻るんだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "#04704F#11Pフフ、もちろんだとも。\x02\x03",

            "#04702Fそれではマイスター、\x01",
            "これで失礼させてもらうよ。\x02\x03",

            "例の子たちも完成しだい、\x01",
            "チェックをお願いするからね？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x101, 0xFF)
    OP_4C(0x102, 0xFF)
    OP_4C(0x109, 0xFF)
    OP_4C(0x105, 0xFF)
    Sleep(400)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0017
    ChrTalk(
        0xB,
        (
            "#03901F#5P#4S……くどい！\x01",
            "とっとと失せるがいい！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    #C0018
    ChrTalk(
        0xA,
        "#04809F#12P#3703V#30Wウフフ、それじゃあまた。\x02",
    )

    CloseMessageWindow()
    OP_24(0xE77)
    OP_C9(0x1, 0x80000000)
    SetCameraDistance(22250, 3000)
    Sleep(300)
    BeginChrThread(0x9, 0, 0, 16)
    BeginChrThread(0xA, 0, 0, 15)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x109)
    OP_64(0x105)
    Sleep(2000)

    #C0019
    ChrTalk(
        0xB,
        "#03900F#5P……何を呆#2Rほう#けている。\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    BeginChrThread(0x101, 0, 0, 11)
    Sleep(50)
    BeginChrThread(0x102, 0, 0, 12)
    Sleep(50)
    BeginChrThread(0x109, 0, 0, 13)
    Sleep(50)
    BeginChrThread(0x105, 0, 0, 14)
    Sleep(300)
    SetCameraDistance(20150, 2000)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xA, 0)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_15D1")

    #C0020
    ChrTalk(
        0x101,
        "#00006F#12Pす、すみません。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x102,
        (
            "#00104F#12Pその節はどうも……\x01",
            "ご無沙汰していました。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xB,
        (
            "#03903F#5P特務支援課か、久しいな。\x02\x03",

            "#03900Fレンはリベールに去った。\x01",
            "今さらここに何の用だ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16F2")

    label("loc_15D1")


    #C0023
    ChrTalk(
        0x101,
        (
            "#00006F#12Pす、すみません。\x02\x03",

            "#00000F……初めまして。\x01",
            "クロスベル警察、\x01",
            "特務支援課の者です。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        (
            "#00100F#12Pローゼンベルク工房の主、\x01",
            "ヨルグ・マイスターでいらっしゃいますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xB,
        (
            "#03903F#5Pフン、レンから多少、\x01",
            "話は聞いておるようだな。\x02\x03",

            "#03900Fレンはリベールに去った。\x01",
            "ここに何の用だ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F2")


    #C0026
    ChrTalk(
        0x101,
        (
            "#00012F#12Pいえ、近くに来たので\x01",
            "挨拶に伺っただけなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        (
            "#00102F#12Pその……\x01",
            "来客中に失礼しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xB,
        (
            "#03901F#5Pフン、招かれざる客だ。\x01",
            "その事は気にしておらん。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_93(0xB, 0x0, 0x1F4)
    Sleep(250)

    #C0029
    ChrTalk(
        0xB,
        (
            "#03903F#11Pだが今は、特に話すことが\x01",
            "あるわけでもあるまい。\x02\x03",

            "何か用件ができたら\x01",
            "改めて訪ねてくるがいい。\x02\x03",

            "#03900Fレンに免じて話くらいは聞こう。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#00011F#12Pあ……\x02",
    )

    CloseMessageWindow()
    OP_68(2420, 1000, 24440, 2000)
    BeginChrThread(0xB, 0, 0, 17)
    Sleep(2000)
    Sound(113, 0, 100, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    Sleep(800)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0031
    ChrTalk(
        0x109,
        "#10105F#12Pか、勝手に門が閉まった……\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x105,
        (
            "#10308F#12Pふぅん、古めかしいけど\x01",
            "何か仕掛けでもあるのかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_68(1870, 1000, 21870, 1300)
    MoveCamera(29, 14, 0, 1300)
    OP_6E(510, 1300)
    SetCameraDistance(19000, 1300)
    TurnDirection(0x101, 0x105, 500)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1A3B")

    #C0033
    ChrTalk(
        0x101,
        (
            "#00006F#5Pああ……\x01",
            "とんでもないカラクリを\x01",
            "作っている場所だからな。\x02\x03",

            "#00008Fそれに……\x01",
            "さっきの来客も気になるな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AB0")

    label("loc_1A3B")


    #C0034
    ChrTalk(
        0x101,
        (
            "#00006F#5Pああ、レンに聞いた通り、\x01",
            "単なる人形工房じゃなさそうだ。\x02\x03",

            "#00008Fそれに……\x01",
            "さっきの来客も気になるな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AB0")

    TurnDirection(0x102, 0x109, 500)

    #C0035
    ChrTalk(
        0x102,
        (
            "#00103F#11Pええ、招かれざる客って\x01",
            "言ってたけど……\x02\x03",

            "#00108F何ていうか、その……\x01",
            "怪しげな感じだったわね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    #C0036
    ChrTalk(
        0x109,
        (
            "#10106F#6Pそうですね……\x02\x03",

            "#10100Fまあ、危険そうには\x01",
            "見えませんでしたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x105,
        (
            "#10304F#12P（……フフ。\x01",
            "  危険そうには見えないか。）\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetChrFlags(0xB, 0x80)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    SetChrPos(0x0, 130, 0, 20860, 0)
    SetScenarioFlags(0x129, 4)
    OP_2C(0xA1, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_6_7AD end

    def Function_7_1BF8(): pass

    label("Function_7_1BF8")

    OP_9B(0x0, 0xFE, 0x4, 0x36B0, 0x7D0, 0x0)

    def lambda_1C0C():

        label("loc_1C0C")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1C0C")

    QueueWorkItem2(0xFE, 2, lambda_1C0C)
    Return()

    # Function_7_1BF8 end

    def Function_8_1C1A(): pass

    label("Function_8_1C1A")

    OP_9B(0x0, 0xFE, 0x5, 0x3BC4, 0x7D0, 0x0)

    def lambda_1C2E():

        label("loc_1C2E")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1C2E")

    QueueWorkItem2(0xFE, 2, lambda_1C2E)
    Return()

    # Function_8_1C1A end

    def Function_9_1C3C(): pass

    label("Function_9_1C3C")

    OP_9B(0x0, 0xFE, 0x6, 0x38A4, 0x7D0, 0x0)

    def lambda_1C50():

        label("loc_1C50")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1C50")

    QueueWorkItem2(0xFE, 2, lambda_1C50)
    Return()

    # Function_9_1C3C end

    def Function_10_1C5E(): pass

    label("Function_10_1C5E")

    OP_9B(0x0, 0xFE, 0x6, 0x3C8C, 0x7D0, 0x0)

    def lambda_1C72():

        label("loc_1C72")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1C72")

    QueueWorkItem2(0xFE, 2, lambda_1C72)
    Return()

    # Function_10_1C5E end

    def Function_11_1C80(): pass

    label("Function_11_1C80")

    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
    Return()

    # Function_11_1C80 end

    def Function_12_1C97(): pass

    label("Function_12_1C97")

    Sleep(50)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xE10, 0x7D0, 0x0)
    Return()

    # Function_12_1C97 end

    def Function_13_1CB1(): pass

    label("Function_13_1CB1")

    Sleep(100)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
    Return()

    # Function_13_1CB1 end

    def Function_14_1CCB(): pass

    label("Function_14_1CCB")

    Sleep(150)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
    Return()

    # Function_14_1CCB end

    def Function_15_1CE5(): pass

    label("Function_15_1CE5")

    Sleep(50)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x2AF8, 0x7D0, 0x0)
    Return()

    # Function_15_1CE5 end

    def Function_16_1D0E(): pass

    label("Function_16_1D0E")

    Sleep(250)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x2AF8, 0x7D0, 0x0)
    Return()

    # Function_16_1D0E end

    def Function_17_1D37(): pass

    label("Function_17_1D37")

    OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0x9C4, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x9C4, 0x0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)

    def lambda_1D6C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1D6C)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    Return()

    # Function_17_1D37 end

    def Function_18_1D97(): pass

    label("Function_18_1D97")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06600.itc", 0x1E)
    LoadChrToIndex("chr/ch24200.itc", 0x1F)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xD, 0x80)
    OP_78(0x2, 0xD)
    OP_49()
    ClearMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFrame(0x2, "light", 0x0, 0x1)
    SetChrPos(0x101, 0, 0, -6000, 0)
    SetChrPos(0x102, 750, 0, -6250, 0)
    SetChrPos(0x103, -750, 0, -7250, 0)
    SetChrPos(0x104, 0, 0, -7750, 0)
    SetChrPos(0x109, 250, 0, -8750, 0)
    SetChrPos(0x105, 1500, 0, -7250, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0xB, 1600, 0, 24300, 180)
    SetChrPos(0xC, 1600, 0, 21300, 0)
    SetChrPos(0xD, 5000, 0, 19000, 180)
    OP_D5(0xD, 0x0, 0x2BF20, 0x0, 0x0)
    OP_68(0, 1000, -7000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21500, 0)
    OP_68(0, 1000, -4000, 3000)
    SetCameraDistance(20500, 3000)
    FadeToBright(1000, 0)

    def lambda_1F0C():
        OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F0C)
    Sleep(10)

    def lambda_1F24():
        OP_9B(0x0, 0x102, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1F24)
    Sleep(10)

    def lambda_1F3C():
        OP_9B(0x0, 0x103, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1F3C)
    Sleep(10)

    def lambda_1F54():
        OP_9B(0x0, 0x104, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1F54)
    Sleep(10)

    def lambda_1F6C():
        OP_9B(0x0, 0x109, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1F6C)
    Sleep(10)

    def lambda_1F84():
        OP_9B(0x0, 0x105, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1F84)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0038
    ChrTalk(
        0x101,
        "#00005F#11Pあれは……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x103,
        "#00205F#12P運搬車……？\x02",
    )

    CloseMessageWindow()
    OP_68(1400, 1000, 22800, 3000)
    MoveCamera(45, 25, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(20500, 3000)
    OP_6F(0x79)

    #C0040
    ChrTalk(
        0xC,
        (
            "#12Pマイスター、\x01",
            "本当に助かりました！\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xC,
        (
            "#12P何とか明後日の公演に\x01",
            "間に合わせられそうです！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xB,
        (
            "#03903F#5Pまったく……\x01",
            "お前たちの劇団ときたら\x01",
            "毎度毎度、要求が高すぎる。\x02\x03",

            "自動人形#8Rオ ー ト マ タ#の調整ならまだしも\x01",
            "新たな舞台装置の発注まで……\x02\x03",

            "#03901Fわしとてヒマではないのだぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xC,
        (
            "#12Pあはは……\x01",
            "本当に申し訳ありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xC,
        (
            "#12P何せイリアさんと\x01",
            "劇団長からの要求が高くて……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xC,
        (
            "#12Pつい、あのような仕掛けまで\x01",
            "追加発注させていただきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xB,
        (
            "#03900F#5Pフン、まあいいだろう。\x02\x03",

            "#03903F……我が工房の技術、\x01",
            "お前たちの舞台に活かす方が\x01",
            "女神の意志には適#2Rかな#うだろうからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xC,
        "#12Pは、はあ……？\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xC,
        "#12P──それはそうと、マイスター。\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xC,
        (
            "#12P前々からお誘いしている通り、\x01",
            "是非ともアルカンシェルの公演を\x01",
            "ご覧になって頂きたいんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xC,
        (
            "#12Pいつも素晴らしい人形と舞台装置を\x01",
            "提供して頂いてるわけですし……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xB,
        (
            "#03903F#5P相応のミラは受け取っている。\x02\x03",

            "#03900F……わしは忙しいのだ。\x01",
            "好意だけ貰っておくとしよう。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xB, 3, 0, 19)

    #C0052
    ChrTalk(
        0xC,
        "#12Pあ……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 3)
    OP_68(1400, 1000, 24300, 1000)
    MoveCamera(45, 25, 0, 1000)
    OP_6E(510, 1000)
    SetCameraDistance(20500, 1000)

    def lambda_247E():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_247E)
    Sleep(1000)
    Sound(113, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    WaitChrThread(0xC, 1)
    Sleep(500)

    #C0053
    ChrTalk(
        0xC,
        (
            "#12P……はぁ。\x01",
            "やっぱり応じてくれないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xC,
        (
            "#12Pせっかくの舞台装置、\x01",
            "どのように使われているのか\x01",
            "一度見て欲しいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#00001F……あの………\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_2565():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2565)
    SetChrPos(0x101, 1400, 0, 15000, 0)
    SetChrPos(0x102, 2150, 0, 14750, 0)
    SetChrPos(0x103, 650, 0, 13750, 0)
    SetChrPos(0x104, 1400, 0, 13250, 0)
    SetChrPos(0x109, 1650, 0, 12250, 0)
    SetChrPos(0x105, 2900, 0, 13750, 0)
    OP_68(1400, 1000, 22500, 3000)
    MoveCamera(45, 25, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(20500, 3000)

    def lambda_2606():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2606)
    Sleep(50)

    def lambda_261E():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_261E)
    Sleep(50)

    def lambda_2636():
        OP_9B(0x0, 0x103, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2636)
    Sleep(50)

    def lambda_264E():
        OP_9B(0x0, 0x104, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_264E)
    Sleep(50)

    def lambda_2666():
        OP_9B(0x0, 0x109, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2666)
    Sleep(50)

    def lambda_267E():
        OP_9B(0x0, 0x105, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_267E)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0xC, 2)
    OP_6F(0x79)

    #C0056
    ChrTalk(
        0xC,
        (
            "#5Pおや……\x01",
            "たしか特務支援課の？\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#00000F#12Pあ、はい。\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        (
            "#00100F#12Pアルカンシェルの\x01",
            "技師をされている方ですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xC,
        (
            "#5Pええ、舞台装置を担当している\x01",
            "ハインツです。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xC,
        (
            "#5P珍しい場所で会いますね。\x01",
            "マイスターに御用ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#00012F#12Pえ、ええ、ちょっと相談に\x01",
            "乗ってもらいたい事がありまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x103,
        (
            "#00200F#12Pそちらは舞台用の装置を\x01",
            "受け取りに……？\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xC,
        (
            "#5Pええ、自動人形の調整と\x01",
            "新しい舞台装置の製作を\x01",
            "お願いしておりまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xC,
        (
            "#5Pリニューアル公演に合わせた\x01",
            "無茶なスケジュールでしたが\x01",
            "何とか仕上げていただきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xC,
        (
            "#5Pいや～、劇団員一同、\x01",
            "マイスターには\x01",
            "足を向けて寝られませんよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x109,
        "#10100F#12Pなるほど……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x104,
        (
            "#00309F#12Pそういやアルカンシェルの\x01",
            "リニューアル舞台の初公演は\x01",
            "いよいよ明後日なんだよなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xC,
        (
            "#5Pええ、イリアさんを始め、\x01",
            "団員全員がかつてないほど\x01",
            "気合いが入っていまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xC,
        (
            "#5P舞台装置担当としても\x01",
            "身が引き締まる思いですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        "#00004F#12Pそうですか……\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x105,
        (
            "#10302F#12Pフフ、さぞかし凄い舞台に\x01",
            "なりそうだねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xC,
        (
            "#5Pおっと、こうしちゃいられない。\x01",
            "早く帰ってセットしないと……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xC,
        (
            "#5P──皆さん、私はこれで！\x01",
            "また劇場にいらしてください！\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x102,
        "#00104F#12Pはい、それでは。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        "#00202F#12Pどうかお気をつけて。\x02",
    )

    CloseMessageWindow()

    def lambda_2B3D():
        OP_9B(0x1, 0xFE, 0xE6, 0x2EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2B3D)
    BeginChrThread(0xC, 1, 0, 20)
    OP_68(2900, 1000, 18300, 5000)
    SetCameraDistance(21500, 5000)

    def lambda_2B72():

        label("loc_2B72")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2B72")

    QueueWorkItem2(0x101, 2, lambda_2B72)

    def lambda_2B84():

        label("loc_2B84")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2B84")

    QueueWorkItem2(0x102, 2, lambda_2B84)

    def lambda_2B96():

        label("loc_2B96")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2B96")

    QueueWorkItem2(0x103, 2, lambda_2B96)

    def lambda_2BA8():

        label("loc_2BA8")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2BA8")

    QueueWorkItem2(0x104, 2, lambda_2BA8)

    def lambda_2BBA():

        label("loc_2BBA")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2BBA")

    QueueWorkItem2(0x109, 2, lambda_2BBA)

    def lambda_2BCC():

        label("loc_2BCC")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2BCC")

    QueueWorkItem2(0x105, 2, lambda_2BCC)
    WaitChrThread(0x105, 1)
    WaitChrThread(0xC, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    Sound(470, 0, 50, 0)
    OP_71(0x2, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0x2)

    def lambda_2C13():

        label("loc_2C13")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2C13")

    QueueWorkItem2(0x101, 2, lambda_2C13)

    def lambda_2C25():

        label("loc_2C25")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2C25")

    QueueWorkItem2(0x102, 2, lambda_2C25)

    def lambda_2C37():

        label("loc_2C37")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2C37")

    QueueWorkItem2(0x103, 2, lambda_2C37)

    def lambda_2C49():

        label("loc_2C49")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2C49")

    QueueWorkItem2(0x104, 2, lambda_2C49)

    def lambda_2C5B():

        label("loc_2C5B")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2C5B")

    QueueWorkItem2(0x109, 2, lambda_2C5B)

    def lambda_2C6D():

        label("loc_2C6D")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2C6D")

    QueueWorkItem2(0x105, 2, lambda_2C6D)
    OP_68(2900, 1000, 10300, 5000)
    SetCameraDistance(22500, 5000)
    Sound(465, 0, 100, 0)
    OP_71(0x2, 0x79, 0xB4, 0x0, 0x20)

    def lambda_2CAB():
        OP_9B(0x1, 0xFE, 0xA, 0x61A8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2CAB)
    OP_D5(0xD, 0x0, 0x2E630, 0x0, 0x7D0)
    WaitChrThread(0xD, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    OP_6F(0x79)
    Fade(500)
    SetChrPos(0x101, 1400, 0, 21000, 180)
    SetChrPos(0x102, 2450, 0, 20750, 0)
    SetChrPos(0x103, 650, 0, 19750, 0)
    SetChrPos(0x104, 1400, 0, 19250, 0)
    SetChrPos(0x109, 1650, 0, 18250, 0)
    SetChrPos(0x105, 2900, 0, 19750, 0)
    OP_68(1680, 1000, 20360, 0)
    MoveCamera(48, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18950, 0)

    def lambda_2D8A():
        TurnDirection(0x101, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2D8A)
    Sleep(0)

    def lambda_2D9A():
        TurnDirection(0x102, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2D9A)
    Sleep(0)

    def lambda_2DAA():
        TurnDirection(0x103, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2DAA)
    Sleep(0)

    def lambda_2DBA():
        TurnDirection(0x104, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2DBA)
    Sleep(0)

    def lambda_2DCA():
        TurnDirection(0x109, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2DCA)
    Sleep(0)

    def lambda_2DDA():
        TurnDirection(0x105, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2DDA)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2ECF")

    #C0076
    ChrTalk(
        0x104,
        (
            "#00306F#12Pしかしアルカンシェルの\x01",
            "舞台装置を手がけてるってのは\x01",
            "聞いていたが……\x02\x03",

            "#00301Fああいう所を見ちまうと\x01",
            "怪しげな結社に関係している\x01",
            "工房とは思えなくなるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        "#00108F#11Pそうね……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3044")

    label("loc_2ECF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_2F56")

    #C0078
    ChrTalk(
        0x104,
        (
            "#00306F#12P……おいおい、どういう事だ？\x02\x03",

            "#00301Fアルカンシェルの舞台装置ってのは\x01",
            "あの爺さんが手がけたモンなのかよ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FCD")

    label("loc_2F56")


    #C0079
    ChrTalk(
        0x104,
        (
            "#00306F#12P……おいおい、どういう事だ？\x02\x03",

            "#00301Fアルカンシェルの舞台装置ってのは\x01",
            "この工房で造られたモンなのかよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FCD")


    #C0080
    ChrTalk(
        0x103,
        (
            "#00203F#6Pそうみたいですね。\x02\x03",

            "#00201Fワイヤーアクションといい、\x01",
            "相当高度な技術が使われているとは\x01",
            "思いましたが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3044")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0081
    ChrTalk(
        0x101,
        (
            "#00003F#5P……とりあえず\x01",
            "留守じゃなくて助かった。\x02\x03",

            "#00013F《結社》の動きについて\x01",
            "話をしてもらえるかどうか……\x01",
            "とにかく聞くだけ聞いてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x109,
        "#10101F#12Pはい……！\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x105,
        (
            "#10304F#12Pフフ……\x01",
            "虎穴に入らずんばって所かな？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetMapObjFlags(0x2, 0x4)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    SetChrPos(0x0, 1400, 0, 21000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearMapFlags(0x10000000)
    SetScenarioFlags(0x162, 2)
    EventEnd(0x5)
    Return()

    # Function_18_1D97 end

    def Function_19_3194(): pass

    label("Function_19_3194")

    OP_93(0xB, 0x0, 0x1F4)
    Sound(113, 0, 100, 0)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)

    def lambda_31B5():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_31B5)
    Sleep(1500)
    Return()

    # Function_19_3194 end

    def Function_20_31C9(): pass

    label("Function_20_31C9")

    OP_95(0xC, 2900, 0, 24300, 2000, 0x0)
    OP_95(0xC, 2900, 0, 18500, 2000, 0x0)
    OP_93(0xC, 0x5A, 0x1F4)
    Sound(464, 0, 100, 0)
    OP_71(0x2, 0x12D, 0x14A, 0x0, 0x0)
    OP_79(0x2)
    Sleep(300)

    def lambda_3215():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_3215)
    OP_95(0xC, 3900, 500, 18500, 2000, 0x0)
    WaitChrThread(0xC, 3)
    Sleep(300)
    Sound(463, 0, 100, 0)
    OP_71(0x2, 0x14B, 0x168, 0x0, 0x0)
    OP_79(0x2)
    Return()

    # Function_20_31C9 end

    def Function_21_3252(): pass

    label("Function_21_3252")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x101, 2000, 0, 25000, 0)
    SetChrPos(0x102, 2750, 0, 24750, 0)
    SetChrPos(0x103, 1250, 0, 23750, 0)
    SetChrPos(0x104, 2000, 0, 23250, 0)
    SetChrPos(0x109, 2250, 0, 22250, 0)
    SetChrPos(0x105, 3500, 0, 23750, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(2000, 1000, 25000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21200, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0084
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※一度、人形工房を訪ねると\x01",
            "  この日はクロスベル市以外の各地を\x01",
            "  訪ねる事が出来なくなってしまいます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【まだ他に用事がある】\x01",            # 0
            "【このまま人形工房を訪ねる】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_33FD"),
        (0, "loc_3D96"),
        (SWITCH_DEFAULT, "loc_3DC2"),
    )


    label("loc_33FD")

    OP_68(2000, 1000, 26000, 1500)
    OP_9B(0x1, 0x101, 0x0, 0x3E8, 0x3E8, 0x0)
    OP_6F(0x79)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0085
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは扉に付いていた鉄製のノッカーを鳴らした。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Sound(956, 0, 100, 0)
    Sleep(1200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0086
    ChrTalk(
        0x101,
        "#00003F#4S#11P──すみません！\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0087
    ChrTalk(
        0x101,
        (
            "#00003F#00001F#11Pクロスベル警察、\x01",
            "特務支援課の者です！\x02\x03",

            "マイスター・ローゼンベルク！\x01",
            "いらっしゃいますか！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(20, 10, -1, -1)
    SetChrName("老人の声")

    #A0088
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……そう大声を\x01",
            "上げずとも聞こえておる。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3698")
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetMessageWindowPos(20, 10, -1, -1)
    SetChrName("老人の声")

    #A0089
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "どうやら聞きたい事があって\x01",
            "訪ねてきたようだな。\x02\x03",

            "あまり時間は取れぬが……\x01",
            "少しの間であれば\x01",
            "話を聞いてやらんでもない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_37D2")

    label("loc_3698")

    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(20, 10, -1, -1)
    SetChrName("老人の声")

    #A0090
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "お前たちが特務支援課か。\x02\x03",

            "どうやら聞きたい事があって\x01",
            "訪ねてきたようだが……\x02\x03",

            "少しの間であれば\x01",
            "話を聞いてやらんでもない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_37D2")

    Sound(113, 0, 100, 0)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 0xFF)
    LoadChrToIndex("apl/ch51402.itc", 0x1E)
    SoundLoad(957)
    Fade(500)
    OP_90(0x8, 2000, 0, 38000, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    OP_68(1840, 600, 28950, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21340, 0)
    SetCameraDistance(18430, 3500)
    ClearChrFlags(0x8, 0x4)

    def lambda_3860():
        OP_96(0xFE, 0x7D0, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3860)
    Sound(957, 2, 40, 0)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x4)
    StopSound(957, 500, 40)
    OP_6F(0x79)

    #C0091
    ChrTalk(
        0x101,
        "#00005F#6Pえ……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x109,
        "#10109F#12P#Nか、可愛いっ……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0093
    ChrTalk(
        0x102,
        "#00112F#12P#Nローゼンベルクドール……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0094
    ChrTalk(
        0x103,
        "#00205F#6P#N……自動人形のようですが……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 5, -1, -1)
    SetChrName("老人の声")

    #A0095
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その子に案内させるから\x01",
            "中に入ってくるがいい。\x02\x03",

            "くれぐれも余計な場所に\x01",
            "入るでないぞ？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(2000, 600, 28000, 3000)
    MoveCamera(25, 16, 0, 3000)
    SetCameraDistance(19000, 3000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_6F(0x79)
    Sleep(300)

    #C0096
    ChrTalk(
        0x8,
        "#5P………………………………\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x101,
        (
            "#00012F#12Pさ、さすがに\x01",
            "喋れはしないみたいだな……？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x104,
        (
            "#00306F#12Pしっかしまあ、\x01",
            "機械仕掛けとは思えねぇぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x105,
        (
            "#10302F#12P……それで君、ご主人の所まで\x01",
            "案内してくれるのかい？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x2)
    OP_A1(0x8, 0x3E8, 0x5, 0x0, 0x1, 0x1, 0x1, 0x0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    OP_0D()
    Sleep(500)
    OP_68(1850, 1200, 29270, 8000)
    MoveCamera(35, 13, 0, 8000)
    OP_6E(510, 8000)
    SetCameraDistance(24000, 8000)
    ClearChrFlags(0x8, 0x4)
    OP_93(0x8, 0x0, 0x1F4)
    BeginChrThread(0xE, 1, 0, 24)
    OP_96(0x8, 0x7D0, 0x9C4, 0xB572, 0x7D0, 0x0)
    OP_93(0x8, 0xB4, 0x1F4)
    StopSound(957, 500, 20)
    SetChrFlags(0x8, 0x4)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0100
    ChrTalk(
        0x109,
        "#10112F#12Pい、行きましょうか。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0101
    ChrTalk(
        0x102,
        (
            "#00106F#12Pそ、そうね。\x01",
            "待たせても悪いし……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0102
    ChrTalk(
        0x101,
        (
            "#00008F#12P（《身喰らう蛇》……\x01",
            "  やっぱり底知れない相手だな。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    SetChrPos(0x0, 1420, 0, 24960, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x8, 0xFF)
    ClearMapObjFlags(0x0, 0x2)
    SetScenarioFlags(0x162, 3)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_29(0xA7, 0x1, 0x1)
    ModifyEventFlags(1, 0, 0x80)
    ClearMapObjFlags(0x1, 0x10)
    OP_10(0x1, 0x0)
    SetBarrier(0x0, 0x0, 0x1, 0x0, 2000, 2000, 46450, 5000, 2000, 0)
    OP_1B(0x0, 0x0, 0x26)
    OP_24(0x3BD)
    Sleep(500)
    EventEnd(0x5)
    SetChrFlags(0x8, 0x8000)
    Jump("loc_3DC2")

    label("loc_3D96")

    SetChrPos(0x0, 1600, 0, 24500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Jump("loc_3DC2")

    label("loc_3DC2")

    Return()

    # Function_21_3252 end

    def Function_22_3DC3(): pass

    label("Function_22_3DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DE0")
    EndChrThread(0x8, 0xFF)
    BeginChrThread(0x8, 0, 0, 35)
    Jump("loc_3DF8")

    label("loc_3DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DF8")
    EndChrThread(0x8, 0xFF)
    BeginChrThread(0x8, 0, 0, 23)

    label("loc_3DF8")

    Return()

    # Function_22_3DC3 end

    def Function_23_3DF9(): pass

    label("Function_23_3DF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3E62")
    SetScenarioFlags(0x168, 0)
    ModifyEventFlags(0, 0, 0x80)
    Sound(957, 2, 40, 0)
    OP_93(0x8, 0x0, 0x1F4)
    Sound(121, 0, 100, 0)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)
    OP_9B(0x1, 0x8, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    StopSound(957, 1000, 30)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_10(0x1, 0x1)
    SetBarrier(0x2, 0x0, 0x1)

    label("loc_3E62")

    Return()

    # Function_23_3DF9 end

    def Function_24_3E63(): pass

    label("Function_24_3E63")

    Sound(957, 2, 40, 0)
    Sleep(1000)
    OP_25(0x3BD, 0x23)
    Sleep(1000)
    OP_25(0x3BD, 0x1E)
    Sleep(1000)
    OP_25(0x3BD, 0x19)
    Sleep(1000)
    OP_25(0x3BD, 0x14)
    Return()

    # Function_24_3E63 end

    def Function_25_3E86(): pass

    label("Function_25_3E86")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51402.itc", 0x1E)
    SoundLoad(957)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x40)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x101, 2000, 2500, 48000, 180)
    SetChrPos(0x102, 1250, 2500, 48000, 180)
    SetChrPos(0x103, 2750, 2500, 48000, 180)
    SetChrPos(0x104, 2000, 2500, 48000, 180)
    SetChrPos(0x109, 1500, 2500, 48000, 180)
    SetChrPos(0x105, 250, 2500, 48000, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x8, 2000, 2500, 48000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(2000, 3100, 47000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21500, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0xA, 0xA, 0x0, 0x0)
    OP_79(0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(121, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)
    OP_68(2000, 600, 23000, 15000)
    MoveCamera(45, 25, 0, 15000)
    OP_6E(510, 15000)
    SetCameraDistance(20000, 15000)
    BeginChrThread(0x8, 1, 0, 26)
    Sleep(2000)
    BeginChrThread(0x101, 1, 0, 28)
    Sleep(500)
    BeginChrThread(0x102, 1, 0, 29)
    Sleep(500)
    BeginChrThread(0x103, 1, 0, 30)
    Sleep(500)
    BeginChrThread(0x104, 1, 0, 31)
    Sleep(300)
    BeginChrThread(0x105, 1, 0, 33)
    Sleep(500)
    BeginChrThread(0x109, 1, 0, 32)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x109, 1)
    BeginChrThread(0x8, 1, 0, 27)
    Sleep(5000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_68(2250, 600, 22100, 2000)
    MoveCamera(46, 25, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(20000, 2000)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x109, 0x2)

    def lambda_4153():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4153)
    Sleep(50)

    def lambda_4163():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4163)
    Sleep(50)

    def lambda_4173():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4173)
    Sleep(50)

    def lambda_4183():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4183)
    Sleep(50)

    def lambda_4193():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4193)
    Sleep(50)

    def lambda_41A3():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_41A3)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    #C0103
    ChrTalk(
        0x102,
        (
            "#00106F#5P……なんだか……\x01",
            "夢を見ているみたいだったわね。\x02\x03",

            "#00108F『幻焔#4Rげんえん#計画』……\x01",
            "そしてクロスベルを訪れるという\x01",
            "２人の《使徒》の存在……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x109,
        (
            "#10106F#5P正直、突拍子もなさすぎて\x01",
            "現実感がないんですが……\x02\x03",

            "#10101Fどこまでが本当なんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#00003F#12P……リベールの異変を聞く限り、\x01",
            "洒落にならない連中なのは確かだろう。\x02\x03",

            "#00008Fただ、リベールの時とは違って\x01",
            "大規模な仕掛けをしているようには\x01",
            "感じなかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x105,
        (
            "#10306F#5Pまあ、巨大な飛行戦艦まで\x01",
            "現れたっていう話だからねぇ。\x02\x03",

            "#10302Fあの《パテル＝マテル》っていう\x01",
            "巨大人形も持ち出したみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_440A():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_440A)
    Sleep(50)

    def lambda_441A():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_441A)
    Sleep(50)

    def lambda_442A():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_442A)
    Sleep(50)

    def lambda_443A():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_443A)
    Sleep(50)

    def lambda_444A():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_444A)
    Sleep(50)

    def lambda_445A():
        TurnDirection(0x105, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_445A)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0107
    ChrTalk(
        0x101,
        (
            "#00011F#11Pよく知ってるな……\x01",
            "一課の機密情報なのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x102,
        (
            "#00105F#11Pそんな事までホストの間では\x01",
            "噂が広まっているの？\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x105,
        "#10304F#6Pフフ、まあそんな所かな。\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x103,
        "#00208F#11P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x104,
        "#00303F#11P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x101, 0x104, 500)

    #C0112
    ChrTalk(
        0x101,
        "#00005F#12Pどうした、２人とも？\x02",
    )

    CloseMessageWindow()

    def lambda_45BC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_45BC)

    def lambda_45C9():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_45C9)

    def lambda_45D6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_45D6)

    def lambda_45E3():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_45E3)
    Sleep(50)

    def lambda_45F3():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_45F3)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x109, 2)

    #C0113
    ChrTalk(
        0x103,
        "#00203F#11Pいえ……\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x104,
        (
            "#00306F#5Pああ……ちょっとな。\x02\x03",

            "#00301Fティオすけの方は\x01",
            "また別の考え事みてぇだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x103,
        (
            "#00206F#11P……そうですね。\x02\x03",

            "#00201F先ほど案内してくれた\x01",
            "人形にしてもそうなのですが……\x02\x03",

            "《結社》というのはどうも、\x01",
            "遊び#4R㈲　㈲#が多い組織だと思いまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        "#00001F#12P遊びが多い……？\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x103,
        (
            "#00206F#11Pええ、エプスタイン財団や\x01",
            "ＺＣＦを上回る技術力を持ちながら\x01",
            "それを無駄に使っているような……\x02\x03",

            "#00201Fあの《パテル＝マテル》にしても\x01",
            "あんな人型兵器を実用レベルで作ったら\x01",
            "飛行艇５０隻は造れてしまいそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        "#00011F#12Pそ、そうなのか。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x102,
        (
            "#00108F#6P豊富な資金源があるのか\x01",
            "それとも……\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x109,
        (
            "#10103F#5P……でも確かに、軍隊や犯罪組織は\x01",
            "基本的に効率性重視の組織形態です。\x02\x03",

            "#10108F遊びの部分などは極力持たずに\x01",
            "目的のために冷徹に動いていく……\x02\x03",

            "#10101Fそういった合理性は\x01",
            "あまり感じられませんでしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x104,
        (
            "#00306F#5P俺が思ったのもそこでな。\x02\x03",

            "#00301Fいかに凄い技術を持っていようが\x01",
            "化物じみた連中を抱えていようが……\x02\x03",

            "《赤い星座》クラスの猟兵団や\x01",
            "《黒月》みたいなシンジケートの方が\x01",
            "現実的な脅威は上かもしれん。\x02\x03",

            "#00303Fましてや帝国、共和国みてぇな大国と\x01",
            "まともにやり合えるとも思えねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        "#00008F#12Pなるほど……\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x105,
        (
            "#10304F#5Pとなると、そうした勢力が\x01",
            "複雑な対立状況を作っている現在……\x02\x03",

            "#10300F《結社》のような連中が\x01",
            "わざわざクロスベルに来て\x01",
            "何を#4R㈲　㈲#狙っているのかが問題なわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x102,
        (
            "#00106F#6Pそうね……\x01",
            "テロリストたちを支援したのも\x01",
            "単なる気まぐれだったみたいだし。\x02\x03",

            "#00101Fどうも、現実的な勢力争いに\x01",
            "積極的に関わっているわけでは\x01",
            "なさそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x103,
        (
            "#00201F#11Pだとしたら……\x01",
            "“現実的ではない”目的のために\x01",
            "動いているという事でしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x104,
        (
            "#00306F#5Pそうなると、さすがに俺たちには\x01",
            "お手上げになっちまいそうだなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x109,
        (
            "#10108F#5Pで、でも実際に\x01",
            "何かしようと企んでいるのは\x01",
            "確かみたいですし……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0128
    ChrTalk(
        0x101,
        (
            "#00003F#12P──とにかく一度、支援課に戻ろう。\x02\x03",

            "#00001F課長には話しておきたいし、\x01",
            "警備隊やギルドにも連絡を取りたい。\x02\x03",

            "《結社》が何をするつもりでも\x01",
            "最低限、備える事はできるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4DA6():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4DA6)
    Sleep(50)

    def lambda_4DB6():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4DB6)
    Sleep(50)

    def lambda_4DC6():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4DC6)
    Sleep(50)

    def lambda_4DD6():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4DD6)
    Sleep(50)

    def lambda_4DE6():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4DE6)
    Sleep(50)

    def lambda_4DF6():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4DF6)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0129
    ChrTalk(
        0x102,
        "#00101F#5Pええ、分かったわ。\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x104,
        (
            "#00300F#5Pそんじゃあ一旦、\x01",
            "クロスベル市に戻るとすっか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x0, 860, 0, 20820, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x162, 4)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_29(0xA7, 0x1, 0x2)
    OP_29(0xA7, 0x4, 0x10)
    OP_1B(0x0, 0xFF, 0xFFFF)
    OP_24(0x3BD)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_25_3E86 end

    def Function_26_4ECE(): pass

    label("Function_26_4ECE")

    Sound(957, 2, 40, 0)

    def lambda_4ED9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4ED9)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, 2000, 0, 24000, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    StopSound(957, 100, 30)
    Sleep(500)
    Sound(957, 2, 40, 0)
    OP_95(0xFE, 3750, 0, 24000, 2000, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    SetChrFlags(0xFE, 0x4)
    ClearChrFlags(0x8, 0x40)
    StopSound(957, 500, 30)
    Return()

    # Function_26_4ECE end

    def Function_27_4F40(): pass

    label("Function_27_4F40")

    Sound(957, 2, 40, 0)
    ClearChrFlags(0xFE, 0x4)
    OP_95(0xFE, 2000, 0, 25000, 2000, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    StopSound(957, 100, 30)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x2)
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x1, 0x1, 0x0)
    SetChrChipByIndex(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x2)
    Sleep(500)
    OP_93(0xFE, 0x0, 0x1F4)
    Sound(957, 2, 40, 0)

    def lambda_4FA9():
        OP_95(0xFE, 2000, 2500, 48000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4FA9)
    Sleep(3000)
    Sound(113, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    Sleep(1500)
    StopSound(957, 4000, 30)
    WaitChrThread(0xFE, 3)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_27_4F40 end

    def Function_28_4FE9(): pass

    label("Function_28_4FE9")


    def lambda_4FEE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4FEE)
    OP_95(0xFE, 2000, 0, 20000, 2000, 0x0)

    def lambda_5013():

        label("loc_5013")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5013")

    QueueWorkItem2(0xFE, 2, lambda_5013)
    Return()

    # Function_28_4FE9 end

    def Function_29_5021(): pass

    label("Function_29_5021")


    def lambda_5026():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5026)
    OP_95(0xFE, 1000, 0, 20750, 2000, 0x0)

    def lambda_504B():

        label("loc_504B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_504B")

    QueueWorkItem2(0xFE, 2, lambda_504B)
    Return()

    # Function_29_5021 end

    def Function_30_5059(): pass

    label("Function_30_5059")


    def lambda_505E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_505E)
    OP_95(0xFE, 3000, 0, 21500, 2000, 0x0)

    def lambda_5083():

        label("loc_5083")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_5083")

    QueueWorkItem2(0xFE, 2, lambda_5083)
    Return()

    # Function_30_5059 end

    def Function_31_5091(): pass

    label("Function_31_5091")


    def lambda_5096():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5096)
    OP_95(0xFE, 2000, 0, 22000, 2000, 0x0)

    def lambda_50BB():

        label("loc_50BB")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_50BB")

    QueueWorkItem2(0xFE, 2, lambda_50BB)
    Return()

    # Function_31_5091 end

    def Function_32_50C9(): pass

    label("Function_32_50C9")


    def lambda_50CE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_50CE)
    OP_95(0xFE, 1500, 0, 23000, 2000, 0x0)

    def lambda_50F3():

        label("loc_50F3")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_50F3")

    QueueWorkItem2(0xFE, 2, lambda_50F3)
    Return()

    # Function_32_50C9 end

    def Function_33_5101(): pass

    label("Function_33_5101")


    def lambda_5106():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5106)
    OP_95(0xFE, 0, 0, 22000, 2000, 0x0)

    def lambda_512B():

        label("loc_512B")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_512B")

    QueueWorkItem2(0xFE, 2, lambda_512B)
    Return()

    # Function_33_5101 end

    def Function_34_5139(): pass

    label("Function_34_5139")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51402.itc", 0x1E)
    SoundLoad(957)
    SetChrPos(0x101, 2000, 0, 16000, 0)
    SetChrPos(0x103, 2750, 0, 14750, 0)
    SetChrPos(0x106, 1250, 0, 13750, 0)
    SetChrPos(0x105, 2000, 0, 13250, 0)
    SetChrPos(0x107, 3500, 0, 13750, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_51B2():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51B2)
    Sleep(100)

    def lambda_51CA():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_51CA)
    Sleep(100)

    def lambda_51E2():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_51E2)
    Sleep(100)

    def lambda_51FA():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_51FA)
    Sleep(100)

    def lambda_5212():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_5212)
    OP_68(2000, 2900, 39350, 0)
    MoveCamera(25, 5, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(32549, 0)
    MoveCamera(45, 20, 0, 6000)
    OP_68(2420, 1000, 25710, 6000)
    SetCameraDistance(21210, 6000)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x106, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x107, 1)
    SetChrSubChip(0x107, 0x5)
    OP_6F(0x79)

    #C0131
    ChrTalk(
        0x101,
        (
            "#00006F#11Pさてと……\x01",
            "留守にしてないといいんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x103,
        (
            "#00201F#12Pこの状況ですし、他の場所には\x01",
            "出かけていないと思いますが……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 20, -1, -1)
    SetChrName("老人の声")

    #A0133
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "うむ、出かけてはおらぬ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0134
    ChrTalk(
        0x101,
        "#00011F#12Pわっ……\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x106,
        "#10701F#12P……伝声管？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 20, -1, -1)
    SetChrName("老人の声")

    #A0136
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そろそろ来る頃だろうと\x01",
            "思っていたぞ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(113, 0, 100, 0)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x8, 0xFF)
    LoadChrToIndex("apl/ch51402.itc", 0x1E)
    SoundLoad(957)
    Fade(500)
    OP_90(0x8, 2000, 0, 38000, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    OP_68(1990, 600, 29050, 0)
    MoveCamera(0, 24, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21340, 0)
    SetCameraDistance(18430, 3500)
    ClearChrFlags(0x8, 0x4)

    def lambda_54DC():
        OP_96(0xFE, 0x7D0, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_54DC)
    Sound(957, 2, 40, 0)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x8, 1)
    SetChrFlags(0x8, 0x4)
    StopSound(957, 500, 40)
    OP_6F(0x79)

    #C0137
    ChrTalk(
        0x106,
        "#10712F#6P#N……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0138
    ChrTalk(
        0x105,
        "#10400F#6P#N案内役の人形さ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("老人の声")

    #A0139
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "入ってくるがいい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 0, -1, -1)
    SetChrName("老人の声")

    #A0140
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "言うまでもないが、\x01",
            "その子からはぐれたら\x01",
            "身の保証はできんぞ？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(2000, 600, 28000, 0)
    MoveCamera(25, 16, 0, 0)
    SetCameraDistance(19000, 0)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x2)
    OP_A1(0x8, 0x3E8, 0x5, 0x0, 0x1, 0x1, 0x1, 0x0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    OP_0D()
    Sleep(500)
    OP_68(1850, 1200, 29270, 8000)
    MoveCamera(35, 13, 0, 8000)
    OP_6E(510, 8000)
    SetCameraDistance(24000, 8000)
    BeginChrThread(0xE, 1, 0, 24)
    ClearChrFlags(0x8, 0x4)
    OP_93(0x8, 0x0, 0x1F4)
    OP_96(0x8, 0x7D0, 0x9C4, 0xB572, 0x7D0, 0x0)
    OP_93(0x8, 0xB4, 0x1F4)
    SetChrFlags(0x8, 0x4)
    StopSound(957, 300, 20)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0141
    ChrTalk(
        0x106,
        "#10710F#12P……えっと……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x107,
        "#01203F#12P#3Cフ……相変わらずだな。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        (
            "#00006F#11Pと、とりあえず\x01",
            "話が早くて助かった。\x02\x03",

            "#00000Fお邪魔させてもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x103,
        "#00202F#12Pですね。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    SetChrPos(0x0, 1250, 0, 24610, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_69(0xFF, 0x0)
    OP_4C(0x8, 0xFF)
    ClearMapObjFlags(0x0, 0x2)
    ModifyEventFlags(1, 0, 0x80)
    ClearMapObjFlags(0x1, 0x10)
    OP_10(0x1, 0x0)
    SetBarrier(0x0, 0x0, 0x1, 0x0, 2000, 2000, 46450, 5000, 2000, 0)
    SetScenarioFlags(0x1A2, 1)
    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_24(0x3BD)
    ClearMapFlags(0x10000000)
    EventEnd(0x5)
    SetChrFlags(0x8, 0x8000)
    Return()

    # Function_34_5139 end

    def Function_35_583C(): pass

    label("Function_35_583C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58A5")
    SetScenarioFlags(0x1AB, 7)
    ModifyEventFlags(0, 0, 0x80)
    Sound(957, 2, 40, 0)
    OP_93(0x8, 0x0, 0x1F4)
    Sound(121, 0, 100, 0)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)
    OP_9B(0x1, 0x8, 0x0, 0x5DC, 0x7D0, 0x0)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
    StopSound(957, 1000, 30)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_10(0x1, 0x1)
    SetBarrier(0x2, 0x0, 0x1)

    label("loc_58A5")

    Return()

    # Function_35_583C end

    def Function_36_58A6(): pass

    label("Function_36_58A6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51402.itc", 0x1E)
    SoundLoad(957)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    OP_4B(0x8, 0xFF)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0xA, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_68(2000, 600, 24500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 2000, 0, 20000, 0)
    SetChrPos(0x103, 1000, 0, 20750, 0)
    SetChrPos(0x106, 3000, 0, 21500, 0)
    SetChrPos(0x105, 2000, 0, 22300, 0)
    SetChrPos(0x107, -500, 0, 20500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x107, 0x5)
    SetChrPos(0x8, 2000, 0, 25000, 180)
    OP_68(2000, 600, 23000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x2)
    OP_A1(0x8, 0x3E8, 0x5, 0x0, 0x1, 0x1, 0x1, 0x0)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x2)
    OP_0D()
    Sleep(500)
    BeginChrThread(0x8, 1, 0, 37)
    Sleep(5000)
    OP_68(2000, 800, 21000, 2000)
    MoveCamera(46, 20, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(18500, 2000)
    SetChrFlags(0x107, 0x20)

    def lambda_5A31():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5A31)
    Sleep(50)

    def lambda_5A41():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5A41)
    Sleep(50)

    def lambda_5A51():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_5A51)
    Sleep(50)

    def lambda_5A61():
        TurnDirection(0x107, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_5A61)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x107, 0)
    ClearChrFlags(0x107, 0x20)
    OP_6F(0x79)

    #C0145
    ChrTalk(
        0x103,
        (
            "#00204F#6P話を聞ければラッキーくらいに\x01",
            "思っていましたが……\x02\x03",

            "#00202F協力までしてくれたのは\x01",
            "予想外でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        (
            "#00002F#12Pああ、《結社》とは言っても\x01",
            "色々あるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x105,
        (
            "#10406F#5Pまあ、だからこそ実態が\x01",
            "掴めていない組織なんだけどね。\x02\x03",

            "#10400Fでもあの老人に関しては\x01",
            "信用しても問題なさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x106,
        (
            "#10704F#11P……そうですね。\x01",
            "理由もあるみたいですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x107,
        (
            "#01203F#6P#3Cヨルグならばいずれ、\x01",
            "有益な情報をもたらすだろう。\x02\x03",

            "#01200Fまあ、過度な期待はせずに\x01",
            "連絡を待っているがいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#00004F#12Pああ、そうするよ。\x02\x03",

            "#00000F──さてと。\x01",
            "そろそろ鉱山町に向かうか。\x02\x03",

            "レジスタンス勢力の動向も\x01",
            "探っておきたいしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x106,
        "#10702F#11P了解しました。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x105,
        "#10402F#5Pそれじゃあ行こうか。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x0, 480, 0, 19570, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A2, 2)
    OP_29(0xAF, 0x1, 0x9)
    OP_66(0x1, 0x1)
    OP_66(0x2, 0x1)
    OP_24(0x3BD)
    EventEnd(0x5)
    Return()

    # Function_36_58A6 end

    def Function_37_5D78(): pass

    label("Function_37_5D78")

    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x1F4)
    Sound(957, 2, 40, 0)

    def lambda_5D8F():
        OP_95(0xFE, 2000, 2500, 48000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5D8F)
    Sleep(3000)
    Sound(113, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    Sleep(1500)
    StopSound(957, 4000, 30)
    WaitChrThread(0xFE, 3)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_37_5D78 end

    def Function_38_5DCF(): pass

    label("Function_38_5DCF")

    EventBegin(0x1)

    #C0153
    ChrTalk(
        0x101,
        (
            "#00001Fあまりマイスターを\x01",
            "待たせるわけにはいかない。\x01",
            "早く工房の中に入ろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 830, 0, -1070, 0)
    EventEnd(0x4)
    SetChrFlags(0x8, 0x8000)
    Return()

    # Function_38_5DCF end

    SaveToFile()

Try(main)
