from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4300.bin",                # FileName
        "e4300",                    # MapName
        "e4300",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\x00',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 2],
    )

    BuildStringList((
        "e4300",                  # 0
        "メルカバ伍号機",         # 1
        "メルカバ玖号機",         # 2
        "共和国飛行艇",           # 3
        "共和国飛行艇",           # 4
        "共和国飛行艇",           # 5
        "共和国飛行艇",           # 6
        "共和国飛行艇",           # 7
        "アイオーン２",           # 8
        "パテルマテル",           # 9
        "レン",                   # 10
        "SE制御",                 # 11
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(708, 0)                                        # 0

    ScpFunction((
        "Function_0_2C4",          # 00, 0
        "Function_1_39D",          # 01, 1
        "Function_2_54E",          # 02, 2
        "Function_3_576",          # 03, 3
        "Function_4_58B",          # 04, 4
        "Function_5_C9A",          # 05, 5
        "Function_6_D4A",          # 06, 6
        "Function_7_DB3",          # 07, 7
        "Function_8_F16",          # 08, 8
        "Function_9_1079",         # 09, 9
        "Function_10_11DC",        # 0A, 10
        "Function_11_133F",        # 0B, 11
        "Function_12_14A2",        # 0C, 12
        "Function_13_166A",        # 0D, 13
        "Function_14_178F",        # 0E, 14
        "Function_15_2062",        # 0F, 15
        "Function_16_20C4",        # 10, 16
        "Function_17_20E3",        # 11, 17
        "Function_18_218E",        # 12, 18
        "Function_19_21F3",        # 13, 19
        "Function_20_2240",        # 14, 20
        "Function_21_22A9",        # 15, 21
        "Function_22_22DA",        # 16, 22
        "Function_23_2DA1",        # 17, 23
        "Function_24_2F22",        # 18, 24
        "Function_25_30A3",        # 19, 25
        "Function_26_33A0",        # 1A, 26
        "Function_27_33E7",        # 1B, 27
        "Function_28_349B",        # 1C, 28
        "Function_29_407B",        # 1D, 29
        "Function_30_409E",        # 1E, 30
        "Function_31_40DB",        # 1F, 31
        "Function_32_416B",        # 20, 32
        "Function_33_42D7",        # 21, 33
        "Function_34_5469",        # 22, 34
        "Function_35_55D2",        # 23, 35
        "Function_36_5681",        # 24, 36
        "Function_37_5688",        # 25, 37
        "Function_38_56CD",        # 26, 38
        "Function_39_5715",        # 27, 39
        "Function_40_5755",        # 28, 40
        "Function_41_577A",        # 29, 41
        "Function_42_57A5",        # 2A, 42
        "Function_43_57CF",        # 2B, 43
        "Function_44_580C",        # 2C, 44
        "Function_45_581C",        # 2D, 45
        "Function_46_581D",        # 2E, 46
        "Function_47_59B6",        # 2F, 47
        "Function_48_59C6",        # 30, 48
        "Function_49_59E5",        # 31, 49
        "Function_50_5A66",        # 32, 50
        "Function_51_5B00",        # 33, 51
        "Function_52_5B9A",        # 34, 52
        "Function_53_5C40",        # 35, 53
        "Function_54_5CE0",        # 36, 54
        "Function_55_5D45",        # 37, 55
        "Function_56_5D6F",        # 38, 56
        "Function_57_5D97",        # 39, 57
        "Function_58_5DC4",        # 3A, 58
        "Function_59_5DD5",        # 3B, 59
        "Function_60_5EEC",        # 3C, 60
        "Function_61_5F0E",        # 3D, 61
        "Function_62_602F",        # 3E, 62
    ))


    def Function_0_2C4(): pass

    label("Function_0_2C4")

    ClearMapObjFlags(0x8, 0x2000000)
    ClearMapObjFlags(0xA, 0x2000000)
    ClearMapObjFlags(0x0, 0x2000000)
    ClearMapObjFlags(0x1, 0x2000000)
    SetMapObjFlags(0x2, 0x2000000)
    SetMapObjFlags(0x3, 0x2000000)
    SetMapObjFlags(0x4, 0x2000000)
    SetMapObjFlags(0x5, 0x2000000)
    SetMapObjFlags(0x6, 0x2000000)
    SetMapObjFlags(0x7, 0x2000000)
    SetMapObjFlags(0x9, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0xD, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)
    SetMapObjFlags(0xF, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 3)), scpexpr(EXPR_END)), "loc_374")
    ClearMapObjFlags(0x2, 0x2000000)
    ClearMapObjFlags(0x3, 0x2000000)
    ClearMapObjFlags(0x4, 0x2000000)
    ClearMapObjFlags(0x5, 0x2000000)
    ClearMapObjFlags(0x6, 0x2000000)
    ClearMapObjFlags(0xB, 0x2000000)
    ClearMapObjFlags(0xC, 0x2000000)
    ClearMapObjFlags(0xD, 0x2000000)
    ClearMapObjFlags(0xE, 0x2000000)
    ClearMapObjFlags(0xF, 0x2000000)
    ClearMapObjFlags(0x7, 0x2000000)
    Jump("loc_374")

    label("loc_374")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 4)), scpexpr(EXPR_END)), "loc_383")
    ClearMapObjFlags(0x9, 0x2000000)

    label("loc_383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_39C")
    ClearMapObjFlags(0x7, 0x2000000)
    ClearMapObjFlags(0xA, 0x2000000)

    label("loc_39C")

    Return()

    # Function_0_2C4 end

    def Function_1_39D(): pass

    label("Function_1_39D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_3AE")
    ClearScenarioFlags(0x22, 0)
    Jump("loc_54D")

    label("loc_3AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_3C5")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 4)
    Jump("loc_54D")

    label("loc_3C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_3D6")
    ClearScenarioFlags(0x22, 2)
    Jump("loc_54D")

    label("loc_3D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_3ED")
    ClearScenarioFlags(0x22, 3)
    SetScenarioFlags(0x0, 0)
    Event(0, 7)
    Jump("loc_54D")

    label("loc_3ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_404")
    ClearScenarioFlags(0x22, 4)
    SetScenarioFlags(0x0, 0)
    Event(0, 8)
    Jump("loc_54D")

    label("loc_404")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_41B")
    ClearScenarioFlags(0x22, 5)
    SetScenarioFlags(0x0, 0)
    Event(0, 9)
    Jump("loc_54D")

    label("loc_41B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_432")
    ClearScenarioFlags(0x22, 6)
    SetScenarioFlags(0x0, 0)
    Event(0, 10)
    Jump("loc_54D")

    label("loc_432")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_449")
    ClearScenarioFlags(0x22, 7)
    SetScenarioFlags(0x0, 0)
    Event(0, 11)
    Jump("loc_54D")

    label("loc_449")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_460")
    ClearScenarioFlags(0x23, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 12)
    Jump("loc_54D")

    label("loc_460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_474")
    ClearScenarioFlags(0x23, 1)
    Event(0, 14)
    Jump("loc_54D")

    label("loc_474")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_485")
    ClearScenarioFlags(0x23, 2)
    Jump("loc_54D")

    label("loc_485")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_496")
    ClearScenarioFlags(0x23, 3)
    Jump("loc_54D")

    label("loc_496")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 4)), scpexpr(EXPR_END)), "loc_4AA")
    ClearScenarioFlags(0x23, 4)
    Event(0, 22)
    Jump("loc_54D")

    label("loc_4AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 5)), scpexpr(EXPR_END)), "loc_4BE")
    ClearScenarioFlags(0x23, 5)
    Event(0, 28)
    Jump("loc_54D")

    label("loc_4BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 6)), scpexpr(EXPR_END)), "loc_4D5")
    ClearScenarioFlags(0x23, 6)
    SetScenarioFlags(0x0, 0)
    Event(0, 32)
    Jump("loc_54D")

    label("loc_4D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 7)), scpexpr(EXPR_END)), "loc_4E6")
    ClearScenarioFlags(0x23, 7)
    Jump("loc_54D")

    label("loc_4E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 0)), scpexpr(EXPR_END)), "loc_4F7")
    ClearScenarioFlags(0x24, 0)
    Jump("loc_54D")

    label("loc_4F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 1)), scpexpr(EXPR_END)), "loc_508")
    ClearScenarioFlags(0x24, 1)
    Jump("loc_54D")

    label("loc_508")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 2)), scpexpr(EXPR_END)), "loc_519")
    ClearScenarioFlags(0x24, 2)
    Jump("loc_54D")

    label("loc_519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 3)), scpexpr(EXPR_END)), "loc_52D")
    ClearScenarioFlags(0x24, 3)
    Event(0, 33)
    Jump("loc_54D")

    label("loc_52D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 4)), scpexpr(EXPR_END)), "loc_541")
    ClearScenarioFlags(0x24, 4)
    Event(0, 61)
    Jump("loc_54D")

    label("loc_541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x24, 5)), scpexpr(EXPR_END)), "loc_54D")
    ClearScenarioFlags(0x24, 5)

    label("loc_54D")

    Return()

    # Function_1_39D end

    def Function_2_54E(): pass

    label("Function_2_54E")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x7D0)
    OP_F3(100000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_575")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x23A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_575")

    Return()

    # Function_2_54E end

    def Function_3_576(): pass

    label("Function_3_576")

    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    Return()

    # Function_3_576 end

    def Function_4_58B(): pass

    label("Function_4_58B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev17086.eff")
    CreatePortrait(0, 16, 20, 528, 84, 0, 0, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis508.itp")
    CreatePortrait(1, 280, 60, 792, 124, 0, 0, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis509.itp")
    CreatePortrait(2, 20, 60, 532, 124, 0, 0, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis510.itp")
    SoundLoad(132)
    SoundLoad(497)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x8, 0x8)
    OP_49()
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x1000)
    OP_71(0x8, 0x1, 0x78, 0x0, 0x20)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x0, 0x9)
    OP_49()
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_71(0x0, 0x1, 0x78, 0x0, 0x20)
    Call(0, 3)
    OP_F3(100000)
    BeginChrThread(0x12, 1, 0, 5)
    Sleep(2200)
    SetChrPos(0x8, 7500, 0, -85000, 0)
    SetChrPos(0x9, -7500, 0, -65000, 0)

    def lambda_6B1():
        OP_9B(0x1, 0xFE, 0x0, 0x249F0, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_6B1)

    def lambda_6C6():
        OP_9B(0x1, 0xFE, 0x0, 0x249F0, 0xC350, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6C6)
    OP_68(0, 1500, 0, 0)
    MoveCamera(180, -10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(45000, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x8, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x9, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0x9, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0x0)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    CancelBlur(0)
    Fade(500)
    SetChrPos(0x8, 7500, 0, -335000, 0)
    SetChrPos(0x9, -7500, 0, -315000, 0)

    def lambda_832():
        OP_9B(0x1, 0xFE, 0x0, 0x6A338, 0xD6D8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_832)

    def lambda_847():
        OP_9B(0x1, 0xFE, 0x0, 0x65518, 0xD6D8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_847)
    OP_68(0, 2500, -250000, 0)
    MoveCamera(40, 25, 5, 0)
    SetCameraDistance(80000, 0)
    OP_68(0, 2500, 0, 7000)
    MoveCamera(10, 5, 5, 7000)
    SetCameraDistance(300000, 7000)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x8, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x9, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0x9, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(4000)
    StopSound(497, 1900, 90)
    Sleep(2000)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    Fade(500)
    BeginChrThread(0x12, 1, 0, 6)
    SetChrPos(0x8, 7500, 20000, -10000, 0)
    SetChrPos(0x9, -7500, 20000, 10000, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x8, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0x9, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0x9, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 500, 0xFF, 0, 0, 0, 0)
    OP_68(0, 22500, 2500, 0)
    MoveCamera(245, 30, 0, 0)
    SetCameraDistance(55000, 0)
    OP_68(0, 22500, 0, 6000)
    SetCameraDistance(50000, 6000)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(3500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Fade(500)
    SetChrPos(0x8, 10500, 20000, -25000, 0)
    SetChrPos(0x9, -10500, 20000, 10000, 0)
    OP_68(10500, 22500, -22500, 0)
    MoveCamera(270, 20, 0, 0)
    SetCameraDistance(29000, 0)
    OP_68(10500, 22500, -21500, 6000)
    MoveCamera(240, 25, 0, 6000)
    SetCameraDistance(32000, 6000)
    OP_0D()
    Sleep(500)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(3500)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_6F(0x79)
    Fade(500)
    SetChrPos(0x8, 7500, 20000, -15000, 0)
    SetChrPos(0x9, -7500, 20000, 10000, 0)
    OP_68(-7500, 22500, 12000, 0)
    MoveCamera(150, 25, 0, 0)
    SetCameraDistance(35000, 0)
    OP_68(-7500, 22500, 13000, 8000)
    MoveCamera(120, 30, 0, 8000)
    SetCameraDistance(29000, 8000)
    OP_0D()
    Sleep(500)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(3500)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(1500)
    SetCameraDistance(24000, 2000)
    FadeToDark(2000, 0, -1)
    StopSound(132, 2000, 100)
    StopSound(497, 2000, 100)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_4_58B end

    def Function_5_C9A(): pass

    label("Function_5_C9A")

    Sound(132, 2, 20, 0)
    Sound(497, 2, 20, 0)
    Sleep(50)
    OP_25(0x84, 0x19)
    OP_25(0x1F1, 0x19)
    Sleep(50)
    OP_25(0x84, 0x1E)
    OP_25(0x1F1, 0x1E)
    Sleep(50)
    OP_25(0x84, 0x23)
    OP_25(0x1F1, 0x23)
    Sleep(50)
    OP_25(0x84, 0x28)
    OP_25(0x1F1, 0x28)
    Sleep(50)
    OP_25(0x84, 0x2D)
    OP_25(0x1F1, 0x2D)
    Sleep(50)
    OP_25(0x84, 0x32)
    OP_25(0x1F1, 0x32)
    Sleep(50)
    OP_25(0x84, 0x37)
    OP_25(0x1F1, 0x37)
    Sleep(50)
    OP_25(0x84, 0x3C)
    OP_25(0x1F1, 0x3C)
    Sleep(50)
    OP_25(0x84, 0x4B)
    OP_25(0x1F1, 0x4B)
    Sleep(50)
    OP_25(0x84, 0x50)
    OP_25(0x1F1, 0x50)
    Sleep(50)
    OP_25(0x84, 0x55)
    OP_25(0x1F1, 0x55)
    Sleep(50)
    OP_25(0x84, 0x5A)
    OP_25(0x1F1, 0x5A)
    Sleep(50)
    OP_25(0x84, 0x5F)
    OP_25(0x1F1, 0x5F)
    Sleep(50)
    OP_25(0x84, 0x64)
    OP_25(0x1F1, 0x64)
    Sleep(2200)
    Sound(499, 0, 80, 0)
    Return()

    # Function_5_C9A end

    def Function_6_D4A(): pass

    label("Function_6_D4A")

    Sound(497, 2, 20, 0)
    Sleep(50)
    OP_25(0x1F1, 0x19)
    Sleep(50)
    OP_25(0x1F1, 0x1E)
    Sleep(50)
    OP_25(0x1F1, 0x23)
    Sleep(50)
    OP_25(0x1F1, 0x28)
    Sleep(50)
    OP_25(0x1F1, 0x2D)
    Sleep(50)
    OP_25(0x1F1, 0x32)
    Sleep(50)
    OP_25(0x1F1, 0x37)
    Sleep(50)
    OP_25(0x1F1, 0x3C)
    Sleep(50)
    OP_25(0x1F1, 0x4B)
    Sleep(50)
    OP_25(0x1F1, 0x50)
    Sleep(50)
    OP_25(0x1F1, 0x55)
    Sleep(50)
    OP_25(0x1F1, 0x5A)
    Sleep(50)
    OP_25(0x1F1, 0x5F)
    Sleep(50)
    OP_25(0x1F1, 0x64)
    Return()

    # Function_6_D4A end

    def Function_7_DB3(): pass

    label("Function_7_DB3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev17086.eff")
    SoundLoad(132)
    SoundLoad(497)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x0, 0x9)
    OP_49()
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_71(0x0, 0x1, 0x78, 0x0, 0x20)
    Call(0, 3)
    PlayEffect(0x0, 0x0, 0x9, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x9, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x9, 0, 0, 0, 0)
    OP_68(0, 1500, 0, 0)
    MoveCamera(280, 15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(40000, 0)
    OP_68(0, 1500, 3000, 6000)
    MoveCamera(230, 20, 0, 6000)
    OP_6E(800, 6000)
    SetCameraDistance(30000, 6000)
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4000)
    StopSound(132, 1000, 100)
    StopSound(497, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_DB3 end

    def Function_8_F16(): pass

    label("Function_8_F16")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev17086.eff")
    SoundLoad(132)
    SoundLoad(497)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x0, 0x9)
    OP_49()
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_71(0x0, 0x1, 0x78, 0x0, 0x20)
    Call(0, 3)
    SetChrPos(0x9, 0, 0, 0, 0)
    OP_68(0, 1500, 3000, 0)
    MoveCamera(150, 30, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(35000, 0)
    OP_68(0, 1500, 3000, 6000)
    MoveCamera(125, 15, 0, 6000)
    OP_6E(800, 6000)
    SetCameraDistance(30000, 6000)
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x9, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x9, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4000)
    StopSound(132, 1000, 100)
    StopSound(497, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 4)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_F16 end

    def Function_9_1079(): pass

    label("Function_9_1079")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev17086.eff")
    SoundLoad(132)
    SoundLoad(497)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x0, 0x9)
    OP_49()
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_71(0x0, 0x1, 0x78, 0x0, 0x20)
    Call(0, 3)
    SetChrPos(0x9, 0, 0, 0, 0)
    OP_68(0, 1500, 3000, 0)
    MoveCamera(150, 30, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(35000, 0)
    OP_68(0, 1500, 3000, 6000)
    MoveCamera(125, 15, 0, 6000)
    OP_6E(800, 6000)
    SetCameraDistance(30000, 6000)
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x9, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x9, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4000)
    StopSound(132, 1000, 100)
    StopSound(497, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 5)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_9_1079 end

    def Function_10_11DC(): pass

    label("Function_10_11DC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev17086.eff")
    SoundLoad(132)
    SoundLoad(497)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x0, 0x9)
    OP_49()
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_71(0x0, 0x1, 0x78, 0x0, 0x20)
    Call(0, 3)
    SetChrPos(0x9, 0, 0, 0, 0)
    OP_68(0, 1500, 0, 0)
    MoveCamera(280, 15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(40000, 0)
    OP_68(0, 1500, 3000, 6000)
    MoveCamera(230, 20, 0, 6000)
    OP_6E(800, 6000)
    SetCameraDistance(30000, 6000)
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x9, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x9, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4000)
    StopSound(132, 1000, 100)
    StopSound(497, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 7)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_10_11DC end

    def Function_11_133F(): pass

    label("Function_11_133F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev17086.eff")
    SoundLoad(132)
    SoundLoad(497)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x0, 0x9)
    OP_49()
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_71(0x0, 0x1, 0x78, 0x0, 0x20)
    Call(0, 3)
    SetChrPos(0x9, 0, 0, 0, 0)
    OP_68(0, 1500, 0, 0)
    MoveCamera(280, 15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(40000, 0)
    OP_68(0, 1500, 3000, 6000)
    MoveCamera(230, 20, 0, 6000)
    OP_6E(800, 6000)
    SetCameraDistance(30000, 6000)
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x9, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x9, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4000)
    StopSound(132, 1000, 100)
    StopSound(497, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_133F end

    def Function_12_14A2(): pass

    label("Function_12_14A2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 16, 20, 528, 84, 0, 0, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis513.itp")
    LoadEffect(0x0, "event/ev17086.eff")
    SoundLoad(132)
    SoundLoad(497)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x0, 0x9)
    OP_49()
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_71(0x0, 0x1, 0x78, 0x0, 0x20)
    Call(0, 3)
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    Sleep(1500)
    SetChrPos(0x9, 0, 0, -100000, 0)
    OP_D5(0x9, 0x0, 0xFFFFB1E0, 0x0, 0x0)
    OP_68(0, 1500, 0, 0)
    MoveCamera(325, -25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(45000, 0)
    MoveCamera(0, 5, 0, 10000)
    BeginChrThread(0x9, 1, 0, 13)
    PlayEffect(0x0, 0x0, 0x9, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x9, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(3500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_6F(0x79)
    SetCameraDistance(40000, 7000)
    Sleep(5000)
    StopSound(132, 1000, 100)
    StopSound(497, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x23, 1)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_14A2 end

    def Function_13_166A(): pass

    label("Function_13_166A")

    SetCameraDistance(60000, 4500)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 0, 0, -100000)
    OP_9F(0x1, -10000, 0, 40000)
    OP_9F(0x1, -10000, 0, 80000)
    OP_9F(0x1, 0, 0, 100000)
    OP_9F(0x1, 15000, 0, 108000)
    OP_9F(0x1, 30000, 0, 108000)
    OP_9F(0x1, 45000, 0, 100000)
    OP_9F(0x2, 0xFE, 30000, 0x6)
    SetCameraDistance(45000, 4500)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 45000, 0, 100000)
    OP_9F(0x1, 50000, 0, 80000)
    OP_9F(0x1, 50000, 0, 60000)
    OP_9F(0x1, 30000, 0, 30000)
    OP_9F(0x1, 20000, 0, 20000)
    OP_9F(0x2, 0xFE, 30000, 0x6)
    OP_95(0xFE, 10000, 0, 10000, 10000, 0x0)
    OP_95(0xFE, 7500, 0, 7500, 7500, 0x0)
    OP_95(0xFE, 5000, 0, 5000, 5000, 0x0)
    OP_95(0xFE, 0, 0, 0, 2500, 0x0)
    Return()

    # Function_13_166A end

    def Function_14_178F(): pass

    label("Function_14_178F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev17086.eff")
    LoadEffect(0x1, "event/ev17024.eff")
    SoundLoad(132)
    SoundLoad(497)
    SoundLoad(496)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x8, 0x8)
    OP_49()
    SetMapObjFlags(0x8, 0x1000)
    OP_71(0x8, 0x1, 0x78, 0x0, 0x20)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x0, 0x9)
    OP_49()
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_71(0x0, 0x1, 0x78, 0x0, 0x20)
    Call(0, 3)
    OP_F3(100000)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1K#30W翌日、９：００──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    PlayEffect(0x0, 0x2, 0x9, 0x5, -2120, 880, -5120, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0x9, 0x5, 2120, 880, -5120, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x9, 0, 0, -100000, 0)

    def lambda_18D9():
        OP_9B(0x1, 0xFE, 0x0, 0x61A80, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_18D9)
    OP_FF(0x0, 0x1F4, 0x1F4, 0x1F4)
    BlurSwitch(0x0, 0x55FFFFFF, 0x0, 0x1, 0x0)
    OP_68(0, 1500, 0, 0)
    MoveCamera(190, 10, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(30000, 0)
    MoveCamera(340, 10, 0, 8500)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(132, 2, 100, 0)
    BeginChrThread(0x12, 1, 0, 20)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4000)
    StopSound(497, 3000, 65)
    OP_6F(0x79)
    Fade(500)
    BeginChrThread(0x12, 1, 0, 21)
    PlayEffect(0x0, 0x2, 0x9, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0x9, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    EndChrThread(0x9, 0x1)
    SetChrPos(0x9, 0, 0, 0, 0)
    OP_FF(0x0, 0x3E8, 0x3E8, 0x3E8)
    OP_68(0, 1500, 3000, 0)
    MoveCamera(150, 30, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(35000, 0)
    OP_68(0, 1500, 3000, 6000)
    MoveCamera(125, 15, 0, 6000)
    OP_6E(800, 6000)
    SetCameraDistance(30000, 6000)
    OP_6F(0x79)
    Fade(500)
    BeginChrThread(0x12, 1, 0, 19)
    PlayEffect(0x0, 0x2, 0x9, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0x9, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x8, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearMapObjFlags(0x8, 0x4)
    SetChrPos(0x8, -48500, 0, -121000, 0)
    OP_D5(0x8, 0x0, 0x7530, 0x0, 0x0)
    SetChrPos(0x9, 7500, 0, -100000, 0)
    BeginChrThread(0x8, 1, 0, 15)
    BeginChrThread(0x9, 1, 0, 17)
    OP_68(0, 1500, -60000, 0)
    MoveCamera(240, 40, 5, 0)
    OP_6E(800, 0)
    SetCameraDistance(90000, 0)
    OP_68(0, 1500, 0, 10000)
    MoveCamera(220, 35, 5, 10000)
    SetCameraDistance(60000, 10000)
    Sleep(7000)
    Fade(500)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    PlayEffect(0x0, 0x2, 0x9, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0x9, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x0, 0x8, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x8, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x8, -7500, 0, -50000, 0)
    OP_D5(0x8, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x9, 7500, 0, 0, 0)
    OP_D5(0x9, 0x0, 0x0, 0x0, 0x0)
    OP_68(0, 1500, 0, 0)
    MoveCamera(280, 15, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(30000, 0)
    OP_68(0, 1500, 3000, 6000)
    MoveCamera(240, 20, 0, 6000)
    OP_6E(800, 6000)
    SetCameraDistance(45000, 6000)
    OP_96(0x8, 0xFFFFE2B4, 0x0, 0x0, 0x3A98, 0x0)
    OP_96(0x8, 0xFFFFE2B4, 0x0, 0x9C4, 0x1D4C, 0x0)
    OP_96(0x8, 0xFFFFE2B4, 0x0, 0x1388, 0x9C4, 0x0)
    Sleep(1000)
    PlayEffect(0x1, 0xFF, 0x8, 0x5, 0, 6000, 1000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x8, 0x5, 0, 6000, 1000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    PlayEffect(0x1, 0xFF, 0x8, 0x5, 0, 6000, 1000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    PlayEffect(0x1, 0xFF, 0x9, 0x5, 0, 6000, 1000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    PlayEffect(0x1, 0xFF, 0x9, 0x5, 0, 6000, 1000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    PlayEffect(0x1, 0xFF, 0x9, 0x5, 0, 6000, 1000, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(2000)
    OP_68(0, 1500, 50000, 4000)
    MoveCamera(235, 0, 0, 4000)
    OP_6E(800, 4000)
    SetCameraDistance(56450, 4000)
    PlayEffect(0x0, 0x0, 0x8, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x8, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x8, 1, 0, 16)
    Sleep(1000)
    PlayEffect(0x0, 0x2, 0x9, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0x9, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x9, 1, 0, 18)
    Sleep(1000)
    StopSound(496, 1500, 40)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    StopSound(132, 1000, 100)
    StopSound(497, 1000, 70)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    SetScenarioFlags(0x22, 0)
    NewScene("r2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_14_178F end

    def Function_15_2062(): pass

    label("Function_15_2062")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -47500, 0, -120000)
    OP_9F(0x1, -37500, 0, -100000)
    OP_9F(0x1, -15500, 0, -60000)
    OP_9F(0x1, -9000, 0, -40000)
    OP_9F(0x1, -8000, 0, -30000)
    OP_9F(0x1, -7500, 0, 0)
    OP_9F(0x2, 0xFE, 13000, 0x6)
    Return()

    # Function_15_2062 end

    def Function_16_20C4(): pass

    label("Function_16_20C4")

    OP_9B(0x1, 0xFE, 0x0, 0x2710, 0x2710, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x186A0, 0x9C40, 0x0)
    Return()

    # Function_16_20C4 end

    def Function_17_20E3(): pass

    label("Function_17_20E3")

    OP_96(0xFE, 0x1D4C, 0x0, 0xFFFFEC78, 0x32C8, 0x0)
    PlayEffect(0x0, 0x2, 0x9, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0x9, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    OP_96(0xFE, 0x1D4C, 0x0, 0xFFFFF63C, 0x1D4C, 0x0)
    OP_96(0xFE, 0x1D4C, 0x0, 0x0, 0x9C4, 0x0)
    Return()

    # Function_17_20E3 end

    def Function_18_218E(): pass

    label("Function_18_218E")

    OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0x2710, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0x3A98, 0x0)
    OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x4E20, 0x0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 7500, 0, 20000)
    OP_9F(0x1, 20000, 0, 45000)
    OP_9F(0x1, 50000, 0, 65000)
    OP_9F(0x2, 0xFE, 40000, 0x6)
    Return()

    # Function_18_218E end

    def Function_19_21F3(): pass

    label("Function_19_21F3")

    Sound(496, 2, 0, 0)
    Sleep(100)
    OP_25(0x1F0, 0x5)
    Sleep(200)
    OP_25(0x1F0, 0xA)
    Sleep(200)
    OP_25(0x1F0, 0xF)
    Sleep(200)
    OP_25(0x1F0, 0x14)
    Sleep(200)
    OP_25(0x1F0, 0x19)
    Sleep(200)
    OP_25(0x1F0, 0x1E)
    Sleep(200)
    OP_25(0x1F0, 0x23)
    Sleep(200)
    OP_25(0x1F0, 0x28)
    Sleep(200)
    OP_25(0x1F0, 0x2D)
    Sleep(200)
    OP_25(0x1F0, 0x32)
    Return()

    # Function_19_21F3 end

    def Function_20_2240(): pass

    label("Function_20_2240")

    Sound(497, 2, 0, 0)
    Sleep(200)
    OP_25(0x1F1, 0x5)
    Sleep(200)
    OP_25(0x1F1, 0xA)
    Sleep(200)
    OP_25(0x1F1, 0xF)
    Sleep(200)
    OP_25(0x1F1, 0x14)
    Sleep(200)
    OP_25(0x1F1, 0x19)
    Sleep(200)
    OP_25(0x1F1, 0x1E)
    Sleep(200)
    OP_25(0x1F1, 0x23)
    Sleep(200)
    OP_25(0x1F1, 0x28)
    Sleep(200)
    OP_25(0x1F1, 0x2D)
    Sleep(200)
    OP_25(0x1F1, 0x32)
    Sleep(200)
    OP_25(0x1F1, 0x37)
    Sleep(200)
    OP_25(0x1F1, 0x3C)
    Sleep(200)
    OP_25(0x1F1, 0x41)
    Sleep(200)
    OP_25(0x1F1, 0x46)
    Return()

    # Function_20_2240 end

    def Function_21_22A9(): pass

    label("Function_21_22A9")

    Sound(497, 2, 40, 0)
    Sleep(200)
    OP_25(0x1F1, 0x2D)
    Sleep(200)
    OP_25(0x1F1, 0x32)
    Sleep(200)
    OP_25(0x1F1, 0x37)
    Sleep(200)
    OP_25(0x1F1, 0x3C)
    Sleep(200)
    OP_25(0x1F1, 0x41)
    Sleep(200)
    OP_25(0x1F1, 0x46)
    Return()

    # Function_21_22A9 end

    def Function_22_22DA(): pass

    label("Function_22_22DA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_F3(200000)
    LoadEffect(0x0, "event/eva03_01.eff")
    LoadEffect(0x1, "event/ev15056.eff")
    LoadEffect(0x2, "event/ev15057.eff")
    LoadEffect(0x3, "event/ev17086.eff")
    LoadEffect(0x4, "event/ev10017.eff")
    LoadEffect(0x5, "event/ev10009.eff")
    LoadEffect(0x6, "event/ev17102.eff")
    LoadEffect(0x7, "event/ev17022.eff")
    LoadEffect(0x8, "event/ev17019.eff")
    LoadEffect(0x9, "event/ev17106.eff")
    LoadEffect(0xA, "event/ev17030.eff")
    SoundLoad(132)
    SoundLoad(497)
    SoundLoad(825)
    SoundLoad(868)
    SoundLoad(980)
    ClearChrFlags(0x8, 0x80)
    OP_78(0xA, 0x8)
    OP_49()
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    OP_71(0xA, 0x1, 0x78, 0x0, 0x20)
    OP_74(0xA, 0x1E)
    PlayEffect(0x6, 0x6, 0x8, 0x5, 3500, 1000, 5000, 0, 0, 0, 1000, 1200, 1000, 0xFF, 0, 0, 0, 500)
    PlayEffect(0x6, 0x7, 0x8, 0x5, -5500, 1000, -4500, 0, 0, 0, 1000, 1200, 1000, 0xFF, 0, 0, 0, 500)
    PlayEffect(0x3, 0xFF, 0x8, 0x5, 0, 0, -12630, 0, 0, 0, 1200, 1200, 4400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x8, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0xFF, 0x8, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 2000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0xF, 0x80)
    OP_78(0x7, 0xF)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    OP_74(0x7, 0x1E)
    OP_70(0x7, 0x6F)
    OP_87(0x7, 0xFF, 0x7, "Null_wing_r0 (66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x7, "Null_wing_r1(67)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x7, "Null_wing_r2(68)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x7, "Null_wing_l0(69)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x7, "Null_wing_l1(70)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x7, "Null_wing_l2(71)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    Call(0, 3)
    PlayBGM("ed7543", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x21F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(132, 2, 100, 0)
    Sound(497, 2, 70, 0)
    Sound(868, 2, 30, 0)
    OP_25(0x364, 0x1E)
    Sound(825, 2, 50, 0)
    SetChrPos(0x8, 0, 0, 40000, 0)
    OP_93(0x8, 0x0, 0x0)
    SetChrPos(0xF, 0, 0, -120000, 0)
    OP_93(0xF, 0x0, 0x0)
    PlayEffect(0x6, 0x6, 0x8, 0x5, 3500, 1000, 5000, 0, 0, 0, 1000, 1200, 1000, 0xFF, 0, 0, 0, 500)
    PlayEffect(0x6, 0x7, 0x8, 0x5, -5500, 1000, -4500, 0, 0, 0, 1000, 1200, 1000, 0xFF, 0, 0, 0, 500)
    OP_68(-3530, 2600, 69480, 0)
    MoveCamera(138, 48, -14, 0)
    OP_6E(800, 0)
    SetCameraDistance(100000, 0)
    Fade(500)
    PlayEffect(0x0, 0x0, 0x8, 0x1, 0, 0, 0, 0, 180, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    OP_68(-2360, 2600, 24440, 3000)
    MoveCamera(133, 55, 0, 3000)
    SetCameraDistance(75000, 3000)
    Sleep(2800)
    OP_68(-4010, 2600, 61850, 0)
    MoveCamera(116, 12, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13770, 0)
    Fade(500)
    BlurSwitch(0x3E8, 0x55FFFFFF, 0x0, 0x1, 0xA)
    OP_25(0x1F1, 0x64)
    OP_68(-7540, 2600, 30020, 2700)
    MoveCamera(96, 5, 0, 2700)
    OP_6E(800, 2700)
    SetCameraDistance(13770, 2700)
    Sleep(1700)
    BeginChrThread(0xF, 3, 0, 23)
    Sleep(800)
    OP_68(-4280, 4400, 6070, 2500)
    MoveCamera(44, 12, 0, 2500)
    OP_6E(800, 2500)
    SetCameraDistance(54580, 2500)
    OP_6F(0x79)
    SetChrPos(0x8, 0, 0, 40000, 0)
    OP_93(0x8, 0x0, 0x0)
    SetChrPos(0xF, 0, 0, -40000, 0)
    OP_93(0xF, 0x0, 0x0)
    Sound(980, 2, 50, 0)
    OP_68(0, 1600, 31820, 0)
    MoveCamera(182, 12, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(48420, 0)
    Fade(500)
    OP_0D()
    Sound(1036, 0, 70, 0)
    OP_87(0x1, 0xFF, 0x7, "Null_bp_cannon(64)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_68(-380, 1600, 31820, 700)
    MoveCamera(193, 15, 0, 700)
    OP_6E(800, 700)
    SetCameraDistance(64879, 700)
    OP_6F(0x79)
    BeginChrThread(0xF, 3, 0, 24)
    OP_68(-380, 1600, 31820, 1200)
    MoveCamera(166, 16, 0, 1200)
    OP_6E(800, 1200)
    SetCameraDistance(64879, 1200)
    OP_6F(0x79)
    CancelBlur(500)
    OP_68(-380, 1600, 31820, 1700)
    MoveCamera(176, 14, 0, 1700)
    OP_6E(800, 1700)
    SetCameraDistance(49960, 1700)
    OP_6F(0x79)
    Sleep(700)
    ClearMapObjFlags(0xA, 0x1000)
    SetChrPos(0x8, 0, 0, 80000, 0)
    OP_93(0x8, 0x0, 0x0)
    SetChrPos(0xF, 0, 0, 0, 0)
    OP_93(0xF, 0x0, 0x0)
    OP_68(0, 1600, 4400, 0)
    MoveCamera(186, 39, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(34890, 0)
    Fade(500)
    Sound(999, 0, 100, 0)
    Sound(499, 0, 100, 0)
    OP_25(0x3D4, 0x64)
    OP_68(0, 5900, -8500, 1500)
    MoveCamera(180, -8, 0, 1500)
    OP_6E(800, 1500)
    SetCameraDistance(21660, 1500)
    OP_0D()
    PlayEffect(0x4, 0x2, 0xF, 0x5, 0, 3000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(655, 0, 50, 0)
    OP_87(0xA, 0xFF, 0x7, "ch88650head:Layer1(11)", 0x7, 0xFFFFFFCE, 0x32, 0xC8, 0x0, 0x0, 0x0, 0x47E, 0x47E, 0x47E, 0x0)
    OP_6F(0x79)
    Sound(1036, 0, 100, 0)
    OP_87(0x1, 0x1, 0x7, "Null_bp_cannon(64)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    BlurSwitch(0x1F4, 0x77FFFFFF, 0x0, 0x1, 0xA)
    Sleep(700)
    StopEffect(0x2, 0x2)
    CancelBlur(500)
    SetChrPos(0x8, 0, -5000, 70000, 0)
    OP_93(0x8, 0x0, 0x0)
    OP_25(0x3D4, 0x32)
    OP_68(0, 3600, 64500, 1100)
    MoveCamera(181, 14, 0, 1100)
    OP_6E(800, 1100)
    SetCameraDistance(45000, 1100)
    StopEffect(0x6, 0x2)
    StopEffect(0x7, 0x2)
    Sleep(300)
    Sound(655, 0, 50, 0)
    BeginChrThread(0x8, 3, 0, 25)
    WaitChrThread(0x8, 3)
    OP_6F(0x79)
    PlayEffect(0x9, 0x6, 0x8, 0x5, 3500, 1000, 5000, 0, 0, 0, 1000, 1200, 1000, 0xFF, 0, 0, 0, 500)
    PlayEffect(0x9, 0x7, 0x8, 0x5, -5500, 1000, -4500, 0, 0, 0, 1000, 1200, 1000, 0xFF, 0, 0, 0, 500)
    OP_82(0x1F4, 0xC8, 0xBB8, 0x5DC)
    Sleep(1500)
    OP_82(0xC8, 0x1F4, 0xBB8, 0x5DC)
    Sleep(1500)
    OP_82(0x1F4, 0xC8, 0xBB8, 0x5DC)
    Sleep(1500)
    OP_82(0xC8, 0xC8, 0xBB8, 0x5DC)
    Sleep(300)
    OP_68(140, -5100, 72160, 0)
    MoveCamera(156, 34, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(33040, 0)
    Fade(500)
    BlurSwitch(0x0, 0x55FFFFFF, 0x0, 0x1, 0xA)
    Sleep(1300)
    CancelBlur(500)
    StopEffect(0x1, 0x0)
    SetChrPos(0x8, 0, 0, 60000, 0)
    OP_93(0x8, 0x0, 0x0)
    SetChrPos(0xF, 0, 20000, -20000, 0)
    OP_D5(0xF, 0x7530, 0x0, 0x0, 0x0)
    OP_68(480, 3400, 32880, 0)
    MoveCamera(43, 23, 13, 0)
    OP_6E(800, 0)
    SetCameraDistance(120220, 0)
    Fade(500)
    BlurSwitch(0x3E8, 0x55FFFFFF, 0x0, 0x1, 0xA)
    BeginChrThread(0x12, 1, 0, 26)
    BeginChrThread(0x12, 2, 0, 27)
    OP_25(0x1F1, 0x32)
    OP_68(0, 3400, 21500, 4000)
    MoveCamera(39, 23, 10, 4000)
    OP_6E(800, 4000)
    SetCameraDistance(130000, 4000)
    Sleep(3000)
    StopSound(497, 1000, 50)
    StopSound(132, 1000, 90)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 5)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_22_22DA end

    def Function_23_2DA1(): pass

    label("Function_23_2DA1")

    PlayEffect(0x8, 0xFF, 0xFF, 0x0, -5000, 22000, -40000, 0, 15, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Sound(1014, 0, 70, 0)
    PlayEffect(0x8, 0xFF, 0xFF, 0x0, -7000, 19000, -40000, 0, 15, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Sound(1014, 0, 70, 0)
    PlayEffect(0x8, 0xFF, 0xFF, 0x0, 5000, 25000, -40000, 0, 15, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Sound(1014, 0, 70, 0)
    PlayEffect(0x8, 0xFF, 0xFF, 0x0, -7000, 21000, -40000, 0, 15, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Sound(1014, 0, 70, 0)
    PlayEffect(0x8, 0xFF, 0xFF, 0x0, -5000, 17000, -40000, 0, 15, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Sound(1014, 0, 70, 0)
    PlayEffect(0x8, 0xFF, 0xFF, 0x0, 5000, 21000, -40000, 0, 15, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Sound(1014, 0, 70, 0)
    Return()

    # Function_23_2DA1 end

    def Function_24_2F22(): pass

    label("Function_24_2F22")

    PlayEffect(0x8, 0xFF, 0xFF, 0x0, 5000, 29000, -40000, 0, 25, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Sound(1014, 0, 70, 0)
    PlayEffect(0x8, 0xFF, 0xFF, 0x0, -7000, 31000, -40000, 2, 25, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Sound(1014, 0, 70, 0)
    PlayEffect(0x8, 0xFF, 0xFF, 0x0, 6000, 28000, -40000, 4, 25, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Sound(1014, 0, 70, 0)
    PlayEffect(0x8, 0xFF, 0xFF, 0x0, -5000, 25000, -40000, 6, 25, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Sound(1014, 0, 70, 0)
    PlayEffect(0x8, 0xFF, 0xFF, 0x0, -6000, 32000, -40000, 8, 25, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Sound(1014, 0, 70, 0)
    PlayEffect(0x8, 0xFF, 0xFF, 0x0, 4000, 33000, -40000, 5, 75, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Sound(1014, 0, 70, 0)
    Return()

    # Function_24_2F22 end

    def Function_25_30A3(): pass

    label("Function_25_30A3")

    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 1000, 3000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(1014, 0, 70, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x5, -3000, 3000, -2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(1014, 0, 70, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x5, -2000, 3000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(1014, 0, 70, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 3000, 3000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(200, 0, 100, 0)
    OP_25(0x364, 0x50)
    OP_25(0x339, 0x64)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 1000, 3000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(1014, 0, 70, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x5, 2000, 3000, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, -3000, 3000, -2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(1014, 0, 70, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x5, -1000, 3000, -3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(196, 0, 100, 0)
    Sound(833, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, -2000, 3000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(1014, 0, 70, 0)
    Sound(556, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 3000, 3000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(200, 0, 100, 0)
    Sound(833, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, 2000, 3000, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x5, 0xFF, 0xFE, 0x5, -1000, 3000, -3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_25_30A3 end

    def Function_26_33A0(): pass

    label("Function_26_33A0")

    Sleep(1000)
    OP_25(0x3D4, 0x2D)
    Sleep(350)
    OP_25(0x3D4, 0x28)
    Sleep(350)
    OP_25(0x3D4, 0x23)
    Sleep(350)
    OP_25(0x3D4, 0x1E)
    Sleep(350)
    OP_25(0x3D4, 0x19)
    Sleep(350)
    OP_25(0x3D4, 0x14)
    Sleep(350)
    OP_25(0x3D4, 0xF)
    Sleep(350)
    OP_25(0x3D4, 0xA)
    Sleep(350)
    OP_25(0x3D4, 0x5)
    Sleep(350)
    OP_25(0x3D4, 0x0)
    Return()

    # Function_26_33A0 end

    def Function_27_33E7(): pass

    label("Function_27_33E7")

    Sleep(2500)
    OP_25(0x364, 0x46)
    OP_25(0x339, 0x5A)
    Sleep(100)
    OP_25(0x364, 0x41)
    OP_25(0x339, 0x55)
    Sleep(100)
    OP_25(0x364, 0x3C)
    OP_25(0x339, 0x46)
    Sleep(100)
    OP_25(0x364, 0x37)
    OP_25(0x339, 0x41)
    Sleep(100)
    OP_25(0x364, 0x32)
    OP_25(0x339, 0x3C)
    Sleep(100)
    OP_25(0x364, 0x2D)
    OP_25(0x339, 0x37)
    Sleep(100)
    OP_25(0x364, 0x28)
    OP_25(0x339, 0x32)
    Sleep(100)
    OP_25(0x364, 0x23)
    OP_25(0x339, 0x2D)
    Sleep(100)
    OP_25(0x364, 0x1E)
    OP_25(0x339, 0x28)
    Sleep(100)
    OP_25(0x364, 0x19)
    OP_25(0x339, 0x23)
    Sleep(100)
    OP_25(0x364, 0x14)
    OP_25(0x339, 0x1E)
    Sleep(100)
    OP_25(0x364, 0xF)
    OP_25(0x339, 0x19)
    Sleep(100)
    OP_25(0x364, 0xA)
    OP_25(0x339, 0x14)
    Sleep(100)
    OP_25(0x364, 0x5)
    OP_25(0x339, 0xF)
    Sleep(100)
    OP_25(0x364, 0x0)
    OP_25(0x339, 0xA)
    Sleep(100)
    OP_25(0x339, 0x5)
    Sleep(100)
    OP_25(0x339, 0x0)
    Return()

    # Function_27_33E7 end

    def Function_28_349B(): pass

    label("Function_28_349B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_F3(200000)
    LoadEffect(0x0, "event/ev17035.eff")
    LoadEffect(0x1, "event/ev17036.eff")
    LoadEffect(0x2, "event/eva03_01.eff")
    LoadEffect(0x3, "event/ev17037.eff")
    LoadEffect(0x4, "event/ev17044.eff")
    LoadEffect(0x5, "event/ev17086.eff")
    LoadEffect(0x6, "event/ev17106.eff")
    LoadEffect(0x7, "event/ev17022.eff")
    LoadEffect(0x8, "event/eva03_01.eff")
    LoadEffect(0xA, "event/ev17047.eff")
    SoundLoad(132)
    SoundLoad(496)
    SoundLoad(497)
    SoundLoad(980)
    SoundLoad(931)
    ClearChrFlags(0x8, 0x80)
    OP_78(0xA, 0x8)
    OP_49()
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    OP_71(0xA, 0x1, 0x78, 0x0, 0x20)
    OP_74(0xA, 0x1E)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 0, -45540, -26370, 0, -73, 0, 1200, 1200, 2400, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, -4250, -42636, -26200, 0, -73, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 4250, -42636, -26200, 0, -73, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0xF, 0x80)
    OP_78(0x7, 0xF)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    OP_74(0x7, 0x1E)
    OP_70(0x7, 0x3D)
    OP_87(0x7, 0xFF, 0x7, "Null_wing_r0 (66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x7, "Null_wing_r1(67)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x7, "Null_wing_r2(68)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x7, "Null_wing_l0(69)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x7, "Null_wing_l1(70)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x7, "Null_wing_l2(71)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    Call(0, 3)
    SetChrPos(0x8, 0, -34641, 20000, 0)
    OP_D5(0x8, 0xFFFF15A0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0xF, 0, 34641, -20000, 0)
    OP_D5(0xF, 0xEA60, 0x0, 0x0, 0x0)
    OP_68(0, 37500, -16500, 0)
    MoveCamera(113, -19, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(28710, 0)
    BlurSwitch(0x0, 0x55FFFFFF, 0x0, 0x1, 0xA)
    Sound(132, 2, 100, 0)
    Sound(980, 2, 100, 0)
    PlayEffect(0xA, 0x6, 0xFF, 0x0, 0, 85282, -50000, 0, 0, 0, 16000, 16000, 16000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8, 0x5, 0xFF, 0x0, 0, 34641, -20000, 180, -60, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_68(0, 37500, -16500, 2000)
    MoveCamera(156, -30, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(14660, 2000)
    OP_0D()
    OP_6F(0x79)
    OP_7D(0x96, 0x96, 0x96, 0x0, 0x7D0)
    Sound(982, 0, 100, 0)
    BeginChrThread(0xF, 0, 0, 29)
    OP_68(0, 34900, -16500, 1000)
    MoveCamera(174, -52, 0, 1000)
    OP_6E(800, 1000)
    SetCameraDistance(10080, 1000)
    OP_6F(0x79)
    WaitChrThread(0xF, 0)
    Sound(983, 0, 80, 0)
    Sound(931, 2, 60, 0)
    Sound(825, 2, 100, 0)
    OP_87(0x4, 0x4, 0x7, "Null_bp_cannon(64)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x7D0, 0x7D0, 0x0)
    OP_68(0, 34900, -16500, 3000)
    MoveCamera(171, -49, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(10080, 3000)
    Sleep(500)
    BlurSwitch(0x3E8, 0x77FFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(2500)
    Sound(919, 0, 70, 0)
    OP_6F(0x79)
    StopSound(980, 2000, 90)
    StopSound(931, 2000, 50)
    StopEffect(0x5, 0x0)
    StopEffect(0x6, 0x0)
    SetChrPos(0x8, 0, -34641, -20000, 0)
    OP_D5(0x8, 0xFFFF15A0, 0x0, 0x0, 0x0)
    SetChrPos(0xF, 0, 34641, 20000, 0)
    OP_D5(0xF, 0xEA60, 0x2BF20, 0x0, 0x0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    PlayEffect(0x6, 0x2, 0xFF, 0x0, 3170, -28340, -18300, 0, -80, 0, 1000, 1200, 1000, 0xFF, 0, 0, 0, 500)
    PlayEffect(0x6, 0x3, 0xFF, 0x0, -5930, -38840, -24290, 0, -80, 60, 1000, 1200, 1000, 0xFF, 0, 0, 0, 500)
    PlayEffect(0x8, 0x5, 0xFF, 0x0, 0, -34641, -20000, 180, 60, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    Sound(497, 2, 100, 0)
    Sound(496, 2, 100, 0)
    OP_68(0, -33340, -20000, 0)
    MoveCamera(285, 12, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(58280, 0)
    Fade(500)
    OP_68(0, -33340, -20000, 2000)
    MoveCamera(214, 60, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(40390, 2000)
    OP_6F(0x79)
    Sound(1002, 0, 100, 0)
    OP_87(0x0, 0xFF, 0xA, "Null_can", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0xBB8, 0xBB8, 0xBB8, 0x0)
    OP_68(0, -33340, -20000, 3000)
    MoveCamera(214, 60, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(40540, 3000)
    Sleep(500)
    BlurSwitch(0x3E8, 0x77FFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(2500)
    Sound(930, 0, 100, 0)
    Sleep(300)
    OP_7D(0xA5, 0xA5, 0xA5, 0x0, 0x3E8)
    OP_6F(0x79)
    StopEffect(0x5, 0x0)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    SetMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    BlurSwitch(0x0, 0x55FFFFFF, 0x0, 0x1, 0xA)
    SetChrPos(0x8, 0, -34641, 20000, 0)
    OP_D5(0x8, 0xFFFF15A0, 0x2BF20, 0x0, 0x0)
    SetChrPos(0xF, 0, 34641, -20000, 0)
    OP_D5(0xF, 0xEA60, 0x0, 0x0, 0x0)
    OP_68(0, 34600, -16500, 0)
    MoveCamera(164, -50, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(7690, 0)
    OP_7D(0x96, 0x96, 0x96, 0x0, 0x0)
    Fade(500)
    StopSound(497, 2000, 100)
    StopSound(496, 2000, 100)
    PlayEffect(0xA, 0x6, 0xFF, 0x0, 0, 88282, -50000, 0, 0, 0, 13000, 13000, 13000, 0xFF, 0, 0, 0, 0)
    Sound(983, 0, 70, 0)
    Sound(931, 2, 70, 0)
    OP_87(0x3, 0x3, 0x7, "Null_bp_cannon(64)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x3E8)
    Sleep(500)
    StopEffect(0x6, 0x2)
    StopEffect(0x4, 0x2)
    Sleep(500)
    Sound(984, 0, 100, 0)
    Sound(833, 0, 80, 0)
    OP_82(0x32, 0x32, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0xA)
    OP_68(5860, 30800, -12600, 700)
    MoveCamera(149, -58, 0, 700)
    OP_6E(800, 700)
    SetCameraDistance(69500, 700)
    OP_6F(0x79)
    CancelBlur(500)
    Sleep(500)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetChrPos(0x8, 0, -34641, -20000, 0)
    OP_D5(0x8, 0xFFFF15A0, 0x0, 0x0, 0x0)
    SetChrPos(0xF, 0, 34641, 20000, 0)
    OP_D5(0xF, 0xEA60, 0x2BF20, 0x0, 0x0)
    OP_68(0, -33340, -20000, 0)
    MoveCamera(214, 60, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(40390, 0)
    OP_7D(0xAF, 0xAF, 0xAF, 0x0, 0x0)
    PlayEffect(0x6, 0x2, 0xFF, 0x0, 3170, -28340, -18300, 0, -80, 0, 1000, 1200, 1000, 0xFF, 0, 0, 0, 500)
    Fade(500)
    StopEffect(0x3, 0x0)
    Sleep(500)
    Sound(984, 0, 100, 0)
    Sound(833, 0, 80, 0)
    OP_25(0x3A3, 0x32)
    OP_87(0x1, 0x1, 0xA, "Null_can", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    Sleep(200)
    OP_82(0x32, 0x32, 0xBB8, 0xC8)
    BlurSwitch(0x0, 0x55FFFFFF, 0x0, 0x1, 0xA)
    OP_68(-10950, -31440, -6360, 700)
    MoveCamera(224, 67, 0, 700)
    OP_6E(800, 700)
    SetCameraDistance(101540, 700)
    OP_6F(0x79)
    Sleep(500)
    CancelBlur(500)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    SetChrPos(0x8, 0, -69282, -40000, 0)
    OP_D5(0x8, 0xFFFF15A0, 0x0, 0x0, 0x0)
    SetChrPos(0xF, 6000, 69282, 48000, 0)
    OP_D5(0xF, 0xEA60, 0x2BF20, 0x0, 0x0)
    OP_68(-22130, 5000, -9110, 0)
    MoveCamera(240, -32, -44, 0)
    OP_6E(800, 0)
    SetCameraDistance(247140, 0)
    SetCameraDistance(270140, 5000)
    BlurSwitch(0x0, 0x55FFFFFF, 0x0, 0x1, 0xA)
    OP_7D(0xD7, 0xD7, 0xD7, 0x0, 0x0)
    StopEffect(0x2, 0x0)
    PlayEffect(0x6, 0x2, 0xFF, 0x0, 3170, -62981, -38300, 0, -80, 0, 1000, 1200, 1000, 0xFF, 0, 0, 0, 500)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, -5930, -73481, -44290, 0, -80, 60, 1000, 1200, 1000, 0xFF, 0, 0, 0, 500)
    StopEffect(0x3, 0x0)
    PlayEffect(0x3, 0x3, 0xFF, 0x0, 0, 69282, 40000, 180, 60, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Fade(500)
    BeginChrThread(0x8, 0, 0, 30)
    Sleep(1500)
    OP_7D(0xB9, 0xB9, 0xB9, 0x0, 0x5DC)
    Sleep(1500)
    Sound(833, 0, 100, 0)
    StopSound(931, 3000, 40)
    StopSound(132, 3000, 100)
    BeginChrThread(0x12, 1, 0, 31)
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    Sleep(2000)
    SetScenarioFlags(0x22, 0)
    NewScene("e4212", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_28_349B end

    def Function_29_407B(): pass

    label("Function_29_407B")

    OP_74(0x7, 0xF)
    OP_71(0x7, 0xC9, 0xDC, 0x0, 0x0)
    OP_79(0x7)
    OP_71(0x7, 0xDD, 0xF0, 0x1, 0x0)
    OP_79(0x7)
    Return()

    # Function_29_407B end

    def Function_30_409E(): pass

    label("Function_30_409E")

    OP_82(0xC8, 0xC8, 0xBB8, 0x5DC)
    Sleep(500)
    OP_82(0x12C, 0x12C, 0xBB8, 0x5DC)
    Sleep(500)
    OP_82(0x190, 0x190, 0xBB8, 0x5DC)
    Sleep(500)
    Return()

    # Function_30_409E end

    def Function_31_40DB(): pass

    label("Function_31_40DB")

    OP_25(0x339, 0x5F)
    Sleep(100)
    OP_25(0x339, 0x5A)
    Sleep(100)
    OP_25(0x339, 0x55)
    Sleep(100)
    OP_25(0x339, 0x50)
    Sleep(100)
    Sound(200, 0, 100, 0)
    OP_25(0x339, 0x4B)
    Sleep(100)
    OP_25(0x339, 0x46)
    Sleep(100)
    OP_25(0x339, 0x41)
    Sleep(100)
    OP_25(0x339, 0x3C)
    Sleep(100)
    OP_25(0x339, 0x37)
    Sleep(100)
    OP_25(0x339, 0x32)
    Sleep(100)
    OP_25(0x339, 0x2D)
    Sleep(100)
    OP_25(0x339, 0x28)
    Sleep(100)
    OP_25(0x339, 0x23)
    Sleep(100)
    OP_25(0x339, 0x1E)
    Sleep(100)
    OP_25(0x339, 0x19)
    Sleep(100)
    OP_25(0x339, 0x14)
    Sleep(100)
    OP_25(0x339, 0xF)
    Sleep(100)
    OP_25(0x339, 0xA)
    Sleep(100)
    OP_25(0x339, 0x5)
    Sleep(100)
    OP_25(0x339, 0x0)
    Return()

    # Function_31_40DB end

    def Function_32_416B(): pass

    label("Function_32_416B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev17086.eff")
    SoundLoad(132)
    SoundLoad(497)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x0, 0x9)
    OP_49()
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x1000)
    OP_71(0x0, 0x1, 0x78, 0x0, 0x20)
    Call(0, 3)
    OP_7D(0xD7, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 0, 0, 0, 0)
    OP_68(0, 1500, 3000, 0)
    MoveCamera(150, 30, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(35000, 0)
    OP_68(0, 1500, 3000, 6000)
    MoveCamera(125, 15, 0, 6000)
    OP_6E(800, 6000)
    SetCameraDistance(30000, 6000)
    Sound(132, 2, 100, 0)
    Sound(497, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x9, 0x5, -4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x9, 0x5, 4250, 1750, -10250, 0, 0, 0, 1000, 1000, 250, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4000)
    StopSound(132, 1000, 100)
    StopSound(497, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 6)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_32_416B end

    def Function_33_42D7(): pass

    label("Function_33_42D7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Call(0, 3)
    LoadEffect(0x0, "event/ev15055.eff")
    LoadEffect(0x1, "event/ev15076.eff")
    LoadEffect(0x2, "event/ev10009.eff")
    LoadEffect(0x3, "event/ev15075.eff")
    LoadEffect(0x4, "event/ev10013.eff")
    LoadEffect(0x5, "event/ev17095.eff")
    LoadEffect(0x6, "battle/btgun00.eff")
    LoadEffect(0x7, "event/ev17022.eff")
    LoadEffect(0x8, "event/ev15070.eff")
    LoadEffect(0x9, "event/eva03_01.eff")
    SoundLoad(132)
    SoundLoad(497)
    SoundLoad(980)
    OP_F0(0x0, 0x4)
    OP_F3(200000)
    ClearChrFlags(0xF, 0x80)
    OP_74(0x7, 0x1E)
    ClearMapObjFlags(0x7, 0x4)
    OP_78(0x7, 0xF)
    SetChrPos(0xF, 0, 0, 0, 0)
    OP_93(0xF, 0xB4, 0x0)
    OP_87(0x7, 0xFF, 0x7, "Null_wing_r0 (66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x7, "Null_wing_r1(67)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x7, "Null_wing_r2(68)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x7, "Null_wing_l0(69)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x7, "Null_wing_l1(70)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x7, "Null_wing_l2(71)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    ClearChrFlags(0xA, 0x80)
    OP_74(0x2, 0x1E)
    ClearMapObjFlags(0x2, 0x4)
    OP_78(0x2, 0xA)
    SetChrPos(0xA, 0, 0, 0, 0)
    OP_93(0xA, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    OP_74(0x3, 0x1E)
    ClearMapObjFlags(0x3, 0x4)
    OP_78(0x3, 0xB)
    SetChrPos(0xB, 0, 0, 0, 0)
    OP_93(0xB, 0x0, 0x0)
    ClearChrFlags(0xC, 0x80)
    OP_74(0x4, 0x1E)
    ClearMapObjFlags(0x4, 0x4)
    OP_78(0x4, 0xC)
    SetChrPos(0xC, 0, 0, 0, 0)
    OP_93(0xC, 0x0, 0x0)
    ClearChrFlags(0xD, 0x80)
    OP_74(0x5, 0x1E)
    ClearMapObjFlags(0x5, 0x4)
    OP_78(0x5, 0xD)
    SetChrPos(0xD, 0, 0, 0, 0)
    OP_93(0xD, 0x0, 0x0)
    ClearChrFlags(0xE, 0x80)
    OP_74(0x6, 0x1E)
    ClearMapObjFlags(0x6, 0x4)
    OP_78(0x6, 0xE)
    SetChrPos(0xE, 0, 0, 0, 0)
    OP_93(0xE, 0x0, 0x0)
    OP_74(0xB, 0x7)
    ClearMapObjFlags(0xB, 0x4)
    OP_74(0xC, 0x7)
    ClearMapObjFlags(0xC, 0x4)
    OP_74(0xD, 0x7)
    ClearMapObjFlags(0xD, 0x4)
    OP_74(0xE, 0x7)
    ClearMapObjFlags(0xE, 0x4)
    OP_74(0xF, 0x7)
    ClearMapObjFlags(0xF, 0x4)
    PlayEffect(0x8, 0x2, 0xA, 0x5, -6400, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8, 0x3, 0xA, 0x5, 6400, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8, 0x4, 0xB, 0x5, -6400, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8, 0x5, 0xB, 0x5, 6400, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8, 0x6, 0xC, 0x5, -6400, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8, 0x7, 0xC, 0x5, 6400, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0xF, 0, 10000, 400000, 180)
    SetChrPos(0xA, 0, -11000, 70000, 0)
    SetChrPos(0xB, 20000, -2000, 40000, 0)
    SetChrPos(0xC, -20000, 2000, 34000, 0)
    SetChrPos(0xD, 15000, 0, -70000, 0)
    SetChrPos(0xE, -15000, -5000, -90000, 0)
    BeginChrThread(0xA, 0, 0, 59)
    BeginChrThread(0xB, 0, 0, 59)
    BeginChrThread(0xC, 0, 0, 59)
    BeginChrThread(0xD, 0, 0, 59)
    BeginChrThread(0xE, 0, 0, 59)
    ClearMapObjFlags(0x7, 0x1000)
    OP_71(0x2, 0x3D, 0x78, 0x0, 0x20)
    OP_71(0x3, 0x3D, 0x78, 0x0, 0x20)
    OP_71(0x4, 0x3D, 0x78, 0x0, 0x20)
    OP_71(0x5, 0x3D, 0x78, 0x0, 0x20)
    OP_71(0x6, 0x3D, 0x78, 0x0, 0x20)
    Sound(132, 2, 100, 0)
    Sound(497, 2, 80, 0)
    FadeToBright(1000, 0)
    OP_68(4500, -10900, 20460, 0)
    MoveCamera(158, 13, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(126140, 0)
    MoveCamera(147, 3, 0, 4500)
    SetCameraDistance(121620, 4500)
    OP_0D()
    OP_6F(0x79)
    OP_71(0x7, 0x6F, 0x96, 0x0, 0x20)
    SetMapObjFlags(0x7, 0x1000)
    Fade(500)
    OP_68(810, 1500, 49990, 0)
    MoveCamera(63, -16, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(80280, 0)
    OP_68(440, 2200, 97540, 3000)
    MoveCamera(30, -10, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(134180, 3000)
    OP_0D()
    BeginChrThread(0xF, 0, 0, 39)
    WaitChrThread(0xF, 0)
    SetChrPos(0xF, 0, 0, 0, 0)
    OP_93(0xF, 0x0, 0x0)
    SetChrPos(0xA, 0, -1000000, 0, 0)
    SetChrPos(0xB, 0, -1000000, 0, 0)
    SetChrPos(0xC, 0, -1000000, 0, 0)
    SetChrPos(0xD, 0, -1000000, 0, 0)
    SetChrPos(0xE, 0, -1000000, 0, 0)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xB, 0x0)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xE, 0x0)
    StopSound(497, 1000, 70)
    Sound(980, 2, 80, 0)
    Fade(500)
    OP_68(0, 3100, 3000, 0)
    MoveCamera(207, 6, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(33500, 0)
    OP_68(0, 2900, -1250, 5000)
    SetCameraDistance(13000, 5000)
    MoveCamera(244, 18, 0, 2000)
    OP_0D()
    Sleep(1000)
    MoveCamera(225, -14, 0, 1500)
    Sleep(500)
    BeginChrThread(0xF, 3, 0, 40)
    Sleep(1000)
    OP_6F(0x79)
    WaitChrThread(0xF, 3)
    Sleep(600)
    Fade(300)
    OP_68(0, 2900, -950, 700)
    MoveCamera(200, 21, 0, 700)
    OP_6E(800, 700)
    SetCameraDistance(15230, 700)
    BeginChrThread(0xF, 3, 0, 41)
    OP_6F(0x79)
    OP_68(0, 2900, 100, 700)
    MoveCamera(199, 32, 0, 700)
    SetCameraDistance(11250, 700)
    WaitChrThread(0xF, 3)
    Sleep(700)
    Call(0, 35)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0x64, 0x64, 0x5DC, 0x1F4)
    SetCameraDistance(16000, 700)
    Sleep(100)
    CancelBlur(3000)
    OP_7D(0xC3, 0xC3, 0xC3, 0x0, 0x2BC)
    Sleep(900)
    OP_68(490, 2000, 2950, 2400)
    MoveCamera(305, 26, 0, 2400)
    OP_6E(800, 2400)
    SetCameraDistance(18720, 2400)
    Sleep(1000)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x7D0)
    Sleep(700)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0x320, 0x320, 0x5DC, 0x1F4)
    OP_25(0x3D4, 0x1E)
    Sound(998, 0, 100, 0)
    Sound(499, 0, 100, 0)
    BeginChrThread(0xF, 0, 0, 43)
    WaitChrThread(0xF, 0)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x2, 0x1000)
    SetMapObjFlags(0x3, 0x1000)
    SetMapObjFlags(0x4, 0x1000)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFlags(0xC, 0x1000)
    SetMapObjFlags(0xD, 0x1000)
    BeginChrThread(0xA, 0, 0, 59)
    BeginChrThread(0xB, 0, 0, 59)
    BeginChrThread(0xC, 0, 0, 59)
    BeginChrThread(0xD, 0, 0, 59)
    BeginChrThread(0xE, 0, 0, 59)
    SetChrPos(0xF, 0, 1000, -85000, 0)
    SetChrPos(0xA, 0, -4000, -24000, 0)
    SetChrPos(0xB, -15000, 2000, 9000, 0)
    SetChrPos(0xC, 15000, 6000, 26000, 0)
    SetChrPos(0xD, 0, -1000000, 0, 0)
    SetChrPos(0xE, 0, -1000000, 0, 0)
    OP_93(0xA, 0xB4, 0x0)
    OP_93(0xB, 0xB4, 0x0)
    OP_93(0xC, 0xB4, 0x0)
    EndChrThread(0xA, 0x0)
    EndChrThread(0xB, 0x0)
    EndChrThread(0xC, 0x0)
    OP_68(0, 4300, -57500, 0)
    MoveCamera(273, 2, 4, 0)
    OP_6E(800, 0)
    SetCameraDistance(36790, 0)
    OP_68(0, 9300, 42850, 2500)
    MoveCamera(291, 16, 4, 2500)
    OP_6E(800, 2500)
    SetCameraDistance(63100, 2500)
    BeginChrThread(0xF, 0, 0, 44)
    BeginChrThread(0xF, 1, 0, 45)
    BeginChrThread(0xF, 2, 0, 46)
    Sound(497, 2, 60, 0)
    Sound(998, 0, 100, 0)
    PlayEffect(0x9, 0x8, 0xFF, 0x0, 3880, 6800, -890, 0, 0, 0, 9000, 1000, 9000, 0xFF, 0, 0, 0, 0)
    Fade(500)
    OP_0D()
    Sleep(200)
    Sound(287, 0, 80, 0)
    CancelBlur(500)
    Sleep(1100)
    WaitChrThread(0xF, 0)
    OP_6F(0x79)
    EndChrThread(0xF, 0x0)
    EndChrThread(0xF, 0x1)
    Fade(500)
    StopEffect(0x8, 0x0)
    OP_82(0x1F4, 0x1F4, 0x1388, 0x7D0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1E)
    SetChrPos(0xF, 0, 0, 25000, 0)
    OP_68(0, 4600, 32000, 0)
    MoveCamera(180, -9, 4, 0)
    OP_6E(800, 0)
    SetCameraDistance(91910, 0)
    OP_68(0, 4600, 40870, 5000)
    MoveCamera(177, -26, 4, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(111910, 5000)
    Sleep(1)
    CancelBlur(2000)
    OP_0D()
    Sound(999, 0, 100, 0)
    StopSound(980, 1000, 30)
    BeginChrThread(0xF, 0, 0, 47)
    BeginChrThread(0xF, 1, 0, 48)
    BeginChrThread(0x12, 1, 0, 60)
    Sleep(300)
    Call(0, 36)
    OP_6F(0x79)
    EndChrThread(0xF, 0x0)
    EndChrThread(0xF, 0x1)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFlags(0x6, 0x1000)
    EndChrThread(0xF, 0x0)
    EndChrThread(0xF, 0x1)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xE, 0x0)
    PlayEffect(0x8, 0x2, 0xD, 0x5, -6400, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8, 0x3, 0xD, 0x5, 6400, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8, 0x4, 0xE, 0x5, -6400, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8, 0x5, 0xE, 0x5, 6400, 1000, 250, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetMapObjFlags(0x7, 0x4)
    SetChrPos(0xF, -200810, -20000, -240990, 65478)
    SetChrPos(0xD, -36600, 10690, 1100, 19)
    SetChrPos(0xE, 32060, -10110, -1340, 16)
    OP_93(0xD, 0x13, 0x0)
    OP_93(0xE, 0x10, 0x0)
    Fade(500)
    OP_68(32310, -5900, 3530, 0)
    MoveCamera(267, -12, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(19810, 0)
    OP_82(0x32, 0x32, 0x1388, 0xBB8)
    Sound(865, 2, 80, 0)
    Sound(861, 2, 80, 0)
    BeginChrThread(0xD, 3, 0, 37)
    BeginChrThread(0xE, 3, 0, 38)
    MoveCamera(247, -11, 0, 2700)
    SetCameraDistance(17880, 2700)
    Sleep(800)

    def lambda_4FE1():
        OP_93(0xFE, 0x4F, 0x14)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_4FE1)
    OP_0D()
    Sleep(200)

    def lambda_4FF2():
        OP_93(0xFE, 0x2E, 0xA)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_4FF2)
    OP_6F(0x79)
    EndChrThread(0xD, 0x2)
    EndChrThread(0xE, 0x2)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    Sound(499, 0, 80, 0)
    Sound(998, 0, 100, 0)
    ClearMapObjFlags(0x7, 0x4)
    OP_70(0x7, 0xFC)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetChrPos(0xF, 50000, 0, 0, 180)
    BeginChrThread(0xF, 0, 0, 54)
    OP_93(0xD, 0x77, 0x0)
    OP_93(0xE, 0x56, 0x0)
    BeginChrThread(0xD, 0, 0, 59)
    BeginChrThread(0xE, 0, 0, 59)
    OP_68(0, 0, 0, 0)
    MoveCamera(131, -3, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16020, 0)
    Sound(980, 2, 50, 0)
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, 0, 0, 2700)
    MoveCamera(293, -9, 0, 2700)
    SetCameraDistance(76330, 3000)

    def lambda_50CE():

        label("loc_50CE")

        TurnDirection(0xFE, 0xF, 30)
        Yield()
        Jump("loc_50CE")

    QueueWorkItem2(0xD, 2, lambda_50CE)

    def lambda_50E0():

        label("loc_50E0")

        TurnDirection(0xFE, 0xF, 30)
        Yield()
        Jump("loc_50E0")

    QueueWorkItem2(0xE, 2, lambda_50E0)
    BeginChrThread(0xE, 3, 0, 34)
    OP_0D()
    CancelBlur(1000)
    Sleep(300)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0xE, 0x1000)
    SetMapObjFlags(0xF, 0x1000)
    Sleep(1000)
    WaitChrThread(0xF, 0)
    OP_6F(0x79)
    Call(0, 35)
    BeginChrThread(0xF, 0, 0, 55)
    BeginChrThread(0xF, 1, 0, 56)
    OP_68(36570, -10400, -4670, 2000)
    MoveCamera(304, -33, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(56510, 2000)
    Sound(999, 0, 50, 0)
    Sleep(630)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x5DC)
    Sound(287, 0, 70, 0)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xD, 0x2)
    Sound(200, 0, 90, 0)
    Sound(833, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xD, 0x0, 0, 3000, 0, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    EndChrThread(0xD, 0x2)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    OP_78(0xE, 0xD)
    OP_D5(0xD, 0x0, 0x297FC, 0x0, 0x0)
    OP_71(0xE, 0x0, 0x1, 0x0, 0x0)
    StopEffect(0x2, 0x2)
    StopEffect(0x3, 0x2)
    StopEffect(0x6, 0x2)
    Sleep(930)
    CancelBlur(1500)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xE, 0x2)
    Sound(196, 0, 90, 0)
    StopSound(865, 500, 70)
    StopSound(861, 500, 70)
    PlayEffect(0x3, 0xFF, 0xE, 0x0, 0, 3000, 0, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    EndChrThread(0xE, 0x2)
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    OP_78(0xF, 0xE)
    OP_D5(0xE, 0x0, 0x35B6A, 0x0, 0x0)
    OP_71(0xF, 0x0, 0x1, 0x0, 0x0)
    StopEffect(0x4, 0x2)
    StopEffect(0x5, 0x2)
    StopEffect(0x6, 0x2)
    WaitChrThread(0xF, 0)
    SetChrPos(0xF, 0, 0, 0, 0)
    SetChrPos(0xD, -1000, 29500, -255500, 60)
    SetChrPos(0xE, -3500, 10500, -192000, 130)
    OP_93(0xF, 0x0, 0x0)
    OP_93(0xD, 0x3C, 0x0)
    OP_93(0xE, 0x82, 0x0)
    OP_68(0, 3700, 1000, 0)
    MoveCamera(200, -1, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(24000, 0)
    OP_70(0x7, 0xDD)
    Fade(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1E)
    OP_68(2490, 3700, 680, 2000)
    MoveCamera(200, 2, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(14750, 2000)
    Sleep(300)
    CancelBlur(750)
    OP_25(0x3D4, 0x3C)
    StopSound(497, 1000, 50)
    BeginChrThread(0xF, 1, 0, 58)
    WaitChrThread(0xF, 1)
    Call(0, 36)
    OP_0D()
    BeginChrThread(0xF, 3, 0, 42)
    WaitChrThread(0xF, 3)
    Sleep(500)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    BeginChrThread(0xD, 3, 0, 52)
    Sleep(500)
    SetMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    BeginChrThread(0xE, 3, 0, 53)
    Sleep(1500)
    MoveCamera(315, 17, 0, 3000)
    SetCameraDistance(15250, 3000)
    Sleep(3500)
    BeginChrThread(0xF, 3, 0, 41)
    WaitChrThread(0xF, 3)
    StopSound(980, 2000, 70)
    OP_68(0, 3700, 1000, 3500)
    MoveCamera(345, 19, 0, 3500)
    Sleep(1000)
    SetCameraDistance(14500, 2500)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    Sound(998, 0, 100, 0)
    Sound(499, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0x1F4, 0x1F4, 0x5DC, 0x1F4)
    BeginChrThread(0xF, 3, 0, 57)
    Sleep(1500)
    CancelBlur(1000)
    StopSound(132, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x84)
    OP_24(0x1F1)
    OP_24(0x3D4)
    SetScenarioFlags(0x22, 0)
    NewScene("r0040", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_33_42D7 end

    def Function_34_5469(): pass

    label("Function_34_5469")

    Sleep(200)
    PlayEffect(0x5, 0x6, 0xFF, 0x0, -6700, -5000, 7030, 290, 25, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    PlayEffect(0x5, 0x7, 0xFF, 0x0, -6700, -5000, 7030, 310, 15, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sleep(100)
    PlayEffect(0x5, 0x6, 0xFF, 0x0, -6700, -5000, 7030, 330, 10, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sleep(100)
    PlayEffect(0x5, 0x7, 0xFF, 0x0, -6700, -5000, 7030, 345, 20, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    Sleep(100)
    StopEffect(0x6, 0x2)
    Sleep(100)
    Sleep(100)
    StopEffect(0x7, 0x2)
    Sleep(100)
    Sleep(100)
    OP_87(0x5, 0x6, 0x5, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x1388, 0x0)
    OP_87(0x5, 0x7, 0x6, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x1388, 0x0)
    Return()

    # Function_34_5469 end

    def Function_35_55D2(): pass

    label("Function_35_55D2")

    Sound(276, 0, 100, 0)
    OP_87(0x6, 0xFF, 0x7, "Null_bp_hou(16)", 0x5, 0xFFFFFC18, 0x15E, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0x0, 0x7, "Null_bp_hou(16)", 0x5, 0x0, 0x15E, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0x1, 0x7, "Null_bp_hou(16)", 0x5, 0x0, 0x32, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x3E8, 0x3E8, 0x0)
    Return()

    # Function_35_55D2 end

    def Function_36_5681(): pass

    label("Function_36_5681")

    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    Return()

    # Function_36_5681 end

    def Function_37_5688(): pass

    label("Function_37_5688")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56CC")
    OP_87(0x4, 0x4, 0x5, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    Sleep(150)
    Jump("Function_37_5688")

    label("loc_56CC")

    Return()

    # Function_37_5688 end

    def Function_38_56CD(): pass

    label("Function_38_56CD")

    Sleep(50)

    label("loc_56D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5714")
    OP_87(0x4, 0x5, 0x6, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    Sleep(150)
    Jump("loc_56D0")

    label("loc_5714")

    Return()

    # Function_38_56CD end

    def Function_39_5715(): pass

    label("Function_39_5715")

    Sleep(2000)
    OP_9B(0x1, 0xFE, 0x0, 0x27100, 0x186A0, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x7D00, 0x13880, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x3E80, 0xEA60, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x1F40, 0x9C40, 0x1)
    Return()

    # Function_39_5715 end

    def Function_40_5755(): pass

    label("Function_40_5755")

    ClearMapObjFlags(0x7, 0x20)
    OP_79(0x7)
    OP_74(0x7, 0xF)
    OP_71(0x7, 0x97, 0xA0, 0x0, 0x0)
    OP_79(0x7)
    OP_74(0x7, 0xF)
    OP_70(0x7, 0xB)
    Return()

    # Function_40_5755 end

    def Function_41_577A(): pass

    label("Function_41_577A")

    ClearMapObjFlags(0x7, 0x20)
    OP_79(0x7)
    Sound(982, 0, 100, 0)
    OP_74(0x7, 0xF)
    OP_71(0x7, 0xC9, 0xDC, 0x0, 0x0)
    OP_79(0x7)
    OP_74(0x7, 0x1E)
    OP_70(0x7, 0xDD)
    Return()

    # Function_41_577A end

    def Function_42_57A5(): pass

    label("Function_42_57A5")

    ClearMapObjFlags(0x7, 0x20)
    OP_79(0x7)
    OP_79(0x7)
    Sound(982, 0, 100, 0)
    OP_74(0x7, 0xF)
    OP_71(0x7, 0x105, 0x118, 0x0, 0x0)
    OP_79(0x7)
    OP_70(0x7, 0xB)
    Return()

    # Function_42_57A5 end

    def Function_43_57CF(): pass

    label("Function_43_57CF")

    OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0xFA0, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x1F40, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x2EE0, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x88B8, 0xC350, 0x1)
    Return()

    # Function_43_57CF end

    def Function_44_580C(): pass

    label("Function_44_580C")

    OP_9B(0x1, 0xFE, 0x0, 0x2F9B8, 0x13880, 0x1)
    Return()

    # Function_44_580C end

    def Function_45_581C(): pass

    label("Function_45_581C")

    Return()

    # Function_45_581C end

    def Function_46_581D(): pass

    label("Function_46_581D")

    Sleep(700)
    Sound(200, 0, 90, 0)
    Sound(833, 0, 100, 0)
    OP_82(0x64, 0x64, 0xBB8, 0x12C)
    PlayEffect(0x3, 0xFF, 0xA, 0x0, 0, 3000, 0, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    SetMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    OP_78(0xB, 0xA)
    OP_D5(0xA, 0x0, 0x2BF20, 0x0, 0x0)
    OP_71(0xB, 0x1, 0x1, 0x0, 0x0)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    Sleep(400)
    Sound(196, 0, 80, 0)
    OP_82(0x64, 0x64, 0xBB8, 0x12C)
    PlayEffect(0x3, 0xFF, 0xB, 0x0, 0, 3000, 0, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    SetMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    OP_78(0xC, 0xB)
    OP_D5(0xB, 0x0, 0x2BF20, 0x0, 0x0)
    OP_71(0xC, 0x1, 0x1, 0x0, 0x0)
    StopEffect(0x4, 0x0)
    StopEffect(0x5, 0x0)
    Sleep(400)
    Sound(556, 0, 80, 0)
    OP_82(0x64, 0x64, 0xBB8, 0x12C)
    PlayEffect(0x3, 0xFF, 0xC, 0x0, 0, 3000, 0, 0, 0, 0, 6000, 6000, 6000, 0xFF, 0, 0, 0, 0)
    SetMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    OP_78(0xD, 0xC)
    OP_D5(0xC, 0x0, 0x2BF20, 0x0, 0x0)
    OP_71(0xD, 0x0, 0x1, 0x0, 0x0)
    StopEffect(0x6, 0x0)
    StopEffect(0x7, 0x0)
    Return()

    # Function_46_581D end

    def Function_47_59B6(): pass

    label("Function_47_59B6")

    OP_9B(0x1, 0xFE, 0x0, 0x186A0, 0xD6D8, 0x1)
    Return()

    # Function_47_59B6 end

    def Function_48_59C6(): pass

    label("Function_48_59C6")

    Sleep(450)
    BeginChrThread(0xA, 3, 0, 49)
    Sleep(250)
    BeginChrThread(0xB, 3, 0, 50)
    Sleep(250)
    BeginChrThread(0xC, 3, 0, 51)
    Sleep(350)
    Return()

    # Function_48_59C6 end

    def Function_49_59E5(): pass

    label("Function_49_59E5")

    OP_71(0xB, 0x1, 0x3C, 0x0, 0x0)
    PlayEffect(0x2, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(900)
    StopEffect(0x2, 0x2)
    Return()

    # Function_49_59E5 end

    def Function_50_5A66(): pass

    label("Function_50_5A66")

    OP_71(0xC, 0x1, 0x3C, 0x0, 0x0)
    PlayEffect(0x2, 0xFF, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x3, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_5AE5():
        OP_D5(0xFE, 0x0, 0x15F90, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_5AE5)
    Sleep(900)
    StopEffect(0x3, 0x2)
    Return()

    # Function_50_5A66 end

    def Function_51_5B00(): pass

    label("Function_51_5B00")

    OP_71(0xD, 0x1, 0x3C, 0x0, 0x0)
    PlayEffect(0x2, 0xFF, 0xC, 0x0, 0, 0, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x4, 0xC, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_5B7F():
        OP_D5(0xFE, 0x0, 0xFFFF15A0, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_5B7F)
    Sleep(900)
    StopEffect(0x4, 0x2)
    Return()

    # Function_51_5B00 end

    def Function_52_5B9A(): pass

    label("Function_52_5B9A")

    Sound(200, 0, 80, 0)
    Sound(833, 0, 100, 0)
    OP_71(0xE, 0x1, 0x3C, 0x0, 0x0)
    PlayEffect(0x2, 0xFF, 0xD, 0x0, 0, 0, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x2, 0xD, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_5C25():
        OP_D5(0xFE, 0x0, 0xFFFF63C0, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_5C25)
    Sleep(900)
    StopEffect(0x2, 0x2)
    Return()

    # Function_52_5B9A end

    def Function_53_5C40(): pass

    label("Function_53_5C40")

    Sound(196, 0, 80, 0)
    OP_71(0xF, 0x1, 0x3C, 0x0, 0x0)
    PlayEffect(0x2, 0xFF, 0xE, 0x0, 0, 0, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x3, 0xE, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_5CC5():
        OP_D5(0xFE, 0x0, 0x9C40, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_5CC5)
    Sleep(900)
    StopEffect(0x3, 0x2)
    Return()

    # Function_53_5C40 end

    def Function_54_5CE0(): pass

    label("Function_54_5CE0")

    SetChrPos(0xFE, 50000, 0, 0, 180)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 40000, 4000, -25000)
    OP_9F(0x1, 25000, -4000, -40000)
    OP_9F(0x1, -10000, 4000, -45000)
    OP_9F(0x1, -65000, -4000, -35000)
    OP_9F(0x1, -85000, 18000, -25000)
    OP_9F(0x2, 0xFE, 80000, 0x2)
    Return()

    # Function_54_5CE0 end

    def Function_55_5D45(): pass

    label("Function_55_5D45")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -27000, 12000, -3000)
    OP_9F(0x1, 72000, -20000, -2000)
    OP_9F(0x2, 0xFE, 80000, 0x7)
    Return()

    # Function_55_5D45 end

    def Function_56_5D6F(): pass

    label("Function_56_5D6F")

    Sleep(500)
    OP_71(0x7, 0xFC, 0x104, 0x0, 0x0)
    OP_79(0x7)
    Sleep(500)
    OP_71(0x7, 0x104, 0xFB, 0x0, 0x0)
    OP_79(0x7)
    Sleep(1300)
    Return()

    # Function_56_5D6F end

    def Function_57_5D97(): pass

    label("Function_57_5D97")

    SetChrPos(0xFE, 0, 0, 0, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 0, -50000, 200000)
    OP_9F(0x2, 0xFE, 100000, 0x2)
    Return()

    # Function_57_5D97 end

    def Function_58_5DC4(): pass

    label("Function_58_5DC4")

    ClearMapObjFlags(0x7, 0x20)
    OP_79(0x7)
    OP_70(0x7, 0xDD)
    Sleep(450)
    Return()

    # Function_58_5DC4 end

    def Function_59_5DD5(): pass

    label("Function_59_5DD5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5EEB")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5DFB")
    Sleep(200)
    Jump("loc_5E4F")

    label("loc_5DFB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5E16")
    Sleep(400)
    Jump("loc_5E4F")

    label("loc_5E16")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5E31")
    Sleep(600)
    Jump("loc_5E4F")

    label("loc_5E31")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5E4C")
    Sleep(800)
    Jump("loc_5E4F")

    label("loc_5E4C")

    Sleep(1000)

    label("loc_5E4F")

    OP_98(0xFE, 0x0, 0xFFFFF63C, 0x0, 0x12C, 0x1)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5E7E")
    Sleep(200)
    Jump("loc_5ED2")

    label("loc_5E7E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5E99")
    Sleep(400)
    Jump("loc_5ED2")

    label("loc_5E99")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5EB4")
    Sleep(600)
    Jump("loc_5ED2")

    label("loc_5EB4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5ECF")
    Sleep(800)
    Jump("loc_5ED2")

    label("loc_5ECF")

    Sleep(1000)

    label("loc_5ED2")

    OP_98(0xFE, 0x0, 0x9C4, 0x0, 0x12C, 0x1)
    Jump("Function_59_5DD5")

    label("loc_5EEB")

    Return()

    # Function_59_5DD5 end

    def Function_60_5EEC(): pass

    label("Function_60_5EEC")

    Sleep(800)
    Sound(833, 0, 100, 0)
    Sound(200, 0, 80, 0)
    Sleep(500)
    Sound(196, 0, 70, 0)
    Sleep(500)
    Sound(556, 0, 70, 0)
    Return()

    # Function_60_5EEC end

    def Function_61_5F0E(): pass

    label("Function_61_5F0E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    LoadEffect(0x0, "event/ev600_01.eff")
    LoadEffect(0x1, "event/ev601_01.eff")
    LoadChrToIndex("chr/ch09500.itc", 0x20)
    SoundLoad(825)
    SoundLoad(933)
    Call(0, 62)
    SetChrPos(0x10, 0, -50000, 0, 0)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0x9, 0x1000)
    OP_68(0, -51500, 0, 0)
    MoveCamera(180, -45, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(57000, 0)
    Sound(825, 2, 100, 0)
    Sound(993, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_68(0, -45000, 0, 4000)
    MoveCamera(180, -22, 0, 4000)
    OP_6E(800, 4000)
    SetCameraDistance(9250, 4000)
    OP_0D()
    Sound(990, 0, 100, 0)
    Sleep(1000)
    Sound(994, 0, 100, 0)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    Sleep(500)
    StopSound(825, 500, 100)
    StopSound(993, 500, 100)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("e4211", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_61_5F0E end

    def Function_62_602F(): pass

    label("Function_62_602F")

    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 0, 0, 0, 0)
    OP_74(0x9, 0x1E)
    OP_78(0x9, 0x10)
    OP_93(0x10, 0x0, 0x0)
    SetChrFlags(0x10, 0x4)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x20)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    OP_52(0x11, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 0, 0, 0, 0)
    OP_D3(0x11, 0x9, "Null_ren(52)")
    OP_87(0x1, 0x0, 0x9, "Null_S_jet_r0(63)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x1, 0x1, 0x9, "Null_S_jet_r2(64)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x1, 0x2, 0x9, "Null_S_jet_l0(66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x1, 0x3, 0x9, "Null_S_jet_l2(65)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0x4, 0x9, "Null_S_jet_r1(61)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0x5, 0x9, "Null_S_jet_l1(62)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0x6, 0x9, "Null_kata_jet_r(53)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0x7, 0x9, "Null_kata_jet_l(54)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_71(0x9, 0xF1, 0x104, 0x1, 0x20)
    Return()

    # Function_62_602F end

    SaveToFile()

Try(main)
