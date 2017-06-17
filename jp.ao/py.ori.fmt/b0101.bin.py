from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "b0101.bin",                # FileName
        "b0101",                    # MapName
        "b0101",                    # Location
        0x0000,                     # MapIndex
        "ed7450",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0xFF,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "b0101",                  # 0
    ))

    ChipFrameInfo(420, 0)                                        # 0

    ScpFunction((
        "Function_0_1A4",          # 00, 0
        "Function_1_1A8",          # 01, 1
        "Function_2_20E",          # 02, 2
        "Function_3_237",          # 03, 3
        "Function_4_264",          # 04, 4
        "Function_5_2EE",          # 05, 5
        "Function_6_353",          # 06, 6
        "Function_7_458",          # 07, 7
    ))


    def Function_0_1A4(): pass

    label("Function_0_1A4")

    Event(0, 7)
    Return()

    # Function_0_1A4 end

    def Function_1_1A8(): pass

    label("Function_1_1A8")

    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis120.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFF000000, 0x1, "c_vis120.itp")
    OP_C9(0x0, 0x10)
    SetMapFlags(0x80)
    OP_16(0x0)
    Return()

    # Function_1_1A8 end

    def Function_2_20E(): pass

    label("Function_2_20E")

    OP_60(0x2)
    OP_60(0x1)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    Sleep(500)
    OP_0D()
    Return()

    # Function_2_20E end

    def Function_3_237(): pass

    label("Function_3_237")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0xC8, 0x0, 0x0)
    Call(0, 4)
    Call(0, 5)
    OP_CB(0x1, 0x3, 0x0, 0x1F4, 0x0, 0x0)
    Return()

    # Function_3_237 end

    def Function_4_264(): pass

    label("Function_4_264")

    SetChrName("")
    SetMessageWindowPos(120, 0, 28, 1)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            "　　　クラフトビューア",
            scpstr(0x18),
            scpstr(0x6),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        1,
        32,
        96,
        1,
        (
            "Ｓクラフト①\x01",          # 0
            "Ｓクラフト②\x01",          # 1
            "Ｓクラフト③\x01",          # 2
            "コンビクラフト①\x01",      # 3
            "コンビクラフト②\x01",      # 4
            "戻る\x01",                  # 5
        )
    )

    MenuCmd(4, 1, 0x3)
    Sleep(200)
    MenuCmd(6, 1)
    Return()

    # Function_4_264 end

    def Function_5_2EE(): pass

    label("Function_5_2EE")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_31C"),
        (1, "loc_325"),
        (2, "loc_32E"),
        (3, "loc_337"),
        (4, "loc_340"),
        (5, "loc_349"),
        (SWITCH_DEFAULT, "loc_352"),
    )


    label("loc_31C")

    MenuCmd(5, 1, 0x0)
    Jump("loc_352")

    label("loc_325")

    MenuCmd(5, 1, 0x1)
    Jump("loc_352")

    label("loc_32E")

    MenuCmd(5, 1, 0x2)
    Jump("loc_352")

    label("loc_337")

    MenuCmd(5, 1, 0x3)
    Jump("loc_352")

    label("loc_340")

    MenuCmd(5, 1, 0x4)
    Jump("loc_352")

    label("loc_349")

    MenuCmd(5, 1, 0x5)
    Jump("loc_352")

    label("loc_352")

    Return()

    # Function_5_2EE end

    def Function_6_353(): pass

    label("Function_6_353")

    MenuCmd(4, 2, 0x3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_3C1"),
        (1, "loc_3CA"),
        (2, "loc_3D3"),
        (3, "loc_3DC"),
        (4, "loc_3E5"),
        (5, "loc_3EE"),
        (6, "loc_3F7"),
        (7, "loc_400"),
        (8, "loc_409"),
        (9, "loc_412"),
        (10, "loc_41B"),
        (11, "loc_424"),
        (12, "loc_42D"),
        (13, "loc_436"),
        (14, "loc_43F"),
        (15, "loc_448"),
        (SWITCH_DEFAULT, "loc_451"),
    )


    label("loc_3C1")

    MenuCmd(5, 2, 0x0)
    Jump("loc_451")

    label("loc_3CA")

    MenuCmd(5, 2, 0x1)
    Jump("loc_451")

    label("loc_3D3")

    MenuCmd(5, 2, 0x2)
    Jump("loc_451")

    label("loc_3DC")

    MenuCmd(5, 2, 0x3)
    Jump("loc_451")

    label("loc_3E5")

    MenuCmd(5, 2, 0x4)
    Jump("loc_451")

    label("loc_3EE")

    MenuCmd(5, 2, 0x5)
    Jump("loc_451")

    label("loc_3F7")

    MenuCmd(5, 2, 0x6)
    Jump("loc_451")

    label("loc_400")

    MenuCmd(5, 2, 0x7)
    Jump("loc_451")

    label("loc_409")

    MenuCmd(5, 2, 0x8)
    Jump("loc_451")

    label("loc_412")

    MenuCmd(5, 2, 0x9)
    Jump("loc_451")

    label("loc_41B")

    MenuCmd(5, 2, 0xA)
    Jump("loc_451")

    label("loc_424")

    MenuCmd(5, 2, 0xB)
    Jump("loc_451")

    label("loc_42D")

    MenuCmd(5, 2, 0xC)
    Jump("loc_451")

    label("loc_436")

    MenuCmd(5, 2, 0xD)
    Jump("loc_451")

    label("loc_43F")

    MenuCmd(5, 2, 0xE)
    Jump("loc_451")

    label("loc_448")

    MenuCmd(5, 2, 0xF)
    Jump("loc_451")

    label("loc_451")

    MenuEnd(0x3)
    OP_60(0x2)
    Return()

    # Function_6_353 end

    def Function_7_458(): pass

    label("Function_7_458")

    OP_CB(0x1, 0x3, 0x0, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    Sleep(500)
    PlayBGM("ed7450", 0)
    OP_C9(0x0, 0x8)
    SetMapFlags(0x2000000)
    SetChrName("")
    SetMessageWindowPos(120, 0, 28, 1)

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "　　　クラフトビューア",
            scpstr(0x18),
            scpstr(0x6),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    label("loc_4B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AC4")
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        1,
        32,
        96,
        1,
        (
            "Ｓクラフト①\x01",          # 0
            "Ｓクラフト②\x01",          # 1
            "Ｓクラフト③\x01",          # 2
            "コンビクラフト①\x01",      # 3
            "コンビクラフト②\x01",      # 4
            "戻る\x01",                  # 5
        )
    )

    MenuCmd(4, 1, 0x3)
    Call(0, 5)
    MenuEnd(0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_565"),
        (1, "loc_ABB"),
        (2, "loc_EDB"),
        (3, "loc_1287"),
        (4, "loc_15F5"),
        (SWITCH_DEFAULT, "loc_1AA6"),
    )


    label("loc_565")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AB3")

    Menu(
        2,
        -1,
        108,
        1,
        (
            "#176I：タイガーチャージ\x01",        # 0
            "#176I：ライジングサン\x01",          # 1
            "#176I：メテオブレイカー\x01",        # 2
            "#177I：オーラレイン\x01",            # 3
            "#177I：エアリアルカノン\x01",        # 4
            "#177I：デバインクルセイド\x01",      # 5
            "#178I：エーテルバスター\x01",        # 6
            "#178I：ゼロ・フィールド\x01",        # 7
            "#178I：エイドロンギア\x01",          # 8
            "#179I：クリムゾンゲイル\x01",        # 9
            "#179I：デススコルピオン\x01",        # 10
            "#179I：ベルゼルガー\x01",            # 11
            "やめる\x01",                         # 12
        )
    )

    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6BD")
    Call(0, 2)
    SetScenarioFlags(0x0, 0)

    label("loc_6BD")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_70F"),
        (1, "loc_75B"),
        (2, "loc_7A7"),
        (3, "loc_7F3"),
        (4, "loc_83F"),
        (5, "loc_88B"),
        (6, "loc_8D7"),
        (7, "loc_923"),
        (8, "loc_96F"),
        (9, "loc_9BB"),
        (10, "loc_A07"),
        (11, "loc_A53"),
        (SWITCH_DEFAULT, "loc_A9F"),
    )


    label("loc_70F")

    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000000, 0x0, 0x0, 0x0, 0x30087200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 0)
    Call(0, 3)
    Jump("loc_AAE")

    label("loc_75B")

    SetScenarioFlags(0x5C, 1)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000000, 0x0, 0x0, 0x0, 0x30087200, 0x30087200, 0x30087200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 1)
    Call(0, 3)
    Jump("loc_AAE")

    label("loc_7A7")

    SetScenarioFlags(0x5C, 2)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000000, 0x0, 0x0, 0x0, 0x30087200, 0x30087200, 0x30087200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 2)
    Call(0, 3)
    Jump("loc_AAE")

    label("loc_7F3")

    SetScenarioFlags(0x5C, 3)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000100, 0x30000000, 0x30000200, 0x30000300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 3)
    Call(0, 3)
    Jump("loc_AAE")

    label("loc_83F")

    SetScenarioFlags(0x5C, 4)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000100, 0x0, 0x0, 0x0, 0x30087500, 0x30087500, 0x30087500, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 4)
    Call(0, 3)
    Jump("loc_AAE")

    label("loc_88B")

    SetScenarioFlags(0x5C, 5)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000100, 0x0, 0x0, 0x0, 0x30087500, 0x30087500, 0x30087500, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 5)
    Call(0, 3)
    Jump("loc_AAE")

    label("loc_8D7")

    SetScenarioFlags(0x5C, 6)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000200, 0x0, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 6)
    Call(0, 3)
    Jump("loc_AAE")

    label("loc_923")

    SetScenarioFlags(0x5C, 7)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000200, 0x30000000, 0x30000100, 0x30000300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 7)
    Call(0, 3)
    Jump("loc_AAE")

    label("loc_96F")

    SetScenarioFlags(0x5D, 0)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000200, 0x0, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 0)
    Call(0, 3)
    Jump("loc_AAE")

    label("loc_9BB")

    SetScenarioFlags(0x5D, 1)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000300, 0x0, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 1)
    Call(0, 3)
    Jump("loc_AAE")

    label("loc_A07")

    SetScenarioFlags(0x5D, 2)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000300, 0x0, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 2)
    Call(0, 3)
    Jump("loc_AAE")

    label("loc_A53")

    SetScenarioFlags(0x5D, 3)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000300, 0x0, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 3)
    Call(0, 3)
    Jump("loc_AAE")

    label("loc_A9F")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_AAE")

    label("loc_AAE")

    Jump("loc_565")

    label("loc_AB3")

    ClearScenarioFlags(0x0, 0)
    Jump("loc_1ABF")

    label("loc_ABB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ED3")

    Menu(
        2,
        -1,
        108,
        1,
        (
            "#180I：デッドリーヘヴン\x01",          # 0
            "#180I：アカシックアーム\x01",          # 1
            "#184I：ブラストストーム\x01",          # 2
            "#184I：アームドフォース\x01",          # 3
            "#181I：幻月の舞\x01",                  # 4
            "#187I：真・幻月の舞\x01",              # 5
            "#185I：ジャスティスハンマー\x01",      # 6
            "#185I：ジャスティスマグナム\x01",      # 7
            "#186I：キリングドライバー\x01",        # 8
            "やめる\x01",                           # 9
        )
    )

    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BD3")
    Call(0, 2)
    SetScenarioFlags(0x0, 0)

    label("loc_BD3")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_C13"),
        (1, "loc_C5F"),
        (2, "loc_CAB"),
        (3, "loc_CF7"),
        (4, "loc_D43"),
        (5, "loc_D8F"),
        (6, "loc_DDB"),
        (7, "loc_E27"),
        (8, "loc_E73"),
        (SWITCH_DEFAULT, "loc_EBF"),
    )


    label("loc_C13")

    SetScenarioFlags(0x5D, 4)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000400, 0x0, 0x0, 0x0, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 4)
    Call(0, 3)
    Jump("loc_ECE")

    label("loc_C5F")

    SetScenarioFlags(0x5D, 5)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30003100, 0x0, 0x0, 0x0, 0x30087400, 0x30087400, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 5)
    Call(0, 3)
    Jump("loc_ECE")

    label("loc_CAB")

    SetScenarioFlags(0x5D, 6)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000800, 0x0, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 6)
    Call(0, 3)
    Jump("loc_ECE")

    label("loc_CF7")

    SetScenarioFlags(0x5D, 7)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000800, 0x0, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 7)
    Call(0, 3)
    Jump("loc_ECE")

    label("loc_D43")

    SetScenarioFlags(0x5E, 0)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000500, 0x0, 0x0, 0x0, 0x30087500, 0x30087500, 0x30087500, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5E, 0)
    Call(0, 3)
    Jump("loc_ECE")

    label("loc_D8F")

    SetScenarioFlags(0x5E, 1)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30003200, 0x0, 0x0, 0x0, 0x30087500, 0x30087500, 0x30087500, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5E, 1)
    Call(0, 3)
    Jump("loc_ECE")

    label("loc_DDB")

    SetScenarioFlags(0x5E, 2)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000900, 0x0, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5E, 2)
    Call(0, 3)
    Jump("loc_ECE")

    label("loc_E27")

    SetScenarioFlags(0x5E, 3)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000900, 0x0, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5E, 3)
    Call(0, 3)
    Jump("loc_ECE")

    label("loc_E73")

    SetScenarioFlags(0x5E, 4)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30004100, 0x0, 0x0, 0x0, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5E, 4)
    Call(0, 3)
    Jump("loc_ECE")

    label("loc_EBF")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_ECE")

    label("loc_ECE")

    Jump("loc_ABB")

    label("loc_ED3")

    ClearScenarioFlags(0x0, 0)
    Jump("loc_1ABF")

    label("loc_EDB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_127F")

    Menu(
        2,
        -1,
        108,
        1,
        (
            "#183I：風神烈破\x01",                    # 0
            "#183I：終の太刀-黒皇-\x01",              # 1
            "#190I：デス・パレード\x01",              # 2
            "#207I：クリムゾンフォール\x01",          # 3
            "#189I：偽・塩の杭\x01",                  # 4
            "#188I：聖技グランドクロス\x01",          # 5
            "#191I：クリムゾンザンバー\x01",          # 6
            "#191I：メリーメリーキャッスル\x01",      # 7
            "やめる\x01",                             # 8
        )
    )

    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FD7")
    Call(0, 2)
    SetScenarioFlags(0x0, 0)

    label("loc_FD7")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1011"),
        (1, "loc_105D"),
        (2, "loc_10A9"),
        (3, "loc_10F5"),
        (4, "loc_1141"),
        (5, "loc_118D"),
        (6, "loc_11D9"),
        (7, "loc_1225"),
        (SWITCH_DEFAULT, "loc_126B"),
    )


    label("loc_1011")

    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30002400, 0x0, 0x0, 0x0, 0x30087400, 0x30087400, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 0)
    Call(0, 3)
    Jump("loc_127A")

    label("loc_105D")

    SetScenarioFlags(0x5C, 1)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30002400, 0x0, 0x0, 0x0, 0x30087400, 0x30087400, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 1)
    Call(0, 3)
    Jump("loc_127A")

    label("loc_10A9")

    SetScenarioFlags(0x5C, 2)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30003400, 0x0, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 2)
    Call(0, 3)
    Jump("loc_127A")

    label("loc_10F5")

    SetScenarioFlags(0x5C, 3)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30003300, 0x0, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 3)
    Call(0, 3)
    Jump("loc_127A")

    label("loc_1141")

    SetScenarioFlags(0x5C, 4)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30003600, 0x0, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 4)
    Call(0, 3)
    Jump("loc_127A")

    label("loc_118D")

    SetScenarioFlags(0x5C, 5)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30004200, 0x0, 0x0, 0x0, 0x30087200, 0x30087200, 0x30087200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 5)
    Call(0, 3)
    Jump("loc_127A")

    label("loc_11D9")

    SetScenarioFlags(0x5C, 6)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30003700, 0x0, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 6)
    Call(0, 3)
    Jump("loc_127A")

    label("loc_1225")

    Battle(0xFFFFFFFF, 0x30200101, "", 0x30003700, 0x0, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    Call(0, 3)
    Jump("loc_127A")

    label("loc_126B")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_127A")

    label("loc_127A")

    Jump("loc_EDB")

    label("loc_127F")

    ClearScenarioFlags(0x0, 0)
    Jump("loc_1ABF")

    label("loc_1287")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15ED")

    Menu(
        2,
        -1,
        108,
        1,
        (
            "#176I#177I：スターブラスト\x01",          # 0
            "#176I#178I：Ωストライク\x01",            # 1
            "#176I#179I：バーニングレイジ\x01",        # 2
            "#176I#184I：ブレイブハーツ\x01",          # 3
            "#176I#180I：ストライクヘヴン\x01",        # 4
            "#176I#187I：比翼双竜撃\x01",              # 5
            "#176I#185I：ハーツオブアイアン\x01",      # 6
            "やめる\x01",                              # 7
        )
    )

    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1388")
    Call(0, 2)
    SetScenarioFlags(0x0, 0)

    label("loc_1388")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_13BC"),
        (1, "loc_1408"),
        (2, "loc_1454"),
        (3, "loc_14A0"),
        (4, "loc_14EC"),
        (5, "loc_1538"),
        (6, "loc_1592"),
        (SWITCH_DEFAULT, "loc_15DE"),
    )


    label("loc_13BC")

    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30000100, 0x0, 0x0, 0x30087500, 0x30087500, 0x30087500, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 0)
    Call(0, 3)
    Jump("loc_15E8")

    label("loc_1408")

    SetScenarioFlags(0x5C, 1)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30000200, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 1)
    Call(0, 3)
    Jump("loc_15E8")

    label("loc_1454")

    SetScenarioFlags(0x5C, 2)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30000300, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 2)
    Call(0, 3)
    Jump("loc_15E8")

    label("loc_14A0")

    SetScenarioFlags(0x5C, 3)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30000800, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 3)
    Call(0, 3)
    Jump("loc_15E8")

    label("loc_14EC")

    SetScenarioFlags(0x5C, 4)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30000400, 0x0, 0x0, 0x30087400, 0x30087400, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 4)
    Call(0, 3)
    Jump("loc_15E8")

    label("loc_1538")

    SetScenarioFlags(0x5C, 5)
    SetChrChipPat(0x5, 0x1, 0x20)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30003200, 0x0, 0x0, 0x30087200, 0x30087200, 0x30087200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    SetChrChipPat(0x5, 0x1, 0x5)
    ClearScenarioFlags(0x5C, 5)
    Call(0, 3)
    Jump("loc_15E8")

    label("loc_1592")

    SetScenarioFlags(0x5C, 6)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30000900, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 6)
    Call(0, 3)
    Jump("loc_15E8")

    label("loc_15DE")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15E8")

    Jump("loc_1287")

    label("loc_15ED")

    ClearScenarioFlags(0x0, 0)
    Jump("loc_1ABF")

    label("loc_15F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A9E")

    Menu(
        2,
        -1,
        108,
        1,
        (
            "#177I#178I：コールドゲヘナ\x01",        # 0
            "#177I#179I：ライアットスター\x01",      # 1
            "#177I#184I：サザンクロス\x01",          # 2
            "#177I#180I：アカシックスター\x01",      # 3
            "#178I#179I：ハーケンストーム\x01",      # 4
            "#178I#184I：ブラストハンマー\x01",      # 5
            "#178I#180I：Σアセンション\x01",        # 6
            "#179I#184I：ハウリングレイド\x01",      # 7
            "#179I#180I：ラストリベリオン\x01",      # 8
            "#180I#184I：ブルーブレイカー\x01",      # 9
            "やめる\x01",                            # 10
        )
    )

    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1751")
    Call(0, 2)
    SetScenarioFlags(0x0, 0)

    label("loc_1751")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1797"),
        (1, "loc_17E3"),
        (2, "loc_182F"),
        (3, "loc_187B"),
        (4, "loc_18C7"),
        (5, "loc_1913"),
        (6, "loc_195F"),
        (7, "loc_19AB"),
        (8, "loc_19F7"),
        (9, "loc_1A43"),
        (SWITCH_DEFAULT, "loc_1A8F"),
    )


    label("loc_1797")

    SetScenarioFlags(0x5C, 7)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000100, 0x30000200, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 7)
    Call(0, 3)
    Jump("loc_1A99")

    label("loc_17E3")

    SetScenarioFlags(0x5D, 0)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000100, 0x30000300, 0x0, 0x0, 0x30087500, 0x30087500, 0x30087500, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 0)
    Call(0, 3)
    Jump("loc_1A99")

    label("loc_182F")

    SetScenarioFlags(0x5D, 1)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000100, 0x30000800, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 1)
    Call(0, 3)
    Jump("loc_1A99")

    label("loc_187B")

    SetScenarioFlags(0x5D, 2)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000100, 0x30000400, 0x0, 0x0, 0x30087400, 0x30087400, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 2)
    Call(0, 3)
    Jump("loc_1A99")

    label("loc_18C7")

    SetScenarioFlags(0x5D, 3)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000200, 0x30000300, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 3)
    Call(0, 3)
    Jump("loc_1A99")

    label("loc_1913")

    SetScenarioFlags(0x5D, 4)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000200, 0x30000800, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 4)
    Call(0, 3)
    Jump("loc_1A99")

    label("loc_195F")

    SetScenarioFlags(0x5D, 5)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000200, 0x30000400, 0x0, 0x0, 0x30087200, 0x30087200, 0x30087200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 5)
    Call(0, 3)
    Jump("loc_1A99")

    label("loc_19AB")

    SetScenarioFlags(0x5D, 6)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000300, 0x30000800, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 6)
    Call(0, 3)
    Jump("loc_1A99")

    label("loc_19F7")

    SetScenarioFlags(0x5D, 7)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000300, 0x30000400, 0x0, 0x0, 0x30087400, 0x30087400, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 7)
    Call(0, 3)
    Jump("loc_1A99")

    label("loc_1A43")

    SetScenarioFlags(0x5E, 0)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000400, 0x30000800, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5E, 0)
    Call(0, 3)
    Jump("loc_1A99")

    label("loc_1A8F")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A99")

    Jump("loc_15F5")

    label("loc_1A9E")

    ClearScenarioFlags(0x0, 0)
    Jump("loc_1ABF")

    label("loc_1AA6")

    FadeToBright(300, 0)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1ABF")

    label("loc_1ABF")

    Jump("loc_4B8")

    label("loc_1AC4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    OP_57(0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    StopBGM(0x3E8)
    Sleep(500)
    OP_C9(0x1, 0x8)
    ClearMapFlags(0x2000000)
    OP_B9(0x2)
    Return()

    # Function_7_458 end

    SaveToFile()

Try(main)
