from ScenarioHelper import *

def main():
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
        "领路人偶",               # 1
        "白衣男人",               # 2
        "少年",                   # 3
        "约鲁古老人",             # 4
        "海因兹",                 # 5
        "车",                     # 6
        "SE控制",                 # 7
        "玛因兹山道",             # 8
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

    PlaceName(-1.6100000143051147, 0.0, -23.0, 0x0000, 0x0000, "玛因兹山道")

    ChipFrameInfo(844, 0)                                        # 0

    ScpFunction((
        "Function_0_34C",          # 00, 0
        "Function_1_404",          # 01, 1
        "Function_2_4E4",          # 02, 2
        "Function_3_6F1",          # 03, 3
        "Function_4_750",          # 04, 4
        "Function_5_788",          # 05, 5
        "Function_6_795",          # 06, 6
        "Function_7_1A5E",         # 07, 7
        "Function_8_1A80",         # 08, 8
        "Function_9_1AA2",         # 09, 9
        "Function_10_1AC4",        # 0A, 10
        "Function_11_1AE6",        # 0B, 11
        "Function_12_1AFD",        # 0C, 12
        "Function_13_1B17",        # 0D, 13
        "Function_14_1B31",        # 0E, 14
        "Function_15_1B4B",        # 0F, 15
        "Function_16_1B74",        # 10, 16
        "Function_17_1B9D",        # 11, 17
        "Function_18_1BFD",        # 12, 18
        "Function_19_2DDA",        # 13, 19
        "Function_20_2E0F",        # 14, 20
        "Function_21_2E98",        # 15, 21
        "Function_22_3953",        # 16, 22
        "Function_23_3989",        # 17, 23
        "Function_24_39F3",        # 18, 24
        "Function_25_3A16",        # 19, 25
        "Function_26_4908",        # 1A, 26
        "Function_27_497A",        # 1B, 27
        "Function_28_4A23",        # 1C, 28
        "Function_29_4A5B",        # 1D, 29
        "Function_30_4A93",        # 1E, 30
        "Function_31_4ACB",        # 1F, 31
        "Function_32_4B03",        # 20, 32
        "Function_33_4B3B",        # 21, 33
        "Function_34_4B73",        # 22, 34
        "Function_35_524E",        # 23, 35
        "Function_36_52B8",        # 24, 36
        "Function_37_573E",        # 25, 37
        "Function_38_5795",        # 26, 38
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
            "『罗赞贝尔克工房』\x01",
            " 无关人员禁止入内。\x02",
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

    def Function_4_750(): pass

    label("Function_4_750")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_762")
    Call(0, 21)
    Return()

    label("loc_762")

    TalkBegin(0xFF)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大门牢固地关闭着。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_4_750 end

    def Function_5_788(): pass

    label("Function_5_788")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    TalkEnd(0xFF)
    Return()

    # Function_5_788 end

    def Function_6_795(): pass

    label("Function_6_795")

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
            "──真啰嗦，\x01",
            "我是不会让你进去的。\x02\x03",

            "就算你是『十三工房』的总负责人，\x01",
            "也没有擅自入内的权力。\x02",
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
            "……呵呵，也罢。\x02\x03",

            "那是Ｎｏ．ⅩⅤ的所有物，\x01",
            "我原本也没打算要强行收回。\x02\x03",

            "不过大师，您至少要把\x01",
            "相关资料全部交给我哦。\x02\x03",

            "这可是『那位大人』\x01",
            "的意思。\x02",
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
            "#03903F#5P……哼，\x01",
            "用不着你说。\x02",
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
            "#3701V#30W呵呵，你们的关系果然很差啊。\x02\x03",

            "#3702V博士也真是的，明知道人家讨厌你，\x01",
            "何必还特意过来。\x02",
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
            "#04709F#11P哈哈，这叫什么话。\x02\x03",

            "#04702F我和大师可是老交情了。\x02\x03",

            "特别是在人偶制造方面，\x01",
            "可是羁绊深厚的\x01",
            "师徒呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xB,
        (
            "#03903F#5P哼，无聊的废话就到此为止吧。\x02\x03",

            "#03900F在结社看来，我的技术\x01",
            "只是一些陈腐过时的东西罢了。\x02\x03",

            "既然已有你的『综合理论』，\x01",
            "根本就不需要再来找我帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x9,
        (
            "#04704F#11P呵呵，您太谦虚了。\x02\x03",

            "在人偶调整领域，\x01",
            "您的技术可是\x01",
            "世上无人能及。\x02\x03",

            "#04705F啊，不过……唯独那个装载在『帕蒂尔·玛蒂尔』\x01",
            "上的回路让人不敢恭维。\x02\x03",

            "#04703F装置着那种东西，\x01",
            "『歼灭天使』难得的潜能\x01",
            "可就要白白浪费掉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xB,
        "#03901F#5P……你这邪门歪道的家伙。\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        "#5P那个……打扰一下。\x02",
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

    def lambda_FD9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_FD9)
    Sleep(50)

    def lambda_FE9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_FE9)
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
        "#04705F#5P哦……？\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xA,
        (
            "#04805F#5P哎？\x01",
            "好像有客人来了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xB,
        (
            "#03903F#5P……肯帕雷拉，\x01",
            "事情已经办完了吧？\x02\x03",

            "#03900F赶快带着这个\x01",
            "令人不快的男人离开吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10DA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_10DA)
    Sleep(50)

    def lambda_10EA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_10EA)
    Sleep(300)

    #C0015
    ChrTalk(
        0xA,
        (
            "#04804F#12P呵呵，知道啦。\x02\x03",

            "#04802F好啦好啦，博士，\x01",
            "我们赶快去下一个地方吧。\x02\x03",

            "不是要在今日之内把事情办完，\x01",
            "然后回实验室的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "#04704F#11P呵呵，说的不错。\x02\x03",

            "#04702F那么，大师，\x01",
            "我们这就告辞了。\x02\x03",

            "等我把那些作品完成之后，\x01",
            "还要请您帮忙检查一下哦。\x02",
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
            "#03901F#5P#4S……真烦人！\x01",
            "赶快滚吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    #C0018
    ChrTalk(
        0xA,
        "#04809F#12P#3703V#30W呵呵，那就再见啦。\x02",
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
        "#03900F#5P……你们在那里发什么呆？\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_14B9")

    #C0020
    ChrTalk(
        0x101,
        "#00006F#12P不、不好意思。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x102,
        (
            "#00104F#12P好久不见了……\x01",
            "当时真是多谢您的通融。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xB,
        (
            "#03903F#5P是特别任务支援科啊，好久不见了。\x02\x03",

            "#03900F玲已经去利贝尔了，\x01",
            "你们还来这里做什么？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15B6")

    label("loc_14B9")


    #C0023
    ChrTalk(
        0x101,
        (
            "#00006F#12P不、不好意思。\x02\x03",

            "#00000F……初次见面，\x01",
            "我们是克洛斯贝尔警察局\x01",
            "特别任务支援科的成员。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        (
            "#00100F#12P您就是罗赞贝尔克工房\x01",
            "的主人约鲁古大师吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xB,
        (
            "#03903F#5P哼，看来玲告诉过\x01",
            "你们一些事情啊。\x02\x03",

            "#03900F玲已经去利贝尔了，\x01",
            "你们来这里做什么？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15B6")


    #C0026
    ChrTalk(
        0x101,
        (
            "#00012F#12P没什么，只是途径此地，\x01",
            "顺便来和您打个招呼。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        (
            "#00102F#12P那个……\x01",
            "在您接待客人时来访，真是打扰了。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xB,
        (
            "#03901F#5P哼，不用介意，\x01",
            "只是两个不速之客而已。\x02",
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
            "#03903F#11P你们现在似乎也没什么\x01",
            "特别的事要说。\x02\x03",

            "以后有什么\x01",
            "事情的时候再来吧。\x02\x03",

            "#03900F看在玲的面子上，我会和你们谈谈的。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#00011F#12P啊……\x02",
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
        "#10105F#12P门、门自己关上了……\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x105,
        (
            "#10308F#12P唔，虽然很古旧，\x01",
            "但好像是某种机械装置呢。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_18D1")

    #C0033
    ChrTalk(
        0x101,
        (
            "#00006F#5P嗯……\x01",
            "毕竟这里是制作\x01",
            "众多惊人的巧妙机关的地方啊。\x02\x03",

            "#00008F我觉得……\x01",
            "刚才那两名来客很令人在意。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1938")

    label("loc_18D1")


    #C0034
    ChrTalk(
        0x101,
        (
            "#00006F#5P嗯，据玲所说，\x01",
            "这里并不是单纯的人偶工房。\x02\x03",

            "#00008F我觉得……\x01",
            "刚才那两名来客很令人在意。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1938")

    TurnDirection(0x102, 0x109, 500)

    #C0035
    ChrTalk(
        0x102,
        (
            "#00103F#11P嗯，约鲁古大师\x01",
            "说他们是不速之客……\x02\x03",

            "#00108F怎么说呢……\x01",
            "总觉得很可疑。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    #C0036
    ChrTalk(
        0x109,
        (
            "#10106F#6P是啊……\x02\x03",

            "#10100F算啦，反正看上去\x01",
            "也不是什么危险人物。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x105,
        (
            "#10304F#12P（……呵呵，\x01",
            "  看上去不是危险人物吗？）\x02",
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

    # Function_6_795 end

    def Function_7_1A5E(): pass

    label("Function_7_1A5E")

    OP_9B(0x0, 0xFE, 0x4, 0x36B0, 0x7D0, 0x0)

    def lambda_1A72():

        label("loc_1A72")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1A72")

    QueueWorkItem2(0xFE, 2, lambda_1A72)
    Return()

    # Function_7_1A5E end

    def Function_8_1A80(): pass

    label("Function_8_1A80")

    OP_9B(0x0, 0xFE, 0x5, 0x3BC4, 0x7D0, 0x0)

    def lambda_1A94():

        label("loc_1A94")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1A94")

    QueueWorkItem2(0xFE, 2, lambda_1A94)
    Return()

    # Function_8_1A80 end

    def Function_9_1AA2(): pass

    label("Function_9_1AA2")

    OP_9B(0x0, 0xFE, 0x6, 0x38A4, 0x7D0, 0x0)

    def lambda_1AB6():

        label("loc_1AB6")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1AB6")

    QueueWorkItem2(0xFE, 2, lambda_1AB6)
    Return()

    # Function_9_1AA2 end

    def Function_10_1AC4(): pass

    label("Function_10_1AC4")

    OP_9B(0x0, 0xFE, 0x6, 0x3C8C, 0x7D0, 0x0)

    def lambda_1AD8():

        label("loc_1AD8")

        TurnDirection(0xFE, 0x9, 500)
        Yield()
        Jump("loc_1AD8")

    QueueWorkItem2(0xFE, 2, lambda_1AD8)
    Return()

    # Function_10_1AC4 end

    def Function_11_1AE6(): pass

    label("Function_11_1AE6")

    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
    Return()

    # Function_11_1AE6 end

    def Function_12_1AFD(): pass

    label("Function_12_1AFD")

    Sleep(50)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xE10, 0x7D0, 0x0)
    Return()

    # Function_12_1AFD end

    def Function_13_1B17(): pass

    label("Function_13_1B17")

    Sleep(100)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
    Return()

    # Function_13_1B17 end

    def Function_14_1B31(): pass

    label("Function_14_1B31")

    Sleep(150)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
    Return()

    # Function_14_1B31 end

    def Function_15_1B4B(): pass

    label("Function_15_1B4B")

    Sleep(50)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x2AF8, 0x7D0, 0x0)
    Return()

    # Function_15_1B4B end

    def Function_16_1B74(): pass

    label("Function_16_1B74")

    Sleep(250)
    OP_93(0xFE, 0xE1, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x2AF8, 0x7D0, 0x0)
    Return()

    # Function_16_1B74 end

    def Function_17_1B9D(): pass

    label("Function_17_1B9D")

    OP_9B(0x0, 0xFE, 0x0, 0x3E80, 0x9C4, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x9C4, 0x0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)

    def lambda_1BD2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1BD2)
    OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_79(0x1)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    Return()

    # Function_17_1B9D end

    def Function_18_1BFD(): pass

    label("Function_18_1BFD")

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

    def lambda_1D72():
        OP_9B(0x0, 0x101, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1D72)
    Sleep(10)

    def lambda_1D8A():
        OP_9B(0x0, 0x102, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1D8A)
    Sleep(10)

    def lambda_1DA2():
        OP_9B(0x0, 0x103, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1DA2)
    Sleep(10)

    def lambda_1DBA():
        OP_9B(0x0, 0x104, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1DBA)
    Sleep(10)

    def lambda_1DD2():
        OP_9B(0x0, 0x109, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1DD2)
    Sleep(10)

    def lambda_1DEA():
        OP_9B(0x0, 0x105, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1DEA)
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
        "#00005F#11P那是……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x103,
        "#00205F#12P运输车……？\x02",
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
            "#12P大师，\x01",
            "真是太感谢您了！\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xC,
        (
            "#12P总算能赶上\x01",
            "后天的公演了！\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xB,
        (
            "#03903F#5P真是的……\x01",
            "你们剧团每次都提出\x01",
            "这么苛刻的要求。\x02\x03",

            "调整自动人偶也就罢了，\x01",
            "竟然还要紧急定制新型舞台装置……\x02\x03",

            "#03901F我可没有那么多闲工夫啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xC,
        (
            "#12P啊哈哈……\x01",
            "真是太麻烦您了。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xC,
        (
            "#12P没办法，伊莉娅小姐\x01",
            "和剧团长的要求都很高……\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xC,
        (
            "#12P于是就加定了\x01",
            "那个机关装置。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xB,
        (
            "#03900F#5P哼，算了。\x02\x03",

            "#03903F……将我这间工房的技术\x01",
            "用于你们的舞台表演，\x01",
            "恐怕会更符合女神的意愿吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xC,
        "#12P啊、啊……？\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xC,
        "#12P对了，大师。\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xC,
        (
            "#12P我们以前也曾邀请过您很多次，\x01",
            "希望您能来观赏\x01",
            "彩虹剧团的表演……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xC,
        (
            "#12P您一直为我们提供精致的人偶\x01",
            "和舞台装置，我们很希望……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xB,
        (
            "#03903F#5P我已经收取了相应的费用。\x02\x03",

            "#03900F……而且我还很忙，\x01",
            "好意就心领了。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0xB, 3, 0, 19)

    #C0052
    ChrTalk(
        0xC,
        "#12P啊……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 3)
    OP_68(1400, 1000, 24300, 1000)
    MoveCamera(45, 25, 0, 1000)
    OP_6E(510, 1000)
    SetCameraDistance(20500, 1000)

    def lambda_2204():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2204)
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
            "#12P……唉，\x01",
            "他果然不答应啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xC,
        (
            "#12P好不容易造出了这么棒的舞台装置，\x01",
            "真希望大师能亲眼见证\x01",
            "它的实际应用啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        "#00001F……那个………\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_22DD():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_22DD)
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

    def lambda_237E():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_237E)
    Sleep(50)

    def lambda_2396():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2396)
    Sleep(50)

    def lambda_23AE():
        OP_9B(0x0, 0x103, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_23AE)
    Sleep(50)

    def lambda_23C6():
        OP_9B(0x0, 0x104, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_23C6)
    Sleep(50)

    def lambda_23DE():
        OP_9B(0x0, 0x109, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_23DE)
    Sleep(50)

    def lambda_23F6():
        OP_9B(0x0, 0x105, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_23F6)
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
            "#5P啊……\x01",
            "你们是特别任务支援科的成员吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#00000F#12P嗯，是的。\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        (
            "#00100F#12P您是彩虹剧团\x01",
            "的技师吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xC,
        (
            "#5P嗯，我是负责舞台装置\x01",
            "的海因兹。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xC,
        (
            "#5P竟然在这么特殊的地方相遇，\x01",
            "你们找大师有事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#00012F#12P嗯，稍微有点事情\x01",
            "想请教约鲁古大师。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x103,
        (
            "#00200F#12P您是来取\x01",
            "舞台装置的……？\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xC,
        (
            "#5P嗯，我们请大师帮忙\x01",
            "调整自动人偶，\x01",
            "并制作新的舞台装置。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xC,
        (
            "#5P为了赶上新版舞剧的公演日，\x01",
            "期限要求非常强人所难，\x01",
            "但大师还是按时帮我们完成了。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xC,
        (
            "#5P哎呀呀～\x01",
            "我们这些剧团成员对大师的\x01",
            "感激之情实在是难以言表。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x109,
        "#10100F#12P原来如此……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x104,
        (
            "#00309F#12P说起来，\x01",
            "彩虹剧团新版舞剧首次公演的\x01",
            "日期就是后天吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xC,
        (
            "#5P嗯，以伊莉娅小姐为代表，\x01",
            "全体团员都拿出了\x01",
            "前所未有的惊人干劲……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xC,
        (
            "#5P身为舞台装置的负责人，\x01",
            "我也必须要全力以赴。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        "#00004F#12P是吗……\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x105,
        (
            "#10302F#12P呵呵，看来表演肯定会\x01",
            "相当精彩呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xC,
        (
            "#5P啊，不能和你们继续聊了，\x01",
            "我得赶快回去布置……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xC,
        (
            "#5P各位，我先告辞啦！\x01",
            "以后再来剧场做客哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x102,
        "#00104F#12P好的，再见。\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x103,
        "#00202F#12P路上请小心。\x02",
    )

    CloseMessageWindow()

    def lambda_27F9():
        OP_9B(0x1, 0xFE, 0xE6, 0x2EE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_27F9)
    BeginChrThread(0xC, 1, 0, 20)
    OP_68(2900, 1000, 18300, 5000)
    SetCameraDistance(21500, 5000)

    def lambda_282E():

        label("loc_282E")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_282E")

    QueueWorkItem2(0x101, 2, lambda_282E)

    def lambda_2840():

        label("loc_2840")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2840")

    QueueWorkItem2(0x102, 2, lambda_2840)

    def lambda_2852():

        label("loc_2852")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2852")

    QueueWorkItem2(0x103, 2, lambda_2852)

    def lambda_2864():

        label("loc_2864")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2864")

    QueueWorkItem2(0x104, 2, lambda_2864)

    def lambda_2876():

        label("loc_2876")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2876")

    QueueWorkItem2(0x109, 2, lambda_2876)

    def lambda_2888():

        label("loc_2888")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_2888")

    QueueWorkItem2(0x105, 2, lambda_2888)
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

    def lambda_28CF():

        label("loc_28CF")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_28CF")

    QueueWorkItem2(0x101, 2, lambda_28CF)

    def lambda_28E1():

        label("loc_28E1")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_28E1")

    QueueWorkItem2(0x102, 2, lambda_28E1)

    def lambda_28F3():

        label("loc_28F3")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_28F3")

    QueueWorkItem2(0x103, 2, lambda_28F3)

    def lambda_2905():

        label("loc_2905")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2905")

    QueueWorkItem2(0x104, 2, lambda_2905)

    def lambda_2917():

        label("loc_2917")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2917")

    QueueWorkItem2(0x109, 2, lambda_2917)

    def lambda_2929():

        label("loc_2929")

        TurnDirection(0xFE, 0xD, 500)
        Yield()
        Jump("loc_2929")

    QueueWorkItem2(0x105, 2, lambda_2929)
    OP_68(2900, 1000, 10300, 5000)
    SetCameraDistance(22500, 5000)
    Sound(465, 0, 100, 0)
    OP_71(0x2, 0x79, 0xB4, 0x0, 0x20)

    def lambda_2967():
        OP_9B(0x1, 0xFE, 0xA, 0x61A8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2967)
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

    def lambda_2A46():
        TurnDirection(0x101, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2A46)
    Sleep(0)

    def lambda_2A56():
        TurnDirection(0x102, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2A56)
    Sleep(0)

    def lambda_2A66():
        TurnDirection(0x103, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2A66)
    Sleep(0)

    def lambda_2A76():
        TurnDirection(0x104, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2A76)
    Sleep(0)

    def lambda_2A86():
        TurnDirection(0x109, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2A86)
    Sleep(0)

    def lambda_2A96():
        TurnDirection(0x105, 0x101, 0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2A96)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2B79")

    #C0076
    ChrTalk(
        0x104,
        (
            "#00306F#12P说起来，\x01",
            "以前的确听说过，彩虹剧团的\x01",
            "舞台装置都是在这里定制的……\x02\x03",

            "#00301F从这方面来看，\x01",
            "很难想象这间工房会与\x01",
            "形迹可疑的结社存在关联呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        "#00108F#11P是啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2C96")

    label("loc_2B79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_2BE4")

    #C0078
    ChrTalk(
        0x104,
        (
            "#00306F#12P……喂喂，这是怎么回事？\x02\x03",

            "#00301F彩虹剧团的舞台装置\x01",
            "竟然是那个老爷爷制造的？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C41")

    label("loc_2BE4")


    #C0079
    ChrTalk(
        0x104,
        (
            "#00306F#12P……喂喂，这是怎么回事？\x02\x03",

            "#00301F彩虹剧团的舞台装置\x01",
            "竟然是在这个工房制作的？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C41")


    #C0080
    ChrTalk(
        0x103,
        (
            "#00203F#6P好像是呢。\x02\x03",

            "#00201F这里还连接着无线网络，\x01",
            "似乎拥有相当先进\x01",
            "的技术……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C96")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0081
    ChrTalk(
        0x101,
        (
            "#00003F#5P……不管怎么说，\x01",
            "还好约鲁古大师没有出门。\x02\x03",

            "#00013F不知他能否告诉我们\x01",
            "『结社』的动向……\x01",
            "总之，我们进去问问吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x109,
        "#10101F#12P嗯……！\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x105,
        (
            "#10304F#12P呵呵……这就是所谓的\x01",
            "『不入虎穴，焉得虎子』吧？\x02",
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

    # Function_18_1BFD end

    def Function_19_2DDA(): pass

    label("Function_19_2DDA")

    OP_93(0xB, 0x0, 0x1F4)
    Sound(113, 0, 100, 0)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)

    def lambda_2DFB():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2DFB)
    Sleep(1500)
    Return()

    # Function_19_2DDA end

    def Function_20_2E0F(): pass

    label("Function_20_2E0F")

    OP_95(0xC, 2900, 0, 24300, 2000, 0x0)
    OP_95(0xC, 2900, 0, 18500, 2000, 0x0)
    OP_93(0xC, 0x5A, 0x1F4)
    Sound(464, 0, 100, 0)
    OP_71(0x2, 0x12D, 0x14A, 0x0, 0x0)
    OP_79(0x2)
    Sleep(300)

    def lambda_2E5B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_2E5B)
    OP_95(0xC, 3900, 500, 18500, 2000, 0x0)
    WaitChrThread(0xC, 3)
    Sleep(300)
    Sound(463, 0, 100, 0)
    OP_71(0x2, 0x14B, 0x168, 0x0, 0x0)
    OP_79(0x2)
    Return()

    # Function_20_2E0F end

    def Function_21_2E98(): pass

    label("Function_21_2E98")

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
            "※一旦进入人偶工房，\x01",
            "  本日之内便无法前往\x01",
            "  克洛斯贝尔市以外的地区了。\x07\x00\x02",
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
            "【还有其它事情】\x01",      # 0
            "【进入人偶工房】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_3013"),
        (0, "loc_3926"),
        (SWITCH_DEFAULT, "loc_3952"),
    )


    label("loc_3013")

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
            "罗伊德叩响了大门上的铁制门环。\x07\x00\x02",
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
        "#00003F#4S#11P打扰了！\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0087
    ChrTalk(
        0x101,
        (
            "#00003F#00001F#11P我们是克洛斯贝尔警察局\x01",
            "特别任务支援科的成员。\x02\x03",

            "罗赞贝尔克大师，\x01",
            "您在里面吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(20, 10, -1, -1)
    SetChrName("老人的声音")

    #A0088
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……不用那么大声喊，\x01",
            "我也能听得到。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x30, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3270")
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
    SetChrName("老人的声音")

    #A0089
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "看来你们是有事想问，\x01",
            "才会特意来访啊。\x02\x03",

            "虽然不能给你们太多时间……\x01",
            "不过简短地谈几句\x01",
            "倒也无妨。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_339E")

    label("loc_3270")

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
    SetChrName("老人的声音")

    #A0090
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "你们就是特别任务支援科的人啊。\x02\x03",

            "看样子，似乎是有事想问，\x01",
            "才会特意来访啊……\x02\x03",

            "和你们简短地谈几句\x01",
            "倒也无妨。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_339E")

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

    def lambda_342C():
        OP_96(0xFE, 0x7D0, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_342C)
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
        "#00005F#6P哎……\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x109,
        "#10109F#12P#N好、好可爱……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0093
    ChrTalk(
        0x102,
        "#00112F#12P#N罗赞贝尔克的人偶……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0094
    ChrTalk(
        0x103,
        "#00205F#6P#N……好像是自动人偶……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 5, -1, -1)
    SetChrName("老人的声音")

    #A0095
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "那孩子会为你们带路的，\x01",
            "跟着进来就行了。\x02\x03",

            "但不要随意进入\x01",
            "一些不该进的地方。\x07\x00\x02",
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
            "#00012F#12P看、看来还没有夸张到\x01",
            "连说话都会啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x104,
        (
            "#00306F#12P不过……看上去\x01",
            "完全不像是机械装置呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x105,
        (
            "#10302F#12P……你能带我们去见\x01",
            "你的主人吗？\x02",
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
        "#10112F#12P我、我们走吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0101
    ChrTalk(
        0x102,
        (
            "#00106F#12P是、是啊，\x01",
            "让人家等太久可不好……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0102
    ChrTalk(
        0x101,
        (
            "#00008F#12P（『噬身之蛇』……\x01",
            "  果然是深不可测的对手啊。）\x02",
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
    Jump("loc_3952")

    label("loc_3926")

    SetChrPos(0x0, 1600, 0, 24500, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Jump("loc_3952")

    label("loc_3952")

    Return()

    # Function_21_2E98 end

    def Function_22_3953(): pass

    label("Function_22_3953")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3970")
    EndChrThread(0x8, 0xFF)
    BeginChrThread(0x8, 0, 0, 35)
    Jump("loc_3988")

    label("loc_3970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3988")
    EndChrThread(0x8, 0xFF)
    BeginChrThread(0x8, 0, 0, 23)

    label("loc_3988")

    Return()

    # Function_22_3953 end

    def Function_23_3989(): pass

    label("Function_23_3989")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x168, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39F2")
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

    label("loc_39F2")

    Return()

    # Function_23_3989 end

    def Function_24_39F3(): pass

    label("Function_24_39F3")

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

    # Function_24_39F3 end

    def Function_25_3A16(): pass

    label("Function_25_3A16")

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

    def lambda_3CE3():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3CE3)
    Sleep(50)

    def lambda_3CF3():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3CF3)
    Sleep(50)

    def lambda_3D03():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3D03)
    Sleep(50)

    def lambda_3D13():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3D13)
    Sleep(50)

    def lambda_3D23():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3D23)
    Sleep(50)

    def lambda_3D33():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3D33)
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
            "#00106F#5P……简直就像是……\x01",
            "做了一场梦呢。\x02\x03",

            "#00108F『幻焰计划』……\x01",
            "还有来到克洛斯贝尔\x01",
            "的两名『使徒』……\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x109,
        (
            "#10106F#5P老实说，那些情报实在是太惊人了，\x01",
            "我一时还很难消化……\x02\x03",

            "#10101F那些话真的完全可信吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        (
            "#00003F#12P……由利贝尔那场异变的传闻来看，\x01",
            "他们的确是一群不可忽视的家伙。\x02\x03",

            "#00008F但和利贝尔那时的情况不同，\x01",
            "他们这次似乎并没有\x01",
            "采取大规模的行动……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x105,
        (
            "#10306F#5P嗯，据说当时连\x01",
            "巨大的飞行战舰都动用了。\x02\x03",

            "#10302F那个名为『帕蒂尔·玛蒂尔』\x01",
            "的巨大智能兵器好像也出动了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3F40():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3F40)
    Sleep(50)

    def lambda_3F50():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3F50)
    Sleep(50)

    def lambda_3F60():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3F60)
    Sleep(50)

    def lambda_3F70():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3F70)
    Sleep(50)

    def lambda_3F80():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3F80)
    Sleep(50)

    def lambda_3F90():
        TurnDirection(0x105, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3F90)
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
            "#00011F#11P你竟然知道这么多……\x01",
            "那可是一科的机密情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x102,
        (
            "#00105F#11P那种事情的传闻\x01",
            "也流传在男公关的圈子里吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x105,
        "#10304F#6P呵呵，可以这么说吧。\x02",
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
        "#00005F#12P你们两个怎么了？\x02",
    )

    CloseMessageWindow()

    def lambda_40E6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_40E6)

    def lambda_40F3():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_40F3)

    def lambda_4100():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4100)

    def lambda_410D():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_410D)
    Sleep(50)

    def lambda_411D():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_411D)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x109, 2)

    #C0113
    ChrTalk(
        0x103,
        "#00203F#11P没什么……\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x104,
        (
            "#00306F#5P嗯……只是在想些事情而已。\x02\x03",

            "#00301F看样子，阿缇好像也在\x01",
            "思考其它的事情吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x103,
        (
            "#00206F#11P……是的。\x02\x03",

            "#00201F从之前给我们带路的\x01",
            "那个人偶也能看出……\x02\x03",

            "『结社』这个组织\x01",
            "过于随意了。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        "#00001F#12P过于随意……？\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x103,
        (
            "#00206F#11P嗯，他们明明拥有远超\x01",
            "爱普斯泰恩财团和蔡斯中央工房的技术力，\x01",
            "却总是随意运用在无关紧要的方面……\x02\x03",

            "#00201F那个『帕蒂尔·玛蒂尔』也是一样，\x01",
            "如果想把那种智能兵器改进到可以实际应用的程度，\x01",
            "所需消耗的成本恐怕可以制造五十艘飞艇了。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        "#00011F#12P是、是吗？\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x102,
        (
            "#00108F#6P难道他们拥有非常充足的资金吗？\x01",
            "还是说……\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x109,
        (
            "#10103F#5P……的确，一般来说，\x01",
            "军队和犯罪组织都很注重效率性。\x02\x03",

            "#10108F为了达到目的，必须保持绝对冷静，\x01",
            "不必要方面的消耗一定要极力控制……\x02\x03",

            "#10101F而『结社』这个组织\x01",
            "却明显没有那种合理性呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x104,
        (
            "#00306F#5P我刚才思考的也是这个问题。\x02\x03",

            "#00301F虽说他们拥有惊人的技术力，\x01",
            "以及众多怪物般的强大成员……\x02\x03",

            "但看样子，\x01",
            "也许还是『赤色星座』那种顶级猎兵团\x01",
            "和『黑月』那种犯罪组织的实际威胁更大。\x02\x03",

            "#00303F而且，我想『结社』应该也不会真正\x01",
            "与帝国、共和国那样的大国勾结在一起。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        "#00008F#12P原来如此……\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x105,
        (
            "#10304F#5P那现在的问题就是，\x01",
            "在各方势力已经形成了复杂对立关系的情况下……\x02\x03",

            "#10300F『结社』的那些家伙\x01",
            "特意赶在这种时期\x01",
            "来到克洛斯贝尔，究竟有何目的。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x102,
        (
            "#00106F#6P是啊……\x01",
            "『结社』支援那些恐怖分子\x01",
            "似乎也只是一时兴起。\x02\x03",

            "#00101F好像并没有\x01",
            "积极参与\x01",
            "那些势力斗争。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x103,
        (
            "#00201F#11P既然如此……\x01",
            "它会不会是为了『非现实』\x01",
            "的目的而行动呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x104,
        (
            "#00306F#5P如果真是那样的话，\x01",
            "我们可就无从着手了。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x109,
        (
            "#10108F#5P但、但是，从目前来看，\x01",
            "『结社』明显是\x01",
            "有着某种企图……\x02",
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
            "#00003F#12P总之，我们先回支援科吧。\x02\x03",

            "#00001F首先要和科长讨论一下，\x01",
            "另外也要联络警备队和游击士协会。\x02\x03",

            "无论『结社』今后展开什么行动，\x01",
            "我们至少要有所准备。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_47F6():
        TurnDirection(0x101, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_47F6)
    Sleep(50)

    def lambda_4806():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4806)
    Sleep(50)

    def lambda_4816():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4816)
    Sleep(50)

    def lambda_4826():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4826)
    Sleep(50)

    def lambda_4836():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4836)
    Sleep(50)

    def lambda_4846():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4846)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0129
    ChrTalk(
        0x102,
        "#00101F#5P嗯，明白了。\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x104,
        (
            "#00300F#5P那我们这就回\x01",
            "克洛斯贝尔市吧。\x02",
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

    # Function_25_3A16 end

    def Function_26_4908(): pass

    label("Function_26_4908")

    Sound(957, 2, 40, 0)

    def lambda_4913():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4913)
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

    # Function_26_4908 end

    def Function_27_497A(): pass

    label("Function_27_497A")

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

    def lambda_49E3():
        OP_95(0xFE, 2000, 2500, 48000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_49E3)
    Sleep(3000)
    Sound(113, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    Sleep(1500)
    StopSound(957, 4000, 30)
    WaitChrThread(0xFE, 3)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_27_497A end

    def Function_28_4A23(): pass

    label("Function_28_4A23")


    def lambda_4A28():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4A28)
    OP_95(0xFE, 2000, 0, 20000, 2000, 0x0)

    def lambda_4A4D():

        label("loc_4A4D")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4A4D")

    QueueWorkItem2(0xFE, 2, lambda_4A4D)
    Return()

    # Function_28_4A23 end

    def Function_29_4A5B(): pass

    label("Function_29_4A5B")


    def lambda_4A60():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4A60)
    OP_95(0xFE, 1000, 0, 20750, 2000, 0x0)

    def lambda_4A85():

        label("loc_4A85")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4A85")

    QueueWorkItem2(0xFE, 2, lambda_4A85)
    Return()

    # Function_29_4A5B end

    def Function_30_4A93(): pass

    label("Function_30_4A93")


    def lambda_4A98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4A98)
    OP_95(0xFE, 3000, 0, 21500, 2000, 0x0)

    def lambda_4ABD():

        label("loc_4ABD")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4ABD")

    QueueWorkItem2(0xFE, 2, lambda_4ABD)
    Return()

    # Function_30_4A93 end

    def Function_31_4ACB(): pass

    label("Function_31_4ACB")


    def lambda_4AD0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4AD0)
    OP_95(0xFE, 2000, 0, 22000, 2000, 0x0)

    def lambda_4AF5():

        label("loc_4AF5")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4AF5")

    QueueWorkItem2(0xFE, 2, lambda_4AF5)
    Return()

    # Function_31_4ACB end

    def Function_32_4B03(): pass

    label("Function_32_4B03")


    def lambda_4B08():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4B08)
    OP_95(0xFE, 1500, 0, 23000, 2000, 0x0)

    def lambda_4B2D():

        label("loc_4B2D")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4B2D")

    QueueWorkItem2(0xFE, 2, lambda_4B2D)
    Return()

    # Function_32_4B03 end

    def Function_33_4B3B(): pass

    label("Function_33_4B3B")


    def lambda_4B40():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4B40)
    OP_95(0xFE, 0, 0, 22000, 2000, 0x0)

    def lambda_4B65():

        label("loc_4B65")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_4B65")

    QueueWorkItem2(0xFE, 2, lambda_4B65)
    Return()

    # Function_33_4B3B end

    def Function_34_4B73(): pass

    label("Function_34_4B73")

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

    def lambda_4BEC():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4BEC)
    Sleep(100)

    def lambda_4C04():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4C04)
    Sleep(100)

    def lambda_4C1C():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4C1C)
    Sleep(100)

    def lambda_4C34():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4C34)
    Sleep(100)

    def lambda_4C4C():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_4C4C)
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
            "#00006F#11P嗯……\x01",
            "希望约鲁古大师没有外出。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x103,
        (
            "#00201F#12P在这种状况下，\x01",
            "应该也没有其它地方可去吧……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 20, -1, -1)
    SetChrName("老人的声音")

    #A0133
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，我没有外出。\x07\x00\x02",
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
        "#00011F#12P哇……\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x106,
        "#10701F#12P……传声管？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 20, -1, -1)
    SetChrName("老人的声音")

    #A0136
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我已经料到\x01",
            "你们快要来了。\x07\x00\x02",
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

    def lambda_4EEC():
        OP_96(0xFE, 0x7D0, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4EEC)
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
        "#10400F#6P#N是领路人偶。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 20, -1, -1)
    SetChrName("老人的声音")

    #A0139
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "进来吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 0, -1, -1)
    SetChrName("老人的声音")

    #A0140
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我想已经不必再提醒了，\x01",
            "如果你们和那孩子走散，\x01",
            "我可不能保证你们的人身安全。\x07\x00\x02",
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
        "#10710F#12P……那个……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x107,
        "#01203F#12P#3C呵……他还是老样子啊。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        (
            "#00006F#11P不、不管怎么说，\x01",
            "至少很爽快地同意我们入内了。\x02\x03",

            "#00000F我们这就进去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x103,
        "#00202F#12P嗯。\x02",
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

    # Function_34_4B73 end

    def Function_35_524E(): pass

    label("Function_35_524E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_52B7")
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

    label("loc_52B7")

    Return()

    # Function_35_524E end

    def Function_36_52B8(): pass

    label("Function_36_52B8")

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

    def lambda_5443():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5443)
    Sleep(50)

    def lambda_5453():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5453)
    Sleep(50)

    def lambda_5463():
        TurnDirection(0x106, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_5463)
    Sleep(50)

    def lambda_5473():
        TurnDirection(0x107, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_5473)
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
            "#00204F#6P本以为只要能探听到\x01",
            "一些消息就算幸运了……\x02\x03",

            "#00202F没想到大师竟然愿意协助我们，\x01",
            "这真是出乎意料呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x101,
        (
            "#00002F#12P嗯，看来就算是『结社』的成员，\x01",
            "也不能一概而论。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x105,
        (
            "#10406F#5P不过也正因如此，才无法掌握\x01",
            "那个组织的情况啊。\x02\x03",

            "#10400F话说回来，我觉得那位老人的话\x01",
            "还是可以相信的。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x106,
        (
            "#10704F#11P……是啊，\x01",
            "他也有帮助我们的理由。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x107,
        (
            "#01203F#6P#3C凭约鲁古的能力，\x01",
            "迟早能为我们带来有用的情报。\x02\x03",

            "#01200F但也不要太过期待，\x01",
            "耐心等待他的联络就好。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#00004F#12P嗯，说的对。\x02\x03",

            "#00000F好，那我们这就\x01",
            "去矿山镇吧。\x02\x03",

            "我很想去探查\x01",
            "反抗势力的动向。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x106,
        "#10702F#11P明白了。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x105,
        "#10402F#5P那我们就出发吧。\x02",
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

    # Function_36_52B8 end

    def Function_37_573E(): pass

    label("Function_37_573E")

    ClearChrFlags(0xFE, 0x4)
    OP_93(0xFE, 0x0, 0x1F4)
    Sound(957, 2, 40, 0)

    def lambda_5755():
        OP_95(0xFE, 2000, 2500, 48000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5755)
    Sleep(3000)
    Sound(113, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x0)
    Sleep(1500)
    StopSound(957, 4000, 30)
    WaitChrThread(0xFE, 3)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_37_573E end

    def Function_38_5795(): pass

    label("Function_38_5795")

    EventBegin(0x1)

    #C0153
    ChrTalk(
        0x101,
        (
            "#00001F不能让大师\x01",
            "等我们太久，\x01",
            "还是赶快进工房吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 830, 0, -1070, 0)
    EventEnd(0x4)
    SetChrFlags(0x8, 0x8000)
    Return()

    # Function_38_5795 end

    SaveToFile()

Try(main)
