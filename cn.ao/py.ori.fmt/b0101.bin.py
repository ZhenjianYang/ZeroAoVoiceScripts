from ScenarioHelper import *

def main():
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
        "Function_5_2D6",          # 05, 5
        "Function_6_33B",          # 06, 6
        "Function_7_440",          # 07, 7
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
            "　　　　　战技一览　　",
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
            "Ｓ战技①\x01",        # 0
            "Ｓ战技②\x01",        # 1
            "Ｓ战技③\x01",        # 2
            "组合战技①\x01",      # 3
            "组合战技②\x01",      # 4
            "返回\x01",            # 5
        )
    )

    MenuCmd(4, 1, 0x3)
    Sleep(200)
    MenuCmd(6, 1)
    Return()

    # Function_4_264 end

    def Function_5_2D6(): pass

    label("Function_5_2D6")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_304"),
        (1, "loc_30D"),
        (2, "loc_316"),
        (3, "loc_31F"),
        (4, "loc_328"),
        (5, "loc_331"),
        (SWITCH_DEFAULT, "loc_33A"),
    )


    label("loc_304")

    MenuCmd(5, 1, 0x0)
    Jump("loc_33A")

    label("loc_30D")

    MenuCmd(5, 1, 0x1)
    Jump("loc_33A")

    label("loc_316")

    MenuCmd(5, 1, 0x2)
    Jump("loc_33A")

    label("loc_31F")

    MenuCmd(5, 1, 0x3)
    Jump("loc_33A")

    label("loc_328")

    MenuCmd(5, 1, 0x4)
    Jump("loc_33A")

    label("loc_331")

    MenuCmd(5, 1, 0x5)
    Jump("loc_33A")

    label("loc_33A")

    Return()

    # Function_5_2D6 end

    def Function_6_33B(): pass

    label("Function_6_33B")

    MenuCmd(4, 2, 0x3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_3A9"),
        (1, "loc_3B2"),
        (2, "loc_3BB"),
        (3, "loc_3C4"),
        (4, "loc_3CD"),
        (5, "loc_3D6"),
        (6, "loc_3DF"),
        (7, "loc_3E8"),
        (8, "loc_3F1"),
        (9, "loc_3FA"),
        (10, "loc_403"),
        (11, "loc_40C"),
        (12, "loc_415"),
        (13, "loc_41E"),
        (14, "loc_427"),
        (15, "loc_430"),
        (SWITCH_DEFAULT, "loc_439"),
    )


    label("loc_3A9")

    MenuCmd(5, 2, 0x0)
    Jump("loc_439")

    label("loc_3B2")

    MenuCmd(5, 2, 0x1)
    Jump("loc_439")

    label("loc_3BB")

    MenuCmd(5, 2, 0x2)
    Jump("loc_439")

    label("loc_3C4")

    MenuCmd(5, 2, 0x3)
    Jump("loc_439")

    label("loc_3CD")

    MenuCmd(5, 2, 0x4)
    Jump("loc_439")

    label("loc_3D6")

    MenuCmd(5, 2, 0x5)
    Jump("loc_439")

    label("loc_3DF")

    MenuCmd(5, 2, 0x6)
    Jump("loc_439")

    label("loc_3E8")

    MenuCmd(5, 2, 0x7)
    Jump("loc_439")

    label("loc_3F1")

    MenuCmd(5, 2, 0x8)
    Jump("loc_439")

    label("loc_3FA")

    MenuCmd(5, 2, 0x9)
    Jump("loc_439")

    label("loc_403")

    MenuCmd(5, 2, 0xA)
    Jump("loc_439")

    label("loc_40C")

    MenuCmd(5, 2, 0xB)
    Jump("loc_439")

    label("loc_415")

    MenuCmd(5, 2, 0xC)
    Jump("loc_439")

    label("loc_41E")

    MenuCmd(5, 2, 0xD)
    Jump("loc_439")

    label("loc_427")

    MenuCmd(5, 2, 0xE)
    Jump("loc_439")

    label("loc_430")

    MenuCmd(5, 2, 0xF)
    Jump("loc_439")

    label("loc_439")

    MenuEnd(0x3)
    OP_60(0x2)
    Return()

    # Function_6_33B end

    def Function_7_440(): pass

    label("Function_7_440")

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
            "　　　　　战技一览　　",
            scpstr(0x18),
            scpstr(0x6),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    label("loc_4A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1952")
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        1,
        32,
        96,
        1,
        (
            "Ｓ战技①\x01",        # 0
            "Ｓ战技②\x01",        # 1
            "Ｓ战技③\x01",        # 2
            "组合战技①\x01",      # 3
            "组合战技②\x01",      # 4
            "返回\x01",            # 5
        )
    )

    MenuCmd(4, 1, 0x3)
    Call(0, 5)
    MenuEnd(0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_535"),
        (1, "loc_A37"),
        (2, "loc_E13"),
        (3, "loc_118F"),
        (4, "loc_14CF"),
        (SWITCH_DEFAULT, "loc_1934"),
    )


    label("loc_535")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A2F")

    Menu(
        2,
        -1,
        108,
        1,
        (
            "#176I：猛虎冲锋\x01",        # 0
            "#176I：升龙旭日\x01",        # 1
            "#176I：陨星粉碎\x01",        # 2
            "#177I：极光之雨\x01",        # 3
            "#177I：大气能量炮\x01",      # 4
            "#177I：神圣十字波\x01",      # 5
            "#178I：以太爆裂\x01",      # 6
            "#178I：虚无领域\x01",        # 7
            "#178I：星灵装甲\x01",        # 8
            "#179I：赤炎飓风\x01",        # 9
            "#179I：死亡天蝎\x01",        # 10
            "#179I：狂战士\x01",          # 11
            "放弃\x01",                   # 12
        )
    )

    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_639")
    Call(0, 2)
    SetScenarioFlags(0x0, 0)

    label("loc_639")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_68B"),
        (1, "loc_6D7"),
        (2, "loc_723"),
        (3, "loc_76F"),
        (4, "loc_7BB"),
        (5, "loc_807"),
        (6, "loc_853"),
        (7, "loc_89F"),
        (8, "loc_8EB"),
        (9, "loc_937"),
        (10, "loc_983"),
        (11, "loc_9CF"),
        (SWITCH_DEFAULT, "loc_A1B"),
    )


    label("loc_68B")

    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000000, 0x0, 0x0, 0x0, 0x30087200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 0)
    Call(0, 3)
    Jump("loc_A2A")

    label("loc_6D7")

    SetScenarioFlags(0x5C, 1)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000000, 0x0, 0x0, 0x0, 0x30087200, 0x30087200, 0x30087200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 1)
    Call(0, 3)
    Jump("loc_A2A")

    label("loc_723")

    SetScenarioFlags(0x5C, 2)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000000, 0x0, 0x0, 0x0, 0x30087200, 0x30087200, 0x30087200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 2)
    Call(0, 3)
    Jump("loc_A2A")

    label("loc_76F")

    SetScenarioFlags(0x5C, 3)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000100, 0x30000000, 0x30000200, 0x30000300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 3)
    Call(0, 3)
    Jump("loc_A2A")

    label("loc_7BB")

    SetScenarioFlags(0x5C, 4)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000100, 0x0, 0x0, 0x0, 0x30087500, 0x30087500, 0x30087500, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 4)
    Call(0, 3)
    Jump("loc_A2A")

    label("loc_807")

    SetScenarioFlags(0x5C, 5)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000100, 0x0, 0x0, 0x0, 0x30087500, 0x30087500, 0x30087500, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 5)
    Call(0, 3)
    Jump("loc_A2A")

    label("loc_853")

    SetScenarioFlags(0x5C, 6)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000200, 0x0, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 6)
    Call(0, 3)
    Jump("loc_A2A")

    label("loc_89F")

    SetScenarioFlags(0x5C, 7)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000200, 0x30000000, 0x30000100, 0x30000300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 7)
    Call(0, 3)
    Jump("loc_A2A")

    label("loc_8EB")

    SetScenarioFlags(0x5D, 0)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000200, 0x0, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 0)
    Call(0, 3)
    Jump("loc_A2A")

    label("loc_937")

    SetScenarioFlags(0x5D, 1)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000300, 0x0, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 1)
    Call(0, 3)
    Jump("loc_A2A")

    label("loc_983")

    SetScenarioFlags(0x5D, 2)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000300, 0x0, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 2)
    Call(0, 3)
    Jump("loc_A2A")

    label("loc_9CF")

    SetScenarioFlags(0x5D, 3)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000300, 0x0, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 3)
    Call(0, 3)
    Jump("loc_A2A")

    label("loc_A1B")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A2A")

    label("loc_A2A")

    Jump("loc_535")

    label("loc_A2F")

    ClearScenarioFlags(0x0, 0)
    Jump("loc_194D")

    label("loc_A37")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E0B")

    Menu(
        2,
        -1,
        108,
        1,
        (
            "#180I：致命天堂\x01",          # 0
            "#180I：虚空手臂\x01",          # 1
            "#184I：爆击风暴\x01",          # 2
            "#184I：武装军势\x01",          # 3
            "#181I：幻月之舞\x01",          # 4
            "#187I：真·幻月之舞\x01",      # 5
            "#185I：正义之拳\x01",          # 6
            "#185I：正义制裁\x01",          # 7
            "#186I：杀戮驱驰\x01",          # 8
            "放弃\x01",                     # 9
        )
    )

    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B0B")
    Call(0, 2)
    SetScenarioFlags(0x0, 0)

    label("loc_B0B")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_B4B"),
        (1, "loc_B97"),
        (2, "loc_BE3"),
        (3, "loc_C2F"),
        (4, "loc_C7B"),
        (5, "loc_CC7"),
        (6, "loc_D13"),
        (7, "loc_D5F"),
        (8, "loc_DAB"),
        (SWITCH_DEFAULT, "loc_DF7"),
    )


    label("loc_B4B")

    SetScenarioFlags(0x5D, 4)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000400, 0x0, 0x0, 0x0, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 4)
    Call(0, 3)
    Jump("loc_E06")

    label("loc_B97")

    SetScenarioFlags(0x5D, 5)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30003100, 0x0, 0x0, 0x0, 0x30087400, 0x30087400, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 5)
    Call(0, 3)
    Jump("loc_E06")

    label("loc_BE3")

    SetScenarioFlags(0x5D, 6)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000800, 0x0, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 6)
    Call(0, 3)
    Jump("loc_E06")

    label("loc_C2F")

    SetScenarioFlags(0x5D, 7)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000800, 0x0, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 7)
    Call(0, 3)
    Jump("loc_E06")

    label("loc_C7B")

    SetScenarioFlags(0x5E, 0)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000500, 0x0, 0x0, 0x0, 0x30087500, 0x30087500, 0x30087500, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5E, 0)
    Call(0, 3)
    Jump("loc_E06")

    label("loc_CC7")

    SetScenarioFlags(0x5E, 1)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30003200, 0x0, 0x0, 0x0, 0x30087500, 0x30087500, 0x30087500, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5E, 1)
    Call(0, 3)
    Jump("loc_E06")

    label("loc_D13")

    SetScenarioFlags(0x5E, 2)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000900, 0x0, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5E, 2)
    Call(0, 3)
    Jump("loc_E06")

    label("loc_D5F")

    SetScenarioFlags(0x5E, 3)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30000900, 0x0, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5E, 3)
    Call(0, 3)
    Jump("loc_E06")

    label("loc_DAB")

    SetScenarioFlags(0x5E, 4)
    Battle(0xFFFFFFFF, 0x30200100, "", 0x30004100, 0x0, 0x0, 0x0, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5E, 4)
    Call(0, 3)
    Jump("loc_E06")

    label("loc_DF7")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E06")

    label("loc_E06")

    Jump("loc_A37")

    label("loc_E0B")

    ClearScenarioFlags(0x0, 0)
    Jump("loc_194D")

    label("loc_E13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1187")

    Menu(
        2,
        -1,
        108,
        1,
        (
            "#183I：风神烈破\x01",            # 0
            "#183I：终之太刀-黑皇-\x01",      # 1
            "#190I：死亡巡游\x01",            # 2
            "#207I：深红陨落\x01",            # 3
            "#189I：伪·盐之桩\x01",          # 4
            "#188I：圣技·大十字\x01",        # 5
            "#191I：真红剑斩\x01",            # 6
            "#191I：快乐城堡\x01",            # 7
            "放弃\x01",                       # 8
        )
    )

    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EDF")
    Call(0, 2)
    SetScenarioFlags(0x0, 0)

    label("loc_EDF")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_F19"),
        (1, "loc_F65"),
        (2, "loc_FB1"),
        (3, "loc_FFD"),
        (4, "loc_1049"),
        (5, "loc_1095"),
        (6, "loc_10E1"),
        (7, "loc_112D"),
        (SWITCH_DEFAULT, "loc_1173"),
    )


    label("loc_F19")

    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30002400, 0x0, 0x0, 0x0, 0x30087400, 0x30087400, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 0)
    Call(0, 3)
    Jump("loc_1182")

    label("loc_F65")

    SetScenarioFlags(0x5C, 1)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30002400, 0x0, 0x0, 0x0, 0x30087400, 0x30087400, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 1)
    Call(0, 3)
    Jump("loc_1182")

    label("loc_FB1")

    SetScenarioFlags(0x5C, 2)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30003400, 0x0, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 2)
    Call(0, 3)
    Jump("loc_1182")

    label("loc_FFD")

    SetScenarioFlags(0x5C, 3)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30003300, 0x0, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 3)
    Call(0, 3)
    Jump("loc_1182")

    label("loc_1049")

    SetScenarioFlags(0x5C, 4)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30003600, 0x0, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 4)
    Call(0, 3)
    Jump("loc_1182")

    label("loc_1095")

    SetScenarioFlags(0x5C, 5)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30004200, 0x0, 0x0, 0x0, 0x30087200, 0x30087200, 0x30087200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 5)
    Call(0, 3)
    Jump("loc_1182")

    label("loc_10E1")

    SetScenarioFlags(0x5C, 6)
    Battle(0xFFFFFFFF, 0x30200101, "", 0x30003700, 0x0, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 6)
    Call(0, 3)
    Jump("loc_1182")

    label("loc_112D")

    Battle(0xFFFFFFFF, 0x30200101, "", 0x30003700, 0x0, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    Call(0, 3)
    Jump("loc_1182")

    label("loc_1173")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1182")

    label("loc_1182")

    Jump("loc_E13")

    label("loc_1187")

    ClearScenarioFlags(0x0, 0)
    Jump("loc_194D")

    label("loc_118F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14C7")

    Menu(
        2,
        -1,
        108,
        1,
        (
            "#176I#177I：星辰爆击\x01",        # 0
            "#176I#178I：Ω强袭\x01",          # 1
            "#176I#179I：燃烧之怒\x01",        # 2
            "#176I#184I：勇猛之心\x01",        # 3
            "#176I#180I：袭空天堂\x01",        # 4
            "#176I#187I：比翼双龙击\x01",      # 5
            "#176I#185I：钢铁雄心\x01",        # 6
            "放弃\x01",                        # 7
        )
    )

    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1262")
    Call(0, 2)
    SetScenarioFlags(0x0, 0)

    label("loc_1262")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1296"),
        (1, "loc_12E2"),
        (2, "loc_132E"),
        (3, "loc_137A"),
        (4, "loc_13C6"),
        (5, "loc_1412"),
        (6, "loc_146C"),
        (SWITCH_DEFAULT, "loc_14B8"),
    )


    label("loc_1296")

    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30000100, 0x0, 0x0, 0x30087500, 0x30087500, 0x30087500, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 0)
    Call(0, 3)
    Jump("loc_14C2")

    label("loc_12E2")

    SetScenarioFlags(0x5C, 1)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30000200, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 1)
    Call(0, 3)
    Jump("loc_14C2")

    label("loc_132E")

    SetScenarioFlags(0x5C, 2)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30000300, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 2)
    Call(0, 3)
    Jump("loc_14C2")

    label("loc_137A")

    SetScenarioFlags(0x5C, 3)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30000800, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 3)
    Call(0, 3)
    Jump("loc_14C2")

    label("loc_13C6")

    SetScenarioFlags(0x5C, 4)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30000400, 0x0, 0x0, 0x30087400, 0x30087400, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 4)
    Call(0, 3)
    Jump("loc_14C2")

    label("loc_1412")

    SetScenarioFlags(0x5C, 5)
    SetChrChipPat(0x5, 0x1, 0x20)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30003200, 0x0, 0x0, 0x30087200, 0x30087200, 0x30087200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    SetChrChipPat(0x5, 0x1, 0x5)
    ClearScenarioFlags(0x5C, 5)
    Call(0, 3)
    Jump("loc_14C2")

    label("loc_146C")

    SetScenarioFlags(0x5C, 6)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000000, 0x30000900, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 6)
    Call(0, 3)
    Jump("loc_14C2")

    label("loc_14B8")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14C2")

    Jump("loc_118F")

    label("loc_14C7")

    ClearScenarioFlags(0x0, 0)
    Jump("loc_194D")

    label("loc_14CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_192C")

    Menu(
        2,
        -1,
        108,
        1,
        (
            "#177I#178I：冷酷冰狱\x01",      # 0
            "#177I#179I：肆虐之星\x01",      # 1
            "#177I#184I：南十字星\x01",      # 2
            "#177I#180I：虚空之星\x01",      # 3
            "#178I#179I：钩刃风暴\x01",      # 4
            "#178I#184I：爆炸重炮\x01",      # 5
            "#178I#180I：Σ升天\x01",        # 6
            "#179I#184I：联合轰鸣\x01",      # 7
            "#179I#180I：最终反击\x01",      # 8
            "#180I#184I：苍蓝冲破\x01",      # 9
            "放弃\x01",                      # 10
        )
    )

    Call(0, 6)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15DF")
    Call(0, 2)
    SetScenarioFlags(0x0, 0)

    label("loc_15DF")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1625"),
        (1, "loc_1671"),
        (2, "loc_16BD"),
        (3, "loc_1709"),
        (4, "loc_1755"),
        (5, "loc_17A1"),
        (6, "loc_17ED"),
        (7, "loc_1839"),
        (8, "loc_1885"),
        (9, "loc_18D1"),
        (SWITCH_DEFAULT, "loc_191D"),
    )


    label("loc_1625")

    SetScenarioFlags(0x5C, 7)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000100, 0x30000200, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5C, 7)
    Call(0, 3)
    Jump("loc_1927")

    label("loc_1671")

    SetScenarioFlags(0x5D, 0)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000100, 0x30000300, 0x0, 0x0, 0x30087500, 0x30087500, 0x30087500, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 0)
    Call(0, 3)
    Jump("loc_1927")

    label("loc_16BD")

    SetScenarioFlags(0x5D, 1)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000100, 0x30000800, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 1)
    Call(0, 3)
    Jump("loc_1927")

    label("loc_1709")

    SetScenarioFlags(0x5D, 2)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000100, 0x30000400, 0x0, 0x0, 0x30087400, 0x30087400, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 2)
    Call(0, 3)
    Jump("loc_1927")

    label("loc_1755")

    SetScenarioFlags(0x5D, 3)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000200, 0x30000300, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 3)
    Call(0, 3)
    Jump("loc_1927")

    label("loc_17A1")

    SetScenarioFlags(0x5D, 4)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000200, 0x30000800, 0x0, 0x0, 0x30087100, 0x30087100, 0x30087100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 4)
    Call(0, 3)
    Jump("loc_1927")

    label("loc_17ED")

    SetScenarioFlags(0x5D, 5)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000200, 0x30000400, 0x0, 0x0, 0x30087200, 0x30087200, 0x30087200, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 5)
    Call(0, 3)
    Jump("loc_1927")

    label("loc_1839")

    SetScenarioFlags(0x5D, 6)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000300, 0x30000800, 0x0, 0x0, 0x30087300, 0x30087300, 0x30087300, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 6)
    Call(0, 3)
    Jump("loc_1927")

    label("loc_1885")

    SetScenarioFlags(0x5D, 7)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000300, 0x30000400, 0x0, 0x0, 0x30087400, 0x30087400, 0x30087400, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5D, 7)
    Call(0, 3)
    Jump("loc_1927")

    label("loc_18D1")

    SetScenarioFlags(0x5E, 0)
    Battle(0xFFFFFFFF, 0x30200200, "", 0x30000400, 0x30000800, 0x0, 0x0, 0x30087000, 0x30087000, 0x30087000, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1C2, 0x8)
    ClearScenarioFlags(0x5E, 0)
    Call(0, 3)
    Jump("loc_1927")

    label("loc_191D")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1927")

    Jump("loc_14CF")

    label("loc_192C")

    ClearScenarioFlags(0x0, 0)
    Jump("loc_194D")

    label("loc_1934")

    FadeToBright(300, 0)
    OP_0D()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_194D")

    label("loc_194D")

    Jump("loc_4A0")

    label("loc_1952")

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

    # Function_7_440 end

    SaveToFile()

Try(main)
