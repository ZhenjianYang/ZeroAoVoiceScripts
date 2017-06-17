from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "e4810.bin",                # FileName
        "e4810",                    # MapName
        "e4810",                    # Location
        0x0000,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "e4810",                  # 0
        "SE制御",                 # 1
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    ChipFrameInfo(200, 0)                                        # 0

    ScpFunction((
        "Function_0_C8",           # 00, 0
        "Function_1_D8",           # 01, 1
        "Function_2_DD",           # 02, 2
        "Function_3_49E",          # 03, 3
        "Function_4_4D6",          # 04, 4
        "Function_5_507",          # 05, 5
    ))


    def Function_0_C8(): pass

    label("Function_0_C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_D7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 2)

    label("loc_D7")

    Return()

    # Function_0_C8 end

    def Function_1_D8(): pass

    label("Function_1_D8")

    OP_F0(0x1, 0x7D0)
    Return()

    # Function_1_D8 end

    def Function_2_DD(): pass

    label("Function_2_DD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    FadeToDark(0, -1, 0)
    SoundLoad(938)
    SoundLoad(939)
    SoundLoad(941)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    OP_68(206680, 0, 0, 0)
    MoveCamera(90, 0, 0, 0)
    OP_6E(0, 0)
    SetCameraDistance(13500, 0)
    SetMapObjFlags(0x1, 0x1000)
    ClearMapObjFlags(0x1, 0x4)
    OP_70(0x1, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFlags(0x0, 0x4)
    OP_70(0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x1, 0x0, 0x12C, 0x0, 0x0)
    BeginChrThread(0x8, 1, 0, 4)
    OP_79(0x1)
    SetChrName("少年")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            "#04804F《星辰#4Rアストラル#のコード》の\x01",
            "インストールを完了……\x02\x03",

            "#04802Fそれじゃあ、始めようかな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 16777215, -1)
    OP_0D()
    OP_68(-23020, 0, 42340, 0)
    MoveCamera(132, 7, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(6500, 0)
    BeginChrThread(0x0, 3, 0, 3)
    FadeToBright(0, -1)
    SetMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x0, 0x4)
    OP_71(0x0, 0x0, 0x257, 0x0, 0x20)
    Sound(938, 2, 50, 0)
    Sound(940, 0, 100, 0)
    Sound(941, 2, 100, 0)
    FadeToBright(2000, 16777215)
    OP_0D()
    Sleep(500)
    SetChrName("少年")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "#04803F#30W──位相空間にアクセス。\x01",
            "導力ネットの全領域をサーチ開始。\x02\x03",

            "複数ルートからの侵入経路を確保。\x02\x03",

            "#04801F第１、第２、第３防壁をクリア……\x02\x03",

            "ロジックキーの解析に成功。\x01",
            "メイン端末への最終防壁を攻略……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(2000, 16777215, -1)
    OP_0D()
    EndChrThread(0x0, 0x3)
    FadeToDark(0, -1, 0)
    OP_68(206680, 0, 0, 0)
    MoveCamera(90, 0, 0, 0)
    OP_6E(0, 0)
    SetCameraDistance(13500, 0)
    ClearMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x0, 0x4)
    OP_71(0x1, 0x15E, 0x1C1, 0x0, 0x20)
    StopSound(938, 1000, 50)
    StopSound(941, 1000, 100)
    Sound(940, 0, 100, 0)
    FadeToBright(1000, 16777215)
    OP_0D()
    BeginChrThread(0x8, 1, 0, 5)
    Sleep(2000)
    SetChrName("少年")

    #A0003
    AnonymousTalk(
        0xFF,
        (
            "#04804Fフフ、さすが博士が\x01",
            "自慢するだけはあるかもね。\x02\x03",

            "#04802Fさてと、お楽しみは取っておくとして\x01",
            "仕掛けのネタを漁ろうかな。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_71(0x1, 0x1C2, 0x3E8, 0x0, 0x0)
    Sound(840, 0, 100, 0)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    OP_24(0x3AA)
    OP_24(0x3AD)
    OP_24(0x3AB)
    SetScenarioFlags(0x22, 2)
    NewScene("m0101", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_2_DD end

    def Function_3_49E(): pass

    label("Function_3_49E")

    MoveCamera(132, 22, 0, 5000)
    OP_6F(0x79)

    label("loc_4AB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4D5")
    MoveCamera(119, -1, 0, 10000)
    OP_6F(0x79)
    MoveCamera(132, 22, 0, 10000)
    OP_6F(0x79)
    Jump("loc_4AB")

    label("loc_4D5")

    Return()

    # Function_3_49E end

    def Function_4_4D6(): pass

    label("Function_4_4D6")

    Sound(939, 2, 100, 0)
    Sleep(800)
    OP_24(0x3AB)
    Sound(202, 0, 100, 0)
    Sleep(1200)
    Sound(939, 2, 100, 0)
    Sleep(4500)
    StopSound(939, 500, 100)
    Sound(202, 0, 100, 0)
    Sound(935, 0, 100, 0)
    Return()

    # Function_4_4D6 end

    def Function_5_507(): pass

    label("Function_5_507")

    Sound(839, 0, 100, 0)
    Sleep(400)
    Sound(839, 0, 100, 0)
    Sleep(800)
    Sound(839, 0, 100, 0)
    Sleep(400)
    Sound(839, 0, 100, 0)
    Return()

    # Function_5_507 end

    SaveToFile()

Try(main)
