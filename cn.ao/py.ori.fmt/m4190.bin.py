from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m4190.bin",                # FileName
        "m4190",                    # MapName
        "m4190",                    # Location
        0x00C8,                     # MapIndex
        "ed7351",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x28,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 200, 0, 0, 0, 1],
    )

    BuildStringList((
        "m4190",                  # 0
        "仙女龙",                 # 1
        "蔡特",                   # 2
        "矿工冈兹",               # 3
        "矿工玛尔罗",             # 4
        "矿工马库斯",             # 5
        "霍夫曼矿山长",           # 6
        "矿工罗基",               # 7
        "SE控制",                 # 8
        "bm4120",                 # 9
        "bm4120",                 # 10
    ))

    ATBonus("ATBonus_26C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_28C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_290", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_294", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_29C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_30C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_310", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_314", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_318", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_31C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_320", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_324", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_328", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_32C", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_330", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_334", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_338", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_33C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_340", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_344", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_348", 0, 0, 180)

    # monster count: 1

    BattleInfo(
        "BattleInfo_390", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "bm4120", 0x00000000, 100, 0, 0, 0,
        (
            ("ms67000.dat", "ms67000.dat", "ms67000.dat", "ms67000.dat", "ms67000.dat", "ms67000.dat", 0, 0, "MonsterBattlePostion_28C", "MonsterBattlePostion_30C", "ed7451", "ed7453", "ATBonus_26C"),
            (),
            (),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_34C", 0x0042, 3, 6, 45, 3, 3, 30, 0, "bm4120", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_32C", "MonsterBattlePostion_30C", "ed7454", "ed7000", "ATBonus_26C"),
            (),
            (),
            (),
        )
    )

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
        "monster/ch67050.itc",               # 10
        "monster/ch67050.itc",               # 11
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-390,    3710,    0,       0x18500B4,    "BattleInfo_390", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0040, 0, 43,  -0.38999998569488525,  3.7100000381469727,    -1.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   0.04874999821186066,   -0.4637500047683716,   0.25,                  1.0])

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(250, 0, [0, 1, 2, 3, 4, 5])                    # 1

    ScpFunction((
        "Function_0_49C",          # 00, 0
        "Function_1_4BD",          # 01, 1
        "Function_2_607",          # 02, 2
        "Function_3_265C",         # 03, 3
        "Function_4_26DA",         # 04, 4
        "Function_5_26F6",         # 05, 5
        "Function_6_2712",         # 06, 6
        "Function_7_272E",         # 07, 7
        "Function_8_274A",         # 08, 8
        "Function_9_27D1",         # 09, 9
        "Function_10_27FB",        # 0A, 10
        "Function_11_287E",        # 0B, 11
        "Function_12_292D",        # 0C, 12
        "Function_13_293D",        # 0D, 13
        "Function_14_294D",        # 0E, 14
        "Function_15_29A3",        # 0F, 15
        "Function_16_29F6",        # 10, 16
        "Function_17_2A4F",        # 11, 17
        "Function_18_2ABC",        # 12, 18
        "Function_19_2B15",        # 13, 19
        "Function_20_2B6B",        # 14, 20
        "Function_21_2BBB",        # 15, 21
        "Function_22_2C08",        # 16, 22
        "Function_23_2C27",        # 17, 23
        "Function_24_2C46",        # 18, 24
        "Function_25_2C65",        # 19, 25
        "Function_26_2C84",        # 1A, 26
        "Function_27_2CC2",        # 1B, 27
        "Function_28_2D17",        # 1C, 28
        "Function_29_2D4D",        # 1D, 29
        "Function_30_2E4B",        # 1E, 30
        "Function_31_2ECD",        # 1F, 31
        "Function_32_3053",        # 20, 32
        "Function_33_306F",        # 21, 33
        "Function_34_3089",        # 22, 34
        "Function_35_315B",        # 23, 35
        "Function_36_3F8E",        # 24, 36
        "Function_37_3FAD",        # 25, 37
        "Function_38_3FD9",        # 26, 38
        "Function_39_4014",        # 27, 39
        "Function_40_4040",        # 28, 40
        "Function_41_4064",        # 29, 41
        "Function_42_4090",        # 2A, 42
        "Function_43_40B4",        # 2B, 43
    ))


    def Function_0_49C(): pass

    label("Function_0_49C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4AD")
    Event(0, 2)

    label("loc_4AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_4BC")
    ClearScenarioFlags(0x22, 0)
    Event(0, 35)

    label("loc_4BC")

    Return()

    # Function_0_49C end

    def Function_1_4BD(): pass

    label("Function_1_4BD")

    SetMapObjFlags(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EA")
    ClearChrFlags(0x10, 0x80)
    ModifyEventFlags(1, 0, 0x80)
    SetChrFlags(0x10, 0x8000)

    label("loc_4EA")

    Jump("loc_4F9")

    label("loc_4EF")

    SetChrFlags(0x10, 0x80)
    ModifyEventFlags(0, 0, 0x80)

    label("loc_4F9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_540")
    SetMapObjFrame(0xFF, "flower00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "flower01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "flower04", 0x0, 0x1)

    label("loc_540")

    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_4BD end

    def Function_2_607(): pass

    label("Function_2_607")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_32(0xFF, 0xF9, 0x0)
    RemoveParty(0x4, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x104, 0x8)
    OP_32(0x3, 0x0, 0x38)
    OP_32(0x3, 0x5, 0x64)
    OP_42(0x3, 0x425, 0xFF)
    OP_42(0x3, 0x5DD, 0xFF)
    OP_42(0x3, 0x643, 0xFF)
    RemoveCraft(0x3, 0xFFFF)
    OP_38(0x3, 0x80, 0x2)
    OP_38(0x3, 0x81, 0x1)
    OP_38(0x3, 0x83, 0x1)
    OP_38(0x3, 0x84, 0x1)
    OP_38(0x3, 0x85, 0x1)
    OP_42(0x3, 0xE2, 0x0)
    OP_42(0x3, 0x84, 0x1)
    OP_42(0x3, 0x6C, 0x3)
    OP_42(0x3, 0x70, 0x4)
    OP_42(0x3, 0x64, 0x5)
    AddCraft(0x3, 0xB4)
    AddCraft(0x3, 0xB5)
    AddCraft(0x3, 0xB6)
    AddCraft(0x3, 0xB7)
    AddCraft(0x3, 0xB8)
    AddCraft(0x3, 0x127)
    AddCraft(0x3, 0x128)
    SetChrChipPat(0x3, 0x6, 0x127)
    SetChrChipPat(0x3, 0x6, 0x128)
    SetChrChipPat(0x3, 0x6, 0x12A)
    SetChrChipPat(0x3, 0x6, 0x12B)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6CE")
    AddCraft(0x3, 0x1B0)
    AddCraft(0x0, 0x1B0)
    Jump("loc_6EC")

    label("loc_6CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 5)), scpexpr(EXPR_END)), "loc_6E4")
    AddCraft(0x3, 0x19C)
    AddCraft(0x0, 0x19C)
    Jump("loc_6EC")

    label("loc_6E4")

    AddCraft(0x3, 0x188)
    AddCraft(0x0, 0x188)

    label("loc_6EC")

    AddCraft(0x1, 0x18A)
    AddCraft(0x3, 0x18A)
    AddCraft(0x0, 0x15E)
    AddCraft(0x1, 0x161)
    AddCraft(0x3, 0x167)
    AddCraft(0x8, 0x176)
    AddCraft(0x4, 0x16A)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00053.itc", 0x20)
    LoadChrToIndex("chr/ch00056.itc", 0x21)
    LoadChrToIndex("chr/ch00150.itc", 0x22)
    LoadChrToIndex("chr/ch00151.itc", 0x23)
    LoadChrToIndex("chr/ch00153.itc", 0x24)
    LoadChrToIndex("chr/ch00156.itc", 0x25)
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch02951.itc", 0x27)
    LoadChrToIndex("chr/ch02953.itc", 0x28)
    LoadChrToIndex("chr/ch02956.itc", 0x29)
    LoadChrToIndex("chr/ch03050.itc", 0x2A)
    LoadChrToIndex("chr/ch03051.itc", 0x2B)
    LoadChrToIndex("chr/ch03053.itc", 0x2C)
    LoadChrToIndex("chr/ch03056.itc", 0x2D)
    LoadChrToIndex("chr/ch00350.itc", 0x2E)
    LoadChrToIndex("chr/ch00351.itc", 0x2F)
    LoadChrToIndex("chr/ch00356.itc", 0x30)
    LoadChrToIndex("chr/ch02750.itc", 0x31)
    LoadChrToIndex("chr/ch02751.itc", 0x32)
    LoadChrToIndex("chr/ch02752.itc", 0x33)
    LoadChrToIndex("chr/ch00352.itc", 0x34)
    LoadEffect(0x0, "event/ev11010.eff")
    LoadEffect(0x1, "battle/bs011_00.eff")
    LoadEffect(0x2, "battle/bs881010.eff")
    LoadEffect(0x3, "event/eva01_01.eff")
    LoadEffect(0x4, "event/eva04_00.eff")
    LoadEffect(0x5, "event/ev11011.eff")
    LoadEffect(0x6, "battle/cr036011.eff")
    LoadEffect(0x7, "event/ev10008.eff")
    LoadEffect(0x8, "event/ev10017.eff")
    SoundLoad(2751)
    SoundLoad(2752)
    SoundLoad(825)
    SoundLoad(931)
    SoundLoad(950)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis234.itp")
    SetChrChipByIndex(0x9, 0x31)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x101, 0, 0, -61500, 0)
    SetChrPos(0x102, 1400, 0, -61500, 0)
    SetChrPos(0x109, 0, 0, -62900, 0)
    SetChrPos(0x105, 1400, 0, -62900, 0)
    SetMapObjFlags(0x0, 0x4)
    OP_68(700, 1800, -58700, 0)
    MoveCamera(37, 26, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(29850, 0)
    OP_68(0, 1300, -52500, 3500)
    SetCameraDistance(28570, 3500)
    FadeToBright(1000, 0)

    def lambda_936():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_936)
    Sleep(50)

    def lambda_94E():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_94E)
    Sleep(50)

    def lambda_966():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_966)
    Sleep(50)

    def lambda_97E():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_97E)
    OP_0D()
    MoveCamera(35, 20, 0, 2500)
    OP_6E(700, 2500)
    SetCameraDistance(27500, 2500)
    OP_6F(0x79)

    #C0001
    ChrTalk(
        0x102,
        "#00105F#11P这里是……\x02",
    )

    CloseMessageWindow()
    OP_68(790, 1500, -52520, 2500)
    MoveCamera(10, 12, 0, 2500)
    OP_6E(700, 2500)
    SetCameraDistance(19620, 2500)
    OP_6F(0x79)
    Sleep(300)

    #C0002
    ChrTalk(
        0x101,
        (
            "#00001F#6P看样子，好像是这座\x01",
            "旧矿山的尽头……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_A37():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A37)
    Sleep(50)

    def lambda_A4F():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A4F)
    Sleep(50)

    def lambda_A67():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A67)
    Sleep(50)

    def lambda_A7F():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A7F)
    Sleep(700)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    SetChrPos(0x101, -700, 0, -41000, 0)
    SetChrPos(0x102, 700, 0, -41000, 0)
    SetChrPos(0x109, -700, 0, -42400, 0)
    SetChrPos(0x105, 700, 0, -42400, 0)
    OP_68(0, 1900, -27500, 0)
    MoveCamera(25, 16, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(26620, 0)
    MoveCamera(25, 24, 0, 7000)
    Fade(500)

    def lambda_B29():
        OP_9B(0x1, 0xFE, 0x0, 0x36B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B29)
    Sleep(50)

    def lambda_B41():
        OP_9B(0x1, 0xFE, 0x0, 0x36B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B41)
    Sleep(50)

    def lambda_B59():
        OP_9B(0x1, 0xFE, 0x0, 0x36B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B59)
    Sleep(50)

    def lambda_B71():
        OP_9B(0x1, 0xFE, 0x0, 0x36B0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B71)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)
    SetChrPos(0x101, -700, 0, -10000, 0)
    SetChrPos(0x102, 700, 0, -10000, 0)
    SetChrPos(0x109, -700, 0, -11400, 0)
    SetChrPos(0x105, 700, 0, -11400, 0)
    OP_68(30, 2300, -8700, 0)
    MoveCamera(120, 8, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13960, 0)
    OP_68(0, 2300, -3200, 5500)
    MoveCamera(50, 12, 0, 5500)
    SetCameraDistance(19670, 5500)
    Fade(500)

    def lambda_C45():
        OP_9B(0x1, 0xFE, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C45)
    Sleep(50)

    def lambda_C5D():
        OP_9B(0x1, 0xFE, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C5D)
    Sleep(50)

    def lambda_C75():
        OP_9B(0x1, 0xFE, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C75)
    Sleep(50)

    def lambda_C8D():
        OP_9B(0x1, 0xFE, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C8D)
    OP_0D()
    WaitChrThread(0x101, 1)
    BeginChrThread(0x101, 3, 0, 4)
    Sleep(100)
    WaitChrThread(0x102, 1)
    BeginChrThread(0x102, 3, 0, 5)
    Sleep(100)
    WaitChrThread(0x109, 1)
    BeginChrThread(0x109, 3, 0, 6)
    Sleep(100)
    WaitChrThread(0x105, 1)
    BeginChrThread(0x105, 3, 0, 7)
    Sleep(2500)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)
    OP_68(0, 1200, -3700, 1500)
    MoveCamera(55, 18, 0, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(13700, 1500)

    def lambda_D15():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_D15)
    Sleep(350)

    def lambda_D25():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_D25)
    Sleep(150)

    def lambda_D35():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D35)
    Sleep(150)

    def lambda_D45():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_D45)
    Sleep(350)
    OP_6F(0x79)

    #C0003
    ChrTalk(
        0x109,
        (
            "#10106F#12P……直到最后也没能\x01",
            "找到其它出口啊。\x02\x03",

            "#10101F现在该怎么办？\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x101,
        (
            "#00006F#5P这个嘛……\x02\x03",

            "#00001F……虽然可能有些危险，\x01",
            "但也只能返回入口了。\x02\x03",

            "我们已经在坑道内调查了一圈，\x01",
            "似乎并没有其它机关。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x105,
        (
            "#10303F#11P话说回来，真是搞不懂啊。\x02\x03",

            "#10301F犯人设置机关\x01",
            "破坏入口，\x01",
            "究竟有何目的？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x105, 500)
    Sleep(200)

    #C0006
    ChrTalk(
        0x102,
        (
            "#00106F#5P是啊……\x01",
            "好像和矿山内部的异常状况\x01",
            "也没有什么直接关系。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x129, 4)), scpexpr(EXPR_END)), "loc_11DA")
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0007
    ChrTalk(
        0x102,
        (
            "#00101F#5P莫非是……\x01",
            "去人偶工房拜访的那两人做的？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_F71():
        TurnDirection(0x101, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F71)
    Sleep(100)

    def lambda_F81():
        TurnDirection(0x109, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F81)
    Sleep(100)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)

    #C0008
    ChrTalk(
        0x109,
        "#10111F#12P啊……\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)

    #C0009
    ChrTalk(
        0x105,
        (
            "#10301F#11P唔，那两人的举止\x01",
            "的确很可疑。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        "#00008F#6P这个嘛……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "可能性很高\x01",      # 0
            "可能性很低\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    def lambda_1063():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1063)
    Sleep(100)

    def lambda_1073():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1073)
    Sleep(100)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_109C"),
        (1, "loc_112F"),
        (SWITCH_DEFAULT, "loc_11D5"),
    )


    label("loc_109C")


    #C0011
    ChrTalk(
        0x101,
        (
            "#00006F#6P……从他们的出现时机来看，\x01",
            "这种可能性或许很高。\x02\x03",

            "#00001F但我们并不了解他们的动机，\x01",
            "所以还无法确定……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        "#00106F#11P是啊……\x02",
    )

    CloseMessageWindow()
    Jump("loc_11D5")

    label("loc_112F")

    OP_2C(0xA2, 0x1)

    #C0013
    ChrTalk(
        0x101,
        (
            "#00003F#6P不对，犯人破坏了坚固的大门，\x01",
            "又安装了那种炸药机关。\x02\x03",

            "#00001F但从外表来看，那两人\x01",
            "并不像是野蛮型的武力派人士。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        "#00106F#11P是啊，的确……\x02",
    )

    CloseMessageWindow()
    Jump("loc_11D5")

    label("loc_11D5")

    Jump("loc_11DA")

    label("loc_11DA")


    #C0015
    ChrTalk(
        0x109,
        (
            "#10108F#12P唔……\x01",
            "究竟是什么人干的呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0016
    ChrTalk(
        0x101,
        (
            "#00003F#5P（机关是在昨天布置的，\x01",
            "  支援科则是在今天接到联络的。）\x02\x03",

            "（时机未免也太巧了，简直就像是\x01",
            "  刻意针对我们一样……）\x02\x03",

            "#00008F（……是我想多了吗？）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x102, 0x101, 500)

    #C0017
    ChrTalk(
        0x102,
        "#00105F#11P罗伊德，怎么了？\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x109,
        "#10105F#12P没、没事吧？\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        (
            "#00012F#5P没什么……\x01",
            "总之，我们原路返回吧。\x02\x03",

            "#00000F说不定冈兹先生\x01",
            "已经叫来帮手了……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(-50, 2400, -3250, 0)
    MoveCamera(304, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(8750, 0)
    OP_0D()
    OP_93(0x101, 0x10E, 0x1F4)

    #C0020
    ChrTalk(
        0x101,
        "#00005F#11P（……嗯……？）\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetCameraDistance(48590, 0)
    OP_68(-20520, 2100, 2420, 0)
    MoveCamera(325, 37, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(46500, 0)
    SetCameraDistance(41350, 3000)
    Sleep(1500)

    #C0021
    ChrTalk(
        0x101,
        "#00001F#5P#N……那是……\x02",
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-50, 2100, -3250, 0)
    MoveCamera(304, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(8750, 0)
    OP_68(280, 1800, -3380, 1000)
    OP_0D()
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x105, 0x4B, 0x1F4)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0022
    ChrTalk(
        0x105,
        "#10307F#5P#4S上面！小心！\x02",
    )

    OP_6F(0x79)
    CloseMessageWindow()
    StopBGM(0x7D0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_154A():
        OP_93(0x101, 0x4B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_154A)
    Sleep(15)

    def lambda_155A():
        OP_93(0x102, 0x4B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_155A)
    Sleep(15)

    def lambda_156A():
        OP_93(0x109, 0x4B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_156A)
    Sleep(15)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)

    #C0023
    ChrTalk(
        0x101,
        "#00013F什么#5P……！？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    MoveCamera(295, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(8750, 0)
    SetChrPos(0x101, -700, 0, -4500, 75)
    SetChrPos(0x102, 700, 0, -4500, 75)
    SetChrPos(0x109, -700, 0, -5900, 75)
    SetChrPos(0x105, 700, 0, -5900, 75)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x0, 0x8)
    ClearMapObjFlags(0x0, 0x4)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x1E0, 0x20C, 0x1, 0x20)
    SetChrPos(0x8, 22000, 14000, -1500, 0)
    OP_93(0x8, 0x104, 0x0)
    SetChrFlags(0x8, 0x1)
    ClearChrFlags(0x8, 0x4)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x8, 3, 0, 8)
    BeginChrThread(0xF, 1, 0, 32)
    OP_68(8930, 3500, -2240, 0)
    MoveCamera(47, 24, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(43790, 0)
    SetCameraDistance(42790, 1000)
    Fade(500)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7454", 0)
    OP_68(6470, 3600, -3210, 1500)
    MoveCamera(62, -5, 0, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(19830, 1500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(2500)
    WaitChrThread(0x8, 3)
    ClearMapObjFlags(0x0, 0x20)
    OP_79(0x0)
    Sound(842, 0, 100, 0)
    Sound(893, 0, 80, 0)
    PlayEffect(0x8, 0x6, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x8, 3, 0, 9)
    Sleep(400)
    BeginChrThread(0x102, 3, 0, 18)
    BeginChrThread(0x105, 3, 0, 21)
    BeginChrThread(0x101, 3, 0, 19)
    BeginChrThread(0x109, 3, 0, 20)
    WaitChrThread(0x8, 3)
    BeginChrThread(0x8, 3, 0, 10)
    StopEffect(0x6, 0x2)
    Sleep(200)
    OP_68(-1760, 2100, -5530, 800)
    MoveCamera(68, 0, 0, 800)
    OP_6E(700, 800)
    SetCameraDistance(13510, 800)
    Sleep(1500)

    #C0024
    ChrTalk(
        0x109,
        "#10110F#6P#N#8A什么……\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0025
    ChrTalk(
        0x102,
        "#00107F#6P#N#12A魔、魔兽……！？\x02",
    )
    #Auto

    CloseMessageWindow()
    WaitChrThread(0x8, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x109, 3)
    CloseMessageWindow()
    OP_5A()
    OP_6F(0x79)
    OP_68(-910, 2100, -7160, 1500)
    MoveCamera(67, 9, 0, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(17710, 1500)
    BeginChrThread(0x8, 3, 0, 11)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x105, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    BeginChrThread(0x101, 3, 0, 22)
    Sleep(50)
    Sound(805, 0, 100, 0)
    BeginChrThread(0x102, 3, 0, 23)
    Sleep(50)
    Sound(531, 0, 100, 0)
    BeginChrThread(0x109, 3, 0, 24)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 25)
    Sleep(50)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    Sleep(500)

    #C0026
    ChrTalk(
        0x101,
        "#00007F#6P#N这、这是什么东西！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0027
    ChrTalk(
        0x105,
        (
            "#10310F#6P#N并不是普通的魔兽！\x01",
            "一定要小心！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    WaitChrThread(0x8, 3)
    OP_68(3340, 3800, -9280, 0)
    MoveCamera(89, 10, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14230, 0)
    OP_71(0x0, 0x78, 0x8C, 0x1, 0x0)
    Sound(842, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(2000)
    BeginChrThread(0x8, 2, 0, 12)
    BeginChrThread(0x8, 1, 0, 14)
    Fade(500)
    OP_0D()
    SetCameraDistance(19280, 1200)
    Sleep(1200)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0xA)
    SetMapObjFrame(0xFF, "m4190:Layer17", 0x0, 0x1)
    OP_68(460, 2400, -8090, 0)
    MoveCamera(340, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(33000, 0)
    MoveCamera(340, 10, 0, 2000)
    SetCameraDistance(23000, 2000)
    Fade(500)
    OP_0D()
    EndChrThread(0x8, 0x1)
    Sleep(500)
    Sleep(100)
    Sound(825, 2, 80, 0)
    Sound(931, 2, 50, 0)
    Sound(950, 2, 60, 0)
    Sleep(300)
    BeginChrThread(0x8, 3, 0, 16)
    Sleep(400)
    SetChrChipByIndex(0x101, 0x20)
    BeginChrThread(0x101, 3, 0, 26)
    PlayEffect(0x5, 0x2, 0x101, 0x1, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    SetChrChipByIndex(0x102, 0x24)
    BeginChrThread(0x102, 3, 0, 26)
    PlayEffect(0x5, 0x3, 0x102, 0x1, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    SetChrChipByIndex(0x105, 0x2C)
    BeginChrThread(0x105, 3, 0, 26)
    PlayEffect(0x5, 0x4, 0x105, 0x1, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    SetChrChipByIndex(0x109, 0x28)
    BeginChrThread(0x109, 3, 0, 26)
    PlayEffect(0x5, 0x5, 0x109, 0x1, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(150)
    OP_6F(0x79)
    SetMapObjFrame(0xFF, "m4190:Layer17", 0x1, 0x1)
    OP_68(-1270, 1800, -7100, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18170, 0)
    Fade(500)
    OP_0D()
    Sleep(200)
    BeginChrThread(0x101, 3, 0, 27)
    Sleep(150)
    BeginChrThread(0x102, 3, 0, 27)
    Sleep(150)
    BeginChrThread(0x105, 3, 0, 27)
    Sleep(150)
    BeginChrThread(0x109, 3, 0, 27)
    Sleep(150)
    Sleep(400)
    OP_71(0x0, 0x96, 0x9F, 0x1, 0x0)
    BeginChrThread(0x8, 2, 0, 13)
    Sleep(400)

    #C0028
    ChrTalk(
        0x102,
        "#00106F#6P#N呀啊啊啊！\x02",
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_5A()

    #C0029
    ChrTalk(
        0x109,
        "#10108F#6P#N身、身体无法动弹……！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0030
    ChrTalk(
        0x101,
        "#00010F#6P#N力量……为何使不出来……！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0031
    ChrTalk(
        0x105,
        (
            "#10307F#6P#N这、这波动夺去了\x01",
            "我们的力量吗……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(-1270, 1800, -7100, 4500)
    MoveCamera(145, 13, 0, 4500)
    OP_6E(700, 4500)
    SetCameraDistance(18170, 4500)
    BeginChrThread(0x8, 1, 0, 17)
    Sleep(3000)

    #C0032
    ChrTalk(
        0x105,
        "#10310F#12P#N……啧……不妙了……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0033
    ChrTalk(
        0x101,
        (
            "#00007F#12P#N可恶……\x01",
            "至少要让艾莉和诺艾尔……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0034
    ChrTalk(
        0x102,
        (
            "#00107F#6P#N别、别说\x01",
            "蠢话了……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0035
    ChrTalk(
        0x109,
        (
            "#10107F#12P#N是啊……！\x01",
            "大家一定要一起……！\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_5A()
    OP_68(-760, 2500, -8580, 1500)
    MoveCamera(147, 1, 0, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(17140, 1500)
    OP_68(-760, 2500, -8580, 0)
    MoveCamera(147, 1, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17140, 0)
    Fade(500)
    OP_71(0x0, 0x78, 0x8C, 0x1, 0x0)
    Sound(842, 0, 100, 0)
    EndChrThread(0x8, 0x1)
    BeginChrThread(0x8, 1, 0, 14)
    BeginChrThread(0x8, 2, 0, 12)
    OP_0D()
    Sleep(800)

    #C0036
    ChrTalk(
        0x101,
        "#00015F#12P#N唔……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Sound(3046, 0, 100, 0)    #voice#Zeit
    Sleep(1000)
    StopSound(931, 1000, 50)
    StopSound(950, 1000, 40)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x8, 0x3)
    BeginChrThread(0x8, 1, 0, 15)
    StopEffect(0x2, 0x2)
    PlayEffect(0x6, 0xFF, 0x101, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(211, 0, 80, 0)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    StopEffect(0x3, 0x2)
    PlayEffect(0x6, 0xFF, 0x102, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    StopEffect(0x4, 0x2)
    PlayEffect(0x6, 0xFF, 0x109, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    StopEffect(0x5, 0x2)
    PlayEffect(0x6, 0xFF, 0x105, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x102, 0x3)
    EndChrThread(0x109, 0x3)
    EndChrThread(0x105, 0x3)
    Sleep(500)
    StopSound(825, 1000, 90)

    #C0037
    ChrTalk(
        0x109,
        "#10105F#12P#N啊……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0038
    ChrTalk(
        0x101,
        "#00011F#12P#N刚、刚才那是……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    ClearChrFlags(0x104, 0x8)
    SetChrChipByIndex(0x104, 0x2E)
    SetChrPos(0x104, 1250, 0, -60500, 352)
    OP_A7(0x104, 0x0, 0x0, 0x0, 0xFF, 0x0)

    def lambda_1FFF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x104, 3, lambda_1FFF)
    OP_68(-2760, 2500, -7990, 0)
    MoveCamera(163, 14, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17140, 0)
    OP_68(-4090, 900, -33450, 2000)
    MoveCamera(153, 9, 0, 2000)
    OP_6E(700, 2000)
    SetCameraDistance(21870, 2000)
    Fade(500)
    BeginChrThread(0x104, 1, 0, 28)
    OP_0D()
    OP_6F(0x79)
    Sound(2765, 255, 100, 0)    #voice#Randy
    OP_68(-4120, 2100, -31180, 0)
    MoveCamera(95, 13, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13730, 0)
    OP_68(-6300, 1900, -25480, 1400)
    MoveCamera(95, 0, 0, 1400)
    OP_6E(700, 1400)
    SetCameraDistance(13430, 1400)
    Fade(500)
    Sleep(650)
    SetChrChip(0x0, 0x104, 0x32, 0x2EE)
    OP_0D()
    OP_6F(0x79)
    OP_68(-6300, 3000, -5480, 1600)
    MoveCamera(95, 0, 0, 1600)
    OP_6E(700, 1600)
    SetCameraDistance(13430, 1600)
    OP_6F(0x79)
    StopEffect(0x2, 0x0)
    OP_68(-4280, 3300, -6210, 500)
    MoveCamera(134, 10, 0, 500)
    OP_6E(700, 500)
    SetCameraDistance(13210, 500)
    Sleep(200)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    StopEffect(0x1, 0x2)
    EndChrThread(0x8, 0x1)
    OP_70(0x0, 0x294)
    Sleep(500)
    SetChrChip(0x1, 0x104, 0x0, 0x0)
    Sleep(500)
    Sound(591, 0, 100, 0)
    Sound(833, 0, 100, 0)
    Sound(842, 0, 100, 0)
    OP_71(0x0, 0x294, 0x2E5, 0x0, 0x0)
    BeginChrThread(0x8, 2, 0, 13)
    BeginChrThread(0x104, 3, 0, 30)
    OP_68(-2530, 600, -9630, 1500)
    MoveCamera(146, 11, 0, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(15200, 1500)
    WaitChrThread(0x104, 3)
    Sleep(1000)
    Fade(350)

    def lambda_21D6():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_21D6)
    Sleep(50)

    def lambda_21F2():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_21F2)
    Sleep(50)

    def lambda_220E():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_220E)
    Sleep(50)

    def lambda_222A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_222A)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x105, 0x2A)
    SetChrSubChip(0x105, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x101, 2)
    OP_0D()

    def lambda_2283():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2283)
    Sleep(100)

    def lambda_2293():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2293)
    Sleep(100)

    def lambda_22A3():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_22A3)
    Sleep(100)

    def lambda_22B3():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_22B3)

    #C0039
    ChrTalk(
        0x101,
        "#00002F#6P啊……！\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x109,
        "#10102F#6P兰、兰迪前辈……！？\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        "#00102F#6P你、你来了……！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -10500, 10000, -42000, 0)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-10500, 3500, -38000, 0)
    MoveCamera(217, 27, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(27390, 0)
    SetCameraDistance(23390, 0)
    Fade(500)
    SetChrPos(0x101, -5310, 0, -9830, 135)
    SetChrPos(0x109, -6130, 0, -11080, 135)
    SetChrPos(0x105, -6410, 0, -8500, 135)
    SetChrPos(0x102, -4640, 0, -6980, 135)
    TurnDirection(0x104, 0x8, 500)
    BeginChrThread(0x9, 3, 0, 31)
    OP_0D()
    OP_68(0, 1300, -10000, 3500)
    MoveCamera(135, 16, 0, 3500)
    OP_6E(700, 3500)
    SetCameraDistance(18000, 3500)
    OP_6F(0x79)
    WaitChrThread(0x9, 3)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    #Sound(3049, 255, 100, 0)    #voice#Zeit

    #C0042
    ChrTalk(
        0x9,
        "#01207F#11P#4S嗷！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0043
    ChrTalk(
        0x101,
        "#00002F#6P#N连蔡特也……！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0044
    ChrTalk(
        0x105,
        (
            "#10309F#6P#N啊哈哈！\x01",
            "出现得真是太及时了！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(2870, 2200, -10980, 3000)
    MoveCamera(100, 0, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(18860, 3000)
    WaitChrThread(0x8, 2)
    ClearMapObjFlags(0x0, 0x20)
    BeginChrThread(0x8, 1, 0, 34)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)

    #C0045
    ChrTalk(
        0x104,
        (
            "#00307F#2751V#12P#N#30W有话之后再说！\x01",
            "先把这个大家伙收拾掉！\x02\x03",

            "#2752V大家拿出全力！\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xAC0)
    OP_57(0x0)
    OP_5A()

    def lambda_252F():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_252F)
    Sleep(50)

    def lambda_253F():
        TurnDirection(0x9, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_253F)
    Sleep(50)

    def lambda_254F():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_254F)
    Sleep(50)

    def lambda_255F():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_255F)
    Sleep(50)

    def lambda_256F():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_256F)
    Sleep(50)

    def lambda_257F():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_257F)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    #Sound(2057, 255, 100, 0)    #voice#Lloyd

    #C0046
    ChrTalk(
        0x101,
        "#00007F#6P#N#30W明白了……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(2099, 255, 100, 0)    #voice#Elie

    #C0047
    ChrTalk(
        0x102,
        "#00107F#6P#N#30W交给我吧……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(4118, 255, 100, 0)    #voice#Noel

    #C0048
    ChrTalk(
        0x109,
        "#10107F#12P#N#30W准备消灭目标！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0x1016)
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    OP_24(0x339)
    OP_24(0x3A3)
    OP_24(0x3B6)
    Battle("BattleInfo_34C", 0x0, 0x0, 0x0, 0x29, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 35)
    Return()

    # Function_2_607 end

    def Function_3_265C(): pass

    label("Function_3_265C")

    SetChrPos(0x101, -4050, 0, -2840, 135)
    SetChrPos(0x102, -6150, 0, -4770, 117)
    SetChrPos(0x109, -7180, 0, -6710, 104)
    SetChrPos(0x105, -5470, 0, -7830, 100)
    SetChrPos(0x104, -4500, 50, -13000, 60)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x2A)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x102, 0x22)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0x2E)
    SetChrSubChip(0x104, 0x0)
    Return()

    # Function_3_265C end

    def Function_4_26DA(): pass

    label("Function_4_26DA")

    OP_93(0xFE, 0x13B, 0x0)
    Sleep(800)
    OP_93(0xFE, 0x0, 0x0)
    Sleep(800)
    OP_93(0xFE, 0x2D, 0x0)
    Return()

    # Function_4_26DA end

    def Function_5_26F6(): pass

    label("Function_5_26F6")

    OP_93(0xFE, 0x0, 0x0)
    Sleep(800)
    OP_93(0xFE, 0x2D, 0x0)
    Sleep(800)
    OP_93(0xFE, 0x0, 0x0)
    Return()

    # Function_5_26F6 end

    def Function_6_2712(): pass

    label("Function_6_2712")

    OP_93(0xFE, 0x2D, 0x0)
    Sleep(800)
    OP_93(0xFE, 0x0, 0x0)
    Sleep(800)
    OP_93(0xFE, 0x13B, 0x0)
    Return()

    # Function_6_2712 end

    def Function_7_272E(): pass

    label("Function_7_272E")

    OP_93(0xFE, 0x0, 0x0)
    Sleep(800)
    OP_93(0xFE, 0x2D, 0x0)
    Sleep(800)
    OP_93(0xFE, 0x13B, 0x0)
    Return()

    # Function_7_272E end

    def Function_8_274A(): pass

    label("Function_8_274A")

    OP_9C(0xFE, 0xFFFFF448, 0xFFFFC950, 0xFFFFFE0C, 0x2EE, 0x5DC)
    Sleep(500)
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
    Sleep(850)
    Return()

    # Function_8_274A end

    def Function_9_27D1(): pass

    label("Function_9_27D1")

    Sound(893, 0, 100, 0)
    OP_71(0x0, 0x20D, 0x222, 0x1, 0x0)
    OP_9C(0xFE, 0xFFFFC568, 0x0, 0xFFFFF63C, 0xFA, 0x4B0)
    Return()

    # Function_9_27D1 end

    def Function_10_27FB(): pass

    label("Function_10_27FB")

    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1750, 3250, 1750, 0xFF, 0, 0, 0, 0)
    OP_71(0x0, 0x22C, 0x253, 0x1, 0x20)
    Sound(833, 0, 100, 0)
    OP_82(0x12C, 0x1F4, 0xBB8, 0x3E8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(1500)
    OP_9C(0xFE, 0xC8, 0x0, 0x0, 0x1F4, 0x5DC)
    Return()

    # Function_10_27FB end

    def Function_11_287E(): pass

    label("Function_11_287E")


    def lambda_2883():
        OP_93(0xFE, 0x127, 0x32)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2883)
    Sound(893, 0, 70, 0)
    OP_71(0x0, 0x263, 0x28E, 0x1, 0x0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_9D(0xFE, 0x1388, 0x0, 0xFFFFD6FC, 0x6D6, 0x5DC)
    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sound(893, 0, 50, 0)
    CancelBlur(1500)
    OP_82(0x64, 0xC8, 0xBB8, 0x2BC)
    Sound(833, 0, 100, 0)
    OP_79(0x0)
    OP_71(0x0, 0xA, 0x2F, 0x0, 0x20)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_11_287E end

    def Function_12_292D(): pass

    label("Function_12_292D")

    OP_79(0x0)
    OP_71(0x0, 0x8D, 0x95, 0x0, 0x20)
    Return()

    # Function_12_292D end

    def Function_13_293D(): pass

    label("Function_13_293D")

    OP_79(0x0)
    OP_71(0x0, 0xA, 0x2F, 0x0, 0x20)
    Return()

    # Function_13_293D end

    def Function_14_294D(): pass

    label("Function_14_294D")

    Sleep(650)

    label("loc_2950")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29A2")
    Sound(665, 0, 100, 0)
    Sound(627, 0, 90, 0)
    OP_87(0x1, 0xFF, 0x0, "Null_kuchi", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(800)
    Jump("loc_2950")

    label("loc_29A2")

    Return()

    # Function_14_294D end

    def Function_15_29A3(): pass

    label("Function_15_29A3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_29F5")
    Sound(665, 0, 60, 0)
    Sound(627, 0, 50, 0)
    OP_87(0x2, 0xFF, 0x0, "Null_kuchi", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(800)
    Jump("Function_15_29A3")

    label("loc_29F5")

    Return()

    # Function_15_29A3 end

    def Function_16_29F6(): pass

    label("Function_16_29F6")

    OP_87(0x0, 0x0, 0x0, "Bone_neck02", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)

    label("loc_2A2A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A4E")
    OP_82(0x64, 0x64, 0x5DC, 0x1F4)
    Sleep(500)
    Jump("loc_2A2A")

    label("loc_2A4E")

    Return()

    # Function_16_29F6 end

    def Function_17_2A4F(): pass

    label("Function_17_2A4F")

    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(1000)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(1000)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(1000)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(1000)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(1000)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(1000)
    Return()

    # Function_17_2A4F end

    def Function_18_2ABC(): pass

    label("Function_18_2ABC")

    OP_9B(0x0, 0xFE, 0xD2, 0x5DC, 0xFA0, 0x1)
    Sound(844, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFF448, 0x0, 0xFFFFF2A4, 0x1F4, 0x5DC)
    Sound(326, 0, 100, 0)
    TurnDirection(0xFE, 0x8, 500)
    Sleep(650)
    Sleep(1000)

    def lambda_2B00():

        label("loc_2B00")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_2B00")

    QueueWorkItem2(0xFE, 2, lambda_2B00)
    Sleep(300)
    EndChrThread(0xFE, 0x2)
    Return()

    # Function_18_2ABC end

    def Function_19_2B15(): pass

    label("Function_19_2B15")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0xC3, 0x5DC, 0xFA0, 0x1)
    Sound(809, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFEC8C, 0x0, 0xFFFFEC50, 0x1F4, 0x5DC)
    TurnDirection(0xFE, 0x8, 500)
    Sleep(350)
    Sleep(1000)

    def lambda_2B56():

        label("loc_2B56")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_2B56")

    QueueWorkItem2(0xFE, 2, lambda_2B56)
    Sleep(300)
    EndChrThread(0xFE, 0x2)
    Return()

    # Function_19_2B15 end

    def Function_20_2B6B(): pass

    label("Function_20_2B6B")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0xB4, 0x5DC, 0xFA0, 0x1)
    OP_9D(0xFE, 0xFFFFE89A, 0x0, 0xFFFFE534, 0x1F4, 0x5DC)
    TurnDirection(0xFE, 0x8, 500)
    Sleep(200)
    Sleep(1000)

    def lambda_2BA6():

        label("loc_2BA6")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_2BA6")

    QueueWorkItem2(0xFE, 2, lambda_2BA6)
    Sleep(300)
    EndChrThread(0xFE, 0x2)
    Return()

    # Function_20_2B6B end

    def Function_21_2BBB(): pass

    label("Function_21_2BBB")

    OP_9B(0x0, 0xFE, 0xA5, 0x5DC, 0xFA0, 0x1)
    OP_9D(0xFE, 0xFFFFEF52, 0x0, 0xFFFFE11A, 0x1F4, 0x5DC)
    TurnDirection(0xFE, 0x8, 500)
    Sleep(500)
    Sleep(1000)

    def lambda_2BF3():

        label("loc_2BF3")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_2BF3")

    QueueWorkItem2(0xFE, 2, lambda_2BF3)
    Sleep(300)
    EndChrThread(0xFE, 0x2)
    Return()

    # Function_21_2BBB end

    def Function_22_2C08(): pass

    label("Function_22_2C08")

    TurnDirection(0xFE, 0x8, 500)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFB50, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_22_2C08 end

    def Function_23_2C27(): pass

    label("Function_23_2C27")

    TurnDirection(0xFE, 0x8, 500)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFB50, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_23_2C27 end

    def Function_24_2C46(): pass

    label("Function_24_2C46")

    TurnDirection(0xFE, 0x8, 500)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFB50, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_24_2C46 end

    def Function_25_2C65(): pass

    label("Function_25_2C65")

    TurnDirection(0xFE, 0x8, 500)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFB50, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_2C65 end

    def Function_26_2C84(): pass

    label("Function_26_2C84")

    SetChrSubChip(0xFE, 0x0)
    OP_A6(0xFE, 0x32, 0x0, 0x514, 0xBB8)

    label("loc_2C9B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2CC1")
    OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
    Sleep(100)
    Jump("loc_2C9B")

    label("loc_2CC1")

    Return()

    # Function_26_2C84 end

    def Function_27_2CC2(): pass

    label("Function_27_2CC2")

    SetChrSubChip(0xFE, 0x2)
    OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
    SetChrSubChip(0xFE, 0x3)
    OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)

    label("loc_2CF0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2D16")
    OP_A6(0xFE, 0x32, 0x0, 0x12C, 0xBB8)
    Sleep(100)
    Jump("loc_2CF0")

    label("loc_2D16")

    Return()

    # Function_27_2CC2 end

    def Function_28_2D17(): pass

    label("Function_28_2D17")

    OP_9B(0x1, 0xFE, 0x0, 0xABE0, 0x2710, 0x1)
    EndChrThread(0xFE, 0x2)
    BeginChrThread(0xFE, 3, 0, 29)
    SetChrFlags(0xFE, 0x4)
    OP_9D(0xFE, 0xFFFFEDC2, 0xCC6, 0xFFFFE26E, 0xDAC, 0x5DC)
    Return()

    # Function_28_2D17 end

    def Function_29_2D4D(): pass

    label("Function_29_2D4D")

    SetChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Sound(844, 0, 100, 0)
    Sound(251, 0, 50, 0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x320)
    Sound(2297, 255, 100, 0)    #voice#Randy
    PlayEffect(0x8, 0x6, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(532, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x12C)
    PlayEffect(0x3, 0xFF, 0xFE, 0x3, 0, 500, 500, 0, 0, 0, 1200, 1000, 1200, 0xFF, 0, 0, 0, 0)
    Sound(627, 0, 100, 0)
    Sound(246, 0, 100, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(250)
    CancelBlur(500)
    Sleep(500)
    StopEffect(0x6, 0x2)
    Return()

    # Function_29_2D4D end

    def Function_30_2E4B(): pass

    label("Function_30_2E4B")

    ClearChrFlags(0xFE, 0x4)

    def lambda_2E55():
        OP_9D(0xFE, 0xFFFFEE6C, 0x32, 0xFFFFCD38, 0xFA, 0x9C4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E55)
    Sleep(250)
    Sound(809, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x2)
    WaitChrThread(0xFE, 2)
    PlayEffect(0x4, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    Sound(326, 0, 100, 0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_30_2E4B end

    def Function_31_2ECD(): pass

    label("Function_31_2ECD")

    SetChrChipByIndex(0x9, 0x32)
    SetChrChip(0x0, 0x9, 0x32, 0x258)
    ClearChrFlags(0xFE, 0x1)
    Sound(844, 0, 100, 0)

    def lambda_2EE9():
        OP_9C(0xFE, 0x0, 0xFFFFE0C0, 0xFA0, 0xA, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2EE9)
    WaitChrThread(0xFE, 1)
    PlayEffect(0x4, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x1)
    SetChrChipByIndex(0x9, 0x31)
    Sound(845, 0, 100, 0)
    Sleep(300)
    BeginChrThread(0xF, 1, 0, 33)
    SetChrChipByIndex(0x9, 0x32)

    def lambda_2F5D():
        OP_9B(0x0, 0xFE, 0x2D, 0xDAC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F5D)
    Sleep(300)
    SetChrChip(0x1, 0x9, 0x0, 0x0)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xF, 0x1)
    SetChrChip(0x0, 0x9, 0x32, 0x2EE)
    Sound(844, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_2FCA():
        OP_9D(0xFE, 0x3E8, 0x0, 0xFFFF8EB8, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FCA)
    WaitChrThread(0xFE, 1)
    PlayEffect(0x4, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0xF, 1, 0, 33)

    def lambda_3028():
        OP_9B(0x0, 0xFE, 0x134, 0x34BC, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3028)
    Sleep(600)
    SetChrChip(0x1, 0x9, 0x0, 0x0)
    Sleep(900)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xF, 0x1)
    SetChrChipByIndex(0x9, 0x31)
    Return()

    # Function_31_2ECD end

    def Function_32_3053(): pass

    label("Function_32_3053")

    Sleep(1200)
    Sound(893, 0, 60, 0)
    Sleep(1200)
    Sound(893, 0, 60, 0)
    Sleep(1200)
    Sound(893, 0, 60, 0)
    Return()

    # Function_32_3053 end

    def Function_33_306F(): pass

    label("Function_33_306F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3088")
    Sound(845, 0, 100, 0)
    Sleep(400)
    Jump("Function_33_306F")

    label("loc_3088")

    Return()

    # Function_33_306F end

    def Function_34_3089(): pass

    label("Function_34_3089")

    OP_74(0x0, 0xF)
    OP_71(0x0, 0x127, 0x132, 0x64, 0x0)
    OP_79(0x0)
    Sound(914, 0, 100, 0)
    OP_71(0x0, 0x133, 0x142, 0x1, 0x0)

    def lambda_30B3():
        OP_93(0xFE, 0x111, 0x46)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_30B3)
    OP_9D(0xFE, 0x16F8, 0x0, 0xFFFFD5D0, 0x9C4, 0x5DC)
    OP_82(0xC8, 0x12C, 0xBB8, 0x3E8)
    PlayEffect(0x7, 0xFF, 0xFE, 0x0, 0, 0, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1)
    CancelBlur(2500)
    Sound(833, 0, 100, 0)
    WaitChrThread(0xFE, 2)
    OP_79(0x0)
    OP_71(0x0, 0x143, 0x14E, 0x1, 0x0)
    OP_79(0x0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xA, 0x2F, 0x0, 0x20)
    Return()

    # Function_34_3089 end

    def Function_35_315B(): pass

    label("Function_35_315B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch02950.itc", 0x20)
    LoadChrToIndex("chr/ch03050.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    LoadChrToIndex("chr/ch02702.itc", 0x23)
    LoadChrToIndex("chr/ch26200.itc", 0x24)
    LoadChrToIndex("chr/ch26300.itc", 0x25)
    LoadChrToIndex("chr/ch30700.itc", 0x26)
    LoadChrToIndex("chr/ch02750.itc", 0x27)
    LoadEffect(0x1, "battle\\bs000001.eff")
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00300.itp")
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
    SetChrPos(0x101, 6190, 200, -2810, 117)
    SetChrPos(0x102, 5160, 200, -4350, 90)
    SetChrPos(0x109, 5730, 0, -6260, 61)
    SetChrPos(0x105, 7720, 0, -6830, 31)
    SetChrPos(0x104, 7240, 200, -4830, 71)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 7450, 100, -8590, 31)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xD, 0x25)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xB, 0x24)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x24)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x0, 0x8)
    ClearMapObjFlags(0x0, 0x4)
    SetChrPos(0x8, 14230, 0, -4380, 0)
    OP_93(0x8, 0xFF, 0x0)
    OP_71(0x0, 0x5A, 0x6D, 0x1, 0x20)
    SetChrFlags(0x8, 0x1)
    ClearChrFlags(0x8, 0x4)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1B58), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(8350, 6800, -4680, 0)
    MoveCamera(69, 33, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(34000, 0)
    OP_68(8350, 7200, -4380, 3000)
    MoveCamera(69, 24, 0, 3000)
    SetCameraDistance(30000, 3000)
    Sound(842, 0, 100, 0)
    FadeToBright(1000, 0)
    Sleep(500)
    PlayEffect(0x1, 0x0, 0x8, 0x1, 0, -750, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sound(667, 0, 80, 0)
    Sound(843, 0, 100, 0)
    OP_6F(0x79)
    OP_75(0x0, 0x1, 0x5DC)

    def lambda_33D8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_33D8)
    OP_68(8350, 2300, -4680, 2500)
    MoveCamera(67, 15, 0, 2500)
    OP_6E(700, 2500)
    SetCameraDistance(17320, 2500)
    Sleep(1000)
    StopEffect(0x0, 0x2)
    OP_6F(0x79)
    Sleep(500)
    OP_68(8540, 600, -5200, 2000)
    MoveCamera(70, 18, 0, 2000)
    OP_6E(700, 2000)
    SetCameraDistance(15120, 2000)
    OP_6F(0x79)
    Sleep(300)

    #C0049
    ChrTalk(
        0x101,
        "#00005F#6P消、消失了……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x102,
        "#00101F#6P……刚才那究竟是……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x8, 0x80)
    SetMapObjFlags(0x0, 0x4)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    Sleep(150)
    BeginChrThread(0x9, 1, 0, 36)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sleep(300)

    def lambda_34BE():
        OP_93(0xFE, 0x104, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_34BE)
    Sleep(300)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)

    def lambda_34D6():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_34D6)
    Sleep(100)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)

    def lambda_34EE():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_34EE)
    Sleep(100)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)

    def lambda_3506():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3506)
    Sleep(100)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)

    def lambda_351E():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_351E)
    Sleep(100)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)

    def lambda_3536():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3536)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x105, 2)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0051
    AnonymousTalk(
        0x104,
        (
            "呼，看样子，似乎不是\x01",
            "普通的魔兽。\x02\x03",

            "不管怎么说，总算把它打倒了。\x02",
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

    #C0052
    ChrTalk(
        0x109,
        (
            "#10109F#12P啊哈哈……\x01",
            "不愧是兰迪前辈。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x105,
        (
            "#10302F#12P哎呀呀，\x01",
            "好惊人的战斗力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        (
            "#00012F#6P哈哈……\x01",
            "真是救了我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x102,
        "#00102F#6P不过，你们为何会……？\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x104,
        (
            "#00304F#5P哦，复健训练已经顺利完成，\x01",
            "我总算卸下了担子，\x01",
            "刚过中午时回到了支援科。\x02\x03",

            "#00300F然后听说你们\x01",
            "去了玛因兹。\x02\x03",

            "难得回来了，我就追了过来，\x01",
            "结果正赶上热闹场面呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#00000F#6P是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        (
            "#00105F#6P也就是说，\x01",
            "塌方的入口已经……？\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x104,
        (
            "#00304F#5P嗯，玛因兹的矿工们\x01",
            "全员出动，把巨石都搬走了。\x02\x03",

            "#00300F随后我就先行一步，\x01",
            "跑进来找你们……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0xD7, 0x1F4)
    Sleep(300)

    #C0060
    ChrTalk(
        0x104,
        (
            "#00302F#5P没想到这家伙突然出现，\x01",
            "把我带到了这里。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)

    def lambda_3854():
        TurnDirection(0x105, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3854)
    Sleep(100)

    def lambda_3864():
        TurnDirection(0x109, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3864)
    Sleep(100)

    def lambda_3874():
        TurnDirection(0x102, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3874)
    Sleep(100)

    def lambda_3884():
        TurnDirection(0x101, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3884)
    Sleep(100)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    Sleep(200)
    #Sound(3054, 255, 100, 0)    #voice#Zeit

    #C0061
    ChrTalk(
        0x9,
        "#01200F#11P嗷。\x02",
    )

    EndChrThread(0x9, 0x1)
    OP_A6(0x9, 0x0, 0x32, 0xC8, 0xBB8)
    SetChrSubChip(0x9, 0x0)
    Sleep(150)
    BeginChrThread(0x9, 1, 0, 36)
    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        "#00012F#5P哈哈，是这样啊……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    TurnDirection(0x105, 0x9, 500)

    #C0063
    ChrTalk(
        0x105,
        (
            "#10302F#5P哎呀呀，\x01",
            "还是如此可靠啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x102,
        "#00104F#5P蔡特，谢谢了。\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    TurnDirection(0x109, 0x9, 500)

    #C0065
    ChrTalk(
        0x109,
        (
            "#10109F#6P嗯，稍后一定要\x01",
            "买些肉作为谢礼……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 10000, 2000, -13900, 0)
    OP_A7(0xA, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #N0066
    NpcTalk(
        0xA,
        "男人的声音",
        "#1P#2S喂！你们没事吧！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    SetChrChipByIndex(0x9, 0x27)
    SetChrSubChip(0x9, 0x0)
    Sleep(200)

    def lambda_3A57():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3A57)
    WaitChrThread(0x9, 2)
    Sleep(200)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    Sleep(800)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0xA, 1000, 0, -39500, 0)
    SetChrPos(0xD, 300, 0, -41500, 0)
    SetChrPos(0xC, 1700, 0, -42000, 0)
    SetChrPos(0xB, 300, 0, -43750, 0)
    SetChrPos(0xE, 1700, 0, -44500, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xE, 0x80)
    OP_68(1720, 600, -34090, 0)
    MoveCamera(74, 24, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(22320, 0)
    OP_68(1280, 1700, -30590, 3000)
    MoveCamera(30, 14, 0, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(20270, 3500)
    Fade(500)

    def lambda_3B4B():
        OP_9B(0x0, 0xFE, 0x0, 0x55F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3B4B)
    Sleep(50)

    def lambda_3B63():
        OP_9B(0x0, 0xFE, 0x0, 0x55F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3B63)
    Sleep(50)

    def lambda_3B7B():
        OP_9B(0x0, 0xFE, 0x0, 0x55F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3B7B)
    Sleep(50)

    def lambda_3B93():
        OP_9B(0x0, 0xFE, 0x0, 0x55F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3B93)
    Sleep(50)

    def lambda_3BAB():
        OP_9B(0x0, 0xFE, 0x0, 0x55F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3BAB)
    Sleep(50)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0xE, 0x1)
    SetChrPos(0xA, 5000, 0, -15500, 0)
    SetChrPos(0xD, 4300, 0, -17500, 0)
    SetChrPos(0xC, 5700, 0, -18000, 0)
    SetChrPos(0xB, 4300, 0, -19750, 0)
    SetChrPos(0xE, 5700, 0, -20500, 0)
    OP_68(10510, -600, -5950, 0)
    MoveCamera(61, 19, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20410, 0)
    Fade(500)
    BeginChrThread(0x101, 3, 0, 37)
    BeginChrThread(0x102, 3, 0, 38)
    BeginChrThread(0x109, 3, 0, 39)
    BeginChrThread(0x105, 3, 0, 40)
    BeginChrThread(0x104, 3, 0, 41)
    BeginChrThread(0x9, 3, 0, 42)

    def lambda_3C89():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3C89)
    Sleep(50)

    def lambda_3CA1():
        OP_9B(0x0, 0xFE, 0x0, 0x1D4C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3CA1)
    Sleep(50)

    def lambda_3CB9():
        OP_9B(0x0, 0xFE, 0x0, 0x1E46, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3CB9)
    Sleep(50)

    def lambda_3CD1():
        OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3CD1)
    Sleep(50)

    def lambda_3CE9():
        OP_9B(0x0, 0xFE, 0x0, 0x203A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3CE9)
    Sleep(50)
    OP_0D()

    #C0067
    ChrTalk(
        0x101,
        "#00002F#5P冈兹先生，还有大家……\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x104,
        "#00309F#5P哦，大家辛苦啦。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 3)

    #C0069
    ChrTalk(
        0xA,
        (
            "#12P太好了……\x01",
            "你们好像都没事啊！\x02",
        )
    )

    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0x101, 3)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xE, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x9, 0x2)
    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x105,
        "#10304F#5P呵呵，多亏你们帮忙。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x102,
        (
            "#00102F#5P多谢大家这么快\x01",
            "就赶过来救我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xD,
        (
            "#12P哪里的话，毕竟是我们\x01",
            "委托你们来调查的。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xD,
        (
            "#12P真没想到旧矿山中\x01",
            "会发生这种事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xC,
        (
            "#11P这应该是我们曾祖父那代矿工\x01",
            "挖掘出来的坑道吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xB,
        (
            "#12P竟然变成这种样子了，\x01",
            "之前从没听说过……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xE,
        (
            "#11P而、而且，入口\x01",
            "为何会突然塌方呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        (
            "#00003F#5P……总之，\x01",
            "我们先回镇上吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x102,
        (
            "#00101F#5P我们需要向镇长先生报告，\x01",
            "到时一起说明一下发生在这里的所有事情。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_35_315B end

    def Function_36_3F8E(): pass

    label("Function_36_3F8E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3FAC")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_36_3F8E")

    label("loc_3FAC")

    Return()

    # Function_36_3F8E end

    def Function_37_3FAD(): pass

    label("Function_37_3FAD")

    TurnDirection(0xFE, 0xA, 500)
    Sleep(3500)
    OP_9B(0x0, 0xFE, 0x7, 0xABE, 0x3E8, 0x0)

    def lambda_3FCB():

        label("loc_3FCB")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_3FCB")

    QueueWorkItem2(0x101, 2, lambda_3FCB)
    Return()

    # Function_37_3FAD end

    def Function_38_3FD9(): pass

    label("Function_38_3FD9")

    TurnDirection(0xFE, 0xA, 500)
    Sleep(3000)
    OP_9B(0x0, 0xFE, 0x2D, 0x2EE, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0x546, 0x3E8, 0x0)

    def lambda_4006():

        label("loc_4006")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_4006")

    QueueWorkItem2(0x102, 2, lambda_4006)
    Return()

    # Function_38_3FD9 end

    def Function_39_4014(): pass

    label("Function_39_4014")

    TurnDirection(0xFE, 0xA, 500)
    Sleep(5600)
    OP_9B(0x1, 0xFE, 0x10E, 0x320, 0x3E8, 0x0)

    def lambda_4032():

        label("loc_4032")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_4032")

    QueueWorkItem2(0x109, 2, lambda_4032)
    Return()

    # Function_39_4014 end

    def Function_40_4040(): pass

    label("Function_40_4040")

    TurnDirection(0xFE, 0xA, 500)
    Sleep(1500)
    OP_93(0xFE, 0xE1, 0x1F4)

    def lambda_4056():

        label("loc_4056")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_4056")

    QueueWorkItem2(0x105, 2, lambda_4056)
    Return()

    # Function_40_4040 end

    def Function_41_4064(): pass

    label("Function_41_4064")

    TurnDirection(0xFE, 0xA, 500)
    Sleep(4000)
    OP_9B(0x1, 0xFE, 0x14A, 0x15E, 0x3E8, 0x0)

    def lambda_4082():

        label("loc_4082")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_4082")

    QueueWorkItem2(0x104, 2, lambda_4082)
    Return()

    # Function_41_4064 end

    def Function_42_4090(): pass

    label("Function_42_4090")

    TurnDirection(0xFE, 0xA, 500)
    Sleep(2800)
    OP_93(0xFE, 0xE1, 0x1F4)

    def lambda_40A6():

        label("loc_40A6")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_40A6")

    QueueWorkItem2(0x9, 2, lambda_40A6)
    Return()

    # Function_42_4090 end

    def Function_43_40B4(): pass

    label("Function_43_40B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21C, 5)), scpexpr(EXPR_END)), "loc_40BE")
    Return()

    label("loc_40BE")

    EventBegin(0x1)
    OP_52(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrSubChip(0x4, 0x0)
    SetChrSubChip(0x5, 0x0)
    SetChrSubChip(0x6, 0x0)
    SetChrSubChip(0x7, 0x0)
    SetChrName("")

    #A0079
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大型魔兽正在四处游荡。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【消灭】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_418A"),
        (SWITCH_DEFAULT, "loc_41A3"),
    )


    label("loc_418A")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, -830, 0, -2300, 181)
    EventEnd(0x5)
    Return()

    label("loc_41A3")

    Battle("BattleInfo_390", 0x0, 0x0, 0x100, 0xC, 0xFF)
    OP_E2(0x2)
    EventBegin(0x1)
    OP_68(-830, 1000, -2300, 0)
    OP_90(0x0, -830, 0, -2300, 181)
    OP_90(0x1, -830, 0, -2300, 181)
    OP_90(0x2, -830, 0, -2300, 181)
    OP_90(0x3, -830, 0, -2300, 181)
    OP_90(0x4, -830, 0, -2300, 181)
    OP_90(0x5, -830, 0, -2300, 181)
    OP_90(0x6, -830, 0, -2300, 181)
    OP_90(0x7, -830, 0, -2300, 181)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_4265"),
        (1, "loc_426A"),
        (SWITCH_DEFAULT, "loc_426D"),
    )


    label("loc_4265")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_426A")

    OP_B9(0x0)
    Return()

    label("loc_426D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-10, 1500, 2730, 0)
    MoveCamera(43, 28, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18570, 0)
    SetChrFlags(0x10, 0x80)
    OP_E2(0x3)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0080
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "消灭了通缉魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0081
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber(0xF, 1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 0, 0, 0, 0)
    SetChrPos(0x102, 0, 0, 5500, 180)
    SetChrPos(0x103, -2000, 0, 3500, 90)
    SetChrPos(0x104, -2000, 0, 1500, 90)
    SetChrPos(0x109, 2000, 0, 3500, 270)
    SetChrPos(0x105, 2000, 0, 1500, 270)
    FadeToBright(300, 0)
    OP_0D()
    Sleep(400)

    #C0082
    ChrTalk(
        0x102,
        (
            "#00104F呵呵，得到了战术书呢。\x02\x03",

            "#00100F这个战技好像很适合\x01",
            "缇欧和诺艾尔小姐吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x103,
        (
            "#00200F诺艾尔小姐，\x01",
            "我们赶快试试看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x109,
        "#10109F嗯，练习一下吧！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x2, 0x190)
    AddCraft(0x8, 0x190)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0085
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "缇欧和诺艾尔习得组合战技\x01\x07\x02",

            "『爆炸重炮』\x07\x05",
            "。\x02",
        )
    )

    CloseMessageWindow()

    #A0086
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "两人各自消耗１００点ＣＰ，\x01",
            "便可以施展威力强大的组合技攻击。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x21C, 5)
    OP_29(0x83, 0x4, 0x10)
    OP_29(0x83, 0x4, 0x2)
    OP_29(0x83, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_E2(0x2)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_43_40B4 end

    SaveToFile()

Try(main)
