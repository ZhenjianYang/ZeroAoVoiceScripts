from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r4090.bin",                # FileName
        "r4090",                    # MapName
        "r4090",                    # Location
        0x00A6,                     # MapIndex
        "ed7354",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x26,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 166, 0, 0, 0, 1],
    )

    BuildStringList((
        "r4090",                  # 0
        "警備隊員",               # 1
        "警備隊員",               # 2
        "警備隊員",               # 3
        "警備隊員",               # 4
        "警備隊員",               # 5
        "警備隊員",               # 6
        "魔人ヴァルド",           # 7
        "ミレイユ三尉",           # 8
        "国防軍兵士",             # 9
        "国防軍兵士",             # 10
        "国防軍兵士",             # 11
        "国防軍兵士",             # 12
        "国防軍兵士",             # 13
        "国防軍兵士",             # 14
        "国防軍兵士",             # 15
        "国防軍隊長",             # 16
        "ツァイト",               # 17
        "倒木",                   # 18
        "倒木",                   # 19
        "倒木",                   # 20
        "汎用ダミー",             # 21
        "SE制御",                 # 22
        "br4020",                 # 23
        "br4020",                 # 24
    ))

    ATBonus("ATBonus_32C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_3EC", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3CC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3D0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3D4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 5, 5, 45)

    # monster count: 0

    # event battle count: 2

    BattleInfo(
        "BattleInfo_450", 0x11C2, 0, 6, 0, 0, 255, 0, 0, "br4020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_3CC", "ed7455", "ed7453", "ATBonus_32C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_40C", 0x00E2, 0, 6, 0, 0, 255, 0, 0, "br4020", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_3CC", "ed7455", "ed7453", "ATBonus_32C"),
            (),
            (),
            (),
        )
    )

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(1464, 0)                                       # 0

    ScpFunction((
        "Function_0_5B8",          # 00, 0
        "Function_1_5F3",          # 01, 1
        "Function_2_62C",          # 02, 2
        "Function_3_1E16",         # 03, 3
        "Function_4_1E3E",         # 04, 4
        "Function_5_1E66",         # 05, 5
        "Function_6_1E8E",         # 06, 6
        "Function_7_1EB6",         # 07, 7
        "Function_8_1EDE",         # 08, 8
        "Function_9_1F06",         # 09, 9
        "Function_10_1F17",        # 0A, 10
        "Function_11_1F37",        # 0B, 11
        "Function_12_1F5B",        # 0C, 12
        "Function_13_1F7B",        # 0D, 13
        "Function_14_1FC1",        # 0E, 14
        "Function_15_3CE9",        # 0F, 15
        "Function_16_3D13",        # 10, 16
        "Function_17_3D3D",        # 11, 17
        "Function_18_3DF3",        # 12, 18
        "Function_19_3EB5",        # 13, 19
        "Function_20_3F61",        # 14, 20
        "Function_21_4007",        # 15, 21
        "Function_22_40A7",        # 16, 22
        "Function_23_4153",        # 17, 23
        "Function_24_4209",        # 18, 24
        "Function_25_433C",        # 19, 25
        "Function_26_435C",        # 1A, 26
        "Function_27_437C",        # 1B, 27
        "Function_28_439C",        # 1C, 28
        "Function_29_43BC",        # 1D, 29
        "Function_30_43DC",        # 1E, 30
        "Function_31_43FC",        # 1F, 31
        "Function_32_4426",        # 20, 32
        "Function_33_444A",        # 21, 33
        "Function_34_446E",        # 22, 34
        "Function_35_4492",        # 23, 35
        "Function_36_44B6",        # 24, 36
        "Function_37_44DA",        # 25, 37
        "Function_38_4509",        # 26, 38
        "Function_39_4532",        # 27, 39
        "Function_40_455B",        # 28, 40
        "Function_41_4584",        # 29, 41
        "Function_42_45AD",        # 2A, 42
        "Function_43_45D6",        # 2B, 43
        "Function_44_45FF",        # 2C, 44
        "Function_45_4622",        # 2D, 45
        "Function_46_6377",        # 2E, 46
        "Function_47_63B9",        # 2F, 47
        "Function_48_63FB",        # 30, 48
        "Function_49_643D",        # 31, 49
        "Function_50_647F",        # 32, 50
        "Function_51_64C1",        # 33, 51
        "Function_52_6517",        # 34, 52
        "Function_53_6559",        # 35, 53
        "Function_54_659B",        # 36, 54
        "Function_55_65A9",        # 37, 55
        "Function_56_65BF",        # 38, 56
        "Function_57_65F5",        # 39, 57
        "Function_58_664A",        # 3A, 58
        "Function_59_674A",        # 3B, 59
        "Function_60_6858",        # 3C, 60
        "Function_61_6877",        # 3D, 61
        "Function_62_68BC",        # 3E, 62
        "Function_63_68FA",        # 3F, 63
        "Function_64_691F",        # 40, 64
        "Function_65_696A",        # 41, 65
        "Function_66_6A3D",        # 42, 66
        "Function_67_6AD3",        # 43, 67
        "Function_68_6AF2",        # 44, 68
        "Function_69_6BDC",        # 45, 69
        "Function_70_6C8F",        # 46, 70
        "Function_71_6D42",        # 47, 71
        "Function_72_6D5F",        # 48, 72
    ))


    def Function_0_5B8(): pass

    label("Function_0_5B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x163, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C9")
    Event(0, 2)

    label("loc_5C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_5E0")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 14)
    Jump("loc_5F2")

    label("loc_5E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_5F2")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 1)
    Event(0, 45)

    label("loc_5F2")

    Return()

    # Function_0_5B8 end

    def Function_1_5F3(): pass

    label("Function_1_5F3")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF3C4169), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_616")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x246), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_62B")

    label("loc_616")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_62B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 1)

    label("loc_62B")

    Return()

    # Function_1_5F3 end

    def Function_2_62C(): pass

    label("Function_2_62C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch02951.itc", 0x27)
    LoadChrToIndex("chr/ch03050.itc", 0x28)
    LoadChrToIndex("chr/ch03051.itc", 0x29)
    LoadChrToIndex("chr/ch00056.itc", 0x2A)
    LoadChrToIndex("chr/ch00156.itc", 0x2B)
    LoadChrToIndex("chr/ch00256.itc", 0x2C)
    LoadChrToIndex("chr/ch00356.itc", 0x2D)
    LoadChrToIndex("chr/ch0295F.itc", 0x2E)
    LoadChrToIndex("chr/ch03056.itc", 0x2F)
    LoadEffect(0x0, "event/ev10008.eff")
    LoadEffect(0x1, "event\\ev15010.eff")
    LoadEffect(0x2, "event/ev14006.eff")
    SoundLoad(2914)
    SoundLoad(3571)
    SoundLoad(3572)
    SoundLoad(3573)
    SoundLoad(3574)
    SoundLoad(3576)
    ClearChrFlags(0xE, 0x80)
    OP_78(0x0, 0xE)
    OP_49()
    SetChrPos(0xE, -5000, 0, 2000, 90)
    OP_D5(0xE, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xB, 0x32, 0x1, 0x20)
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_7C2")
    SetChrPos(0x101, -2000, 0, 1550, 270)
    SetChrPos(0x102, -1600, 0, 2550, 270)
    SetChrPos(0x103, -200, 0, 1750, 270)
    SetChrPos(0x104, -350, 0, 3100, 270)
    SetChrPos(0x109, -400, 0, 750, 270)
    SetChrPos(0x105, 850, 0, 2350, 270)
    Jump("loc_828")

    label("loc_7C2")

    SetChrPos(0x101, 11000, 0, 1550, 270)
    SetChrPos(0x102, 11400, 0, 2550, 270)
    SetChrPos(0x103, 12800, 0, 1750, 270)
    SetChrPos(0x104, 12650, 0, 3100, 270)
    SetChrPos(0x109, 12600, 0, 750, 270)
    SetChrPos(0x105, 13850, 0, 2350, 270)

    label("loc_828")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_855")
    FadeToBright(0, 0)
    Jump("loc_F3B")

    label("loc_855")

    FadeToBright(1000, 0)
    OP_68(-2000, 15700, 2000, 0)
    MoveCamera(345, 0, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(28000, 0)
    OP_68(-2000, 700, 2000, 15000)
    MoveCamera(315, 25, 0, 15000)
    SetCameraDistance(56000, 15000)
    Sleep(7000)

    def lambda_8B9():
        OP_9B(0x0, 0x101, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8B9)
    Sleep(50)

    def lambda_8D1():
        OP_9B(0x0, 0x102, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8D1)
    Sleep(50)

    def lambda_8E9():
        OP_9B(0x0, 0x103, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8E9)
    Sleep(50)

    def lambda_901():
        OP_9B(0x0, 0x104, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_901)
    Sleep(50)

    def lambda_919():
        OP_9B(0x0, 0x109, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_919)
    Sleep(50)

    def lambda_931():
        OP_9B(0x0, 0x105, 0x0, 0x32C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_931)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(-1000, 700, 2000, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(17000, 2000)
    OP_6F(0x79)
    OP_0D()

    #C0001
    ChrTalk(
        0x105,
        "#10308F#12P……開けた場所に出たね。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x101,
        (
            "#00001F#5P俺もこのあたりまでしか\x01",
            "訓練で来なかったけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(500)
    OP_93(0x101, 0xE1, 0x1F4)
    Sleep(500)

    #C0003
    ChrTalk(
        0x101,
        (
            "#00005F#5Pあれ……？\x01",
            "ここって行き止まりだったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x109,
        (
            "#10101F#6Pいえ、まだこの先にも\x01",
            "獣道は続いていたはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x104,
        (
            "#00303F#11Pどうやら倒木が\x01",
            "道を塞いだみてぇだが……\x02\x03",

            "#00301F倒れたのは一月くらい前か。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x102,
        (
            "#00108F#12Pで、でもそれじゃあ\x01",
            "例の魔獣は一体どこに？\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x103,
        (
            "#00208F#12P……何かの気配は\x01",
            "感じるんですが……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(3574, 255, 100, 0)    #voice#Wald
    Sound(833, 0, 40, 0)
    StopBGM(0xFA0)
    Fade(1500)
    SetCameraDistance(19000, 1000)
    OP_6F(0x79)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x101, 0x10E, 0x1F4)

    #C0008
    ChrTalk(
        0x101,
        "#00011F#5P！？\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x104,
        "#00305F#11P笑い声だと……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(30, 15, -1, -1)
    SetChrName("不気味な声")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3571V#40W#53Aクク……揃いも揃って\x01",
            "のこのこと現れやがったか……\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    SetChrName("不気味な声")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3572V#40W#30A相変わらずメデたい連中だぜ……\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7582", 0)
    Fade(500)
    OP_68(-1000, 1000, 2000, 0)
    MoveCamera(225, 30, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(35000, 0)
    OP_68(-1000, 1000, 2000, 10000)
    MoveCamera(270, 15, 0, 10000)
    SetCameraDistance(16650, 10000)
    OP_0D()

    #C0012
    ChrTalk(
        0x101,
        "#00013F#5Pこ、これは……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x109,
        (
            "#10107F#5Pまさか……\x01",
            "魔獣を操ってた犯人……？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x103,
        "#00208F#6Pい、いえ……それよりも……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        (
            "#00101F#5Pこの声……\x01",
            "どこかで聞いた事があるような……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x105,
        "#10310F#6P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x104,
        "#00310F#12Pおいおい、まさか──\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-1000, 1000, 2000, 500)
    MoveCamera(270, 15, 0, 500)
    SetCameraDistance(15650, 500)
    OP_6F(0x79)
    CancelBlur(0)
    OP_0D()
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0018
    ChrTalk(
        0x105,
        "#10307F#2914V#6P#4S#11A来る──下がれっ！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()

    #C0019
    ChrTalk(
        0x101,
        "#00010F#5P！！#8A\x02",
    )
    #Auto

    CloseMessageWindow()

    label("loc_F3B")

    Fade(500)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetChrPos(0xE, -22000, 17000, 15000, 135)
    OP_D5(0xE, 0x0, 0x20F58, 0x0, 0x0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x393, 0x3A2, 0x1, 0x8)
    Sound(3552, 255, 100, 0)    #voice#Wald
    Sound(200, 0, 50, 0)
    Sound(251, 0, 100, 0)
    OP_68(-22000, 22000, 15000, 0)
    MoveCamera(315, 0, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(10000, 0)
    OP_68(-3000, 1300, 2000, 2300)
    MoveCamera(315, 20, 0, 2300)
    SetCameraDistance(18500, 2300)
    Sound(834, 0, 100, 0)

    def lambda_101A():
        OP_9D(0xFE, 0xFFFFE4A8, 0xFFFFFE70, 0x1388, 0xC8, 0x5DC)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_101A)
    Sleep(1500)
    Sound(893, 0, 100, 0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x3A3, 0x3A7, 0x1, 0x8)
    Sound(3544, 255, 100, 0)    #voice#Wald
    Sleep(300)
    Sound(833, 0, 100, 0)
    Sound(248, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xE, 0x5, 0, 1000, 3000, 0, 0, 0, 1500, 2500, 1500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xE, 0x5, 0, 2500, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x1F4, 0x12C, 0x1388, 0x7D0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 3)
    BeginChrThread(0x102, 3, 0, 4)
    BeginChrThread(0x103, 3, 0, 5)
    BeginChrThread(0x104, 3, 0, 6)
    BeginChrThread(0x109, 3, 0, 7)
    BeginChrThread(0x105, 3, 0, 8)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0xE, 1)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    OP_82(0x96, 0x5A, 0x1388, 0x3E8)
    SetChrPos(0xE, -6000, 0, 0, 135)
    OP_D5(0xE, 0x0, 0x20F58, 0x0, 0x0)
    BeginChrThread(0xE, 3, 0, 9)
    SetChrFlags(0xE, 0x1)
    OP_68(-6000, 2300, 300, 0)
    MoveCamera(200, 18, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(7800, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0xA)
    OP_68(-1350, 1300, 300, 3000)
    MoveCamera(115, 18, 0, 3000)
    SetCameraDistance(12800, 3000)
    Sleep(500)
    CancelBlur(1000)
    OP_6F(0x79)
    OP_0D()

    #C0020
    ChrTalk(
        0x101,
        "#00007F#5Pな──！？\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x109,
        "#10107F#5Pお、鬼……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(280, 150, -1, -1)
    SetChrName("鬼")

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3573V#50W#20A……クックックッ…………\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0x3E8, 0x3E8)
    SetChrName("鬼")

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3574V#40W#4S#26A………カハハハハハハッ………\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    Fade(500)
    Sound(889, 0, 40, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrPos(0xE, -5000, 0, 2000, 90)
    OP_D5(0xE, 0x0, 0x15F90, 0x0, 0x0)
    EndChrThread(0xE, 0x3)
    OP_74(0x0, 0x5)
    OP_68(-5000, 2100, 2000, 0)
    MoveCamera(180, 51, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13650, 0)
    OP_68(-5000, 4000, 2000, 5000)
    MoveCamera(270, -10, 0, 5000)
    SetCameraDistance(7350, 5000)
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_71(0x0, 0x3DE, 0x3F2, 0x1, 0x8)
    OP_79(0x0)
    CancelBlur(0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0xB, 0x32, 0x1, 0x8)
    OP_79(0x0)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x41A, 0x442, 0x1, 0x8)
    Sound(892, 0, 100, 0)
    Sleep(1300)
    Sound(892, 0, 100, 0)
    OP_79(0x0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0xB, 0x32, 0x1, 0x20)
    OP_6F(0x79)
    OP_0D()
    Sleep(300)
    SetMessageWindowPos(30, 160, -1, -1)

    #A0024
    AnonymousTalk(
        0x102,
        "#00107F………っ…………！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 160, -1, -1)

    #A0025
    AnonymousTalk(
        0x103,
        "#00201Fこ、これは……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 160, -1, -1)

    #A0026
    AnonymousTalk(
        0x109,
        (
            "#10110Fま、まさかグノーシスで\x01",
            "魔人化したのと同じ……！？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(280, 160, -1, -1)

    #A0027
    AnonymousTalk(
        0x104,
        "#00311Fてめえ……もしかして……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(30, 160, -1, -1)

    #A0028
    AnonymousTalk(
        0x101,
        (
            "#00007Fヴァルド──\x01",
            "あんたなのか！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    Sleep(300)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("鬼")

    #A0029
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#51A#3S#3576V#50Wククク…#1500W…\x01",
            "#40W#5Sハハハハハハハハハハハッ！\x07\x00\x02",
        )
    )
    #Auto

    Sleep(1600)
    Fade(300)
    Sound(196, 0, 70, 0)
    Sound(200, 0, 60, 0)
    Sound(833, 0, 100, 0)
    OP_82(0x64, 0xC8, 0xBB8, 0x7D0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    CancelBlur(1200)
    OP_68(-5000, 3500, 2000, 1000)
    MoveCamera(270, 40, 0, 1000)
    SetCameraDistance(16000, 1000)
    BeginChrThread(0xE, 3, 0, 10)
    WaitChrThread(0xE, 3)
    OP_82(0x1F4, 0x0, 0xBB8, 0x4B0)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_6F(0x79)
    OP_C9(0x1, 0x80000000)
    Fade(500)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x109, 0x8)
    ClearChrFlags(0x105, 0x8)
    EndChrThread(0xE, 0x3)
    BeginChrThread(0xE, 3, 0, 11)
    OP_68(-1740, 2600, 2210, 0)
    MoveCamera(295, 3, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14050, 0)
    SetCameraDistance(12750, 1500)
    OP_6F(0x79)
    OP_0D()
    SetMessageWindowPos(10, 80, -1, -1)

    #A0030
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30Wバニングスにオルランド……\x01",
            "ずいぶん久しぶりじゃねぇか。\x02\x03",

            "#30Wクク……\x01",
            "それにワジ……テメェともな。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0031
    ChrTalk(
        0x105,
        (
            "#10306F#12P#Nああ……そうだね。\x02\x03",

            "#10308F君のファッションの\x01",
            "悪趣味さは知っていたけど……\x02\x03",

            "#10310Fさすがにそれ#4R㈲　㈲#は、幾らなんでも\x01",
            "やりすぎなんじゃないの……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(40, 80, -1, -1)

    #A0032
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#11P#30Wクク……抜かせ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0033
    ChrTalk(
        0x101,
        "#00010F#4P#Nちょ、ちょっと待ってくれ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0034
    ChrTalk(
        0x109,
        (
            "#10107F#4P#Nそ、それじゃああなたが\x01",
            "列車を脱線させた……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(10, 80, -1, -1)

    #A0035
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30Wクク……何を判りきったことを\x01",
            "わざわざ確認してやがる……？\x02\x03",

            "#30Wそこらの魔獣ごときに\x01",
            "あんな真似ができるわけねぇだろ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(-5000, 4200, 2000, 0)
    MoveCamera(270, 0, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(7000, 0)
    Sound(892, 0, 100, 0)
    Sound(200, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xE, 0x5, 0, 500, 0, 0, 0, 0, 2000, 2500, 2000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-500, 2300, 2000, 1000)
    MoveCamera(270, 14, 0, 1000)
    SetCameraDistance(23000, 1000)
    EndChrThread(0xE, 0x3)
    BeginChrThread(0xE, 3, 0, 12)
    Sleep(500)
    CancelBlur(500)
    OP_6F(0x79)
    OP_0D()
    OP_82(0x1F4, 0x0, 0xBB8, 0x1F4)
    SetMessageWindowPos(-1, 110, -1, -1)

    #A0036
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#4S新たな“チカラ”を手に入れた\x01",
            "このヴァルド・ヴァレス以外になアアッ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(-2000, 2500, 2000, 0)
    MoveCamera(60, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    MoveCamera(50, 24, 0, 10000)
    OP_0D()

    #C0037
    ChrTalk(
        0x103,
        "#00210F#11Pっ……\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x102,
        "#00108F#11Pなんて鬼気……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        "#00310F#11P洒落になってねぇぞ……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 150, -1, -1)

    #A0040
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30Wさてと、わざわざここまで\x01",
            "俺を追ってきてくれたんだ……\x02",
        )
    )

    CloseMessageWindow()

    #A0041
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30Wとっとと始めるとしようか……？\x02",
        )
    )

    CloseMessageWindow()

    #A0042
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30Wこの俺がどれだけ“上”か……\x01",
            "骨の髄まで判らせるためによォ……？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0043
    ChrTalk(
        0x101,
        "#00010F#11Pくっ……！\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x105,
        "#10301F#11P……どうやら本気みたいだね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-5000, 3200, 2000, 0)
    MoveCamera(270, 0, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18250, 0)
    OP_68(-5000, 4500, 2000, 2000)
    SetCameraDistance(8250, 2000)
    MoveCamera(270, 15, 0, 2000)
    StopBGM(0xFA0)
    EndChrThread(0xE, 0x3)
    Sound(889, 0, 70, 0)
    BeginChrThread(0xE, 3, 0, 13)
    Sleep(500)
    StopSound(889, 1000, 70)
    CancelBlur(500)
    Sleep(1500)
    SetMessageWindowPos(260, 160, -1, -1)

    #A0045
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30Wクク、てめぇらごとき\x01",
            "今さら本気を出すまでもねぇ……\x02\x03",

            "#30Wせいぜい優しく撫でてやるから\x01",
            "死なない程度に味わいやがれよ……？\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)
    Fade(500)
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(6730, 500)
    OP_6F(0x79)
    CancelBlur(0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7455", 0)
    OP_82(0x1F4, 0x0, 0xBB8, 0x1F4)

    #A0046
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#4S──このオレが手に入れた\x01",
            "正真正銘の“チカラ”をなああッ！！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-5000, 5800, 2000, 0)
    MoveCamera(270, 5, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15000, 0)
    OP_68(-5000, 1500, 2000, 500)
    SetCameraDistance(23000, 500)
    EndChrThread(0xE, 0x3)
    Sound(893, 0, 100, 0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x3A3, 0x3A7, 0x1, 0x8)
    Sleep(300)
    Sound(833, 0, 100, 0)
    Sound(196, 0, 100, 0)
    OP_82(0x0, 0x64, 0x1388, 0x1F4)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sleep(500)
    SetScenarioFlags(0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_END)), "loc_1DF8")
    Battle("BattleInfo_450", 0x30200011, 0x0, 0x100, 0x13, 0xFF)
    Jump("loc_1E08")

    label("loc_1DF8")

    Battle("BattleInfo_40C", 0x30200011, 0x0, 0x100, 0x13, 0xFF)

    label("loc_1E08")

    FadeToDark(0, 0, -1)
    Call(0, 14)
    Return()

    # Function_2_62C end

    def Function_3_1E16(): pass

    label("Function_3_1E16")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x9C4, 0x0, 0x0, 0x1F4, 0xDAC)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_3_1E16 end

    def Function_4_1E3E(): pass

    label("Function_4_1E3E")

    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x9C4, 0x0, 0x0, 0x258, 0xBB8)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_4_1E3E end

    def Function_5_1E66(): pass

    label("Function_5_1E66")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x9C4, 0x0, 0x0, 0x2BC, 0x9C4)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_5_1E66 end

    def Function_6_1E8E(): pass

    label("Function_6_1E8E")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x9C4, 0x0, 0x0, 0x1F4, 0xDAC)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_6_1E8E end

    def Function_7_1EB6(): pass

    label("Function_7_1EB6")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x9C4, 0x0, 0x0, 0x258, 0xBB8)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_7_1EB6 end

    def Function_8_1EDE(): pass

    label("Function_8_1EDE")

    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0x9C4, 0x0, 0x0, 0x2BC, 0x9C4)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_8_1EDE end

    def Function_9_1F06(): pass

    label("Function_9_1F06")

    OP_74(0x0, 0x5)
    OP_71(0x0, 0x3CA, 0x3DE, 0x1, 0x20)
    Return()

    # Function_9_1F06 end

    def Function_10_1F17(): pass

    label("Function_10_1F17")

    OP_74(0x0, 0x14)
    OP_71(0x0, 0x5B, 0x78, 0x1, 0x8)
    OP_79(0x0)
    OP_71(0x0, 0x65, 0x78, 0x0, 0x20)
    Return()

    # Function_10_1F17 end

    def Function_11_1F37(): pass

    label("Function_11_1F37")

    OP_74(0x0, 0xF)
    OP_71(0x0, 0x78, 0x82, 0x1, 0x8)
    OP_79(0x0)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0xB, 0x32, 0x1, 0x20)
    Return()

    # Function_11_1F37 end

    def Function_12_1F5B(): pass

    label("Function_12_1F5B")

    OP_74(0x0, 0xA)
    OP_71(0x0, 0x3F2, 0x3FC, 0x1, 0x8)
    OP_79(0x0)
    OP_71(0x0, 0x3FC, 0x410, 0x1, 0x20)
    Return()

    # Function_12_1F5B end

    def Function_13_1F7B(): pass

    label("Function_13_1F7B")

    OP_74(0x0, 0x5)
    OP_71(0x0, 0x335, 0x339, 0x1, 0x8)
    OP_79(0x0)

    label("loc_1F8E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1FC0")
    OP_74(0x0, 0x1)
    OP_71(0x0, 0x339, 0x33B, 0x1, 0x8)
    OP_79(0x0)
    OP_71(0x0, 0x33B, 0x339, 0x1, 0x8)
    OP_79(0x0)
    Jump("loc_1F8E")

    label("loc_1FC0")

    Return()

    # Function_13_1F7B end

    def Function_14_1FC1(): pass

    label("Function_14_1FC1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch02950.itc", 0x26)
    LoadChrToIndex("chr/ch02951.itc", 0x27)
    LoadChrToIndex("chr/ch03050.itc", 0x28)
    LoadChrToIndex("chr/ch03051.itc", 0x29)
    LoadChrToIndex("chr/ch00056.itc", 0x2A)
    LoadChrToIndex("chr/ch00156.itc", 0x2B)
    LoadChrToIndex("chr/ch00256.itc", 0x2C)
    LoadChrToIndex("chr/ch00356.itc", 0x2D)
    LoadChrToIndex("chr/ch0295F.itc", 0x2E)
    LoadChrToIndex("chr/ch03056.itc", 0x2F)
    LoadChrToIndex("chr/ch32650.itc", 0x30)
    LoadChrToIndex("chr/ch32651.itc", 0x31)
    LoadChrToIndex("chr/ch32657.itc", 0x32)
    LoadChrToIndex("chr/ch32653.itc", 0x33)
    LoadChrToIndex("chr/ch31250.itc", 0x34)
    LoadChrToIndex("chr/ch31251.itc", 0x35)
    LoadChrToIndex("chr/ch31252.itc", 0x36)
    LoadChrToIndex("chr/ch31253.itc", 0x37)
    LoadChrToIndex("apl/ch51444.itc", 0x38)
    SoundLoad(3575)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    LoadEffect(0x0, "battle/btgun00.eff")
    LoadEffect(0x1, "event/ev606_00.eff")
    LoadEffect(0x2, "battle/cr326000.eff")
    LoadEffect(0x3, "event\\ev15010.eff")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xCF, 0xB5, 0x5A, 0x96, 0x0)
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFFFFCFB5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2157")
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x2D)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x2F)
    SetChrSubChip(0x105, 0x0)
    Jump("loc_21CA")

    label("loc_2157")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_219A")
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2E)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)
    Jump("loc_21CA")

    label("loc_219A")

    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)

    label("loc_21CA")

    SetChrPos(0x101, 1000, 0, 1550, 270)
    SetChrPos(0x102, 1400, 0, 2550, 270)
    SetChrPos(0x103, 2800, 0, 1750, 270)
    SetChrPos(0x104, 2650, 0, 3100, 270)
    SetChrPos(0x109, 2600, 0, 750, 270)
    SetChrPos(0x105, 3850, 0, 2350, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x30)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x34)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x34)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x34)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x34)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x34)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x34)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xF, 12000, 0, 2000, 270)
    SetChrPos(0x8, 13700, 0, 3000, 270)
    SetChrPos(0x9, 14700, 0, 2500, 270)
    SetChrPos(0xA, 15300, 0, 3500, 270)
    SetChrPos(0xB, 13200, 0, 1000, 270)
    SetChrPos(0xC, 15000, 0, 1500, 270)
    SetChrPos(0xD, 15300, 0, 500, 270)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x80)
    OP_78(0x0, 0xE)
    OP_49()
    SetChrPos(0xE, -5000, 0, 2000, 90)
    OP_D5(0xE, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0xB, 0x32, 0x1, 0x20)
    SetChrFlags(0xE, 0x1)
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_23DA")
    FadeToBright(0, 0)
    Jump("loc_32E6")

    label("loc_23DA")

    OP_68(-1740, 2600, 2210, 0)
    MoveCamera(295, 3, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14050, 0)
    SetCameraDistance(12750, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2629")
    SetMessageWindowPos(10, 80, -1, -1)

    #A0047
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W……オイオイ……\x01",
            "てめぇら、舐めてんのか？\x02",
        )
    )

    CloseMessageWindow()

    #A0048
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30Wいくらなんでも\x01",
            "呆気なさすぎるだろうが……？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_24B3():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_24B3)

    def lambda_24CC():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_24CC)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    OP_0D()
    WaitChrThread(0x101, 2)
    WaitChrThread(0x104, 2)

    #C0049
    ChrTalk(
        0x101,
        "#00006F#4P#Nくっ……はあはあ……\x02",
    )

    CloseMessageWindow()

    def lambda_252C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_252C)

    def lambda_2545():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2545)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)

    #C0050
    ChrTalk(
        0x102,
        "#00108F#12P#Nぜ、全然通用してない……？\x02",
    )

    CloseMessageWindow()

    def lambda_25AC():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_25AC)

    def lambda_25C5():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_25C5)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x105, 0x28)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    WaitChrThread(0x105, 2)
    WaitChrThread(0x109, 2)

    #C0051
    ChrTalk(
        0x103,
        "#00206F#12P#Nとんでもないです……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_287C")

    label("loc_2629")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2792")
    OP_2C(0xA8, 0x1)
    SetMessageWindowPos(10, 80, -1, -1)

    #A0052
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30Wクク……\x01",
            "まあそんなモンだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #A0053
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30Wやれやれ……\x01",
            "ちょいと強くなりすぎたかァ？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0054
    ChrTalk(
        0x101,
        "#00010F#4P#Nくっ……\x02",
    )

    CloseMessageWindow()

    def lambda_26D4():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_26D4)

    def lambda_26ED():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_26ED)

    def lambda_2706():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2706)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x109, 0x26)
    SetChrSubChip(0x109, 0x0)
    OP_0D()
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x109, 2)

    #C0055
    ChrTalk(
        0x109,
        (
            "#10108F#4P#Nあ、あれだけやったのに\x01",
            "殆んど効いていない……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_287C")

    label("loc_2792")

    OP_2C(0xA8, 0x2)
    SetMessageWindowPos(10, 80, -1, -1)

    #A0056
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30Wクク……\x01",
            "思ったよりもやるじゃねぇか。\x02",
        )
    )

    CloseMessageWindow()

    #A0057
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30Wお楽しみに取っておくつもりが\x01",
            "喰っちまいたくなるぜぇ……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0058
    ChrTalk(
        0x101,
        "#00013F#4P#Nくっ……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0059
    ChrTalk(
        0x104,
        (
            "#00311F#12P#Nチッ……\x01",
            "６人がかりでこの程度かよ！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_287C")


    #C0060
    ChrTalk(
        0x105,
        "#10303F#12P#N……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-2000, 2500, 2000, 0)
    MoveCamera(60, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    MoveCamera(50, 24, 0, 15000)
    Sleep(500)
    SetMessageWindowPos(10, 120, -1, -1)

    #A0061
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30Wクク……どうしたワジ……？\x02",
        )
    )

    CloseMessageWindow()

    #A0062
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30Wいつもみたいに小奇麗なツラで\x01",
            "スカしたことを言ってみろよ……？\x02",
        )
    )

    CloseMessageWindow()

    #A0063
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30Wそうじゃなくちゃ\x01",
            "面白くならねぇだろうが……？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0064
    ChrTalk(
        0x105,
        (
            "#10306F──ヴァルド。\x02\x03",

            "#10301F一体どこで\x01",
            "《グノーシス》を手に入れた？\x02",
        )
    )

    CloseMessageWindow()
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
    Sleep(1000)

    #C0065
    ChrTalk(
        0x101,
        "#00011F#11Pそ、そういえば……！\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x102,
        (
            "#00101F#11Pヨアヒム先生が製造したものは\x01",
            "調査用のサンプルを除いて\x01",
            "全て廃棄された筈……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x104,
        (
            "#00307F#11Pてめぇ……\x01",
            "どこから手に入れやがった！？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(10, 120, -1, -1)

    #A0068
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30Wクク……さてなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #A0069
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30Wそれに、カン違いするな。\x02",
        )
    )

    CloseMessageWindow()

    #A0070
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30Wこの“チカラ”は何も\x01",
            "クスリだけのモンじゃねえ……\x02",
        )
    )

    CloseMessageWindow()

    #A0071
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30Wクスリはあくまできっかけ──\x01",
            "コイツはオレ自身から生み出された\x01",
            "混じりけのない“チカラ”だ。\x02",
        )
    )

    CloseMessageWindow()

    #A0072
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30Wヨアヒムってのが手に入れた\x01",
            "紛いモンの“チカラ”と違ってなぁ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0073
    ChrTalk(
        0x103,
        (
            "#00201F#11P……確かに……\x01",
            "ヨアヒム先生の時とは違って\x01",
            "暴走はしていないようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x105,
        (
            "#10303F#11Pきっかけはどうあれ\x01",
            "使いこなせてるってわけか……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-530, 2600, 2300, 0)
    MoveCamera(271, 4, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12750, 0)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xF, 0x8)
    Sleep(300)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrPos(0x1C, 8000, 0, 1750, 270)

    #N0075
    NpcTalk(
        0x1C,
        "男の声",
        "#2S#5Pな、なんだ！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x1C, 8000, 0, 2250, 270)

    #N0076
    NpcTalk(
        0x1C,
        "男の声",
        "#2S#11Pば、化物……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrFlags(0x1C, 0x80)
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
    Fade(500)
    OP_68(12000, 1000, 2000, 0)
    OP_68(4500, 1000, 2000, 2500)
    MoveCamera(45, 24, 0, 0)
    MoveCamera(35, 21, 0, 2500)
    OP_6E(510, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(16000, 2500)
    OP_93(0x101, 0x5A, 0x0)
    OP_93(0x102, 0x5A, 0x0)
    OP_93(0x103, 0x5A, 0x0)
    OP_93(0x104, 0x5A, 0x0)
    OP_93(0x109, 0x5A, 0x0)
    OP_93(0x105, 0x5A, 0x0)
    SetMapObjFlags(0x0, 0x4)
    BeginChrThread(0xF, 3, 0, 15)
    Sleep(10)
    BeginChrThread(0x8, 3, 0, 16)
    BeginChrThread(0x9, 3, 0, 16)
    Sleep(10)
    BeginChrThread(0xA, 3, 0, 16)
    BeginChrThread(0xB, 3, 0, 16)
    Sleep(10)
    BeginChrThread(0xC, 3, 0, 16)
    BeginChrThread(0xD, 3, 0, 16)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    OP_6F(0x79)
    OP_0D()

    #C0077
    ChrTalk(
        0x104,
        "#00305F#6Pミレイユ……！\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x109,
        "#10102F#6Pミレイユ三尉……！\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x102,
        (
            "#00102F#6Pよかった……！\x01",
            "復旧が終わったんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xF,
        (
            "#07905F#11Pえ、ええ、それで\x01",
            "急いで駆けつけたんだけど……\x02\x03",

            "#07907Fな、なんなのその化物……！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3033():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3033)
    Sleep(50)

    def lambda_3043():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3043)
    Sleep(50)

    def lambda_3053():
        OP_93(0x103, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3053)
    Sleep(50)

    def lambda_3063():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3063)
    Sleep(50)

    def lambda_3073():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3073)
    Sleep(50)

    def lambda_3083():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3083)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Fade(500)
    OP_68(-2000, 2500, 2000, 0)
    MoveCamera(55, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12750, 0)
    ClearMapObjFlags(0x0, 0x4)
    OP_0D()
    SetMessageWindowPos(10, 120, -1, -1)

    #A0081
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30Wクク……今日はここでお開きか。\x02",
        )
    )

    CloseMessageWindow()

    #A0082
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W特務支援課……それからワジ。\x02",
        )
    )

    CloseMessageWindow()

    #A0083
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30W次会った時はもう少しくらいは\x01",
            "オレを愉しませろや……？\x02",
        )
    )

    CloseMessageWindow()

    #A0084
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#30Wあの旧市街でやった\x01",
            "チェイスバトルくらいにはなァ？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0085
    ChrTalk(
        0x101,
        "#00013F#11Pくっ……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x104,
        "#00310F#11Pてめぇ……\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x105,
        "#10307F#11Pヴァルド……！\x02",
    )

    CloseMessageWindow()
    OP_68(6000, 1000, 2000, 1500)
    SetCameraDistance(13000, 1500)
    OP_6F(0x79)

    #C0088
    ChrTalk(
        0xF,
        (
            "#07901F#11Pに、逃がすもんですかッ！\x02\x03",

            "#07907F総員、戦闘準備ッ！\x01",
            "ミサイルポッドの使用も許可する！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0xC8)
    SetMessageWindowPos(280, 10, -1, -1)
    SetChrName("警備隊員たち")

    #A0089
    AnonymousTalk(
        0xFF,
        "#4Sイエス・マム！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_32E6")

    Fade(500)
    OP_68(7150, 1500, 2000, 0)
    MoveCamera(270, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13800, 0)
    OP_68(-1750, 1500, 2000, 3000)
    MoveCamera(310, 9, 0, 3000)
    SetCameraDistance(19800, 3000)
    ClearChrFlags(0xF, 0x8)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)
    SetChrPos(0xF, 6000, 0, 2000, 270)
    SetChrPos(0x8, 7700, 0, 3000, 270)
    SetChrPos(0x9, 8700, 0, 2500, 270)
    SetChrPos(0xA, 9300, 0, 3500, 270)
    SetChrPos(0xB, 7200, 0, 1000, 270)
    SetChrPos(0xC, 9000, 0, 1500, 270)
    SetChrPos(0xD, 9300, 0, 500, 270)
    BeginChrThread(0xF, 3, 0, 17)
    BeginChrThread(0x8, 3, 0, 18)
    BeginChrThread(0x9, 3, 0, 19)
    BeginChrThread(0xA, 3, 0, 20)
    BeginChrThread(0xB, 3, 0, 21)
    BeginChrThread(0xC, 3, 0, 22)
    BeginChrThread(0xD, 3, 0, 23)
    Sleep(800)
    BeginChrThread(0x101, 3, 0, 25)
    BeginChrThread(0x102, 3, 0, 26)
    BeginChrThread(0x103, 3, 0, 27)
    BeginChrThread(0x104, 3, 0, 28)
    BeginChrThread(0x109, 3, 0, 29)
    BeginChrThread(0x105, 3, 0, 30)
    OP_6F(0x79)
    BeginChrThread(0x101, 0, 0, 24)
    MoveCamera(295, 9, 0, 9000)
    OP_6F(0x79)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    OP_0D()
    Fade(500)
    OP_68(-5000, 3300, 2000, 0)
    MoveCamera(270, 40, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    MoveCamera(270, 30, 0, 10000)
    SetCameraDistance(13500, 10000)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x41A, 0x442, 0x1, 0x8)
    Sound(892, 0, 100, 0)
    Sleep(1300)
    Sound(892, 0, 100, 0)
    OP_79(0x0)
    OP_74(0x0, 0x14)
    OP_71(0x0, 0xB, 0x32, 0x1, 0x20)
    OP_0D()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 140, -1, -1)

    #A0090
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#40A#3575Vカカ……\x01",
            "#4Sぬるいんだよオオオオッ！\x07\x00\x05\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-5000, 4250, 2000, 1200)
    MoveCamera(270, 15, 0, 1200)
    OP_6E(600, 1200)
    SetCameraDistance(9000, 1200)
    Sound(892, 0, 100, 0)
    OP_74(0x0, 0x7)
    OP_71(0x0, 0x335, 0x33E, 0x1, 0x8)
    OP_79(0x0)
    EndChrThread(0x101, 0x0)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x9, 0x3)
    EndChrThread(0xA, 0x3)
    EndChrThread(0xB, 0x3)
    EndChrThread(0xC, 0x3)
    EndChrThread(0xD, 0x3)
    CancelBlur(500)
    Sleep(500)
    OP_6F(0x79)
    Sound(893, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x33E, 0x348, 0x1, 0x8)
    Sound(3543, 255, 100, 0)    #voice#Wald
    Sound(833, 0, 100, 0)
    Sound(862, 0, 100, 0)
    OP_82(0x1F4, 0x1F4, 0x2328, 0x5DC)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x3, 0xFF, 0xE, 0x5, 0, 2000, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_68(-5000, 800, 2000, 1000)
    MoveCamera(270, 16, 0, 1000)
    SetCameraDistance(33000, 1000)
    Sleep(700)
    CancelBlur(500)
    BeginChrThread(0xF, 3, 0, 37)
    BeginChrThread(0x8, 3, 0, 38)
    BeginChrThread(0x9, 3, 0, 39)
    BeginChrThread(0xA, 3, 0, 40)
    BeginChrThread(0xB, 3, 0, 41)
    BeginChrThread(0xC, 3, 0, 42)
    BeginChrThread(0xD, 3, 0, 43)
    BeginChrThread(0x101, 3, 0, 31)
    BeginChrThread(0x102, 3, 0, 32)
    BeginChrThread(0x103, 3, 0, 33)
    BeginChrThread(0x104, 3, 0, 34)
    BeginChrThread(0x109, 3, 0, 35)
    BeginChrThread(0x105, 3, 0, 36)

    #C0091
    ChrTalk(
        0xF,
        "#07911Fきゃああッ！？\x05\x02",
    )


    #C0092
    ChrTalk(
        0xD,
        "うわあああっ！？\x05\x02",
    )

    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0xF, 3)
    Sound(514, 0, 100, 0)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    OP_79(0x0)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(-5000, 2800, 2000, 0)
    MoveCamera(120, 42, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(27000, 0)
    BeginChrThread(0xE, 3, 0, 44)
    OP_D5(0xE, 0x0, 0x5F370, 0x0, 0x0)
    OP_D5(0xE, 0x0, 0x4BAF0, 0x0, 0x2BC)
    WaitChrThread(0xE, 3)
    OP_0D()
    Sleep(200)
    Fade(500)
    OP_68(-5000, 3800, 2000, 2000)
    MoveCamera(340, -15, 0, 2000)
    SetCameraDistance(12000, 2000)
    OP_74(0x0, 0xA)
    OP_71(0x0, 0x105, 0x118, 0x1, 0x8)
    OP_79(0x0)
    OP_74(0x0, 0x5)
    OP_71(0x0, 0x119, 0x122, 0x1, 0x20)
    Sleep(500)
    OP_68(-5000, 10000, 2000, 500)
    MoveCamera(340, -40, 0, 500)
    SetCameraDistance(20000, 500)
    OP_82(0xC8, 0x1F4, 0xFA0, 0x1F4)
    Sound(833, 0, 80, 0)
    Sound(251, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1)
    CancelBlur(1000)

    def lambda_3824():
        OP_9C(0xFE, 0xFFFEEE90, 0x0, 0x7530, 0x88B8, 0x5DC)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3824)
    PlayEffect(0x3, 0xFF, 0xE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0xE, 0x1)
    OP_74(0x0, 0x2D)
    OP_71(0x0, 0x123, 0x12C, 0x1, 0x8)
    OP_79(0x0)
    OP_71(0x0, 0x12D, 0x140, 0x1, 0x20)
    OP_0D()
    Sleep(2500)
    Fade(500)
    EndChrThread(0xE, 0x1)
    OP_F0(0x0, 0x1)
    OP_F0(0x1, 0x3E8)
    OP_68(-26540, 13300, 18780, 0)
    MoveCamera(85, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(48960, 0)
    OP_68(-26540, 8300, 18780, 4000)
    MoveCamera(112, 23, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(73320, 4000)
    SetChrPos(0xE, -18600, 15800, 15800, 0)

    def lambda_391E():
        OP_9D(0xFE, 0xFFFF9688, 0x23F0, 0x79AE, 0x1388, 0x1388)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_391E)
    OP_74(0x0, 0xF)
    OP_71(0x0, 0x141, 0x154, 0x1, 0x8)
    Sleep(1100)
    Sound(833, 0, 80, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    PlayEffect(0x3, 0xFF, 0xE, 0x0, 0, 0, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_D5(0xE, 0x0, 0x41EB0, 0x0, 0x12C)
    OP_79(0x0)
    WaitChrThread(0xE, 1)
    Sound(251, 0, 100, 0)

    def lambda_39BC():
        OP_9D(0xFE, 0xFFFF444E, 0x3458, 0x57E4, 0x2710, 0x1388)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_39BC)
    OP_74(0x0, 0x23)
    OP_71(0x0, 0x123, 0x154, 0x1, 0x8)
    Sleep(1100)
    Sound(833, 0, 80, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    PlayEffect(0x3, 0xFF, 0xE, 0x0, 0, 0, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_D5(0xE, 0x0, 0x4CE78, 0x0, 0x12C)
    OP_79(0x0)
    WaitChrThread(0xE, 1)
    Sound(251, 0, 100, 0)

    def lambda_3A5A():
        OP_9C(0xFE, 0xFFFEE2D8, 0x0, 0x9C40, 0x36B0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3A5A)
    OP_74(0x0, 0x14)
    OP_71(0x0, 0x123, 0x154, 0x1, 0x8)
    Sleep(550)
    BlurSwitch(0x96, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(150)
    OP_82(0x5DC, 0x5DC, 0x1388, 0x3E8)
    Sleep(1000)
    CancelBlur(3000)
    OP_79(0x0)
    WaitChrThread(0xE, 1)
    OP_0D()
    StopBGM(0x2710)
    Fade(1000)
    OP_68(-14380, 14500, -2230, 0)
    MoveCamera(350, 38, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(60750, 0)
    OP_68(-14380, 14500, -2230, 10000)
    MoveCamera(308, 0, 0, 10000)
    SetCameraDistance(60750, 10000)
    OP_6F(0x79)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    Sleep(500)
    SetChrName("")

    #A0093
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その後、ロイドたちは\x01",
            "ミレイユの部隊と協力しながら\x01",
            "広大な樹海を捜索したが……\x02\x03",

            "結局、魔人化したヴァルドの姿を\x01",
            "発見することは出来なかった。\x02\x03",

            "そして夜も更けて\x01",
            "いったん捜索が打ち切られた後……\x02\x03",

            "ロイドたちは深夜近くに支援課に戻り、\x01",
            "キーアが用意していた鍋をつつく気力もなく\x01",
            "泥のような眠りにつくのだった。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_32(0xFF, 0xFE, 0x0)
    ReplaceBGM(-1, -1)
    OP_C9(0x0, 0x10000)
    SetScenarioFlags(0x22, 2)
    NewScene("c1400", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_1FC1 end

    def Function_15_3CE9(): pass

    label("Function_15_3CE9")

    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3CF6():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CF6)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_15_3CE9 end

    def Function_16_3D13(): pass

    label("Function_16_3D13")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3D20():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D20)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x34)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_16_3D13 end

    def Function_17_3D3D(): pass

    label("Function_17_3D3D")

    SetChrChipByIndex(0xFE, 0x31)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3D4A():
        OP_95(0xFE, 1950, 0, 5200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D4A)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x30)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    SetChrChipByIndex(0xFE, 0x32)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)

    label("loc_3D7F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3DF2")
    Sound(545, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 300, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xE, 0, 0, 0, 0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x4, 0x5, 0x3)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(1000)
    Sound(196, 0, 80, 0)
    Sleep(2000)
    Jump("loc_3D7F")

    label("loc_3DF2")

    Return()

    # Function_17_3D3D end

    def Function_18_3DF3(): pass

    label("Function_18_3DF3")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3E00():
        OP_95(0xFE, -2100, 0, 9400, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E00)
    WaitChrThread(0xFE, 1)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 80, 0)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    SetChrChipByIndex(0xFE, 0x38)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)

    label("loc_3E41")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3EB4")
    Sound(545, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 300, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xE, 0, 0, 0, 0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x4, 0x5, 0x3)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(1000)
    Sound(196, 0, 80, 0)
    Sleep(2000)
    Jump("loc_3E41")

    label("loc_3EB4")

    Return()

    # Function_18_3DF3 end

    def Function_19_3EB5(): pass

    label("Function_19_3EB5")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3EC2():
        OP_95(0xFE, 1700, 0, 7650, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3EC2)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x36)
    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)

    label("loc_3EFB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3F60")
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sound(987, 0, 50, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1050, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sleep(1000)
    Jump("loc_3EFB")

    label("loc_3F60")

    Return()

    # Function_19_3EB5 end

    def Function_20_3F61(): pass

    label("Function_20_3F61")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_3F6E():
        OP_95(0xFE, 1100, 0, 10100, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F6E)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    SetChrChipByIndex(0xFE, 0x36)
    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)

    label("loc_3FA1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4006")
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sound(567, 0, 50, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1050, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sleep(1000)
    Jump("loc_3FA1")

    label("loc_4006")

    Return()

    # Function_20_3F61 end

    def Function_21_4007(): pass

    label("Function_21_4007")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_4014():
        OP_95(0xFE, -550, 0, -5000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4014)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    SetChrChipByIndex(0xFE, 0x36)
    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)

    label("loc_4047")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_40A6")
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1050, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sleep(1000)
    Jump("loc_4047")

    label("loc_40A6")

    Return()

    # Function_21_4007 end

    def Function_22_40A7(): pass

    label("Function_22_40A7")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_40B4():
        OP_95(0xFE, 1950, 0, -1300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_40B4)
    WaitChrThread(0xFE, 1)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    SetChrChipByIndex(0xFE, 0x36)
    OP_A1(0xFE, 0x3E8, 0x2, 0x0, 0x1)

    label("loc_40ED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4152")
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sound(530, 0, 40, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x5, 0, 1050, 1200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    Sleep(1000)
    Jump("loc_40ED")

    label("loc_4152")

    Return()

    # Function_22_40A7 end

    def Function_23_4153(): pass

    label("Function_23_4153")

    SetChrChipByIndex(0xFE, 0x35)
    SetChrSubChip(0xFE, 0x0)

    def lambda_4160():
        OP_95(0xFE, 2300, 0, -3900, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4160)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(50)
    TurnDirection(0xFE, 0xE, 500)
    SetChrChipByIndex(0xFE, 0x38)
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x3)

    label("loc_4195")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4208")
    Sound(545, 0, 80, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 300, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xE, 0, 0, 0, 0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x4, 0x5, 0x3)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(1000)
    Sound(196, 0, 80, 0)
    Sleep(2000)
    Jump("loc_4195")

    label("loc_4208")

    Return()

    # Function_23_4153 end

    def Function_24_4209(): pass

    label("Function_24_4209")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_433B")
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -6050, 0, 6310, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -4270, 0, -2050, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1110, 0, 2390, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(450)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -2860, 0, 530, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(350)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -1580, 0, -1780, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jump("Function_24_4209")

    label("loc_433B")

    Return()

    # Function_24_4209 end

    def Function_25_433C(): pass

    label("Function_25_433C")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_25_433C end

    def Function_26_435C(): pass

    label("Function_26_435C")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_26_435C end

    def Function_27_437C(): pass

    label("Function_27_437C")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_27_437C end

    def Function_28_439C(): pass

    label("Function_28_439C")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_28_439C end

    def Function_29_43BC(): pass

    label("Function_29_43BC")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_29_43BC end

    def Function_30_43DC(): pass

    label("Function_30_43DC")

    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0xB4, 0x7D0, 0x7D0, 0x0)
    SetChrChipByIndex(0xFE, 0x28)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_30_43DC end

    def Function_31_43FC(): pass

    label("Function_31_43FC")

    Sound(250, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_31_43FC end

    def Function_32_4426(): pass

    label("Function_32_4426")

    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_32_4426 end

    def Function_33_444A(): pass

    label("Function_33_444A")

    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_33_444A end

    def Function_34_446E(): pass

    label("Function_34_446E")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_34_446E end

    def Function_35_4492(): pass

    label("Function_35_4492")

    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_35_4492 end

    def Function_36_44B6(): pass

    label("Function_36_44B6")

    SetChrChipByIndex(0xFE, 0x2F)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x3E8, 0xBB8)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_36_44B6 end

    def Function_37_44DA(): pass

    label("Function_37_44DA")

    SetChrChipByIndex(0xFE, 0x33)
    SetChrSubChip(0xFE, 0x0)
    Sound(815, 0, 100, 0)
    OP_9D(0xFE, 0x154A, 0x0, 0x18EC, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_37_44DA end

    def Function_38_4509(): pass

    label("Function_38_4509")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x50, 0x0, 0x2CD8, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_38_4509 end

    def Function_39_4532(): pass

    label("Function_39_4532")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x1068, 0x0, 0x2314, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_39_4532 end

    def Function_40_455B(): pass

    label("Function_40_455B")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0xC1C, 0x0, 0x2CBA, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_40_455B end

    def Function_41_4584(): pass

    label("Function_41_4584")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x672, 0x0, 0xFFFFE502, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_41_4584 end

    def Function_42_45AD(): pass

    label("Function_42_45AD")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x154A, 0x0, 0xFFFFF7EA, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_42_45AD end

    def Function_43_45D6(): pass

    label("Function_43_45D6")

    SetChrChipByIndex(0xFE, 0x37)
    SetChrSubChip(0xFE, 0x0)
    OP_9D(0xFE, 0x1324, 0x0, 0xFFFFEA98, 0x1F4, 0x7D0)
    OP_A1(0xFE, 0x3E8, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_43_45D6 end

    def Function_44_45FF(): pass

    label("Function_44_45FF")

    OP_74(0x0, 0xF)
    OP_71(0x0, 0x173, 0x17A, 0x1, 0x8)
    OP_79(0x0)
    OP_71(0x0, 0x17A, 0x173, 0x1, 0x8)
    OP_79(0x0)
    Return()

    # Function_44_45FF end

    def Function_45_4622(): pass

    label("Function_45_4622")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "eff\\cutin00.eff")
    LoadEffect(0x1, "eff\\\\step00.eff")
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00056.itc", 0x20)
    LoadChrToIndex("chr/ch41450.itc", 0x21)
    LoadChrToIndex("chr/ch41451.itc", 0x22)
    LoadChrToIndex("chr/ch41452.itc", 0x23)
    LoadChrToIndex("chr/ch41453.itc", 0x24)
    LoadChrToIndex("apl/ch51613.itc", 0x25)
    SoundLoad(825)
    SoundLoad(2949)
    SoundLoad(2950)
    SoundLoad(2951)
    SoundLoad(2952)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x1, 0x18)
    OP_49()
    SetChrPos(0x18, -36800, 0, 26550, 135)
    OP_D5(0x18, 0x0, 0x20F58, 0x0, 0x0)
    SetMapObjFlags(0x1, 0x1000)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0xA, 0x32, 0x1, 0x20)
    SetChrFlags(0x18, 0x1)
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x206C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0x1, "879mabuta:Layer1(43)", 0x0, 0x1)
    SetMapObjFrame(0x1, "879mabuta:Layer2(44)", 0x0, 0x1)
    SetChrChipByIndex(0x101, 0x20)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, -5000, 0, 2000, 180)
    SetChrChipByIndex(0x10, 0x21)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -6000, 0, -5000, 0)
    SetChrChipByIndex(0x11, 0x21)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -7000, 0, -3500, 0)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -8500, 0, -2500, 45)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -4000, 0, -4500, 0)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -3000, 0, -3000, 0)
    SetChrChipByIndex(0x15, 0x21)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -2000, 0, -4500, 0)
    SetChrChipByIndex(0x16, 0x21)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, -500, 0, -2500, 315)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -5000, 0, -2500, 0)
    SetMapObjFrame(0xFF, "touboku00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "touboku01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "touboku02", 0x0, 0x1)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFlags(0x3, 0x1000)
    SetMapObjFlags(0x4, 0x1000)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x2, 0x19)
    OP_49()
    SetChrPos(0x19, -28500, 0, 21580, 0)
    OP_D5(0x19, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x1A, 0x80)
    OP_78(0x3, 0x1A)
    OP_49()
    SetChrPos(0x1A, -27250, 0, 18000, 0)
    OP_D5(0x1A, 0x0, 0x0, 0x0, 0x0)
    ClearChrFlags(0x1B, 0x80)
    OP_78(0x4, 0x1B)
    OP_49()
    SetChrPos(0x1B, -24500, 0, 18250, 0)
    OP_D5(0x1B, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4953")
    FadeToBright(0, 0)
    Jump("loc_50A0")

    label("loc_4953")

    OP_68(-5000, 1000, 2000, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(22500, 0)
    SetMapObjFrame(0xFF, "hikari", 0x0, 0x1)
    FadeToBright(1000, 0)
    OP_68(-5000, 1000, -300, 2500)
    OP_6F(0x79)
    OP_0D()
    OP_A6(0x101, 0x0, 0x32, 0x1F4, 0xBB8)

    #C0094
    ChrTalk(
        0x101,
        "#00006F#50W#5Pはあはあはあ……ぐうっ……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x10,
        (
            "#12P……フン。\x01",
            "なかなか見上げたもんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x13,
        (
            "#12Pまさか警察官ごときが\x01",
            "俺たち新生国防軍を\x01",
            "ここまで翻弄するとは……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x12,
        (
            "#6P確かシーカー少尉の\x01",
            "元同僚だったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x12,
        "#6Pさすがと言うべきか……\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x17,
        "#11Pよし、武装解除するぞ。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x17,
        (
            "#11Pあまり傷付けずに\x01",
            "捕らえろとの命令だ。\x02",
        )
    )

    CloseMessageWindow()
    PlayBGM("ed7356", 0)
    OP_A6(0x101, 0x0, 0x32, 0x1F4, 0xBB8)

    #C0101
    ChrTalk(
        0x101,
        "#00015F#60W#5P………お断り………だ………\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20500, 10000)

    def lambda_4B51():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4B51)
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(805, 0, 100, 0)
    Sound(802, 0, 100, 0)
    BeginChrThread(0x101, 0, 0, 67)
    OP_0D()
    WaitChrThread(0x101, 2)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(531, 0, 100, 0)
    BeginChrThread(0x17, 3, 0, 54)
    BeginChrThread(0x10, 3, 0, 54)
    BeginChrThread(0x11, 3, 0, 54)
    Sleep(50)
    BeginChrThread(0x12, 3, 0, 54)
    BeginChrThread(0x13, 3, 0, 54)
    Sleep(50)
    Sound(531, 0, 100, 0)
    BeginChrThread(0x14, 3, 0, 54)
    BeginChrThread(0x15, 3, 0, 54)
    BeginChrThread(0x16, 3, 0, 54)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)

    #C0102
    ChrTalk(
        0x10,
        "#12Pこいつ……！\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x11,
        "#12Pまだ動けるのか！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x17)

    #C0104
    ChrTalk(
        0x17,
        (
            "#11P……判らんな。\x01",
            "どうしてそこまでする？\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x17,
        (
            "#11Pどうやら、新たなクロスベルの\x01",
            "体制が気に喰わんようだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x17,
        (
            "#11Pお前一人が抗#2Rあらが#ったところで\x01",
            "状況が変わるものでもなかろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-5000, 1000, 2000, 8000)
    MoveCamera(0, 27, 0, 8000)
    SetCameraDistance(19500, 8000)

    #C0107
    ChrTalk(
        0x101,
        (
            "#00010F#5P#40Wそれでも……\x02\x03",

            "……それでも\x01",
            "誰かが立ち上がらなかったら\x01",
            "何も変わらない……！\x02\x03",

            "#00015F流されるだけじゃなく……\x01",
            "……自分自身の目で\x01",
            "真実を見極めるためにも……\x02\x03",

            "#00007F大切な人たちを……\x01",
            "……取り戻すためにも……！\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(833, 0, 60, 0)
    Fade(500)
    BlurSwitch(0x1, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-5000, 1000, 2000, 500)
    MoveCamera(0, 27, 0, 500)
    SetCameraDistance(17500, 500)
    OP_6F(0x79)
    CancelBlur(0)
    OP_0D()
    Sleep(1200)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0108
    ChrTalk(
        0x101,
        (
            "#00007F#4S#5P俺は……！\x01",
            "絶対に諦めたりしない！\x02\x03",

            "#4S何度でも……！\x01",
            "たとえ足をへし折られても\x01",
            "立ち上がってみせる……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-5000, 1000, -1400, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20250, 0)
    OP_0D()

    #C0109
    ChrTalk(
        0x10,
        "#6Pうっ……\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x13,
        "#12Pこいつは……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x17,
        "#5P……惜しいな。\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x17,
        (
            "#5P一気にかかれ。\x01",
            "抵抗させずに落とすぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x11,
        "#6P了解#4Rラジャ#。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x15,
        "#12P足を狙え。\x02",
    )

    CloseMessageWindow()

    label("loc_50A0")

    Fade(500)
    OP_68(-5000, 1000, -300, 0)
    MoveCamera(135, 35, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(25500, 0)
    SetMapObjFrame(0xFF, "hikari", 0x1, 0x1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x10, 0x23)
    SetChrSubChip(0x10, 0x2)
    SetChrChipByIndex(0x11, 0x23)
    SetChrSubChip(0x11, 0x2)
    SetChrChipByIndex(0x12, 0x23)
    SetChrSubChip(0x12, 0x2)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x2)
    SetChrChipByIndex(0x14, 0x23)
    SetChrSubChip(0x14, 0x2)
    SetChrChipByIndex(0x15, 0x23)
    SetChrSubChip(0x15, 0x2)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x2)
    SetChrChipByIndex(0x17, 0x23)
    SetChrSubChip(0x17, 0x2)
    OP_68(-5000, 1000, 2000, 2500)
    MoveCamera(0, 21, 0, 10000)
    OP_6E(550, 10000)
    SetCameraDistance(17000, 7500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(1)
    CancelBlur(2500)
    BeginChrThread(0x17, 3, 0, 46)
    BeginChrThread(0x10, 3, 0, 47)
    BeginChrThread(0x11, 3, 0, 48)
    BeginChrThread(0x12, 3, 0, 49)
    BeginChrThread(0x13, 3, 0, 50)
    BeginChrThread(0x14, 3, 0, 51)
    BeginChrThread(0x15, 3, 0, 52)
    BeginChrThread(0x16, 3, 0, 53)
    OP_0D()
    Sleep(800)

    #C0115
    ChrTalk(
        0x101,
        (
            "#00013F#5P#40W（……最後まで……\x01",
            "  最後まで諦めるな……）\x02\x03",

            "#00003F（キーア……\x01",
            "  ……エリィ……ティオ……）\x02\x03",

            "（ランディ……ワジ……\x01",
            "  ……セルゲイ課長も……）\x02\x03",

            "#00010F（どうか俺に……\x01",
            "  ……俺に力を貸してくれ……！）\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x17, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)
    OP_6F(0x79)
    Sleep(200)
    Sound(912, 0, 100, 0)
    Fade(500)
    OP_68(-5000, 1000, 2000, 0)
    MoveCamera(90, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(12500, 0)
    SetCameraDistance(22500, 1500)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(30, 30, -1, -1)
    SetChrName("声")

    #A0116
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#2949V#40W#4S──やれやれ。\x02",
        )
    )

    CloseMessageWindow()

    #A0117
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#2950V#40W#4S頼むべき存在を１つ、\x01",
            "忘れているようだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xB86)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    EndChrThread(0x101, 0x0)
    SetChrSubChip(0x101, 0x0)
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0118
    ChrTalk(
        0x101,
        "#00005F#5Pえ……\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x17,
        "#11P……！？\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x16,
        "#5Pい、今のは……\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x13,
        "#11P頭に響いて──\x02",
    )

    CloseMessageWindow()
    Sound(913, 0, 100, 0)
    OP_82(0xC8, 0x12C, 0x1770, 0x7D0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(1500)
    CancelBlur(1000)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    EndChrThread(0x101, 0x0)
    SetChrSubChip(0x101, 0x0)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x10, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_A6(0x10, 0x0, 0x32, 0x1F4, 0xBB8)
    Sleep(500)
    OP_64(0x10)

    #C0122
    ChrTalk(
        0x10,
        "#12Pひっ……！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_A6(0x15, 0x0, 0x32, 0x1F4, 0xBB8)
    Sleep(500)
    OP_64(0x15)

    #C0123
    ChrTalk(
        0x15,
        "#5Pな、なんだ……！？\x02",
    )

    CloseMessageWindow()
    Sound(914, 0, 100, 0)
    OP_82(0x5A, 0x96, 0x1388, 0x1F4)
    Sleep(500)
    Sleep(200)

    def lambda_5643():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5643)
    BeginChrThread(0x17, 3, 0, 55)
    BeginChrThread(0x10, 3, 0, 55)
    Sleep(50)
    BeginChrThread(0x11, 3, 0, 55)
    BeginChrThread(0x12, 3, 0, 55)
    Sleep(50)
    BeginChrThread(0x13, 3, 0, 55)
    BeginChrThread(0x14, 3, 0, 55)
    Sleep(50)
    BeginChrThread(0x15, 3, 0, 55)
    BeginChrThread(0x16, 3, 0, 55)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)
    WaitChrThread(0x101, 2)
    Fade(1000)
    SetChrPos(0x17, -5500, 0, -2150, 315)
    SetChrPos(0x12, -4750, 0, 4450, 300)
    OP_68(-36800, 4000, 26550, 0)
    MoveCamera(3, 30, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(43000, 0)
    OP_68(-16120, 4000, 9190, 8500)
    MoveCamera(288, 3, 0, 8500)
    OP_6E(550, 8500)
    SetCameraDistance(23000, 8500)
    ClearMapObjFlags(0x1, 0x4)
    BeginChrThread(0x18, 3, 0, 65)
    WaitChrThread(0x18, 3)
    OP_6F(0x79)
    OP_0D()
    Sleep(800)
    OP_68(-9220, 3300, 3410, 2000)
    MoveCamera(284, 8, 0, 2000)
    OP_6E(550, 2000)
    SetCameraDistance(28200, 2000)
    OP_6F(0x79)

    #C0124
    ChrTalk(
        0x10,
        "#5P#40W#2S………え…………？\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x16,
        "#11P#40W#2S…………な………………\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        "#00005F#5P#30W………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-9550, 3300, 4600, 0)
    MoveCamera(102, 26, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(22200, 0)
    SetCameraDistance(20700, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(50, 150, -1, -1)
    SetChrName("白き巨狼")

    #A0127
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#2951V#40W#4S去れ──\x01",
            "偽りの聖地を守る兵#2Rつわもの#どもよ。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(40, 155, -1, -1)
    SetChrName("白き巨狼")

    #A0128
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#2952V#40W#4Sこの者は私が預からせてもらう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xB88)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_82(0x96, 0x0, 0xBB8, 0x1F4)
    BeginChrThread(0x17, 3, 0, 56)
    BeginChrThread(0x10, 3, 0, 57)

    #C0129
    ChrTalk(
        0x10,
        "#11Pひ、ひいいいっ……！\x05\x02",
    )

    Sleep(50)
    BeginChrThread(0x11, 3, 0, 57)
    BeginChrThread(0x12, 3, 0, 57)
    Sleep(50)
    BeginChrThread(0x13, 3, 0, 57)
    BeginChrThread(0x14, 3, 0, 57)

    #C0130
    ChrTalk(
        0x15,
        "#11Pうわあああっ……！\x05\x02",
    )

    Sleep(50)
    BeginChrThread(0x15, 3, 0, 57)
    BeginChrThread(0x16, 3, 0, 57)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)
    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_68(-9550, 1700, 4600, 1500)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    OP_9B(0x0, 0x17, 0x9, 0x1770, 0x1388, 0x0)
    SetChrChipByIndex(0x17, 0x23)
    OP_A1(0x17, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Sound(531, 0, 100, 0)
    OP_6F(0x79)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0131
    ChrTalk(
        0x17,
        "#11P#4Sふ、ふざけるなっ……！\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x17,
        (
            "#11P#4S新生クロスベル国防軍が\x01",
            "幻獣ごときに屈して──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-15640, 9800, 8050, 0)
    MoveCamera(315, 35, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15000, 0)
    Sound(913, 0, 100, 0)
    OP_82(0xC8, 0x12C, 0x1770, 0x3E8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-10700, 1000, 4500, 1500)
    MoveCamera(279, 26, 0, 1500)
    OP_6E(550, 1500)
    SetCameraDistance(18500, 1500)
    SetChrPos(0x18, -15350, 0, 8550, 225)
    SetChrPos(0x17, -10700, 0, 4500, 315)
    SetChrFlags(0x12, 0x8)
    OP_93(0x11, 0x0, 0x0)
    OP_93(0x14, 0xE1, 0x0)
    OP_74(0x1, 0x14)
    OP_71(0x1, 0xB5, 0xDC, 0x0, 0x8)
    Sleep(300)
    CancelBlur(0)
    Sleep(850)
    StopSound(913, 700, 100)
    Sound(915, 0, 100, 0)
    SetChrFlags(0x17, 0x8)
    BeginChrThread(0x17, 3, 0, 58)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_79(0x1)
    OP_71(0x1, 0x3D, 0x64, 0x0, 0x20)
    Sound(912, 0, 50, 0)

    #C0133
    ChrTalk(
        0x11,
        "#5P#50W………ぇ……………\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x14,
        "#11P#50W…………ぅぁ………………\x02",
    )

    CloseMessageWindow()
    StopSound(912, 500, 40)
    Fade(500)
    OP_68(-8350, 5600, 2950, 0)
    MoveCamera(106, 31, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(26750, 0)
    OP_68(-8350, 2100, 2950, 1500)
    MoveCamera(92, 36, 0, 1500)
    OP_6E(550, 1500)
    SetCameraDistance(23000, 1500)

    def lambda_5CB6():

        label("loc_5CB6")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5CB6")

    QueueWorkItem2(0x101, 2, lambda_5CB6)

    def lambda_5CC8():

        label("loc_5CC8")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5CC8")

    QueueWorkItem2(0x10, 2, lambda_5CC8)

    def lambda_5CDA():

        label("loc_5CDA")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5CDA")

    QueueWorkItem2(0x11, 2, lambda_5CDA)

    def lambda_5CEC():

        label("loc_5CEC")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5CEC")

    QueueWorkItem2(0x12, 2, lambda_5CEC)

    def lambda_5CFE():

        label("loc_5CFE")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5CFE")

    QueueWorkItem2(0x13, 2, lambda_5CFE)

    def lambda_5D10():

        label("loc_5D10")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5D10")

    QueueWorkItem2(0x14, 2, lambda_5D10)

    def lambda_5D22():

        label("loc_5D22")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5D22")

    QueueWorkItem2(0x15, 2, lambda_5D22)

    def lambda_5D34():

        label("loc_5D34")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_5D34")

    QueueWorkItem2(0x16, 2, lambda_5D34)
    ClearChrFlags(0x12, 0x8)
    OP_64(0x17)
    SetChrFlags(0x17, 0x8)
    OP_74(0x1, 0x5)
    OP_71(0x1, 0xB5, 0xB7, 0x1F4, 0x8)
    Sleep(500)
    ClearChrFlags(0x17, 0x8)
    BeginChrThread(0x17, 3, 0, 59)
    OP_79(0x1)
    OP_74(0x1, 0x3)
    OP_71(0x1, 0xB7, 0xB5, 0x0, 0x8)
    OP_79(0x1)
    OP_74(0x1, 0x14)
    OP_71(0x1, 0x3D, 0x64, 0x12C, 0x20)
    WaitChrThread(0x17, 3)
    OP_6F(0x79)
    OP_0D()
    EndChrThread(0x10, 0x2)
    EndChrThread(0x11, 0x2)
    EndChrThread(0x12, 0x2)
    EndChrThread(0x13, 0x2)
    EndChrThread(0x14, 0x2)
    EndChrThread(0x15, 0x2)
    EndChrThread(0x16, 0x2)
    Sleep(500)

    #C0135
    ChrTalk(
        0x17,
        "#60W#12P…………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(50, 150, -1, -1)
    SetChrName("白き巨狼")

    #A0136
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#30W──さて。\x01",
            "同じ事を言おうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrSubChip(0x17, 0x3)
    OP_A6(0x17, 0x0, 0x32, 0x1F4, 0xBB8)
    Sleep(300)

    #C0137
    ChrTalk(
        0x17,
        "#60W#12P#60W………その必要はない…………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-7900, 1000, 2580, 0)
    MoveCamera(354, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15500, 0)
    SetChrSubChip(0x17, 0x1)
    SetCameraDistance(14000, 1500)
    OP_6F(0x79)
    OP_0D()
    Sleep(200)
    Fade(250)
    SetChrFlags(0x17, 0x20)
    ClearChrFlags(0x17, 0x2)
    SetChrSubChip(0x17, 0x1)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_93(0x17, 0x87, 0x1F4)
    Sleep(500)
    SetCameraDistance(25000, 750)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x12C, 0x0, 0xBB8, 0x1F4)

    #C0138
    ChrTalk(
        0x17,
        "#5S#5P撤収──ッ！！！\x05\x02",
    )

    Sleep(1000)
    CancelBlur(500)
    OP_6F(0x79)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(-4700, 2550, -400, 0)
    MoveCamera(310, 9, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21000, 0)
    OP_68(-4700, 1550, -400, 5000)
    SetCameraDistance(25000, 5000)
    BeginChrThread(0x18, 0, 0, 63)
    Sound(871, 0, 60, 0)
    Sound(825, 2, 40, 0)
    BeginChrThread(0x17, 3, 0, 61)
    Sleep(50)
    BeginChrThread(0x10, 3, 0, 62)
    Sleep(50)
    BeginChrThread(0x11, 3, 0, 62)

    #C0139
    ChrTalk(
        0x11,
        "#5Pうわあああああああっ！！\x05\x02",
    )

    Sleep(50)
    BeginChrThread(0x12, 3, 0, 62)
    Sleep(50)
    BeginChrThread(0x13, 3, 0, 62)
    Sleep(50)
    BeginChrThread(0x14, 3, 0, 62)
    Sound(916, 0, 100, 0)

    #C0140
    ChrTalk(
        0x14,
        "#11Pめ、女神さまああああっ！！\x05\x02",
    )

    Sleep(50)
    BeginChrThread(0x15, 3, 0, 62)
    Sleep(50)
    BeginChrThread(0x16, 3, 0, 62)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x11, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)
    CloseMessageWindow()
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x18, 0x0)
    OP_82(0x0, 0x46, 0xBB8, 0x5DC)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    StopSound(825, 1000, 40)
    OP_68(-5000, 1200, 2000, 0)
    MoveCamera(354, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)
    SetCameraDistance(19000, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_64(0x101)
    Sleep(1000)

    #C0141
    ChrTalk(
        0x101,
        "#00011F#5P#30W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_68(-7330, 3200, 1550, 2000)
    MoveCamera(348, 19, 0, 2000)
    OP_6E(550, 2000)
    SetCameraDistance(20760, 2000)
    BeginChrThread(0x18, 0, 0, 66)
    BeginChrThread(0x1D, 1, 0, 72)
    OP_74(0x1, 0x14)
    OP_71(0x1, 0x172, 0x19A, 0x1, 0x20)
    OP_93(0x18, 0x87, 0x0)
    OP_9B(0x0, 0x18, 0x0, 0x1B58, 0xBB8, 0x0)
    EndChrThread(0x18, 0x0)
    EndChrThread(0x1D, 0x1)
    OP_74(0x1, 0x14)
    OP_71(0x1, 0x3D, 0x64, 0x2BC, 0x20)
    OP_6F(0x79)
    Sleep(800)
    SetMessageWindowPos(20, 120, -1, -1)
    SetChrName("白き巨狼")

    #A0142
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#30Wフム、さすがに\x01",
            "驚かせてしまったか。\x02",
        )
    )

    CloseMessageWindow()

    #A0143
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#30Wこの姿に戻ったのは久しいゆえ、\x01",
            "いささか加減が分からぬな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(805, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0144
    ChrTalk(
        0x101,
        (
            "#00006F#5P#30W……言いたいことは\x01",
            "色々あるんだけど……\x02\x03",

            "とりあえず\x01",
            "これだけは言わせてくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_74(0x1, 0x14)
    OP_71(0x1, 0x1A4, 0x1AE, 0x0, 0x8)
    OP_79(0x1)
    OP_71(0x1, 0x1AE, 0x1D6, 0x0, 0x20)
    SetMessageWindowPos(30, 120, -1, -1)
    SetChrName("白き巨狼")

    #A0145
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#30Wフム、なんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-7330, 3200, 1550, 1200)
    MoveCamera(332, -2, 0, 1200)
    OP_6E(550, 1200)
    SetCameraDistance(20760, 1200)
    TurnDirection(0x101, 0x18, 500)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x190)

    #C0146
    ChrTalk(
        0x101,
        (
            "#00007F#12P#4S#N──ツァイト！\x01",
            "さすがにタイミング良すぎだろ！？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x1770)
    WaitBGM()
    OP_24(0x339)
    SetScenarioFlags(0x22, 0)
    NewScene("e4200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_45_4622 end

    def Function_46_6377(): pass

    label("Function_46_6377")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_96(0xFE, 0xFFFFEC78, 0x0, 0xFFFFF254, 0xBB8, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_46_6377 end

    def Function_47_63B9(): pass

    label("Function_47_63B9")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -9000, 0, -3000, 4000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_47_63B9 end

    def Function_48_63FB(): pass

    label("Function_48_63FB")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -10500, 0, 1000, 4000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_48_63FB end

    def Function_49_643D(): pass

    label("Function_49_643D")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -10700, 0, 4500, 4200, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_49_643D end

    def Function_50_647F(): pass

    label("Function_50_647F")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -1000, 0, -2000, 4000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_50_647F end

    def Function_51_64C1(): pass

    label("Function_51_64C1")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -2000, 0, 6500, 6000, 0x1)
    OP_95(0xFE, -6000, 0, 7500, 6000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_51_64C1 end

    def Function_52_6517(): pass

    label("Function_52_6517")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, 1000, 0, 2000, 5000, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_52_6517 end

    def Function_53_6559(): pass

    label("Function_53_6559")

    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -2000, 0, 6500, 4200, 0x0)
    TurnDirection(0xFE, 0x101, 500)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Sound(531, 0, 70, 0)
    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x3E8, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_53_6559 end

    def Function_54_659B(): pass

    label("Function_54_659B")

    SetChrChipByIndex(0xFE, 0x23)
    OP_A1(0xFE, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    Return()

    # Function_54_659B end

    def Function_55_65A9(): pass

    label("Function_55_65A9")

    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    TurnDirection(0xFE, 0x18, 500)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_55_65A9 end

    def Function_56_65BF(): pass

    label("Function_56_65BF")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_65D6():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_65D6)
    WaitChrThread(0xFE, 1)
    Sleep(500)
    OP_64(0xFE)
    Return()

    # Function_56_65BF end

    def Function_57_65F5(): pass

    label("Function_57_65F5")

    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_660C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_660C)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0xBB8, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0xFE, 1)
    Sleep(500)
    OP_64(0xFE)
    Return()

    # Function_57_65F5 end

    def Function_58_664A(): pass

    label("Function_58_664A")

    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -10700, 500, 4500, 0, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x7)
    ClearChrFlags(0xFE, 0x100)
    SetChrFlags(0xFE, 0x800)
    SetChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    OP_D3(0x17, 0x1, "Null_kuti(41)")
    OP_52(0xFE, 0x23, (scpexpr(EXPR_PUSH_LONG, 0xAF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_D5(0xFE, 0x4E20, 0x41EB0, 0x0, 0x0)
    OP_D5(0xFE, 0x4E20, 0x41EB0, 0xFFFF8AD0, 0x64)
    OP_D5(0xFE, 0x4E20, 0x41EB0, 0xEA60, 0x190)
    OP_D5(0xFE, 0x4E20, 0x41EB0, 0x61A8, 0x190)
    OP_63(0xFE, 0x0, 300, 0x28, 0x2B, 0x64, 0x0)

    label("loc_6723")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6749")
    OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
    Sleep(1000)
    Jump("loc_6723")

    label("loc_6749")

    Return()

    # Function_58_664A end

    def Function_59_674A(): pass

    label("Function_59_674A")

    Sound(915, 0, 100, 0)
    SetChrChip(0x0, 0xFE, 0x5, 0x96)
    SetChrFlags(0xFE, 0x1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x64, 0x0, 0x1388, 0x12C)
    OP_D3(0x17, 0xFF, "")
    OP_52(0xFE, 0x23, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x4)
    SetChrFlags(0xFE, 0x100)
    ClearChrFlags(0xFE, 0x800)
    OP_D5(0xFE, 0x4E20, 0x0, 0x0, 0x0)
    Sound(844, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFE124, 0x0, 0xA14, 0x1F4, 0x9C4)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    OP_93(0xFE, 0x13B, 0x0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -7900, 150, 2580, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_6831():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6831)
    Sound(811, 0, 100, 0)
    OP_A1(0xFE, 0x3E8, 0x2, 0x3, 0x2)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_59_674A end

    def Function_60_6858(): pass

    label("Function_60_6858")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6876")
    OP_A1(0xFE, 0x9C4, 0x8, 0x10, 0x11, 0x12, 0x11, 0x10, 0x13, 0x14, 0x13)
    Jump("Function_60_6858")

    label("loc_6876")

    Return()

    # Function_60_6858 end

    def Function_61_6877(): pass

    label("Function_61_6877")

    SetChrFlags(0xFE, 0x2)
    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 64)
    BeginChrThread(0xFE, 1, 0, 60)
    OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1770, 0x0)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0xFE, 0x1)
    OP_64(0xFE)
    Return()

    # Function_61_6877 end

    def Function_62_68BC(): pass

    label("Function_62_68BC")

    OP_63(0xFE, 0x0, 1700, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0xFE, 0x87, 0x1F4)
    BeginChrThread(0xFE, 0, 0, 64)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1770, 0x0)
    EndChrThread(0xFE, 0x0)
    OP_64(0xFE)
    Return()

    # Function_62_68BC end

    def Function_63_68FA(): pass

    label("Function_63_68FA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_691E")
    OP_82(0x3C, 0x64, 0x1388, 0x1F4)
    Sleep(500)
    Jump("Function_63_68FA")

    label("loc_691E")

    Return()

    # Function_63_68FA end

    def Function_64_691F(): pass

    label("Function_64_691F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6969")
    PlayEffect(0x1, 0xFF, 0xFE, 0x4, 0, 200, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jump("Function_64_691F")

    label("loc_6969")

    Return()

    # Function_64_691F end

    def Function_65_696A(): pass

    label("Function_65_696A")

    BeginChrThread(0xFE, 0, 0, 66)
    BeginChrThread(0x1D, 1, 0, 71)
    OP_74(0x1, 0x14)
    OP_71(0x1, 0x172, 0x19A, 0x1, 0x20)

    def lambda_698B():
        OP_9B(0x0, 0xFE, 0x163, 0x61A8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_698B)
    Sleep(1800)
    OP_82(0x64, 0x1F4, 0xFA0, 0x1F4)
    BeginChrThread(0x19, 3, 0, 68)
    Sleep(1000)
    OP_82(0x64, 0x1F4, 0xFA0, 0x1F4)
    BeginChrThread(0x1A, 3, 0, 69)
    Sleep(1000)
    OP_82(0x64, 0x1F4, 0xFA0, 0x1F4)
    BeginChrThread(0x1B, 3, 0, 70)
    WaitChrThread(0xFE, 1)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0x1D, 0x1)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -15430, 500, 8570, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    OP_74(0x1, 0x14)
    OP_71(0x1, 0x3D, 0x64, 0x2BC, 0x20)
    Return()

    # Function_65_696A end

    def Function_66_6A3D(): pass

    label("Function_66_6A3D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6AD2")
    OP_82(0x5A, 0x96, 0x1388, 0x1F4)
    PlayEffect(0x1, 0xFF, 0xFE, 0x4, 0, 500, -2500, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFE, 0x4, 0, 500, 2500, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jump("Function_66_6A3D")

    label("loc_6AD2")

    Return()

    # Function_66_6A3D end

    def Function_67_6AD3(): pass

    label("Function_67_6AD3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6AF1")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_67_6AD3")

    label("loc_6AF1")

    Return()

    # Function_67_6AD3 end

    def Function_68_6AF2(): pass

    label("Function_68_6AF2")

    Sound(917, 0, 80, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -28500, 500, 21580, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -30500, 1500, 20080, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)

    def lambda_6B6B():
        OP_98(0xFE, 0x0, 0xFFFFF448, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B6B)
    OP_D5(0xFE, 0x0, 0x0, 0x7530, 0x3E8)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -28500, 500, 21580, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)
    OP_75(0x2, 0x1, 0x3E8)
    Sleep(1000)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_68_6AF2 end

    def Function_69_6BDC(): pass

    label("Function_69_6BDC")

    Sound(917, 0, 70, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -27250, 500, 18000, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)

    def lambda_6C1E():
        OP_98(0xFE, 0x0, 0xFFFFF448, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6C1E)
    OP_D5(0xFE, 0x0, 0x0, 0xFFFF8AD0, 0x3E8)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -27250, 500, 18000, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)
    OP_75(0x3, 0x1, 0x3E8)
    Sleep(1000)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_69_6BDC end

    def Function_70_6C8F(): pass

    label("Function_70_6C8F")

    Sound(917, 0, 60, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -24500, 500, 18250, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)

    def lambda_6CD1():
        OP_98(0xFE, 0x0, 0xFFFFF448, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6CD1)
    OP_D5(0xFE, 0x0, 0x0, 0x7530, 0x3E8)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, -24500, 500, 18250, 0, 0, 0, 7000, 7000, 7000, 0xFF, 0, 0, 0, 0)
    OP_75(0x4, 0x1, 0x3E8)
    Sleep(1000)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_70_6C8F end

    def Function_71_6D42(): pass

    label("Function_71_6D42")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D5E")
    Sleep(100)
    Sound(914, 0, 100, 0)
    Sleep(800)
    Jump("Function_71_6D42")

    label("loc_6D5E")

    Return()

    # Function_71_6D42 end

    def Function_72_6D5F(): pass

    label("Function_72_6D5F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6D7B")
    Sleep(250)
    Sound(914, 0, 100, 0)
    Sleep(650)
    Jump("Function_72_6D5F")

    label("loc_6D7B")

    Return()

    # Function_72_6D5F end

    SaveToFile()

Try(main)
