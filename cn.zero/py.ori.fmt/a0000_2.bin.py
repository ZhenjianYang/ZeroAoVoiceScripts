from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "a0000_2.bin",                # FileName
        "map1",                    # MapName
        "map1",                    # Location
        0x0001,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [324, 621, 916, 1121, 1471, 1595, 1755, 1894, 2051, 0, 2277, 0, 2323, 2516, 2688, 2824, 0, 2963, 0, 48, 12, 0, 0],
    )

    BuildStringList((
        "a0000_2",                # 0
    ))

    ScpFunction((
        "Function_0_144",          # 00, 0
        "Function_1_26D",          # 01, 1
        "Function_2_394",          # 02, 2
        "Function_3_461",          # 03, 3
        "Function_4_5BF",          # 04, 4
        "Function_5_63B",          # 05, 5
        "Function_6_6DB",          # 06, 6
        "Function_7_766",          # 07, 7
        "Function_8_803",          # 08, 8
        "Function_9_8E5",          # 09, 9
        "Function_10_913",         # 0A, 10
        "Function_11_9D4",         # 0B, 11
        "Function_12_A80",         # 0C, 12
        "Function_13_B08",         # 0D, 13
        "Function_14_B93",         # 0E, 14
        "Function_15_C30",         # 0F, 15
        "Function_16_D15",         # 10, 16
        "Function_17_D43",         # 11, 17
        "Function_18_DFB",         # 12, 18
        "Function_19_EA7",         # 13, 19
        "Function_20_1270",        # 14, 20
        "Function_21_168B",        # 15, 21
        "Function_22_1892",        # 16, 22
        "Function_23_1BED",        # 17, 23
        "Function_24_1FBF",        # 18, 24
        "Function_25_23A4",        # 19, 25
        "Function_26_2745",        # 1A, 26
        "Function_27_2B30",        # 1B, 27
        "Function_28_2F39",        # 1C, 28
        "Function_29_3324",        # 1D, 29
        "Function_30_3785",        # 1E, 30
        "Function_31_3BDD",        # 1F, 31
        "Function_32_3C83",        # 20, 32
        "Function_33_40F0",        # 21, 33
        "Function_34_450A",        # 22, 34
        "Function_35_45B0",        # 23, 35
        "Function_36_4942",        # 24, 36
        "Function_37_4CB8",        # 25, 37
        "Function_38_5067",        # 26, 38
        "Function_39_54B4",        # 27, 39
        "Function_40_586D",        # 28, 40
        "Function_41_5CA3",        # 29, 41
        "Function_42_606D",        # 2A, 42
        "Function_43_6471",        # 2B, 43
        "Function_44_6667",        # 2C, 44
        "Function_45_6840",        # 2D, 45
        "Function_46_6AA6",        # 2E, 46
        "Function_47_6CC9",        # 2F, 47
        "Function_48_6F93",        # 30, 48
        "Function_49_7255",        # 31, 49
        "Function_50_74ED",        # 32, 50
        "Function_51_768E",        # 33, 51
        "Function_52_77A9",        # 34, 52
        "Function_53_7894",        # 35, 53
        "Function_54_797F",        # 36, 54
        "Function_55_B808",        # 37, 55
        "Function_56_D785",        # 38, 56
        "Function_57_EDA4",        # 39, 57
        "Function_58_11DAC",       # 3A, 58
        "Function_59_125B8",       # 3B, 59
    ))


    def Function_0_144(): pass

    label("Function_0_144")

    Call(2, 4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_151")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25F")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼０章①\x01",        # 0
            "▼０章②\x01",        # 1
            "▼０章③\x01",        # 2
            "▼１章①\x01",        # 3
            "▼１章②\x01",        # 4
            "▼１章③\x01",        # 5
            "▼２章①\x01",        # 6
            "▼２章②\x01",        # 7
            "▼２章③\x01",        # 8
            "キャンセル\x01",      # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_208"),
        (1, "loc_210"),
        (2, "loc_218"),
        (3, "loc_220"),
        (4, "loc_228"),
        (5, "loc_230"),
        (6, "loc_238"),
        (7, "loc_240"),
        (8, "loc_248"),
        (SWITCH_DEFAULT, "loc_250"),
    )


    label("loc_208")

    Call(2, 19)
    Jump("loc_25A")

    label("loc_210")

    Call(2, 20)
    Jump("loc_25A")

    label("loc_218")

    Call(2, 21)
    Jump("loc_25A")

    label("loc_220")

    Call(2, 22)
    Jump("loc_25A")

    label("loc_228")

    Call(2, 23)
    Jump("loc_25A")

    label("loc_230")

    Call(2, 24)
    Jump("loc_25A")

    label("loc_238")

    Call(2, 25)
    Jump("loc_25A")

    label("loc_240")

    Call(2, 26)
    Jump("loc_25A")

    label("loc_248")

    Call(2, 27)
    Jump("loc_25A")

    label("loc_250")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25A")

    Jump("loc_151")

    label("loc_25F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_0_144 end

    def Function_1_26D(): pass

    label("Function_1_26D")

    Call(2, 4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_386")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼３章①\x01",        # 0
            "▼３章②\x01",        # 1
            "▼３章③\x01",        # 2
            "▼３章④\x01",        # 3
            "▼３章⑤\x01",        # 4
            "▼幕間\x01",          # 5
            "▼４章①\x01",        # 6
            "▼４章②\x01",        # 7
            "▼４章③\x01",        # 8
            "キャンセル\x01",      # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_32F"),
        (1, "loc_337"),
        (2, "loc_33F"),
        (3, "loc_347"),
        (4, "loc_34F"),
        (5, "loc_357"),
        (6, "loc_35F"),
        (7, "loc_367"),
        (8, "loc_36F"),
        (SWITCH_DEFAULT, "loc_377"),
    )


    label("loc_32F")

    Call(2, 28)
    Jump("loc_381")

    label("loc_337")

    Call(2, 29)
    Jump("loc_381")

    label("loc_33F")

    Call(2, 30)
    Jump("loc_381")

    label("loc_347")

    Call(2, 32)
    Jump("loc_381")

    label("loc_34F")

    Call(2, 33)
    Jump("loc_381")

    label("loc_357")

    Call(2, 35)
    Jump("loc_381")

    label("loc_35F")

    Call(2, 36)
    Jump("loc_381")

    label("loc_367")

    Call(2, 37)
    Jump("loc_381")

    label("loc_36F")

    Call(2, 38)
    Jump("loc_381")

    label("loc_377")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_381")

    Jump("loc_27A")

    label("loc_386")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_1_26D end

    def Function_2_394(): pass

    label("Function_2_394")

    Call(2, 4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3A1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_453")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼５章①\x01",        # 0
            "▼５章②\x01",        # 1
            "▼５章③\x01",        # 2
            "▼５章④\x01",        # 3
            "▼５章⑤\x01",        # 4
            "キャンセル\x01",      # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_41C"),
        (1, "loc_424"),
        (2, "loc_42C"),
        (3, "loc_434"),
        (4, "loc_43C"),
        (SWITCH_DEFAULT, "loc_444"),
    )


    label("loc_41C")

    Call(2, 39)
    Jump("loc_44E")

    label("loc_424")

    Call(2, 40)
    Jump("loc_44E")

    label("loc_42C")

    Call(2, 41)
    Jump("loc_44E")

    label("loc_434")

    Call(2, 42)
    Jump("loc_44E")

    label("loc_43C")

    Call(2, 43)
    Jump("loc_44E")

    label("loc_444")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_44E")

    Jump("loc_3A1")

    label("loc_453")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_2_394 end

    def Function_3_461(): pass

    label("Function_3_461")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_46B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B1")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼序章\x01",                  # 0
            "▼１章\x01",                  # 1
            "▼２章\x01",                  # 2
            "▼３章①\x01",                # 3
            "▼３章②＆幕間\x01",          # 4
            "▼４章\x01",                  # 5
            "▼終章\x01",                  # 6
            "絆ポイント弄\x01",            # 7
            "オークションのお供\x01",      # 8
            "幕間のお供\x01",              # 9
            "キャンセル\x01",              # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_53D"),
        (1, "loc_548"),
        (2, "loc_553"),
        (3, "loc_55E"),
        (4, "loc_569"),
        (5, "loc_574"),
        (6, "loc_57F"),
        (7, "loc_58A"),
        (8, "loc_592"),
        (9, "loc_59A"),
        (SWITCH_DEFAULT, "loc_5A2"),
    )


    label("loc_53D")

    Call(2, 4)
    Call(2, 44)
    Jump("loc_5AC")

    label("loc_548")

    Call(2, 4)
    Call(2, 45)
    Jump("loc_5AC")

    label("loc_553")

    Call(2, 4)
    Call(2, 46)
    Jump("loc_5AC")

    label("loc_55E")

    Call(2, 4)
    Call(2, 47)
    Jump("loc_5AC")

    label("loc_569")

    Call(2, 4)
    Call(2, 48)
    Jump("loc_5AC")

    label("loc_574")

    Call(2, 4)
    Call(2, 49)
    Jump("loc_5AC")

    label("loc_57F")

    Call(2, 4)
    Call(2, 50)
    Jump("loc_5AC")

    label("loc_58A")

    Call(2, 51)
    Jump("loc_5AC")

    label("loc_592")

    Call(2, 52)
    Jump("loc_5AC")

    label("loc_59A")

    Call(2, 53)
    Jump("loc_5AC")

    label("loc_5A2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5AC")

    Jump("loc_46B")

    label("loc_5B1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_3_461 end

    def Function_4_5BF(): pass

    label("Function_4_5BF")

    ClearScenarioFlags(0x5C, 0)
    ClearScenarioFlags(0x5C, 1)
    ClearScenarioFlags(0x5C, 2)
    ClearScenarioFlags(0x5C, 3)
    ClearScenarioFlags(0x5C, 4)
    ClearScenarioFlags(0x5C, 5)
    ClearScenarioFlags(0x5C, 6)
    ClearScenarioFlags(0x5C, 7)
    ClearScenarioFlags(0x5D, 1)
    ClearScenarioFlags(0x5D, 2)
    ClearScenarioFlags(0x5D, 3)
    ClearScenarioFlags(0x5D, 4)
    ClearScenarioFlags(0x5D, 5)
    ClearScenarioFlags(0x5D, 6)
    ClearScenarioFlags(0x5D, 7)
    ClearScenarioFlags(0x5E, 0)
    ClearScenarioFlags(0x5E, 1)
    ClearScenarioFlags(0x5E, 2)
    ClearScenarioFlags(0x5E, 3)
    ClearScenarioFlags(0x5E, 4)
    ClearScenarioFlags(0x5E, 5)
    ClearScenarioFlags(0x5E, 6)
    ClearScenarioFlags(0x5E, 7)
    ClearScenarioFlags(0x5F, 0)
    ClearScenarioFlags(0x5F, 1)
    Call(2, 12)
    Call(2, 13)
    Call(2, 14)
    Call(2, 15)
    Call(2, 16)
    Call(2, 17)
    Call(2, 18)
    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_4_5BF end

    def Function_5_63B(): pass

    label("Function_5_63B")

    SetScenarioFlags(0x40, 0)
    SetScenarioFlags(0x40, 1)
    SetScenarioFlags(0x40, 2)
    SetScenarioFlags(0x40, 3)
    SetScenarioFlags(0x40, 4)
    SetScenarioFlags(0x40, 5)
    SetScenarioFlags(0x40, 6)
    SetScenarioFlags(0x40, 7)
    SetScenarioFlags(0x41, 0)
    SetScenarioFlags(0x41, 1)
    SetScenarioFlags(0x41, 2)
    SetScenarioFlags(0x41, 3)
    SetScenarioFlags(0x41, 4)
    SetScenarioFlags(0x41, 5)
    OP_29(0x1, 0x4, 0x2)
    OP_29(0x1, 0x4, 0x10)
    OP_29(0x1, 0x4, 0x20)
    SetScenarioFlags(0x41, 6)
    SetScenarioFlags(0x41, 7)
    SetScenarioFlags(0x42, 0)
    SetScenarioFlags(0x42, 1)
    SetScenarioFlags(0x42, 2)
    SetScenarioFlags(0x42, 3)
    SetScenarioFlags(0x42, 4)
    SetScenarioFlags(0x42, 5)
    SetScenarioFlags(0x42, 6)
    SetScenarioFlags(0x42, 7)
    SetScenarioFlags(0x43, 0)
    SetScenarioFlags(0x43, 1)
    SetScenarioFlags(0x43, 2)
    SetScenarioFlags(0x44, 0)
    SetScenarioFlags(0x44, 1)
    SetScenarioFlags(0x44, 2)
    SetScenarioFlags(0x44, 4)
    SetScenarioFlags(0x44, 5)
    SetScenarioFlags(0x44, 6)
    SetScenarioFlags(0x44, 7)
    SetScenarioFlags(0x45, 0)
    SetScenarioFlags(0x45, 1)
    SetScenarioFlags(0x45, 2)
    SetScenarioFlags(0x45, 3)
    SetScenarioFlags(0x47, 3)
    SetScenarioFlags(0x47, 4)
    SetScenarioFlags(0x45, 5)
    SetScenarioFlags(0x45, 6)
    SetScenarioFlags(0x45, 7)
    SetScenarioFlags(0x46, 0)
    SetScenarioFlags(0x47, 5)
    SetScenarioFlags(0x4C, 1)
    SetScenarioFlags(0x46, 1)
    SetScenarioFlags(0x4C, 2)
    Return()

    # Function_5_63B end

    def Function_6_6DB(): pass

    label("Function_6_6DB")

    SetScenarioFlags(0x60, 0)
    SetScenarioFlags(0x60, 1)
    SetScenarioFlags(0x60, 2)
    SetScenarioFlags(0x60, 3)
    SetScenarioFlags(0x60, 4)
    SetScenarioFlags(0x60, 5)
    SetScenarioFlags(0x60, 6)
    SetScenarioFlags(0x60, 7)
    SetScenarioFlags(0x61, 0)
    SetScenarioFlags(0x61, 1)
    SetScenarioFlags(0x61, 2)
    SetScenarioFlags(0x61, 3)
    SetScenarioFlags(0x61, 4)
    SetScenarioFlags(0x61, 5)
    SetScenarioFlags(0x61, 6)
    SetScenarioFlags(0x61, 7)
    SetScenarioFlags(0x62, 0)
    SetScenarioFlags(0x62, 1)
    SetScenarioFlags(0x62, 2)
    SetScenarioFlags(0x62, 3)
    SetScenarioFlags(0x62, 4)
    SetScenarioFlags(0x62, 5)
    SetScenarioFlags(0x62, 6)
    SetScenarioFlags(0x62, 7)
    SetScenarioFlags(0x63, 0)
    SetScenarioFlags(0x63, 1)
    SetScenarioFlags(0x63, 2)
    SetScenarioFlags(0x63, 3)
    SetScenarioFlags(0x63, 4)
    SetScenarioFlags(0x63, 5)
    SetScenarioFlags(0x63, 6)
    SetScenarioFlags(0x63, 7)
    SetScenarioFlags(0x64, 0)
    SetScenarioFlags(0x64, 1)
    SetScenarioFlags(0x64, 2)
    SetScenarioFlags(0x64, 3)
    SetScenarioFlags(0x64, 4)
    SetScenarioFlags(0x64, 5)
    SetScenarioFlags(0x64, 6)
    SetScenarioFlags(0x64, 7)
    SetScenarioFlags(0x65, 0)
    SetScenarioFlags(0x65, 1)
    SetScenarioFlags(0x65, 2)
    SetScenarioFlags(0x65, 3)
    SetScenarioFlags(0x65, 4)
    SetScenarioFlags(0x65, 5)
    Return()

    # Function_6_6DB end

    def Function_7_766(): pass

    label("Function_7_766")

    SetScenarioFlags(0x80, 0)
    SetScenarioFlags(0x80, 1)
    SetScenarioFlags(0x80, 2)
    SetScenarioFlags(0x80, 3)
    SetScenarioFlags(0x80, 4)
    SetScenarioFlags(0x80, 5)
    SetScenarioFlags(0x80, 6)
    SetScenarioFlags(0x80, 7)
    SetScenarioFlags(0x81, 0)
    SetScenarioFlags(0x81, 1)
    SetScenarioFlags(0x81, 2)
    SetScenarioFlags(0x81, 3)
    SetScenarioFlags(0x81, 4)
    SetScenarioFlags(0x81, 5)
    SetScenarioFlags(0x81, 6)
    SetScenarioFlags(0x81, 7)
    SetScenarioFlags(0x82, 0)
    SetScenarioFlags(0x82, 1)
    SetScenarioFlags(0x82, 2)
    SetScenarioFlags(0x82, 3)
    SetScenarioFlags(0x82, 4)
    SetScenarioFlags(0x82, 5)
    SetScenarioFlags(0x82, 6)
    SetScenarioFlags(0x82, 7)
    SetScenarioFlags(0x83, 0)
    SetScenarioFlags(0x83, 1)
    SetScenarioFlags(0x83, 2)
    SetScenarioFlags(0x83, 3)
    SetScenarioFlags(0x83, 4)
    SetScenarioFlags(0x83, 5)
    SetScenarioFlags(0x83, 6)
    SetScenarioFlags(0x83, 7)
    SetScenarioFlags(0x84, 0)
    SetScenarioFlags(0x84, 1)
    SetScenarioFlags(0x84, 2)
    SetScenarioFlags(0x84, 3)
    SetScenarioFlags(0x84, 4)
    SetScenarioFlags(0x84, 5)
    SetScenarioFlags(0x84, 6)
    SetScenarioFlags(0x84, 7)
    SetScenarioFlags(0x85, 0)
    SetScenarioFlags(0x85, 1)
    SetScenarioFlags(0x85, 2)
    SetScenarioFlags(0x85, 3)
    SetScenarioFlags(0x85, 4)
    SetScenarioFlags(0x85, 5)
    SetScenarioFlags(0x85, 6)
    SetScenarioFlags(0x85, 7)
    SetScenarioFlags(0x86, 0)
    SetScenarioFlags(0x86, 1)
    SetScenarioFlags(0x87, 3)
    SetScenarioFlags(0x87, 5)
    Return()

    # Function_7_766 end

    def Function_8_803(): pass

    label("Function_8_803")

    SetScenarioFlags(0xA0, 0)
    SetScenarioFlags(0xA0, 1)
    SetScenarioFlags(0xA0, 2)
    SetScenarioFlags(0xA0, 3)
    SetScenarioFlags(0xA0, 4)
    SetScenarioFlags(0xA0, 5)
    SetScenarioFlags(0xA0, 6)
    SetScenarioFlags(0xA0, 7)
    SetScenarioFlags(0xA1, 0)
    SetScenarioFlags(0xA1, 1)
    SetScenarioFlags(0xA1, 2)
    SetScenarioFlags(0xA1, 3)
    SetScenarioFlags(0xA1, 4)
    SetScenarioFlags(0xA1, 5)
    SetScenarioFlags(0xA1, 6)
    SetScenarioFlags(0xA1, 7)
    SetScenarioFlags(0xB9, 3)
    SetScenarioFlags(0xA2, 0)
    SetScenarioFlags(0xB9, 4)
    SetScenarioFlags(0xA2, 1)
    SetScenarioFlags(0xA2, 2)
    SetScenarioFlags(0xA2, 3)
    SetScenarioFlags(0xB9, 5)
    SetScenarioFlags(0xA2, 4)
    SetScenarioFlags(0xA2, 5)
    SetScenarioFlags(0xAC, 5)
    SetScenarioFlags(0xAC, 6)
    SetScenarioFlags(0xB9, 6)
    SetScenarioFlags(0xA2, 6)
    SetScenarioFlags(0xB9, 7)
    SetScenarioFlags(0xA2, 7)
    SetScenarioFlags(0xA3, 0)
    SetScenarioFlags(0xA3, 1)
    SetScenarioFlags(0xA3, 2)
    SetScenarioFlags(0xA3, 3)
    SetScenarioFlags(0xA3, 4)
    SetScenarioFlags(0xA3, 5)
    SetScenarioFlags(0xA3, 6)
    SetScenarioFlags(0xA3, 7)
    SetScenarioFlags(0xA4, 0)
    SetScenarioFlags(0xA4, 1)
    SetScenarioFlags(0xA4, 2)
    SetScenarioFlags(0xA4, 3)
    SetScenarioFlags(0xA4, 4)
    SetScenarioFlags(0xA4, 5)
    SetScenarioFlags(0xA4, 6)
    SetScenarioFlags(0xA4, 7)
    SetScenarioFlags(0xA5, 0)
    SetScenarioFlags(0xA5, 1)
    SetScenarioFlags(0xA5, 2)
    SetScenarioFlags(0xA5, 3)
    SetScenarioFlags(0xA5, 4)
    SetScenarioFlags(0xA5, 5)
    SetScenarioFlags(0xA5, 6)
    SetScenarioFlags(0xA5, 7)
    SetScenarioFlags(0xA6, 0)
    SetScenarioFlags(0xA6, 1)
    SetScenarioFlags(0xA6, 2)
    SetScenarioFlags(0xA6, 3)
    SetScenarioFlags(0xA6, 4)
    SetScenarioFlags(0xA6, 5)
    SetScenarioFlags(0xA6, 6)
    SetScenarioFlags(0xA6, 7)
    SetScenarioFlags(0xA7, 0)
    SetScenarioFlags(0xA7, 1)
    SetScenarioFlags(0xA7, 2)
    SetScenarioFlags(0xA7, 3)
    SetScenarioFlags(0xA7, 4)
    SetScenarioFlags(0xA7, 5)
    SetScenarioFlags(0xA9, 1)
    SetScenarioFlags(0xA9, 2)
    SetScenarioFlags(0xA9, 3)
    SetScenarioFlags(0xAA, 0)
    SetScenarioFlags(0xAA, 1)
    SetScenarioFlags(0xAA, 2)
    Return()

    # Function_8_803 end

    def Function_9_8E5(): pass

    label("Function_9_8E5")

    SetScenarioFlags(0xA7, 6)
    SetScenarioFlags(0xA7, 7)
    SetScenarioFlags(0xA8, 0)
    SetScenarioFlags(0xA8, 1)
    SetScenarioFlags(0xA8, 2)
    SetScenarioFlags(0xA8, 3)
    SetScenarioFlags(0xA8, 4)
    SetScenarioFlags(0xA8, 5)
    SetScenarioFlags(0xA8, 6)
    SetScenarioFlags(0xA8, 7)
    SetScenarioFlags(0xA9, 0)
    SetScenarioFlags(0xA9, 4)
    SetScenarioFlags(0xA9, 5)
    SetScenarioFlags(0xA9, 6)
    SetScenarioFlags(0xA9, 7)
    Return()

    # Function_9_8E5 end

    def Function_10_913(): pass

    label("Function_10_913")

    SetScenarioFlags(0xC0, 0)
    SetScenarioFlags(0xC0, 1)
    SetScenarioFlags(0xC0, 2)
    SetScenarioFlags(0xC0, 3)
    SetScenarioFlags(0xC0, 4)
    SetScenarioFlags(0xC0, 5)
    SetScenarioFlags(0xC0, 6)
    SetScenarioFlags(0xC0, 7)
    SetScenarioFlags(0xC1, 0)
    SetScenarioFlags(0xC1, 1)
    SetScenarioFlags(0xC1, 2)
    SetScenarioFlags(0xC1, 3)
    SetScenarioFlags(0xC1, 4)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xC1, 5)
    SetScenarioFlags(0xC1, 6)
    SetScenarioFlags(0xC1, 7)
    SetScenarioFlags(0xC2, 0)
    SetScenarioFlags(0xC2, 1)
    SetScenarioFlags(0xC2, 2)
    SetScenarioFlags(0xC2, 3)
    SetScenarioFlags(0xC2, 4)
    SetScenarioFlags(0xC2, 5)
    SetScenarioFlags(0xC2, 6)
    SetScenarioFlags(0xC2, 7)
    SetScenarioFlags(0xC3, 0)
    SetScenarioFlags(0xC3, 1)
    SetScenarioFlags(0xC3, 2)
    SetScenarioFlags(0xC3, 3)
    SetScenarioFlags(0xC3, 4)
    SetScenarioFlags(0xC3, 5)
    SetScenarioFlags(0xC3, 6)
    SetScenarioFlags(0xC3, 7)
    SetScenarioFlags(0xC4, 0)
    SetScenarioFlags(0xC4, 1)
    SetScenarioFlags(0xC4, 2)
    SetScenarioFlags(0xC4, 3)
    SetScenarioFlags(0xC4, 4)
    SetScenarioFlags(0xC4, 5)
    SetScenarioFlags(0xC4, 6)
    SetScenarioFlags(0xC4, 7)
    SetScenarioFlags(0xC5, 0)
    SetScenarioFlags(0xC5, 1)
    SetScenarioFlags(0xC5, 2)
    SetScenarioFlags(0xC5, 3)
    SetScenarioFlags(0xC6, 5)
    SetScenarioFlags(0xC5, 4)
    SetScenarioFlags(0xC5, 5)
    SetScenarioFlags(0xC5, 6)
    SetScenarioFlags(0xC5, 7)
    SetScenarioFlags(0xC6, 0)
    SetScenarioFlags(0xC6, 1)
    SetScenarioFlags(0xC6, 2)
    SetScenarioFlags(0xC6, 3)
    SetScenarioFlags(0xC6, 4)
    SetScenarioFlags(0xC6, 6)
    SetScenarioFlags(0xC6, 7)
    SetScenarioFlags(0xC8, 0)
    SetScenarioFlags(0xC8, 1)
    SetScenarioFlags(0xC8, 2)
    SetScenarioFlags(0xC8, 3)
    SetScenarioFlags(0xC8, 4)
    Return()

    # Function_10_913 end

    def Function_11_9D4(): pass

    label("Function_11_9D4")

    SetScenarioFlags(0xE0, 0)
    SetScenarioFlags(0xE0, 1)
    SetScenarioFlags(0xE0, 2)
    SetScenarioFlags(0xE0, 3)
    SetScenarioFlags(0xE0, 4)
    SetScenarioFlags(0xE0, 5)
    SetScenarioFlags(0xE0, 6)
    SetScenarioFlags(0xE0, 7)
    SetScenarioFlags(0xE1, 0)
    SetScenarioFlags(0xE1, 1)
    SetScenarioFlags(0xE1, 2)
    SetScenarioFlags(0xE1, 3)
    SetScenarioFlags(0xE1, 4)
    SetScenarioFlags(0xE1, 5)
    SetScenarioFlags(0xE1, 6)
    SetScenarioFlags(0xE1, 7)
    SetScenarioFlags(0xE2, 0)
    SetScenarioFlags(0xE2, 1)
    SetScenarioFlags(0xE2, 2)
    SetScenarioFlags(0xE2, 3)
    SetScenarioFlags(0xE2, 4)
    SetScenarioFlags(0xE2, 5)
    SetScenarioFlags(0xE2, 6)
    SetScenarioFlags(0xE2, 7)
    SetScenarioFlags(0xE3, 0)
    SetScenarioFlags(0xE3, 1)
    SetScenarioFlags(0xE3, 2)
    SetScenarioFlags(0xE3, 3)
    SetScenarioFlags(0xE3, 4)
    SetScenarioFlags(0xE3, 5)
    SetScenarioFlags(0xE3, 6)
    SetScenarioFlags(0xE3, 7)
    SetScenarioFlags(0xE4, 0)
    SetScenarioFlags(0xE4, 1)
    SetScenarioFlags(0xE4, 2)
    SetScenarioFlags(0xE4, 3)
    SetScenarioFlags(0xE4, 4)
    SetScenarioFlags(0xE7, 5)
    SetScenarioFlags(0xE4, 5)
    SetScenarioFlags(0xE4, 6)
    SetScenarioFlags(0xE4, 7)
    SetScenarioFlags(0xE5, 0)
    SetScenarioFlags(0xE5, 1)
    SetScenarioFlags(0xE5, 2)
    SetScenarioFlags(0xE5, 3)
    SetScenarioFlags(0xE5, 4)
    SetScenarioFlags(0xE5, 5)
    SetScenarioFlags(0xE5, 6)
    SetScenarioFlags(0xE5, 7)
    SetScenarioFlags(0xE6, 0)
    SetScenarioFlags(0xE6, 1)
    SetScenarioFlags(0xE6, 2)
    SetScenarioFlags(0xE6, 3)
    SetScenarioFlags(0xE6, 4)
    SetScenarioFlags(0xE6, 5)
    SetScenarioFlags(0xE6, 6)
    SetScenarioFlags(0xE6, 7)
    Return()

    # Function_11_9D4 end

    def Function_12_A80(): pass

    label("Function_12_A80")

    ClearScenarioFlags(0x40, 0)
    ClearScenarioFlags(0x40, 1)
    ClearScenarioFlags(0x40, 2)
    ClearScenarioFlags(0x40, 3)
    ClearScenarioFlags(0x40, 4)
    ClearScenarioFlags(0x40, 5)
    ClearScenarioFlags(0x40, 6)
    ClearScenarioFlags(0x40, 7)
    ClearScenarioFlags(0x41, 0)
    ClearScenarioFlags(0x41, 1)
    ClearScenarioFlags(0x41, 2)
    ClearScenarioFlags(0x41, 3)
    ClearScenarioFlags(0x41, 4)
    ClearScenarioFlags(0x41, 5)
    OP_29(0x1, 0x3, 0x2)
    OP_29(0x1, 0x3, 0x10)
    OP_29(0x1, 0x3, 0x20)
    ClearScenarioFlags(0x41, 6)
    ClearScenarioFlags(0x41, 7)
    ClearScenarioFlags(0x42, 0)
    ClearScenarioFlags(0x42, 1)
    ClearScenarioFlags(0x42, 2)
    ClearScenarioFlags(0x42, 3)
    ClearScenarioFlags(0x42, 4)
    ClearScenarioFlags(0x42, 5)
    ClearScenarioFlags(0x42, 6)
    ClearScenarioFlags(0x42, 7)
    ClearScenarioFlags(0x43, 0)
    ClearScenarioFlags(0x43, 1)
    ClearScenarioFlags(0x43, 2)
    ClearScenarioFlags(0x44, 0)
    ClearScenarioFlags(0x44, 1)
    ClearScenarioFlags(0x44, 2)
    ClearScenarioFlags(0x45, 5)
    ClearScenarioFlags(0x45, 6)
    ClearScenarioFlags(0x45, 7)
    ClearScenarioFlags(0x46, 0)
    ClearScenarioFlags(0x47, 5)
    ClearScenarioFlags(0x4C, 1)
    ClearScenarioFlags(0x46, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_A80 end

    def Function_13_B08(): pass

    label("Function_13_B08")

    ClearScenarioFlags(0x60, 0)
    ClearScenarioFlags(0x60, 1)
    ClearScenarioFlags(0x60, 2)
    ClearScenarioFlags(0x60, 3)
    ClearScenarioFlags(0x60, 4)
    ClearScenarioFlags(0x60, 5)
    ClearScenarioFlags(0x60, 6)
    ClearScenarioFlags(0x60, 7)
    ClearScenarioFlags(0x61, 0)
    ClearScenarioFlags(0x61, 1)
    ClearScenarioFlags(0x61, 2)
    ClearScenarioFlags(0x61, 3)
    ClearScenarioFlags(0x61, 4)
    ClearScenarioFlags(0x61, 5)
    ClearScenarioFlags(0x61, 6)
    ClearScenarioFlags(0x61, 7)
    ClearScenarioFlags(0x62, 0)
    ClearScenarioFlags(0x62, 1)
    ClearScenarioFlags(0x62, 2)
    ClearScenarioFlags(0x62, 3)
    ClearScenarioFlags(0x62, 4)
    ClearScenarioFlags(0x62, 5)
    ClearScenarioFlags(0x62, 6)
    ClearScenarioFlags(0x62, 7)
    ClearScenarioFlags(0x63, 0)
    ClearScenarioFlags(0x63, 1)
    ClearScenarioFlags(0x63, 2)
    ClearScenarioFlags(0x63, 3)
    ClearScenarioFlags(0x63, 4)
    ClearScenarioFlags(0x63, 5)
    ClearScenarioFlags(0x63, 6)
    ClearScenarioFlags(0x63, 7)
    ClearScenarioFlags(0x64, 0)
    ClearScenarioFlags(0x64, 1)
    ClearScenarioFlags(0x64, 2)
    ClearScenarioFlags(0x64, 3)
    ClearScenarioFlags(0x64, 4)
    ClearScenarioFlags(0x64, 5)
    ClearScenarioFlags(0x64, 6)
    ClearScenarioFlags(0x64, 7)
    ClearScenarioFlags(0x65, 0)
    ClearScenarioFlags(0x65, 1)
    ClearScenarioFlags(0x65, 2)
    ClearScenarioFlags(0x65, 3)
    ClearScenarioFlags(0x65, 4)
    ClearScenarioFlags(0x65, 5)
    Return()

    # Function_13_B08 end

    def Function_14_B93(): pass

    label("Function_14_B93")

    ClearScenarioFlags(0x80, 0)
    ClearScenarioFlags(0x80, 1)
    ClearScenarioFlags(0x80, 2)
    ClearScenarioFlags(0x80, 3)
    ClearScenarioFlags(0x80, 4)
    ClearScenarioFlags(0x80, 5)
    ClearScenarioFlags(0x80, 6)
    ClearScenarioFlags(0x80, 7)
    ClearScenarioFlags(0x81, 0)
    ClearScenarioFlags(0x81, 1)
    ClearScenarioFlags(0x81, 2)
    ClearScenarioFlags(0x81, 3)
    ClearScenarioFlags(0x81, 4)
    ClearScenarioFlags(0x81, 5)
    ClearScenarioFlags(0x81, 6)
    ClearScenarioFlags(0x81, 7)
    ClearScenarioFlags(0x82, 0)
    ClearScenarioFlags(0x82, 1)
    ClearScenarioFlags(0x82, 2)
    ClearScenarioFlags(0x82, 3)
    ClearScenarioFlags(0x82, 4)
    ClearScenarioFlags(0x82, 5)
    ClearScenarioFlags(0x82, 6)
    ClearScenarioFlags(0x82, 7)
    ClearScenarioFlags(0x83, 0)
    ClearScenarioFlags(0x83, 1)
    ClearScenarioFlags(0x83, 2)
    ClearScenarioFlags(0x83, 3)
    ClearScenarioFlags(0x83, 4)
    ClearScenarioFlags(0x83, 5)
    ClearScenarioFlags(0x83, 6)
    ClearScenarioFlags(0x83, 7)
    ClearScenarioFlags(0x84, 0)
    ClearScenarioFlags(0x84, 1)
    ClearScenarioFlags(0x84, 2)
    ClearScenarioFlags(0x84, 3)
    ClearScenarioFlags(0x84, 4)
    ClearScenarioFlags(0x84, 5)
    ClearScenarioFlags(0x84, 6)
    ClearScenarioFlags(0x84, 7)
    ClearScenarioFlags(0x85, 0)
    ClearScenarioFlags(0x85, 1)
    ClearScenarioFlags(0x85, 2)
    ClearScenarioFlags(0x85, 3)
    ClearScenarioFlags(0x85, 4)
    ClearScenarioFlags(0x85, 5)
    ClearScenarioFlags(0x85, 6)
    ClearScenarioFlags(0x85, 7)
    ClearScenarioFlags(0x86, 0)
    ClearScenarioFlags(0x86, 1)
    ClearScenarioFlags(0x87, 3)
    ClearScenarioFlags(0x87, 5)
    Return()

    # Function_14_B93 end

    def Function_15_C30(): pass

    label("Function_15_C30")

    ClearScenarioFlags(0xA0, 0)
    ClearScenarioFlags(0xA0, 1)
    ClearScenarioFlags(0xA0, 2)
    ClearScenarioFlags(0xA0, 3)
    ClearScenarioFlags(0xA0, 4)
    ClearScenarioFlags(0xA0, 5)
    ClearScenarioFlags(0xA0, 6)
    ClearScenarioFlags(0xA0, 7)
    ClearScenarioFlags(0xA1, 0)
    ClearScenarioFlags(0xA1, 1)
    ClearScenarioFlags(0xA1, 2)
    ClearScenarioFlags(0xA1, 3)
    ClearScenarioFlags(0xA1, 4)
    ClearScenarioFlags(0xA1, 5)
    ClearScenarioFlags(0xA1, 6)
    ClearScenarioFlags(0xA1, 7)
    ClearScenarioFlags(0xB9, 3)
    ClearScenarioFlags(0xA2, 0)
    ClearScenarioFlags(0xB9, 4)
    ClearScenarioFlags(0xA2, 1)
    ClearScenarioFlags(0xA2, 2)
    ClearScenarioFlags(0xA2, 3)
    ClearScenarioFlags(0xB9, 5)
    ClearScenarioFlags(0xA2, 4)
    ClearScenarioFlags(0xA2, 5)
    ClearScenarioFlags(0xAC, 5)
    ClearScenarioFlags(0xB1, 0)
    ClearScenarioFlags(0xAC, 6)
    ClearScenarioFlags(0xB9, 6)
    ClearScenarioFlags(0xA2, 6)
    ClearScenarioFlags(0xB9, 7)
    ClearScenarioFlags(0xA2, 7)
    ClearScenarioFlags(0xA3, 0)
    ClearScenarioFlags(0xA3, 1)
    ClearScenarioFlags(0xA3, 2)
    ClearScenarioFlags(0xA3, 3)
    ClearScenarioFlags(0xA3, 4)
    ClearScenarioFlags(0xA3, 5)
    ClearScenarioFlags(0xA3, 6)
    ClearScenarioFlags(0xA3, 7)
    ClearScenarioFlags(0xA4, 0)
    ClearScenarioFlags(0xA4, 1)
    ClearScenarioFlags(0xA4, 2)
    ClearScenarioFlags(0xA4, 3)
    ClearScenarioFlags(0xA4, 4)
    ClearScenarioFlags(0xA4, 5)
    ClearScenarioFlags(0xA4, 6)
    ClearScenarioFlags(0xA4, 7)
    ClearScenarioFlags(0xA5, 0)
    ClearScenarioFlags(0xA5, 1)
    ClearScenarioFlags(0xA5, 2)
    ClearScenarioFlags(0xA5, 3)
    ClearScenarioFlags(0xA5, 4)
    ClearScenarioFlags(0xA5, 5)
    ClearScenarioFlags(0xA5, 6)
    ClearScenarioFlags(0xA5, 7)
    ClearScenarioFlags(0xA6, 0)
    ClearScenarioFlags(0xA6, 1)
    ClearScenarioFlags(0xA6, 2)
    ClearScenarioFlags(0xA6, 3)
    ClearScenarioFlags(0xA6, 4)
    ClearScenarioFlags(0xA6, 5)
    ClearScenarioFlags(0xA6, 6)
    ClearScenarioFlags(0xA6, 7)
    ClearScenarioFlags(0xA7, 0)
    ClearScenarioFlags(0xA7, 1)
    ClearScenarioFlags(0xA7, 2)
    ClearScenarioFlags(0xA7, 3)
    ClearScenarioFlags(0xA7, 4)
    ClearScenarioFlags(0xA7, 5)
    ClearScenarioFlags(0xA9, 1)
    ClearScenarioFlags(0xA9, 2)
    ClearScenarioFlags(0xA9, 3)
    ClearScenarioFlags(0xAA, 0)
    ClearScenarioFlags(0xAA, 1)
    ClearScenarioFlags(0xAA, 2)
    Return()

    # Function_15_C30 end

    def Function_16_D15(): pass

    label("Function_16_D15")

    ClearScenarioFlags(0xA7, 6)
    ClearScenarioFlags(0xA7, 7)
    ClearScenarioFlags(0xA8, 0)
    ClearScenarioFlags(0xA8, 1)
    ClearScenarioFlags(0xA8, 2)
    ClearScenarioFlags(0xA8, 3)
    ClearScenarioFlags(0xA8, 4)
    ClearScenarioFlags(0xA8, 5)
    ClearScenarioFlags(0xA8, 6)
    ClearScenarioFlags(0xA8, 7)
    ClearScenarioFlags(0xA9, 0)
    ClearScenarioFlags(0xA9, 4)
    ClearScenarioFlags(0xA9, 5)
    ClearScenarioFlags(0xA9, 6)
    ClearScenarioFlags(0xA9, 7)
    Return()

    # Function_16_D15 end

    def Function_17_D43(): pass

    label("Function_17_D43")

    ClearScenarioFlags(0xC0, 0)
    ClearScenarioFlags(0xC0, 1)
    ClearScenarioFlags(0xC0, 2)
    ClearScenarioFlags(0xC0, 3)
    ClearScenarioFlags(0xC0, 4)
    ClearScenarioFlags(0xC0, 5)
    ClearScenarioFlags(0xC0, 6)
    ClearScenarioFlags(0xC0, 7)
    ClearScenarioFlags(0xC1, 0)
    ClearScenarioFlags(0xC1, 1)
    ClearScenarioFlags(0xC1, 2)
    ClearScenarioFlags(0xC1, 3)
    ClearScenarioFlags(0xC1, 4)
    ClearScenarioFlags(0xC1, 5)
    ClearScenarioFlags(0xC1, 6)
    ClearScenarioFlags(0xC1, 7)
    ClearScenarioFlags(0xC2, 0)
    ClearScenarioFlags(0xC2, 1)
    ClearScenarioFlags(0xC2, 2)
    ClearScenarioFlags(0xC2, 3)
    ClearScenarioFlags(0xC2, 4)
    ClearScenarioFlags(0xC2, 5)
    ClearScenarioFlags(0xC2, 6)
    ClearScenarioFlags(0xC2, 7)
    ClearScenarioFlags(0xC3, 0)
    ClearScenarioFlags(0xC3, 1)
    ClearScenarioFlags(0xC3, 2)
    ClearScenarioFlags(0xC3, 3)
    ClearScenarioFlags(0xC3, 4)
    ClearScenarioFlags(0xC3, 5)
    ClearScenarioFlags(0xC3, 6)
    ClearScenarioFlags(0xC3, 7)
    ClearScenarioFlags(0xC4, 0)
    ClearScenarioFlags(0xC4, 1)
    ClearScenarioFlags(0xC4, 2)
    ClearScenarioFlags(0xC4, 3)
    ClearScenarioFlags(0xC4, 4)
    ClearScenarioFlags(0xC4, 5)
    ClearScenarioFlags(0xC4, 6)
    ClearScenarioFlags(0xC4, 7)
    ClearScenarioFlags(0xC5, 0)
    ClearScenarioFlags(0xC5, 1)
    ClearScenarioFlags(0xC5, 2)
    ClearScenarioFlags(0xC5, 3)
    ClearScenarioFlags(0xC6, 5)
    ClearScenarioFlags(0xC5, 4)
    ClearScenarioFlags(0xC5, 5)
    ClearScenarioFlags(0xC5, 6)
    ClearScenarioFlags(0xC5, 7)
    ClearScenarioFlags(0xC6, 0)
    ClearScenarioFlags(0xC6, 1)
    ClearScenarioFlags(0xC6, 2)
    ClearScenarioFlags(0xC6, 3)
    ClearScenarioFlags(0xC6, 4)
    ClearScenarioFlags(0xC6, 6)
    ClearScenarioFlags(0xC6, 7)
    ClearScenarioFlags(0xC8, 0)
    ClearScenarioFlags(0xC8, 1)
    ClearScenarioFlags(0xC8, 2)
    ClearScenarioFlags(0xC8, 3)
    ClearScenarioFlags(0xC8, 4)
    Return()

    # Function_17_D43 end

    def Function_18_DFB(): pass

    label("Function_18_DFB")

    ClearScenarioFlags(0xE0, 0)
    ClearScenarioFlags(0xE0, 1)
    ClearScenarioFlags(0xE0, 2)
    ClearScenarioFlags(0xE0, 3)
    ClearScenarioFlags(0xE0, 4)
    ClearScenarioFlags(0xE0, 5)
    ClearScenarioFlags(0xE0, 6)
    ClearScenarioFlags(0xE0, 7)
    ClearScenarioFlags(0xE1, 0)
    ClearScenarioFlags(0xE1, 1)
    ClearScenarioFlags(0xE1, 2)
    ClearScenarioFlags(0xE1, 3)
    ClearScenarioFlags(0xE1, 4)
    ClearScenarioFlags(0xE1, 5)
    ClearScenarioFlags(0xE1, 6)
    ClearScenarioFlags(0xE1, 7)
    ClearScenarioFlags(0xE2, 0)
    ClearScenarioFlags(0xE2, 1)
    ClearScenarioFlags(0xE2, 2)
    ClearScenarioFlags(0xE2, 3)
    ClearScenarioFlags(0xE2, 4)
    ClearScenarioFlags(0xE2, 5)
    ClearScenarioFlags(0xE2, 6)
    ClearScenarioFlags(0xE2, 7)
    ClearScenarioFlags(0xE3, 0)
    ClearScenarioFlags(0xE3, 1)
    ClearScenarioFlags(0xE3, 2)
    ClearScenarioFlags(0xE3, 3)
    ClearScenarioFlags(0xE3, 4)
    ClearScenarioFlags(0xE3, 5)
    ClearScenarioFlags(0xE3, 6)
    ClearScenarioFlags(0xE3, 7)
    ClearScenarioFlags(0xE4, 0)
    ClearScenarioFlags(0xE4, 1)
    ClearScenarioFlags(0xE4, 2)
    ClearScenarioFlags(0xE4, 3)
    ClearScenarioFlags(0xE4, 4)
    ClearScenarioFlags(0xE7, 5)
    ClearScenarioFlags(0xE4, 5)
    ClearScenarioFlags(0xE4, 6)
    ClearScenarioFlags(0xE4, 7)
    ClearScenarioFlags(0xE5, 0)
    ClearScenarioFlags(0xE5, 1)
    ClearScenarioFlags(0xE5, 2)
    ClearScenarioFlags(0xE5, 3)
    ClearScenarioFlags(0xE5, 4)
    ClearScenarioFlags(0xE5, 5)
    ClearScenarioFlags(0xE5, 6)
    ClearScenarioFlags(0xE5, 7)
    ClearScenarioFlags(0xE6, 0)
    ClearScenarioFlags(0xE6, 1)
    ClearScenarioFlags(0xE6, 2)
    ClearScenarioFlags(0xE6, 3)
    ClearScenarioFlags(0xE6, 4)
    ClearScenarioFlags(0xE6, 5)
    ClearScenarioFlags(0xE6, 6)
    ClearScenarioFlags(0xE6, 7)
    Return()

    # Function_18_DFB end

    def Function_19_EA7(): pass

    label("Function_19_EA7")

    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1262")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼プロローグ\x01",                   # 0
            "②▼大陸横断鉄道列車内\x01",           # 1
            "③▼クロスベル駅到着\x01",             # 2
            "④▼警察受付に話しかける\x01",         # 3
            "⑤▼ジオフロント前に到着\x01",         # 4
            "⑥▼子供の泣き声を聞く\x01",           # 5
            "⑦▼もう一人の子供を発見\x01",         # 6
            "⑧▼戦闘後アリオス登場\x01",           # 7
            "⑨▼新聞記者グレイス登場\x01",         # 8
            "⑩▼副局長室で叱責される\x01",         # 9
            "?▼特務支援課ビルに到着する\x01",      # 10
            "?▼仲間の部屋を訪ねる\x01",            # 11
            "?▼ティオと話すイベント\x01",          # 12
            "?▼子供達が会いに来る\x01",            # 13
            "キャンセル\x01",                       # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_1080"),
        (12, "loc_1083"),
        (11, "loc_1089"),
        (10, "loc_108C"),
        (9, "loc_108C"),
        (8, "loc_108C"),
        (7, "loc_108C"),
        (6, "loc_108F"),
        (5, "loc_1095"),
        (4, "loc_10A1"),
        (3, "loc_10A1"),
        (2, "loc_10A4"),
        (1, "loc_10A4"),
        (0, "loc_10A7"),
        (SWITCH_DEFAULT, "loc_10BB"),
    )


    label("loc_1080")

    SetScenarioFlags(0x41, 4)

    label("loc_1083")

    SetScenarioFlags(0x41, 2)
    SetScenarioFlags(0x41, 3)

    label("loc_1089")

    SetScenarioFlags(0x41, 1)

    label("loc_108C")

    SetScenarioFlags(0x41, 0)

    label("loc_108F")

    SetScenarioFlags(0x40, 6)
    SetScenarioFlags(0x40, 7)

    label("loc_1095")

    SetScenarioFlags(0x40, 2)
    SetScenarioFlags(0x40, 3)
    SetScenarioFlags(0x40, 4)
    SetScenarioFlags(0x40, 5)

    label("loc_10A1")

    SetScenarioFlags(0x40, 1)

    label("loc_10A4")

    SetScenarioFlags(0x40, 0)

    label("loc_10A7")

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 46)
    Jump("loc_10C0")

    label("loc_10BB")

    Jump("loc_10C0")

    label("loc_10C0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10E5")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)

    label("loc_10E5")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1143"),
        (1, "loc_1154"),
        (2, "loc_1165"),
        (3, "loc_1176"),
        (4, "loc_1184"),
        (5, "loc_1195"),
        (6, "loc_11A3"),
        (7, "loc_11B5"),
        (8, "loc_11CE"),
        (9, "loc_11E7"),
        (10, "loc_11F8"),
        (11, "loc_1209"),
        (12, "loc_1220"),
        (13, "loc_1237"),
        (SWITCH_DEFAULT, "loc_124E"),
    )


    label("loc_1143")

    SetScenarioFlags(0x5C, 1)
    NewScene("m3000", 0, 0, 0)
    IdleLoop()
    Jump("loc_125D")

    label("loc_1154")

    SetScenarioFlags(0x5C, 0)
    NewScene("e0410", 0, 0, 0)
    IdleLoop()
    Jump("loc_125D")

    label("loc_1165")

    SetScenarioFlags(0x5C, 0)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Jump("loc_125D")

    label("loc_1176")

    NewScene("c1150", 0, 0, 0)
    IdleLoop()
    Jump("loc_125D")

    label("loc_1184")

    SetScenarioFlags(0x5C, 1)
    NewScene("c0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_125D")

    label("loc_1195")

    NewScene("m0001", 0, 0, 0)
    IdleLoop()
    Jump("loc_125D")

    label("loc_11A3")

    AddParty(0x96, 0xFF, 0xFF)
    NewScene("m0002", 0, 0, 0)
    IdleLoop()
    Jump("loc_125D")

    label("loc_11B5")

    AddParty(0x96, 0xFF, 0xFF)
    AddParty(0x97, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 0)
    NewScene("m0002", 0, 0, 0)
    IdleLoop()
    Jump("loc_125D")

    label("loc_11CE")

    AddParty(0x96, 0xFF, 0xFF)
    AddParty(0x97, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 2)
    NewScene("c0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_125D")

    label("loc_11E7")

    SetScenarioFlags(0x5C, 0)
    NewScene("c1160", 0, 0, 0)
    IdleLoop()
    Jump("loc_125D")

    label("loc_11F8")

    SetScenarioFlags(0x5C, 0)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Jump("loc_125D")

    label("loc_1209")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Jump("loc_125D")

    label("loc_1220")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Jump("loc_125D")

    label("loc_1237")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c010B", 105, 0, 0)
    IdleLoop()
    Jump("loc_125D")

    label("loc_124E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_125D")

    label("loc_125D")

    Jump("loc_EB6")

    label("loc_1262")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_19_EA7 end

    def Function_20_1270(): pass

    label("Function_20_1270")

    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_128B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_167D")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼回想～墓前のロイド\x01",            # 0
            "②▼特務支援課の説明を聞く\x01",        # 1
            "③▼初の捜査任務が入る\x01",            # 2
            "④▼不良の喧嘩仲裁をする\x01",          # 3
            "⑤▼戦闘後ワジ＆ヴァルド登場\x01",      # 4
            "⑥▼ワジから話を聞く\x01",              # 5
            "⑦▼イグニスの前でのやり取り\x01",      # 6
            "⑧▼ヴァルドから話を聞く\x01",          # 7
            "⑨▼戦闘後ヴァルドに話を聞く\x01",      # 8
            "⑩▼イグニスから出てくる\x01",          # 9
            "?▼グレイスから話を聞く\x01",           # 10
            "?▼セルゲイから話を聞く\x01",           # 11
            "?▼ダドリーとすれ違う\x01",             # 12
            "?▼イアン弁護士から話を聞く\x01",       # 13
            "キャンセル\x01",                        # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_1471"),
        (12, "loc_1474"),
        (11, "loc_1477"),
        (10, "loc_147A"),
        (9, "loc_147D"),
        (8, "loc_1480"),
        (7, "loc_1480"),
        (6, "loc_1483"),
        (5, "loc_1486"),
        (4, "loc_1489"),
        (3, "loc_1489"),
        (2, "loc_148C"),
        (1, "loc_14A4"),
        (0, "loc_14A4"),
        (SWITCH_DEFAULT, "loc_14DF"),
    )


    label("loc_1471")

    SetScenarioFlags(0x42, 7)

    label("loc_1474")

    SetScenarioFlags(0x42, 6)

    label("loc_1477")

    SetScenarioFlags(0x42, 5)

    label("loc_147A")

    SetScenarioFlags(0x42, 4)

    label("loc_147D")

    SetScenarioFlags(0x42, 3)

    label("loc_1480")

    SetScenarioFlags(0x42, 2)

    label("loc_1483")

    SetScenarioFlags(0x42, 1)

    label("loc_1486")

    SetScenarioFlags(0x42, 0)

    label("loc_1489")

    SetScenarioFlags(0x41, 7)

    label("loc_148C")

    SetScenarioFlags(0x41, 6)
    SetScenarioFlags(0x41, 5)
    SetScenarioFlags(0x4C, 1)
    OP_29(0x1, 0x4, 0x2)
    OP_29(0x1, 0x4, 0x10)
    OP_29(0x1, 0x4, 0x20)

    label("loc_14A4")

    SetScenarioFlags(0x41, 4)
    SetScenarioFlags(0x41, 2)
    SetScenarioFlags(0x41, 3)
    SetScenarioFlags(0x41, 1)
    SetScenarioFlags(0x41, 0)
    SetScenarioFlags(0x40, 7)
    SetScenarioFlags(0x40, 6)
    SetScenarioFlags(0x40, 2)
    SetScenarioFlags(0x40, 3)
    SetScenarioFlags(0x40, 4)
    SetScenarioFlags(0x40, 5)
    SetScenarioFlags(0x40, 1)
    SetScenarioFlags(0x40, 0)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 47)
    Jump("loc_14E4")

    label("loc_14DF")

    Jump("loc_14E4")

    label("loc_14E4")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1542"),
        (1, "loc_1553"),
        (2, "loc_1564"),
        (3, "loc_1575"),
        (4, "loc_1583"),
        (5, "loc_159D"),
        (6, "loc_15B5"),
        (7, "loc_15CD"),
        (8, "loc_15E5"),
        (9, "loc_1600"),
        (10, "loc_1618"),
        (11, "loc_1630"),
        (12, "loc_1643"),
        (13, "loc_1656"),
        (SWITCH_DEFAULT, "loc_1669"),
    )


    label("loc_1542")

    SetScenarioFlags(0x5C, 0)
    NewScene("t4100", 0, 0, 0)
    IdleLoop()
    Jump("loc_1678")

    label("loc_1553")

    SetScenarioFlags(0x5C, 1)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_1678")

    label("loc_1564")

    SetScenarioFlags(0x5C, 1)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_1678")

    label("loc_1575")

    NewScene("c1400", 0, 0, 0)
    IdleLoop()
    Jump("loc_1678")

    label("loc_1583")

    SetScenarioFlags(0x5C, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x205), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c1400", 0, 0, 0)
    IdleLoop()
    Jump("loc_1678")

    label("loc_159D")

    ReplaceBGM("ed7101", "ed7103")
    ReplaceBGM("ed7100", "ed7103")
    NewScene("c1410", 0, 0, 0)
    IdleLoop()
    Jump("loc_1678")

    label("loc_15B5")

    ReplaceBGM("ed7101", "ed7103")
    ReplaceBGM("ed7100", "ed7103")
    NewScene("c1400", 0, 0, 0)
    IdleLoop()
    Jump("loc_1678")

    label("loc_15CD")

    ReplaceBGM("ed7101", "ed7103")
    ReplaceBGM("ed7100", "ed7103")
    NewScene("c1420", 0, 0, 0)
    IdleLoop()
    Jump("loc_1678")

    label("loc_15E5")

    ReplaceBGM("ed7101", "ed7103")
    ReplaceBGM("ed7100", "ed7103")
    SetScenarioFlags(0x5C, 0)
    NewScene("c1420", 0, 0, 0)
    IdleLoop()
    Jump("loc_1678")

    label("loc_1600")

    ReplaceBGM("ed7101", "ed7103")
    ReplaceBGM("ed7100", "ed7103")
    NewScene("c1400", 0, 0, 0)
    IdleLoop()
    Jump("loc_1678")

    label("loc_1618")

    ReplaceBGM("ed7101", "ed7103")
    ReplaceBGM("ed7100", "ed7103")
    NewScene("c1030", 0, 0, 0)
    IdleLoop()
    Jump("loc_1678")

    label("loc_1630")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_1678")

    label("loc_1643")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("c0200", 0, 0, 0)
    IdleLoop()
    Jump("loc_1678")

    label("loc_1656")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("c0220", 0, 0, 0)
    IdleLoop()
    Jump("loc_1678")

    label("loc_1669")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1678")

    label("loc_1678")

    Jump("loc_128B")

    label("loc_167D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_20_1270 end

    def Function_21_168B(): pass

    label("Function_21_168B")

    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_16A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1884")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼特務支援課に戻ってくる\x01",          # 0
            "②▼ワジとヴァルドに真相を話す\x01",      # 1
            "③▼マフィアを罠にかける\x01",            # 2
            "④▼戦闘後マフィアが逃げる\x01",          # 3
            "⑤▼支援課で任務完了報告をする\x01",      # 4
            "キャンセル\x01",                          # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (4, "loc_1781"),
        (3, "loc_1781"),
        (2, "loc_1781"),
        (1, "loc_1781"),
        (0, "loc_1787"),
        (SWITCH_DEFAULT, "loc_17E9"),
    )


    label("loc_1781")

    SetScenarioFlags(0x43, 1)
    SetScenarioFlags(0x43, 2)

    label("loc_1787")

    SetScenarioFlags(0x46, 1)
    SetScenarioFlags(0x43, 0)
    SetScenarioFlags(0x42, 7)
    SetScenarioFlags(0x42, 6)
    SetScenarioFlags(0x42, 5)
    SetScenarioFlags(0x42, 4)
    SetScenarioFlags(0x42, 3)
    SetScenarioFlags(0x42, 2)
    SetScenarioFlags(0x42, 1)
    SetScenarioFlags(0x42, 0)
    SetScenarioFlags(0x41, 7)
    SetScenarioFlags(0x41, 6)
    SetScenarioFlags(0x41, 5)
    SetScenarioFlags(0x41, 4)
    SetScenarioFlags(0x41, 2)
    SetScenarioFlags(0x41, 3)
    SetScenarioFlags(0x41, 1)
    SetScenarioFlags(0x41, 0)
    SetScenarioFlags(0x40, 7)
    SetScenarioFlags(0x40, 6)
    SetScenarioFlags(0x40, 2)
    SetScenarioFlags(0x40, 3)
    SetScenarioFlags(0x40, 4)
    SetScenarioFlags(0x40, 5)
    SetScenarioFlags(0x40, 1)
    SetScenarioFlags(0x40, 0)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 48)
    Jump("loc_17EE")

    label("loc_17E9")

    Jump("loc_17EE")

    label("loc_17EE")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1816"),
        (1, "loc_1829"),
        (2, "loc_183A"),
        (3, "loc_184B"),
        (4, "loc_185F"),
        (SWITCH_DEFAULT, "loc_1870"),
    )


    label("loc_1816")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_187F")

    label("loc_1829")

    SetScenarioFlags(0x5C, 0)
    NewScene("c000B", 0, 0, 0)
    IdleLoop()
    Jump("loc_187F")

    label("loc_183A")

    SetScenarioFlags(0x5C, 0)
    NewScene("c140B", 0, 0, 0)
    IdleLoop()
    Jump("loc_187F")

    label("loc_184B")

    SetScenarioFlags(0x45, 5)
    SetScenarioFlags(0x5C, 1)
    NewScene("c140B", 0, 0, 0)
    IdleLoop()
    Jump("loc_187F")

    label("loc_185F")

    SetScenarioFlags(0x5C, 3)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Jump("loc_187F")

    label("loc_1870")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_187F")

    label("loc_187F")

    Jump("loc_16A6")

    label("loc_1884")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_21_168B end

    def Function_22_1892(): pass

    label("Function_22_1892")

    Call(2, 5)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BDF")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼プロローグ\x01",                  # 0
            "②▼朝のクロスベル\x01",              # 1
            "③▼警察本部\x01",                    # 2
            "④▼調書に目を通す\x01",              # 3
            "⑤▼導力バスがいってしまう\x01",      # 4
            "⑥▼分岐地点に到着\x01",              # 5
            "⑦▼休憩所に到着\x01",                # 6
            "⑧▼アルモリカ村に到着\x01",          # 7
            "⑨▼村長の家を訪問する\x01",          # 8
            "⑩▼アルモリカ村を後にする\x01",      # 9
            "?▼ハロルドに送ってもらう\x01",       # 10
            "?▼クロスベルに戻ってくる\x01",       # 11
            "?▼バス停のバスを待つ\x01",           # 12
            "?▼バスを発見\x01",                   # 13
            "キャンセル\x01",                      # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_1A56"),
        (12, "loc_1A59"),
        (11, "loc_1A5C"),
        (10, "loc_1A5C"),
        (9, "loc_1A5F"),
        (8, "loc_1A68"),
        (7, "loc_1A6B"),
        (6, "loc_1A6E"),
        (5, "loc_1A71"),
        (4, "loc_1A74"),
        (3, "loc_1A77"),
        (2, "loc_1A77"),
        (1, "loc_1A77"),
        (0, "loc_1A77"),
        (SWITCH_DEFAULT, "loc_1A8B"),
    )


    label("loc_1A56")

    SetScenarioFlags(0x61, 2)

    label("loc_1A59")

    SetScenarioFlags(0x61, 1)

    label("loc_1A5C")

    SetScenarioFlags(0x61, 0)

    label("loc_1A5F")

    SetScenarioFlags(0x60, 7)
    SetScenarioFlags(0x60, 5)
    SetScenarioFlags(0x60, 6)

    label("loc_1A68")

    SetScenarioFlags(0x60, 4)

    label("loc_1A6B")

    SetScenarioFlags(0x60, 3)

    label("loc_1A6E")

    SetScenarioFlags(0x60, 2)

    label("loc_1A71")

    SetScenarioFlags(0x60, 1)

    label("loc_1A74")

    SetScenarioFlags(0x60, 0)

    label("loc_1A77")

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 49)
    Jump("loc_1A90")

    label("loc_1A8B")

    Jump("loc_1A90")

    label("loc_1A90")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1AEE"),
        (1, "loc_1AFF"),
        (2, "loc_1B10"),
        (3, "loc_1B21"),
        (4, "loc_1B32"),
        (5, "loc_1B40"),
        (6, "loc_1B4E"),
        (7, "loc_1B5C"),
        (8, "loc_1B6A"),
        (9, "loc_1B78"),
        (10, "loc_1B86"),
        (11, "loc_1B94"),
        (12, "loc_1BAA"),
        (13, "loc_1BBD"),
        (SWITCH_DEFAULT, "loc_1BD0"),
    )


    label("loc_1AEE")

    SetScenarioFlags(0x5C, 0)
    NewScene("c1010", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BDA")

    label("loc_1AFF")

    SetScenarioFlags(0x5C, 3)
    NewScene("c0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BDA")

    label("loc_1B10")

    SetScenarioFlags(0x5C, 1)
    NewScene("c1100", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BDA")

    label("loc_1B21")

    SetScenarioFlags(0x5C, 3)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BDA")

    label("loc_1B32")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BDA")

    label("loc_1B40")

    NewScene("r0030", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BDA")

    label("loc_1B4E")

    NewScene("r0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BDA")

    label("loc_1B5C")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BDA")

    label("loc_1B6A")

    NewScene("t0010", 103, 0, 0)
    IdleLoop()
    Jump("loc_1BDA")

    label("loc_1B78")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BDA")

    label("loc_1B86")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BDA")

    label("loc_1B94")

    SetScenarioFlags(0x5C, 3)
    ReplaceBGM("ed7100", "ed7102")
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BDA")

    label("loc_1BAA")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("r1500", 100, 0, 0)
    IdleLoop()
    Jump("loc_1BDA")

    label("loc_1BBD")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("r1520", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BDA")

    label("loc_1BD0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BDA")

    Jump("loc_18B0")

    label("loc_1BDF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_22_1892 end

    def Function_23_1BED(): pass

    label("Function_23_1BED")

    Call(2, 5)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FB1")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼戦闘後エステル登場\x01",          # 0
            "②▼エステルイベント\x01",            # 1
            "③▼医科大学に到着する\x01",          # 2
            "④▼セシルと再会する\x01",            # 3
            "⑤▼研修医から話を聞く\x01",          # 4
            "⑥▼襲われた場所を調べる\x01",        # 5
            "⑦▼セシルの行方を聞く\x01",          # 6
            "⑧▼シズクと知り合う\x01",            # 7
            "⑨▼セシルに調査結果を報告\x01",      # 8
            "⑩▼導力バスに乗って帰る\x01",        # 9
            "?▼回想シーン\x01",                   # 10
            "?▼北口で遠吠えを聞く\x01",           # 11
            "?▼山道で遠吠えを聞く\x01",           # 12
            "?▼分岐地点に到着\x01",               # 13
            "キャンセル\x01",                      # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_1DC3"),
        (12, "loc_1DC6"),
        (11, "loc_1DC9"),
        (10, "loc_1DCC"),
        (9, "loc_1DCF"),
        (8, "loc_1DD2"),
        (7, "loc_1DD2"),
        (6, "loc_1DDB"),
        (5, "loc_1DF6"),
        (4, "loc_1DFC"),
        (3, "loc_1DFF"),
        (2, "loc_1E05"),
        (1, "loc_1E0B"),
        (0, "loc_1E0E"),
        (SWITCH_DEFAULT, "loc_1E43"),
    )


    label("loc_1DC3")

    SetScenarioFlags(0x64, 3)

    label("loc_1DC6")

    SetScenarioFlags(0x64, 2)

    label("loc_1DC9")

    SetScenarioFlags(0x64, 1)

    label("loc_1DCC")

    SetScenarioFlags(0x64, 0)

    label("loc_1DCF")

    SetScenarioFlags(0x63, 7)

    label("loc_1DD2")

    SetScenarioFlags(0x63, 4)
    SetScenarioFlags(0x63, 5)
    SetScenarioFlags(0x63, 6)

    label("loc_1DDB")

    SetScenarioFlags(0x62, 3)
    SetScenarioFlags(0x62, 4)
    SetScenarioFlags(0x62, 5)
    SetScenarioFlags(0x62, 6)
    SetScenarioFlags(0x62, 7)
    SetScenarioFlags(0x63, 0)
    SetScenarioFlags(0x63, 1)
    SetScenarioFlags(0x63, 2)
    SetScenarioFlags(0x63, 3)

    label("loc_1DF6")

    SetScenarioFlags(0x62, 1)
    SetScenarioFlags(0x62, 2)

    label("loc_1DFC")

    SetScenarioFlags(0x62, 0)

    label("loc_1DFF")

    SetScenarioFlags(0x61, 6)
    SetScenarioFlags(0x61, 7)

    label("loc_1E05")

    SetScenarioFlags(0x61, 4)
    SetScenarioFlags(0x61, 5)

    label("loc_1E0B")

    SetScenarioFlags(0x61, 3)

    label("loc_1E0E")

    SetScenarioFlags(0x60, 0)
    SetScenarioFlags(0x60, 1)
    SetScenarioFlags(0x60, 2)
    SetScenarioFlags(0x60, 3)
    SetScenarioFlags(0x60, 4)
    SetScenarioFlags(0x60, 5)
    SetScenarioFlags(0x60, 6)
    SetScenarioFlags(0x60, 7)
    SetScenarioFlags(0x61, 0)
    SetScenarioFlags(0x61, 1)
    SetScenarioFlags(0x61, 2)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 50)
    Jump("loc_1E48")

    label("loc_1E43")

    Jump("loc_1E48")

    label("loc_1E48")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1EA6"),
        (1, "loc_1EBC"),
        (2, "loc_1ECF"),
        (3, "loc_1EE2"),
        (4, "loc_1EF5"),
        (5, "loc_1F07"),
        (6, "loc_1F19"),
        (7, "loc_1F27"),
        (8, "loc_1F35"),
        (9, "loc_1F4A"),
        (10, "loc_1F58"),
        (11, "loc_1F69"),
        (12, "loc_1F7C"),
        (13, "loc_1F8F"),
        (SWITCH_DEFAULT, "loc_1FA2"),
    )


    label("loc_1EA6")

    SetScenarioFlags(0x5C, 0)
    ReplaceBGM("ed7100", "ed7102")
    NewScene("r1520", 0, 0, 0)
    IdleLoop()
    Jump("loc_1FAC")

    label("loc_1EBC")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("r1520", 0, 0, 0)
    IdleLoop()
    Jump("loc_1FAC")

    label("loc_1ECF")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("t1500", 100, 0, 0)
    IdleLoop()
    Jump("loc_1FAC")

    label("loc_1EE2")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("t1530", 0, 0, 0)
    IdleLoop()
    Jump("loc_1FAC")

    label("loc_1EF5")

    AddParty(0x35, 0xFF, 0xFF)
    NewScene("t1540", 0, 0, 0)
    IdleLoop()
    Jump("loc_1FAC")

    label("loc_1F07")

    AddParty(0x35, 0xFF, 0xFF)
    NewScene("t1600", 103, 0, 0)
    IdleLoop()
    Jump("loc_1FAC")

    label("loc_1F19")

    NewScene("t1540", 0, 0, 0)
    IdleLoop()
    Jump("loc_1FAC")

    label("loc_1F27")

    NewScene("t1550", 107, 0, 0)
    IdleLoop()
    Jump("loc_1FAC")

    label("loc_1F35")

    SetScenarioFlags(0x5C, 0)
    AddParty(0x35, 0xFF, 0xFF)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1FAC")

    label("loc_1F4A")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1FAC")

    label("loc_1F58")

    SetScenarioFlags(0x5C, 4)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_1FAC")

    label("loc_1F69")

    ReplaceBGM("ed7100", "ed7103")
    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_1FAC")

    label("loc_1F7C")

    ReplaceBGM("ed7100", "ed7103")
    NewScene("r2020", 0, 0, 0)
    IdleLoop()
    Jump("loc_1FAC")

    label("loc_1F8F")

    ReplaceBGM("ed7100", "ed7103")
    NewScene("r2030", 0, 0, 0)
    IdleLoop()
    Jump("loc_1FAC")

    label("loc_1FA2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1FAC")

    Jump("loc_1C0B")

    label("loc_1FB1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_23_1BED end

    def Function_24_1FBF(): pass

    label("Function_24_1FBF")

    Call(2, 5)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1FDD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2396")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼レンと遭遇する\x01",                  # 0
            "②▼トンネル道に入る\x01",                # 1
            "③▼ツァイトと遭遇する\x01",              # 2
            "④▼マインツに到着する\x01",              # 3
            "⑤▼マフィアの手下が現れる\x01",          # 4
            "⑥▼町長から話を聞く\x01",                # 5
            "⑦▼ミーティング開始\x01",                # 6
            "⑧▼狼型魔獣を撃退する\x01",              # 7
            "⑨▼戦闘後マフィアを見つける\x01",        # 8
            "⑩▼戦闘後ツァイトに助けられる\x01",      # 9
            "?▼マフィアを連行する\x01",               # 10
            "?▼クロスベルに帰ってくる\x01",           # 11
            "?★夜の病院（回想シーン専用）\x01",       # 12
            "キャンセル\x01",                          # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (12, "loc_2197"),
        (11, "loc_2197"),
        (10, "loc_2197"),
        (9, "loc_2197"),
        (8, "loc_2197"),
        (7, "loc_2197"),
        (6, "loc_219A"),
        (5, "loc_219D"),
        (4, "loc_21A0"),
        (3, "loc_21A6"),
        (2, "loc_21A9"),
        (1, "loc_21AF"),
        (0, "loc_21B2"),
        (SWITCH_DEFAULT, "loc_2235"),
    )


    label("loc_2197")

    SetScenarioFlags(0x65, 5)

    label("loc_219A")

    SetScenarioFlags(0x65, 4)

    label("loc_219D")

    SetScenarioFlags(0x65, 3)

    label("loc_21A0")

    SetScenarioFlags(0x65, 1)
    SetScenarioFlags(0x65, 2)

    label("loc_21A6")

    SetScenarioFlags(0x65, 0)

    label("loc_21A9")

    SetScenarioFlags(0x64, 6)
    SetScenarioFlags(0x64, 7)

    label("loc_21AF")

    SetScenarioFlags(0x64, 5)

    label("loc_21B2")

    SetScenarioFlags(0x60, 0)
    SetScenarioFlags(0x60, 1)
    SetScenarioFlags(0x60, 2)
    SetScenarioFlags(0x60, 3)
    SetScenarioFlags(0x60, 4)
    SetScenarioFlags(0x60, 5)
    SetScenarioFlags(0x60, 6)
    SetScenarioFlags(0x60, 7)
    SetScenarioFlags(0x61, 0)
    SetScenarioFlags(0x61, 1)
    SetScenarioFlags(0x61, 2)
    SetScenarioFlags(0x61, 3)
    SetScenarioFlags(0x61, 4)
    SetScenarioFlags(0x61, 5)
    SetScenarioFlags(0x61, 6)
    SetScenarioFlags(0x61, 7)
    SetScenarioFlags(0x62, 0)
    SetScenarioFlags(0x62, 1)
    SetScenarioFlags(0x62, 2)
    SetScenarioFlags(0x62, 3)
    SetScenarioFlags(0x62, 4)
    SetScenarioFlags(0x62, 5)
    SetScenarioFlags(0x62, 6)
    SetScenarioFlags(0x62, 7)
    SetScenarioFlags(0x63, 0)
    SetScenarioFlags(0x63, 1)
    SetScenarioFlags(0x63, 2)
    SetScenarioFlags(0x63, 3)
    SetScenarioFlags(0x63, 4)
    SetScenarioFlags(0x63, 5)
    SetScenarioFlags(0x63, 6)
    SetScenarioFlags(0x63, 7)
    SetScenarioFlags(0x64, 0)
    SetScenarioFlags(0x64, 1)
    SetScenarioFlags(0x64, 2)
    SetScenarioFlags(0x64, 3)
    SetScenarioFlags(0x64, 4)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 51)
    Jump("loc_223A")

    label("loc_2235")

    Jump("loc_223A")

    label("loc_223A")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2292"),
        (1, "loc_22A5"),
        (2, "loc_22B8"),
        (3, "loc_22CB"),
        (4, "loc_22DE"),
        (5, "loc_22EC"),
        (6, "loc_2304"),
        (7, "loc_2312"),
        (8, "loc_2320"),
        (9, "loc_233A"),
        (10, "loc_234B"),
        (11, "loc_235C"),
        (12, "loc_2376"),
        (SWITCH_DEFAULT, "loc_2387"),
    )


    label("loc_2292")

    ReplaceBGM("ed7100", "ed7103")
    NewScene("t3000", 0, 0, 0)
    IdleLoop()
    Jump("loc_2391")

    label("loc_22A5")

    ReplaceBGM("ed7100", "ed7103")
    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_2391")

    label("loc_22B8")

    ReplaceBGM("ed7100", "ed7103")
    NewScene("r2060", 0, 0, 0)
    IdleLoop()
    Jump("loc_2391")

    label("loc_22CB")

    ReplaceBGM("ed7100", "ed7103")
    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_2391")

    label("loc_22DE")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_2391")

    label("loc_22EC")

    ReplaceBGM("ed7121", "ed7302")
    ReplaceBGM("ed7100", "ed7103")
    NewScene("t0510", 0, 0, 0)
    IdleLoop()
    Jump("loc_2391")

    label("loc_2304")

    NewScene("t0520", 0, 0, 0)
    IdleLoop()
    Jump("loc_2391")

    label("loc_2312")

    NewScene("t052B", 0, 0, 0)
    IdleLoop()
    Jump("loc_2391")

    label("loc_2320")

    SetScenarioFlags(0x5C, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1FF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("r206B", 0, 0, 0)
    IdleLoop()
    Jump("loc_2391")

    label("loc_233A")

    SetScenarioFlags(0x5C, 1)
    NewScene("r206B", 0, 0, 0)
    IdleLoop()
    Jump("loc_2391")

    label("loc_234B")

    SetScenarioFlags(0x5C, 1)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_2391")

    label("loc_235C")

    SetScenarioFlags(0x5C, 4)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_2391")

    label("loc_2376")

    SetScenarioFlags(0x5C, 5)
    NewScene("t150B", 0, 0, 0)
    IdleLoop()
    Jump("loc_2391")

    label("loc_2387")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2391")

    Jump("loc_1FDD")

    label("loc_2396")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_24_1FBF end

    def Function_25_23A4(): pass

    label("Function_25_23A4")

    Call(2, 5)
    Call(2, 6)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_23C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2737")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼プロローグ１\x01",                  # 0
            "②▼プロローグ２\x01",                  # 1
            "③▼プロローグ３\x01",                  # 2
            "④▼支援要請を確認する\x01",            # 3
            "⑤▼フランからの連絡\x01",              # 4
            "⑥▼リーシャと面会\x01",                # 5
            "⑦▼アルカンシェル前に到着\x01",        # 6
            "⑧▼イリアの特訓を目撃\x01",            # 7
            "⑨▼ルバーチェ商会前に来る\x01",        # 8
            "⑩▼イアン弁護士から話を聞く\x01",      # 9
            "?▼黒月貿易公司を訪ねる\x01",           # 10
            "?▼ツァオとの初会見\x01",               # 11
            "?▼マクダエル市長と会う\x01",           # 12
            "?▼イリアとリーシャに報告\x01",         # 13
            "キャンセル\x01",                        # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_2583"),
        (12, "loc_2586"),
        (11, "loc_2589"),
        (10, "loc_258C"),
        (9, "loc_2592"),
        (8, "loc_2595"),
        (7, "loc_259E"),
        (6, "loc_25A4"),
        (5, "loc_25A7"),
        (4, "loc_25AA"),
        (3, "loc_25AD"),
        (2, "loc_25AD"),
        (1, "loc_25AD"),
        (0, "loc_25AD"),
        (SWITCH_DEFAULT, "loc_25C1"),
    )


    label("loc_2583")

    SetScenarioFlags(0x81, 4)

    label("loc_2586")

    SetScenarioFlags(0x81, 3)

    label("loc_2589")

    SetScenarioFlags(0x81, 2)

    label("loc_258C")

    SetScenarioFlags(0x81, 0)
    SetScenarioFlags(0x81, 1)

    label("loc_2592")

    SetScenarioFlags(0x80, 7)

    label("loc_2595")

    SetScenarioFlags(0x80, 5)
    SetScenarioFlags(0x80, 6)
    SetScenarioFlags(0x87, 3)

    label("loc_259E")

    SetScenarioFlags(0x80, 3)
    SetScenarioFlags(0x80, 4)

    label("loc_25A4")

    SetScenarioFlags(0x80, 2)

    label("loc_25A7")

    SetScenarioFlags(0x80, 1)

    label("loc_25AA")

    SetScenarioFlags(0x80, 0)

    label("loc_25AD")

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 52)
    Jump("loc_25C6")

    label("loc_25C1")

    Jump("loc_25C6")

    label("loc_25C6")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2624"),
        (1, "loc_263E"),
        (2, "loc_264F"),
        (3, "loc_2660"),
        (4, "loc_2671"),
        (5, "loc_2682"),
        (6, "loc_2690"),
        (7, "loc_269E"),
        (8, "loc_26AC"),
        (9, "loc_26BA"),
        (10, "loc_26D2"),
        (11, "loc_26EA"),
        (12, "loc_2702"),
        (13, "loc_271A"),
        (SWITCH_DEFAULT, "loc_2728"),
    )


    label("loc_2624")

    SetScenarioFlags(0x5C, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c050B", 0, 0, 0)
    IdleLoop()
    Jump("loc_2732")

    label("loc_263E")

    SetScenarioFlags(0x5C, 0)
    NewScene("c0420", 0, 0, 0)
    IdleLoop()
    Jump("loc_2732")

    label("loc_264F")

    SetScenarioFlags(0x5C, 0)
    NewScene("m0101", 0, 0, 0)
    IdleLoop()
    Jump("loc_2732")

    label("loc_2660")

    SetScenarioFlags(0x5C, 5)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_2732")

    label("loc_2671")

    SetScenarioFlags(0x5C, 6)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_2732")

    label("loc_2682")

    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_2732")

    label("loc_2690")

    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Jump("loc_2732")

    label("loc_269E")

    NewScene("c0420", 0, 0, 0)
    IdleLoop()
    Jump("loc_2732")

    label("loc_26AC")

    NewScene("c0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_2732")

    label("loc_26BA")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0220", 0, 0, 0)
    IdleLoop()
    Jump("loc_2732")

    label("loc_26D2")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Jump("loc_2732")

    label("loc_26EA")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c1210", 102, 0, 0)
    IdleLoop()
    Jump("loc_2732")

    label("loc_2702")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0400", 0, 0, 0)
    IdleLoop()
    Jump("loc_2732")

    label("loc_271A")

    NewScene("c0420", 0, 0, 0)
    IdleLoop()
    Jump("loc_2732")

    label("loc_2728")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2732")

    Jump("loc_23C5")

    label("loc_2737")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_25_23A4 end

    def Function_26_2745(): pass

    label("Function_26_2745")

    Call(2, 5)
    Call(2, 6)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2766")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2B22")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼アーネストが訪ねてくる\x01",       # 0
            "②▼屋上でのエリィとの会話\x01",       # 1
            "③▼《銀》からの依頼\x01",             # 2
            "④▼ＩＢＣビル前に来る\x01",           # 3
            "⑤▼受付に問い合わせる\x01",           # 4
            "⑥▼エレベーターに乗り込む\x01",       # 5
            "⑦▼ディーター＆マリアベル\x01",       # 6
            "⑧▼端末室に向かう\x01",               # 7
            "⑨▼ＩＢＣの端末室に入る\x01",         # 8
            "⑩▼マリアベルとの会話\x01",           # 9
            "?▼ＩＢＣビルから出てくる\x01",        # 10
            "?▼市庁舎の受付で鍵を借りる\x01",      # 11
            "?▼ジオフロントＢ区画に入る\x01",      # 12
            "?▼ヨナの隠れ処を発見\x01",            # 13
            "キャンセル\x01",                       # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_2944"),
        (12, "loc_294D"),
        (11, "loc_2950"),
        (10, "loc_2953"),
        (9, "loc_2956"),
        (8, "loc_2959"),
        (7, "loc_295C"),
        (6, "loc_295F"),
        (5, "loc_2965"),
        (4, "loc_2968"),
        (3, "loc_296B"),
        (2, "loc_296E"),
        (1, "loc_296E"),
        (0, "loc_2971"),
        (SWITCH_DEFAULT, "loc_29B2"),
    )


    label("loc_2944")

    SetScenarioFlags(0x86, 1)
    SetScenarioFlags(0x83, 3)
    SetScenarioFlags(0x83, 4)

    label("loc_294D")

    SetScenarioFlags(0x83, 2)

    label("loc_2950")

    SetScenarioFlags(0x83, 1)

    label("loc_2953")

    SetScenarioFlags(0x83, 0)

    label("loc_2956")

    SetScenarioFlags(0x82, 7)

    label("loc_2959")

    SetScenarioFlags(0x82, 6)

    label("loc_295C")

    SetScenarioFlags(0x82, 5)

    label("loc_295F")

    SetScenarioFlags(0x82, 3)
    SetScenarioFlags(0x82, 4)

    label("loc_2965")

    SetScenarioFlags(0x82, 2)

    label("loc_2968")

    SetScenarioFlags(0x82, 1)

    label("loc_296B")

    SetScenarioFlags(0x82, 0)

    label("loc_296E")

    SetScenarioFlags(0x81, 6)

    label("loc_2971")

    SetScenarioFlags(0x80, 0)
    SetScenarioFlags(0x80, 1)
    SetScenarioFlags(0x80, 2)
    SetScenarioFlags(0x80, 3)
    SetScenarioFlags(0x80, 4)
    SetScenarioFlags(0x87, 3)
    SetScenarioFlags(0x80, 5)
    SetScenarioFlags(0x80, 6)
    SetScenarioFlags(0x80, 7)
    SetScenarioFlags(0x81, 0)
    SetScenarioFlags(0x81, 1)
    SetScenarioFlags(0x81, 2)
    SetScenarioFlags(0x81, 3)
    SetScenarioFlags(0x81, 4)
    SetScenarioFlags(0x81, 5)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 53)
    Jump("loc_29B7")

    label("loc_29B2")

    Jump("loc_29B7")

    label("loc_29B7")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A15"),
        (1, "loc_2A28"),
        (2, "loc_2A48"),
        (3, "loc_2A62"),
        (4, "loc_2A70"),
        (5, "loc_2A7E"),
        (6, "loc_2A8C"),
        (7, "loc_2A9A"),
        (8, "loc_2AAC"),
        (9, "loc_2ABE"),
        (10, "loc_2ACC"),
        (11, "loc_2ADF"),
        (12, "loc_2AF2"),
        (13, "loc_2B05"),
        (SWITCH_DEFAULT, "loc_2B13"),
    )


    label("loc_2A15")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_2B1D")

    label("loc_2A28")

    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c010B", 110, 0, 0)
    IdleLoop()
    Jump("loc_2B1D")

    label("loc_2A48")

    SetScenarioFlags(0x5C, 7)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_2B1D")

    label("loc_2A62")

    NewScene("c1300", 0, 0, 0)
    IdleLoop()
    Jump("loc_2B1D")

    label("loc_2A70")

    NewScene("c1310", 0, 0, 0)
    IdleLoop()
    Jump("loc_2B1D")

    label("loc_2A7E")

    NewScene("c1310", 0, 0, 0)
    IdleLoop()
    Jump("loc_2B1D")

    label("loc_2A8C")

    NewScene("c1340", 0, 0, 0)
    IdleLoop()
    Jump("loc_2B1D")

    label("loc_2A9A")

    AddParty(0x37, 0xFF, 0xFF)
    NewScene("c1330", 0, 0, 0)
    IdleLoop()
    Jump("loc_2B1D")

    label("loc_2AAC")

    AddParty(0x37, 0xFF, 0xFF)
    NewScene("c1320", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B1D")

    label("loc_2ABE")

    NewScene("c1320", 0, 0, 0)
    IdleLoop()
    Jump("loc_2B1D")

    label("loc_2ACC")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("c1300", 0, 0, 0)
    IdleLoop()
    Jump("loc_2B1D")

    label("loc_2ADF")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("c1110", 0, 0, 0)
    IdleLoop()
    Jump("loc_2B1D")

    label("loc_2AF2")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("c0300", 0, 0, 0)
    IdleLoop()
    Jump("loc_2B1D")

    label("loc_2B05")

    NewScene("m0101", 133, 0, 0)
    IdleLoop()
    Jump("loc_2B1D")

    label("loc_2B13")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B1D")

    Jump("loc_2766")

    label("loc_2B22")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_26_2745 end

    def Function_27_2B30(): pass

    label("Function_27_2B30")

    Call(2, 5)
    Call(2, 6)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2B51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F2B")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼星見の塔に向かう\x01",          # 0
            "②▼脇道まで来る\x01",              # 1
            "③▼星見の塔に入る\x01",            # 2
            "④▼ゴーレムとの戦闘後\x01",        # 3
            "⑤▼塔の最上階で銀と戦闘\x01",      # 4
            "⑥▼銀との戦闘後\x01",              # 5
            "⑦▼招待客が集まってくる\x01",      # 6
            "⑧▼開幕、巡回開始\x01",            # 7
            "⑨▼第２幕が始まった\x01",          # 8
            "⑩▼第３幕が始まった\x01",          # 9
            "?▼最終幕が始まった\x01",           # 10
            "?▼グレイスを発見する\x01",         # 11
            "?▼エピローグ１\x01",               # 12
            "?▼エピローグ２\x01",               # 13
            "キャンセル\x01",                    # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_2CEF"),
        (12, "loc_2CEF"),
        (11, "loc_2CEF"),
        (10, "loc_2CF2"),
        (9, "loc_2CFE"),
        (8, "loc_2D0A"),
        (7, "loc_2D16"),
        (6, "loc_2D16"),
        (5, "loc_2D16"),
        (4, "loc_2D16"),
        (3, "loc_2D19"),
        (2, "loc_2D19"),
        (1, "loc_2D22"),
        (0, "loc_2D25"),
        (SWITCH_DEFAULT, "loc_2D99"),
    )


    label("loc_2CEF")

    SetScenarioFlags(0x86, 0)

    label("loc_2CF2")

    SetScenarioFlags(0x85, 4)
    SetScenarioFlags(0x85, 5)
    SetScenarioFlags(0x85, 6)
    SetScenarioFlags(0x85, 7)

    label("loc_2CFE")

    SetScenarioFlags(0x85, 0)
    SetScenarioFlags(0x85, 1)
    SetScenarioFlags(0x85, 2)
    SetScenarioFlags(0x85, 3)

    label("loc_2D0A")

    SetScenarioFlags(0x84, 4)
    SetScenarioFlags(0x84, 5)
    SetScenarioFlags(0x84, 6)
    SetScenarioFlags(0x84, 7)

    label("loc_2D16")

    SetScenarioFlags(0x84, 3)

    label("loc_2D19")

    SetScenarioFlags(0x84, 0)
    SetScenarioFlags(0x84, 1)
    SetScenarioFlags(0x84, 2)

    label("loc_2D22")

    SetScenarioFlags(0x83, 7)

    label("loc_2D25")

    SetScenarioFlags(0x80, 0)
    SetScenarioFlags(0x80, 1)
    SetScenarioFlags(0x80, 2)
    SetScenarioFlags(0x80, 3)
    SetScenarioFlags(0x80, 4)
    SetScenarioFlags(0x87, 3)
    SetScenarioFlags(0x80, 5)
    SetScenarioFlags(0x80, 6)
    SetScenarioFlags(0x80, 7)
    SetScenarioFlags(0x81, 0)
    SetScenarioFlags(0x81, 1)
    SetScenarioFlags(0x81, 2)
    SetScenarioFlags(0x81, 3)
    SetScenarioFlags(0x81, 4)
    SetScenarioFlags(0x81, 5)
    SetScenarioFlags(0x81, 6)
    SetScenarioFlags(0x81, 7)
    SetScenarioFlags(0x82, 0)
    SetScenarioFlags(0x82, 1)
    SetScenarioFlags(0x82, 2)
    SetScenarioFlags(0x82, 3)
    SetScenarioFlags(0x82, 4)
    SetScenarioFlags(0x82, 5)
    SetScenarioFlags(0x82, 6)
    SetScenarioFlags(0x82, 7)
    SetScenarioFlags(0x83, 0)
    SetScenarioFlags(0x83, 1)
    SetScenarioFlags(0x83, 2)
    SetScenarioFlags(0x83, 3)
    SetScenarioFlags(0x83, 4)
    SetScenarioFlags(0x83, 5)
    SetScenarioFlags(0x83, 6)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 54)
    Jump("loc_2D9E")

    label("loc_2D99")

    Jump("loc_2D9E")

    label("loc_2D9E")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2DFC"),
        (1, "loc_2E0F"),
        (2, "loc_2E1D"),
        (3, "loc_2E2F"),
        (4, "loc_2E44"),
        (5, "loc_2E56"),
        (6, "loc_2E70"),
        (7, "loc_2E81"),
        (8, "loc_2E98"),
        (9, "loc_2EAC"),
        (10, "loc_2EC0"),
        (11, "loc_2ED4"),
        (12, "loc_2EF1"),
        (13, "loc_2F02"),
        (SWITCH_DEFAULT, "loc_2F1C"),
    )


    label("loc_2DFC")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("c0300", 0, 0, 0)
    IdleLoop()
    Jump("loc_2F26")

    label("loc_2E0F")

    NewScene("r1520", 0, 0, 0)
    IdleLoop()
    Jump("loc_2F26")

    label("loc_2E1D")

    AddParty(0x8, 0xFF, 0xFF)
    NewScene("m1020", 0, 0, 0)
    IdleLoop()
    Jump("loc_2F26")

    label("loc_2E2F")

    AddParty(0x8, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 0)
    NewScene("m1020", 0, 0, 0)
    IdleLoop()
    Jump("loc_2F26")

    label("loc_2E44")

    AddParty(0x8, 0xFF, 0xFF)
    NewScene("m1099", 0, 0, 0)
    IdleLoop()
    Jump("loc_2F26")

    label("loc_2E56")

    AddParty(0x8, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 0)
    ReplaceBGM("ed7100", "ed7102")
    NewScene("m1099", 0, 0, 0)
    IdleLoop()
    Jump("loc_2F26")

    label("loc_2E70")

    SetScenarioFlags(0x5C, 0)
    NewScene("c040B", 0, 0, 0)
    IdleLoop()
    Jump("loc_2F26")

    label("loc_2E81")

    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    SetScenarioFlags(0x5C, 2)
    NewScene("e3400", 0, 0, 0)
    IdleLoop()
    Jump("loc_2F26")

    label("loc_2E98")

    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    NewScene("c0410", 101, 0, 0)
    IdleLoop()
    Jump("loc_2F26")

    label("loc_2EAC")

    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    NewScene("c0410", 101, 0, 0)
    IdleLoop()
    Jump("loc_2F26")

    label("loc_2EC0")

    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    NewScene("c0410", 101, 0, 0)
    IdleLoop()
    Jump("loc_2F26")

    label("loc_2ED4")

    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x213), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c0410", 105, 0, 0)
    IdleLoop()
    Jump("loc_2F26")

    label("loc_2EF1")

    SetScenarioFlags(0x5D, 2)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_2F26")

    label("loc_2F02")

    SetScenarioFlags(0x5C, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Jump("loc_2F26")

    label("loc_2F1C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F26")

    Jump("loc_2B51")

    label("loc_2F2B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_27_2B30 end

    def Function_28_2F39(): pass

    label("Function_28_2F39")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F5D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3316")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼市庁舎の式典会場\x01",            # 0
            "②▼記念祭\x01",                      # 1
            "③▼アルカンシェル劇場前\x01",        # 2
            "④▼２日目の朝\x01",                  # 3
            "⑤▼フランからの連絡\x01",            # 4
            "⑥▼不良たちのタイマン勝負\x01",      # 5
            "⑦▼旧市街のチェイス１\x01",          # 6
            "⑧▼旧市街のチェイス２\x01",          # 7
            "⑨▼旧市街のチェイス３\x01",          # 8
            "⑩▼３日目の朝\x01",                  # 9
            "?▼ヨナからの連絡\x01",               # 10
            "?▼ヨナから依頼内容を聞く\x01",       # 11
            "?▼ジオフロントＡに到着\x01",         # 12
            "?▼ジオフロントＡ２に到着\x01",       # 13
            "キャンセル\x01",                      # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_310B"),
        (12, "loc_3111"),
        (11, "loc_3117"),
        (10, "loc_311A"),
        (9, "loc_311D"),
        (8, "loc_311D"),
        (7, "loc_311D"),
        (6, "loc_311D"),
        (5, "loc_311D"),
        (4, "loc_3120"),
        (3, "loc_3123"),
        (2, "loc_3123"),
        (1, "loc_3123"),
        (0, "loc_3123"),
        (SWITCH_DEFAULT, "loc_3137"),
    )


    label("loc_310B")

    SetScenarioFlags(0xA0, 6)
    SetScenarioFlags(0xA0, 7)

    label("loc_3111")

    SetScenarioFlags(0xA0, 5)
    SetScenarioFlags(0xA0, 4)

    label("loc_3117")

    SetScenarioFlags(0xA0, 3)

    label("loc_311A")

    SetScenarioFlags(0xA0, 2)

    label("loc_311D")

    SetScenarioFlags(0xA0, 1)

    label("loc_3120")

    SetScenarioFlags(0xA0, 0)

    label("loc_3123")

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 55)
    Jump("loc_313C")

    label("loc_3137")

    Jump("loc_313C")

    label("loc_313C")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_319A"),
        (1, "loc_31AB"),
        (2, "loc_31CA"),
        (3, "loc_31E0"),
        (4, "loc_31FB"),
        (5, "loc_3216"),
        (6, "loc_322E"),
        (7, "loc_3252"),
        (8, "loc_3276"),
        (9, "loc_3291"),
        (10, "loc_32AC"),
        (11, "loc_32C7"),
        (12, "loc_32DF"),
        (13, "loc_32F3"),
        (SWITCH_DEFAULT, "loc_3307"),
    )


    label("loc_319A")

    SetScenarioFlags(0x5C, 1)
    NewScene("c1120", 0, 0, 0)
    IdleLoop()
    Jump("loc_3311")

    label("loc_31AB")

    SetScenarioFlags(0x5C, 0)
    ReplaceBGM("ed7100", "ed7106")
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c110C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3311")

    label("loc_31CA")

    SetScenarioFlags(0x5C, 1)
    ReplaceBGM("ed7100", "ed7106")
    NewScene("c040C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3311")

    label("loc_31E0")

    SetScenarioFlags(0x5C, 6)
    ReplaceBGM("ed7100", "ed7106")
    ReplaceBGM("ed7101", "ed7106")
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3311")

    label("loc_31FB")

    SetScenarioFlags(0x5C, 0)
    ReplaceBGM("ed7100", "ed7106")
    ReplaceBGM("ed7101", "ed7106")
    NewScene("c000C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3311")

    label("loc_3216")

    ReplaceBGM("ed7100", "ed7106")
    ReplaceBGM("ed7101", "ed7106")
    NewScene("c120C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3311")

    label("loc_322E")

    SetScenarioFlags(0x5C, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x206), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7100", "ed7106")
    ReplaceBGM("ed7101", "ed7106")
    NewScene("c140C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3311")

    label("loc_3252")

    SetScenarioFlags(0x5C, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x206), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7100", "ed7106")
    ReplaceBGM("ed7101", "ed7106")
    NewScene("c140C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3311")

    label("loc_3276")

    SetScenarioFlags(0x5C, 2)
    ReplaceBGM("ed7100", "ed7106")
    ReplaceBGM("ed7101", "ed7106")
    NewScene("c140C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3311")

    label("loc_3291")

    SetScenarioFlags(0x5C, 0)
    ReplaceBGM("ed7100", "ed7106")
    ReplaceBGM("ed7101", "ed7106")
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3311")

    label("loc_32AC")

    SetScenarioFlags(0x5C, 0)
    ReplaceBGM("ed7100", "ed7106")
    ReplaceBGM("ed7101", "ed7106")
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3311")

    label("loc_32C7")

    ReplaceBGM("ed7100", "ed7106")
    ReplaceBGM("ed7101", "ed7106")
    NewScene("m0101", 135, 0, 0)
    IdleLoop()
    Jump("loc_3311")

    label("loc_32DF")

    RemoveParty(0x1, 0x0)
    RemoveParty(0x3, 0x0)
    NewScene("m0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_3311")

    label("loc_32F3")

    RemoveParty(0x1, 0x0)
    RemoveParty(0x3, 0x0)
    NewScene("m0010", 103, 0, 0)
    IdleLoop()
    Jump("loc_3311")

    label("loc_3307")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3311")

    Jump("loc_2F5D")

    label("loc_3316")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_28_2F39 end

    def Function_29_3324(): pass

    label("Function_29_3324")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3348")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3777")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼中ボスと遭遇する\x01",            # 0
            "②▼中ボスと戦闘後\x01",              # 1
            "③▼第３制御端末室\x01",              # 2
            "④▼ジオフロントＡから出る\x01",      # 3
            "⑤▼マフィアの情報を確認\x01",        # 4
            "⑥▼４日目の朝（エリィ）\x01",        # 5
            "⑦▼４日目の朝（ティオ）\x01",        # 6
            "⑧▼４日目の朝（ランディ）\x01",      # 7
            "⑨▼フランから連絡２\x01",            # 8
            "⑩▼ヘイワースから話を聞く\x01",      # 9
            "?▼アルカンシェルを確認\x01",         # 10
            "?▼ランディからの連絡\x01",           # 11
            "?▼レンが現れる\x01",                 # 12
            "?▼エリィからの連絡\x01",             # 13
            "キャンセル\x01",                      # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_350A"),
        (12, "loc_3510"),
        (11, "loc_3516"),
        (10, "loc_3519"),
        (9, "loc_351C"),
        (8, "loc_3522"),
        (7, "loc_3525"),
        (6, "loc_3525"),
        (5, "loc_3525"),
        (4, "loc_3525"),
        (3, "loc_3525"),
        (2, "loc_3528"),
        (1, "loc_352B"),
        (0, "loc_352B"),
        (SWITCH_DEFAULT, "loc_355D"),
    )


    label("loc_350A")

    SetScenarioFlags(0xA2, 1)
    SetScenarioFlags(0xB9, 4)

    label("loc_3510")

    SetScenarioFlags(0xA2, 0)
    SetScenarioFlags(0xB9, 3)

    label("loc_3516")

    SetScenarioFlags(0xA1, 7)

    label("loc_3519")

    SetScenarioFlags(0xA1, 6)

    label("loc_351C")

    SetScenarioFlags(0xA1, 5)
    SetScenarioFlags(0xAA, 2)

    label("loc_3522")

    SetScenarioFlags(0xA1, 4)

    label("loc_3525")

    SetScenarioFlags(0xA1, 3)

    label("loc_3528")

    SetScenarioFlags(0xA1, 2)

    label("loc_352B")

    SetScenarioFlags(0xA0, 0)
    SetScenarioFlags(0xA0, 1)
    SetScenarioFlags(0xA0, 2)
    SetScenarioFlags(0xA0, 3)
    SetScenarioFlags(0xA0, 4)
    SetScenarioFlags(0xA0, 5)
    SetScenarioFlags(0xA0, 6)
    SetScenarioFlags(0xA0, 7)
    SetScenarioFlags(0xA1, 0)
    SetScenarioFlags(0xA1, 1)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 56)
    Jump("loc_3562")

    label("loc_355D")

    Jump("loc_3562")

    label("loc_3562")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3581")
    RemoveParty(0x1, 0x0)
    RemoveParty(0x3, 0x0)

    label("loc_3581")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35A3")
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)

    label("loc_35A3")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3601"),
        (1, "loc_360F"),
        (2, "loc_3620"),
        (3, "loc_362E"),
        (4, "loc_3646"),
        (5, "loc_3657"),
        (6, "loc_3683"),
        (7, "loc_36AF"),
        (8, "loc_36DB"),
        (9, "loc_36EC"),
        (10, "loc_3704"),
        (11, "loc_371C"),
        (12, "loc_3734"),
        (13, "loc_374C"),
        (SWITCH_DEFAULT, "loc_3768"),
    )


    label("loc_3601")

    NewScene("m0013", 0, 0, 0)
    IdleLoop()
    Jump("loc_3772")

    label("loc_360F")

    SetScenarioFlags(0x5C, 0)
    NewScene("m0013", 0, 0, 0)
    IdleLoop()
    Jump("loc_3772")

    label("loc_3620")

    NewScene("m0013", 0, 0, 0)
    IdleLoop()
    Jump("loc_3772")

    label("loc_362E")

    ReplaceBGM("ed7100", "ed7106")
    ReplaceBGM("ed7101", "ed7106")
    NewScene("c000C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3772")

    label("loc_3646")

    SetScenarioFlags(0x5C, 5)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Jump("loc_3772")

    label("loc_3657")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 2)
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3772")

    label("loc_3683")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 2)
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3772")

    label("loc_36AF")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 2)
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3772")

    label("loc_36DB")

    SetScenarioFlags(0x5C, 1)
    NewScene("c100C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3772")

    label("loc_36EC")

    ReplaceBGM("ed7100", "ed7104")
    ReplaceBGM("ed7101", "ed7104")
    NewScene("c110C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3772")

    label("loc_3704")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c041C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3772")

    label("loc_371C")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c050C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3772")

    label("loc_3734")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c050C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3772")

    label("loc_374C")

    AddParty(0x5F, 0xFF, 0xFF)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3772")

    label("loc_3768")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3772")

    Jump("loc_3348")

    label("loc_3777")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_29_3324 end

    def Function_30_3785(): pass

    label("Function_30_3785")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_37A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3BCF")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼デパートに入った\x01",            # 0
            "②▼ティオからの連絡\x01",            # 1
            "③▼ゲートをチェック\x01",            # 2
            "④▼Ｒ＆Ｔからの連絡\x01",            # 3
            "⑤▼Ｅ＆Ｔからの連絡\x01",            # 4
            "⑥▼端末を操作しているレン\x01",      # 5
            "⑦▼西口から街道に出る\x01",          # 6
            "⑧▼運搬車を発見する\x01",            # 7
            "⑨▼子供の歓声を聞く\x01",            # 8
            "⑩▼コリン発見\x01",                  # 9
            "?▼コリン発見、戦闘後\x01",           # 10
            "?▼ロイドの私室\x01",                 # 11
            "?▼ロイドの私室２\x01",               # 12
            "?▼最終日の朝\x01",                   # 13
            "キャンセル\x01",                      # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_3947"),
        (12, "loc_3947"),
        (11, "loc_3947"),
        (10, "loc_3947"),
        (9, "loc_3947"),
        (8, "loc_394A"),
        (7, "loc_394D"),
        (6, "loc_3950"),
        (5, "loc_3953"),
        (4, "loc_3953"),
        (3, "loc_3959"),
        (2, "loc_395F"),
        (1, "loc_3962"),
        (0, "loc_3968"),
        (SWITCH_DEFAULT, "loc_39BE"),
    )


    label("loc_3947")

    SetScenarioFlags(0xA3, 2)

    label("loc_394A")

    SetScenarioFlags(0xA3, 1)

    label("loc_394D")

    SetScenarioFlags(0xA3, 0)

    label("loc_3950")

    SetScenarioFlags(0xA2, 7)

    label("loc_3953")

    SetScenarioFlags(0xA2, 6)
    SetScenarioFlags(0xB9, 7)

    label("loc_3959")

    SetScenarioFlags(0xA2, 5)
    SetScenarioFlags(0xB9, 6)

    label("loc_395F")

    SetScenarioFlags(0xA2, 4)

    label("loc_3962")

    SetScenarioFlags(0xA2, 3)
    SetScenarioFlags(0xB9, 5)

    label("loc_3968")

    SetScenarioFlags(0xA0, 0)
    SetScenarioFlags(0xA0, 1)
    SetScenarioFlags(0xA0, 2)
    SetScenarioFlags(0xA0, 3)
    SetScenarioFlags(0xA0, 4)
    SetScenarioFlags(0xA0, 5)
    SetScenarioFlags(0xA0, 6)
    SetScenarioFlags(0xA0, 7)
    SetScenarioFlags(0xA1, 0)
    SetScenarioFlags(0xA1, 1)
    SetScenarioFlags(0xA1, 2)
    SetScenarioFlags(0xA1, 3)
    SetScenarioFlags(0xA1, 4)
    SetScenarioFlags(0xA1, 5)
    SetScenarioFlags(0xAA, 2)
    SetScenarioFlags(0xA1, 6)
    SetScenarioFlags(0xA1, 7)
    SetScenarioFlags(0xB9, 3)
    SetScenarioFlags(0xA2, 0)
    SetScenarioFlags(0xB9, 4)
    SetScenarioFlags(0xA2, 1)
    SetScenarioFlags(0xA2, 2)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 57)
    Jump("loc_39C3")

    label("loc_39BE")

    Jump("loc_39C3")

    label("loc_39C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39E5")
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)

    label("loc_39E5")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3A43"),
        (1, "loc_3A5F"),
        (2, "loc_3A7B"),
        (3, "loc_3A97"),
        (4, "loc_3AB3"),
        (5, "loc_3ACF"),
        (6, "loc_3AEE"),
        (7, "loc_3B0A"),
        (8, "loc_3B26"),
        (9, "loc_3B42"),
        (10, "loc_3B54"),
        (11, "loc_3B69"),
        (12, "loc_3B87"),
        (13, "loc_3BA5"),
        (SWITCH_DEFAULT, "loc_3BC0"),
    )


    label("loc_3A43")

    AddParty(0x5F, 0xFF, 0xFF)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c017C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3BCA")

    label("loc_3A5F")

    AddParty(0x5F, 0xFF, 0xFF)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c000C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3BCA")

    label("loc_3A7B")

    AddParty(0x5F, 0xFF, 0xFF)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c000C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3BCA")

    label("loc_3A97")

    AddParty(0x5F, 0xFF, 0xFF)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3BCA")

    label("loc_3AB3")

    AddParty(0x5F, 0xFF, 0xFF)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c020C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3BCA")

    label("loc_3ACF")

    AddParty(0x5F, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 3)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3BCA")

    label("loc_3AEE")

    AddParty(0x5F, 0xFF, 0xFF)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_3BCA")

    label("loc_3B0A")

    AddParty(0x5F, 0xFF, 0xFF)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("r1020", 0, 0, 0)
    IdleLoop()
    Jump("loc_3BCA")

    label("loc_3B26")

    AddParty(0x5F, 0xFF, 0xFF)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("r1030", 0, 0, 0)
    IdleLoop()
    Jump("loc_3BCA")

    label("loc_3B42")

    AddParty(0x5F, 0xFF, 0xFF)
    NewScene("r1030", 0, 0, 0)
    IdleLoop()
    Jump("loc_3BCA")

    label("loc_3B54")

    AddParty(0x5F, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 0)
    NewScene("r1030", 0, 0, 0)
    IdleLoop()
    Jump("loc_3BCA")

    label("loc_3B69")

    AddParty(0x5F, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 2)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x20B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3BCA")

    label("loc_3B87")

    AddParty(0x5F, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 5)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x202), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3BCA")

    label("loc_3BA5")

    SetScenarioFlags(0x5C, 1)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Jump("loc_3BCA")

    label("loc_3BC0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3BCA")

    Jump("loc_37A9")

    label("loc_3BCF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_30_3785 end

    def Function_31_3BDD(): pass

    label("Function_31_3BDD")

    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)

    Menu(
        2,
        -1,
        -1,
        0,
        (
            "☆パートナー?エリィ\x01",        # 0
            "☆パートナー?ティオ\x01",        # 1
            "☆パートナー?ランディ\x01",      # 2
        )
    )

    MenuEnd(0x5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_3C4C"),
        (1, "loc_3C5E"),
        (2, "loc_3C70"),
        (SWITCH_DEFAULT, "loc_3C82"),
    )


    label("loc_3C4C")

    SetScenarioFlags(0xA9, 1)
    ClearScenarioFlags(0xA9, 2)
    ClearScenarioFlags(0xA9, 3)
    AddParty(0x1, 0xEF, 0xFF)
    Jump("loc_3C82")

    label("loc_3C5E")

    ClearScenarioFlags(0xA9, 1)
    SetScenarioFlags(0xA9, 2)
    ClearScenarioFlags(0xA9, 3)
    AddParty(0x2, 0xEF, 0xFF)
    Jump("loc_3C82")

    label("loc_3C70")

    ClearScenarioFlags(0xA9, 1)
    ClearScenarioFlags(0xA9, 2)
    SetScenarioFlags(0xA9, 3)
    AddParty(0x3, 0xEF, 0xFF)
    Jump("loc_3C82")

    label("loc_3C82")

    Return()

    # Function_31_3BDD end

    def Function_32_3C83(): pass

    label("Function_32_3C83")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3CA7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40E2")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼水上バスに乗り込む\x01",        # 0
            "②▼水上バス内の会話\x01",          # 1
            "③▼ミシュラムに到着\x01",          # 2
            "④▼議長邸を確認\x01",              # 3
            "⑤▼テーマパークを確認\x01",        # 4
            "⑥▼情報を整理する\x01",            # 5
            "⑦▼ワジの部屋\x01",                # 6
            "⑧▼ブティックに入る\x01",          # 7
            "⑨▼オークションに向かう\x01",      # 8
            "⑩▼オークションに到着\x01",        # 9
            "?▼会場のチェック\x01",             # 10
            "?▼マリアベル登場\x01",             # 11
            "?▼オークション開始\x01",           # 12
            "?▼《銀》との遭遇\x01",             # 13
            "キャンセル\x01",                    # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (13, "loc_3E45"),
        (12, "loc_3E48"),
        (11, "loc_3E4B"),
        (10, "loc_3E63"),
        (9, "loc_3E66"),
        (8, "loc_3E69"),
        (7, "loc_3E69"),
        (6, "loc_3E6C"),
        (5, "loc_3E72"),
        (4, "loc_3E7B"),
        (3, "loc_3E7B"),
        (2, "loc_3E7E"),
        (1, "loc_3E84"),
        (0, "loc_3E8A"),
        (SWITCH_DEFAULT, "loc_3F04"),
    )


    label("loc_3E45")

    SetScenarioFlags(0xA6, 2)

    label("loc_3E48")

    SetScenarioFlags(0xA6, 1)

    label("loc_3E4B")

    SetScenarioFlags(0xA5, 1)
    SetScenarioFlags(0xA5, 2)
    SetScenarioFlags(0xA5, 3)
    SetScenarioFlags(0xA5, 4)
    SetScenarioFlags(0xA5, 5)
    SetScenarioFlags(0xA5, 6)
    SetScenarioFlags(0xA5, 7)
    SetScenarioFlags(0xA6, 0)

    label("loc_3E63")

    SetScenarioFlags(0xA5, 0)

    label("loc_3E66")

    SetScenarioFlags(0xA4, 7)

    label("loc_3E69")

    SetScenarioFlags(0xA4, 6)

    label("loc_3E6C")

    SetScenarioFlags(0xA4, 4)
    SetScenarioFlags(0xA4, 5)

    label("loc_3E72")

    SetScenarioFlags(0xA4, 1)
    SetScenarioFlags(0xA4, 2)
    SetScenarioFlags(0xA4, 3)

    label("loc_3E7B")

    SetScenarioFlags(0xA4, 0)

    label("loc_3E7E")

    SetScenarioFlags(0xA3, 6)
    SetScenarioFlags(0xA3, 7)

    label("loc_3E84")

    SetScenarioFlags(0xA3, 4)
    SetScenarioFlags(0xA3, 5)

    label("loc_3E8A")

    SetScenarioFlags(0xA0, 0)
    SetScenarioFlags(0xA0, 1)
    SetScenarioFlags(0xA0, 2)
    SetScenarioFlags(0xA0, 3)
    SetScenarioFlags(0xA0, 4)
    SetScenarioFlags(0xA0, 5)
    SetScenarioFlags(0xA0, 6)
    SetScenarioFlags(0xA0, 7)
    SetScenarioFlags(0xA1, 0)
    SetScenarioFlags(0xA1, 1)
    SetScenarioFlags(0xA1, 2)
    SetScenarioFlags(0xA1, 3)
    SetScenarioFlags(0xA1, 4)
    SetScenarioFlags(0xA1, 5)
    SetScenarioFlags(0xAA, 2)
    SetScenarioFlags(0xA1, 6)
    SetScenarioFlags(0xA1, 7)
    SetScenarioFlags(0xB9, 3)
    SetScenarioFlags(0xA2, 0)
    SetScenarioFlags(0xB9, 4)
    SetScenarioFlags(0xA2, 1)
    SetScenarioFlags(0xA2, 2)
    SetScenarioFlags(0xA2, 3)
    SetScenarioFlags(0xB9, 5)
    SetScenarioFlags(0xA2, 4)
    SetScenarioFlags(0xA2, 5)
    SetScenarioFlags(0xB9, 6)
    SetScenarioFlags(0xA2, 6)
    SetScenarioFlags(0xB9, 7)
    SetScenarioFlags(0xA2, 7)
    SetScenarioFlags(0xA3, 0)
    SetScenarioFlags(0xA3, 1)
    SetScenarioFlags(0xA3, 2)
    SetScenarioFlags(0xA3, 3)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 58)
    Jump("loc_3F09")

    label("loc_3F04")

    Jump("loc_3F09")

    label("loc_3F09")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3F67"),
        (1, "loc_3F7F"),
        (2, "loc_3F8D"),
        (3, "loc_3F9E"),
        (4, "loc_3FAC"),
        (5, "loc_3FBA"),
        (6, "loc_3FC8"),
        (7, "loc_3FD6"),
        (8, "loc_3FE8"),
        (9, "loc_4039"),
        (10, "loc_4087"),
        (11, "loc_4098"),
        (12, "loc_40A9"),
        (13, "loc_40BE"),
        (SWITCH_DEFAULT, "loc_40D3"),
    )


    label("loc_3F67")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c120C", 0, 0, 0)
    IdleLoop()
    Jump("loc_40DD")

    label("loc_3F7F")

    NewScene("e0510", 0, 0, 0)
    IdleLoop()
    Jump("loc_40DD")

    label("loc_3F8D")

    SetScenarioFlags(0x5C, 0)
    NewScene("t1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_40DD")

    label("loc_3F9E")

    NewScene("t1100", 0, 0, 0)
    IdleLoop()
    Jump("loc_40DD")

    label("loc_3FAC")

    NewScene("t1030", 100, 0, 0)
    IdleLoop()
    Jump("loc_40DD")

    label("loc_3FBA")

    NewScene("t1020", 0, 0, 0)
    IdleLoop()
    Jump("loc_40DD")

    label("loc_3FC8")

    NewScene("t1050", 107, 0, 0)
    IdleLoop()
    Jump("loc_40DD")

    label("loc_3FD6")

    AddParty(0x50, 0xFF, 0xFF)
    NewScene("t1040", 100, 0, 0)
    IdleLoop()
    Jump("loc_40DD")

    label("loc_3FE8")

    Call(2, 31)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4001")
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_4028")

    label("loc_4001")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4017")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_4028")

    label("loc_4017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4028")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)

    label("loc_4028")

    SetScenarioFlags(0x5C, 0)
    NewScene("e3110", 0, 0, 0)
    IdleLoop()
    Jump("loc_40DD")

    label("loc_4039")

    Call(2, 31)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 1)), scpexpr(EXPR_END)), "loc_4052")
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_4079")

    label("loc_4052")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 2)), scpexpr(EXPR_END)), "loc_4068")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    Jump("loc_4079")

    label("loc_4068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 3)), scpexpr(EXPR_END)), "loc_4079")
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)

    label("loc_4079")

    NewScene("t110B", 0, 0, 0)
    IdleLoop()
    Jump("loc_40DD")

    label("loc_4087")

    Call(2, 31)
    NewScene("t111B", 0, 0, 0)
    IdleLoop()
    Jump("loc_40DD")

    label("loc_4098")

    Call(2, 31)
    NewScene("t111B", 0, 0, 0)
    IdleLoop()
    Jump("loc_40DD")

    label("loc_40A9")

    Call(2, 31)
    AddParty(0x37, 0xFF, 0xFF)
    NewScene("t112B", 0, 0, 0)
    IdleLoop()
    Jump("loc_40DD")

    label("loc_40BE")

    Call(2, 31)
    AddParty(0x50, 0xFF, 0xFF)
    NewScene("t111B", 0, 0, 0)
    IdleLoop()
    Jump("loc_40DD")

    label("loc_40D3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_40DD")

    Jump("loc_3CA7")

    label("loc_40E2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_32_3C83 end

    def Function_33_40F0(): pass

    label("Function_33_40F0")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4114")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_44FC")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼宝物室に入る\x01",            # 0
            "②▼脱出開始\x01",                # 1
            "③▼玄関広間が封鎖右\x01",        # 2
            "④▼玄関広間が封鎖左\x01",        # 3
            "⑤▼議長の居室に入る\x01",        # 4
            "⑥▼玄関広間を強行突破\x01",      # 5
            "⑦▼強行突破、戦闘後\x01",        # 6
            "⑧▼街区での戦い\x01",            # 7
            "⑨▼アーケードでの戦い\x01",      # 8
            "⑩▼ガルシアと戦闘\x01",          # 9
            "?▼ガルシアと戦闘後\x01",         # 10
            "キャンセル\x01",                  # 11
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (10, "loc_425E"),
        (9, "loc_425E"),
        (8, "loc_4261"),
        (7, "loc_4264"),
        (6, "loc_426A"),
        (5, "loc_426A"),
        (4, "loc_426D"),
        (3, "loc_4270"),
        (2, "loc_4276"),
        (1, "loc_4279"),
        (0, "loc_427F"),
        (SWITCH_DEFAULT, "loc_4332"),
    )


    label("loc_425E")

    SetScenarioFlags(0xA7, 5)

    label("loc_4261")

    SetScenarioFlags(0xA7, 4)

    label("loc_4264")

    SetScenarioFlags(0xA7, 3)
    SetScenarioFlags(0x5A, 3)

    label("loc_426A")

    SetScenarioFlags(0xA7, 2)

    label("loc_426D")

    SetScenarioFlags(0xA7, 1)

    label("loc_4270")

    SetScenarioFlags(0xA6, 7)
    SetScenarioFlags(0xA7, 0)

    label("loc_4276")

    SetScenarioFlags(0xA6, 6)

    label("loc_4279")

    SetScenarioFlags(0xA6, 4)
    SetScenarioFlags(0xA6, 5)

    label("loc_427F")

    SetScenarioFlags(0xA0, 0)
    SetScenarioFlags(0xA0, 1)
    SetScenarioFlags(0xA0, 2)
    SetScenarioFlags(0xA0, 3)
    SetScenarioFlags(0xA0, 4)
    SetScenarioFlags(0xA0, 5)
    SetScenarioFlags(0xA0, 6)
    SetScenarioFlags(0xA0, 7)
    SetScenarioFlags(0xA1, 0)
    SetScenarioFlags(0xA1, 1)
    SetScenarioFlags(0xA1, 2)
    SetScenarioFlags(0xA1, 3)
    SetScenarioFlags(0xA1, 4)
    SetScenarioFlags(0xA1, 5)
    SetScenarioFlags(0xAA, 2)
    SetScenarioFlags(0xA1, 6)
    SetScenarioFlags(0xA1, 7)
    SetScenarioFlags(0xA2, 0)
    SetScenarioFlags(0xA2, 1)
    SetScenarioFlags(0xA2, 2)
    SetScenarioFlags(0xA2, 3)
    SetScenarioFlags(0xA2, 4)
    SetScenarioFlags(0xA2, 5)
    SetScenarioFlags(0xA2, 6)
    SetScenarioFlags(0xA2, 7)
    SetScenarioFlags(0xA3, 0)
    SetScenarioFlags(0xA3, 1)
    SetScenarioFlags(0xA3, 2)
    SetScenarioFlags(0xA3, 3)
    SetScenarioFlags(0xA3, 4)
    SetScenarioFlags(0xA3, 5)
    SetScenarioFlags(0xA3, 6)
    SetScenarioFlags(0xA3, 7)
    SetScenarioFlags(0xA4, 0)
    SetScenarioFlags(0xA4, 1)
    SetScenarioFlags(0xA4, 2)
    SetScenarioFlags(0xA4, 3)
    SetScenarioFlags(0xA4, 4)
    SetScenarioFlags(0xA4, 5)
    SetScenarioFlags(0xA4, 6)
    SetScenarioFlags(0xA4, 7)
    SetScenarioFlags(0xA5, 0)
    SetScenarioFlags(0xA5, 1)
    SetScenarioFlags(0xA5, 2)
    SetScenarioFlags(0xA5, 3)
    SetScenarioFlags(0xA5, 4)
    SetScenarioFlags(0xA5, 5)
    SetScenarioFlags(0xA5, 6)
    SetScenarioFlags(0xA5, 7)
    SetScenarioFlags(0xA6, 0)
    SetScenarioFlags(0xA6, 1)
    SetScenarioFlags(0xA6, 2)
    SetScenarioFlags(0xA6, 3)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 59)
    Jump("loc_4337")

    label("loc_4332")

    Jump("loc_4337")

    label("loc_4337")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4353")
    Call(2, 31)

    label("loc_4353")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4374")
    AddParty(0x4, 0xFF, 0xFF)
    AddParty(0x32, 0xFF, 0xFF)

    label("loc_4374")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4395")
    SetChrChipPat(0x0, 0x1, 0x9A)
    LoadChrChipPat()

    label("loc_4395")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_43E1"),
        (1, "loc_43FC"),
        (2, "loc_4414"),
        (3, "loc_442C"),
        (4, "loc_4444"),
        (5, "loc_445C"),
        (6, "loc_4474"),
        (7, "loc_448F"),
        (8, "loc_44A7"),
        (9, "loc_44BF"),
        (10, "loc_44D7"),
        (SWITCH_DEFAULT, "loc_44ED"),
    )


    label("loc_43E1")

    AddParty(0x50, 0xFF, 0xFF)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("t116B", 0, 0, 0)
    IdleLoop()
    Jump("loc_44F7")

    label("loc_43FC")

    ReplaceBGM("ed7513", "ed7509")
    ReplaceBGM("ed7125", "ed7509")
    NewScene("t116B", 0, 0, 0)
    IdleLoop()
    Jump("loc_44F7")

    label("loc_4414")

    ReplaceBGM("ed7513", "ed7509")
    ReplaceBGM("ed7125", "ed7509")
    NewScene("t119B", 102, 0, 0)
    IdleLoop()
    Jump("loc_44F7")

    label("loc_442C")

    ReplaceBGM("ed7513", "ed7509")
    ReplaceBGM("ed7125", "ed7509")
    NewScene("t119B", 103, 0, 0)
    IdleLoop()
    Jump("loc_44F7")

    label("loc_4444")

    ReplaceBGM("ed7513", "ed7509")
    ReplaceBGM("ed7125", "ed7509")
    NewScene("t121B", 106, 0, 0)
    IdleLoop()
    Jump("loc_44F7")

    label("loc_445C")

    ReplaceBGM("ed7513", "ed7509")
    ReplaceBGM("ed7125", "ed7509")
    NewScene("t111B", 0, 0, 0)
    IdleLoop()
    Jump("loc_44F7")

    label("loc_4474")

    ReplaceBGM("ed7513", "ed7509")
    ReplaceBGM("ed7125", "ed7509")
    SetScenarioFlags(0x5C, 4)
    NewScene("t111B", 0, 0, 0)
    IdleLoop()
    Jump("loc_44F7")

    label("loc_448F")

    ReplaceBGM("ed7513", "ed7509")
    ReplaceBGM("ed7125", "ed7509")
    NewScene("t101B", 0, 0, 0)
    IdleLoop()
    Jump("loc_44F7")

    label("loc_44A7")

    ReplaceBGM("ed7513", "ed7509")
    ReplaceBGM("ed7125", "ed7509")
    NewScene("t102B", 0, 0, 0)
    IdleLoop()
    Jump("loc_44F7")

    label("loc_44BF")

    ReplaceBGM("ed7513", "ed7509")
    ReplaceBGM("ed7125", "ed7509")
    NewScene("t100B", 0, 0, 0)
    IdleLoop()
    Jump("loc_44F7")

    label("loc_44D7")

    SetScenarioFlags(0x5C, 0)
    ReplaceBGM("ed7513", "ed7509")
    NewScene("t100B", 0, 0, 0)
    IdleLoop()
    Jump("loc_44F7")

    label("loc_44ED")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_44F7")

    Jump("loc_4114")

    label("loc_44FC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_33_40F0 end

    def Function_34_450A(): pass

    label("Function_34_450A")

    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)

    Menu(
        2,
        -1,
        -1,
        0,
        (
            "☆パートナー?エリィ\x01",        # 0
            "☆パートナー?ティオ\x01",        # 1
            "☆パートナー?ランディ\x01",      # 2
        )
    )

    MenuEnd(0x5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_4579"),
        (1, "loc_458B"),
        (2, "loc_459D"),
        (SWITCH_DEFAULT, "loc_45AF"),
    )


    label("loc_4579")

    SetScenarioFlags(0xA9, 4)
    ClearScenarioFlags(0xA9, 5)
    ClearScenarioFlags(0xA9, 6)
    AddParty(0x1, 0xEF, 0xFF)
    Jump("loc_45AF")

    label("loc_458B")

    ClearScenarioFlags(0xA9, 4)
    SetScenarioFlags(0xA9, 5)
    ClearScenarioFlags(0xA9, 6)
    AddParty(0x2, 0xEF, 0xFF)
    Jump("loc_45AF")

    label("loc_459D")

    ClearScenarioFlags(0xA9, 4)
    ClearScenarioFlags(0xA9, 5)
    SetScenarioFlags(0xA9, 6)
    AddParty(0x3, 0xEF, 0xFF)
    Jump("loc_45AF")

    label("loc_45AF")

    Return()

    # Function_34_450A end

    def Function_35_45B0(): pass

    label("Function_35_45B0")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_45D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4934")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼状況整理\x01",                   # 0
            "②▼中央広場に出る\x01",             # 1
            "③▼遊撃士協会を訪問\x01",           # 2
            "④▼大聖堂に到着\x01",               # 3
            "⑤▼シスターに相談\x01",             # 4
            "⑥▼大聖堂から出る\x01",             # 5
            "⑦▼バスに乗り込む\x01",             # 6
            "⑧▼病院に到着\x01",                 # 7
            "⑨▼セシルと再会する\x01",           # 8
            "⑩▼ヨアヒムの研究室\x01",           # 9
            "?▼キーアとシズクが出会う\x01",      # 10
            "?▼キーアたちを発見\x01",            # 11
            "?▼ルバーチェでの密談\x01",          # 12
            "キャンセル\x01",                     # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (12, "loc_4751"),
        (11, "loc_4751"),
        (10, "loc_4754"),
        (9, "loc_475A"),
        (8, "loc_475D"),
        (7, "loc_4760"),
        (6, "loc_4760"),
        (5, "loc_4763"),
        (4, "loc_4766"),
        (3, "loc_4769"),
        (2, "loc_476C"),
        (1, "loc_476F"),
        (0, "loc_4772"),
        (SWITCH_DEFAULT, "loc_4786"),
    )


    label("loc_4751")

    SetScenarioFlags(0xA9, 0)

    label("loc_4754")

    SetScenarioFlags(0xA8, 6)
    SetScenarioFlags(0xA8, 7)

    label("loc_475A")

    SetScenarioFlags(0xA8, 5)

    label("loc_475D")

    SetScenarioFlags(0xA8, 4)

    label("loc_4760")

    SetScenarioFlags(0xA8, 3)

    label("loc_4763")

    SetScenarioFlags(0xA8, 2)

    label("loc_4766")

    SetScenarioFlags(0xA8, 1)

    label("loc_4769")

    SetScenarioFlags(0xA8, 0)

    label("loc_476C")

    SetScenarioFlags(0xA7, 7)

    label("loc_476F")

    SetScenarioFlags(0xA7, 6)

    label("loc_4772")

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 59)
    Jump("loc_478B")

    label("loc_4786")

    Jump("loc_478B")

    label("loc_478B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47A8")
    AddParty(0x52, 0xFF, 0xFF)

    label("loc_47A8")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4800"),
        (1, "loc_4811"),
        (2, "loc_482C"),
        (3, "loc_4847"),
        (4, "loc_4862"),
        (5, "loc_487D"),
        (6, "loc_4898"),
        (7, "loc_48B3"),
        (8, "loc_48C7"),
        (9, "loc_48D8"),
        (10, "loc_48E9"),
        (11, "loc_48FA"),
        (12, "loc_490B"),
        (SWITCH_DEFAULT, "loc_4925"),
    )


    label("loc_4800")

    SetScenarioFlags(0x5D, 3)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_492F")

    label("loc_4811")

    Call(2, 34)
    ReplaceBGM("ed7100", "ed7105")
    ReplaceBGM("ed7101", "ed7105")
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_492F")

    label("loc_482C")

    Call(2, 34)
    ReplaceBGM("ed7100", "ed7105")
    ReplaceBGM("ed7101", "ed7105")
    NewScene("c1010", 0, 0, 0)
    IdleLoop()
    Jump("loc_492F")

    label("loc_4847")

    Call(2, 34)
    ReplaceBGM("ed7100", "ed7105")
    ReplaceBGM("ed7101", "ed7105")
    NewScene("t4000", 0, 0, 0)
    IdleLoop()
    Jump("loc_492F")

    label("loc_4862")

    Call(2, 34)
    ReplaceBGM("ed7100", "ed7105")
    ReplaceBGM("ed7101", "ed7105")
    NewScene("t4010", 0, 0, 0)
    IdleLoop()
    Jump("loc_492F")

    label("loc_487D")

    Call(2, 34)
    ReplaceBGM("ed7100", "ed7105")
    ReplaceBGM("ed7101", "ed7105")
    NewScene("t4000", 0, 0, 0)
    IdleLoop()
    Jump("loc_492F")

    label("loc_4898")

    Call(2, 34)
    ReplaceBGM("ed7100", "ed7105")
    ReplaceBGM("ed7101", "ed7105")
    NewScene("r1500", 100, 0, 0)
    IdleLoop()
    Jump("loc_492F")

    label("loc_48B3")

    Call(2, 34)
    SetScenarioFlags(0x5C, 1)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_492F")

    label("loc_48C7")

    Call(2, 34)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_492F")

    label("loc_48D8")

    Call(2, 34)
    NewScene("t1650", 0, 0, 0)
    IdleLoop()
    Jump("loc_492F")

    label("loc_48E9")

    Call(2, 34)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_492F")

    label("loc_48FA")

    Call(2, 34)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_492F")

    label("loc_490B")

    SetScenarioFlags(0x5C, 3)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x73), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Jump("loc_492F")

    label("loc_4925")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_492F")

    Jump("loc_45D7")

    label("loc_4934")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_35_45B0 end

    def Function_36_4942(): pass

    label("Function_36_4942")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_496C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4CAA")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼料理を手伝うキーア\x01",          # 0
            "②▼北口に停車している車\x01",        # 1
            "③▼トンネル途中にある分岐\x01",      # 2
            "④▼月の僧院前に到着\x01",            # 3
            "⑤▼礼拝堂に到着\x01",                # 4
            "⑥▼戦闘後、礼拝堂に\x01",            # 5
            "⑦▼儀式の間に到着\x01",              # 6
            "⑧▼戦闘後、儀式の間\x01",            # 7
            "⑨▼鐘の共鳴を止める\x01",            # 8
            "⑩▼礼拝堂に戻ってくる\x01",          # 9
            "?▼フランからの連絡\x01",             # 10
            "?▼マインツに到着\x01",               # 11
            "?▼町長宅を訪ねる\x01",               # 12
            "キャンセル\x01",                      # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (12, "loc_4AFC"),
        (11, "loc_4AFF"),
        (10, "loc_4B02"),
        (9, "loc_4B05"),
        (8, "loc_4B08"),
        (7, "loc_4B0B"),
        (6, "loc_4B0B"),
        (5, "loc_4B0E"),
        (4, "loc_4B0E"),
        (3, "loc_4B11"),
        (2, "loc_4B14"),
        (1, "loc_4B17"),
        (0, "loc_4B23"),
        (SWITCH_DEFAULT, "loc_4B37"),
    )


    label("loc_4AFC")

    SetScenarioFlags(0xC1, 1)

    label("loc_4AFF")

    SetScenarioFlags(0xC1, 0)

    label("loc_4B02")

    SetScenarioFlags(0xC0, 7)

    label("loc_4B05")

    SetScenarioFlags(0xC0, 6)

    label("loc_4B08")

    SetScenarioFlags(0xC0, 5)

    label("loc_4B0B")

    SetScenarioFlags(0xC0, 4)

    label("loc_4B0E")

    SetScenarioFlags(0xC0, 3)

    label("loc_4B11")

    SetScenarioFlags(0xC0, 2)

    label("loc_4B14")

    SetScenarioFlags(0xC0, 1)

    label("loc_4B17")

    SetScenarioFlags(0xC0, 0)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4B23")

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 60)
    Jump("loc_4B3C")

    label("loc_4B37")

    Jump("loc_4B3C")

    label("loc_4B3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B59")
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_4B59")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4BB1"),
        (1, "loc_4BC2"),
        (2, "loc_4BD5"),
        (3, "loc_4BE8"),
        (4, "loc_4BFB"),
        (5, "loc_4C0E"),
        (6, "loc_4C24"),
        (7, "loc_4C37"),
        (8, "loc_4C4D"),
        (9, "loc_4C60"),
        (10, "loc_4C6E"),
        (11, "loc_4C7C"),
        (12, "loc_4C8D"),
        (SWITCH_DEFAULT, "loc_4C9B"),
    )


    label("loc_4BB1")

    SetScenarioFlags(0x5D, 1)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_4CA5")

    label("loc_4BC2")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_4CA5")

    label("loc_4BD5")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_4CA5")

    label("loc_4BE8")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("r2070", 0, 0, 0)
    IdleLoop()
    Jump("loc_4CA5")

    label("loc_4BFB")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("m2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_4CA5")

    label("loc_4C0E")

    SetScenarioFlags(0x5C, 0)
    ReplaceBGM("ed7100", "ed7102")
    NewScene("m2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_4CA5")

    label("loc_4C24")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("m2099", 0, 0, 0)
    IdleLoop()
    Jump("loc_4CA5")

    label("loc_4C37")

    SetScenarioFlags(0x5C, 0)
    ReplaceBGM("ed7100", "ed7102")
    NewScene("m2099", 0, 0, 0)
    IdleLoop()
    Jump("loc_4CA5")

    label("loc_4C4D")

    ReplaceBGM("ed7100", "ed7102")
    NewScene("m2060", 0, 0, 0)
    IdleLoop()
    Jump("loc_4CA5")

    label("loc_4C60")

    NewScene("m2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_4CA5")

    label("loc_4C6E")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_4CA5")

    label("loc_4C7C")

    SetScenarioFlags(0x5C, 2)
    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_4CA5")

    label("loc_4C8D")

    NewScene("t0510", 0, 0, 0)
    IdleLoop()
    Jump("loc_4CA5")

    label("loc_4C9B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4CA5")

    Jump("loc_496C")

    label("loc_4CAA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_36_4942 end

    def Function_37_4CB8(): pass

    label("Function_37_4CB8")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4CE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5059")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼広場まで送ってもらう\x01",      # 0
            "②▼カジノを訪ねる\x01",            # 1
            "③▼オーナーから話を聞く\x01",      # 2
            "④▼ガンツの羽振りを確認\x01",      # 3
            "⑤▼支援課に戻ってくる\x01",        # 4
            "⑥▼イアン弁護士との会話\x01",      # 5
            "⑦▼黒月の襲撃\x01",                # 6
            "⑧▼ヨナからの連絡\x01",            # 7
            "⑨▼黒月を訪問\x01",                # 8
            "⑩▼ツァオと会話\x01",              # 9
            "?▼ガルシアと会話\x01",             # 10
            "?▼グレイスと情報交換\x01",         # 11
            "?▼カジノでの勝負\x01",             # 12
            "キャンセル\x01",                    # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (12, "loc_4E6A"),
        (11, "loc_4E6D"),
        (10, "loc_4E70"),
        (9, "loc_4E73"),
        (8, "loc_4E76"),
        (7, "loc_4E79"),
        (6, "loc_4E79"),
        (5, "loc_4E79"),
        (4, "loc_4E7C"),
        (3, "loc_4E7F"),
        (2, "loc_4E85"),
        (1, "loc_4E88"),
        (0, "loc_4E94"),
        (SWITCH_DEFAULT, "loc_4ED5"),
    )


    label("loc_4E6A")

    SetScenarioFlags(0xC2, 6)

    label("loc_4E6D")

    SetScenarioFlags(0xC2, 5)

    label("loc_4E70")

    SetScenarioFlags(0xC2, 4)

    label("loc_4E73")

    SetScenarioFlags(0xC2, 3)

    label("loc_4E76")

    SetScenarioFlags(0xC2, 2)

    label("loc_4E79")

    SetScenarioFlags(0xC2, 1)

    label("loc_4E7C")

    SetScenarioFlags(0xC2, 0)

    label("loc_4E7F")

    SetScenarioFlags(0xC1, 6)
    SetScenarioFlags(0xC1, 7)

    label("loc_4E85")

    SetScenarioFlags(0xC1, 5)

    label("loc_4E88")

    SetScenarioFlags(0xC1, 4)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4E94")

    SetScenarioFlags(0xC0, 0)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xC0, 1)
    SetScenarioFlags(0xC0, 2)
    SetScenarioFlags(0xC0, 3)
    SetScenarioFlags(0xC0, 4)
    SetScenarioFlags(0xC0, 5)
    SetScenarioFlags(0xC0, 6)
    SetScenarioFlags(0xC0, 7)
    SetScenarioFlags(0xC1, 0)
    SetScenarioFlags(0xC1, 1)
    SetScenarioFlags(0xC1, 2)
    SetScenarioFlags(0xC1, 3)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 61)
    Jump("loc_4EDA")

    label("loc_4ED5")

    Jump("loc_4EDA")

    label("loc_4EDA")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4F32"),
        (1, "loc_4F50"),
        (2, "loc_4F5E"),
        (3, "loc_4F6C"),
        (4, "loc_4F7A"),
        (5, "loc_4F88"),
        (6, "loc_4F99"),
        (7, "loc_4FB3"),
        (8, "loc_4FCE"),
        (9, "loc_4FE6"),
        (10, "loc_4FFE"),
        (11, "loc_5016"),
        (12, "loc_502E"),
        (SWITCH_DEFAULT, "loc_504A"),
    )


    label("loc_4F32")

    AddParty(0x8, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("r2030", 0, 0, 0)
    IdleLoop()
    Jump("loc_5054")

    label("loc_4F50")

    NewScene("c0470", 0, 0, 0)
    IdleLoop()
    Jump("loc_5054")

    label("loc_4F5E")

    NewScene("c0470", 0, 0, 0)
    IdleLoop()
    Jump("loc_5054")

    label("loc_4F6C")

    NewScene("c045B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5054")

    label("loc_4F7A")

    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5054")

    label("loc_4F88")

    RemoveParty(0x2, 0x0)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5054")

    label("loc_4F99")

    SetScenarioFlags(0x5C, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c120B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5054")

    label("loc_4FB3")

    SetScenarioFlags(0x5D, 4)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_5054")

    label("loc_4FCE")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c1200", 0, 0, 0)
    IdleLoop()
    Jump("loc_5054")

    label("loc_4FE6")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c1210", 102, 0, 0)
    IdleLoop()
    Jump("loc_5054")

    label("loc_4FFE")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_5054")

    label("loc_5016")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0570", 0, 0, 0)
    IdleLoop()
    Jump("loc_5054")

    label("loc_502E")

    AddParty(0x3C, 0xFF, 0xFF)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0470", 0, 0, 0)
    IdleLoop()
    Jump("loc_5054")

    label("loc_504A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5054")

    Jump("loc_4CE2")

    label("loc_5059")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_37_4CB8 end

    def Function_38_5067(): pass

    label("Function_38_5067")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5091")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_54A6")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼錠剤を発見する\x01",              # 0
            "②▼セルゲイへ報告\x01",              # 1
            "③▼病院に到着\x01",                  # 2
            "④▼受付で研究室に連絡\x01",          # 3
            "⑤▼ヨアヒムに錠剤を見せる\x01",      # 4
            "⑥▼倒れるティオ\x01",                # 5
            "⑦▼Ｄ∴Ｇ教団の情報\x01",            # 6
            "⑧▼鉱員が失踪した\x01",              # 7
            "⑨▼ダドリーからの連絡\x01",          # 8
            "⑩▼ダドリーと合流\x01",              # 9
            "?▼会長室前のボス戦\x01",             # 10
            "?▼戦闘後、会長室前\x01",             # 11
            "?▼会長室の探索開始\x01",             # 12
            "キャンセル\x01",                      # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (12, "loc_5215"),
        (11, "loc_5218"),
        (10, "loc_5218"),
        (9, "loc_5254"),
        (8, "loc_5257"),
        (7, "loc_525A"),
        (6, "loc_525A"),
        (5, "loc_525A"),
        (4, "loc_5260"),
        (3, "loc_5263"),
        (2, "loc_5266"),
        (1, "loc_526C"),
        (0, "loc_526F"),
        (SWITCH_DEFAULT, "loc_52DA"),
    )


    label("loc_5215")

    SetScenarioFlags(0xC6, 1)

    label("loc_5218")

    SetScenarioFlags(0xC4, 0)
    SetScenarioFlags(0xC4, 1)
    SetScenarioFlags(0xC4, 2)
    SetScenarioFlags(0xC4, 3)
    SetScenarioFlags(0xC4, 4)
    SetScenarioFlags(0xC4, 5)
    SetScenarioFlags(0xC4, 6)
    SetScenarioFlags(0xC4, 7)
    SetScenarioFlags(0xC5, 0)
    SetScenarioFlags(0xC5, 1)
    SetScenarioFlags(0xC5, 2)
    SetScenarioFlags(0xC5, 3)
    SetScenarioFlags(0xC6, 5)
    SetScenarioFlags(0xC5, 4)
    SetScenarioFlags(0xC5, 5)
    SetScenarioFlags(0xC5, 6)
    SetScenarioFlags(0xC5, 7)
    SetScenarioFlags(0xC6, 0)
    SetScenarioFlags(0xC6, 6)
    SetScenarioFlags(0xC6, 7)

    label("loc_5254")

    SetScenarioFlags(0xC3, 7)

    label("loc_5257")

    SetScenarioFlags(0xC3, 6)

    label("loc_525A")

    SetScenarioFlags(0xC3, 4)
    SetScenarioFlags(0xC3, 5)

    label("loc_5260")

    SetScenarioFlags(0xC3, 3)

    label("loc_5263")

    SetScenarioFlags(0xC3, 2)

    label("loc_5266")

    SetScenarioFlags(0xC3, 0)
    SetScenarioFlags(0xC3, 1)

    label("loc_526C")

    SetScenarioFlags(0xC2, 7)

    label("loc_526F")

    SetScenarioFlags(0xC0, 0)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xC0, 1)
    SetScenarioFlags(0xC0, 2)
    SetScenarioFlags(0xC0, 3)
    SetScenarioFlags(0xC0, 4)
    SetScenarioFlags(0xC0, 5)
    SetScenarioFlags(0xC0, 6)
    SetScenarioFlags(0xC0, 7)
    SetScenarioFlags(0xC1, 0)
    SetScenarioFlags(0xC1, 1)
    SetScenarioFlags(0xC1, 2)
    SetScenarioFlags(0xC1, 3)
    SetScenarioFlags(0xC1, 4)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xC1, 5)
    SetScenarioFlags(0xC1, 6)
    SetScenarioFlags(0xC1, 7)
    SetScenarioFlags(0xC2, 0)
    SetScenarioFlags(0xC2, 1)
    SetScenarioFlags(0xC2, 2)
    SetScenarioFlags(0xC2, 3)
    SetScenarioFlags(0xC2, 4)
    SetScenarioFlags(0xC2, 5)
    SetScenarioFlags(0xC2, 6)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 62)
    Jump("loc_52DF")

    label("loc_52DA")

    Jump("loc_52DF")

    label("loc_52DF")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5337"),
        (1, "loc_535F"),
        (2, "loc_5377"),
        (3, "loc_538F"),
        (4, "loc_53A7"),
        (5, "loc_53BF"),
        (6, "loc_53D7"),
        (7, "loc_53F2"),
        (8, "loc_540D"),
        (9, "loc_5428"),
        (10, "loc_5440"),
        (11, "loc_545C"),
        (12, "loc_547B"),
        (SWITCH_DEFAULT, "loc_5497"),
    )


    label("loc_5337")

    AddParty(0x3C, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0450", 0, 0, 0)
    IdleLoop()
    Jump("loc_54A1")

    label("loc_535F")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_54A1")

    label("loc_5377")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("t1500", 100, 0, 0)
    IdleLoop()
    Jump("loc_54A1")

    label("loc_538F")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("t1530", 0, 0, 0)
    IdleLoop()
    Jump("loc_54A1")

    label("loc_53A7")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("t1650", 0, 0, 0)
    IdleLoop()
    Jump("loc_54A1")

    label("loc_53BF")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_54A1")

    label("loc_53D7")

    SetScenarioFlags(0x5C, 6)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Jump("loc_54A1")

    label("loc_53F2")

    SetScenarioFlags(0x5D, 5)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_54A1")

    label("loc_540D")

    SetScenarioFlags(0x5D, 6)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_54A1")

    label("loc_5428")

    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_54A1")

    label("loc_5440")

    AddParty(0x9, 0xFF, 0xFF)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0597", 0, 0, 0)
    IdleLoop()
    Jump("loc_54A1")

    label("loc_545C")

    AddParty(0x9, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 2)
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    NewScene("c0597", 0, 0, 0)
    IdleLoop()
    Jump("loc_54A1")

    label("loc_547B")

    AddParty(0x9, 0xFF, 0xFF)
    NewScene("c0597", 0, 0, 0)
    IdleLoop()
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    Jump("loc_54A1")

    label("loc_5497")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_54A1")

    Jump("loc_5091")

    label("loc_54A6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_38_5067 end

    def Function_39_54B4(): pass

    label("Function_39_54B4")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    Call(2, 10)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_54E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_585F")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼人形工房\x01",                 # 0
            "②▼遊撃士と協力する\x01",         # 1
            "③▼病院に向かう\x01",             # 2
            "④▼ダドリーからの連絡\x01",       # 3
            "⑤▼無人のバスを発見\x01",         # 4
            "⑥▼夜の病院に到着\x01",           # 5
            "⑦▼戦闘後、夜の病院\x01",         # 6
            "⑧▼宿泊施設１階?入口\x01",        # 7
            "⑨▼宿泊施設１階を確認\x01",       # 8
            "⑩▼宿泊施設２階?テラス\x01",      # 9
            "?▼病棟の鍵を開ける\x01",          # 10
            "?▼病棟２階?廊下①\x01",           # 11
            "?▼病棟２階?廊下②\x01",           # 12
            "キャンセル\x01",                   # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (12, "loc_5665"),
        (11, "loc_5668"),
        (10, "loc_566E"),
        (9, "loc_5674"),
        (8, "loc_567A"),
        (7, "loc_567D"),
        (6, "loc_5680"),
        (5, "loc_5680"),
        (4, "loc_5683"),
        (3, "loc_5686"),
        (2, "loc_5689"),
        (1, "loc_5689"),
        (0, "loc_5689"),
        (SWITCH_DEFAULT, "loc_569D"),
    )


    label("loc_5665")

    SetScenarioFlags(0xE1, 7)

    label("loc_5668")

    SetScenarioFlags(0xE1, 3)
    SetScenarioFlags(0xE1, 4)

    label("loc_566E")

    SetScenarioFlags(0xE0, 7)
    SetScenarioFlags(0xE1, 0)

    label("loc_5674")

    SetScenarioFlags(0xE0, 5)
    SetScenarioFlags(0xE0, 6)

    label("loc_567A")

    SetScenarioFlags(0xE0, 4)

    label("loc_567D")

    SetScenarioFlags(0xE0, 3)

    label("loc_5680")

    SetScenarioFlags(0xE0, 2)

    label("loc_5683")

    SetScenarioFlags(0xE0, 1)

    label("loc_5686")

    SetScenarioFlags(0xE0, 0)

    label("loc_5689")

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 63)
    Jump("loc_56A2")

    label("loc_569D")

    Jump("loc_56A2")

    label("loc_56A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56BF")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_56BF")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5717"),
        (1, "loc_5728"),
        (2, "loc_5739"),
        (3, "loc_574A"),
        (4, "loc_5758"),
        (5, "loc_578E"),
        (6, "loc_57C4"),
        (7, "loc_57DE"),
        (8, "loc_57F1"),
        (9, "loc_5804"),
        (10, "loc_5817"),
        (11, "loc_582A"),
        (12, "loc_583D"),
        (SWITCH_DEFAULT, "loc_5850"),
    )


    label("loc_5717")

    SetScenarioFlags(0x5C, 0)
    NewScene("t3010", 0, 0, 0)
    IdleLoop()
    Jump("loc_585A")

    label("loc_5728")

    SetScenarioFlags(0x5C, 0)
    NewScene("c1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_585A")

    label("loc_5739")

    SetScenarioFlags(0x5D, 7)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_585A")

    label("loc_574A")

    NewScene("r1500", 100, 0, 0)
    IdleLoop()
    Jump("loc_585A")

    label("loc_5758")

    ReplaceBGM("ed7200", "ed7203")
    ReplaceBGM("ed7202", "ed7203")
    ReplaceBGM("ed7100", "ed7203")
    ReplaceBGM("ed7101", "ed7203")
    ReplaceBGM("ed7111", "ed7203")
    ReplaceBGM("ed7116", "ed7203")
    ReplaceBGM("ed7117", "ed7203")
    ReplaceBGM("ed7124", "ed7203")
    NewScene("r1530", 0, 0, 0)
    IdleLoop()
    Jump("loc_585A")

    label("loc_578E")

    ReplaceBGM("ed7200", "ed7203")
    ReplaceBGM("ed7202", "ed7203")
    ReplaceBGM("ed7100", "ed7203")
    ReplaceBGM("ed7101", "ed7203")
    ReplaceBGM("ed7111", "ed7203")
    ReplaceBGM("ed7116", "ed7203")
    ReplaceBGM("ed7117", "ed7203")
    ReplaceBGM("ed7124", "ed7203")
    NewScene("t150B", 0, 0, 0)
    IdleLoop()
    Jump("loc_585A")

    label("loc_57C4")

    SetScenarioFlags(0x5C, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x12F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("t150B", 0, 0, 0)
    IdleLoop()
    Jump("loc_585A")

    label("loc_57DE")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t151B", 0, 0, 0)
    IdleLoop()
    Jump("loc_585A")

    label("loc_57F1")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t151B", 0, 0, 0)
    IdleLoop()
    Jump("loc_585A")

    label("loc_5804")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t150B", 105, 0, 0)
    IdleLoop()
    Jump("loc_585A")

    label("loc_5817")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t150B", 0, 0, 0)
    IdleLoop()
    Jump("loc_585A")

    label("loc_582A")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t154B", 0, 0, 0)
    IdleLoop()
    Jump("loc_585A")

    label("loc_583D")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t154B", 0, 0, 0)
    IdleLoop()
    Jump("loc_585A")

    label("loc_5850")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_585A")

    Jump("loc_54E1")

    label("loc_585F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_39_54B4 end

    def Function_40_586D(): pass

    label("Function_40_586D")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    Call(2, 10)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_589A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5C95")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼病棟３階?廊下\x01",               # 0
            "②▼フィリアたちを確認\x01",          # 1
            "③▼セシルを助ける\x01",              # 2
            "④▼戦闘後、セシルを助ける\x01",      # 3
            "⑤▼研究棟１階?入口\x01",             # 4
            "⑥▼教授たちを発見\x01",              # 5
            "⑦▼カードキーを入手\x01",            # 6
            "⑧▼アーネスト戦\x01",                # 7
            "⑨▼アーネスト戦後\x01",              # 8
            "⑩▼ヨアヒムの研究室\x01",            # 9
            "?▼警備隊がやってきた\x01",           # 10
            "?▼支援課襲撃\x01",                   # 11
            "?▼支援課襲撃２\x01",                 # 12
            "?★アーネスト、飛竜で逃走\x01",       # 13
            "?★レン、パテマテで逃走\x01",         # 14
            "キャンセル\x01",                      # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (14, "loc_5A56"),
        (13, "loc_5A56"),
        (12, "loc_5A56"),
        (11, "loc_5A56"),
        (10, "loc_5A56"),
        (9, "loc_5A59"),
        (8, "loc_5A5C"),
        (7, "loc_5A5C"),
        (6, "loc_5A62"),
        (5, "loc_5A65"),
        (4, "loc_5A68"),
        (3, "loc_5A6B"),
        (2, "loc_5A6B"),
        (1, "loc_5A6E"),
        (0, "loc_5A71"),
        (SWITCH_DEFAULT, "loc_5AAC"),
    )


    label("loc_5A56")

    SetScenarioFlags(0xE3, 6)

    label("loc_5A59")

    SetScenarioFlags(0xE3, 5)

    label("loc_5A5C")

    SetScenarioFlags(0xE3, 3)
    SetScenarioFlags(0xE3, 4)

    label("loc_5A62")

    SetScenarioFlags(0xE3, 2)

    label("loc_5A65")

    SetScenarioFlags(0xE3, 0)

    label("loc_5A68")

    SetScenarioFlags(0xE2, 7)

    label("loc_5A6B")

    SetScenarioFlags(0xE2, 4)

    label("loc_5A6E")

    SetScenarioFlags(0xE2, 3)

    label("loc_5A71")

    SetScenarioFlags(0xE0, 0)
    SetScenarioFlags(0xE0, 1)
    SetScenarioFlags(0xE0, 2)
    SetScenarioFlags(0xE0, 3)
    SetScenarioFlags(0xE0, 4)
    SetScenarioFlags(0xE0, 5)
    SetScenarioFlags(0xE0, 6)
    SetScenarioFlags(0xE0, 7)
    SetScenarioFlags(0xE1, 0)
    SetScenarioFlags(0xE1, 3)
    SetScenarioFlags(0xE1, 4)
    SetScenarioFlags(0xE1, 7)
    SetScenarioFlags(0xE2, 1)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 63)
    Jump("loc_5AB1")

    label("loc_5AAC")

    Jump("loc_5AB1")

    label("loc_5AB1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5ACE")
    AddParty(0x5, 0xFF, 0xFF)

    label("loc_5ACE")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5B32"),
        (1, "loc_5B45"),
        (2, "loc_5B58"),
        (3, "loc_5B6B"),
        (4, "loc_5B81"),
        (5, "loc_5B94"),
        (6, "loc_5BA7"),
        (7, "loc_5BBA"),
        (8, "loc_5BCD"),
        (9, "loc_5BE3"),
        (10, "loc_5BFA"),
        (11, "loc_5C14"),
        (12, "loc_5C2B"),
        (13, "loc_5C5E"),
        (14, "loc_5C75"),
        (SWITCH_DEFAULT, "loc_5C86"),
    )


    label("loc_5B32")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t155B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5C90")

    label("loc_5B45")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t155B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5C90")

    label("loc_5B58")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t160B", 103, 0, 0)
    IdleLoop()
    Jump("loc_5C90")

    label("loc_5B6B")

    SetScenarioFlags(0x5C, 1)
    ReplaceBGM("ed7123", "ed7510")
    NewScene("t160B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5C90")

    label("loc_5B81")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t162B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5C90")

    label("loc_5B94")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t163B", 102, 0, 0)
    IdleLoop()
    Jump("loc_5C90")

    label("loc_5BA7")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t164B", 116, 0, 0)
    IdleLoop()
    Jump("loc_5C90")

    label("loc_5BBA")

    ReplaceBGM("ed7123", "ed7510")
    NewScene("t165B", 101, 0, 0)
    IdleLoop()
    Jump("loc_5C90")

    label("loc_5BCD")

    SetScenarioFlags(0x5C, 0)
    ReplaceBGM("ed7123", "ed7510")
    NewScene("t165B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5C90")

    label("loc_5BE3")

    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x20E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("t165B", 101, 0, 0)
    IdleLoop()
    Jump("loc_5C90")

    label("loc_5BFA")

    SetScenarioFlags(0x5C, 2)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("t150B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5C90")

    label("loc_5C14")

    Call(1, 29)
    Call(1, 64)
    SetScenarioFlags(0x5C, 5)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5C90")

    label("loc_5C2B")

    AddParty(0x9, 0xFF, 0xFF)
    Call(1, 29)
    Call(1, 64)
    SetChrChipPat(0x0, 0x1, 0x9B)
    SetChrChipPat(0x3, 0x1, 0x9C)
    LoadChrChipPat()
    SetScenarioFlags(0x5C, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c020B", 0, 0, 0)
    IdleLoop()
    Jump("loc_5C90")

    label("loc_5C5E")

    Call(1, 29)
    Call(1, 64)
    SetScenarioFlags(0x5C, 0)
    NewScene("e3300", 0, 0, 0)
    IdleLoop()
    Jump("loc_5C90")

    label("loc_5C75")

    SetScenarioFlags(0x5C, 1)
    NewScene("e3300", 0, 0, 0)
    IdleLoop()
    Jump("loc_5C90")

    label("loc_5C86")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5C90")

    Jump("loc_589A")

    label("loc_5C95")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_40_586D end

    def Function_41_5CA3(): pass

    label("Function_41_5CA3")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    Call(2, 10)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5CD0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_605F")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼東口の橋\x01",                  # 0
            "②▼戦闘後、東口の橋\x01",          # 1
            "③▼リムジン内\x01",                # 2
            "④▼ＩＢＣで事情を説明\x01",        # 3
            "⑤▼ＩＢＣで休憩\x01",              # 4
            "⑥▼総裁室からの連絡\x01",          # 5
            "⑦▼警備員から報告\x01",            # 6
            "⑧▼攻防戦開始\x01",                # 7
            "⑨▼攻防戦終了\x01",                # 8
            "⑩▼バイパー＆テスタ参戦\x01",      # 9
            "?▼ヨアヒムが逃げる\x01",           # 10
            "?▼リムジンで橋を突破\x01",         # 11
            "?▼リムジン内\x01",                 # 12
            "キャンセル\x01",                    # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (12, "loc_5E3E"),
        (11, "loc_5E3E"),
        (10, "loc_5E3E"),
        (9, "loc_5E3E"),
        (8, "loc_5E3E"),
        (7, "loc_5E3E"),
        (6, "loc_5E41"),
        (5, "loc_5E44"),
        (4, "loc_5E50"),
        (3, "loc_5E56"),
        (2, "loc_5E56"),
        (1, "loc_5E56"),
        (0, "loc_5E56"),
        (SWITCH_DEFAULT, "loc_5EAC"),
    )


    label("loc_5E3E")

    SetScenarioFlags(0xE7, 5)

    label("loc_5E41")

    SetScenarioFlags(0xE4, 4)

    label("loc_5E44")

    SetScenarioFlags(0xE4, 0)
    SetScenarioFlags(0xE4, 1)
    SetScenarioFlags(0xE4, 2)
    SetScenarioFlags(0xE4, 3)

    label("loc_5E50")

    Call(2, 51)
    SetScenarioFlags(0xE3, 7)

    label("loc_5E56")

    SetScenarioFlags(0xE0, 0)
    SetScenarioFlags(0xE0, 1)
    SetScenarioFlags(0xE0, 2)
    SetScenarioFlags(0xE0, 3)
    SetScenarioFlags(0xE0, 4)
    SetScenarioFlags(0xE0, 5)
    SetScenarioFlags(0xE0, 6)
    SetScenarioFlags(0xE0, 7)
    SetScenarioFlags(0xE1, 0)
    SetScenarioFlags(0xE1, 3)
    SetScenarioFlags(0xE1, 4)
    SetScenarioFlags(0xE1, 7)
    SetScenarioFlags(0xE2, 1)
    SetScenarioFlags(0xE2, 3)
    SetScenarioFlags(0xE2, 4)
    SetScenarioFlags(0xE2, 7)
    SetScenarioFlags(0xE3, 0)
    SetScenarioFlags(0xE3, 2)
    SetScenarioFlags(0xE3, 3)
    SetScenarioFlags(0xE3, 4)
    SetScenarioFlags(0xE3, 5)
    SetScenarioFlags(0xE3, 6)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(1, 29)
    Call(1, 64)
    Jump("loc_5EB1")

    label("loc_5EAC")

    Jump("loc_5EB1")

    label("loc_5EB1")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5F09"),
        (1, "loc_5F32"),
        (2, "loc_5F63"),
        (3, "loc_5F7C"),
        (4, "loc_5F8D"),
        (5, "loc_5FA4"),
        (6, "loc_5FBB"),
        (7, "loc_5FD2"),
        (8, "loc_5FE0"),
        (9, "loc_5FF1"),
        (10, "loc_600B"),
        (11, "loc_6025"),
        (12, "loc_6036"),
        (SWITCH_DEFAULT, "loc_6050"),
    )


    label("loc_5F09")

    SetChrChipPat(0x0, 0x1, 0x9B)
    SetChrChipPat(0x3, 0x1, 0x9C)
    LoadChrChipPat()
    SetScenarioFlags(0x5C, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("r000B", 0, 0, 0)
    IdleLoop()
    Jump("loc_605A")

    label("loc_5F32")

    AddParty(0x9F, 0xFF, 0xFF)
    AddParty(0x57, 0xFF, 0xFF)
    SetChrChipPat(0x0, 0x1, 0x9B)
    SetChrChipPat(0x3, 0x1, 0x9C)
    LoadChrChipPat()
    SetScenarioFlags(0x5C, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("r000B", 0, 0, 0)
    IdleLoop()
    Jump("loc_605A")

    label("loc_5F63")

    AddParty(0x52, 0xFF, 0xFF)
    AddParty(0x57, 0xFF, 0xFF)
    SetScenarioFlags(0x5C, 0)
    NewScene("e0111", 0, 0, 0)
    IdleLoop()
    Jump("loc_605A")

    label("loc_5F7C")

    SetScenarioFlags(0x5C, 0)
    NewScene("c130B", 0, 0, 0)
    IdleLoop()
    Jump("loc_605A")

    label("loc_5F8D")

    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    NewScene("c134B", 101, 0, 0)
    IdleLoop()
    Jump("loc_605A")

    label("loc_5FA4")

    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    NewScene("c134B", 101, 0, 0)
    IdleLoop()
    Jump("loc_605A")

    label("loc_5FBB")

    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    NewScene("c134B", 101, 0, 0)
    IdleLoop()
    Jump("loc_605A")

    label("loc_5FD2")

    NewScene("c131B", 0, 0, 0)
    IdleLoop()
    Jump("loc_605A")

    label("loc_5FE0")

    SetScenarioFlags(0x5C, 2)
    NewScene("c130B", 0, 0, 0)
    IdleLoop()
    Jump("loc_605A")

    label("loc_5FF1")

    SetScenarioFlags(0x5C, 2)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c120B", 0, 0, 0)
    IdleLoop()
    Jump("loc_605A")

    label("loc_600B")

    SetScenarioFlags(0x5C, 3)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("c130B", 0, 0, 0)
    IdleLoop()
    Jump("loc_605A")

    label("loc_6025")

    SetScenarioFlags(0x5C, 2)
    NewScene("r000B", 0, 0, 0)
    IdleLoop()
    Jump("loc_605A")

    label("loc_6036")

    SetScenarioFlags(0x5C, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x20F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("e0111", 0, 0, 0)
    IdleLoop()
    Jump("loc_605A")

    label("loc_6050")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_605A")

    Jump("loc_5CD0")

    label("loc_605F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_41_5CA3 end

    def Function_42_606D(): pass

    label("Function_42_606D")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    Call(2, 10)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_609A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6463")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼太陽の砦に到着\x01",          # 0
            "②▼教団のマークを発見\x01",      # 1
            "③▼地下の縦穴を発見\x01",        # 2
            "④▼魔人化したマフィア\x01",      # 3
            "⑤▼血の池エリア\x01",            # 4
            "⑥▼行方不明者を発見\x01",        # 5
            "⑦▼マルコーニを発見\x01",        # 6
            "⑧▼魔人アーネスト戦\x01",        # 7
            "⑨▼魔人アーネスト戦後\x01",      # 8
            "⑩▼ガルシア戦\x01",              # 9
            "?▼ガルシア戦後\x01",             # 10
            "?▼ヨアヒムとの対決\x01",         # 11
            "?▼魔人ヨアヒム戦\x01",           # 12
            "キャンセル\x01",                  # 13
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (12, "loc_621A"),
        (11, "loc_621A"),
        (10, "loc_621D"),
        (9, "loc_621D"),
        (8, "loc_6220"),
        (7, "loc_6220"),
        (6, "loc_6223"),
        (5, "loc_622F"),
        (4, "loc_6232"),
        (3, "loc_6241"),
        (2, "loc_6244"),
        (1, "loc_6247"),
        (0, "loc_624A"),
        (SWITCH_DEFAULT, "loc_62AF"),
    )


    label("loc_621A")

    SetScenarioFlags(0xE6, 4)

    label("loc_621D")

    SetScenarioFlags(0xE6, 3)

    label("loc_6220")

    SetScenarioFlags(0xE6, 2)

    label("loc_6223")

    SetScenarioFlags(0xE5, 6)
    SetScenarioFlags(0xE5, 7)
    SetScenarioFlags(0xE6, 0)
    SetScenarioFlags(0xE6, 1)

    label("loc_622F")

    SetScenarioFlags(0xE5, 5)

    label("loc_6232")

    SetScenarioFlags(0xE5, 0)
    SetScenarioFlags(0xE5, 1)
    SetScenarioFlags(0xE5, 2)
    SetScenarioFlags(0xE5, 3)
    SetScenarioFlags(0xE5, 4)

    label("loc_6241")

    SetScenarioFlags(0xE4, 7)

    label("loc_6244")

    SetScenarioFlags(0xE4, 6)

    label("loc_6247")

    SetScenarioFlags(0xE4, 5)

    label("loc_624A")

    SetScenarioFlags(0xE0, 0)
    SetScenarioFlags(0xE0, 1)
    SetScenarioFlags(0xE0, 2)
    SetScenarioFlags(0xE0, 3)
    SetScenarioFlags(0xE0, 4)
    SetScenarioFlags(0xE0, 5)
    SetScenarioFlags(0xE0, 6)
    SetScenarioFlags(0xE0, 7)
    SetScenarioFlags(0xE1, 0)
    SetScenarioFlags(0xE1, 3)
    SetScenarioFlags(0xE1, 4)
    SetScenarioFlags(0xE1, 7)
    SetScenarioFlags(0xE2, 1)
    SetScenarioFlags(0xE2, 3)
    SetScenarioFlags(0xE2, 4)
    SetScenarioFlags(0xE2, 7)
    SetScenarioFlags(0xE3, 0)
    SetScenarioFlags(0xE3, 2)
    SetScenarioFlags(0xE3, 3)
    SetScenarioFlags(0xE3, 4)
    SetScenarioFlags(0xE3, 5)
    SetScenarioFlags(0xE3, 6)
    SetScenarioFlags(0xE3, 7)
    SetScenarioFlags(0xE4, 0)
    SetScenarioFlags(0xE4, 1)
    SetScenarioFlags(0xE4, 2)
    SetScenarioFlags(0xE4, 3)
    SetScenarioFlags(0xE4, 4)
    SetScenarioFlags(0xE7, 5)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_62B4")

    label("loc_62AF")

    Jump("loc_62B4")

    label("loc_62B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_62D5")
    AddParty(0x6, 0xFF, 0xFF)
    AddParty(0x7, 0xFF, 0xFF)

    label("loc_62D5")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_632D"),
        (1, "loc_6344"),
        (2, "loc_635D"),
        (3, "loc_6371"),
        (4, "loc_6385"),
        (5, "loc_6399"),
        (6, "loc_63AD"),
        (7, "loc_63C1"),
        (8, "loc_63D5"),
        (9, "loc_63EC"),
        (10, "loc_6400"),
        (11, "loc_6420"),
        (12, "loc_6434"),
        (SWITCH_DEFAULT, "loc_6454"),
    )


    label("loc_632D")

    Call(1, 29)
    Call(1, 65)
    SetScenarioFlags(0x5C, 0)
    NewScene("r307B", 0, 0, 0)
    IdleLoop()
    Jump("loc_645E")

    label("loc_6344")

    Call(1, 29)
    Call(1, 65)
    ReplaceBGM("ed7510", "ed7305")
    NewScene("m3000", 108, 0, 0)
    IdleLoop()
    Jump("loc_645E")

    label("loc_635D")

    Call(1, 29)
    Call(1, 65)
    NewScene("m3002", 0, 0, 0)
    IdleLoop()
    Jump("loc_645E")

    label("loc_6371")

    Call(1, 29)
    Call(1, 66)
    NewScene("m3012", 0, 0, 0)
    IdleLoop()
    Jump("loc_645E")

    label("loc_6385")

    Call(1, 29)
    Call(1, 66)
    NewScene("m3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_645E")

    label("loc_6399")

    Call(1, 29)
    Call(1, 66)
    NewScene("m3021", 0, 0, 0)
    IdleLoop()
    Jump("loc_645E")

    label("loc_63AD")

    Call(1, 29)
    Call(1, 66)
    NewScene("m3023", 104, 0, 0)
    IdleLoop()
    Jump("loc_645E")

    label("loc_63C1")

    Call(1, 29)
    Call(1, 66)
    NewScene("m3021", 105, 0, 0)
    IdleLoop()
    Jump("loc_645E")

    label("loc_63D5")

    Call(1, 29)
    Call(1, 66)
    SetScenarioFlags(0x5C, 0)
    NewScene("m3021", 0, 0, 0)
    IdleLoop()
    Jump("loc_645E")

    label("loc_63EC")

    Call(1, 29)
    Call(1, 67)
    NewScene("m3034", 0, 0, 0)
    IdleLoop()
    Jump("loc_645E")

    label("loc_6400")

    Call(1, 29)
    Call(1, 67)
    SetScenarioFlags(0x5C, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x7A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m3034", 0, 0, 0)
    IdleLoop()
    Jump("loc_645E")

    label("loc_6420")

    Call(1, 29)
    Call(1, 68)
    NewScene("m3099", 0, 0, 0)
    IdleLoop()
    Jump("loc_645E")

    label("loc_6434")

    Call(1, 29)
    Call(1, 68)
    SetScenarioFlags(0x5C, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1FE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m3099", 0, 0, 0)
    IdleLoop()
    Jump("loc_645E")

    label("loc_6454")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_645E")

    Jump("loc_609A")

    label("loc_6463")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_42_606D end

    def Function_43_6471(): pass

    label("Function_43_6471")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    Call(2, 10)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_649E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6659")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "①▼パテル＝マテル参戦\x01",      # 0
            "②▼魔人ヨアヒム戦後\x01",        # 1
            "③▼夜明けの古戦場\x01",          # 2
            "④▼スタッフロール\x01",          # 3
            "⑤▼エピローグ\x01",              # 4
            "⑥▼エピローグ２\x01",            # 5
            "キャンセル\x01",                  # 6
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (5, "loc_6564"),
        (4, "loc_6564"),
        (3, "loc_6564"),
        (2, "loc_6564"),
        (1, "loc_6564"),
        (0, "loc_6564"),
        (SWITCH_DEFAULT, "loc_6575"),
    )


    label("loc_6564")

    Call(2, 11)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_657A")

    label("loc_6575")

    Jump("loc_657A")

    label("loc_657A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_659B")
    AddParty(0x6, 0xFF, 0xFF)
    AddParty(0x7, 0xFF, 0xFF)

    label("loc_659B")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_65C9"),
        (1, "loc_65E3"),
        (2, "loc_65FD"),
        (3, "loc_6617"),
        (4, "loc_6628"),
        (5, "loc_6639"),
        (SWITCH_DEFAULT, "loc_664A"),
    )


    label("loc_65C9")

    SetScenarioFlags(0x5C, 1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x196), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m3099", 0, 0, 0)
    IdleLoop()
    Jump("loc_6654")

    label("loc_65E3")

    SetScenarioFlags(0x5C, 2)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x196), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m3099", 0, 0, 0)
    IdleLoop()
    Jump("loc_6654")

    label("loc_65FD")

    SetScenarioFlags(0x5C, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x208), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("r308E", 0, 0, 0)
    IdleLoop()
    Jump("loc_6654")

    label("loc_6617")

    SetScenarioFlags(0x5C, 1)
    NewScene("r308E", 0, 0, 0)
    IdleLoop()
    Jump("loc_6654")

    label("loc_6628")

    SetScenarioFlags(0x5C, 0)
    NewScene("c1120", 0, 0, 0)
    IdleLoop()
    Jump("loc_6654")

    label("loc_6639")

    SetScenarioFlags(0x5E, 0)
    NewScene("e3500", 0, 0, 0)
    IdleLoop()
    Jump("loc_6654")

    label("loc_664A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6654")

    Jump("loc_649E")

    label("loc_6659")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_43_6471 end

    def Function_44_6667(): pass

    label("Function_44_6667")

    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_667A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6832")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "★「クロスベル警察に到着した」\x01",        # 0
            "★「特務支援課のビルに到着した」\x01",      # 1
            "★「ティオと話すイベント」\x01",            # 2
            "★「特務支援課の説明を聞いた」\x01",        # 3
            "▼①序章開始\x01",                          # 4
            "★「初の捜査任務が入ってきた」\x01",        # 5
            "▼②グレイスから情報を聞いた\x01",          # 6
            "★「イアン弁護士から話を聞いた」\x01",      # 7
            "キャンセル\x01",                            # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (7, "loc_67BE"),
        (6, "loc_67C7"),
        (5, "loc_67D9"),
        (4, "loc_67E7"),
        (3, "loc_67EA"),
        (2, "loc_67ED"),
        (1, "loc_67F6"),
        (0, "loc_680E"),
        (SWITCH_DEFAULT, "loc_6823"),
    )


    label("loc_67BE")

    SetScenarioFlags(0x42, 6)
    SetScenarioFlags(0x42, 7)
    SetScenarioFlags(0x43, 0)

    label("loc_67C7")

    SetScenarioFlags(0x42, 0)
    SetScenarioFlags(0x42, 1)
    SetScenarioFlags(0x42, 2)
    SetScenarioFlags(0x42, 3)
    SetScenarioFlags(0x42, 4)
    SetScenarioFlags(0x42, 5)

    label("loc_67D9")

    SetScenarioFlags(0x41, 7)
    OP_29(0x3E, 0x4, 0x2)
    OP_29(0x3E, 0x1, 0x0)

    label("loc_67E7")

    SetScenarioFlags(0x41, 6)

    label("loc_67EA")

    SetScenarioFlags(0x41, 5)

    label("loc_67ED")

    SetScenarioFlags(0x41, 2)
    SetScenarioFlags(0x41, 3)
    SetScenarioFlags(0x41, 4)

    label("loc_67F6")

    SetScenarioFlags(0x40, 2)
    SetScenarioFlags(0x40, 3)
    SetScenarioFlags(0x40, 4)
    SetScenarioFlags(0x40, 5)
    SetScenarioFlags(0x40, 6)
    SetScenarioFlags(0x40, 7)
    SetScenarioFlags(0x41, 0)
    SetScenarioFlags(0x41, 1)

    label("loc_680E")

    SetScenarioFlags(0x40, 0)
    SetScenarioFlags(0x40, 1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_682D")

    label("loc_6823")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_682D")

    Jump("loc_667A")

    label("loc_6832")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_44_6667 end

    def Function_45_6840(): pass

    label("Function_45_6840")

    Call(2, 5)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6856")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A98")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼③一章開始\x01",                        # 0
            "★「村長の家から出た」\x01",              # 1
            "★「聞き込みが終わった」\x01",            # 2
            "▼④アルモリカ村から帰ってきた\x01",      # 3
            "★「バスを探しにいく」\x01",              # 4
            "★「セシルと再会した」\x01",              # 5
            "★「研修医から話を聞いた」\x01",          # 6
            "★「魔獣の足跡を見つけた」\x01",          # 7
            "★「魔獣の対策をした」\x01",              # 8
            "▼⑤２日目、マインツに向かう\x01",        # 9
            "★「町長と会話した」\x01",                # 10
            "★「ミーティングをした」\x01",            # 11
            "キャンセル\x01",                          # 12
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (11, "loc_69F0"),
        (10, "loc_69F3"),
        (9, "loc_6A14"),
        (8, "loc_6A1A"),
        (7, "loc_6A2C"),
        (6, "loc_6A44"),
        (5, "loc_6A47"),
        (4, "loc_6A59"),
        (3, "loc_6A5C"),
        (2, "loc_6A5F"),
        (1, "loc_6A65"),
        (0, "loc_6A77"),
        (SWITCH_DEFAULT, "loc_6A89"),
    )


    label("loc_69F0")

    SetScenarioFlags(0x65, 5)

    label("loc_69F3")

    SetScenarioFlags(0x64, 2)
    SetScenarioFlags(0x64, 3)
    SetScenarioFlags(0x64, 4)
    SetScenarioFlags(0x64, 5)
    SetScenarioFlags(0x64, 6)
    SetScenarioFlags(0x64, 7)
    SetScenarioFlags(0x65, 0)
    SetScenarioFlags(0x65, 1)
    SetScenarioFlags(0x65, 2)
    SetScenarioFlags(0x65, 3)
    SetScenarioFlags(0x65, 4)

    label("loc_6A14")

    SetScenarioFlags(0x64, 0)
    SetScenarioFlags(0x64, 1)

    label("loc_6A1A")

    SetScenarioFlags(0x63, 2)
    SetScenarioFlags(0x63, 3)
    SetScenarioFlags(0x63, 4)
    SetScenarioFlags(0x63, 5)
    SetScenarioFlags(0x63, 6)
    SetScenarioFlags(0x63, 7)

    label("loc_6A2C")

    SetScenarioFlags(0x62, 2)
    SetScenarioFlags(0x62, 3)
    SetScenarioFlags(0x62, 4)
    SetScenarioFlags(0x62, 5)
    SetScenarioFlags(0x62, 6)
    SetScenarioFlags(0x62, 7)
    SetScenarioFlags(0x63, 0)
    SetScenarioFlags(0x63, 1)

    label("loc_6A44")

    SetScenarioFlags(0x62, 1)

    label("loc_6A47")

    SetScenarioFlags(0x61, 3)
    SetScenarioFlags(0x61, 4)
    SetScenarioFlags(0x61, 5)
    SetScenarioFlags(0x61, 6)
    SetScenarioFlags(0x61, 7)
    SetScenarioFlags(0x62, 0)

    label("loc_6A59")

    SetScenarioFlags(0x61, 2)

    label("loc_6A5C")

    SetScenarioFlags(0x61, 1)

    label("loc_6A5F")

    SetScenarioFlags(0x60, 7)
    SetScenarioFlags(0x61, 0)

    label("loc_6A65")

    SetScenarioFlags(0x60, 1)
    SetScenarioFlags(0x60, 2)
    SetScenarioFlags(0x60, 3)
    SetScenarioFlags(0x60, 4)
    SetScenarioFlags(0x60, 5)
    SetScenarioFlags(0x60, 6)

    label("loc_6A77")

    SetScenarioFlags(0x60, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6A93")

    label("loc_6A89")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6A93")

    Jump("loc_6856")

    label("loc_6A98")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_45_6840 end

    def Function_46_6AA6(): pass

    label("Function_46_6AA6")

    Call(2, 5)
    Call(2, 6)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6ABF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6CBB")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼⑥二章開始\x01",                      # 0
            "▼⑦聞き込みを開始する\x01",            # 1
            "★「支援課に帰ることにした」\x01",      # 2
            "★「エリィを探す」\x01",                # 3
            "▼⑧ＩＢＣビルへ向かう\x01",            # 4
            "▼⑨星見の塔に向かう\x01",              # 5
            "★「巡回を開始した」\x01",              # 6
            "★「第２幕が始まった」\x01",            # 7
            "★「第３幕が始まった」\x01",            # 8
            "★「最終幕が始まった」\x01",            # 9
            "キャンセル\x01",                        # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (9, "loc_6C05"),
        (8, "loc_6C11"),
        (7, "loc_6C1D"),
        (6, "loc_6C29"),
        (5, "loc_6C38"),
        (4, "loc_6C65"),
        (3, "loc_6C6B"),
        (2, "loc_6C6E"),
        (1, "loc_6C80"),
        (0, "loc_6C95"),
        (SWITCH_DEFAULT, "loc_6CA7"),
    )


    label("loc_6C05")

    SetScenarioFlags(0x85, 5)
    SetScenarioFlags(0x85, 6)
    SetScenarioFlags(0x85, 7)
    SetScenarioFlags(0x86, 0)

    label("loc_6C11")

    SetScenarioFlags(0x85, 1)
    SetScenarioFlags(0x85, 2)
    SetScenarioFlags(0x85, 3)
    SetScenarioFlags(0x85, 4)

    label("loc_6C1D")

    SetScenarioFlags(0x84, 5)
    SetScenarioFlags(0x84, 6)
    SetScenarioFlags(0x84, 7)
    SetScenarioFlags(0x85, 0)

    label("loc_6C29")

    SetScenarioFlags(0x84, 0)
    SetScenarioFlags(0x84, 1)
    SetScenarioFlags(0x84, 2)
    SetScenarioFlags(0x84, 3)
    SetScenarioFlags(0x84, 4)

    label("loc_6C38")

    SetScenarioFlags(0x82, 1)
    SetScenarioFlags(0x82, 2)
    SetScenarioFlags(0x82, 3)
    SetScenarioFlags(0x82, 4)
    SetScenarioFlags(0x82, 5)
    SetScenarioFlags(0x82, 6)
    SetScenarioFlags(0x82, 7)
    SetScenarioFlags(0x83, 0)
    SetScenarioFlags(0x83, 1)
    SetScenarioFlags(0x83, 2)
    SetScenarioFlags(0x83, 3)
    SetScenarioFlags(0x83, 4)
    SetScenarioFlags(0x83, 5)
    SetScenarioFlags(0x83, 6)
    SetScenarioFlags(0x83, 7)

    label("loc_6C65")

    SetScenarioFlags(0x81, 7)
    SetScenarioFlags(0x82, 0)

    label("loc_6C6B")

    SetScenarioFlags(0x81, 6)

    label("loc_6C6E")

    SetScenarioFlags(0x81, 0)
    SetScenarioFlags(0x81, 1)
    SetScenarioFlags(0x81, 2)
    SetScenarioFlags(0x81, 3)
    SetScenarioFlags(0x81, 4)
    SetScenarioFlags(0x81, 5)

    label("loc_6C80")

    SetScenarioFlags(0x80, 1)
    SetScenarioFlags(0x80, 2)
    SetScenarioFlags(0x80, 3)
    SetScenarioFlags(0x80, 4)
    SetScenarioFlags(0x80, 5)
    SetScenarioFlags(0x80, 6)
    SetScenarioFlags(0x80, 7)

    label("loc_6C95")

    SetScenarioFlags(0x80, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6CB6")

    label("loc_6CA7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6CB6")

    label("loc_6CB6")

    Jump("loc_6ABF")

    label("loc_6CBB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_46_6AA6 end

    def Function_47_6CC9(): pass

    label("Function_47_6CC9")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6CE5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F85")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼⑩記念祭２日目開始\x01",                  # 0
            "★「???からの連絡が来た」3-1\x01",          # 1
            "▼?記念祭３日目開始\x01",                   # 2
            "▼?記念祭３日目??????後戻る\x01",           # 3
            "★「???????Ａ区画に到着した」\x01",         # 4
            "▼?記念祭４日目開始\x01",                   # 5
            "▼?記念祭４日目??????後戻る\x01",           # 6
            "★「フランからの連絡が来た」3-3\x01",       # 7
            "★「コリンの捜索を開始した」\x01",          # 8
            "★「ランディからの連絡①がきた」\x01",      # 9
            "★「レンが同行者となった」\x01",            # 10
            "★「エリィからの連絡①がきた」\x01",        # 11
            "★「ティオからの連絡①がきた」\x01",        # 12
            "★「?????＆???からの連絡がきた」\x01",      # 13
            "★「西??????街道????を探??行?」\x01",       # 14
            "キャンセル\x01",                            # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (14, "loc_6F17"),
        (13, "loc_6F1A"),
        (12, "loc_6F20"),
        (11, "loc_6F26"),
        (10, "loc_6F29"),
        (9, "loc_6F2C"),
        (8, "loc_6F32"),
        (7, "loc_6F35"),
        (6, "loc_6F38"),
        (5, "loc_6F3B"),
        (4, "loc_6F4D"),
        (3, "loc_6F56"),
        (2, "loc_6F59"),
        (1, "loc_6F5C"),
        (0, "loc_6F5F"),
        (SWITCH_DEFAULT, "loc_6F71"),
    )


    label("loc_6F17")

    SetScenarioFlags(0xA2, 7)

    label("loc_6F1A")

    SetScenarioFlags(0xA2, 5)
    SetScenarioFlags(0xA2, 6)

    label("loc_6F20")

    SetScenarioFlags(0xA2, 3)
    SetScenarioFlags(0xA2, 4)

    label("loc_6F26")

    SetScenarioFlags(0xA2, 2)

    label("loc_6F29")

    SetScenarioFlags(0xA2, 1)

    label("loc_6F2C")

    SetScenarioFlags(0xA1, 7)
    SetScenarioFlags(0xA2, 0)

    label("loc_6F32")

    SetScenarioFlags(0xA1, 6)

    label("loc_6F35")

    SetScenarioFlags(0xA1, 5)

    label("loc_6F38")

    SetScenarioFlags(0xAA, 2)

    label("loc_6F3B")

    SetScenarioFlags(0xA0, 7)
    SetScenarioFlags(0xA1, 0)
    SetScenarioFlags(0xA1, 1)
    SetScenarioFlags(0xA1, 2)
    SetScenarioFlags(0xA1, 3)
    SetScenarioFlags(0xA1, 4)

    label("loc_6F4D")

    SetScenarioFlags(0xA0, 4)
    SetScenarioFlags(0xA0, 5)
    SetScenarioFlags(0xA0, 6)

    label("loc_6F56")

    SetScenarioFlags(0xA0, 3)

    label("loc_6F59")

    SetScenarioFlags(0xA0, 2)

    label("loc_6F5C")

    SetScenarioFlags(0xA0, 1)

    label("loc_6F5F")

    SetScenarioFlags(0xA0, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F80")

    label("loc_6F71")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6F80")

    label("loc_6F80")

    Jump("loc_6CE5")

    label("loc_6F85")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_47_6CC9 end

    def Function_48_6F93(): pass

    label("Function_48_6F93")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    SetScenarioFlags(0xA0, 0)
    SetScenarioFlags(0xA0, 1)
    SetScenarioFlags(0xA0, 2)
    SetScenarioFlags(0xA0, 3)
    SetScenarioFlags(0xA0, 4)
    SetScenarioFlags(0xA0, 5)
    SetScenarioFlags(0xA0, 6)
    SetScenarioFlags(0xA0, 7)
    SetScenarioFlags(0xA1, 0)
    SetScenarioFlags(0xA1, 1)
    SetScenarioFlags(0xA1, 2)
    SetScenarioFlags(0xA1, 3)
    SetScenarioFlags(0xA1, 4)
    SetScenarioFlags(0xAA, 2)
    SetScenarioFlags(0xA1, 5)
    SetScenarioFlags(0xA1, 6)
    SetScenarioFlags(0xA1, 7)
    SetScenarioFlags(0xA2, 0)
    SetScenarioFlags(0xA2, 1)
    SetScenarioFlags(0xA2, 2)
    SetScenarioFlags(0xA2, 3)
    SetScenarioFlags(0xA2, 4)
    SetScenarioFlags(0xA2, 5)
    SetScenarioFlags(0xA2, 6)
    SetScenarioFlags(0xA2, 7)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6FF1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7247")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼?記念祭最終日\x01",                      # 0
            "★「ミシュラムに到着した」\x01",           # 1
            "★「ブティックに向かう」\x01",             # 2
            "★「??????会場に向かう」\x01",             # 3
            "★「??????会場に到着した」\x01",           # 4
            "★「マリアベルと合流した」\x01",           # 5
            "★「屋敷に異変が起きた」\x01",             # 6
            "★「キーアを発見した」\x01",               # 7
            "▼?幕間\x01",                              # 8
            "★「??????????に相談した」\x01",           # 9
            "★「????病院に到着した」\x01",             # 10
            "★「???を追いかけることにした」\x01",      # 11
            "キャンセル\x01",                           # 12
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (7, "loc_7188"),
        (6, "loc_7191"),
        (5, "loc_7194"),
        (4, "loc_71AF"),
        (3, "loc_71B2"),
        (2, "loc_71B5"),
        (1, "loc_71C7"),
        (0, "loc_71D6"),
        (11, "loc_71FA"),
        (10, "loc_7203"),
        (9, "loc_7209"),
        (8, "loc_7215"),
        (SWITCH_DEFAULT, "loc_7233"),
    )


    label("loc_7188")

    SetScenarioFlags(0xA6, 3)
    SetScenarioFlags(0xA6, 4)
    SetScenarioFlags(0xA6, 5)

    label("loc_7191")

    SetScenarioFlags(0xA6, 2)

    label("loc_7194")

    SetScenarioFlags(0xA5, 1)
    SetScenarioFlags(0xA5, 2)
    SetScenarioFlags(0xA5, 3)
    SetScenarioFlags(0xA5, 4)
    SetScenarioFlags(0xA5, 5)
    SetScenarioFlags(0xA5, 6)
    SetScenarioFlags(0xA5, 7)
    SetScenarioFlags(0xA6, 0)
    SetScenarioFlags(0xA6, 1)

    label("loc_71AF")

    SetScenarioFlags(0xA5, 0)

    label("loc_71B2")

    SetScenarioFlags(0xA4, 7)

    label("loc_71B5")

    SetScenarioFlags(0xA4, 1)
    SetScenarioFlags(0xA4, 2)
    SetScenarioFlags(0xA4, 3)
    SetScenarioFlags(0xA4, 4)
    SetScenarioFlags(0xA4, 5)
    SetScenarioFlags(0xA4, 6)

    label("loc_71C7")

    SetScenarioFlags(0xA3, 4)
    SetScenarioFlags(0xA3, 5)
    SetScenarioFlags(0xA3, 6)
    SetScenarioFlags(0xA3, 7)
    SetScenarioFlags(0xA4, 0)

    label("loc_71D6")

    SetScenarioFlags(0xA3, 0)
    SetScenarioFlags(0xA3, 1)
    SetScenarioFlags(0xA3, 2)
    SetScenarioFlags(0xA3, 3)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7242")

    label("loc_71FA")

    SetScenarioFlags(0xA8, 5)
    SetScenarioFlags(0xA8, 6)
    SetScenarioFlags(0xA8, 7)

    label("loc_7203")

    SetScenarioFlags(0xA8, 3)
    SetScenarioFlags(0xA8, 4)

    label("loc_7209")

    SetScenarioFlags(0xA7, 7)
    SetScenarioFlags(0xA8, 0)
    SetScenarioFlags(0xA8, 1)
    SetScenarioFlags(0xA8, 2)

    label("loc_7215")

    SetScenarioFlags(0xA7, 6)
    Call(2, 8)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7242")

    label("loc_7233")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7242")

    label("loc_7242")

    Jump("loc_6FF1")

    label("loc_7247")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_48_6F93 end

    def Function_49_7255(): pass

    label("Function_49_7255")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7277")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74DF")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼?四章開始（１日目）\x01",               # 0
            "★「??????市?車両??戻?事???」\x01",       # 1
            "★「オーナーから話を聞いた」\x01",        # 2
            "▼?四章２日目（黒月襲撃）\x01",           # 3
            "★「一課?協力??薬物捜査?始??」\x01",      # 4
            "★「??????に戻ることにした」\x01",        # 5
            "▼?四章３日目（失踪者）\x01",             # 6
            "★「住宅街の証券マンの失踪」\x01",        # 7
            "★「??????からの連絡が来た」\x01",        # 8
            "★「会長室の探索を開始した」\x01",        # 9
            "キャンセル\x01",                          # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (9, "loc_73F9"),
        (8, "loc_743B"),
        (7, "loc_744A"),
        (6, "loc_744D"),
        (5, "loc_7450"),
        (4, "loc_745F"),
        (3, "loc_7471"),
        (2, "loc_747D"),
        (1, "loc_748F"),
        (0, "loc_74B0"),
        (SWITCH_DEFAULT, "loc_74CB"),
    )


    label("loc_73F9")

    SetScenarioFlags(0xC4, 0)
    SetScenarioFlags(0xC4, 1)
    SetScenarioFlags(0xC4, 2)
    SetScenarioFlags(0xC4, 3)
    SetScenarioFlags(0xC4, 4)
    SetScenarioFlags(0xC4, 5)
    SetScenarioFlags(0xC4, 6)
    SetScenarioFlags(0xC4, 7)
    SetScenarioFlags(0xC5, 0)
    SetScenarioFlags(0xC5, 1)
    SetScenarioFlags(0xC5, 2)
    SetScenarioFlags(0xC5, 3)
    SetScenarioFlags(0xC6, 5)
    SetScenarioFlags(0xC5, 4)
    SetScenarioFlags(0xC5, 5)
    SetScenarioFlags(0xC5, 6)
    SetScenarioFlags(0xC5, 7)
    SetScenarioFlags(0xC6, 0)
    SetScenarioFlags(0xC6, 1)
    SetScenarioFlags(0xC6, 2)
    SetScenarioFlags(0xC6, 6)
    SetScenarioFlags(0xC6, 7)

    label("loc_743B")

    SetScenarioFlags(0xC3, 7)
    SetScenarioFlags(0xC8, 0)
    SetScenarioFlags(0xC8, 1)
    SetScenarioFlags(0xC8, 2)
    SetScenarioFlags(0xC8, 4)

    label("loc_744A")

    SetScenarioFlags(0xC8, 3)

    label("loc_744D")

    SetScenarioFlags(0xC3, 6)

    label("loc_7450")

    SetScenarioFlags(0xC3, 1)
    SetScenarioFlags(0xC3, 2)
    SetScenarioFlags(0xC3, 3)
    SetScenarioFlags(0xC3, 4)
    SetScenarioFlags(0xC3, 5)

    label("loc_745F")

    SetScenarioFlags(0xC2, 3)
    SetScenarioFlags(0xC2, 4)
    SetScenarioFlags(0xC2, 5)
    SetScenarioFlags(0xC2, 6)
    SetScenarioFlags(0xC2, 7)
    SetScenarioFlags(0xC3, 0)

    label("loc_7471")

    SetScenarioFlags(0xC1, 7)
    SetScenarioFlags(0xC2, 0)
    SetScenarioFlags(0xC2, 1)
    SetScenarioFlags(0xC2, 2)

    label("loc_747D")

    SetScenarioFlags(0xC1, 4)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xC1, 5)
    SetScenarioFlags(0xC1, 6)

    label("loc_748F")

    SetScenarioFlags(0xC0, 1)
    SetScenarioFlags(0xC0, 2)
    SetScenarioFlags(0xC0, 3)
    SetScenarioFlags(0xC0, 4)
    SetScenarioFlags(0xC0, 5)
    SetScenarioFlags(0xC0, 6)
    SetScenarioFlags(0xC0, 7)
    SetScenarioFlags(0xC1, 0)
    SetScenarioFlags(0xC1, 1)
    SetScenarioFlags(0xC1, 2)
    SetScenarioFlags(0xC1, 3)

    label("loc_74B0")

    SetScenarioFlags(0xC0, 0)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_74DA")

    label("loc_74CB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_74DA")

    label("loc_74DA")

    Jump("loc_7277")

    label("loc_74DF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_49_7255 end

    def Function_50_74ED(): pass

    label("Function_50_74ED")

    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    Call(2, 10)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7512")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7680")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼21夕方のクロスベル市\x01",              # 0
            "★「ダドリーからの連絡が来た」\x01",      # 1
            "★「無人のバスを発見した」\x01",          # 2
            "★「少し休憩することにした」\x01",        # 3
            "★「総裁室からの連絡が来た」\x01",        # 4
            "キャンセル\x01",                          # 5
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (4, "loc_75EB"),
        (3, "loc_75FD"),
        (2, "loc_7654"),
        (1, "loc_7657"),
        (0, "loc_765A"),
        (SWITCH_DEFAULT, "loc_766C"),
    )


    label("loc_75EB")

    SetScenarioFlags(0xE4, 0)
    SetScenarioFlags(0xE4, 1)
    SetScenarioFlags(0xE4, 2)
    SetScenarioFlags(0xE4, 3)
    SetScenarioFlags(0xE4, 4)
    SetScenarioFlags(0xE7, 5)

    label("loc_75FD")

    SetScenarioFlags(0xE0, 3)
    SetScenarioFlags(0xE0, 4)
    SetScenarioFlags(0xE0, 5)
    SetScenarioFlags(0xE0, 6)
    SetScenarioFlags(0xE0, 7)
    SetScenarioFlags(0xE1, 0)
    SetScenarioFlags(0xE1, 1)
    SetScenarioFlags(0xE1, 2)
    SetScenarioFlags(0xE1, 3)
    SetScenarioFlags(0xE1, 4)
    SetScenarioFlags(0xE1, 5)
    SetScenarioFlags(0xE1, 6)
    SetScenarioFlags(0xE1, 7)
    SetScenarioFlags(0xE2, 0)
    SetScenarioFlags(0xE2, 1)
    SetScenarioFlags(0xE2, 2)
    SetScenarioFlags(0xE2, 3)
    SetScenarioFlags(0xE2, 4)
    SetScenarioFlags(0xE2, 5)
    SetScenarioFlags(0xE2, 6)
    SetScenarioFlags(0xE2, 7)
    SetScenarioFlags(0xE3, 0)
    SetScenarioFlags(0xE3, 1)
    SetScenarioFlags(0xE3, 2)
    SetScenarioFlags(0xE3, 3)
    SetScenarioFlags(0xE3, 4)
    SetScenarioFlags(0xE3, 5)
    SetScenarioFlags(0xE3, 6)
    SetScenarioFlags(0xE3, 7)

    label("loc_7654")

    SetScenarioFlags(0xE0, 2)

    label("loc_7657")

    SetScenarioFlags(0xE0, 1)

    label("loc_765A")

    SetScenarioFlags(0xE0, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_767B")

    label("loc_766C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_767B")

    label("loc_767B")

    Jump("loc_7512")

    label("loc_7680")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_50_74ED end

    def Function_51_768E(): pass

    label("Function_51_768E")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7698")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_779B")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "★エリィが好き\x01",        # 0
            "★ティオが好き\x01",        # 1
            "★ランディが好き\x01",      # 2
            "キャンセル\x01",            # 3
        )
    )

    MenuEnd(0x5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_7709"),
        (1, "loc_7733"),
        (2, "loc_775D"),
        (SWITCH_DEFAULT, "loc_7787"),
    )


    label("loc_7709")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x41), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7796")

    label("loc_7733")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x41), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7796")

    label("loc_775D")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x67, (scpexpr(EXPR_PUSH_LONG, 0x41), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7796")

    label("loc_7787")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7796")

    label("loc_7796")

    Jump("loc_7698")

    label("loc_779B")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_51_768E end

    def Function_52_77A9(): pass

    label("Function_52_77A9")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_77B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7886")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "★エリィを選んだ\x01",        # 0
            "★ティオを選んだ\x01",        # 1
            "★ランディを選んだ\x01",      # 2
            "キャンセル\x01",              # 3
        )
    )

    MenuEnd(0x5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_782A"),
        (1, "loc_7842"),
        (2, "loc_785A"),
        (SWITCH_DEFAULT, "loc_7872"),
    )


    label("loc_782A")

    SetScenarioFlags(0xA9, 1)
    ClearScenarioFlags(0xA9, 2)
    ClearScenarioFlags(0xA9, 3)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7881")

    label("loc_7842")

    SetScenarioFlags(0xA9, 2)
    ClearScenarioFlags(0xA9, 1)
    ClearScenarioFlags(0xA9, 3)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7881")

    label("loc_785A")

    SetScenarioFlags(0xA9, 3)
    ClearScenarioFlags(0xA9, 1)
    ClearScenarioFlags(0xA9, 2)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7881")

    label("loc_7872")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_7881")

    label("loc_7881")

    Jump("loc_77B3")

    label("loc_7886")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_52_77A9 end

    def Function_53_7894(): pass

    label("Function_53_7894")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_789E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7971")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "★エリィを選んだ\x01",        # 0
            "★ティオを選んだ\x01",        # 1
            "★ランディを選んだ\x01",      # 2
            "キャンセル\x01",              # 3
        )
    )

    MenuEnd(0x5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_7915"),
        (1, "loc_792D"),
        (2, "loc_7945"),
        (SWITCH_DEFAULT, "loc_795D"),
    )


    label("loc_7915")

    SetScenarioFlags(0xA9, 4)
    ClearScenarioFlags(0xA9, 5)
    ClearScenarioFlags(0xA9, 6)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_796C")

    label("loc_792D")

    SetScenarioFlags(0xA9, 5)
    ClearScenarioFlags(0xA9, 4)
    ClearScenarioFlags(0xA9, 6)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_796C")

    label("loc_7945")

    SetScenarioFlags(0xA9, 6)
    ClearScenarioFlags(0xA9, 4)
    ClearScenarioFlags(0xA9, 5)
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_796C")

    label("loc_795D")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_796C")

    label("loc_796C")

    Jump("loc_789E")

    label("loc_7971")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_53_7894 end

    def Function_54_797F(): pass

    label("Function_54_797F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7989")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B7FA")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "▼クエスト序章～１章\x01",      # 0
            "▼クエスト   ２章\x01",         # 1
            "▼クエスト   ３章\x01",         # 2
            "▼クエスト   幕間\x01",         # 3
            "▼クエスト４章～終章\x01",      # 4
            "▼手配魔獣と戦う\x01",          # 5
            "▼全内容確認\x01",              # 6
            "キャンセル\x01",                # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7A61"),
        (1, "loc_7A69"),
        (2, "loc_7A71"),
        (3, "loc_7A79"),
        (4, "loc_7A81"),
        (5, "loc_7A89"),
        (6, "loc_8AF4"),
        (SWITCH_DEFAULT, "loc_B7E6"),
    )


    label("loc_7A61")

    Call(2, 55)
    Jump("loc_B7F5")

    label("loc_7A69")

    Call(2, 56)
    Jump("loc_B7F5")

    label("loc_7A71")

    Call(2, 57)
    Jump("loc_B7F5")

    label("loc_7A79")

    Call(2, 58)
    Jump("loc_B7F5")

    label("loc_7A81")

    Call(2, 59)
    Jump("loc_B7F5")

    label("loc_7A89")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7A93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8AE2")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "序 手配魔獣①メガロバット*1+お供\x01",       # 0
            "１ 手配魔獣②フォールワシ*2\x01",            # 1
            "２ 手配魔獣③ネペンテスＧ*3\x01",            # 2
            "２ 手配魔獣④サベージホーン*2\x01",          # 3
            "３ 手配魔獣⑤メガロクイーン*1お供\x01",      # 4
            "３ 手配魔獣⑥セピスデーモン*2\x01",          # 5
            "３ 手配魔獣⑦カニバボリャーＧ*2\x01",        # 6
            "３ 手配魔獣⑧鉄鋼ドリュー*1+お供\x01",       # 7
            "イ 手配魔獣⑨ゴルドチャバネイ*1\x01",        # 8
            "４ 手配魔獣⑩ビジョウ*2\x01",                # 9
            "４ 手配魔獣?ケツアルコアトル*2\x01",         # 10
            "４ 手配魔獣?オーグヴィラージ*2\x01",         # 11
            "４ 手配魔獣?ダークレジェンド*2\x01",         # 12
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7C93"),
        (1, "loc_7DBD"),
        (2, "loc_7F1E"),
        (3, "loc_801F"),
        (4, "loc_8150"),
        (5, "loc_8254"),
        (6, "loc_8361"),
        (7, "loc_8489"),
        (8, "loc_85E1"),
        (9, "loc_86E8"),
        (10, "loc_87FB"),
        (11, "loc_8944"),
        (12, "loc_8944"),
        (SWITCH_DEFAULT, "loc_8ACE"),
    )


    label("loc_7C93")

    OP_29(0x35, 0x3, 0x0)
    OP_29(0x35, 0x3, 0x1)
    OP_29(0x35, 0x3, 0x2)
    OP_29(0x35, 0x3, 0x10)
    OP_29(0x35, 0x3, 0x20)
    OP_29(0x35, 0x3, 0x40)
    OP_29(0x35, 0x2, 0x0)
    OP_29(0x35, 0x2, 0x1)
    OP_29(0x35, 0x2, 0x2)
    OP_29(0x35, 0x2, 0x3)
    OP_29(0x35, 0x2, 0x4)
    OP_29(0x35, 0x2, 0x5)
    OP_29(0x35, 0x2, 0x6)
    OP_29(0x35, 0x2, 0x7)
    OP_29(0x35, 0x2, 0x8)
    OP_29(0x35, 0x2, 0x9)
    OP_29(0x35, 0x2, 0xA)
    OP_29(0x35, 0x2, 0xB)
    OP_29(0x35, 0x2, 0xC)
    OP_29(0x35, 0x2, 0xD)
    OP_29(0x35, 0x2, 0xE)
    OP_29(0x35, 0x2, 0xF)
    OP_29(0x35, 0x2, 0x10)
    OP_29(0x35, 0x2, 0x11)
    OP_29(0x35, 0x2, 0x12)
    OP_29(0x35, 0x2, 0x13)
    OP_29(0x35, 0x2, 0x14)
    OP_29(0x35, 0x2, 0x15)
    OP_29(0x35, 0x2, 0x16)
    OP_29(0x35, 0x2, 0x17)
    OP_29(0x35, 0x2, 0x18)
    OP_29(0x35, 0x2, 0x19)
    OP_29(0x35, 0x2, 0x1A)
    OP_29(0x35, 0x2, 0x1B)
    OP_29(0x35, 0x2, 0x1C)
    OP_29(0x35, 0x2, 0x1D)
    OP_29(0x35, 0x2, 0x1E)
    OP_29(0x35, 0x2, 0x1F)
    Call(2, 4)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x41, 6)
    SetScenarioFlags(0x41, 5)
    SetScenarioFlags(0x41, 2)
    SetScenarioFlags(0x41, 3)
    SetScenarioFlags(0x41, 4)
    SetScenarioFlags(0x40, 2)
    SetScenarioFlags(0x40, 3)
    SetScenarioFlags(0x40, 4)
    SetScenarioFlags(0x40, 5)
    SetScenarioFlags(0x40, 6)
    SetScenarioFlags(0x40, 7)
    SetScenarioFlags(0x41, 0)
    SetScenarioFlags(0x41, 1)
    SetScenarioFlags(0x40, 0)
    SetScenarioFlags(0x40, 1)
    OP_29(0x35, 0x4, 0x2)
    NewScene("m0002", 0, 0, 0)
    IdleLoop()
    Jump("loc_8ADD")

    label("loc_7DBD")

    OP_29(0xB, 0x3, 0x0)
    OP_29(0xB, 0x3, 0x1)
    OP_29(0xB, 0x3, 0x2)
    OP_29(0xB, 0x3, 0x10)
    OP_29(0xB, 0x3, 0x20)
    OP_29(0xB, 0x3, 0x40)
    OP_29(0xB, 0x2, 0x0)
    OP_29(0xB, 0x2, 0x1)
    OP_29(0xB, 0x2, 0x2)
    OP_29(0xB, 0x2, 0x3)
    OP_29(0xB, 0x2, 0x4)
    OP_29(0xB, 0x2, 0x5)
    OP_29(0xB, 0x2, 0x6)
    OP_29(0xB, 0x2, 0x7)
    OP_29(0xB, 0x2, 0x8)
    OP_29(0xB, 0x2, 0x9)
    OP_29(0xB, 0x2, 0xA)
    OP_29(0xB, 0x2, 0xB)
    OP_29(0xB, 0x2, 0xC)
    OP_29(0xB, 0x2, 0xD)
    OP_29(0xB, 0x2, 0xE)
    OP_29(0xB, 0x2, 0xF)
    OP_29(0xB, 0x2, 0x10)
    OP_29(0xB, 0x2, 0x11)
    OP_29(0xB, 0x2, 0x12)
    OP_29(0xB, 0x2, 0x13)
    OP_29(0xB, 0x2, 0x14)
    OP_29(0xB, 0x2, 0x15)
    OP_29(0xB, 0x2, 0x16)
    OP_29(0xB, 0x2, 0x17)
    OP_29(0xB, 0x2, 0x18)
    OP_29(0xB, 0x2, 0x19)
    OP_29(0xB, 0x2, 0x1A)
    OP_29(0xB, 0x2, 0x1B)
    OP_29(0xB, 0x2, 0x1C)
    OP_29(0xB, 0x2, 0x1D)
    OP_29(0xB, 0x2, 0x1E)
    OP_29(0xB, 0x2, 0x1F)
    Call(2, 4)
    Call(2, 5)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x64, 0)
    SetScenarioFlags(0x64, 1)
    SetScenarioFlags(0x63, 2)
    SetScenarioFlags(0x63, 3)
    SetScenarioFlags(0x63, 4)
    SetScenarioFlags(0x63, 5)
    SetScenarioFlags(0x63, 6)
    SetScenarioFlags(0x63, 7)
    SetScenarioFlags(0x62, 2)
    SetScenarioFlags(0x62, 3)
    SetScenarioFlags(0x62, 4)
    SetScenarioFlags(0x62, 5)
    SetScenarioFlags(0x62, 6)
    SetScenarioFlags(0x62, 7)
    SetScenarioFlags(0x63, 0)
    SetScenarioFlags(0x63, 1)
    SetScenarioFlags(0x62, 1)
    SetScenarioFlags(0x61, 3)
    SetScenarioFlags(0x61, 4)
    SetScenarioFlags(0x61, 5)
    SetScenarioFlags(0x61, 6)
    SetScenarioFlags(0x61, 7)
    SetScenarioFlags(0x62, 0)
    SetScenarioFlags(0x61, 2)
    SetScenarioFlags(0x61, 1)
    SetScenarioFlags(0x60, 7)
    SetScenarioFlags(0x61, 0)
    SetScenarioFlags(0x60, 1)
    SetScenarioFlags(0x60, 2)
    SetScenarioFlags(0x60, 3)
    SetScenarioFlags(0x60, 4)
    SetScenarioFlags(0x60, 5)
    SetScenarioFlags(0x60, 6)
    SetScenarioFlags(0x60, 0)
    NewScene("r2040", 0, 0, 0)
    IdleLoop()
    Jump("loc_8ADD")

    label("loc_7F1E")

    OP_29(0x10, 0x3, 0x0)
    OP_29(0x10, 0x3, 0x1)
    OP_29(0x10, 0x3, 0x2)
    OP_29(0x10, 0x3, 0x10)
    OP_29(0x10, 0x3, 0x20)
    OP_29(0x10, 0x3, 0x40)
    OP_29(0x10, 0x2, 0x0)
    OP_29(0x10, 0x2, 0x1)
    OP_29(0x10, 0x2, 0x2)
    OP_29(0x10, 0x2, 0x3)
    OP_29(0x10, 0x2, 0x4)
    OP_29(0x10, 0x2, 0x5)
    OP_29(0x10, 0x2, 0x6)
    OP_29(0x10, 0x2, 0x7)
    OP_29(0x10, 0x2, 0x8)
    OP_29(0x10, 0x2, 0x9)
    OP_29(0x10, 0x2, 0xA)
    OP_29(0x10, 0x2, 0xB)
    OP_29(0x10, 0x2, 0xC)
    OP_29(0x10, 0x2, 0xD)
    OP_29(0x10, 0x2, 0xE)
    OP_29(0x10, 0x2, 0xF)
    OP_29(0x10, 0x2, 0x10)
    OP_29(0x10, 0x2, 0x11)
    OP_29(0x10, 0x2, 0x12)
    OP_29(0x10, 0x2, 0x13)
    OP_29(0x10, 0x2, 0x14)
    OP_29(0x10, 0x2, 0x15)
    OP_29(0x10, 0x2, 0x16)
    OP_29(0x10, 0x2, 0x17)
    OP_29(0x10, 0x2, 0x18)
    OP_29(0x10, 0x2, 0x19)
    OP_29(0x10, 0x2, 0x1A)
    OP_29(0x10, 0x2, 0x1B)
    OP_29(0x10, 0x2, 0x1C)
    OP_29(0x10, 0x2, 0x1D)
    OP_29(0x10, 0x2, 0x1E)
    OP_29(0x10, 0x2, 0x1F)
    Call(2, 4)
    Call(2, 5)
    Call(2, 6)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x80, 0)
    NewScene("r1030", 0, 0, 0)
    IdleLoop()
    Jump("loc_8ADD")

    label("loc_801F")

    OP_29(0x14, 0x3, 0x0)
    OP_29(0x14, 0x3, 0x1)
    OP_29(0x14, 0x3, 0x2)
    OP_29(0x14, 0x3, 0x10)
    OP_29(0x14, 0x3, 0x20)
    OP_29(0x14, 0x3, 0x40)
    OP_29(0x14, 0x2, 0x0)
    OP_29(0x14, 0x2, 0x1)
    OP_29(0x14, 0x2, 0x2)
    OP_29(0x14, 0x2, 0x3)
    OP_29(0x14, 0x2, 0x4)
    OP_29(0x14, 0x2, 0x5)
    OP_29(0x14, 0x2, 0x6)
    OP_29(0x14, 0x2, 0x7)
    OP_29(0x14, 0x2, 0x8)
    OP_29(0x14, 0x2, 0x9)
    OP_29(0x14, 0x2, 0xA)
    OP_29(0x14, 0x2, 0xB)
    OP_29(0x14, 0x2, 0xC)
    OP_29(0x14, 0x2, 0xD)
    OP_29(0x14, 0x2, 0xE)
    OP_29(0x14, 0x2, 0xF)
    OP_29(0x14, 0x2, 0x10)
    OP_29(0x14, 0x2, 0x11)
    OP_29(0x14, 0x2, 0x12)
    OP_29(0x14, 0x2, 0x13)
    OP_29(0x14, 0x2, 0x14)
    OP_29(0x14, 0x2, 0x15)
    OP_29(0x14, 0x2, 0x16)
    OP_29(0x14, 0x2, 0x17)
    OP_29(0x14, 0x2, 0x18)
    OP_29(0x14, 0x2, 0x19)
    OP_29(0x14, 0x2, 0x1A)
    OP_29(0x14, 0x2, 0x1B)
    OP_29(0x14, 0x2, 0x1C)
    OP_29(0x14, 0x2, 0x1D)
    OP_29(0x14, 0x2, 0x1E)
    OP_29(0x14, 0x2, 0x1F)
    Call(2, 4)
    Call(2, 5)
    Call(2, 6)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x81, 7)
    SetScenarioFlags(0x82, 0)
    SetScenarioFlags(0x81, 6)
    SetScenarioFlags(0x81, 0)
    SetScenarioFlags(0x81, 1)
    SetScenarioFlags(0x81, 2)
    SetScenarioFlags(0x81, 3)
    SetScenarioFlags(0x81, 4)
    SetScenarioFlags(0x81, 5)
    SetScenarioFlags(0x80, 1)
    SetScenarioFlags(0x80, 2)
    SetScenarioFlags(0x80, 3)
    SetScenarioFlags(0x80, 4)
    SetScenarioFlags(0x80, 5)
    SetScenarioFlags(0x80, 6)
    SetScenarioFlags(0x80, 7)
    SetScenarioFlags(0x80, 0)
    NewScene("r0040", 0, 0, 0)
    IdleLoop()
    Jump("loc_8ADD")

    label("loc_8150")

    OP_29(0x1A, 0x3, 0x0)
    OP_29(0x1A, 0x3, 0x1)
    OP_29(0x1A, 0x3, 0x2)
    OP_29(0x1A, 0x3, 0x10)
    OP_29(0x1A, 0x3, 0x20)
    OP_29(0x1A, 0x3, 0x40)
    OP_29(0x1A, 0x2, 0x0)
    OP_29(0x1A, 0x2, 0x1)
    OP_29(0x1A, 0x2, 0x2)
    OP_29(0x1A, 0x2, 0x3)
    OP_29(0x1A, 0x2, 0x4)
    OP_29(0x1A, 0x2, 0x5)
    OP_29(0x1A, 0x2, 0x6)
    OP_29(0x1A, 0x2, 0x7)
    OP_29(0x1A, 0x2, 0x8)
    OP_29(0x1A, 0x2, 0x9)
    OP_29(0x1A, 0x2, 0xA)
    OP_29(0x1A, 0x2, 0xB)
    OP_29(0x1A, 0x2, 0xC)
    OP_29(0x1A, 0x2, 0xD)
    OP_29(0x1A, 0x2, 0xE)
    OP_29(0x1A, 0x2, 0xF)
    OP_29(0x1A, 0x2, 0x10)
    OP_29(0x1A, 0x2, 0x11)
    OP_29(0x1A, 0x2, 0x12)
    OP_29(0x1A, 0x2, 0x13)
    OP_29(0x1A, 0x2, 0x14)
    OP_29(0x1A, 0x2, 0x15)
    OP_29(0x1A, 0x2, 0x16)
    OP_29(0x1A, 0x2, 0x17)
    OP_29(0x1A, 0x2, 0x18)
    OP_29(0x1A, 0x2, 0x19)
    OP_29(0x1A, 0x2, 0x1A)
    OP_29(0x1A, 0x2, 0x1B)
    OP_29(0x1A, 0x2, 0x1C)
    OP_29(0x1A, 0x2, 0x1D)
    OP_29(0x1A, 0x2, 0x1E)
    OP_29(0x1A, 0x2, 0x1F)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(2, 4)
    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    SetScenarioFlags(0xA0, 0)
    NewScene("m0102", 0, 0, 0)
    IdleLoop()
    Jump("loc_8ADD")

    label("loc_8254")

    OP_29(0x1E, 0x3, 0x0)
    OP_29(0x1E, 0x3, 0x1)
    OP_29(0x1E, 0x3, 0x2)
    OP_29(0x1E, 0x3, 0x10)
    OP_29(0x1E, 0x3, 0x20)
    OP_29(0x1E, 0x3, 0x40)
    OP_29(0x1E, 0x2, 0x0)
    OP_29(0x1E, 0x2, 0x1)
    OP_29(0x1E, 0x2, 0x2)
    OP_29(0x1E, 0x2, 0x3)
    OP_29(0x1E, 0x2, 0x4)
    OP_29(0x1E, 0x2, 0x5)
    OP_29(0x1E, 0x2, 0x6)
    OP_29(0x1E, 0x2, 0x7)
    OP_29(0x1E, 0x2, 0x8)
    OP_29(0x1E, 0x2, 0x9)
    OP_29(0x1E, 0x2, 0xA)
    OP_29(0x1E, 0x2, 0xB)
    OP_29(0x1E, 0x2, 0xC)
    OP_29(0x1E, 0x2, 0xD)
    OP_29(0x1E, 0x2, 0xE)
    OP_29(0x1E, 0x2, 0xF)
    OP_29(0x1E, 0x2, 0x10)
    OP_29(0x1E, 0x2, 0x11)
    OP_29(0x1E, 0x2, 0x12)
    OP_29(0x1E, 0x2, 0x13)
    OP_29(0x1E, 0x2, 0x14)
    OP_29(0x1E, 0x2, 0x15)
    OP_29(0x1E, 0x2, 0x16)
    OP_29(0x1E, 0x2, 0x17)
    OP_29(0x1E, 0x2, 0x18)
    OP_29(0x1E, 0x2, 0x19)
    OP_29(0x1E, 0x2, 0x1A)
    OP_29(0x1E, 0x2, 0x1B)
    OP_29(0x1E, 0x2, 0x1C)
    OP_29(0x1E, 0x2, 0x1D)
    OP_29(0x1E, 0x2, 0x1E)
    OP_29(0x1E, 0x2, 0x1F)
    Call(2, 4)
    Call(2, 4)
    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA0, 2)
    SetScenarioFlags(0xA0, 1)
    SetScenarioFlags(0xA0, 0)
    NewScene("r0110", 0, 0, 0)
    IdleLoop()
    Jump("loc_8ADD")

    label("loc_8361")

    OP_29(0x21, 0x3, 0x0)
    OP_29(0x21, 0x3, 0x1)
    OP_29(0x21, 0x3, 0x2)
    OP_29(0x21, 0x3, 0x10)
    OP_29(0x21, 0x3, 0x20)
    OP_29(0x21, 0x3, 0x40)
    OP_29(0x21, 0x2, 0x0)
    OP_29(0x21, 0x2, 0x1)
    OP_29(0x21, 0x2, 0x2)
    OP_29(0x21, 0x2, 0x3)
    OP_29(0x21, 0x2, 0x4)
    OP_29(0x21, 0x2, 0x5)
    OP_29(0x21, 0x2, 0x6)
    OP_29(0x21, 0x2, 0x7)
    OP_29(0x21, 0x2, 0x8)
    OP_29(0x21, 0x2, 0x9)
    OP_29(0x21, 0x2, 0xA)
    OP_29(0x21, 0x2, 0xB)
    OP_29(0x21, 0x2, 0xC)
    OP_29(0x21, 0x2, 0xD)
    OP_29(0x21, 0x2, 0xE)
    OP_29(0x21, 0x2, 0xF)
    OP_29(0x21, 0x2, 0x10)
    OP_29(0x21, 0x2, 0x11)
    OP_29(0x21, 0x2, 0x12)
    OP_29(0x21, 0x2, 0x13)
    OP_29(0x21, 0x2, 0x14)
    OP_29(0x21, 0x2, 0x15)
    OP_29(0x21, 0x2, 0x16)
    OP_29(0x21, 0x2, 0x17)
    OP_29(0x21, 0x2, 0x18)
    OP_29(0x21, 0x2, 0x19)
    OP_29(0x21, 0x2, 0x1A)
    OP_29(0x21, 0x2, 0x1B)
    OP_29(0x21, 0x2, 0x1C)
    OP_29(0x21, 0x2, 0x1D)
    OP_29(0x21, 0x2, 0x1E)
    OP_29(0x21, 0x2, 0x1F)
    Call(2, 4)
    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA0, 7)
    SetScenarioFlags(0xA1, 0)
    SetScenarioFlags(0xA1, 1)
    SetScenarioFlags(0xA1, 2)
    SetScenarioFlags(0xA1, 3)
    SetScenarioFlags(0xA1, 4)
    SetScenarioFlags(0xA0, 4)
    SetScenarioFlags(0xA0, 5)
    SetScenarioFlags(0xA0, 6)
    SetScenarioFlags(0xA0, 3)
    SetScenarioFlags(0xA0, 2)
    SetScenarioFlags(0xA0, 1)
    SetScenarioFlags(0xA0, 0)
    NewScene("r0020", 0, 0, 0)
    IdleLoop()
    Jump("loc_8ADD")

    label("loc_8489")

    OP_29(0x23, 0x3, 0x0)
    OP_29(0x23, 0x3, 0x1)
    OP_29(0x23, 0x3, 0x2)
    OP_29(0x23, 0x3, 0x10)
    OP_29(0x23, 0x3, 0x20)
    OP_29(0x23, 0x3, 0x40)
    OP_29(0x23, 0x2, 0x0)
    OP_29(0x23, 0x2, 0x1)
    OP_29(0x23, 0x2, 0x2)
    OP_29(0x23, 0x2, 0x3)
    OP_29(0x23, 0x2, 0x4)
    OP_29(0x23, 0x2, 0x5)
    OP_29(0x23, 0x2, 0x6)
    OP_29(0x23, 0x2, 0x7)
    OP_29(0x23, 0x2, 0x8)
    OP_29(0x23, 0x2, 0x9)
    OP_29(0x23, 0x2, 0xA)
    OP_29(0x23, 0x2, 0xB)
    OP_29(0x23, 0x2, 0xC)
    OP_29(0x23, 0x2, 0xD)
    OP_29(0x23, 0x2, 0xE)
    OP_29(0x23, 0x2, 0xF)
    OP_29(0x23, 0x2, 0x10)
    OP_29(0x23, 0x2, 0x11)
    OP_29(0x23, 0x2, 0x12)
    OP_29(0x23, 0x2, 0x13)
    OP_29(0x23, 0x2, 0x14)
    OP_29(0x23, 0x2, 0x15)
    OP_29(0x23, 0x2, 0x16)
    OP_29(0x23, 0x2, 0x17)
    OP_29(0x23, 0x2, 0x18)
    OP_29(0x23, 0x2, 0x19)
    OP_29(0x23, 0x2, 0x1A)
    OP_29(0x23, 0x2, 0x1B)
    OP_29(0x23, 0x2, 0x1C)
    OP_29(0x23, 0x2, 0x1D)
    OP_29(0x23, 0x2, 0x1E)
    OP_29(0x23, 0x2, 0x1F)
    Call(2, 4)
    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA0, 0)
    SetScenarioFlags(0xA0, 1)
    SetScenarioFlags(0xA0, 2)
    SetScenarioFlags(0xA0, 3)
    SetScenarioFlags(0xA0, 4)
    SetScenarioFlags(0xA0, 5)
    SetScenarioFlags(0xA0, 6)
    SetScenarioFlags(0xA0, 7)
    SetScenarioFlags(0xA1, 0)
    SetScenarioFlags(0xA1, 1)
    SetScenarioFlags(0xA1, 2)
    SetScenarioFlags(0xA1, 3)
    SetScenarioFlags(0xA1, 4)
    SetScenarioFlags(0xAA, 2)
    SetScenarioFlags(0xA1, 5)
    SetScenarioFlags(0xA1, 6)
    SetScenarioFlags(0xA1, 7)
    SetScenarioFlags(0xA2, 0)
    SetScenarioFlags(0xA2, 1)
    SetScenarioFlags(0xA2, 2)
    SetScenarioFlags(0xA2, 3)
    SetScenarioFlags(0xA2, 4)
    SetScenarioFlags(0xA2, 5)
    SetScenarioFlags(0xA2, 6)
    SetScenarioFlags(0xA2, 7)
    SetScenarioFlags(0xA3, 0)
    SetScenarioFlags(0xA3, 1)
    SetScenarioFlags(0xA3, 2)
    SetScenarioFlags(0xA3, 3)
    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_8ADD")

    label("loc_85E1")

    OP_29(0x25, 0x3, 0x0)
    OP_29(0x25, 0x3, 0x1)
    OP_29(0x25, 0x3, 0x2)
    OP_29(0x25, 0x3, 0x10)
    OP_29(0x25, 0x3, 0x20)
    OP_29(0x25, 0x3, 0x40)
    OP_29(0x25, 0x2, 0x0)
    OP_29(0x25, 0x2, 0x1)
    OP_29(0x25, 0x2, 0x2)
    OP_29(0x25, 0x2, 0x3)
    OP_29(0x25, 0x2, 0x4)
    OP_29(0x25, 0x2, 0x5)
    OP_29(0x25, 0x2, 0x6)
    OP_29(0x25, 0x2, 0x7)
    OP_29(0x25, 0x2, 0x8)
    OP_29(0x25, 0x2, 0x9)
    OP_29(0x25, 0x2, 0xA)
    OP_29(0x25, 0x2, 0xB)
    OP_29(0x25, 0x2, 0xC)
    OP_29(0x25, 0x2, 0xD)
    OP_29(0x25, 0x2, 0xE)
    OP_29(0x25, 0x2, 0xF)
    OP_29(0x25, 0x2, 0x10)
    OP_29(0x25, 0x2, 0x11)
    OP_29(0x25, 0x2, 0x12)
    OP_29(0x25, 0x2, 0x13)
    OP_29(0x25, 0x2, 0x14)
    OP_29(0x25, 0x2, 0x15)
    OP_29(0x25, 0x2, 0x16)
    OP_29(0x25, 0x2, 0x17)
    OP_29(0x25, 0x2, 0x18)
    OP_29(0x25, 0x2, 0x19)
    OP_29(0x25, 0x2, 0x1A)
    OP_29(0x25, 0x2, 0x1B)
    OP_29(0x25, 0x2, 0x1C)
    OP_29(0x25, 0x2, 0x1D)
    OP_29(0x25, 0x2, 0x1E)
    OP_29(0x25, 0x2, 0x1F)
    Call(2, 4)
    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xA7, 6)
    NewScene("m0013", 0, 0, 0)
    IdleLoop()
    Jump("loc_8ADD")

    label("loc_86E8")

    OP_29(0x2B, 0x3, 0x0)
    OP_29(0x2B, 0x3, 0x1)
    OP_29(0x2B, 0x3, 0x2)
    OP_29(0x2B, 0x3, 0x10)
    OP_29(0x2B, 0x3, 0x20)
    OP_29(0x2B, 0x3, 0x40)
    OP_29(0x2B, 0x2, 0x0)
    OP_29(0x2B, 0x2, 0x1)
    OP_29(0x2B, 0x2, 0x2)
    OP_29(0x2B, 0x2, 0x3)
    OP_29(0x2B, 0x2, 0x4)
    OP_29(0x2B, 0x2, 0x5)
    OP_29(0x2B, 0x2, 0x6)
    OP_29(0x2B, 0x2, 0x7)
    OP_29(0x2B, 0x2, 0x8)
    OP_29(0x2B, 0x2, 0x9)
    OP_29(0x2B, 0x2, 0xA)
    OP_29(0x2B, 0x2, 0xB)
    OP_29(0x2B, 0x2, 0xC)
    OP_29(0x2B, 0x2, 0xD)
    OP_29(0x2B, 0x2, 0xE)
    OP_29(0x2B, 0x2, 0xF)
    OP_29(0x2B, 0x2, 0x10)
    OP_29(0x2B, 0x2, 0x11)
    OP_29(0x2B, 0x2, 0x12)
    OP_29(0x2B, 0x2, 0x13)
    OP_29(0x2B, 0x2, 0x14)
    OP_29(0x2B, 0x2, 0x15)
    OP_29(0x2B, 0x2, 0x16)
    OP_29(0x2B, 0x2, 0x17)
    OP_29(0x2B, 0x2, 0x18)
    OP_29(0x2B, 0x2, 0x19)
    OP_29(0x2B, 0x2, 0x1A)
    OP_29(0x2B, 0x2, 0x1B)
    OP_29(0x2B, 0x2, 0x1C)
    OP_29(0x2B, 0x2, 0x1D)
    OP_29(0x2B, 0x2, 0x1E)
    OP_29(0x2B, 0x2, 0x1F)
    Call(2, 4)
    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xC0, 0)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("r1530", 0, 0, 0)
    IdleLoop()
    Jump("loc_8ADD")

    label("loc_87FB")

    OP_29(0x2F, 0x3, 0x0)
    OP_29(0x2F, 0x3, 0x1)
    OP_29(0x2F, 0x3, 0x2)
    OP_29(0x2F, 0x3, 0x10)
    OP_29(0x2F, 0x3, 0x20)
    OP_29(0x2F, 0x3, 0x40)
    OP_29(0x2F, 0x2, 0x0)
    OP_29(0x2F, 0x2, 0x1)
    OP_29(0x2F, 0x2, 0x2)
    OP_29(0x2F, 0x2, 0x3)
    OP_29(0x2F, 0x2, 0x4)
    OP_29(0x2F, 0x2, 0x5)
    OP_29(0x2F, 0x2, 0x6)
    OP_29(0x2F, 0x2, 0x7)
    OP_29(0x2F, 0x2, 0x8)
    OP_29(0x2F, 0x2, 0x9)
    OP_29(0x2F, 0x2, 0xA)
    OP_29(0x2F, 0x2, 0xB)
    OP_29(0x2F, 0x2, 0xC)
    OP_29(0x2F, 0x2, 0xD)
    OP_29(0x2F, 0x2, 0xE)
    OP_29(0x2F, 0x2, 0xF)
    OP_29(0x2F, 0x2, 0x10)
    OP_29(0x2F, 0x2, 0x11)
    OP_29(0x2F, 0x2, 0x12)
    OP_29(0x2F, 0x2, 0x13)
    OP_29(0x2F, 0x2, 0x14)
    OP_29(0x2F, 0x2, 0x15)
    OP_29(0x2F, 0x2, 0x16)
    OP_29(0x2F, 0x2, 0x17)
    OP_29(0x2F, 0x2, 0x18)
    OP_29(0x2F, 0x2, 0x19)
    OP_29(0x2F, 0x2, 0x1A)
    OP_29(0x2F, 0x2, 0x1B)
    OP_29(0x2F, 0x2, 0x1C)
    OP_29(0x2F, 0x2, 0x1D)
    OP_29(0x2F, 0x2, 0x1E)
    OP_29(0x2F, 0x2, 0x1F)
    Call(2, 4)
    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xC1, 7)
    SetScenarioFlags(0xC2, 0)
    SetScenarioFlags(0xC2, 1)
    SetScenarioFlags(0xC2, 2)
    SetScenarioFlags(0xC1, 4)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xC1, 5)
    SetScenarioFlags(0xC1, 6)
    SetScenarioFlags(0xC0, 1)
    SetScenarioFlags(0xC0, 2)
    SetScenarioFlags(0xC0, 3)
    SetScenarioFlags(0xC0, 4)
    SetScenarioFlags(0xC0, 5)
    SetScenarioFlags(0xC0, 6)
    SetScenarioFlags(0xC0, 7)
    SetScenarioFlags(0xC1, 0)
    SetScenarioFlags(0xC1, 1)
    SetScenarioFlags(0xC1, 2)
    SetScenarioFlags(0xC1, 3)
    SetScenarioFlags(0xC0, 0)
    NewScene("r1020", 0, 0, 0)
    IdleLoop()
    Jump("loc_8ADD")

    label("loc_8944")

    OP_29(0x32, 0x3, 0x0)
    OP_29(0x32, 0x3, 0x1)
    OP_29(0x32, 0x3, 0x2)
    OP_29(0x32, 0x3, 0x10)
    OP_29(0x32, 0x3, 0x20)
    OP_29(0x32, 0x3, 0x40)
    OP_29(0x32, 0x2, 0x0)
    OP_29(0x32, 0x2, 0x1)
    OP_29(0x32, 0x2, 0x2)
    OP_29(0x32, 0x2, 0x3)
    OP_29(0x32, 0x2, 0x4)
    OP_29(0x32, 0x2, 0x5)
    OP_29(0x32, 0x2, 0x6)
    OP_29(0x32, 0x2, 0x7)
    OP_29(0x32, 0x2, 0x8)
    OP_29(0x32, 0x2, 0x9)
    OP_29(0x32, 0x2, 0xA)
    OP_29(0x32, 0x2, 0xB)
    OP_29(0x32, 0x2, 0xC)
    OP_29(0x32, 0x2, 0xD)
    OP_29(0x32, 0x2, 0xE)
    OP_29(0x32, 0x2, 0xF)
    OP_29(0x32, 0x2, 0x10)
    OP_29(0x32, 0x2, 0x11)
    OP_29(0x32, 0x2, 0x12)
    OP_29(0x32, 0x2, 0x13)
    OP_29(0x32, 0x2, 0x14)
    OP_29(0x32, 0x2, 0x15)
    OP_29(0x32, 0x2, 0x16)
    OP_29(0x32, 0x2, 0x17)
    OP_29(0x32, 0x2, 0x18)
    OP_29(0x32, 0x2, 0x19)
    OP_29(0x32, 0x2, 0x1A)
    OP_29(0x32, 0x2, 0x1B)
    OP_29(0x32, 0x2, 0x1C)
    OP_29(0x32, 0x2, 0x1D)
    OP_29(0x32, 0x2, 0x1E)
    OP_29(0x32, 0x2, 0x1F)
    Call(2, 4)
    Call(2, 5)
    Call(2, 6)
    Call(2, 7)
    Call(2, 8)
    Call(2, 9)
    OP_50(0x4, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xC3, 6)
    SetScenarioFlags(0xC3, 1)
    SetScenarioFlags(0xC3, 2)
    SetScenarioFlags(0xC3, 3)
    SetScenarioFlags(0xC3, 4)
    SetScenarioFlags(0xC3, 5)
    SetScenarioFlags(0xC2, 3)
    SetScenarioFlags(0xC2, 4)
    SetScenarioFlags(0xC2, 5)
    SetScenarioFlags(0xC2, 6)
    SetScenarioFlags(0xC2, 7)
    SetScenarioFlags(0xC3, 0)
    SetScenarioFlags(0xC1, 7)
    SetScenarioFlags(0xC2, 0)
    SetScenarioFlags(0xC2, 1)
    SetScenarioFlags(0xC2, 2)
    SetScenarioFlags(0xC1, 4)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0xC1, 5)
    SetScenarioFlags(0xC1, 6)
    SetScenarioFlags(0xC0, 1)
    SetScenarioFlags(0xC0, 2)
    SetScenarioFlags(0xC0, 3)
    SetScenarioFlags(0xC0, 4)
    SetScenarioFlags(0xC0, 5)
    SetScenarioFlags(0xC0, 6)
    SetScenarioFlags(0xC0, 7)
    SetScenarioFlags(0xC1, 0)
    SetScenarioFlags(0xC1, 1)
    SetScenarioFlags(0xC1, 2)
    SetScenarioFlags(0xC1, 3)
    SetScenarioFlags(0xC0, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8AC0")
    NewScene("m1090", 0, 0, 0)
    IdleLoop()
    Jump("loc_8AC9")

    label("loc_8AC0")

    NewScene("r3080", 0, 0, 0)
    IdleLoop()

    label("loc_8AC9")

    Jump("loc_8ADD")

    label("loc_8ACE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8ADD")

    label("loc_8ADD")

    Jump("loc_7A93")

    label("loc_8AE2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Jump("loc_B7F5")

    label("loc_8AF4")

    OP_29(0x1, 0x4, 0x0)
    OP_29(0x1, 0x4, 0x1)
    OP_29(0x1, 0x4, 0x2)
    OP_29(0x1, 0x4, 0x10)
    OP_29(0x1, 0x4, 0x20)
    OP_29(0x2, 0x4, 0x0)
    OP_29(0x2, 0x4, 0x1)
    OP_29(0x2, 0x4, 0x2)
    OP_29(0x2, 0x4, 0x10)
    OP_29(0x2, 0x4, 0x20)
    OP_29(0x3, 0x4, 0x0)
    OP_29(0x3, 0x4, 0x1)
    OP_29(0x3, 0x4, 0x2)
    OP_29(0x3, 0x4, 0x10)
    OP_29(0x3, 0x4, 0x20)
    OP_29(0x4, 0x4, 0x0)
    OP_29(0x4, 0x4, 0x1)
    OP_29(0x4, 0x4, 0x2)
    OP_29(0x4, 0x4, 0x10)
    OP_29(0x4, 0x4, 0x20)
    OP_29(0x35, 0x4, 0x0)
    OP_29(0x35, 0x4, 0x1)
    OP_29(0x35, 0x4, 0x2)
    OP_29(0x35, 0x4, 0x10)
    OP_29(0x35, 0x4, 0x20)
    OP_29(0x5, 0x4, 0x0)
    OP_29(0x5, 0x4, 0x1)
    OP_29(0x5, 0x4, 0x2)
    OP_29(0x5, 0x4, 0x10)
    OP_29(0x5, 0x4, 0x20)
    OP_29(0x6, 0x4, 0x0)
    OP_29(0x6, 0x4, 0x1)
    OP_29(0x6, 0x4, 0x2)
    OP_29(0x6, 0x4, 0x10)
    OP_29(0x6, 0x4, 0x20)
    OP_29(0x7, 0x4, 0x0)
    OP_29(0x7, 0x4, 0x1)
    OP_29(0x7, 0x4, 0x2)
    OP_29(0x7, 0x4, 0x10)
    OP_29(0x7, 0x4, 0x20)
    OP_29(0x8, 0x4, 0x0)
    OP_29(0x8, 0x4, 0x1)
    OP_29(0x8, 0x4, 0x2)
    OP_29(0x8, 0x4, 0x10)
    OP_29(0x8, 0x4, 0x20)
    OP_29(0x9, 0x4, 0x0)
    OP_29(0x9, 0x4, 0x1)
    OP_29(0x9, 0x4, 0x2)
    OP_29(0x9, 0x4, 0x10)
    OP_29(0x9, 0x4, 0x20)
    OP_29(0xA, 0x4, 0x0)
    OP_29(0xA, 0x4, 0x1)
    OP_29(0xA, 0x4, 0x2)
    OP_29(0xA, 0x4, 0x10)
    OP_29(0xA, 0x4, 0x20)
    OP_29(0xB, 0x4, 0x0)
    OP_29(0xB, 0x4, 0x1)
    OP_29(0xB, 0x4, 0x2)
    OP_29(0xB, 0x4, 0x10)
    OP_29(0xB, 0x4, 0x20)
    OP_29(0xC, 0x4, 0x0)
    OP_29(0xC, 0x4, 0x1)
    OP_29(0xC, 0x4, 0x2)
    OP_29(0xC, 0x4, 0x10)
    OP_29(0xC, 0x4, 0x20)
    OP_29(0xD, 0x4, 0x0)
    OP_29(0xD, 0x4, 0x1)
    OP_29(0xD, 0x4, 0x2)
    OP_29(0xD, 0x4, 0x10)
    OP_29(0xD, 0x4, 0x20)
    OP_29(0xE, 0x4, 0x0)
    OP_29(0xE, 0x4, 0x1)
    OP_29(0xE, 0x4, 0x2)
    OP_29(0xE, 0x4, 0x10)
    OP_29(0xE, 0x4, 0x20)
    OP_29(0xF, 0x4, 0x0)
    OP_29(0xF, 0x4, 0x1)
    OP_29(0xF, 0x4, 0x2)
    OP_29(0xF, 0x4, 0x10)
    OP_29(0xF, 0x4, 0x20)
    OP_29(0x10, 0x4, 0x0)
    OP_29(0x10, 0x4, 0x1)
    OP_29(0x10, 0x4, 0x2)
    OP_29(0x10, 0x4, 0x10)
    OP_29(0x10, 0x4, 0x20)
    OP_29(0x11, 0x4, 0x0)
    OP_29(0x11, 0x4, 0x1)
    OP_29(0x11, 0x4, 0x2)
    OP_29(0x11, 0x4, 0x10)
    OP_29(0x11, 0x4, 0x20)
    OP_29(0x12, 0x4, 0x0)
    OP_29(0x12, 0x4, 0x1)
    OP_29(0x12, 0x4, 0x2)
    OP_29(0x12, 0x4, 0x10)
    OP_29(0x12, 0x4, 0x20)
    OP_29(0x13, 0x4, 0x0)
    OP_29(0x13, 0x4, 0x1)
    OP_29(0x13, 0x4, 0x2)
    OP_29(0x13, 0x4, 0x10)
    OP_29(0x13, 0x4, 0x20)
    OP_29(0x14, 0x4, 0x0)
    OP_29(0x14, 0x4, 0x1)
    OP_29(0x14, 0x4, 0x2)
    OP_29(0x14, 0x4, 0x10)
    OP_29(0x14, 0x4, 0x20)
    OP_29(0x15, 0x4, 0x0)
    OP_29(0x15, 0x4, 0x1)
    OP_29(0x15, 0x4, 0x2)
    OP_29(0x15, 0x4, 0x10)
    OP_29(0x15, 0x4, 0x20)
    OP_29(0x16, 0x4, 0x0)
    OP_29(0x16, 0x4, 0x1)
    OP_29(0x16, 0x4, 0x2)
    OP_29(0x16, 0x4, 0x10)
    OP_29(0x16, 0x4, 0x20)
    OP_29(0x17, 0x4, 0x0)
    OP_29(0x17, 0x4, 0x1)
    OP_29(0x17, 0x4, 0x2)
    OP_29(0x17, 0x4, 0x10)
    OP_29(0x17, 0x4, 0x20)
    OP_29(0x18, 0x4, 0x0)
    OP_29(0x18, 0x4, 0x1)
    OP_29(0x18, 0x4, 0x2)
    OP_29(0x18, 0x4, 0x10)
    OP_29(0x18, 0x4, 0x20)
    OP_29(0x19, 0x4, 0x0)
    OP_29(0x19, 0x4, 0x1)
    OP_29(0x19, 0x4, 0x2)
    OP_29(0x19, 0x4, 0x10)
    OP_29(0x19, 0x4, 0x20)
    OP_29(0x1A, 0x4, 0x0)
    OP_29(0x1A, 0x4, 0x1)
    OP_29(0x1A, 0x4, 0x2)
    OP_29(0x1A, 0x4, 0x10)
    OP_29(0x1A, 0x4, 0x20)
    OP_29(0x1B, 0x4, 0x0)
    OP_29(0x1B, 0x4, 0x1)
    OP_29(0x1B, 0x4, 0x2)
    OP_29(0x1B, 0x4, 0x10)
    OP_29(0x1B, 0x4, 0x20)
    OP_29(0x1C, 0x4, 0x0)
    OP_29(0x1C, 0x4, 0x1)
    OP_29(0x1C, 0x4, 0x2)
    OP_29(0x1C, 0x4, 0x10)
    OP_29(0x1C, 0x4, 0x20)
    OP_29(0x1D, 0x4, 0x0)
    OP_29(0x1D, 0x4, 0x1)
    OP_29(0x1D, 0x4, 0x2)
    OP_29(0x1D, 0x4, 0x10)
    OP_29(0x1D, 0x4, 0x20)
    OP_29(0x1E, 0x4, 0x0)
    OP_29(0x1E, 0x4, 0x1)
    OP_29(0x1E, 0x4, 0x2)
    OP_29(0x1E, 0x4, 0x10)
    OP_29(0x1E, 0x4, 0x20)
    OP_29(0x1F, 0x4, 0x0)
    OP_29(0x1F, 0x4, 0x1)
    OP_29(0x1F, 0x4, 0x2)
    OP_29(0x1F, 0x4, 0x10)
    OP_29(0x1F, 0x4, 0x20)
    OP_29(0x20, 0x4, 0x0)
    OP_29(0x20, 0x4, 0x1)
    OP_29(0x20, 0x4, 0x2)
    OP_29(0x20, 0x4, 0x10)
    OP_29(0x20, 0x4, 0x20)
    OP_29(0x21, 0x4, 0x0)
    OP_29(0x21, 0x4, 0x1)
    OP_29(0x21, 0x4, 0x2)
    OP_29(0x21, 0x4, 0x10)
    OP_29(0x21, 0x4, 0x20)
    OP_29(0x22, 0x4, 0x0)
    OP_29(0x22, 0x4, 0x1)
    OP_29(0x22, 0x4, 0x2)
    OP_29(0x22, 0x4, 0x10)
    OP_29(0x22, 0x4, 0x20)
    OP_29(0x23, 0x4, 0x0)
    OP_29(0x23, 0x4, 0x1)
    OP_29(0x23, 0x4, 0x2)
    OP_29(0x23, 0x4, 0x10)
    OP_29(0x23, 0x4, 0x20)
    OP_29(0x24, 0x4, 0x0)
    OP_29(0x24, 0x4, 0x1)
    OP_29(0x24, 0x4, 0x2)
    OP_29(0x24, 0x4, 0x10)
    OP_29(0x24, 0x4, 0x20)
    OP_29(0x25, 0x4, 0x0)
    OP_29(0x25, 0x4, 0x1)
    OP_29(0x25, 0x4, 0x2)
    OP_29(0x25, 0x4, 0x10)
    OP_29(0x25, 0x4, 0x20)
    OP_29(0x26, 0x4, 0x0)
    OP_29(0x26, 0x4, 0x1)
    OP_29(0x26, 0x4, 0x2)
    OP_29(0x26, 0x4, 0x10)
    OP_29(0x26, 0x4, 0x20)
    OP_29(0x27, 0x4, 0x0)
    OP_29(0x27, 0x4, 0x1)
    OP_29(0x27, 0x4, 0x2)
    OP_29(0x27, 0x4, 0x10)
    OP_29(0x27, 0x4, 0x20)
    OP_29(0x28, 0x4, 0x0)
    OP_29(0x28, 0x4, 0x1)
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x4, 0x10)
    OP_29(0x28, 0x4, 0x20)
    OP_29(0x29, 0x4, 0x0)
    OP_29(0x29, 0x4, 0x1)
    OP_29(0x29, 0x4, 0x2)
    OP_29(0x29, 0x4, 0x10)
    OP_29(0x29, 0x4, 0x20)
    OP_29(0x2A, 0x4, 0x0)
    OP_29(0x2A, 0x4, 0x1)
    OP_29(0x2A, 0x4, 0x2)
    OP_29(0x2A, 0x4, 0x10)
    OP_29(0x2A, 0x4, 0x20)
    OP_29(0x2B, 0x4, 0x0)
    OP_29(0x2B, 0x4, 0x1)
    OP_29(0x2B, 0x4, 0x2)
    OP_29(0x2B, 0x4, 0x10)
    OP_29(0x2B, 0x4, 0x20)
    OP_29(0x2C, 0x4, 0x0)
    OP_29(0x2C, 0x4, 0x1)
    OP_29(0x2C, 0x4, 0x2)
    OP_29(0x2C, 0x4, 0x10)
    OP_29(0x2C, 0x4, 0x20)
    OP_29(0x2D, 0x4, 0x0)
    OP_29(0x2D, 0x4, 0x1)
    OP_29(0x2D, 0x4, 0x2)
    OP_29(0x2D, 0x4, 0x10)
    OP_29(0x2D, 0x4, 0x20)
    OP_29(0x2E, 0x4, 0x0)
    OP_29(0x2E, 0x4, 0x1)
    OP_29(0x2E, 0x4, 0x2)
    OP_29(0x2E, 0x4, 0x10)
    OP_29(0x2E, 0x4, 0x20)
    OP_29(0x2F, 0x4, 0x0)
    OP_29(0x2F, 0x4, 0x1)
    OP_29(0x2F, 0x4, 0x2)
    OP_29(0x2F, 0x4, 0x10)
    OP_29(0x2F, 0x4, 0x20)
    OP_29(0x30, 0x4, 0x0)
    OP_29(0x30, 0x4, 0x1)
    OP_29(0x30, 0x4, 0x2)
    OP_29(0x30, 0x4, 0x10)
    OP_29(0x30, 0x4, 0x20)
    OP_29(0x31, 0x4, 0x0)
    OP_29(0x31, 0x4, 0x1)
    OP_29(0x31, 0x4, 0x2)
    OP_29(0x31, 0x4, 0x10)
    OP_29(0x31, 0x4, 0x20)
    OP_29(0x32, 0x4, 0x0)
    OP_29(0x32, 0x4, 0x1)
    OP_29(0x32, 0x4, 0x2)
    OP_29(0x32, 0x4, 0x10)
    OP_29(0x32, 0x4, 0x20)
    OP_29(0x33, 0x4, 0x0)
    OP_29(0x33, 0x4, 0x1)
    OP_29(0x33, 0x4, 0x2)
    OP_29(0x33, 0x4, 0x10)
    OP_29(0x33, 0x4, 0x20)
    OP_29(0x34, 0x4, 0x0)
    OP_29(0x34, 0x4, 0x1)
    OP_29(0x34, 0x4, 0x2)
    OP_29(0x34, 0x4, 0x10)
    OP_29(0x34, 0x4, 0x20)
    OP_29(0x1, 0x1, 0x0)
    OP_29(0x1, 0x1, 0x1)
    OP_29(0x1, 0x1, 0x2)
    OP_29(0x1, 0x1, 0x3)
    OP_29(0x1, 0x1, 0x4)
    OP_29(0x1, 0x1, 0x5)
    OP_29(0x1, 0x1, 0x6)
    OP_29(0x1, 0x1, 0x7)
    OP_29(0x1, 0x1, 0x8)
    OP_29(0x1, 0x1, 0x9)
    OP_29(0x1, 0x1, 0xA)
    OP_29(0x1, 0x1, 0xB)
    OP_29(0x1, 0x1, 0xC)
    OP_29(0x1, 0x1, 0xD)
    OP_29(0x1, 0x1, 0xE)
    OP_29(0x1, 0x1, 0xF)
    OP_29(0x1, 0x1, 0x10)
    OP_29(0x1, 0x1, 0x11)
    OP_29(0x1, 0x1, 0x12)
    OP_29(0x1, 0x1, 0x13)
    OP_29(0x1, 0x1, 0x14)
    OP_29(0x1, 0x1, 0x15)
    OP_29(0x1, 0x1, 0x16)
    OP_29(0x1, 0x1, 0x17)
    OP_29(0x1, 0x1, 0x18)
    OP_29(0x1, 0x1, 0x19)
    OP_29(0x1, 0x1, 0x1A)
    OP_29(0x1, 0x1, 0x1B)
    OP_29(0x1, 0x1, 0x1C)
    OP_29(0x1, 0x1, 0x1D)
    OP_29(0x1, 0x1, 0x1E)
    OP_29(0x1, 0x1, 0x1F)
    OP_29(0x2, 0x1, 0x0)
    OP_29(0x2, 0x1, 0x1)
    OP_29(0x2, 0x1, 0x2)
    OP_29(0x2, 0x1, 0x3)
    OP_29(0x2, 0x1, 0x4)
    OP_29(0x2, 0x1, 0x5)
    OP_29(0x2, 0x1, 0x6)
    OP_29(0x2, 0x1, 0x7)
    OP_29(0x2, 0x1, 0x8)
    OP_29(0x2, 0x1, 0x9)
    OP_29(0x2, 0x1, 0xA)
    OP_29(0x2, 0x1, 0xB)
    OP_29(0x2, 0x1, 0xC)
    OP_29(0x2, 0x1, 0xD)
    OP_29(0x2, 0x1, 0xE)
    OP_29(0x2, 0x1, 0xF)
    OP_29(0x2, 0x1, 0x10)
    OP_29(0x2, 0x1, 0x11)
    OP_29(0x2, 0x1, 0x12)
    OP_29(0x2, 0x1, 0x13)
    OP_29(0x2, 0x1, 0x14)
    OP_29(0x2, 0x1, 0x15)
    OP_29(0x2, 0x1, 0x16)
    OP_29(0x2, 0x1, 0x17)
    OP_29(0x2, 0x1, 0x18)
    OP_29(0x2, 0x1, 0x19)
    OP_29(0x2, 0x1, 0x1A)
    OP_29(0x2, 0x1, 0x1B)
    OP_29(0x2, 0x1, 0x1C)
    OP_29(0x2, 0x1, 0x1D)
    OP_29(0x2, 0x1, 0x1E)
    OP_29(0x2, 0x1, 0x1F)
    OP_29(0x3, 0x1, 0x0)
    OP_29(0x3, 0x1, 0x1)
    OP_29(0x3, 0x1, 0x2)
    OP_29(0x3, 0x1, 0x3)
    OP_29(0x3, 0x1, 0x4)
    OP_29(0x3, 0x1, 0x5)
    OP_29(0x3, 0x1, 0x6)
    OP_29(0x3, 0x1, 0x7)
    OP_29(0x3, 0x1, 0x8)
    OP_29(0x3, 0x1, 0x9)
    OP_29(0x3, 0x1, 0xA)
    OP_29(0x3, 0x1, 0xB)
    OP_29(0x3, 0x1, 0xC)
    OP_29(0x3, 0x1, 0xD)
    OP_29(0x3, 0x1, 0xE)
    OP_29(0x3, 0x1, 0xF)
    OP_29(0x3, 0x1, 0x10)
    OP_29(0x3, 0x1, 0x11)
    OP_29(0x3, 0x1, 0x12)
    OP_29(0x3, 0x1, 0x13)
    OP_29(0x3, 0x1, 0x14)
    OP_29(0x3, 0x1, 0x15)
    OP_29(0x3, 0x1, 0x16)
    OP_29(0x3, 0x1, 0x17)
    OP_29(0x3, 0x1, 0x18)
    OP_29(0x3, 0x1, 0x19)
    OP_29(0x3, 0x1, 0x1A)
    OP_29(0x3, 0x1, 0x1B)
    OP_29(0x3, 0x1, 0x1C)
    OP_29(0x3, 0x1, 0x1D)
    OP_29(0x3, 0x1, 0x1E)
    OP_29(0x3, 0x1, 0x1F)
    OP_29(0x4, 0x1, 0x0)
    OP_29(0x4, 0x1, 0x1)
    OP_29(0x4, 0x1, 0x2)
    OP_29(0x4, 0x1, 0x3)
    OP_29(0x4, 0x1, 0x4)
    OP_29(0x4, 0x1, 0x5)
    OP_29(0x4, 0x1, 0x6)
    OP_29(0x4, 0x1, 0x7)
    OP_29(0x4, 0x1, 0x8)
    OP_29(0x4, 0x1, 0x9)
    OP_29(0x4, 0x1, 0xA)
    OP_29(0x4, 0x1, 0xB)
    OP_29(0x4, 0x1, 0xC)
    OP_29(0x4, 0x1, 0xD)
    OP_29(0x4, 0x1, 0xE)
    OP_29(0x4, 0x1, 0xF)
    OP_29(0x4, 0x1, 0x10)
    OP_29(0x4, 0x1, 0x11)
    OP_29(0x4, 0x1, 0x12)
    OP_29(0x4, 0x1, 0x13)
    OP_29(0x4, 0x1, 0x14)
    OP_29(0x4, 0x1, 0x15)
    OP_29(0x4, 0x1, 0x16)
    OP_29(0x4, 0x1, 0x17)
    OP_29(0x4, 0x1, 0x18)
    OP_29(0x4, 0x1, 0x19)
    OP_29(0x4, 0x1, 0x1A)
    OP_29(0x4, 0x1, 0x1B)
    OP_29(0x4, 0x1, 0x1C)
    OP_29(0x4, 0x1, 0x1D)
    OP_29(0x4, 0x1, 0x1E)
    OP_29(0x4, 0x1, 0x1F)
    OP_29(0x35, 0x1, 0x0)
    OP_29(0x35, 0x1, 0x1)
    OP_29(0x35, 0x1, 0x2)
    OP_29(0x35, 0x1, 0x3)
    OP_29(0x35, 0x1, 0x4)
    OP_29(0x35, 0x1, 0x5)
    OP_29(0x35, 0x1, 0x6)
    OP_29(0x35, 0x1, 0x7)
    OP_29(0x35, 0x1, 0x8)
    OP_29(0x35, 0x1, 0x9)
    OP_29(0x35, 0x1, 0xA)
    OP_29(0x35, 0x1, 0xB)
    OP_29(0x35, 0x1, 0xC)
    OP_29(0x35, 0x1, 0xD)
    OP_29(0x35, 0x1, 0xE)
    OP_29(0x35, 0x1, 0xF)
    OP_29(0x35, 0x1, 0x10)
    OP_29(0x35, 0x1, 0x11)
    OP_29(0x35, 0x1, 0x12)
    OP_29(0x35, 0x1, 0x13)
    OP_29(0x35, 0x1, 0x14)
    OP_29(0x35, 0x1, 0x15)
    OP_29(0x35, 0x1, 0x16)
    OP_29(0x35, 0x1, 0x17)
    OP_29(0x35, 0x1, 0x18)
    OP_29(0x35, 0x1, 0x19)
    OP_29(0x35, 0x1, 0x1A)
    OP_29(0x35, 0x1, 0x1B)
    OP_29(0x35, 0x1, 0x1C)
    OP_29(0x35, 0x1, 0x1D)
    OP_29(0x35, 0x1, 0x1E)
    OP_29(0x35, 0x1, 0x1F)
    OP_29(0x5, 0x1, 0x0)
    OP_29(0x5, 0x1, 0x1)
    OP_29(0x5, 0x1, 0x2)
    OP_29(0x5, 0x1, 0x3)
    OP_29(0x5, 0x1, 0x4)
    OP_29(0x5, 0x1, 0x5)
    OP_29(0x5, 0x1, 0x6)
    OP_29(0x5, 0x1, 0x7)
    OP_29(0x5, 0x1, 0x8)
    OP_29(0x5, 0x1, 0x9)
    OP_29(0x5, 0x1, 0xA)
    OP_29(0x5, 0x1, 0xB)
    OP_29(0x5, 0x1, 0xC)
    OP_29(0x5, 0x1, 0xD)
    OP_29(0x5, 0x1, 0xE)
    OP_29(0x5, 0x1, 0xF)
    OP_29(0x5, 0x1, 0x10)
    OP_29(0x5, 0x1, 0x11)
    OP_29(0x5, 0x1, 0x12)
    OP_29(0x5, 0x1, 0x13)
    OP_29(0x5, 0x1, 0x14)
    OP_29(0x5, 0x1, 0x15)
    OP_29(0x5, 0x1, 0x16)
    OP_29(0x5, 0x1, 0x17)
    OP_29(0x5, 0x1, 0x18)
    OP_29(0x5, 0x1, 0x19)
    OP_29(0x5, 0x1, 0x1A)
    OP_29(0x5, 0x1, 0x1B)
    OP_29(0x5, 0x1, 0x1C)
    OP_29(0x5, 0x1, 0x1D)
    OP_29(0x5, 0x1, 0x1E)
    OP_29(0x5, 0x1, 0x1F)
    OP_29(0x6, 0x1, 0x0)
    OP_29(0x6, 0x1, 0x1)
    OP_29(0x6, 0x1, 0x2)
    OP_29(0x6, 0x1, 0x3)
    OP_29(0x6, 0x1, 0x4)
    OP_29(0x6, 0x1, 0x5)
    OP_29(0x6, 0x1, 0x6)
    OP_29(0x6, 0x1, 0x7)
    OP_29(0x6, 0x1, 0x8)
    OP_29(0x6, 0x1, 0x9)
    OP_29(0x6, 0x1, 0xA)
    OP_29(0x6, 0x1, 0xB)
    OP_29(0x6, 0x1, 0xC)
    OP_29(0x6, 0x1, 0xD)
    OP_29(0x6, 0x1, 0xE)
    OP_29(0x6, 0x1, 0xF)
    OP_29(0x6, 0x1, 0x10)
    OP_29(0x6, 0x1, 0x11)
    OP_29(0x6, 0x1, 0x12)
    OP_29(0x6, 0x1, 0x13)
    OP_29(0x6, 0x1, 0x14)
    OP_29(0x6, 0x1, 0x15)
    OP_29(0x6, 0x1, 0x16)
    OP_29(0x6, 0x1, 0x17)
    OP_29(0x6, 0x1, 0x18)
    OP_29(0x6, 0x1, 0x19)
    OP_29(0x6, 0x1, 0x1A)
    OP_29(0x6, 0x1, 0x1B)
    OP_29(0x6, 0x1, 0x1C)
    OP_29(0x6, 0x1, 0x1D)
    OP_29(0x6, 0x1, 0x1E)
    OP_29(0x6, 0x1, 0x1F)
    OP_29(0x7, 0x1, 0x0)
    OP_29(0x7, 0x1, 0x1)
    OP_29(0x7, 0x1, 0x2)
    OP_29(0x7, 0x1, 0x3)
    OP_29(0x7, 0x1, 0x4)
    OP_29(0x7, 0x1, 0x5)
    OP_29(0x7, 0x1, 0x6)
    OP_29(0x7, 0x1, 0x7)
    OP_29(0x7, 0x1, 0x8)
    OP_29(0x7, 0x1, 0x9)
    OP_29(0x7, 0x1, 0xA)
    OP_29(0x7, 0x1, 0xB)
    OP_29(0x7, 0x1, 0xC)
    OP_29(0x7, 0x1, 0xD)
    OP_29(0x7, 0x1, 0xE)
    OP_29(0x7, 0x1, 0xF)
    OP_29(0x7, 0x1, 0x10)
    OP_29(0x7, 0x1, 0x11)
    OP_29(0x7, 0x1, 0x12)
    OP_29(0x7, 0x1, 0x13)
    OP_29(0x7, 0x1, 0x14)
    OP_29(0x7, 0x1, 0x15)
    OP_29(0x7, 0x1, 0x16)
    OP_29(0x7, 0x1, 0x17)
    OP_29(0x7, 0x1, 0x18)
    OP_29(0x7, 0x1, 0x19)
    OP_29(0x7, 0x1, 0x1A)
    OP_29(0x7, 0x1, 0x1B)
    OP_29(0x7, 0x1, 0x1C)
    OP_29(0x7, 0x1, 0x1D)
    OP_29(0x7, 0x1, 0x1E)
    OP_29(0x7, 0x1, 0x1F)
    OP_29(0x8, 0x1, 0x0)
    OP_29(0x8, 0x1, 0x1)
    OP_29(0x8, 0x1, 0x2)
    OP_29(0x8, 0x1, 0x3)
    OP_29(0x8, 0x1, 0x4)
    OP_29(0x8, 0x1, 0x5)
    OP_29(0x8, 0x1, 0x6)
    OP_29(0x8, 0x1, 0x7)
    OP_29(0x8, 0x1, 0x8)
    OP_29(0x8, 0x1, 0x9)
    OP_29(0x8, 0x1, 0xA)
    OP_29(0x8, 0x1, 0xB)
    OP_29(0x8, 0x1, 0xC)
    OP_29(0x8, 0x1, 0xD)
    OP_29(0x8, 0x1, 0xE)
    OP_29(0x8, 0x1, 0xF)
    OP_29(0x8, 0x1, 0x10)
    OP_29(0x8, 0x1, 0x11)
    OP_29(0x8, 0x1, 0x12)
    OP_29(0x8, 0x1, 0x13)
    OP_29(0x8, 0x1, 0x14)
    OP_29(0x8, 0x1, 0x15)
    OP_29(0x8, 0x1, 0x16)
    OP_29(0x8, 0x1, 0x17)
    OP_29(0x8, 0x1, 0x18)
    OP_29(0x8, 0x1, 0x19)
    OP_29(0x8, 0x1, 0x1A)
    OP_29(0x8, 0x1, 0x1B)
    OP_29(0x8, 0x1, 0x1C)
    OP_29(0x8, 0x1, 0x1D)
    OP_29(0x8, 0x1, 0x1E)
    OP_29(0x8, 0x1, 0x1F)
    OP_29(0x9, 0x1, 0x0)
    OP_29(0x9, 0x1, 0x1)
    OP_29(0x9, 0x1, 0x2)
    OP_29(0x9, 0x1, 0x3)
    OP_29(0x9, 0x1, 0x4)
    OP_29(0x9, 0x1, 0x5)
    OP_29(0x9, 0x1, 0x6)
    OP_29(0x9, 0x1, 0x7)
    OP_29(0x9, 0x1, 0x8)
    OP_29(0x9, 0x1, 0x9)
    OP_29(0x9, 0x1, 0xA)
    OP_29(0x9, 0x1, 0xB)
    OP_29(0x9, 0x1, 0xC)
    OP_29(0x9, 0x1, 0xD)
    OP_29(0x9, 0x1, 0xE)
    OP_29(0x9, 0x1, 0xF)
    OP_29(0x9, 0x1, 0x10)
    OP_29(0x9, 0x1, 0x11)
    OP_29(0x9, 0x1, 0x12)
    OP_29(0x9, 0x1, 0x13)
    OP_29(0x9, 0x1, 0x14)
    OP_29(0x9, 0x1, 0x15)
    OP_29(0x9, 0x1, 0x16)
    OP_29(0x9, 0x1, 0x17)
    OP_29(0x9, 0x1, 0x18)
    OP_29(0x9, 0x1, 0x19)
    OP_29(0x9, 0x1, 0x1A)
    OP_29(0x9, 0x1, 0x1B)
    OP_29(0x9, 0x1, 0x1C)
    OP_29(0x9, 0x1, 0x1D)
    OP_29(0x9, 0x1, 0x1E)
    OP_29(0x9, 0x1, 0x1F)
    OP_29(0xA, 0x1, 0x0)
    OP_29(0xA, 0x1, 0x1)
    OP_29(0xA, 0x1, 0x2)
    OP_29(0xA, 0x1, 0x3)
    OP_29(0xA, 0x1, 0x4)
    OP_29(0xA, 0x1, 0x5)
    OP_29(0xA, 0x1, 0x6)
    OP_29(0xA, 0x1, 0x7)
    OP_29(0xA, 0x1, 0x8)
    OP_29(0xA, 0x1, 0x9)
    OP_29(0xA, 0x1, 0xA)
    OP_29(0xA, 0x1, 0xB)
    OP_29(0xA, 0x1, 0xC)
    OP_29(0xA, 0x1, 0xD)
    OP_29(0xA, 0x1, 0xE)
    OP_29(0xA, 0x1, 0xF)
    OP_29(0xA, 0x1, 0x10)
    OP_29(0xA, 0x1, 0x11)
    OP_29(0xA, 0x1, 0x12)
    OP_29(0xA, 0x1, 0x13)
    OP_29(0xA, 0x1, 0x14)
    OP_29(0xA, 0x1, 0x15)
    OP_29(0xA, 0x1, 0x16)
    OP_29(0xA, 0x1, 0x17)
    OP_29(0xA, 0x1, 0x18)
    OP_29(0xA, 0x1, 0x19)
    OP_29(0xA, 0x1, 0x1A)
    OP_29(0xA, 0x1, 0x1B)
    OP_29(0xA, 0x1, 0x1C)
    OP_29(0xA, 0x1, 0x1D)
    OP_29(0xA, 0x1, 0x1E)
    OP_29(0xA, 0x1, 0x1F)
    OP_29(0xB, 0x1, 0x0)
    OP_29(0xB, 0x1, 0x1)
    OP_29(0xB, 0x1, 0x2)
    OP_29(0xB, 0x1, 0x3)
    OP_29(0xB, 0x1, 0x4)
    OP_29(0xB, 0x1, 0x5)
    OP_29(0xB, 0x1, 0x6)
    OP_29(0xB, 0x1, 0x7)
    OP_29(0xB, 0x1, 0x8)
    OP_29(0xB, 0x1, 0x9)
    OP_29(0xB, 0x1, 0xA)
    OP_29(0xB, 0x1, 0xB)
    OP_29(0xB, 0x1, 0xC)
    OP_29(0xB, 0x1, 0xD)
    OP_29(0xB, 0x1, 0xE)
    OP_29(0xB, 0x1, 0xF)
    OP_29(0xB, 0x1, 0x10)
    OP_29(0xB, 0x1, 0x11)
    OP_29(0xB, 0x1, 0x12)
    OP_29(0xB, 0x1, 0x13)
    OP_29(0xB, 0x1, 0x14)
    OP_29(0xB, 0x1, 0x15)
    OP_29(0xB, 0x1, 0x16)
    OP_29(0xB, 0x1, 0x17)
    OP_29(0xB, 0x1, 0x18)
    OP_29(0xB, 0x1, 0x19)
    OP_29(0xB, 0x1, 0x1A)
    OP_29(0xB, 0x1, 0x1B)
    OP_29(0xB, 0x1, 0x1C)
    OP_29(0xB, 0x1, 0x1D)
    OP_29(0xB, 0x1, 0x1E)
    OP_29(0xB, 0x1, 0x1F)
    OP_29(0xC, 0x1, 0x0)
    OP_29(0xC, 0x1, 0x1)
    OP_29(0xC, 0x1, 0x2)
    OP_29(0xC, 0x1, 0x3)
    OP_29(0xC, 0x1, 0x4)
    OP_29(0xC, 0x1, 0x5)
    OP_29(0xC, 0x1, 0x6)
    OP_29(0xC, 0x1, 0x7)
    OP_29(0xC, 0x1, 0x8)
    OP_29(0xC, 0x1, 0x9)
    OP_29(0xC, 0x1, 0xA)
    OP_29(0xC, 0x1, 0xB)
    OP_29(0xC, 0x1, 0xC)
    OP_29(0xC, 0x1, 0xD)
    OP_29(0xC, 0x1, 0xE)
    OP_29(0xC, 0x1, 0xF)
    OP_29(0xC, 0x1, 0x10)
    OP_29(0xC, 0x1, 0x11)
    OP_29(0xC, 0x1, 0x12)
    OP_29(0xC, 0x1, 0x13)
    OP_29(0xC, 0x1, 0x14)
    OP_29(0xC, 0x1, 0x15)
    OP_29(0xC, 0x1, 0x16)
    OP_29(0xC, 0x1, 0x17)
    OP_29(0xC, 0x1, 0x18)
    OP_29(0xC, 0x1, 0x19)
    OP_29(0xC, 0x1, 0x1A)
    OP_29(0xC, 0x1, 0x1B)
    OP_29(0xC, 0x1, 0x1C)
    OP_29(0xC, 0x1, 0x1D)
    OP_29(0xC, 0x1, 0x1E)
    OP_29(0xC, 0x1, 0x1F)
    OP_29(0xD, 0x1, 0x0)
    OP_29(0xD, 0x1, 0x1)
    OP_29(0xD, 0x1, 0x2)
    OP_29(0xD, 0x1, 0x3)
    OP_29(0xD, 0x1, 0x4)
    OP_29(0xD, 0x1, 0x5)
    OP_29(0xD, 0x1, 0x6)
    OP_29(0xD, 0x1, 0x7)
    OP_29(0xD, 0x1, 0x8)
    OP_29(0xD, 0x1, 0x9)
    OP_29(0xD, 0x1, 0xA)
    OP_29(0xD, 0x1, 0xB)
    OP_29(0xD, 0x1, 0xC)
    OP_29(0xD, 0x1, 0xD)
    OP_29(0xD, 0x1, 0xE)
    OP_29(0xD, 0x1, 0xF)
    OP_29(0xD, 0x1, 0x10)
    OP_29(0xD, 0x1, 0x11)
    OP_29(0xD, 0x1, 0x12)
    OP_29(0xD, 0x1, 0x13)
    OP_29(0xD, 0x1, 0x14)
    OP_29(0xD, 0x1, 0x15)
    OP_29(0xD, 0x1, 0x16)
    OP_29(0xD, 0x1, 0x17)
    OP_29(0xD, 0x1, 0x18)
    OP_29(0xD, 0x1, 0x19)
    OP_29(0xD, 0x1, 0x1A)
    OP_29(0xD, 0x1, 0x1B)
    OP_29(0xD, 0x1, 0x1C)
    OP_29(0xD, 0x1, 0x1D)
    OP_29(0xD, 0x1, 0x1E)
    OP_29(0xD, 0x1, 0x1F)
    OP_29(0xE, 0x1, 0x0)
    OP_29(0xE, 0x1, 0x1)
    OP_29(0xE, 0x1, 0x2)
    OP_29(0xE, 0x1, 0x3)
    OP_29(0xE, 0x1, 0x4)
    OP_29(0xE, 0x1, 0x5)
    OP_29(0xE, 0x1, 0x6)
    OP_29(0xE, 0x1, 0x7)
    OP_29(0xE, 0x1, 0x8)
    OP_29(0xE, 0x1, 0x9)
    OP_29(0xE, 0x1, 0xA)
    OP_29(0xE, 0x1, 0xB)
    OP_29(0xE, 0x1, 0xC)
    OP_29(0xE, 0x1, 0xD)
    OP_29(0xE, 0x1, 0xE)
    OP_29(0xE, 0x1, 0xF)
    OP_29(0xE, 0x1, 0x10)
    OP_29(0xE, 0x1, 0x11)
    OP_29(0xE, 0x1, 0x12)
    OP_29(0xE, 0x1, 0x13)
    OP_29(0xE, 0x1, 0x14)
    OP_29(0xE, 0x1, 0x15)
    OP_29(0xE, 0x1, 0x16)
    OP_29(0xE, 0x1, 0x17)
    OP_29(0xE, 0x1, 0x18)
    OP_29(0xE, 0x1, 0x19)
    OP_29(0xE, 0x1, 0x1A)
    OP_29(0xE, 0x1, 0x1B)
    OP_29(0xE, 0x1, 0x1C)
    OP_29(0xE, 0x1, 0x1D)
    OP_29(0xE, 0x1, 0x1E)
    OP_29(0xE, 0x1, 0x1F)
    OP_29(0xF, 0x1, 0x0)
    OP_29(0xF, 0x1, 0x1)
    OP_29(0xF, 0x1, 0x2)
    OP_29(0xF, 0x1, 0x3)
    OP_29(0xF, 0x1, 0x4)
    OP_29(0xF, 0x1, 0x5)
    OP_29(0xF, 0x1, 0x6)
    OP_29(0xF, 0x1, 0x7)
    OP_29(0xF, 0x1, 0x8)
    OP_29(0xF, 0x1, 0x9)
    OP_29(0xF, 0x1, 0xA)
    OP_29(0xF, 0x1, 0xB)
    OP_29(0xF, 0x1, 0xC)
    OP_29(0xF, 0x1, 0xD)
    OP_29(0xF, 0x1, 0xE)
    OP_29(0xF, 0x1, 0xF)
    OP_29(0xF, 0x1, 0x10)
    OP_29(0xF, 0x1, 0x11)
    OP_29(0xF, 0x1, 0x12)
    OP_29(0xF, 0x1, 0x13)
    OP_29(0xF, 0x1, 0x14)
    OP_29(0xF, 0x1, 0x15)
    OP_29(0xF, 0x1, 0x16)
    OP_29(0xF, 0x1, 0x17)
    OP_29(0xF, 0x1, 0x18)
    OP_29(0xF, 0x1, 0x19)
    OP_29(0xF, 0x1, 0x1A)
    OP_29(0xF, 0x1, 0x1B)
    OP_29(0xF, 0x1, 0x1C)
    OP_29(0xF, 0x1, 0x1D)
    OP_29(0xF, 0x1, 0x1E)
    OP_29(0xF, 0x1, 0x1F)
    OP_29(0x10, 0x1, 0x0)
    OP_29(0x10, 0x1, 0x1)
    OP_29(0x10, 0x1, 0x2)
    OP_29(0x10, 0x1, 0x3)
    OP_29(0x10, 0x1, 0x4)
    OP_29(0x10, 0x1, 0x5)
    OP_29(0x10, 0x1, 0x6)
    OP_29(0x10, 0x1, 0x7)
    OP_29(0x10, 0x1, 0x8)
    OP_29(0x10, 0x1, 0x9)
    OP_29(0x10, 0x1, 0xA)
    OP_29(0x10, 0x1, 0xB)
    OP_29(0x10, 0x1, 0xC)
    OP_29(0x10, 0x1, 0xD)
    OP_29(0x10, 0x1, 0xE)
    OP_29(0x10, 0x1, 0xF)
    OP_29(0x10, 0x1, 0x10)
    OP_29(0x10, 0x1, 0x11)
    OP_29(0x10, 0x1, 0x12)
    OP_29(0x10, 0x1, 0x13)
    OP_29(0x10, 0x1, 0x14)
    OP_29(0x10, 0x1, 0x15)
    OP_29(0x10, 0x1, 0x16)
    OP_29(0x10, 0x1, 0x17)
    OP_29(0x10, 0x1, 0x18)
    OP_29(0x10, 0x1, 0x19)
    OP_29(0x10, 0x1, 0x1A)
    OP_29(0x10, 0x1, 0x1B)
    OP_29(0x10, 0x1, 0x1C)
    OP_29(0x10, 0x1, 0x1D)
    OP_29(0x10, 0x1, 0x1E)
    OP_29(0x10, 0x1, 0x1F)
    OP_29(0x11, 0x1, 0x0)
    OP_29(0x11, 0x1, 0x1)
    OP_29(0x11, 0x1, 0x2)
    OP_29(0x11, 0x1, 0x3)
    OP_29(0x11, 0x1, 0x4)
    OP_29(0x11, 0x1, 0x5)
    OP_29(0x11, 0x1, 0x6)
    OP_29(0x11, 0x1, 0x7)
    OP_29(0x11, 0x1, 0x8)
    OP_29(0x11, 0x1, 0x9)
    OP_29(0x11, 0x1, 0xA)
    OP_29(0x11, 0x1, 0xB)
    OP_29(0x11, 0x1, 0xC)
    OP_29(0x11, 0x1, 0xD)
    OP_29(0x11, 0x1, 0xE)
    OP_29(0x11, 0x1, 0xF)
    OP_29(0x11, 0x1, 0x10)
    OP_29(0x11, 0x1, 0x11)
    OP_29(0x11, 0x1, 0x12)
    OP_29(0x11, 0x1, 0x13)
    OP_29(0x11, 0x1, 0x14)
    OP_29(0x11, 0x1, 0x15)
    OP_29(0x11, 0x1, 0x16)
    OP_29(0x11, 0x1, 0x17)
    OP_29(0x11, 0x1, 0x18)
    OP_29(0x11, 0x1, 0x19)
    OP_29(0x11, 0x1, 0x1A)
    OP_29(0x11, 0x1, 0x1B)
    OP_29(0x11, 0x1, 0x1C)
    OP_29(0x11, 0x1, 0x1D)
    OP_29(0x11, 0x1, 0x1E)
    OP_29(0x11, 0x1, 0x1F)
    OP_29(0x12, 0x1, 0x0)
    OP_29(0x12, 0x1, 0x1)
    OP_29(0x12, 0x1, 0x2)
    OP_29(0x12, 0x1, 0x3)
    OP_29(0x12, 0x1, 0x4)
    OP_29(0x12, 0x1, 0x5)
    OP_29(0x12, 0x1, 0x6)
    OP_29(0x12, 0x1, 0x7)
    OP_29(0x12, 0x1, 0x8)
    OP_29(0x12, 0x1, 0x9)
    OP_29(0x12, 0x1, 0xA)
    OP_29(0x12, 0x1, 0xB)
    OP_29(0x12, 0x1, 0xC)
    OP_29(0x12, 0x1, 0xD)
    OP_29(0x12, 0x1, 0xE)
    OP_29(0x12, 0x1, 0xF)
    OP_29(0x12, 0x1, 0x10)
    OP_29(0x12, 0x1, 0x11)
    OP_29(0x12, 0x1, 0x12)
    OP_29(0x12, 0x1, 0x13)
    OP_29(0x12, 0x1, 0x14)
    OP_29(0x12, 0x1, 0x15)
    OP_29(0x12, 0x1, 0x16)
    OP_29(0x12, 0x1, 0x17)
    OP_29(0x12, 0x1, 0x18)
    OP_29(0x12, 0x1, 0x19)
    OP_29(0x12, 0x1, 0x1A)
    OP_29(0x12, 0x1, 0x1B)
    OP_29(0x12, 0x1, 0x1C)
    OP_29(0x12, 0x1, 0x1D)
    OP_29(0x12, 0x1, 0x1E)
    OP_29(0x12, 0x1, 0x1F)
    OP_29(0x13, 0x1, 0x0)
    OP_29(0x13, 0x1, 0x1)
    OP_29(0x13, 0x1, 0x2)
    OP_29(0x13, 0x1, 0x3)
    OP_29(0x13, 0x1, 0x4)
    OP_29(0x13, 0x1, 0x5)
    OP_29(0x13, 0x1, 0x6)
    OP_29(0x13, 0x1, 0x7)
    OP_29(0x13, 0x1, 0x8)
    OP_29(0x13, 0x1, 0x9)
    OP_29(0x13, 0x1, 0xA)
    OP_29(0x13, 0x1, 0xB)
    OP_29(0x13, 0x1, 0xC)
    OP_29(0x13, 0x1, 0xD)
    OP_29(0x13, 0x1, 0xE)
    OP_29(0x13, 0x1, 0xF)
    OP_29(0x13, 0x1, 0x10)
    OP_29(0x13, 0x1, 0x11)
    OP_29(0x13, 0x1, 0x12)
    OP_29(0x13, 0x1, 0x13)
    OP_29(0x13, 0x1, 0x14)
    OP_29(0x13, 0x1, 0x15)
    OP_29(0x13, 0x1, 0x16)
    OP_29(0x13, 0x1, 0x17)
    OP_29(0x13, 0x1, 0x18)
    OP_29(0x13, 0x1, 0x19)
    OP_29(0x13, 0x1, 0x1A)
    OP_29(0x13, 0x1, 0x1B)
    OP_29(0x13, 0x1, 0x1C)
    OP_29(0x13, 0x1, 0x1D)
    OP_29(0x13, 0x1, 0x1E)
    OP_29(0x13, 0x1, 0x1F)
    OP_29(0x14, 0x1, 0x0)
    OP_29(0x14, 0x1, 0x1)
    OP_29(0x14, 0x1, 0x2)
    OP_29(0x14, 0x1, 0x3)
    OP_29(0x14, 0x1, 0x4)
    OP_29(0x14, 0x1, 0x5)
    OP_29(0x14, 0x1, 0x6)
    OP_29(0x14, 0x1, 0x7)
    OP_29(0x14, 0x1, 0x8)
    OP_29(0x14, 0x1, 0x9)
    OP_29(0x14, 0x1, 0xA)
    OP_29(0x14, 0x1, 0xB)
    OP_29(0x14, 0x1, 0xC)
    OP_29(0x14, 0x1, 0xD)
    OP_29(0x14, 0x1, 0xE)
    OP_29(0x14, 0x1, 0xF)
    OP_29(0x14, 0x1, 0x10)
    OP_29(0x14, 0x1, 0x11)
    OP_29(0x14, 0x1, 0x12)
    OP_29(0x14, 0x1, 0x13)
    OP_29(0x14, 0x1, 0x14)
    OP_29(0x14, 0x1, 0x15)
    OP_29(0x14, 0x1, 0x16)
    OP_29(0x14, 0x1, 0x17)
    OP_29(0x14, 0x1, 0x18)
    OP_29(0x14, 0x1, 0x19)
    OP_29(0x14, 0x1, 0x1A)
    OP_29(0x14, 0x1, 0x1B)
    OP_29(0x14, 0x1, 0x1C)
    OP_29(0x14, 0x1, 0x1D)
    OP_29(0x14, 0x1, 0x1E)
    OP_29(0x14, 0x1, 0x1F)
    OP_29(0x15, 0x1, 0x0)
    OP_29(0x15, 0x1, 0x1)
    OP_29(0x15, 0x1, 0x2)
    OP_29(0x15, 0x1, 0x3)
    OP_29(0x15, 0x1, 0x4)
    OP_29(0x15, 0x1, 0x5)
    OP_29(0x15, 0x1, 0x6)
    OP_29(0x15, 0x1, 0x7)
    OP_29(0x15, 0x1, 0x8)
    OP_29(0x15, 0x1, 0x9)
    OP_29(0x15, 0x1, 0xA)
    OP_29(0x15, 0x1, 0xB)
    OP_29(0x15, 0x1, 0xC)
    OP_29(0x15, 0x1, 0xD)
    OP_29(0x15, 0x1, 0xE)
    OP_29(0x15, 0x1, 0xF)
    OP_29(0x15, 0x1, 0x10)
    OP_29(0x15, 0x1, 0x11)
    OP_29(0x15, 0x1, 0x12)
    OP_29(0x15, 0x1, 0x13)
    OP_29(0x15, 0x1, 0x14)
    OP_29(0x15, 0x1, 0x15)
    OP_29(0x15, 0x1, 0x16)
    OP_29(0x15, 0x1, 0x17)
    OP_29(0x15, 0x1, 0x18)
    OP_29(0x15, 0x1, 0x19)
    OP_29(0x15, 0x1, 0x1A)
    OP_29(0x15, 0x1, 0x1B)
    OP_29(0x15, 0x1, 0x1C)
    OP_29(0x15, 0x1, 0x1D)
    OP_29(0x15, 0x1, 0x1E)
    OP_29(0x15, 0x1, 0x1F)
    OP_29(0x16, 0x1, 0x0)
    OP_29(0x16, 0x1, 0x1)
    OP_29(0x16, 0x1, 0x2)
    OP_29(0x16, 0x1, 0x3)
    OP_29(0x16, 0x1, 0x4)
    OP_29(0x16, 0x1, 0x5)
    OP_29(0x16, 0x1, 0x6)
    OP_29(0x16, 0x1, 0x7)
    OP_29(0x16, 0x1, 0x8)
    OP_29(0x16, 0x1, 0x9)
    OP_29(0x16, 0x1, 0xA)
    OP_29(0x16, 0x1, 0xB)
    OP_29(0x16, 0x1, 0xC)
    OP_29(0x16, 0x1, 0xD)
    OP_29(0x16, 0x1, 0xE)
    OP_29(0x16, 0x1, 0xF)
    OP_29(0x16, 0x1, 0x10)
    OP_29(0x16, 0x1, 0x11)
    OP_29(0x16, 0x1, 0x12)
    OP_29(0x16, 0x1, 0x13)
    OP_29(0x16, 0x1, 0x14)
    OP_29(0x16, 0x1, 0x15)
    OP_29(0x16, 0x1, 0x16)
    OP_29(0x16, 0x1, 0x17)
    OP_29(0x16, 0x1, 0x18)
    OP_29(0x16, 0x1, 0x19)
    OP_29(0x16, 0x1, 0x1A)
    OP_29(0x16, 0x1, 0x1B)
    OP_29(0x16, 0x1, 0x1C)
    OP_29(0x16, 0x1, 0x1D)
    OP_29(0x16, 0x1, 0x1E)
    OP_29(0x16, 0x1, 0x1F)
    OP_29(0x17, 0x1, 0x0)
    OP_29(0x17, 0x1, 0x1)
    OP_29(0x17, 0x1, 0x2)
    OP_29(0x17, 0x1, 0x3)
    OP_29(0x17, 0x1, 0x4)
    OP_29(0x17, 0x1, 0x5)
    OP_29(0x17, 0x1, 0x6)
    OP_29(0x17, 0x1, 0x7)
    OP_29(0x17, 0x1, 0x8)
    OP_29(0x17, 0x1, 0x9)
    OP_29(0x17, 0x1, 0xA)
    OP_29(0x17, 0x1, 0xB)
    OP_29(0x17, 0x1, 0xC)
    OP_29(0x17, 0x1, 0xD)
    OP_29(0x17, 0x1, 0xE)
    OP_29(0x17, 0x1, 0xF)
    OP_29(0x17, 0x1, 0x10)
    OP_29(0x17, 0x1, 0x11)
    OP_29(0x17, 0x1, 0x12)
    OP_29(0x17, 0x1, 0x13)
    OP_29(0x17, 0x1, 0x14)
    OP_29(0x17, 0x1, 0x15)
    OP_29(0x17, 0x1, 0x16)
    OP_29(0x17, 0x1, 0x17)
    OP_29(0x17, 0x1, 0x18)
    OP_29(0x17, 0x1, 0x19)
    OP_29(0x17, 0x1, 0x1A)
    OP_29(0x17, 0x1, 0x1B)
    OP_29(0x17, 0x1, 0x1C)
    OP_29(0x17, 0x1, 0x1D)
    OP_29(0x17, 0x1, 0x1E)
    OP_29(0x17, 0x1, 0x1F)
    OP_29(0x18, 0x1, 0x0)
    OP_29(0x18, 0x1, 0x1)
    OP_29(0x18, 0x1, 0x2)
    OP_29(0x18, 0x1, 0x3)
    OP_29(0x18, 0x1, 0x4)
    OP_29(0x18, 0x1, 0x5)
    OP_29(0x18, 0x1, 0x6)
    OP_29(0x18, 0x1, 0x7)
    OP_29(0x18, 0x1, 0x8)
    OP_29(0x18, 0x1, 0x9)
    OP_29(0x18, 0x1, 0xA)
    OP_29(0x18, 0x1, 0xB)
    OP_29(0x18, 0x1, 0xC)
    OP_29(0x18, 0x1, 0xD)
    OP_29(0x18, 0x1, 0xE)
    OP_29(0x18, 0x1, 0xF)
    OP_29(0x18, 0x1, 0x10)
    OP_29(0x18, 0x1, 0x11)
    OP_29(0x18, 0x1, 0x12)
    OP_29(0x18, 0x1, 0x13)
    OP_29(0x18, 0x1, 0x14)
    OP_29(0x18, 0x1, 0x15)
    OP_29(0x18, 0x1, 0x16)
    OP_29(0x18, 0x1, 0x17)
    OP_29(0x18, 0x1, 0x18)
    OP_29(0x18, 0x1, 0x19)
    OP_29(0x18, 0x1, 0x1A)
    OP_29(0x18, 0x1, 0x1B)
    OP_29(0x18, 0x1, 0x1C)
    OP_29(0x18, 0x1, 0x1D)
    OP_29(0x18, 0x1, 0x1E)
    OP_29(0x18, 0x1, 0x1F)
    OP_29(0x19, 0x1, 0x0)
    OP_29(0x19, 0x1, 0x1)
    OP_29(0x19, 0x1, 0x2)
    OP_29(0x19, 0x1, 0x3)
    OP_29(0x19, 0x1, 0x4)
    OP_29(0x19, 0x1, 0x5)
    OP_29(0x19, 0x1, 0x6)
    OP_29(0x19, 0x1, 0x7)
    OP_29(0x19, 0x1, 0x8)
    OP_29(0x19, 0x1, 0x9)
    OP_29(0x19, 0x1, 0xA)
    OP_29(0x19, 0x1, 0xB)
    OP_29(0x19, 0x1, 0xC)
    OP_29(0x19, 0x1, 0xD)
    OP_29(0x19, 0x1, 0xE)
    OP_29(0x19, 0x1, 0xF)
    OP_29(0x19, 0x1, 0x10)
    OP_29(0x19, 0x1, 0x11)
    OP_29(0x19, 0x1, 0x12)
    OP_29(0x19, 0x1, 0x13)
    OP_29(0x19, 0x1, 0x14)
    OP_29(0x19, 0x1, 0x15)
    OP_29(0x19, 0x1, 0x16)
    OP_29(0x19, 0x1, 0x17)
    OP_29(0x19, 0x1, 0x18)
    OP_29(0x19, 0x1, 0x19)
    OP_29(0x19, 0x1, 0x1A)
    OP_29(0x19, 0x1, 0x1B)
    OP_29(0x19, 0x1, 0x1C)
    OP_29(0x19, 0x1, 0x1D)
    OP_29(0x19, 0x1, 0x1E)
    OP_29(0x19, 0x1, 0x1F)
    OP_29(0x1A, 0x1, 0x0)
    OP_29(0x1A, 0x1, 0x1)
    OP_29(0x1A, 0x1, 0x2)
    OP_29(0x1A, 0x1, 0x3)
    OP_29(0x1A, 0x1, 0x4)
    OP_29(0x1A, 0x1, 0x5)
    OP_29(0x1A, 0x1, 0x6)
    OP_29(0x1A, 0x1, 0x7)
    OP_29(0x1A, 0x1, 0x8)
    OP_29(0x1A, 0x1, 0x9)
    OP_29(0x1A, 0x1, 0xA)
    OP_29(0x1A, 0x1, 0xB)
    OP_29(0x1A, 0x1, 0xC)
    OP_29(0x1A, 0x1, 0xD)
    OP_29(0x1A, 0x1, 0xE)
    OP_29(0x1A, 0x1, 0xF)
    OP_29(0x1A, 0x1, 0x10)
    OP_29(0x1A, 0x1, 0x11)
    OP_29(0x1A, 0x1, 0x12)
    OP_29(0x1A, 0x1, 0x13)
    OP_29(0x1A, 0x1, 0x14)
    OP_29(0x1A, 0x1, 0x15)
    OP_29(0x1A, 0x1, 0x16)
    OP_29(0x1A, 0x1, 0x17)
    OP_29(0x1A, 0x1, 0x18)
    OP_29(0x1A, 0x1, 0x19)
    OP_29(0x1A, 0x1, 0x1A)
    OP_29(0x1A, 0x1, 0x1B)
    OP_29(0x1A, 0x1, 0x1C)
    OP_29(0x1A, 0x1, 0x1D)
    OP_29(0x1A, 0x1, 0x1E)
    OP_29(0x1A, 0x1, 0x1F)
    OP_29(0x1B, 0x1, 0x0)
    OP_29(0x1B, 0x1, 0x1)
    OP_29(0x1B, 0x1, 0x2)
    OP_29(0x1B, 0x1, 0x3)
    OP_29(0x1B, 0x1, 0x4)
    OP_29(0x1B, 0x1, 0x5)
    OP_29(0x1B, 0x1, 0x6)
    OP_29(0x1B, 0x1, 0x7)
    OP_29(0x1B, 0x1, 0x8)
    OP_29(0x1B, 0x1, 0x9)
    OP_29(0x1B, 0x1, 0xA)
    OP_29(0x1B, 0x1, 0xB)
    OP_29(0x1B, 0x1, 0xC)
    OP_29(0x1B, 0x1, 0xD)
    OP_29(0x1B, 0x1, 0xE)
    OP_29(0x1B, 0x1, 0xF)
    OP_29(0x1B, 0x1, 0x10)
    OP_29(0x1B, 0x1, 0x11)
    OP_29(0x1B, 0x1, 0x12)
    OP_29(0x1B, 0x1, 0x13)
    OP_29(0x1B, 0x1, 0x14)
    OP_29(0x1B, 0x1, 0x15)
    OP_29(0x1B, 0x1, 0x16)
    OP_29(0x1B, 0x1, 0x17)
    OP_29(0x1B, 0x1, 0x18)
    OP_29(0x1B, 0x1, 0x19)
    OP_29(0x1B, 0x1, 0x1A)
    OP_29(0x1B, 0x1, 0x1B)
    OP_29(0x1B, 0x1, 0x1C)
    OP_29(0x1B, 0x1, 0x1D)
    OP_29(0x1B, 0x1, 0x1E)
    OP_29(0x1B, 0x1, 0x1F)
    OP_29(0x1C, 0x1, 0x0)
    OP_29(0x1C, 0x1, 0x1)
    OP_29(0x1C, 0x1, 0x2)
    OP_29(0x1C, 0x1, 0x3)
    OP_29(0x1C, 0x1, 0x4)
    OP_29(0x1C, 0x1, 0x5)
    OP_29(0x1C, 0x1, 0x6)
    OP_29(0x1C, 0x1, 0x7)
    OP_29(0x1C, 0x1, 0x8)
    OP_29(0x1C, 0x1, 0x9)
    OP_29(0x1C, 0x1, 0xA)
    OP_29(0x1C, 0x1, 0xB)
    OP_29(0x1C, 0x1, 0xC)
    OP_29(0x1C, 0x1, 0xD)
    OP_29(0x1C, 0x1, 0xE)
    OP_29(0x1C, 0x1, 0xF)
    OP_29(0x1C, 0x1, 0x10)
    OP_29(0x1C, 0x1, 0x11)
    OP_29(0x1C, 0x1, 0x12)
    OP_29(0x1C, 0x1, 0x13)
    OP_29(0x1C, 0x1, 0x14)
    OP_29(0x1C, 0x1, 0x15)
    OP_29(0x1C, 0x1, 0x16)
    OP_29(0x1C, 0x1, 0x17)
    OP_29(0x1C, 0x1, 0x18)
    OP_29(0x1C, 0x1, 0x19)
    OP_29(0x1C, 0x1, 0x1A)
    OP_29(0x1C, 0x1, 0x1B)
    OP_29(0x1C, 0x1, 0x1C)
    OP_29(0x1C, 0x1, 0x1D)
    OP_29(0x1C, 0x1, 0x1E)
    OP_29(0x1C, 0x1, 0x1F)
    OP_29(0x1D, 0x1, 0x0)
    OP_29(0x1D, 0x1, 0x1)
    OP_29(0x1D, 0x1, 0x2)
    OP_29(0x1D, 0x1, 0x3)
    OP_29(0x1D, 0x1, 0x4)
    OP_29(0x1D, 0x1, 0x5)
    OP_29(0x1D, 0x1, 0x6)
    OP_29(0x1D, 0x1, 0x7)
    OP_29(0x1D, 0x1, 0x8)
    OP_29(0x1D, 0x1, 0x9)
    OP_29(0x1D, 0x1, 0xA)
    OP_29(0x1D, 0x1, 0xB)
    OP_29(0x1D, 0x1, 0xC)
    OP_29(0x1D, 0x1, 0xD)
    OP_29(0x1D, 0x1, 0xE)
    OP_29(0x1D, 0x1, 0xF)
    OP_29(0x1D, 0x1, 0x10)
    OP_29(0x1D, 0x1, 0x11)
    OP_29(0x1D, 0x1, 0x12)
    OP_29(0x1D, 0x1, 0x13)
    OP_29(0x1D, 0x1, 0x14)
    OP_29(0x1D, 0x1, 0x15)
    OP_29(0x1D, 0x1, 0x16)
    OP_29(0x1D, 0x1, 0x17)
    OP_29(0x1D, 0x1, 0x18)
    OP_29(0x1D, 0x1, 0x19)
    OP_29(0x1D, 0x1, 0x1A)
    OP_29(0x1D, 0x1, 0x1B)
    OP_29(0x1D, 0x1, 0x1C)
    OP_29(0x1D, 0x1, 0x1D)
    OP_29(0x1D, 0x1, 0x1E)
    OP_29(0x1D, 0x1, 0x1F)
    OP_29(0x1E, 0x1, 0x0)
    OP_29(0x1E, 0x1, 0x1)
    OP_29(0x1E, 0x1, 0x2)
    OP_29(0x1E, 0x1, 0x3)
    OP_29(0x1E, 0x1, 0x4)
    OP_29(0x1E, 0x1, 0x5)
    OP_29(0x1E, 0x1, 0x6)
    OP_29(0x1E, 0x1, 0x7)
    OP_29(0x1E, 0x1, 0x8)
    OP_29(0x1E, 0x1, 0x9)
    OP_29(0x1E, 0x1, 0xA)
    OP_29(0x1E, 0x1, 0xB)
    OP_29(0x1E, 0x1, 0xC)
    OP_29(0x1E, 0x1, 0xD)
    OP_29(0x1E, 0x1, 0xE)
    OP_29(0x1E, 0x1, 0xF)
    OP_29(0x1E, 0x1, 0x10)
    OP_29(0x1E, 0x1, 0x11)
    OP_29(0x1E, 0x1, 0x12)
    OP_29(0x1E, 0x1, 0x13)
    OP_29(0x1E, 0x1, 0x14)
    OP_29(0x1E, 0x1, 0x15)
    OP_29(0x1E, 0x1, 0x16)
    OP_29(0x1E, 0x1, 0x17)
    OP_29(0x1E, 0x1, 0x18)
    OP_29(0x1E, 0x1, 0x19)
    OP_29(0x1E, 0x1, 0x1A)
    OP_29(0x1E, 0x1, 0x1B)
    OP_29(0x1E, 0x1, 0x1C)
    OP_29(0x1E, 0x1, 0x1D)
    OP_29(0x1E, 0x1, 0x1E)
    OP_29(0x1E, 0x1, 0x1F)
    OP_29(0x1F, 0x1, 0x0)
    OP_29(0x1F, 0x1, 0x1)
    OP_29(0x1F, 0x1, 0x2)
    OP_29(0x1F, 0x1, 0x3)
    OP_29(0x1F, 0x1, 0x4)
    OP_29(0x1F, 0x1, 0x5)
    OP_29(0x1F, 0x1, 0x6)
    OP_29(0x1F, 0x1, 0x7)
    OP_29(0x1F, 0x1, 0x8)
    OP_29(0x1F, 0x1, 0x9)
    OP_29(0x1F, 0x1, 0xA)
    OP_29(0x1F, 0x1, 0xB)
    OP_29(0x1F, 0x1, 0xC)
    OP_29(0x1F, 0x1, 0xD)
    OP_29(0x1F, 0x1, 0xE)
    OP_29(0x1F, 0x1, 0xF)
    OP_29(0x1F, 0x1, 0x10)
    OP_29(0x1F, 0x1, 0x11)
    OP_29(0x1F, 0x1, 0x12)
    OP_29(0x1F, 0x1, 0x13)
    OP_29(0x1F, 0x1, 0x14)
    OP_29(0x1F, 0x1, 0x15)
    OP_29(0x1F, 0x1, 0x16)
    OP_29(0x1F, 0x1, 0x17)
    OP_29(0x1F, 0x1, 0x18)
    OP_29(0x1F, 0x1, 0x19)
    OP_29(0x1F, 0x1, 0x1A)
    OP_29(0x1F, 0x1, 0x1B)
    OP_29(0x1F, 0x1, 0x1C)
    OP_29(0x1F, 0x1, 0x1D)
    OP_29(0x1F, 0x1, 0x1E)
    OP_29(0x1F, 0x1, 0x1F)
    OP_29(0x20, 0x1, 0x0)
    OP_29(0x20, 0x1, 0x1)
    OP_29(0x20, 0x1, 0x2)
    OP_29(0x20, 0x1, 0x3)
    OP_29(0x20, 0x1, 0x4)
    OP_29(0x20, 0x1, 0x5)
    OP_29(0x20, 0x1, 0x6)
    OP_29(0x20, 0x1, 0x7)
    OP_29(0x20, 0x1, 0x8)
    OP_29(0x20, 0x1, 0x9)
    OP_29(0x20, 0x1, 0xA)
    OP_29(0x20, 0x1, 0xB)
    OP_29(0x20, 0x1, 0xC)
    OP_29(0x20, 0x1, 0xD)
    OP_29(0x20, 0x1, 0xE)
    OP_29(0x20, 0x1, 0xF)
    OP_29(0x20, 0x1, 0x10)
    OP_29(0x20, 0x1, 0x11)
    OP_29(0x20, 0x1, 0x12)
    OP_29(0x20, 0x1, 0x13)
    OP_29(0x20, 0x1, 0x14)
    OP_29(0x20, 0x1, 0x15)
    OP_29(0x20, 0x1, 0x16)
    OP_29(0x20, 0x1, 0x17)
    OP_29(0x20, 0x1, 0x18)
    OP_29(0x20, 0x1, 0x19)
    OP_29(0x20, 0x1, 0x1A)
    OP_29(0x20, 0x1, 0x1B)
    OP_29(0x20, 0x1, 0x1C)
    OP_29(0x20, 0x1, 0x1D)
    OP_29(0x20, 0x1, 0x1E)
    OP_29(0x20, 0x1, 0x1F)
    OP_29(0x21, 0x1, 0x0)
    OP_29(0x21, 0x1, 0x1)
    OP_29(0x21, 0x1, 0x2)
    OP_29(0x21, 0x1, 0x3)
    OP_29(0x21, 0x1, 0x4)
    OP_29(0x21, 0x1, 0x5)
    OP_29(0x21, 0x1, 0x6)
    OP_29(0x21, 0x1, 0x7)
    OP_29(0x21, 0x1, 0x8)
    OP_29(0x21, 0x1, 0x9)
    OP_29(0x21, 0x1, 0xA)
    OP_29(0x21, 0x1, 0xB)
    OP_29(0x21, 0x1, 0xC)
    OP_29(0x21, 0x1, 0xD)
    OP_29(0x21, 0x1, 0xE)
    OP_29(0x21, 0x1, 0xF)
    OP_29(0x21, 0x1, 0x10)
    OP_29(0x21, 0x1, 0x11)
    OP_29(0x21, 0x1, 0x12)
    OP_29(0x21, 0x1, 0x13)
    OP_29(0x21, 0x1, 0x14)
    OP_29(0x21, 0x1, 0x15)
    OP_29(0x21, 0x1, 0x16)
    OP_29(0x21, 0x1, 0x17)
    OP_29(0x21, 0x1, 0x18)
    OP_29(0x21, 0x1, 0x19)
    OP_29(0x21, 0x1, 0x1A)
    OP_29(0x21, 0x1, 0x1B)
    OP_29(0x21, 0x1, 0x1C)
    OP_29(0x21, 0x1, 0x1D)
    OP_29(0x21, 0x1, 0x1E)
    OP_29(0x21, 0x1, 0x1F)
    OP_29(0x22, 0x1, 0x0)
    OP_29(0x22, 0x1, 0x1)
    OP_29(0x22, 0x1, 0x2)
    OP_29(0x22, 0x1, 0x3)
    OP_29(0x22, 0x1, 0x4)
    OP_29(0x22, 0x1, 0x5)
    OP_29(0x22, 0x1, 0x6)
    OP_29(0x22, 0x1, 0x7)
    OP_29(0x22, 0x1, 0x8)
    OP_29(0x22, 0x1, 0x9)
    OP_29(0x22, 0x1, 0xA)
    OP_29(0x22, 0x1, 0xB)
    OP_29(0x22, 0x1, 0xC)
    OP_29(0x22, 0x1, 0xD)
    OP_29(0x22, 0x1, 0xE)
    OP_29(0x22, 0x1, 0xF)
    OP_29(0x22, 0x1, 0x10)
    OP_29(0x22, 0x1, 0x11)
    OP_29(0x22, 0x1, 0x12)
    OP_29(0x22, 0x1, 0x13)
    OP_29(0x22, 0x1, 0x14)
    OP_29(0x22, 0x1, 0x15)
    OP_29(0x22, 0x1, 0x16)
    OP_29(0x22, 0x1, 0x17)
    OP_29(0x22, 0x1, 0x18)
    OP_29(0x22, 0x1, 0x19)
    OP_29(0x22, 0x1, 0x1A)
    OP_29(0x22, 0x1, 0x1B)
    OP_29(0x22, 0x1, 0x1C)
    OP_29(0x22, 0x1, 0x1D)
    OP_29(0x22, 0x1, 0x1E)
    OP_29(0x22, 0x1, 0x1F)
    OP_29(0x23, 0x1, 0x0)
    OP_29(0x23, 0x1, 0x1)
    OP_29(0x23, 0x1, 0x2)
    OP_29(0x23, 0x1, 0x3)
    OP_29(0x23, 0x1, 0x4)
    OP_29(0x23, 0x1, 0x5)
    OP_29(0x23, 0x1, 0x6)
    OP_29(0x23, 0x1, 0x7)
    OP_29(0x23, 0x1, 0x8)
    OP_29(0x23, 0x1, 0x9)
    OP_29(0x23, 0x1, 0xA)
    OP_29(0x23, 0x1, 0xB)
    OP_29(0x23, 0x1, 0xC)
    OP_29(0x23, 0x1, 0xD)
    OP_29(0x23, 0x1, 0xE)
    OP_29(0x23, 0x1, 0xF)
    OP_29(0x23, 0x1, 0x10)
    OP_29(0x23, 0x1, 0x11)
    OP_29(0x23, 0x1, 0x12)
    OP_29(0x23, 0x1, 0x13)
    OP_29(0x23, 0x1, 0x14)
    OP_29(0x23, 0x1, 0x15)
    OP_29(0x23, 0x1, 0x16)
    OP_29(0x23, 0x1, 0x17)
    OP_29(0x23, 0x1, 0x18)
    OP_29(0x23, 0x1, 0x19)
    OP_29(0x23, 0x1, 0x1A)
    OP_29(0x23, 0x1, 0x1B)
    OP_29(0x23, 0x1, 0x1C)
    OP_29(0x23, 0x1, 0x1D)
    OP_29(0x23, 0x1, 0x1E)
    OP_29(0x23, 0x1, 0x1F)
    OP_29(0x24, 0x1, 0x0)
    OP_29(0x24, 0x1, 0x1)
    OP_29(0x24, 0x1, 0x2)
    OP_29(0x24, 0x1, 0x3)
    OP_29(0x24, 0x1, 0x4)
    OP_29(0x24, 0x1, 0x5)
    OP_29(0x24, 0x1, 0x6)
    OP_29(0x24, 0x1, 0x7)
    OP_29(0x24, 0x1, 0x8)
    OP_29(0x24, 0x1, 0x9)
    OP_29(0x24, 0x1, 0xA)
    OP_29(0x24, 0x1, 0xB)
    OP_29(0x24, 0x1, 0xC)
    OP_29(0x24, 0x1, 0xD)
    OP_29(0x24, 0x1, 0xE)
    OP_29(0x24, 0x1, 0xF)
    OP_29(0x24, 0x1, 0x10)
    OP_29(0x24, 0x1, 0x11)
    OP_29(0x24, 0x1, 0x12)
    OP_29(0x24, 0x1, 0x13)
    OP_29(0x24, 0x1, 0x14)
    OP_29(0x24, 0x1, 0x15)
    OP_29(0x24, 0x1, 0x16)
    OP_29(0x24, 0x1, 0x17)
    OP_29(0x24, 0x1, 0x18)
    OP_29(0x24, 0x1, 0x19)
    OP_29(0x24, 0x1, 0x1A)
    OP_29(0x24, 0x1, 0x1B)
    OP_29(0x24, 0x1, 0x1C)
    OP_29(0x24, 0x1, 0x1D)
    OP_29(0x24, 0x1, 0x1E)
    OP_29(0x24, 0x1, 0x1F)
    OP_29(0x25, 0x1, 0x0)
    OP_29(0x25, 0x1, 0x1)
    OP_29(0x25, 0x1, 0x2)
    OP_29(0x25, 0x1, 0x3)
    OP_29(0x25, 0x1, 0x4)
    OP_29(0x25, 0x1, 0x5)
    OP_29(0x25, 0x1, 0x6)
    OP_29(0x25, 0x1, 0x7)
    OP_29(0x25, 0x1, 0x8)
    OP_29(0x25, 0x1, 0x9)
    OP_29(0x25, 0x1, 0xA)
    OP_29(0x25, 0x1, 0xB)
    OP_29(0x25, 0x1, 0xC)
    OP_29(0x25, 0x1, 0xD)
    OP_29(0x25, 0x1, 0xE)
    OP_29(0x25, 0x1, 0xF)
    OP_29(0x25, 0x1, 0x10)
    OP_29(0x25, 0x1, 0x11)
    OP_29(0x25, 0x1, 0x12)
    OP_29(0x25, 0x1, 0x13)
    OP_29(0x25, 0x1, 0x14)
    OP_29(0x25, 0x1, 0x15)
    OP_29(0x25, 0x1, 0x16)
    OP_29(0x25, 0x1, 0x17)
    OP_29(0x25, 0x1, 0x18)
    OP_29(0x25, 0x1, 0x19)
    OP_29(0x25, 0x1, 0x1A)
    OP_29(0x25, 0x1, 0x1B)
    OP_29(0x25, 0x1, 0x1C)
    OP_29(0x25, 0x1, 0x1D)
    OP_29(0x25, 0x1, 0x1E)
    OP_29(0x25, 0x1, 0x1F)
    OP_29(0x26, 0x1, 0x0)
    OP_29(0x26, 0x1, 0x1)
    OP_29(0x26, 0x1, 0x2)
    OP_29(0x26, 0x1, 0x3)
    OP_29(0x26, 0x1, 0x4)
    OP_29(0x26, 0x1, 0x5)
    OP_29(0x26, 0x1, 0x6)
    OP_29(0x26, 0x1, 0x7)
    OP_29(0x26, 0x1, 0x8)
    OP_29(0x26, 0x1, 0x9)
    OP_29(0x26, 0x1, 0xA)
    OP_29(0x26, 0x1, 0xB)
    OP_29(0x26, 0x1, 0xC)
    OP_29(0x26, 0x1, 0xD)
    OP_29(0x26, 0x1, 0xE)
    OP_29(0x26, 0x1, 0xF)
    OP_29(0x26, 0x1, 0x10)
    OP_29(0x26, 0x1, 0x11)
    OP_29(0x26, 0x1, 0x12)
    OP_29(0x26, 0x1, 0x13)
    OP_29(0x26, 0x1, 0x14)
    OP_29(0x26, 0x1, 0x15)
    OP_29(0x26, 0x1, 0x16)
    OP_29(0x26, 0x1, 0x17)
    OP_29(0x26, 0x1, 0x18)
    OP_29(0x26, 0x1, 0x19)
    OP_29(0x26, 0x1, 0x1A)
    OP_29(0x26, 0x1, 0x1B)
    OP_29(0x26, 0x1, 0x1C)
    OP_29(0x26, 0x1, 0x1D)
    OP_29(0x26, 0x1, 0x1E)
    OP_29(0x26, 0x1, 0x1F)
    OP_29(0x27, 0x1, 0x0)
    OP_29(0x27, 0x1, 0x1)
    OP_29(0x27, 0x1, 0x2)
    OP_29(0x27, 0x1, 0x3)
    OP_29(0x27, 0x1, 0x4)
    OP_29(0x27, 0x1, 0x5)
    OP_29(0x27, 0x1, 0x6)
    OP_29(0x27, 0x1, 0x7)
    OP_29(0x27, 0x1, 0x8)
    OP_29(0x27, 0x1, 0x9)
    OP_29(0x27, 0x1, 0xA)
    OP_29(0x27, 0x1, 0xB)
    OP_29(0x27, 0x1, 0xC)
    OP_29(0x27, 0x1, 0xD)
    OP_29(0x27, 0x1, 0xE)
    OP_29(0x27, 0x1, 0xF)
    OP_29(0x27, 0x1, 0x10)
    OP_29(0x27, 0x1, 0x11)
    OP_29(0x27, 0x1, 0x12)
    OP_29(0x27, 0x1, 0x13)
    OP_29(0x27, 0x1, 0x14)
    OP_29(0x27, 0x1, 0x15)
    OP_29(0x27, 0x1, 0x16)
    OP_29(0x27, 0x1, 0x17)
    OP_29(0x27, 0x1, 0x18)
    OP_29(0x27, 0x1, 0x19)
    OP_29(0x27, 0x1, 0x1A)
    OP_29(0x27, 0x1, 0x1B)
    OP_29(0x27, 0x1, 0x1C)
    OP_29(0x27, 0x1, 0x1D)
    OP_29(0x27, 0x1, 0x1E)
    OP_29(0x27, 0x1, 0x1F)
    OP_29(0x28, 0x1, 0x0)
    OP_29(0x28, 0x1, 0x1)
    OP_29(0x28, 0x1, 0x2)
    OP_29(0x28, 0x1, 0x3)
    OP_29(0x28, 0x1, 0x4)
    OP_29(0x28, 0x1, 0x5)
    OP_29(0x28, 0x1, 0x6)
    OP_29(0x28, 0x1, 0x7)
    OP_29(0x28, 0x1, 0x8)
    OP_29(0x28, 0x1, 0x9)
    OP_29(0x28, 0x1, 0xA)
    OP_29(0x28, 0x1, 0xB)
    OP_29(0x28, 0x1, 0xC)
    OP_29(0x28, 0x1, 0xD)
    OP_29(0x28, 0x1, 0xE)
    OP_29(0x28, 0x1, 0xF)
    OP_29(0x28, 0x1, 0x10)
    OP_29(0x28, 0x1, 0x11)
    OP_29(0x28, 0x1, 0x12)
    OP_29(0x28, 0x1, 0x13)
    OP_29(0x28, 0x1, 0x14)
    OP_29(0x28, 0x1, 0x15)
    OP_29(0x28, 0x1, 0x16)
    OP_29(0x28, 0x1, 0x17)
    OP_29(0x28, 0x1, 0x18)
    OP_29(0x28, 0x1, 0x19)
    OP_29(0x28, 0x1, 0x1A)
    OP_29(0x28, 0x1, 0x1B)
    OP_29(0x28, 0x1, 0x1C)
    OP_29(0x28, 0x1, 0x1D)
    OP_29(0x28, 0x1, 0x1E)
    OP_29(0x28, 0x1, 0x1F)
    OP_29(0x29, 0x1, 0x0)
    OP_29(0x29, 0x1, 0x1)
    OP_29(0x29, 0x1, 0x2)
    OP_29(0x29, 0x1, 0x3)
    OP_29(0x29, 0x1, 0x4)
    OP_29(0x29, 0x1, 0x5)
    OP_29(0x29, 0x1, 0x6)
    OP_29(0x29, 0x1, 0x7)
    OP_29(0x29, 0x1, 0x8)
    OP_29(0x29, 0x1, 0x9)
    OP_29(0x29, 0x1, 0xA)
    OP_29(0x29, 0x1, 0xB)
    OP_29(0x29, 0x1, 0xC)
    OP_29(0x29, 0x1, 0xD)
    OP_29(0x29, 0x1, 0xE)
    OP_29(0x29, 0x1, 0xF)
    OP_29(0x29, 0x1, 0x10)
    OP_29(0x29, 0x1, 0x11)
    OP_29(0x29, 0x1, 0x12)
    OP_29(0x29, 0x1, 0x13)
    OP_29(0x29, 0x1, 0x14)
    OP_29(0x29, 0x1, 0x15)
    OP_29(0x29, 0x1, 0x16)
    OP_29(0x29, 0x1, 0x17)
    OP_29(0x29, 0x1, 0x18)
    OP_29(0x29, 0x1, 0x19)
    OP_29(0x29, 0x1, 0x1A)
    OP_29(0x29, 0x1, 0x1B)
    OP_29(0x29, 0x1, 0x1C)
    OP_29(0x29, 0x1, 0x1D)
    OP_29(0x29, 0x1, 0x1E)
    OP_29(0x29, 0x1, 0x1F)
    OP_29(0x2A, 0x1, 0x0)
    OP_29(0x2A, 0x1, 0x1)
    OP_29(0x2A, 0x1, 0x2)
    OP_29(0x2A, 0x1, 0x3)
    OP_29(0x2A, 0x1, 0x4)
    OP_29(0x2A, 0x1, 0x5)
    OP_29(0x2A, 0x1, 0x6)
    OP_29(0x2A, 0x1, 0x7)
    OP_29(0x2A, 0x1, 0x8)
    OP_29(0x2A, 0x1, 0x9)
    OP_29(0x2A, 0x1, 0xA)
    OP_29(0x2A, 0x1, 0xB)
    OP_29(0x2A, 0x1, 0xC)
    OP_29(0x2A, 0x1, 0xD)
    OP_29(0x2A, 0x1, 0xE)
    OP_29(0x2A, 0x1, 0xF)
    OP_29(0x2A, 0x1, 0x10)
    OP_29(0x2A, 0x1, 0x11)
    OP_29(0x2A, 0x1, 0x12)
    OP_29(0x2A, 0x1, 0x13)
    OP_29(0x2A, 0x1, 0x14)
    OP_29(0x2A, 0x1, 0x15)
    OP_29(0x2A, 0x1, 0x16)
    OP_29(0x2A, 0x1, 0x17)
    OP_29(0x2A, 0x1, 0x18)
    OP_29(0x2A, 0x1, 0x19)
    OP_29(0x2A, 0x1, 0x1A)
    OP_29(0x2A, 0x1, 0x1B)
    OP_29(0x2A, 0x1, 0x1C)
    OP_29(0x2A, 0x1, 0x1D)
    OP_29(0x2A, 0x1, 0x1E)
    OP_29(0x2A, 0x1, 0x1F)
    OP_29(0x2B, 0x1, 0x0)
    OP_29(0x2B, 0x1, 0x1)
    OP_29(0x2B, 0x1, 0x2)
    OP_29(0x2B, 0x1, 0x3)
    OP_29(0x2B, 0x1, 0x4)
    OP_29(0x2B, 0x1, 0x5)
    OP_29(0x2B, 0x1, 0x6)
    OP_29(0x2B, 0x1, 0x7)
    OP_29(0x2B, 0x1, 0x8)
    OP_29(0x2B, 0x1, 0x9)
    OP_29(0x2B, 0x1, 0xA)
    OP_29(0x2B, 0x1, 0xB)
    OP_29(0x2B, 0x1, 0xC)
    OP_29(0x2B, 0x1, 0xD)
    OP_29(0x2B, 0x1, 0xE)
    OP_29(0x2B, 0x1, 0xF)
    OP_29(0x2B, 0x1, 0x10)
    OP_29(0x2B, 0x1, 0x11)
    OP_29(0x2B, 0x1, 0x12)
    OP_29(0x2B, 0x1, 0x13)
    OP_29(0x2B, 0x1, 0x14)
    OP_29(0x2B, 0x1, 0x15)
    OP_29(0x2B, 0x1, 0x16)
    OP_29(0x2B, 0x1, 0x17)
    OP_29(0x2B, 0x1, 0x18)
    OP_29(0x2B, 0x1, 0x19)
    OP_29(0x2B, 0x1, 0x1A)
    OP_29(0x2B, 0x1, 0x1B)
    OP_29(0x2B, 0x1, 0x1C)
    OP_29(0x2B, 0x1, 0x1D)
    OP_29(0x2B, 0x1, 0x1E)
    OP_29(0x2B, 0x1, 0x1F)
    OP_29(0x2C, 0x1, 0x0)
    OP_29(0x2C, 0x1, 0x1)
    OP_29(0x2C, 0x1, 0x2)
    OP_29(0x2C, 0x1, 0x3)
    OP_29(0x2C, 0x1, 0x4)
    OP_29(0x2C, 0x1, 0x5)
    OP_29(0x2C, 0x1, 0x6)
    OP_29(0x2C, 0x1, 0x7)
    OP_29(0x2C, 0x1, 0x8)
    OP_29(0x2C, 0x1, 0x9)
    OP_29(0x2C, 0x1, 0xA)
    OP_29(0x2C, 0x1, 0xB)
    OP_29(0x2C, 0x1, 0xC)
    OP_29(0x2C, 0x1, 0xD)
    OP_29(0x2C, 0x1, 0xE)
    OP_29(0x2C, 0x1, 0xF)
    OP_29(0x2C, 0x1, 0x10)
    OP_29(0x2C, 0x1, 0x11)
    OP_29(0x2C, 0x1, 0x12)
    OP_29(0x2C, 0x1, 0x13)
    OP_29(0x2C, 0x1, 0x14)
    OP_29(0x2C, 0x1, 0x15)
    OP_29(0x2C, 0x1, 0x16)
    OP_29(0x2C, 0x1, 0x17)
    OP_29(0x2C, 0x1, 0x18)
    OP_29(0x2C, 0x1, 0x19)
    OP_29(0x2C, 0x1, 0x1A)
    OP_29(0x2C, 0x1, 0x1B)
    OP_29(0x2C, 0x1, 0x1C)
    OP_29(0x2C, 0x1, 0x1D)
    OP_29(0x2C, 0x1, 0x1E)
    OP_29(0x2C, 0x1, 0x1F)
    OP_29(0x2D, 0x1, 0x0)
    OP_29(0x2D, 0x1, 0x1)
    OP_29(0x2D, 0x1, 0x2)
    OP_29(0x2D, 0x1, 0x3)
    OP_29(0x2D, 0x1, 0x4)
    OP_29(0x2D, 0x1, 0x5)
    OP_29(0x2D, 0x1, 0x6)
    OP_29(0x2D, 0x1, 0x7)
    OP_29(0x2D, 0x1, 0x8)
    OP_29(0x2D, 0x1, 0x9)
    OP_29(0x2D, 0x1, 0xA)
    OP_29(0x2D, 0x1, 0xB)
    OP_29(0x2D, 0x1, 0xC)
    OP_29(0x2D, 0x1, 0xD)
    OP_29(0x2D, 0x1, 0xE)
    OP_29(0x2D, 0x1, 0xF)
    OP_29(0x2D, 0x1, 0x10)
    OP_29(0x2D, 0x1, 0x11)
    OP_29(0x2D, 0x1, 0x12)
    OP_29(0x2D, 0x1, 0x13)
    OP_29(0x2D, 0x1, 0x14)
    OP_29(0x2D, 0x1, 0x15)
    OP_29(0x2D, 0x1, 0x16)
    OP_29(0x2D, 0x1, 0x17)
    OP_29(0x2D, 0x1, 0x18)
    OP_29(0x2D, 0x1, 0x19)
    OP_29(0x2D, 0x1, 0x1A)
    OP_29(0x2D, 0x1, 0x1B)
    OP_29(0x2D, 0x1, 0x1C)
    OP_29(0x2D, 0x1, 0x1D)
    OP_29(0x2D, 0x1, 0x1E)
    OP_29(0x2D, 0x1, 0x1F)
    OP_29(0x2E, 0x1, 0x0)
    OP_29(0x2E, 0x1, 0x1)
    OP_29(0x2E, 0x1, 0x2)
    OP_29(0x2E, 0x1, 0x3)
    OP_29(0x2E, 0x1, 0x4)
    OP_29(0x2E, 0x1, 0x5)
    OP_29(0x2E, 0x1, 0x6)
    OP_29(0x2E, 0x1, 0x7)
    OP_29(0x2E, 0x1, 0x8)
    OP_29(0x2E, 0x1, 0x9)
    OP_29(0x2E, 0x1, 0xA)
    OP_29(0x2E, 0x1, 0xB)
    OP_29(0x2E, 0x1, 0xC)
    OP_29(0x2E, 0x1, 0xD)
    OP_29(0x2E, 0x1, 0xE)
    OP_29(0x2E, 0x1, 0xF)
    OP_29(0x2E, 0x1, 0x10)
    OP_29(0x2E, 0x1, 0x11)
    OP_29(0x2E, 0x1, 0x12)
    OP_29(0x2E, 0x1, 0x13)
    OP_29(0x2E, 0x1, 0x14)
    OP_29(0x2E, 0x1, 0x15)
    OP_29(0x2E, 0x1, 0x16)
    OP_29(0x2E, 0x1, 0x17)
    OP_29(0x2E, 0x1, 0x18)
    OP_29(0x2E, 0x1, 0x19)
    OP_29(0x2E, 0x1, 0x1A)
    OP_29(0x2E, 0x1, 0x1B)
    OP_29(0x2E, 0x1, 0x1C)
    OP_29(0x2E, 0x1, 0x1D)
    OP_29(0x2E, 0x1, 0x1E)
    OP_29(0x2E, 0x1, 0x1F)
    OP_29(0x2F, 0x1, 0x0)
    OP_29(0x2F, 0x1, 0x1)
    OP_29(0x2F, 0x1, 0x2)
    OP_29(0x2F, 0x1, 0x3)
    OP_29(0x2F, 0x1, 0x4)
    OP_29(0x2F, 0x1, 0x5)
    OP_29(0x2F, 0x1, 0x6)
    OP_29(0x2F, 0x1, 0x7)
    OP_29(0x2F, 0x1, 0x8)
    OP_29(0x2F, 0x1, 0x9)
    OP_29(0x2F, 0x1, 0xA)
    OP_29(0x2F, 0x1, 0xB)
    OP_29(0x2F, 0x1, 0xC)
    OP_29(0x2F, 0x1, 0xD)
    OP_29(0x2F, 0x1, 0xE)
    OP_29(0x2F, 0x1, 0xF)
    OP_29(0x2F, 0x1, 0x10)
    OP_29(0x2F, 0x1, 0x11)
    OP_29(0x2F, 0x1, 0x12)
    OP_29(0x2F, 0x1, 0x13)
    OP_29(0x2F, 0x1, 0x14)
    OP_29(0x2F, 0x1, 0x15)
    OP_29(0x2F, 0x1, 0x16)
    OP_29(0x2F, 0x1, 0x17)
    OP_29(0x2F, 0x1, 0x18)
    OP_29(0x2F, 0x1, 0x19)
    OP_29(0x2F, 0x1, 0x1A)
    OP_29(0x2F, 0x1, 0x1B)
    OP_29(0x2F, 0x1, 0x1C)
    OP_29(0x2F, 0x1, 0x1D)
    OP_29(0x2F, 0x1, 0x1E)
    OP_29(0x2F, 0x1, 0x1F)
    OP_29(0x30, 0x1, 0x0)
    OP_29(0x30, 0x1, 0x1)
    OP_29(0x30, 0x1, 0x2)
    OP_29(0x30, 0x1, 0x3)
    OP_29(0x30, 0x1, 0x4)
    OP_29(0x30, 0x1, 0x5)
    OP_29(0x30, 0x1, 0x6)
    OP_29(0x30, 0x1, 0x7)
    OP_29(0x30, 0x1, 0x8)
    OP_29(0x30, 0x1, 0x9)
    OP_29(0x30, 0x1, 0xA)
    OP_29(0x30, 0x1, 0xB)
    OP_29(0x30, 0x1, 0xC)
    OP_29(0x30, 0x1, 0xD)
    OP_29(0x30, 0x1, 0xE)
    OP_29(0x30, 0x1, 0xF)
    OP_29(0x30, 0x1, 0x10)
    OP_29(0x30, 0x1, 0x11)
    OP_29(0x30, 0x1, 0x12)
    OP_29(0x30, 0x1, 0x13)
    OP_29(0x30, 0x1, 0x14)
    OP_29(0x30, 0x1, 0x15)
    OP_29(0x30, 0x1, 0x16)
    OP_29(0x30, 0x1, 0x17)
    OP_29(0x30, 0x1, 0x18)
    OP_29(0x30, 0x1, 0x19)
    OP_29(0x30, 0x1, 0x1A)
    OP_29(0x30, 0x1, 0x1B)
    OP_29(0x30, 0x1, 0x1C)
    OP_29(0x30, 0x1, 0x1D)
    OP_29(0x30, 0x1, 0x1E)
    OP_29(0x30, 0x1, 0x1F)
    OP_29(0x31, 0x1, 0x0)
    OP_29(0x31, 0x1, 0x1)
    OP_29(0x31, 0x1, 0x2)
    OP_29(0x31, 0x1, 0x3)
    OP_29(0x31, 0x1, 0x4)
    OP_29(0x31, 0x1, 0x5)
    OP_29(0x31, 0x1, 0x6)
    OP_29(0x31, 0x1, 0x7)
    OP_29(0x31, 0x1, 0x8)
    OP_29(0x31, 0x1, 0x9)
    OP_29(0x31, 0x1, 0xA)
    OP_29(0x31, 0x1, 0xB)
    OP_29(0x31, 0x1, 0xC)
    OP_29(0x31, 0x1, 0xD)
    OP_29(0x31, 0x1, 0xE)
    OP_29(0x31, 0x1, 0xF)
    OP_29(0x31, 0x1, 0x10)
    OP_29(0x31, 0x1, 0x11)
    OP_29(0x31, 0x1, 0x12)
    OP_29(0x31, 0x1, 0x13)
    OP_29(0x31, 0x1, 0x14)
    OP_29(0x31, 0x1, 0x15)
    OP_29(0x31, 0x1, 0x16)
    OP_29(0x31, 0x1, 0x17)
    OP_29(0x31, 0x1, 0x18)
    OP_29(0x31, 0x1, 0x19)
    OP_29(0x31, 0x1, 0x1A)
    OP_29(0x31, 0x1, 0x1B)
    OP_29(0x31, 0x1, 0x1C)
    OP_29(0x31, 0x1, 0x1D)
    OP_29(0x31, 0x1, 0x1E)
    OP_29(0x31, 0x1, 0x1F)
    OP_29(0x32, 0x1, 0x0)
    OP_29(0x32, 0x1, 0x1)
    OP_29(0x32, 0x1, 0x2)
    OP_29(0x32, 0x1, 0x3)
    OP_29(0x32, 0x1, 0x4)
    OP_29(0x32, 0x1, 0x5)
    OP_29(0x32, 0x1, 0x6)
    OP_29(0x32, 0x1, 0x7)
    OP_29(0x32, 0x1, 0x8)
    OP_29(0x32, 0x1, 0x9)
    OP_29(0x32, 0x1, 0xA)
    OP_29(0x32, 0x1, 0xB)
    OP_29(0x32, 0x1, 0xC)
    OP_29(0x32, 0x1, 0xD)
    OP_29(0x32, 0x1, 0xE)
    OP_29(0x32, 0x1, 0xF)
    OP_29(0x32, 0x1, 0x10)
    OP_29(0x32, 0x1, 0x11)
    OP_29(0x32, 0x1, 0x12)
    OP_29(0x32, 0x1, 0x13)
    OP_29(0x32, 0x1, 0x14)
    OP_29(0x32, 0x1, 0x15)
    OP_29(0x32, 0x1, 0x16)
    OP_29(0x32, 0x1, 0x17)
    OP_29(0x32, 0x1, 0x18)
    OP_29(0x32, 0x1, 0x19)
    OP_29(0x32, 0x1, 0x1A)
    OP_29(0x32, 0x1, 0x1B)
    OP_29(0x32, 0x1, 0x1C)
    OP_29(0x32, 0x1, 0x1D)
    OP_29(0x32, 0x1, 0x1E)
    OP_29(0x32, 0x1, 0x1F)
    OP_29(0x33, 0x1, 0x0)
    OP_29(0x33, 0x1, 0x1)
    OP_29(0x33, 0x1, 0x2)
    OP_29(0x33, 0x1, 0x3)
    OP_29(0x33, 0x1, 0x4)
    OP_29(0x33, 0x1, 0x5)
    OP_29(0x33, 0x1, 0x6)
    OP_29(0x33, 0x1, 0x7)
    OP_29(0x33, 0x1, 0x8)
    OP_29(0x33, 0x1, 0x9)
    OP_29(0x33, 0x1, 0xA)
    OP_29(0x33, 0x1, 0xB)
    OP_29(0x33, 0x1, 0xC)
    OP_29(0x33, 0x1, 0xD)
    OP_29(0x33, 0x1, 0xE)
    OP_29(0x33, 0x1, 0xF)
    OP_29(0x33, 0x1, 0x10)
    OP_29(0x33, 0x1, 0x11)
    OP_29(0x33, 0x1, 0x12)
    OP_29(0x33, 0x1, 0x13)
    OP_29(0x33, 0x1, 0x14)
    OP_29(0x33, 0x1, 0x15)
    OP_29(0x33, 0x1, 0x16)
    OP_29(0x33, 0x1, 0x17)
    OP_29(0x33, 0x1, 0x18)
    OP_29(0x33, 0x1, 0x19)
    OP_29(0x33, 0x1, 0x1A)
    OP_29(0x33, 0x1, 0x1B)
    OP_29(0x33, 0x1, 0x1C)
    OP_29(0x33, 0x1, 0x1D)
    OP_29(0x33, 0x1, 0x1E)
    OP_29(0x33, 0x1, 0x1F)
    OP_29(0x34, 0x1, 0x0)
    OP_29(0x34, 0x1, 0x1)
    OP_29(0x34, 0x1, 0x2)
    OP_29(0x34, 0x1, 0x3)
    OP_29(0x34, 0x1, 0x4)
    OP_29(0x34, 0x1, 0x5)
    OP_29(0x34, 0x1, 0x6)
    OP_29(0x34, 0x1, 0x7)
    OP_29(0x34, 0x1, 0x8)
    OP_29(0x34, 0x1, 0x9)
    OP_29(0x34, 0x1, 0xA)
    OP_29(0x34, 0x1, 0xB)
    OP_29(0x34, 0x1, 0xC)
    OP_29(0x34, 0x1, 0xD)
    OP_29(0x34, 0x1, 0xE)
    OP_29(0x34, 0x1, 0xF)
    OP_29(0x34, 0x1, 0x10)
    OP_29(0x34, 0x1, 0x11)
    OP_29(0x34, 0x1, 0x12)
    OP_29(0x34, 0x1, 0x13)
    OP_29(0x34, 0x1, 0x14)
    OP_29(0x34, 0x1, 0x15)
    OP_29(0x34, 0x1, 0x16)
    OP_29(0x34, 0x1, 0x17)
    OP_29(0x34, 0x1, 0x18)
    OP_29(0x34, 0x1, 0x19)
    OP_29(0x34, 0x1, 0x1A)
    OP_29(0x34, 0x1, 0x1B)
    OP_29(0x34, 0x1, 0x1C)
    OP_29(0x34, 0x1, 0x1D)
    OP_29(0x34, 0x1, 0x1E)
    OP_29(0x34, 0x1, 0x1F)
    Jump("loc_B7F5")

    label("loc_B7E6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B7F5")

    label("loc_B7F5")

    Jump("loc_7989")

    label("loc_B7FA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_54_797F end

    def Function_55_B808(): pass

    label("Function_55_B808")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B812")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D76D")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "----------序章--------------\x01",       # 0
            "QS_0001  戦闘手帳の交付      \x01",      # 1
            "QS_0002  落し物の捜索        \x01",      # 2
            "QS_0003  不在住戸の確認      \x01",      # 3
            "QS_0004  ギルド受付の挑戦    \x01",      # 4
            "QS_0005  手配魔獣①          \x01",      # 5
            "----------１章--------------\x01",       # 6
            "QS_0101  延滞本の回収        \x01",      # 7
            "QS_0102  食材集めの依頼      \x01",      # 8
            "QS_0103  新サービスの運用協力\x01",      # 9
            "QS_0104  仔猫の飼い主探し    \x01",      # 10
            "QS_0105  帝国臨検官の手伝い  \x01",      # 11
            "QS_0106  廃アパートの魔獣退治\x01",      # 12
            "QS_0107  手配魔獣②          \x01",      # 13
            "QS_0108  憧れのみっしぃ      \x01",      # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_BA45"),
        (2, "loc_BA45"),
        (3, "loc_BA45"),
        (4, "loc_BA45"),
        (5, "loc_BA45"),
        (7, "loc_BA45"),
        (8, "loc_BA45"),
        (9, "loc_BA45"),
        (10, "loc_BA45"),
        (11, "loc_BA45"),
        (12, "loc_BA45"),
        (13, "loc_BA45"),
        (14, "loc_BA45"),
        (SWITCH_DEFAULT, "loc_BABE"),
    )


    label("loc_BA45")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期化\x01",      # 0
            "開始\x01",        # 1
            "QF_01\x01",       # 2
            "QF_02\x01",       # 3
            "QF_03\x01",       # 4
            "QF_04\x01",       # 5
            "QF_05\x01",       # 6
            "QF_06\x01",       # 7
            "QF_07\x01",       # 8
            "QF_08\x01",       # 9
            "QF_09\x01",       # 10
            "QF_10\x01",       # 11
            "QF_11\x01",       # 12
            "QF_12\x01",       # 13
            "達成\x01",        # 14
            "報告\x01",        # 15
        )
    )

    MenuEnd(0x5)
    Jump("loc_BACD")

    label("loc_BABE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_BACD")

    label("loc_BACD")

    OP_60(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D768")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_BB37"),
        (2, "loc_BD70"),
        (3, "loc_BF9A"),
        (4, "loc_C1C4"),
        (5, "loc_C3EE"),
        (7, "loc_C618"),
        (8, "loc_C842"),
        (9, "loc_CA6C"),
        (10, "loc_CC96"),
        (11, "loc_CEC0"),
        (12, "loc_D0EA"),
        (13, "loc_D314"),
        (14, "loc_D53E"),
        (SWITCH_DEFAULT, "loc_D768"),
    )


    label("loc_BB37")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC27")
    OP_29(0x1, 0x3, 0x0)
    OP_29(0x1, 0x3, 0x1)
    OP_29(0x1, 0x3, 0x2)
    OP_29(0x1, 0x3, 0x10)
    OP_29(0x1, 0x3, 0x20)
    OP_29(0x1, 0x3, 0x40)
    OP_29(0x1, 0x2, 0x0)
    OP_29(0x1, 0x2, 0x1)
    OP_29(0x1, 0x2, 0x2)
    OP_29(0x1, 0x2, 0x3)
    OP_29(0x1, 0x2, 0x4)
    OP_29(0x1, 0x2, 0x5)
    OP_29(0x1, 0x2, 0x6)
    OP_29(0x1, 0x2, 0x7)
    OP_29(0x1, 0x2, 0x8)
    OP_29(0x1, 0x2, 0x9)
    OP_29(0x1, 0x2, 0xA)
    OP_29(0x1, 0x2, 0xB)
    OP_29(0x1, 0x2, 0xC)
    OP_29(0x1, 0x2, 0xD)
    OP_29(0x1, 0x2, 0xE)
    OP_29(0x1, 0x2, 0xF)
    OP_29(0x1, 0x2, 0x10)
    OP_29(0x1, 0x2, 0x11)
    OP_29(0x1, 0x2, 0x12)
    OP_29(0x1, 0x2, 0x13)
    OP_29(0x1, 0x2, 0x14)
    OP_29(0x1, 0x2, 0x15)
    OP_29(0x1, 0x2, 0x16)
    OP_29(0x1, 0x2, 0x17)
    OP_29(0x1, 0x2, 0x18)
    OP_29(0x1, 0x2, 0x19)
    OP_29(0x1, 0x2, 0x1A)
    OP_29(0x1, 0x2, 0x1B)
    OP_29(0x1, 0x2, 0x1C)
    OP_29(0x1, 0x2, 0x1D)
    OP_29(0x1, 0x2, 0x1E)
    OP_29(0x1, 0x2, 0x1F)
    ClearScenarioFlags(0x50, 1)

    label("loc_BC27")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BC3B")
    OP_29(0x1, 0x4, 0x2)

    label("loc_BC3B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BC50")
    OP_29(0x1, 0x1, 0x0)

    label("loc_BC50")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BC65")
    OP_29(0x1, 0x1, 0x1)

    label("loc_BC65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BC7A")
    OP_29(0x1, 0x1, 0x2)

    label("loc_BC7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BC8F")
    OP_29(0x1, 0x1, 0x3)

    label("loc_BC8F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BCA4")
    OP_29(0x1, 0x1, 0x4)

    label("loc_BCA4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BCB9")
    OP_29(0x1, 0x1, 0x5)

    label("loc_BCB9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BCCE")
    OP_29(0x1, 0x1, 0x6)

    label("loc_BCCE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BCE3")
    OP_29(0x1, 0x1, 0x7)

    label("loc_BCE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BCF8")
    OP_29(0x1, 0x1, 0x8)

    label("loc_BCF8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BD0D")
    OP_29(0x1, 0x1, 0x9)

    label("loc_BD0D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BD22")
    OP_29(0x1, 0x1, 0xA)

    label("loc_BD22")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BD37")
    OP_29(0x1, 0x1, 0xB)

    label("loc_BD37")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BD57")
    OP_29(0x1, 0x2, 0x0)
    OP_29(0x1, 0x2, 0x1)
    OP_29(0x1, 0x4, 0x10)

    label("loc_BD57")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BD6B")
    OP_29(0x1, 0x4, 0x20)

    label("loc_BD6B")

    Jump("loc_D768")

    label("loc_BD70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE5D")
    OP_29(0x2, 0x3, 0x0)
    OP_29(0x2, 0x3, 0x1)
    OP_29(0x2, 0x3, 0x2)
    OP_29(0x2, 0x3, 0x10)
    OP_29(0x2, 0x3, 0x20)
    OP_29(0x2, 0x3, 0x40)
    OP_29(0x2, 0x2, 0x0)
    OP_29(0x2, 0x2, 0x1)
    OP_29(0x2, 0x2, 0x2)
    OP_29(0x2, 0x2, 0x3)
    OP_29(0x2, 0x2, 0x4)
    OP_29(0x2, 0x2, 0x5)
    OP_29(0x2, 0x2, 0x6)
    OP_29(0x2, 0x2, 0x7)
    OP_29(0x2, 0x2, 0x8)
    OP_29(0x2, 0x2, 0x9)
    OP_29(0x2, 0x2, 0xA)
    OP_29(0x2, 0x2, 0xB)
    OP_29(0x2, 0x2, 0xC)
    OP_29(0x2, 0x2, 0xD)
    OP_29(0x2, 0x2, 0xE)
    OP_29(0x2, 0x2, 0xF)
    OP_29(0x2, 0x2, 0x10)
    OP_29(0x2, 0x2, 0x11)
    OP_29(0x2, 0x2, 0x12)
    OP_29(0x2, 0x2, 0x13)
    OP_29(0x2, 0x2, 0x14)
    OP_29(0x2, 0x2, 0x15)
    OP_29(0x2, 0x2, 0x16)
    OP_29(0x2, 0x2, 0x17)
    OP_29(0x2, 0x2, 0x18)
    OP_29(0x2, 0x2, 0x19)
    OP_29(0x2, 0x2, 0x1A)
    OP_29(0x2, 0x2, 0x1B)
    OP_29(0x2, 0x2, 0x1C)
    OP_29(0x2, 0x2, 0x1D)
    OP_29(0x2, 0x2, 0x1E)
    OP_29(0x2, 0x2, 0x1F)

    label("loc_BE5D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BE71")
    OP_29(0x2, 0x4, 0x2)

    label("loc_BE71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BE86")
    OP_29(0x2, 0x1, 0x0)

    label("loc_BE86")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BE9B")
    OP_29(0x2, 0x1, 0x1)

    label("loc_BE9B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BEB0")
    OP_29(0x2, 0x1, 0x2)

    label("loc_BEB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BEC5")
    OP_29(0x2, 0x1, 0x3)

    label("loc_BEC5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BEDA")
    OP_29(0x2, 0x1, 0x4)

    label("loc_BEDA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BEEF")
    OP_29(0x2, 0x1, 0x5)

    label("loc_BEEF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BF04")
    OP_29(0x2, 0x1, 0x6)

    label("loc_BF04")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BF19")
    OP_29(0x2, 0x1, 0x7)

    label("loc_BF19")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BF2E")
    OP_29(0x2, 0x1, 0x8)

    label("loc_BF2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BF43")
    OP_29(0x2, 0x1, 0x9)

    label("loc_BF43")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BF58")
    OP_29(0x2, 0x1, 0xA)

    label("loc_BF58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BF6D")
    OP_29(0x2, 0x1, 0xB)

    label("loc_BF6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BF81")
    OP_29(0x2, 0x4, 0x10)

    label("loc_BF81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BF95")
    OP_29(0x2, 0x4, 0x20)

    label("loc_BF95")

    Jump("loc_D768")

    label("loc_BF9A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C087")
    OP_29(0x3, 0x3, 0x0)
    OP_29(0x3, 0x3, 0x1)
    OP_29(0x3, 0x3, 0x2)
    OP_29(0x3, 0x3, 0x10)
    OP_29(0x3, 0x3, 0x20)
    OP_29(0x3, 0x3, 0x40)
    OP_29(0x3, 0x2, 0x0)
    OP_29(0x3, 0x2, 0x1)
    OP_29(0x3, 0x2, 0x2)
    OP_29(0x3, 0x2, 0x3)
    OP_29(0x3, 0x2, 0x4)
    OP_29(0x3, 0x2, 0x5)
    OP_29(0x3, 0x2, 0x6)
    OP_29(0x3, 0x2, 0x7)
    OP_29(0x3, 0x2, 0x8)
    OP_29(0x3, 0x2, 0x9)
    OP_29(0x3, 0x2, 0xA)
    OP_29(0x3, 0x2, 0xB)
    OP_29(0x3, 0x2, 0xC)
    OP_29(0x3, 0x2, 0xD)
    OP_29(0x3, 0x2, 0xE)
    OP_29(0x3, 0x2, 0xF)
    OP_29(0x3, 0x2, 0x10)
    OP_29(0x3, 0x2, 0x11)
    OP_29(0x3, 0x2, 0x12)
    OP_29(0x3, 0x2, 0x13)
    OP_29(0x3, 0x2, 0x14)
    OP_29(0x3, 0x2, 0x15)
    OP_29(0x3, 0x2, 0x16)
    OP_29(0x3, 0x2, 0x17)
    OP_29(0x3, 0x2, 0x18)
    OP_29(0x3, 0x2, 0x19)
    OP_29(0x3, 0x2, 0x1A)
    OP_29(0x3, 0x2, 0x1B)
    OP_29(0x3, 0x2, 0x1C)
    OP_29(0x3, 0x2, 0x1D)
    OP_29(0x3, 0x2, 0x1E)
    OP_29(0x3, 0x2, 0x1F)

    label("loc_C087")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C09B")
    OP_29(0x3, 0x4, 0x2)

    label("loc_C09B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C0B0")
    OP_29(0x3, 0x1, 0x0)

    label("loc_C0B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C0C5")
    OP_29(0x3, 0x1, 0x1)

    label("loc_C0C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C0DA")
    OP_29(0x3, 0x1, 0x2)

    label("loc_C0DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C0EF")
    OP_29(0x3, 0x1, 0x3)

    label("loc_C0EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C104")
    OP_29(0x3, 0x1, 0x4)

    label("loc_C104")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C119")
    OP_29(0x3, 0x1, 0x5)

    label("loc_C119")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C12E")
    OP_29(0x3, 0x1, 0x6)

    label("loc_C12E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C143")
    OP_29(0x3, 0x1, 0x7)

    label("loc_C143")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C158")
    OP_29(0x3, 0x1, 0x8)

    label("loc_C158")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C16D")
    OP_29(0x3, 0x1, 0x9)

    label("loc_C16D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C182")
    OP_29(0x3, 0x1, 0xA)

    label("loc_C182")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C197")
    OP_29(0x3, 0x1, 0xB)

    label("loc_C197")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C1AB")
    OP_29(0x3, 0x4, 0x10)

    label("loc_C1AB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C1BF")
    OP_29(0x3, 0x4, 0x20)

    label("loc_C1BF")

    Jump("loc_D768")

    label("loc_C1C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2B1")
    OP_29(0x4, 0x3, 0x0)
    OP_29(0x4, 0x3, 0x1)
    OP_29(0x4, 0x3, 0x2)
    OP_29(0x4, 0x3, 0x10)
    OP_29(0x4, 0x3, 0x20)
    OP_29(0x4, 0x3, 0x40)
    OP_29(0x4, 0x2, 0x0)
    OP_29(0x4, 0x2, 0x1)
    OP_29(0x4, 0x2, 0x2)
    OP_29(0x4, 0x2, 0x3)
    OP_29(0x4, 0x2, 0x4)
    OP_29(0x4, 0x2, 0x5)
    OP_29(0x4, 0x2, 0x6)
    OP_29(0x4, 0x2, 0x7)
    OP_29(0x4, 0x2, 0x8)
    OP_29(0x4, 0x2, 0x9)
    OP_29(0x4, 0x2, 0xA)
    OP_29(0x4, 0x2, 0xB)
    OP_29(0x4, 0x2, 0xC)
    OP_29(0x4, 0x2, 0xD)
    OP_29(0x4, 0x2, 0xE)
    OP_29(0x4, 0x2, 0xF)
    OP_29(0x4, 0x2, 0x10)
    OP_29(0x4, 0x2, 0x11)
    OP_29(0x4, 0x2, 0x12)
    OP_29(0x4, 0x2, 0x13)
    OP_29(0x4, 0x2, 0x14)
    OP_29(0x4, 0x2, 0x15)
    OP_29(0x4, 0x2, 0x16)
    OP_29(0x4, 0x2, 0x17)
    OP_29(0x4, 0x2, 0x18)
    OP_29(0x4, 0x2, 0x19)
    OP_29(0x4, 0x2, 0x1A)
    OP_29(0x4, 0x2, 0x1B)
    OP_29(0x4, 0x2, 0x1C)
    OP_29(0x4, 0x2, 0x1D)
    OP_29(0x4, 0x2, 0x1E)
    OP_29(0x4, 0x2, 0x1F)

    label("loc_C2B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C2C5")
    OP_29(0x4, 0x4, 0x2)

    label("loc_C2C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C2DA")
    OP_29(0x4, 0x1, 0x0)

    label("loc_C2DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C2EF")
    OP_29(0x4, 0x1, 0x1)

    label("loc_C2EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C304")
    OP_29(0x4, 0x1, 0x2)

    label("loc_C304")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C319")
    OP_29(0x4, 0x1, 0x3)

    label("loc_C319")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C32E")
    OP_29(0x4, 0x1, 0x4)

    label("loc_C32E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C343")
    OP_29(0x4, 0x1, 0x5)

    label("loc_C343")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C358")
    OP_29(0x4, 0x1, 0x6)

    label("loc_C358")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C36D")
    OP_29(0x4, 0x1, 0x7)

    label("loc_C36D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C382")
    OP_29(0x4, 0x1, 0x8)

    label("loc_C382")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C397")
    OP_29(0x4, 0x1, 0x9)

    label("loc_C397")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C3AC")
    OP_29(0x4, 0x1, 0xA)

    label("loc_C3AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C3C1")
    OP_29(0x4, 0x1, 0xB)

    label("loc_C3C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C3D5")
    OP_29(0x4, 0x4, 0x10)

    label("loc_C3D5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C3E9")
    OP_29(0x4, 0x4, 0x20)

    label("loc_C3E9")

    Jump("loc_D768")

    label("loc_C3EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4DB")
    OP_29(0x35, 0x3, 0x0)
    OP_29(0x35, 0x3, 0x1)
    OP_29(0x35, 0x3, 0x2)
    OP_29(0x35, 0x3, 0x10)
    OP_29(0x35, 0x3, 0x20)
    OP_29(0x35, 0x3, 0x40)
    OP_29(0x35, 0x2, 0x0)
    OP_29(0x35, 0x2, 0x1)
    OP_29(0x35, 0x2, 0x2)
    OP_29(0x35, 0x2, 0x3)
    OP_29(0x35, 0x2, 0x4)
    OP_29(0x35, 0x2, 0x5)
    OP_29(0x35, 0x2, 0x6)
    OP_29(0x35, 0x2, 0x7)
    OP_29(0x35, 0x2, 0x8)
    OP_29(0x35, 0x2, 0x9)
    OP_29(0x35, 0x2, 0xA)
    OP_29(0x35, 0x2, 0xB)
    OP_29(0x35, 0x2, 0xC)
    OP_29(0x35, 0x2, 0xD)
    OP_29(0x35, 0x2, 0xE)
    OP_29(0x35, 0x2, 0xF)
    OP_29(0x35, 0x2, 0x10)
    OP_29(0x35, 0x2, 0x11)
    OP_29(0x35, 0x2, 0x12)
    OP_29(0x35, 0x2, 0x13)
    OP_29(0x35, 0x2, 0x14)
    OP_29(0x35, 0x2, 0x15)
    OP_29(0x35, 0x2, 0x16)
    OP_29(0x35, 0x2, 0x17)
    OP_29(0x35, 0x2, 0x18)
    OP_29(0x35, 0x2, 0x19)
    OP_29(0x35, 0x2, 0x1A)
    OP_29(0x35, 0x2, 0x1B)
    OP_29(0x35, 0x2, 0x1C)
    OP_29(0x35, 0x2, 0x1D)
    OP_29(0x35, 0x2, 0x1E)
    OP_29(0x35, 0x2, 0x1F)

    label("loc_C4DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C4EF")
    OP_29(0x35, 0x4, 0x2)

    label("loc_C4EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C504")
    OP_29(0x35, 0x1, 0x0)

    label("loc_C504")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C519")
    OP_29(0x35, 0x1, 0x1)

    label("loc_C519")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C52E")
    OP_29(0x35, 0x1, 0x2)

    label("loc_C52E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C543")
    OP_29(0x35, 0x1, 0x3)

    label("loc_C543")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C558")
    OP_29(0x35, 0x1, 0x4)

    label("loc_C558")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C56D")
    OP_29(0x35, 0x1, 0x5)

    label("loc_C56D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C582")
    OP_29(0x35, 0x1, 0x6)

    label("loc_C582")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C597")
    OP_29(0x35, 0x1, 0x7)

    label("loc_C597")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C5AC")
    OP_29(0x35, 0x1, 0x8)

    label("loc_C5AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C5C1")
    OP_29(0x35, 0x1, 0x9)

    label("loc_C5C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C5D6")
    OP_29(0x35, 0x1, 0xA)

    label("loc_C5D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C5EB")
    OP_29(0x35, 0x1, 0xB)

    label("loc_C5EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C5FF")
    OP_29(0x35, 0x4, 0x10)

    label("loc_C5FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C613")
    OP_29(0x35, 0x4, 0x20)

    label("loc_C613")

    Jump("loc_D768")

    label("loc_C618")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C705")
    OP_29(0x5, 0x3, 0x0)
    OP_29(0x5, 0x3, 0x1)
    OP_29(0x5, 0x3, 0x2)
    OP_29(0x5, 0x3, 0x10)
    OP_29(0x5, 0x3, 0x20)
    OP_29(0x5, 0x3, 0x40)
    OP_29(0x5, 0x2, 0x0)
    OP_29(0x5, 0x2, 0x1)
    OP_29(0x5, 0x2, 0x2)
    OP_29(0x5, 0x2, 0x3)
    OP_29(0x5, 0x2, 0x4)
    OP_29(0x5, 0x2, 0x5)
    OP_29(0x5, 0x2, 0x6)
    OP_29(0x5, 0x2, 0x7)
    OP_29(0x5, 0x2, 0x8)
    OP_29(0x5, 0x2, 0x9)
    OP_29(0x5, 0x2, 0xA)
    OP_29(0x5, 0x2, 0xB)
    OP_29(0x5, 0x2, 0xC)
    OP_29(0x5, 0x2, 0xD)
    OP_29(0x5, 0x2, 0xE)
    OP_29(0x5, 0x2, 0xF)
    OP_29(0x5, 0x2, 0x10)
    OP_29(0x5, 0x2, 0x11)
    OP_29(0x5, 0x2, 0x12)
    OP_29(0x5, 0x2, 0x13)
    OP_29(0x5, 0x2, 0x14)
    OP_29(0x5, 0x2, 0x15)
    OP_29(0x5, 0x2, 0x16)
    OP_29(0x5, 0x2, 0x17)
    OP_29(0x5, 0x2, 0x18)
    OP_29(0x5, 0x2, 0x19)
    OP_29(0x5, 0x2, 0x1A)
    OP_29(0x5, 0x2, 0x1B)
    OP_29(0x5, 0x2, 0x1C)
    OP_29(0x5, 0x2, 0x1D)
    OP_29(0x5, 0x2, 0x1E)
    OP_29(0x5, 0x2, 0x1F)

    label("loc_C705")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C719")
    OP_29(0x5, 0x4, 0x2)

    label("loc_C719")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C72E")
    OP_29(0x5, 0x1, 0x0)

    label("loc_C72E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C743")
    OP_29(0x5, 0x1, 0x1)

    label("loc_C743")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C758")
    OP_29(0x5, 0x1, 0x2)

    label("loc_C758")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C76D")
    OP_29(0x5, 0x1, 0x3)

    label("loc_C76D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C782")
    OP_29(0x5, 0x1, 0x4)

    label("loc_C782")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C797")
    OP_29(0x5, 0x1, 0x5)

    label("loc_C797")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C7AC")
    OP_29(0x5, 0x1, 0x6)

    label("loc_C7AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C7C1")
    OP_29(0x5, 0x1, 0x7)

    label("loc_C7C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C7D6")
    OP_29(0x5, 0x1, 0x8)

    label("loc_C7D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C7EB")
    OP_29(0x5, 0x1, 0x9)

    label("loc_C7EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C800")
    OP_29(0x5, 0x1, 0xA)

    label("loc_C800")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C815")
    OP_29(0x5, 0x1, 0xB)

    label("loc_C815")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C829")
    OP_29(0x5, 0x4, 0x10)

    label("loc_C829")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C83D")
    OP_29(0x5, 0x4, 0x20)

    label("loc_C83D")

    Jump("loc_D768")

    label("loc_C842")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C92F")
    OP_29(0x6, 0x3, 0x0)
    OP_29(0x6, 0x3, 0x1)
    OP_29(0x6, 0x3, 0x2)
    OP_29(0x6, 0x3, 0x10)
    OP_29(0x6, 0x3, 0x20)
    OP_29(0x6, 0x3, 0x40)
    OP_29(0x6, 0x2, 0x0)
    OP_29(0x6, 0x2, 0x1)
    OP_29(0x6, 0x2, 0x2)
    OP_29(0x6, 0x2, 0x3)
    OP_29(0x6, 0x2, 0x4)
    OP_29(0x6, 0x2, 0x5)
    OP_29(0x6, 0x2, 0x6)
    OP_29(0x6, 0x2, 0x7)
    OP_29(0x6, 0x2, 0x8)
    OP_29(0x6, 0x2, 0x9)
    OP_29(0x6, 0x2, 0xA)
    OP_29(0x6, 0x2, 0xB)
    OP_29(0x6, 0x2, 0xC)
    OP_29(0x6, 0x2, 0xD)
    OP_29(0x6, 0x2, 0xE)
    OP_29(0x6, 0x2, 0xF)
    OP_29(0x6, 0x2, 0x10)
    OP_29(0x6, 0x2, 0x11)
    OP_29(0x6, 0x2, 0x12)
    OP_29(0x6, 0x2, 0x13)
    OP_29(0x6, 0x2, 0x14)
    OP_29(0x6, 0x2, 0x15)
    OP_29(0x6, 0x2, 0x16)
    OP_29(0x6, 0x2, 0x17)
    OP_29(0x6, 0x2, 0x18)
    OP_29(0x6, 0x2, 0x19)
    OP_29(0x6, 0x2, 0x1A)
    OP_29(0x6, 0x2, 0x1B)
    OP_29(0x6, 0x2, 0x1C)
    OP_29(0x6, 0x2, 0x1D)
    OP_29(0x6, 0x2, 0x1E)
    OP_29(0x6, 0x2, 0x1F)

    label("loc_C92F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C943")
    OP_29(0x6, 0x4, 0x2)

    label("loc_C943")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C958")
    OP_29(0x6, 0x1, 0x0)

    label("loc_C958")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C96D")
    OP_29(0x6, 0x1, 0x1)

    label("loc_C96D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C982")
    OP_29(0x6, 0x1, 0x2)

    label("loc_C982")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C997")
    OP_29(0x6, 0x1, 0x3)

    label("loc_C997")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C9AC")
    OP_29(0x6, 0x1, 0x4)

    label("loc_C9AC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C9C1")
    OP_29(0x6, 0x1, 0x5)

    label("loc_C9C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C9D6")
    OP_29(0x6, 0x1, 0x6)

    label("loc_C9D6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_C9EB")
    OP_29(0x6, 0x1, 0x7)

    label("loc_C9EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CA00")
    OP_29(0x6, 0x1, 0x8)

    label("loc_CA00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CA15")
    OP_29(0x6, 0x1, 0x9)

    label("loc_CA15")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CA2A")
    OP_29(0x6, 0x1, 0xA)

    label("loc_CA2A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CA3F")
    OP_29(0x6, 0x1, 0xB)

    label("loc_CA3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CA53")
    OP_29(0x6, 0x4, 0x10)

    label("loc_CA53")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CA67")
    OP_29(0x6, 0x4, 0x20)

    label("loc_CA67")

    Jump("loc_D768")

    label("loc_CA6C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB59")
    OP_29(0x7, 0x3, 0x0)
    OP_29(0x7, 0x3, 0x1)
    OP_29(0x7, 0x3, 0x2)
    OP_29(0x7, 0x3, 0x10)
    OP_29(0x7, 0x3, 0x20)
    OP_29(0x7, 0x3, 0x40)
    OP_29(0x7, 0x2, 0x0)
    OP_29(0x7, 0x2, 0x1)
    OP_29(0x7, 0x2, 0x2)
    OP_29(0x7, 0x2, 0x3)
    OP_29(0x7, 0x2, 0x4)
    OP_29(0x7, 0x2, 0x5)
    OP_29(0x7, 0x2, 0x6)
    OP_29(0x7, 0x2, 0x7)
    OP_29(0x7, 0x2, 0x8)
    OP_29(0x7, 0x2, 0x9)
    OP_29(0x7, 0x2, 0xA)
    OP_29(0x7, 0x2, 0xB)
    OP_29(0x7, 0x2, 0xC)
    OP_29(0x7, 0x2, 0xD)
    OP_29(0x7, 0x2, 0xE)
    OP_29(0x7, 0x2, 0xF)
    OP_29(0x7, 0x2, 0x10)
    OP_29(0x7, 0x2, 0x11)
    OP_29(0x7, 0x2, 0x12)
    OP_29(0x7, 0x2, 0x13)
    OP_29(0x7, 0x2, 0x14)
    OP_29(0x7, 0x2, 0x15)
    OP_29(0x7, 0x2, 0x16)
    OP_29(0x7, 0x2, 0x17)
    OP_29(0x7, 0x2, 0x18)
    OP_29(0x7, 0x2, 0x19)
    OP_29(0x7, 0x2, 0x1A)
    OP_29(0x7, 0x2, 0x1B)
    OP_29(0x7, 0x2, 0x1C)
    OP_29(0x7, 0x2, 0x1D)
    OP_29(0x7, 0x2, 0x1E)
    OP_29(0x7, 0x2, 0x1F)

    label("loc_CB59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CB6D")
    OP_29(0x7, 0x4, 0x2)

    label("loc_CB6D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CB82")
    OP_29(0x7, 0x1, 0x0)

    label("loc_CB82")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CB97")
    OP_29(0x7, 0x1, 0x1)

    label("loc_CB97")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CBAC")
    OP_29(0x7, 0x1, 0x2)

    label("loc_CBAC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CBC1")
    OP_29(0x7, 0x1, 0x3)

    label("loc_CBC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CBD6")
    OP_29(0x7, 0x1, 0x4)

    label("loc_CBD6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CBEB")
    OP_29(0x7, 0x1, 0x5)

    label("loc_CBEB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CC00")
    OP_29(0x7, 0x1, 0x6)

    label("loc_CC00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CC15")
    OP_29(0x7, 0x1, 0x7)

    label("loc_CC15")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CC2A")
    OP_29(0x7, 0x1, 0x8)

    label("loc_CC2A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CC3F")
    OP_29(0x7, 0x1, 0x9)

    label("loc_CC3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CC54")
    OP_29(0x7, 0x1, 0xA)

    label("loc_CC54")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CC69")
    OP_29(0x7, 0x1, 0xB)

    label("loc_CC69")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CC7D")
    OP_29(0x7, 0x4, 0x10)

    label("loc_CC7D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CC91")
    OP_29(0x7, 0x4, 0x20)

    label("loc_CC91")

    Jump("loc_D768")

    label("loc_CC96")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD83")
    OP_29(0x8, 0x3, 0x0)
    OP_29(0x8, 0x3, 0x1)
    OP_29(0x8, 0x3, 0x2)
    OP_29(0x8, 0x3, 0x10)
    OP_29(0x8, 0x3, 0x20)
    OP_29(0x8, 0x3, 0x40)
    OP_29(0x8, 0x2, 0x0)
    OP_29(0x8, 0x2, 0x1)
    OP_29(0x8, 0x2, 0x2)
    OP_29(0x8, 0x2, 0x3)
    OP_29(0x8, 0x2, 0x4)
    OP_29(0x8, 0x2, 0x5)
    OP_29(0x8, 0x2, 0x6)
    OP_29(0x8, 0x2, 0x7)
    OP_29(0x8, 0x2, 0x8)
    OP_29(0x8, 0x2, 0x9)
    OP_29(0x8, 0x2, 0xA)
    OP_29(0x8, 0x2, 0xB)
    OP_29(0x8, 0x2, 0xC)
    OP_29(0x8, 0x2, 0xD)
    OP_29(0x8, 0x2, 0xE)
    OP_29(0x8, 0x2, 0xF)
    OP_29(0x8, 0x2, 0x10)
    OP_29(0x8, 0x2, 0x11)
    OP_29(0x8, 0x2, 0x12)
    OP_29(0x8, 0x2, 0x13)
    OP_29(0x8, 0x2, 0x14)
    OP_29(0x8, 0x2, 0x15)
    OP_29(0x8, 0x2, 0x16)
    OP_29(0x8, 0x2, 0x17)
    OP_29(0x8, 0x2, 0x18)
    OP_29(0x8, 0x2, 0x19)
    OP_29(0x8, 0x2, 0x1A)
    OP_29(0x8, 0x2, 0x1B)
    OP_29(0x8, 0x2, 0x1C)
    OP_29(0x8, 0x2, 0x1D)
    OP_29(0x8, 0x2, 0x1E)
    OP_29(0x8, 0x2, 0x1F)

    label("loc_CD83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CD97")
    OP_29(0x8, 0x4, 0x2)

    label("loc_CD97")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CDAC")
    OP_29(0x8, 0x1, 0x0)

    label("loc_CDAC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CDC1")
    OP_29(0x8, 0x1, 0x1)

    label("loc_CDC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CDD6")
    OP_29(0x8, 0x1, 0x2)

    label("loc_CDD6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CDEB")
    OP_29(0x8, 0x1, 0x3)

    label("loc_CDEB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CE00")
    OP_29(0x8, 0x1, 0x4)

    label("loc_CE00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CE15")
    OP_29(0x8, 0x1, 0x5)

    label("loc_CE15")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CE2A")
    OP_29(0x8, 0x1, 0x6)

    label("loc_CE2A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CE3F")
    OP_29(0x8, 0x1, 0x7)

    label("loc_CE3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CE54")
    OP_29(0x8, 0x1, 0x8)

    label("loc_CE54")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CE69")
    OP_29(0x8, 0x1, 0x9)

    label("loc_CE69")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CE7E")
    OP_29(0x8, 0x1, 0xA)

    label("loc_CE7E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CE93")
    OP_29(0x8, 0x1, 0xB)

    label("loc_CE93")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CEA7")
    OP_29(0x8, 0x4, 0x10)

    label("loc_CEA7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CEBB")
    OP_29(0x8, 0x4, 0x20)

    label("loc_CEBB")

    Jump("loc_D768")

    label("loc_CEC0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFAD")
    OP_29(0x9, 0x3, 0x0)
    OP_29(0x9, 0x3, 0x1)
    OP_29(0x9, 0x3, 0x2)
    OP_29(0x9, 0x3, 0x10)
    OP_29(0x9, 0x3, 0x20)
    OP_29(0x9, 0x3, 0x40)
    OP_29(0x9, 0x2, 0x0)
    OP_29(0x9, 0x2, 0x1)
    OP_29(0x9, 0x2, 0x2)
    OP_29(0x9, 0x2, 0x3)
    OP_29(0x9, 0x2, 0x4)
    OP_29(0x9, 0x2, 0x5)
    OP_29(0x9, 0x2, 0x6)
    OP_29(0x9, 0x2, 0x7)
    OP_29(0x9, 0x2, 0x8)
    OP_29(0x9, 0x2, 0x9)
    OP_29(0x9, 0x2, 0xA)
    OP_29(0x9, 0x2, 0xB)
    OP_29(0x9, 0x2, 0xC)
    OP_29(0x9, 0x2, 0xD)
    OP_29(0x9, 0x2, 0xE)
    OP_29(0x9, 0x2, 0xF)
    OP_29(0x9, 0x2, 0x10)
    OP_29(0x9, 0x2, 0x11)
    OP_29(0x9, 0x2, 0x12)
    OP_29(0x9, 0x2, 0x13)
    OP_29(0x9, 0x2, 0x14)
    OP_29(0x9, 0x2, 0x15)
    OP_29(0x9, 0x2, 0x16)
    OP_29(0x9, 0x2, 0x17)
    OP_29(0x9, 0x2, 0x18)
    OP_29(0x9, 0x2, 0x19)
    OP_29(0x9, 0x2, 0x1A)
    OP_29(0x9, 0x2, 0x1B)
    OP_29(0x9, 0x2, 0x1C)
    OP_29(0x9, 0x2, 0x1D)
    OP_29(0x9, 0x2, 0x1E)
    OP_29(0x9, 0x2, 0x1F)

    label("loc_CFAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CFC1")
    OP_29(0x9, 0x4, 0x2)

    label("loc_CFC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CFD6")
    OP_29(0x9, 0x1, 0x0)

    label("loc_CFD6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CFEB")
    OP_29(0x9, 0x1, 0x1)

    label("loc_CFEB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D000")
    OP_29(0x9, 0x1, 0x2)

    label("loc_D000")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D015")
    OP_29(0x9, 0x1, 0x3)

    label("loc_D015")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D02A")
    OP_29(0x9, 0x1, 0x4)

    label("loc_D02A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D03F")
    OP_29(0x9, 0x1, 0x5)

    label("loc_D03F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D054")
    OP_29(0x9, 0x1, 0x6)

    label("loc_D054")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D069")
    OP_29(0x9, 0x1, 0x7)

    label("loc_D069")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D07E")
    OP_29(0x9, 0x1, 0x8)

    label("loc_D07E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D093")
    OP_29(0x9, 0x1, 0x9)

    label("loc_D093")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D0A8")
    OP_29(0x9, 0x1, 0xA)

    label("loc_D0A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D0BD")
    OP_29(0x9, 0x1, 0xB)

    label("loc_D0BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D0D1")
    OP_29(0x9, 0x4, 0x10)

    label("loc_D0D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D0E5")
    OP_29(0x9, 0x4, 0x20)

    label("loc_D0E5")

    Jump("loc_D768")

    label("loc_D0EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D1D7")
    OP_29(0xA, 0x3, 0x0)
    OP_29(0xA, 0x3, 0x1)
    OP_29(0xA, 0x3, 0x2)
    OP_29(0xA, 0x3, 0x10)
    OP_29(0xA, 0x3, 0x20)
    OP_29(0xA, 0x3, 0x40)
    OP_29(0xA, 0x2, 0x0)
    OP_29(0xA, 0x2, 0x1)
    OP_29(0xA, 0x2, 0x2)
    OP_29(0xA, 0x2, 0x3)
    OP_29(0xA, 0x2, 0x4)
    OP_29(0xA, 0x2, 0x5)
    OP_29(0xA, 0x2, 0x6)
    OP_29(0xA, 0x2, 0x7)
    OP_29(0xA, 0x2, 0x8)
    OP_29(0xA, 0x2, 0x9)
    OP_29(0xA, 0x2, 0xA)
    OP_29(0xA, 0x2, 0xB)
    OP_29(0xA, 0x2, 0xC)
    OP_29(0xA, 0x2, 0xD)
    OP_29(0xA, 0x2, 0xE)
    OP_29(0xA, 0x2, 0xF)
    OP_29(0xA, 0x2, 0x10)
    OP_29(0xA, 0x2, 0x11)
    OP_29(0xA, 0x2, 0x12)
    OP_29(0xA, 0x2, 0x13)
    OP_29(0xA, 0x2, 0x14)
    OP_29(0xA, 0x2, 0x15)
    OP_29(0xA, 0x2, 0x16)
    OP_29(0xA, 0x2, 0x17)
    OP_29(0xA, 0x2, 0x18)
    OP_29(0xA, 0x2, 0x19)
    OP_29(0xA, 0x2, 0x1A)
    OP_29(0xA, 0x2, 0x1B)
    OP_29(0xA, 0x2, 0x1C)
    OP_29(0xA, 0x2, 0x1D)
    OP_29(0xA, 0x2, 0x1E)
    OP_29(0xA, 0x2, 0x1F)

    label("loc_D1D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D1EB")
    OP_29(0xA, 0x4, 0x2)

    label("loc_D1EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D200")
    OP_29(0xA, 0x1, 0x0)

    label("loc_D200")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D215")
    OP_29(0xA, 0x1, 0x1)

    label("loc_D215")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D22A")
    OP_29(0xA, 0x1, 0x2)

    label("loc_D22A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D23F")
    OP_29(0xA, 0x1, 0x3)

    label("loc_D23F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D254")
    OP_29(0xA, 0x1, 0x4)

    label("loc_D254")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D269")
    OP_29(0xA, 0x1, 0x5)

    label("loc_D269")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D27E")
    OP_29(0xA, 0x1, 0x6)

    label("loc_D27E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D293")
    OP_29(0xA, 0x1, 0x7)

    label("loc_D293")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D2A8")
    OP_29(0xA, 0x1, 0x8)

    label("loc_D2A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D2BD")
    OP_29(0xA, 0x1, 0x9)

    label("loc_D2BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D2D2")
    OP_29(0xA, 0x1, 0xA)

    label("loc_D2D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D2E7")
    OP_29(0xA, 0x1, 0xB)

    label("loc_D2E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D2FB")
    OP_29(0xA, 0x4, 0x10)

    label("loc_D2FB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D30F")
    OP_29(0xA, 0x4, 0x20)

    label("loc_D30F")

    Jump("loc_D768")

    label("loc_D314")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D401")
    OP_29(0xB, 0x3, 0x0)
    OP_29(0xB, 0x3, 0x1)
    OP_29(0xB, 0x3, 0x2)
    OP_29(0xB, 0x3, 0x10)
    OP_29(0xB, 0x3, 0x20)
    OP_29(0xB, 0x3, 0x40)
    OP_29(0xB, 0x2, 0x0)
    OP_29(0xB, 0x2, 0x1)
    OP_29(0xB, 0x2, 0x2)
    OP_29(0xB, 0x2, 0x3)
    OP_29(0xB, 0x2, 0x4)
    OP_29(0xB, 0x2, 0x5)
    OP_29(0xB, 0x2, 0x6)
    OP_29(0xB, 0x2, 0x7)
    OP_29(0xB, 0x2, 0x8)
    OP_29(0xB, 0x2, 0x9)
    OP_29(0xB, 0x2, 0xA)
    OP_29(0xB, 0x2, 0xB)
    OP_29(0xB, 0x2, 0xC)
    OP_29(0xB, 0x2, 0xD)
    OP_29(0xB, 0x2, 0xE)
    OP_29(0xB, 0x2, 0xF)
    OP_29(0xB, 0x2, 0x10)
    OP_29(0xB, 0x2, 0x11)
    OP_29(0xB, 0x2, 0x12)
    OP_29(0xB, 0x2, 0x13)
    OP_29(0xB, 0x2, 0x14)
    OP_29(0xB, 0x2, 0x15)
    OP_29(0xB, 0x2, 0x16)
    OP_29(0xB, 0x2, 0x17)
    OP_29(0xB, 0x2, 0x18)
    OP_29(0xB, 0x2, 0x19)
    OP_29(0xB, 0x2, 0x1A)
    OP_29(0xB, 0x2, 0x1B)
    OP_29(0xB, 0x2, 0x1C)
    OP_29(0xB, 0x2, 0x1D)
    OP_29(0xB, 0x2, 0x1E)
    OP_29(0xB, 0x2, 0x1F)

    label("loc_D401")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D415")
    OP_29(0xB, 0x4, 0x2)

    label("loc_D415")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D42A")
    OP_29(0xB, 0x1, 0x0)

    label("loc_D42A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D43F")
    OP_29(0xB, 0x1, 0x1)

    label("loc_D43F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D454")
    OP_29(0xB, 0x1, 0x2)

    label("loc_D454")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D469")
    OP_29(0xB, 0x1, 0x3)

    label("loc_D469")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D47E")
    OP_29(0xB, 0x1, 0x4)

    label("loc_D47E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D493")
    OP_29(0xB, 0x1, 0x5)

    label("loc_D493")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D4A8")
    OP_29(0xB, 0x1, 0x6)

    label("loc_D4A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D4BD")
    OP_29(0xB, 0x1, 0x7)

    label("loc_D4BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D4D2")
    OP_29(0xB, 0x1, 0x8)

    label("loc_D4D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D4E7")
    OP_29(0xB, 0x1, 0x9)

    label("loc_D4E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D4FC")
    OP_29(0xB, 0x1, 0xA)

    label("loc_D4FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D511")
    OP_29(0xB, 0x1, 0xB)

    label("loc_D511")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D525")
    OP_29(0xB, 0x4, 0x10)

    label("loc_D525")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D539")
    OP_29(0xB, 0x4, 0x20)

    label("loc_D539")

    Jump("loc_D768")

    label("loc_D53E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D62B")
    OP_29(0xC, 0x3, 0x0)
    OP_29(0xC, 0x3, 0x1)
    OP_29(0xC, 0x3, 0x2)
    OP_29(0xC, 0x3, 0x10)
    OP_29(0xC, 0x3, 0x20)
    OP_29(0xC, 0x3, 0x40)
    OP_29(0xC, 0x2, 0x0)
    OP_29(0xC, 0x2, 0x1)
    OP_29(0xC, 0x2, 0x2)
    OP_29(0xC, 0x2, 0x3)
    OP_29(0xC, 0x2, 0x4)
    OP_29(0xC, 0x2, 0x5)
    OP_29(0xC, 0x2, 0x6)
    OP_29(0xC, 0x2, 0x7)
    OP_29(0xC, 0x2, 0x8)
    OP_29(0xC, 0x2, 0x9)
    OP_29(0xC, 0x2, 0xA)
    OP_29(0xC, 0x2, 0xB)
    OP_29(0xC, 0x2, 0xC)
    OP_29(0xC, 0x2, 0xD)
    OP_29(0xC, 0x2, 0xE)
    OP_29(0xC, 0x2, 0xF)
    OP_29(0xC, 0x2, 0x10)
    OP_29(0xC, 0x2, 0x11)
    OP_29(0xC, 0x2, 0x12)
    OP_29(0xC, 0x2, 0x13)
    OP_29(0xC, 0x2, 0x14)
    OP_29(0xC, 0x2, 0x15)
    OP_29(0xC, 0x2, 0x16)
    OP_29(0xC, 0x2, 0x17)
    OP_29(0xC, 0x2, 0x18)
    OP_29(0xC, 0x2, 0x19)
    OP_29(0xC, 0x2, 0x1A)
    OP_29(0xC, 0x2, 0x1B)
    OP_29(0xC, 0x2, 0x1C)
    OP_29(0xC, 0x2, 0x1D)
    OP_29(0xC, 0x2, 0x1E)
    OP_29(0xC, 0x2, 0x1F)

    label("loc_D62B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D63F")
    OP_29(0xC, 0x4, 0x2)

    label("loc_D63F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D654")
    OP_29(0xC, 0x1, 0x0)

    label("loc_D654")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D669")
    OP_29(0xC, 0x1, 0x1)

    label("loc_D669")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D67E")
    OP_29(0xC, 0x1, 0x2)

    label("loc_D67E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D693")
    OP_29(0xC, 0x1, 0x3)

    label("loc_D693")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D6A8")
    OP_29(0xC, 0x1, 0x4)

    label("loc_D6A8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D6BD")
    OP_29(0xC, 0x1, 0x5)

    label("loc_D6BD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D6D2")
    OP_29(0xC, 0x1, 0x6)

    label("loc_D6D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D6E7")
    OP_29(0xC, 0x1, 0x7)

    label("loc_D6E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D6FC")
    OP_29(0xC, 0x1, 0x8)

    label("loc_D6FC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D711")
    OP_29(0xC, 0x1, 0x9)

    label("loc_D711")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D726")
    OP_29(0xC, 0x1, 0xA)

    label("loc_D726")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D73B")
    OP_29(0xC, 0x1, 0xB)

    label("loc_D73B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D74F")
    OP_29(0xC, 0x4, 0x10)

    label("loc_D74F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D763")
    OP_29(0xC, 0x4, 0x20)

    label("loc_D763")

    Jump("loc_D768")

    label("loc_D768")

    Jump("loc_B812")

    label("loc_D76D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_55_B808 end

    def Function_56_D785(): pass

    label("Function_56_D785")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D78F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ED8C")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "----------２章--------------\x01",        # 0
            "QS_0201  古道私有地の魔獣退治 \x01",      # 1
            "QS_0202  エニグマの実戦テスト \x01",      # 2
            "QS_0203  タングラム門での演習 \x01",      # 3
            "QS_0204  手配魔獣③           \x01",      # 4
            "QS_0205  魚料理の食材集め     \x01",      # 5
            "QS_0206  不良たちとの手合わせ \x01",      # 6
            "QS_0207  ラゴー教授の手伝い   \x01",      # 7
            "QS_0208  手配魔獣④           \x01",      # 8
            "QS_0209  失くした結婚指輪     \x01",      # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (3, "loc_D91E"),
        (7, "loc_D9CF"),
        (1, "loc_DA6E"),
        (2, "loc_DA6E"),
        (4, "loc_DA6E"),
        (5, "loc_DA6E"),
        (6, "loc_DA6E"),
        (8, "loc_DA6E"),
        (9, "loc_DA6E"),
        (SWITCH_DEFAULT, "loc_DAE7"),
    )


    label("loc_D91E")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期化\x01",                     # 0
            "開始\x01",                       # 1
            "QF_01\x09",                      # 2
            "★01 依頼内容を聞いた\x01",      # 3
            "QF_02\x09",                      # 4
            "★02 １戦目で負けた\x01",        # 5
            "QF_03\x09",                      # 6
            "★03 ２戦目で負けた\x01",        # 7
            "QF_04\x09",                      # 8
            "★04 全て勝利した\x01",          # 9
            "QF_05\x09",                      # 10
            "★05 達成イベント\x01",          # 11
            "達成\x01",                       # 12
            "報告\x01",                       # 13
        )
    )

    MenuEnd(0x5)
    Jump("loc_DAF6")

    label("loc_D9CF")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期化\x01",                         # 0
            "開始\x01",                           # 1
            "QF_01\x09",                          # 2
            "★01 依頼内容を聞いた\x01",          # 3
            "QF_02\x09",                          # 4
            "★02 大司教と話した\x01",            # 5
            "QF_03\x09",                          # 6
            "★03 ルピナス草を入手した\x01",      # 7
            "QF_04\x09",                          # 8
            "★04 達成イベント\x01",              # 9
            "達成\x01",                           # 10
            "報告\x01",                           # 11
        )
    )

    MenuEnd(0x5)
    Jump("loc_DAF6")

    label("loc_DA6E")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期化\x01",      # 0
            "開始\x01",        # 1
            "QF_01\x01",       # 2
            "QF_02\x01",       # 3
            "QF_03\x01",       # 4
            "QF_04\x01",       # 5
            "QF_05\x01",       # 6
            "QF_06\x01",       # 7
            "QF_07\x01",       # 8
            "QF_08\x01",       # 9
            "QF_09\x01",       # 10
            "QF_10\x01",       # 11
            "QF_11\x01",       # 12
            "QF_12\x01",       # 13
            "達成\x01",        # 14
            "報告\x01",        # 15
        )
    )

    MenuEnd(0x5)
    Jump("loc_DAF6")

    label("loc_DAE7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_DAF6")

    label("loc_DAF6")

    OP_60(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ED87")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_DB48"),
        (2, "loc_DD72"),
        (3, "loc_DF9C"),
        (4, "loc_E133"),
        (5, "loc_E35D"),
        (6, "loc_E587"),
        (7, "loc_E7B1"),
        (8, "loc_E933"),
        (9, "loc_EB5D"),
        (SWITCH_DEFAULT, "loc_ED87"),
    )


    label("loc_DB48")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC35")
    OP_29(0xD, 0x3, 0x0)
    OP_29(0xD, 0x3, 0x1)
    OP_29(0xD, 0x3, 0x2)
    OP_29(0xD, 0x3, 0x10)
    OP_29(0xD, 0x3, 0x20)
    OP_29(0xD, 0x3, 0x40)
    OP_29(0xD, 0x2, 0x0)
    OP_29(0xD, 0x2, 0x1)
    OP_29(0xD, 0x2, 0x2)
    OP_29(0xD, 0x2, 0x3)
    OP_29(0xD, 0x2, 0x4)
    OP_29(0xD, 0x2, 0x5)
    OP_29(0xD, 0x2, 0x6)
    OP_29(0xD, 0x2, 0x7)
    OP_29(0xD, 0x2, 0x8)
    OP_29(0xD, 0x2, 0x9)
    OP_29(0xD, 0x2, 0xA)
    OP_29(0xD, 0x2, 0xB)
    OP_29(0xD, 0x2, 0xC)
    OP_29(0xD, 0x2, 0xD)
    OP_29(0xD, 0x2, 0xE)
    OP_29(0xD, 0x2, 0xF)
    OP_29(0xD, 0x2, 0x10)
    OP_29(0xD, 0x2, 0x11)
    OP_29(0xD, 0x2, 0x12)
    OP_29(0xD, 0x2, 0x13)
    OP_29(0xD, 0x2, 0x14)
    OP_29(0xD, 0x2, 0x15)
    OP_29(0xD, 0x2, 0x16)
    OP_29(0xD, 0x2, 0x17)
    OP_29(0xD, 0x2, 0x18)
    OP_29(0xD, 0x2, 0x19)
    OP_29(0xD, 0x2, 0x1A)
    OP_29(0xD, 0x2, 0x1B)
    OP_29(0xD, 0x2, 0x1C)
    OP_29(0xD, 0x2, 0x1D)
    OP_29(0xD, 0x2, 0x1E)
    OP_29(0xD, 0x2, 0x1F)

    label("loc_DC35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DC49")
    OP_29(0xD, 0x4, 0x2)

    label("loc_DC49")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DC5E")
    OP_29(0xD, 0x1, 0x0)

    label("loc_DC5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DC73")
    OP_29(0xD, 0x1, 0x1)

    label("loc_DC73")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DC88")
    OP_29(0xD, 0x1, 0x2)

    label("loc_DC88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DC9D")
    OP_29(0xD, 0x1, 0x3)

    label("loc_DC9D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DCB2")
    OP_29(0xD, 0x1, 0x4)

    label("loc_DCB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DCC7")
    OP_29(0xD, 0x1, 0x5)

    label("loc_DCC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DCDC")
    OP_29(0xD, 0x1, 0x6)

    label("loc_DCDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DCF1")
    OP_29(0xD, 0x1, 0x7)

    label("loc_DCF1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DD06")
    OP_29(0xD, 0x1, 0x8)

    label("loc_DD06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DD1B")
    OP_29(0xD, 0x1, 0x9)

    label("loc_DD1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DD30")
    OP_29(0xD, 0x1, 0xA)

    label("loc_DD30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DD45")
    OP_29(0xD, 0x1, 0xB)

    label("loc_DD45")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DD59")
    OP_29(0xD, 0x4, 0x10)

    label("loc_DD59")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DD6D")
    OP_29(0xD, 0x4, 0x20)

    label("loc_DD6D")

    Jump("loc_ED87")

    label("loc_DD72")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE5F")
    OP_29(0xE, 0x3, 0x0)
    OP_29(0xE, 0x3, 0x1)
    OP_29(0xE, 0x3, 0x2)
    OP_29(0xE, 0x3, 0x10)
    OP_29(0xE, 0x3, 0x20)
    OP_29(0xE, 0x3, 0x40)
    OP_29(0xE, 0x2, 0x0)
    OP_29(0xE, 0x2, 0x1)
    OP_29(0xE, 0x2, 0x2)
    OP_29(0xE, 0x2, 0x3)
    OP_29(0xE, 0x2, 0x4)
    OP_29(0xE, 0x2, 0x5)
    OP_29(0xE, 0x2, 0x6)
    OP_29(0xE, 0x2, 0x7)
    OP_29(0xE, 0x2, 0x8)
    OP_29(0xE, 0x2, 0x9)
    OP_29(0xE, 0x2, 0xA)
    OP_29(0xE, 0x2, 0xB)
    OP_29(0xE, 0x2, 0xC)
    OP_29(0xE, 0x2, 0xD)
    OP_29(0xE, 0x2, 0xE)
    OP_29(0xE, 0x2, 0xF)
    OP_29(0xE, 0x2, 0x10)
    OP_29(0xE, 0x2, 0x11)
    OP_29(0xE, 0x2, 0x12)
    OP_29(0xE, 0x2, 0x13)
    OP_29(0xE, 0x2, 0x14)
    OP_29(0xE, 0x2, 0x15)
    OP_29(0xE, 0x2, 0x16)
    OP_29(0xE, 0x2, 0x17)
    OP_29(0xE, 0x2, 0x18)
    OP_29(0xE, 0x2, 0x19)
    OP_29(0xE, 0x2, 0x1A)
    OP_29(0xE, 0x2, 0x1B)
    OP_29(0xE, 0x2, 0x1C)
    OP_29(0xE, 0x2, 0x1D)
    OP_29(0xE, 0x2, 0x1E)
    OP_29(0xE, 0x2, 0x1F)

    label("loc_DE5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DE73")
    OP_29(0xE, 0x4, 0x2)

    label("loc_DE73")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DE88")
    OP_29(0xE, 0x1, 0x0)

    label("loc_DE88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DE9D")
    OP_29(0xE, 0x1, 0x1)

    label("loc_DE9D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DEB2")
    OP_29(0xE, 0x1, 0x2)

    label("loc_DEB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DEC7")
    OP_29(0xE, 0x1, 0x3)

    label("loc_DEC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DEDC")
    OP_29(0xE, 0x1, 0x4)

    label("loc_DEDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DEF1")
    OP_29(0xE, 0x1, 0x5)

    label("loc_DEF1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DF06")
    OP_29(0xE, 0x1, 0x6)

    label("loc_DF06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DF1B")
    OP_29(0xE, 0x1, 0x7)

    label("loc_DF1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DF30")
    OP_29(0xE, 0x1, 0x8)

    label("loc_DF30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DF45")
    OP_29(0xE, 0x1, 0x9)

    label("loc_DF45")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DF5A")
    OP_29(0xE, 0x1, 0xA)

    label("loc_DF5A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DF6F")
    OP_29(0xE, 0x1, 0xB)

    label("loc_DF6F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DF83")
    OP_29(0xE, 0x4, 0x10)

    label("loc_DF83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_DF97")
    OP_29(0xE, 0x4, 0x20)

    label("loc_DF97")

    Jump("loc_ED87")

    label("loc_DF9C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E089")
    OP_29(0xF, 0x3, 0x0)
    OP_29(0xF, 0x3, 0x1)
    OP_29(0xF, 0x3, 0x2)
    OP_29(0xF, 0x3, 0x10)
    OP_29(0xF, 0x3, 0x20)
    OP_29(0xF, 0x3, 0x40)
    OP_29(0xF, 0x2, 0x0)
    OP_29(0xF, 0x2, 0x1)
    OP_29(0xF, 0x2, 0x2)
    OP_29(0xF, 0x2, 0x3)
    OP_29(0xF, 0x2, 0x4)
    OP_29(0xF, 0x2, 0x5)
    OP_29(0xF, 0x2, 0x6)
    OP_29(0xF, 0x2, 0x7)
    OP_29(0xF, 0x2, 0x8)
    OP_29(0xF, 0x2, 0x9)
    OP_29(0xF, 0x2, 0xA)
    OP_29(0xF, 0x2, 0xB)
    OP_29(0xF, 0x2, 0xC)
    OP_29(0xF, 0x2, 0xD)
    OP_29(0xF, 0x2, 0xE)
    OP_29(0xF, 0x2, 0xF)
    OP_29(0xF, 0x2, 0x10)
    OP_29(0xF, 0x2, 0x11)
    OP_29(0xF, 0x2, 0x12)
    OP_29(0xF, 0x2, 0x13)
    OP_29(0xF, 0x2, 0x14)
    OP_29(0xF, 0x2, 0x15)
    OP_29(0xF, 0x2, 0x16)
    OP_29(0xF, 0x2, 0x17)
    OP_29(0xF, 0x2, 0x18)
    OP_29(0xF, 0x2, 0x19)
    OP_29(0xF, 0x2, 0x1A)
    OP_29(0xF, 0x2, 0x1B)
    OP_29(0xF, 0x2, 0x1C)
    OP_29(0xF, 0x2, 0x1D)
    OP_29(0xF, 0x2, 0x1E)
    OP_29(0xF, 0x2, 0x1F)

    label("loc_E089")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E09D")
    OP_29(0xF, 0x4, 0x2)

    label("loc_E09D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E0B2")
    OP_29(0xF, 0x1, 0x0)

    label("loc_E0B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E0C7")
    OP_29(0xF, 0x1, 0x1)

    label("loc_E0C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E0DC")
    OP_29(0xF, 0x1, 0x2)

    label("loc_E0DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E0F1")
    OP_29(0xF, 0x1, 0x3)

    label("loc_E0F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E106")
    OP_29(0xF, 0x1, 0x4)

    label("loc_E106")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E11A")
    OP_29(0xF, 0x4, 0x10)

    label("loc_E11A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E12E")
    OP_29(0xF, 0x4, 0x20)

    label("loc_E12E")

    Jump("loc_ED87")

    label("loc_E133")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E220")
    OP_29(0x10, 0x3, 0x0)
    OP_29(0x10, 0x3, 0x1)
    OP_29(0x10, 0x3, 0x2)
    OP_29(0x10, 0x3, 0x10)
    OP_29(0x10, 0x3, 0x20)
    OP_29(0x10, 0x3, 0x40)
    OP_29(0x10, 0x2, 0x0)
    OP_29(0x10, 0x2, 0x1)
    OP_29(0x10, 0x2, 0x2)
    OP_29(0x10, 0x2, 0x3)
    OP_29(0x10, 0x2, 0x4)
    OP_29(0x10, 0x2, 0x5)
    OP_29(0x10, 0x2, 0x6)
    OP_29(0x10, 0x2, 0x7)
    OP_29(0x10, 0x2, 0x8)
    OP_29(0x10, 0x2, 0x9)
    OP_29(0x10, 0x2, 0xA)
    OP_29(0x10, 0x2, 0xB)
    OP_29(0x10, 0x2, 0xC)
    OP_29(0x10, 0x2, 0xD)
    OP_29(0x10, 0x2, 0xE)
    OP_29(0x10, 0x2, 0xF)
    OP_29(0x10, 0x2, 0x10)
    OP_29(0x10, 0x2, 0x11)
    OP_29(0x10, 0x2, 0x12)
    OP_29(0x10, 0x2, 0x13)
    OP_29(0x10, 0x2, 0x14)
    OP_29(0x10, 0x2, 0x15)
    OP_29(0x10, 0x2, 0x16)
    OP_29(0x10, 0x2, 0x17)
    OP_29(0x10, 0x2, 0x18)
    OP_29(0x10, 0x2, 0x19)
    OP_29(0x10, 0x2, 0x1A)
    OP_29(0x10, 0x2, 0x1B)
    OP_29(0x10, 0x2, 0x1C)
    OP_29(0x10, 0x2, 0x1D)
    OP_29(0x10, 0x2, 0x1E)
    OP_29(0x10, 0x2, 0x1F)

    label("loc_E220")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E234")
    OP_29(0x10, 0x4, 0x2)

    label("loc_E234")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E249")
    OP_29(0x10, 0x1, 0x0)

    label("loc_E249")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E25E")
    OP_29(0x10, 0x1, 0x1)

    label("loc_E25E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E273")
    OP_29(0x10, 0x1, 0x2)

    label("loc_E273")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E288")
    OP_29(0x10, 0x1, 0x3)

    label("loc_E288")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E29D")
    OP_29(0x10, 0x1, 0x4)

    label("loc_E29D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E2B2")
    OP_29(0x10, 0x1, 0x5)

    label("loc_E2B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E2C7")
    OP_29(0x10, 0x1, 0x6)

    label("loc_E2C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E2DC")
    OP_29(0x10, 0x1, 0x7)

    label("loc_E2DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E2F1")
    OP_29(0x10, 0x1, 0x8)

    label("loc_E2F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E306")
    OP_29(0x10, 0x1, 0x9)

    label("loc_E306")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E31B")
    OP_29(0x10, 0x1, 0xA)

    label("loc_E31B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E330")
    OP_29(0x10, 0x1, 0xB)

    label("loc_E330")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E344")
    OP_29(0x10, 0x4, 0x10)

    label("loc_E344")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E358")
    OP_29(0x10, 0x4, 0x20)

    label("loc_E358")

    Jump("loc_ED87")

    label("loc_E35D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E44A")
    OP_29(0x11, 0x3, 0x0)
    OP_29(0x11, 0x3, 0x1)
    OP_29(0x11, 0x3, 0x2)
    OP_29(0x11, 0x3, 0x10)
    OP_29(0x11, 0x3, 0x20)
    OP_29(0x11, 0x3, 0x40)
    OP_29(0x11, 0x2, 0x0)
    OP_29(0x11, 0x2, 0x1)
    OP_29(0x11, 0x2, 0x2)
    OP_29(0x11, 0x2, 0x3)
    OP_29(0x11, 0x2, 0x4)
    OP_29(0x11, 0x2, 0x5)
    OP_29(0x11, 0x2, 0x6)
    OP_29(0x11, 0x2, 0x7)
    OP_29(0x11, 0x2, 0x8)
    OP_29(0x11, 0x2, 0x9)
    OP_29(0x11, 0x2, 0xA)
    OP_29(0x11, 0x2, 0xB)
    OP_29(0x11, 0x2, 0xC)
    OP_29(0x11, 0x2, 0xD)
    OP_29(0x11, 0x2, 0xE)
    OP_29(0x11, 0x2, 0xF)
    OP_29(0x11, 0x2, 0x10)
    OP_29(0x11, 0x2, 0x11)
    OP_29(0x11, 0x2, 0x12)
    OP_29(0x11, 0x2, 0x13)
    OP_29(0x11, 0x2, 0x14)
    OP_29(0x11, 0x2, 0x15)
    OP_29(0x11, 0x2, 0x16)
    OP_29(0x11, 0x2, 0x17)
    OP_29(0x11, 0x2, 0x18)
    OP_29(0x11, 0x2, 0x19)
    OP_29(0x11, 0x2, 0x1A)
    OP_29(0x11, 0x2, 0x1B)
    OP_29(0x11, 0x2, 0x1C)
    OP_29(0x11, 0x2, 0x1D)
    OP_29(0x11, 0x2, 0x1E)
    OP_29(0x11, 0x2, 0x1F)

    label("loc_E44A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E45E")
    OP_29(0x11, 0x4, 0x2)

    label("loc_E45E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E473")
    OP_29(0x11, 0x1, 0x0)

    label("loc_E473")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E488")
    OP_29(0x11, 0x1, 0x1)

    label("loc_E488")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E49D")
    OP_29(0x11, 0x1, 0x2)

    label("loc_E49D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E4B2")
    OP_29(0x11, 0x1, 0x3)

    label("loc_E4B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E4C7")
    OP_29(0x11, 0x1, 0x4)

    label("loc_E4C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E4DC")
    OP_29(0x11, 0x1, 0x5)

    label("loc_E4DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E4F1")
    OP_29(0x11, 0x1, 0x6)

    label("loc_E4F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E506")
    OP_29(0x11, 0x1, 0x7)

    label("loc_E506")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E51B")
    OP_29(0x11, 0x1, 0x8)

    label("loc_E51B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E530")
    OP_29(0x11, 0x1, 0x9)

    label("loc_E530")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E545")
    OP_29(0x11, 0x1, 0xA)

    label("loc_E545")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E55A")
    OP_29(0x11, 0x1, 0xB)

    label("loc_E55A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E56E")
    OP_29(0x11, 0x4, 0x10)

    label("loc_E56E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E582")
    OP_29(0x11, 0x4, 0x20)

    label("loc_E582")

    Jump("loc_ED87")

    label("loc_E587")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E674")
    OP_29(0x12, 0x3, 0x0)
    OP_29(0x12, 0x3, 0x1)
    OP_29(0x12, 0x3, 0x2)
    OP_29(0x12, 0x3, 0x10)
    OP_29(0x12, 0x3, 0x20)
    OP_29(0x12, 0x3, 0x40)
    OP_29(0x12, 0x2, 0x0)
    OP_29(0x12, 0x2, 0x1)
    OP_29(0x12, 0x2, 0x2)
    OP_29(0x12, 0x2, 0x3)
    OP_29(0x12, 0x2, 0x4)
    OP_29(0x12, 0x2, 0x5)
    OP_29(0x12, 0x2, 0x6)
    OP_29(0x12, 0x2, 0x7)
    OP_29(0x12, 0x2, 0x8)
    OP_29(0x12, 0x2, 0x9)
    OP_29(0x12, 0x2, 0xA)
    OP_29(0x12, 0x2, 0xB)
    OP_29(0x12, 0x2, 0xC)
    OP_29(0x12, 0x2, 0xD)
    OP_29(0x12, 0x2, 0xE)
    OP_29(0x12, 0x2, 0xF)
    OP_29(0x12, 0x2, 0x10)
    OP_29(0x12, 0x2, 0x11)
    OP_29(0x12, 0x2, 0x12)
    OP_29(0x12, 0x2, 0x13)
    OP_29(0x12, 0x2, 0x14)
    OP_29(0x12, 0x2, 0x15)
    OP_29(0x12, 0x2, 0x16)
    OP_29(0x12, 0x2, 0x17)
    OP_29(0x12, 0x2, 0x18)
    OP_29(0x12, 0x2, 0x19)
    OP_29(0x12, 0x2, 0x1A)
    OP_29(0x12, 0x2, 0x1B)
    OP_29(0x12, 0x2, 0x1C)
    OP_29(0x12, 0x2, 0x1D)
    OP_29(0x12, 0x2, 0x1E)
    OP_29(0x12, 0x2, 0x1F)

    label("loc_E674")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E688")
    OP_29(0x12, 0x4, 0x2)

    label("loc_E688")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E69D")
    OP_29(0x12, 0x1, 0x0)

    label("loc_E69D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E6B2")
    OP_29(0x12, 0x1, 0x1)

    label("loc_E6B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E6C7")
    OP_29(0x12, 0x1, 0x2)

    label("loc_E6C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E6DC")
    OP_29(0x12, 0x1, 0x3)

    label("loc_E6DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E6F1")
    OP_29(0x12, 0x1, 0x4)

    label("loc_E6F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E706")
    OP_29(0x12, 0x1, 0x5)

    label("loc_E706")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E71B")
    OP_29(0x12, 0x1, 0x6)

    label("loc_E71B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E730")
    OP_29(0x12, 0x1, 0x7)

    label("loc_E730")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E745")
    OP_29(0x12, 0x1, 0x8)

    label("loc_E745")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E75A")
    OP_29(0x12, 0x1, 0x9)

    label("loc_E75A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E76F")
    OP_29(0x12, 0x1, 0xA)

    label("loc_E76F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E784")
    OP_29(0x12, 0x1, 0xB)

    label("loc_E784")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E798")
    OP_29(0x12, 0x4, 0x10)

    label("loc_E798")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E7AC")
    OP_29(0x12, 0x4, 0x20)

    label("loc_E7AC")

    Jump("loc_ED87")

    label("loc_E7B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E89E")
    OP_29(0x13, 0x3, 0x0)
    OP_29(0x13, 0x3, 0x1)
    OP_29(0x13, 0x3, 0x2)
    OP_29(0x13, 0x3, 0x10)
    OP_29(0x13, 0x3, 0x20)
    OP_29(0x13, 0x3, 0x40)
    OP_29(0x13, 0x2, 0x0)
    OP_29(0x13, 0x2, 0x1)
    OP_29(0x13, 0x2, 0x2)
    OP_29(0x13, 0x2, 0x3)
    OP_29(0x13, 0x2, 0x4)
    OP_29(0x13, 0x2, 0x5)
    OP_29(0x13, 0x2, 0x6)
    OP_29(0x13, 0x2, 0x7)
    OP_29(0x13, 0x2, 0x8)
    OP_29(0x13, 0x2, 0x9)
    OP_29(0x13, 0x2, 0xA)
    OP_29(0x13, 0x2, 0xB)
    OP_29(0x13, 0x2, 0xC)
    OP_29(0x13, 0x2, 0xD)
    OP_29(0x13, 0x2, 0xE)
    OP_29(0x13, 0x2, 0xF)
    OP_29(0x13, 0x2, 0x10)
    OP_29(0x13, 0x2, 0x11)
    OP_29(0x13, 0x2, 0x12)
    OP_29(0x13, 0x2, 0x13)
    OP_29(0x13, 0x2, 0x14)
    OP_29(0x13, 0x2, 0x15)
    OP_29(0x13, 0x2, 0x16)
    OP_29(0x13, 0x2, 0x17)
    OP_29(0x13, 0x2, 0x18)
    OP_29(0x13, 0x2, 0x19)
    OP_29(0x13, 0x2, 0x1A)
    OP_29(0x13, 0x2, 0x1B)
    OP_29(0x13, 0x2, 0x1C)
    OP_29(0x13, 0x2, 0x1D)
    OP_29(0x13, 0x2, 0x1E)
    OP_29(0x13, 0x2, 0x1F)

    label("loc_E89E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E8B2")
    OP_29(0x13, 0x4, 0x2)

    label("loc_E8B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E8C7")
    OP_29(0x13, 0x1, 0x0)

    label("loc_E8C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E8DC")
    OP_29(0x13, 0x1, 0x1)

    label("loc_E8DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E8F1")
    OP_29(0x13, 0x1, 0x2)

    label("loc_E8F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E906")
    OP_29(0x13, 0x1, 0x3)

    label("loc_E906")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E91A")
    OP_29(0x13, 0x4, 0x10)

    label("loc_E91A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_E92E")
    OP_29(0x13, 0x4, 0x20)

    label("loc_E92E")

    Jump("loc_ED87")

    label("loc_E933")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EA20")
    OP_29(0x14, 0x3, 0x0)
    OP_29(0x14, 0x3, 0x1)
    OP_29(0x14, 0x3, 0x2)
    OP_29(0x14, 0x3, 0x10)
    OP_29(0x14, 0x3, 0x20)
    OP_29(0x14, 0x3, 0x40)
    OP_29(0x14, 0x2, 0x0)
    OP_29(0x14, 0x2, 0x1)
    OP_29(0x14, 0x2, 0x2)
    OP_29(0x14, 0x2, 0x3)
    OP_29(0x14, 0x2, 0x4)
    OP_29(0x14, 0x2, 0x5)
    OP_29(0x14, 0x2, 0x6)
    OP_29(0x14, 0x2, 0x7)
    OP_29(0x14, 0x2, 0x8)
    OP_29(0x14, 0x2, 0x9)
    OP_29(0x14, 0x2, 0xA)
    OP_29(0x14, 0x2, 0xB)
    OP_29(0x14, 0x2, 0xC)
    OP_29(0x14, 0x2, 0xD)
    OP_29(0x14, 0x2, 0xE)
    OP_29(0x14, 0x2, 0xF)
    OP_29(0x14, 0x2, 0x10)
    OP_29(0x14, 0x2, 0x11)
    OP_29(0x14, 0x2, 0x12)
    OP_29(0x14, 0x2, 0x13)
    OP_29(0x14, 0x2, 0x14)
    OP_29(0x14, 0x2, 0x15)
    OP_29(0x14, 0x2, 0x16)
    OP_29(0x14, 0x2, 0x17)
    OP_29(0x14, 0x2, 0x18)
    OP_29(0x14, 0x2, 0x19)
    OP_29(0x14, 0x2, 0x1A)
    OP_29(0x14, 0x2, 0x1B)
    OP_29(0x14, 0x2, 0x1C)
    OP_29(0x14, 0x2, 0x1D)
    OP_29(0x14, 0x2, 0x1E)
    OP_29(0x14, 0x2, 0x1F)

    label("loc_EA20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EA34")
    OP_29(0x14, 0x4, 0x2)

    label("loc_EA34")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EA49")
    OP_29(0x14, 0x1, 0x0)

    label("loc_EA49")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EA5E")
    OP_29(0x14, 0x1, 0x1)

    label("loc_EA5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EA73")
    OP_29(0x14, 0x1, 0x2)

    label("loc_EA73")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EA88")
    OP_29(0x14, 0x1, 0x3)

    label("loc_EA88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EA9D")
    OP_29(0x14, 0x1, 0x4)

    label("loc_EA9D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EAB2")
    OP_29(0x14, 0x1, 0x5)

    label("loc_EAB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EAC7")
    OP_29(0x14, 0x1, 0x6)

    label("loc_EAC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EADC")
    OP_29(0x14, 0x1, 0x7)

    label("loc_EADC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EAF1")
    OP_29(0x14, 0x1, 0x8)

    label("loc_EAF1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EB06")
    OP_29(0x14, 0x1, 0x9)

    label("loc_EB06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EB1B")
    OP_29(0x14, 0x1, 0xA)

    label("loc_EB1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EB30")
    OP_29(0x14, 0x1, 0xB)

    label("loc_EB30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EB44")
    OP_29(0x14, 0x4, 0x10)

    label("loc_EB44")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EB58")
    OP_29(0x14, 0x4, 0x20)

    label("loc_EB58")

    Jump("loc_ED87")

    label("loc_EB5D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC4A")
    OP_29(0x15, 0x3, 0x0)
    OP_29(0x15, 0x3, 0x1)
    OP_29(0x15, 0x3, 0x2)
    OP_29(0x15, 0x3, 0x10)
    OP_29(0x15, 0x3, 0x20)
    OP_29(0x15, 0x3, 0x40)
    OP_29(0x15, 0x2, 0x0)
    OP_29(0x15, 0x2, 0x1)
    OP_29(0x15, 0x2, 0x2)
    OP_29(0x15, 0x2, 0x3)
    OP_29(0x15, 0x2, 0x4)
    OP_29(0x15, 0x2, 0x5)
    OP_29(0x15, 0x2, 0x6)
    OP_29(0x15, 0x2, 0x7)
    OP_29(0x15, 0x2, 0x8)
    OP_29(0x15, 0x2, 0x9)
    OP_29(0x15, 0x2, 0xA)
    OP_29(0x15, 0x2, 0xB)
    OP_29(0x15, 0x2, 0xC)
    OP_29(0x15, 0x2, 0xD)
    OP_29(0x15, 0x2, 0xE)
    OP_29(0x15, 0x2, 0xF)
    OP_29(0x15, 0x2, 0x10)
    OP_29(0x15, 0x2, 0x11)
    OP_29(0x15, 0x2, 0x12)
    OP_29(0x15, 0x2, 0x13)
    OP_29(0x15, 0x2, 0x14)
    OP_29(0x15, 0x2, 0x15)
    OP_29(0x15, 0x2, 0x16)
    OP_29(0x15, 0x2, 0x17)
    OP_29(0x15, 0x2, 0x18)
    OP_29(0x15, 0x2, 0x19)
    OP_29(0x15, 0x2, 0x1A)
    OP_29(0x15, 0x2, 0x1B)
    OP_29(0x15, 0x2, 0x1C)
    OP_29(0x15, 0x2, 0x1D)
    OP_29(0x15, 0x2, 0x1E)
    OP_29(0x15, 0x2, 0x1F)

    label("loc_EC4A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EC5E")
    OP_29(0x15, 0x4, 0x2)

    label("loc_EC5E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EC73")
    OP_29(0x15, 0x1, 0x0)

    label("loc_EC73")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EC88")
    OP_29(0x15, 0x1, 0x1)

    label("loc_EC88")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_EC9D")
    OP_29(0x15, 0x1, 0x2)

    label("loc_EC9D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ECB2")
    OP_29(0x15, 0x1, 0x3)

    label("loc_ECB2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ECC7")
    OP_29(0x15, 0x1, 0x4)

    label("loc_ECC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ECDC")
    OP_29(0x15, 0x1, 0x5)

    label("loc_ECDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ECF1")
    OP_29(0x15, 0x1, 0x6)

    label("loc_ECF1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ED06")
    OP_29(0x15, 0x1, 0x7)

    label("loc_ED06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ED1B")
    OP_29(0x15, 0x1, 0x8)

    label("loc_ED1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ED30")
    OP_29(0x15, 0x1, 0x9)

    label("loc_ED30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ED45")
    OP_29(0x15, 0x1, 0xA)

    label("loc_ED45")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ED5A")
    OP_29(0x15, 0x1, 0xB)

    label("loc_ED5A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ED6E")
    OP_29(0x15, 0x4, 0x10)

    label("loc_ED6E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_ED82")
    OP_29(0x15, 0x4, 0x20)

    label("loc_ED82")

    Jump("loc_ED87")

    label("loc_ED87")

    Jump("loc_D78F")

    label("loc_ED8C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_56_D785 end

    def Function_57_EDA4(): pass

    label("Function_57_EDA4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EDAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11D94")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "----------３章--------------\x01",        # 0
            "QS_0301  消えた準教授の捜索   \x01",      # 1
            "QS_0302  違法駐車の取り締まり \x01",      # 2
            "QS_0303  クロスベル百景の撮影 \x01",      # 3
            "QS_0304  ベルガード門の紛失物 \x01",      # 4
            "QS_0305  手配魔獣⑤           \x01",      # 5
            "QS_0306  捜査二課の手伝い     \x01",      # 6
            "QS_0307  鉱山の魔獣退治       \x01",      # 7
            "QS_0308  ストーカー事件の捜査 \x01",      # 8
            "QS_0309  手配魔獣⑥           \x01",      # 9
            "QS_0310  行方不明の観光客     \x01",      # 10
            "QS_0311  窃盗事件の捜査       \x01",      # 11
            "QS_0312  手配魔獣⑦           \x01",      # 12
            "QS_0313  怪盗Ｂの挑戦         \x01",      # 13
            "QS_0314  手配魔獣⑧           \x01",      # 14
            "QS_0315  落とした婚約指輪     \x01",      # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_F01B"),
        (2, "loc_F138"),
        (3, "loc_F31E"),
        (4, "loc_F508"),
        (6, "loc_F5ED"),
        (7, "loc_F6C9"),
        (11, "loc_F791"),
        (13, "loc_F8F7"),
        (5, "loc_FA4F"),
        (8, "loc_FA4F"),
        (9, "loc_FA4F"),
        (10, "loc_FA4F"),
        (12, "loc_FA4F"),
        (15, "loc_FA4F"),
        (14, "loc_FA4F"),
        (SWITCH_DEFAULT, "loc_FAC8"),
    )


    label("loc_F01B")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期化\x01",                           # 0
            "開始\x01",                             # 1
            "QF_01★病院で事情を聞いた\x01",        # 2
            "QF_02★釣公師団を訪れた\x01",          # 3
            "GF   ★中州で釣り大会を確認\x01",      # 4
            "QF_03★釣り勝負開始\x01",              # 5
            "QF_04★負けた\x01",                    # 6
            "QF_05★引き分けた\x01",                # 7
            "QF_06★勝った\x01",                    # 8
            "QF_07★クエストをクリアした\x01",      # 9
            "QF_08（不使用）\x01",                  # 10
            "QF_09（不使用）\x01",                  # 11
            "QF_10（不使用）\x01",                  # 12
            "QF_11（不使用）\x01",                  # 13
            "達成\x01",                             # 14
            "報告\x01",                             # 15
        )
    )

    MenuEnd(0x5)
    Jump("loc_FAD7")

    label("loc_F138")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期化\x01",                             # 0
            "開始\x01",                               # 1
            "QF_01★開始\x01",                        # 2
            "QF_03★西口?車両１ステッカー\x01",       # 3
            "QF_05★西口?車両２ステッカー\x01",       # 4
            "QF_07★西口?車両３ステッカー\x01",       # 5
            "QF_09★西口?車両４ステッカー\x01",       # 6
            "QF_11★東口?車両５ステッカー\x01",       # 7
            "QF_13★東口?車両６ステッカー\x01",       # 8
            "QF_15★東口?車両７ステッカー\x01",       # 9
            "QF_17★東口?車両８ステッカー\x01",       # 10
            "QF_19★東口?車両９ステッカー\x01",       # 11
            "QF_20★全車両ナンバー見た\x01",          # 12
            "QF_21★重複ナンバーに気付いた\x01",      # 13
            "【→次へ】\x01",                         # 14
        )
    )

    MenuEnd(0x5)
    OP_60(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F319")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "QF_22★失敗終了\x01",      # 0
            "QF_23★成功終了\x01",      # 1
            "達成\x01",                 # 2
            "報告\x01",                 # 3
        )
    )

    MenuEnd(0x5)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F319")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F319")

    Jump("loc_FAD7")

    label("loc_F31E")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期化\x01",                                # 0
            "開始\x01",                                  # 1
            "QF_01★01 受付トリアと話した\x01",          # 2
            "QF_02★02 依頼内容を聞いた\x01",            # 3
            "QF_03★03 古道の田園風景\x01",              # 4
            "QF_04★04 アルモリカ村の花畑\x01",          # 5
            "QF_05★05 ウルスラ間道見晴らし台\x01",      # 6
            "QF_06★06 大聖堂墓地からの光景\x01",        # 7
            "QF_07★07 マインツ山道の滝\x01",            # 8
            "QF_08★08 西クロスベル街道の線路\x01",      # 9
            "QF_09★09 星見の塔の遠景\x01",              # 10
            "QF_10★10 月の僧院の遠景\x01",              # 11
            "QF_11★11 太陽の砦の遠景\x01",              # 12
            "【→次へ】\x01",                            # 13
        )
    )

    MenuEnd(0x5)
    OP_60(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F503")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "QF_12★12 写真提出?大満足\x01",          # 0
            "QF_13★13 写真提出?数そこそこ\x01",      # 1
            "達成\x01",                               # 2
            "報告\x01",                               # 3
        )
    )

    MenuEnd(0x5)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F503")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F503")

    Jump("loc_FAD7")

    label("loc_F508")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期化\x01",                                # 0
            "開始\x01",                                  # 1
            "QF_01★01 カバー装甲車を調べた\x01",        # 2
            "QF_02★02 依頼内容を聞いた\x01",            # 3
            "QF_03★03 依頼を引き受けた\x01",            # 4
            "QF_04★04 ディーターに話を聞いた\x01",      # 5
            "QF_05★05 ステラに話を聞いた\x01",          # 6
            "QF_06★06 屋上での捜査を開始した\x01",      # 7
            "達成\x01",                                  # 8
            "報告\x01",                                  # 9
        )
    )

    MenuEnd(0x5)
    Jump("loc_FAD7")

    label("loc_F5ED")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期化\x01",                                # 0
            "開始\x01",                                  # 1
            "QF_01★01 捜査二課から依頼がきた\x01",      # 2
            "QF_02★02 ミーティングした\x01",            # 3
            "QF_03★03 ソーニャと話した \x01",           # 4
            "QF_04★04 作戦を開始した\x01",              # 5
            "QF_05★05 聞き込みを開始した\x01",          # 6
            "QF_14★14 聞き込みを終了した\x01",          # 7
            "達成\x01",                                  # 8
            "報告\x01",                                  # 9
        )
    )

    MenuEnd(0x5)
    Jump("loc_FAD7")

    label("loc_F6C9")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期化\x01",                              # 0
            "開始\x01",                                # 1
            "QF_01★01 依頼内容を聞いた\x01",          # 2
            "QF_02★02 依頼を引き受けた\x01",          # 3
            "QF_03★03 廃坑の鍵を使った\x09\x01",      # 4
            "QF_04★04 鉱山に入った\x01",              # 5
            "QF_05★05 魔獣を殲滅した\x01",            # 6
            "★あと１匹で全滅完了\x01",                # 7
            "達成\x01",                                # 8
            "報告\x01",                                # 9
        )
    )

    MenuEnd(0x5)
    Jump("loc_FAD7")

    label("loc_F791")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期化\x01",          # 0
            "開始\x01",            # 1
            "QF_01\x01",           # 2
            "QF_02\x01",           # 3
            "QF_03\x01",           # 4
            "QF_04\x01",           # 5
            "QF_05\x01",           # 6
            "QF_06\x01",           # 7
            "QF_07\x01",           # 8
            "QF_08\x01",           # 9
            "QF_09\x01",           # 10
            "QF_10\x01",           # 11
            "QF_11\x01",           # 12
            "QF_12\x01",           # 13
            "QF_13\x01",           # 14
            "【→次へ】\x01",      # 15
        )
    )

    MenuEnd(0x5)
    OP_60(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F8F2")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "QF_14\x01",                  # 0
            "QF_15\x01",                  # 1
            "QF_16\x01",                  # 2
            "QF_17\x01",                  # 3
            "QF_18\x01",                  # 4
            "QF_19\x01",                  # 5
            "QF_20\x01",                  # 6
            "QF_21\x01",                  # 7
            "QF_22\x01",                  # 8
            "【C010C張り込み】\x01",      # 9
            "【C110C張り込み】\x01",      # 10
            "【C040C張り込み】\x01",      # 11
            "【C120C張り込み】\x01",      # 12
            "【張り込み失敗】\x01",       # 13
            "【解決イベント】\x01",       # 14
            "報告\x01",                   # 15
        )
    )

    MenuEnd(0x5)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F8F2")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_F8F2")

    Jump("loc_FAD7")

    label("loc_F8F7")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期化\x01",                                # 0
            "開始\x01",                                  # 1
            "QF_01★01 事情を聞いて捜査開始\x01",        # 2
            "QF_02★02 中央区の鐘を調べた\x01",          # 3
            "QF_03★03 釣公師団の水槽を調べた\x01",      # 4
            "QF_04★04 イグニスのスピーカー\x01",        # 5
            "QF_05★05 図書館のイベントを見た\x01",      # 6
            "QF_06★06 空港でカードを見つけた\x01",      # 7
            "QF_07★07 ＣＮＳを調べた\x01",              # 8
            "QF_08（不使用）\x01",                       # 9
            "QF_09（不使用）\x01",                       # 10
            "QF_10（不使用）\x01",                       # 11
            "QF_11（不使用）\x01",                       # 12
            "QF_12（不使用）\x01",                       # 13
            "達成\x01",                                  # 14
            "報告\x01",                                  # 15
        )
    )

    MenuEnd(0x5)
    Jump("loc_FAD7")

    label("loc_FA4F")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期化\x01",      # 0
            "開始\x01",        # 1
            "QF_01\x01",       # 2
            "QF_02\x01",       # 3
            "QF_03\x01",       # 4
            "QF_04\x01",       # 5
            "QF_05\x01",       # 6
            "QF_06\x01",       # 7
            "QF_07\x01",       # 8
            "QF_08\x01",       # 9
            "QF_09\x01",       # 10
            "QF_10\x01",       # 11
            "QF_11\x01",       # 12
            "QF_12\x01",       # 13
            "達成\x01",        # 14
            "報告\x01",        # 15
        )
    )

    MenuEnd(0x5)
    Jump("loc_FAD7")

    label("loc_FAC8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_FAD7")

    label("loc_FAD7")

    OP_60(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11D8F")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_FB4D"),
        (2, "loc_FD74"),
        (3, "loc_FFC8"),
        (4, "loc_10207"),
        (5, "loc_103B3"),
        (6, "loc_105DD"),
        (7, "loc_10789"),
        (8, "loc_10AC1"),
        (9, "loc_10CEB"),
        (10, "loc_10F15"),
        (11, "loc_1113F"),
        (12, "loc_114E7"),
        (13, "loc_11711"),
        (14, "loc_1193B"),
        (15, "loc_11B65"),
        (SWITCH_DEFAULT, "loc_11D8F"),
    )


    label("loc_FB4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC3A")
    OP_29(0x16, 0x3, 0x0)
    OP_29(0x16, 0x3, 0x1)
    OP_29(0x16, 0x3, 0x2)
    OP_29(0x16, 0x3, 0x10)
    OP_29(0x16, 0x3, 0x20)
    OP_29(0x16, 0x3, 0x40)
    OP_29(0x16, 0x2, 0x0)
    OP_29(0x16, 0x2, 0x1)
    OP_29(0x16, 0x2, 0x2)
    OP_29(0x16, 0x2, 0x3)
    OP_29(0x16, 0x2, 0x4)
    OP_29(0x16, 0x2, 0x5)
    OP_29(0x16, 0x2, 0x6)
    OP_29(0x16, 0x2, 0x7)
    OP_29(0x16, 0x2, 0x8)
    OP_29(0x16, 0x2, 0x9)
    OP_29(0x16, 0x2, 0xA)
    OP_29(0x16, 0x2, 0xB)
    OP_29(0x16, 0x2, 0xC)
    OP_29(0x16, 0x2, 0xD)
    OP_29(0x16, 0x2, 0xE)
    OP_29(0x16, 0x2, 0xF)
    OP_29(0x16, 0x2, 0x10)
    OP_29(0x16, 0x2, 0x11)
    OP_29(0x16, 0x2, 0x12)
    OP_29(0x16, 0x2, 0x13)
    OP_29(0x16, 0x2, 0x14)
    OP_29(0x16, 0x2, 0x15)
    OP_29(0x16, 0x2, 0x16)
    OP_29(0x16, 0x2, 0x17)
    OP_29(0x16, 0x2, 0x18)
    OP_29(0x16, 0x2, 0x19)
    OP_29(0x16, 0x2, 0x1A)
    OP_29(0x16, 0x2, 0x1B)
    OP_29(0x16, 0x2, 0x1C)
    OP_29(0x16, 0x2, 0x1D)
    OP_29(0x16, 0x2, 0x1E)
    OP_29(0x16, 0x2, 0x1F)

    label("loc_FC3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FC4E")
    OP_29(0x16, 0x4, 0x2)

    label("loc_FC4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FC63")
    OP_29(0x16, 0x1, 0x0)

    label("loc_FC63")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FC78")
    OP_29(0x16, 0x1, 0x1)

    label("loc_FC78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FC8A")
    SetScenarioFlags(0xBD, 3)

    label("loc_FC8A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FC9F")
    OP_29(0x16, 0x1, 0x2)

    label("loc_FC9F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FCB4")
    OP_29(0x16, 0x1, 0x3)

    label("loc_FCB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FCC9")
    OP_29(0x16, 0x1, 0x4)

    label("loc_FCC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FCDE")
    OP_29(0x16, 0x1, 0x5)

    label("loc_FCDE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FCF3")
    OP_29(0x16, 0x1, 0x6)

    label("loc_FCF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FD08")
    OP_29(0x16, 0x1, 0x7)

    label("loc_FD08")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FD1D")
    OP_29(0x16, 0x1, 0x8)

    label("loc_FD1D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FD32")
    OP_29(0x16, 0x1, 0x9)

    label("loc_FD32")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FD47")
    OP_29(0x16, 0x1, 0xA)

    label("loc_FD47")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FD5B")
    OP_29(0x16, 0x4, 0x10)

    label("loc_FD5B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FD6F")
    OP_29(0x16, 0x4, 0x20)

    label("loc_FD6F")

    Jump("loc_11D8F")

    label("loc_FD74")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE61")
    OP_29(0x17, 0x3, 0x0)
    OP_29(0x17, 0x3, 0x1)
    OP_29(0x17, 0x3, 0x2)
    OP_29(0x17, 0x3, 0x10)
    OP_29(0x17, 0x3, 0x20)
    OP_29(0x17, 0x3, 0x40)
    OP_29(0x17, 0x2, 0x0)
    OP_29(0x17, 0x2, 0x1)
    OP_29(0x17, 0x2, 0x2)
    OP_29(0x17, 0x2, 0x3)
    OP_29(0x17, 0x2, 0x4)
    OP_29(0x17, 0x2, 0x5)
    OP_29(0x17, 0x2, 0x6)
    OP_29(0x17, 0x2, 0x7)
    OP_29(0x17, 0x2, 0x8)
    OP_29(0x17, 0x2, 0x9)
    OP_29(0x17, 0x2, 0xA)
    OP_29(0x17, 0x2, 0xB)
    OP_29(0x17, 0x2, 0xC)
    OP_29(0x17, 0x2, 0xD)
    OP_29(0x17, 0x2, 0xE)
    OP_29(0x17, 0x2, 0xF)
    OP_29(0x17, 0x2, 0x10)
    OP_29(0x17, 0x2, 0x11)
    OP_29(0x17, 0x2, 0x12)
    OP_29(0x17, 0x2, 0x13)
    OP_29(0x17, 0x2, 0x14)
    OP_29(0x17, 0x2, 0x15)
    OP_29(0x17, 0x2, 0x16)
    OP_29(0x17, 0x2, 0x17)
    OP_29(0x17, 0x2, 0x18)
    OP_29(0x17, 0x2, 0x19)
    OP_29(0x17, 0x2, 0x1A)
    OP_29(0x17, 0x2, 0x1B)
    OP_29(0x17, 0x2, 0x1C)
    OP_29(0x17, 0x2, 0x1D)
    OP_29(0x17, 0x2, 0x1E)
    OP_29(0x17, 0x2, 0x1F)

    label("loc_FE61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FE75")
    OP_29(0x17, 0x4, 0x2)

    label("loc_FE75")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FE8A")
    OP_29(0x17, 0x1, 0x0)

    label("loc_FE8A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FE9F")
    OP_29(0x17, 0x1, 0x2)

    label("loc_FE9F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FEB4")
    OP_29(0x17, 0x1, 0x4)

    label("loc_FEB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FEC9")
    OP_29(0x17, 0x1, 0x6)

    label("loc_FEC9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FEDE")
    OP_29(0x17, 0x1, 0x8)

    label("loc_FEDE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FEF3")
    OP_29(0x17, 0x1, 0xA)

    label("loc_FEF3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FF08")
    OP_29(0x17, 0x1, 0xC)

    label("loc_FF08")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FF1D")
    OP_29(0x17, 0x1, 0xE)

    label("loc_FF1D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FF32")
    OP_29(0x17, 0x1, 0x10)

    label("loc_FF32")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FF47")
    OP_29(0x17, 0x1, 0x12)

    label("loc_FF47")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FF5C")
    OP_29(0x17, 0x1, 0x13)

    label("loc_FF5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FF71")
    OP_29(0x17, 0x1, 0x14)

    label("loc_FF71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FF86")
    OP_29(0x17, 0x1, 0x15)

    label("loc_FF86")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FF9B")
    OP_29(0x17, 0x1, 0x16)

    label("loc_FF9B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FFAF")
    OP_29(0x17, 0x4, 0x10)

    label("loc_FFAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_FFC3")
    OP_29(0x17, 0x4, 0x20)

    label("loc_FFC3")

    Jump("loc_11D8F")

    label("loc_FFC8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_100B5")
    OP_29(0x18, 0x3, 0x0)
    OP_29(0x18, 0x3, 0x1)
    OP_29(0x18, 0x3, 0x2)
    OP_29(0x18, 0x3, 0x10)
    OP_29(0x18, 0x3, 0x20)
    OP_29(0x18, 0x3, 0x40)
    OP_29(0x18, 0x2, 0x0)
    OP_29(0x18, 0x2, 0x1)
    OP_29(0x18, 0x2, 0x2)
    OP_29(0x18, 0x2, 0x3)
    OP_29(0x18, 0x2, 0x4)
    OP_29(0x18, 0x2, 0x5)
    OP_29(0x18, 0x2, 0x6)
    OP_29(0x18, 0x2, 0x7)
    OP_29(0x18, 0x2, 0x8)
    OP_29(0x18, 0x2, 0x9)
    OP_29(0x18, 0x2, 0xA)
    OP_29(0x18, 0x2, 0xB)
    OP_29(0x18, 0x2, 0xC)
    OP_29(0x18, 0x2, 0xD)
    OP_29(0x18, 0x2, 0xE)
    OP_29(0x18, 0x2, 0xF)
    OP_29(0x18, 0x2, 0x10)
    OP_29(0x18, 0x2, 0x11)
    OP_29(0x18, 0x2, 0x12)
    OP_29(0x18, 0x2, 0x13)
    OP_29(0x18, 0x2, 0x14)
    OP_29(0x18, 0x2, 0x15)
    OP_29(0x18, 0x2, 0x16)
    OP_29(0x18, 0x2, 0x17)
    OP_29(0x18, 0x2, 0x18)
    OP_29(0x18, 0x2, 0x19)
    OP_29(0x18, 0x2, 0x1A)
    OP_29(0x18, 0x2, 0x1B)
    OP_29(0x18, 0x2, 0x1C)
    OP_29(0x18, 0x2, 0x1D)
    OP_29(0x18, 0x2, 0x1E)
    OP_29(0x18, 0x2, 0x1F)

    label("loc_100B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_100C9")
    OP_29(0x18, 0x4, 0x2)

    label("loc_100C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_100DE")
    OP_29(0x18, 0x1, 0x0)

    label("loc_100DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_100F3")
    OP_29(0x18, 0x1, 0x1)

    label("loc_100F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10108")
    OP_29(0x18, 0x1, 0x2)

    label("loc_10108")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1011D")
    OP_29(0x18, 0x1, 0x3)

    label("loc_1011D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10132")
    OP_29(0x18, 0x1, 0x4)

    label("loc_10132")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10147")
    OP_29(0x18, 0x1, 0x5)

    label("loc_10147")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1015C")
    OP_29(0x18, 0x1, 0x6)

    label("loc_1015C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10171")
    OP_29(0x18, 0x1, 0x7)

    label("loc_10171")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10186")
    OP_29(0x18, 0x1, 0x8)

    label("loc_10186")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1019B")
    OP_29(0x18, 0x1, 0x9)

    label("loc_1019B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_101B0")
    OP_29(0x18, 0x1, 0xA)

    label("loc_101B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_101C5")
    OP_29(0x18, 0x1, 0xB)

    label("loc_101C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_101DA")
    OP_29(0x18, 0x1, 0xC)

    label("loc_101DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_101EE")
    OP_29(0x18, 0x4, 0x10)

    label("loc_101EE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10202")
    OP_29(0x18, 0x4, 0x20)

    label("loc_10202")

    Jump("loc_11D8F")

    label("loc_10207")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_102F4")
    OP_29(0x19, 0x3, 0x0)
    OP_29(0x19, 0x3, 0x1)
    OP_29(0x19, 0x3, 0x2)
    OP_29(0x19, 0x3, 0x10)
    OP_29(0x19, 0x3, 0x20)
    OP_29(0x19, 0x3, 0x40)
    OP_29(0x19, 0x2, 0x0)
    OP_29(0x19, 0x2, 0x1)
    OP_29(0x19, 0x2, 0x2)
    OP_29(0x19, 0x2, 0x3)
    OP_29(0x19, 0x2, 0x4)
    OP_29(0x19, 0x2, 0x5)
    OP_29(0x19, 0x2, 0x6)
    OP_29(0x19, 0x2, 0x7)
    OP_29(0x19, 0x2, 0x8)
    OP_29(0x19, 0x2, 0x9)
    OP_29(0x19, 0x2, 0xA)
    OP_29(0x19, 0x2, 0xB)
    OP_29(0x19, 0x2, 0xC)
    OP_29(0x19, 0x2, 0xD)
    OP_29(0x19, 0x2, 0xE)
    OP_29(0x19, 0x2, 0xF)
    OP_29(0x19, 0x2, 0x10)
    OP_29(0x19, 0x2, 0x11)
    OP_29(0x19, 0x2, 0x12)
    OP_29(0x19, 0x2, 0x13)
    OP_29(0x19, 0x2, 0x14)
    OP_29(0x19, 0x2, 0x15)
    OP_29(0x19, 0x2, 0x16)
    OP_29(0x19, 0x2, 0x17)
    OP_29(0x19, 0x2, 0x18)
    OP_29(0x19, 0x2, 0x19)
    OP_29(0x19, 0x2, 0x1A)
    OP_29(0x19, 0x2, 0x1B)
    OP_29(0x19, 0x2, 0x1C)
    OP_29(0x19, 0x2, 0x1D)
    OP_29(0x19, 0x2, 0x1E)
    OP_29(0x19, 0x2, 0x1F)

    label("loc_102F4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10308")
    OP_29(0x19, 0x4, 0x2)

    label("loc_10308")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1031D")
    OP_29(0x19, 0x1, 0x0)

    label("loc_1031D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10332")
    OP_29(0x19, 0x1, 0x1)

    label("loc_10332")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10347")
    OP_29(0x19, 0x1, 0x2)

    label("loc_10347")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1035C")
    OP_29(0x19, 0x1, 0x3)

    label("loc_1035C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10371")
    OP_29(0x19, 0x1, 0x4)

    label("loc_10371")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10386")
    OP_29(0x19, 0x1, 0x5)

    label("loc_10386")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1039A")
    OP_29(0x19, 0x4, 0x10)

    label("loc_1039A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_103AE")
    OP_29(0x19, 0x4, 0x20)

    label("loc_103AE")

    Jump("loc_11D8F")

    label("loc_103B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_104A0")
    OP_29(0x1A, 0x3, 0x0)
    OP_29(0x1A, 0x3, 0x1)
    OP_29(0x1A, 0x3, 0x2)
    OP_29(0x1A, 0x3, 0x10)
    OP_29(0x1A, 0x3, 0x20)
    OP_29(0x1A, 0x3, 0x40)
    OP_29(0x1A, 0x2, 0x0)
    OP_29(0x1A, 0x2, 0x1)
    OP_29(0x1A, 0x2, 0x2)
    OP_29(0x1A, 0x2, 0x3)
    OP_29(0x1A, 0x2, 0x4)
    OP_29(0x1A, 0x2, 0x5)
    OP_29(0x1A, 0x2, 0x6)
    OP_29(0x1A, 0x2, 0x7)
    OP_29(0x1A, 0x2, 0x8)
    OP_29(0x1A, 0x2, 0x9)
    OP_29(0x1A, 0x2, 0xA)
    OP_29(0x1A, 0x2, 0xB)
    OP_29(0x1A, 0x2, 0xC)
    OP_29(0x1A, 0x2, 0xD)
    OP_29(0x1A, 0x2, 0xE)
    OP_29(0x1A, 0x2, 0xF)
    OP_29(0x1A, 0x2, 0x10)
    OP_29(0x1A, 0x2, 0x11)
    OP_29(0x1A, 0x2, 0x12)
    OP_29(0x1A, 0x2, 0x13)
    OP_29(0x1A, 0x2, 0x14)
    OP_29(0x1A, 0x2, 0x15)
    OP_29(0x1A, 0x2, 0x16)
    OP_29(0x1A, 0x2, 0x17)
    OP_29(0x1A, 0x2, 0x18)
    OP_29(0x1A, 0x2, 0x19)
    OP_29(0x1A, 0x2, 0x1A)
    OP_29(0x1A, 0x2, 0x1B)
    OP_29(0x1A, 0x2, 0x1C)
    OP_29(0x1A, 0x2, 0x1D)
    OP_29(0x1A, 0x2, 0x1E)
    OP_29(0x1A, 0x2, 0x1F)

    label("loc_104A0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_104B4")
    OP_29(0x1A, 0x4, 0x2)

    label("loc_104B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_104C9")
    OP_29(0x1A, 0x1, 0x0)

    label("loc_104C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_104DE")
    OP_29(0x1A, 0x1, 0x1)

    label("loc_104DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_104F3")
    OP_29(0x1A, 0x1, 0x2)

    label("loc_104F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10508")
    OP_29(0x1A, 0x1, 0x3)

    label("loc_10508")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1051D")
    OP_29(0x1A, 0x1, 0x4)

    label("loc_1051D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10532")
    OP_29(0x1A, 0x1, 0x5)

    label("loc_10532")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10547")
    OP_29(0x1A, 0x1, 0x6)

    label("loc_10547")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1055C")
    OP_29(0x1A, 0x1, 0x7)

    label("loc_1055C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10571")
    OP_29(0x1A, 0x1, 0x8)

    label("loc_10571")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10586")
    OP_29(0x1A, 0x1, 0x9)

    label("loc_10586")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1059B")
    OP_29(0x1A, 0x1, 0xA)

    label("loc_1059B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_105B0")
    OP_29(0x1A, 0x1, 0xB)

    label("loc_105B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_105C4")
    OP_29(0x1A, 0x4, 0x10)

    label("loc_105C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_105D8")
    OP_29(0x1A, 0x4, 0x20)

    label("loc_105D8")

    Jump("loc_11D8F")

    label("loc_105DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_106CA")
    OP_29(0x1B, 0x3, 0x0)
    OP_29(0x1B, 0x3, 0x1)
    OP_29(0x1B, 0x3, 0x2)
    OP_29(0x1B, 0x3, 0x10)
    OP_29(0x1B, 0x3, 0x20)
    OP_29(0x1B, 0x3, 0x40)
    OP_29(0x1B, 0x2, 0x0)
    OP_29(0x1B, 0x2, 0x1)
    OP_29(0x1B, 0x2, 0x2)
    OP_29(0x1B, 0x2, 0x3)
    OP_29(0x1B, 0x2, 0x4)
    OP_29(0x1B, 0x2, 0x5)
    OP_29(0x1B, 0x2, 0x6)
    OP_29(0x1B, 0x2, 0x7)
    OP_29(0x1B, 0x2, 0x8)
    OP_29(0x1B, 0x2, 0x9)
    OP_29(0x1B, 0x2, 0xA)
    OP_29(0x1B, 0x2, 0xB)
    OP_29(0x1B, 0x2, 0xC)
    OP_29(0x1B, 0x2, 0xD)
    OP_29(0x1B, 0x2, 0xE)
    OP_29(0x1B, 0x2, 0xF)
    OP_29(0x1B, 0x2, 0x10)
    OP_29(0x1B, 0x2, 0x11)
    OP_29(0x1B, 0x2, 0x12)
    OP_29(0x1B, 0x2, 0x13)
    OP_29(0x1B, 0x2, 0x14)
    OP_29(0x1B, 0x2, 0x15)
    OP_29(0x1B, 0x2, 0x16)
    OP_29(0x1B, 0x2, 0x17)
    OP_29(0x1B, 0x2, 0x18)
    OP_29(0x1B, 0x2, 0x19)
    OP_29(0x1B, 0x2, 0x1A)
    OP_29(0x1B, 0x2, 0x1B)
    OP_29(0x1B, 0x2, 0x1C)
    OP_29(0x1B, 0x2, 0x1D)
    OP_29(0x1B, 0x2, 0x1E)
    OP_29(0x1B, 0x2, 0x1F)

    label("loc_106CA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_106DE")
    OP_29(0x1B, 0x4, 0x2)

    label("loc_106DE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_106F3")
    OP_29(0x1B, 0x1, 0x0)

    label("loc_106F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10708")
    OP_29(0x1B, 0x1, 0x1)

    label("loc_10708")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1071D")
    OP_29(0x1B, 0x1, 0x2)

    label("loc_1071D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10732")
    OP_29(0x1B, 0x1, 0x3)

    label("loc_10732")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10747")
    OP_29(0x1B, 0x1, 0x4)

    label("loc_10747")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1075C")
    OP_29(0x1A, 0x1, 0xD)

    label("loc_1075C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10770")
    OP_29(0x1B, 0x4, 0x10)

    label("loc_10770")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10784")
    OP_29(0x1B, 0x4, 0x20)

    label("loc_10784")

    Jump("loc_11D8F")

    label("loc_10789")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10876")
    OP_29(0x1C, 0x3, 0x0)
    OP_29(0x1C, 0x3, 0x1)
    OP_29(0x1C, 0x3, 0x2)
    OP_29(0x1C, 0x3, 0x10)
    OP_29(0x1C, 0x3, 0x20)
    OP_29(0x1C, 0x3, 0x40)
    OP_29(0x1C, 0x2, 0x0)
    OP_29(0x1C, 0x2, 0x1)
    OP_29(0x1C, 0x2, 0x2)
    OP_29(0x1C, 0x2, 0x3)
    OP_29(0x1C, 0x2, 0x4)
    OP_29(0x1C, 0x2, 0x5)
    OP_29(0x1C, 0x2, 0x6)
    OP_29(0x1C, 0x2, 0x7)
    OP_29(0x1C, 0x2, 0x8)
    OP_29(0x1C, 0x2, 0x9)
    OP_29(0x1C, 0x2, 0xA)
    OP_29(0x1C, 0x2, 0xB)
    OP_29(0x1C, 0x2, 0xC)
    OP_29(0x1C, 0x2, 0xD)
    OP_29(0x1C, 0x2, 0xE)
    OP_29(0x1C, 0x2, 0xF)
    OP_29(0x1C, 0x2, 0x10)
    OP_29(0x1C, 0x2, 0x11)
    OP_29(0x1C, 0x2, 0x12)
    OP_29(0x1C, 0x2, 0x13)
    OP_29(0x1C, 0x2, 0x14)
    OP_29(0x1C, 0x2, 0x15)
    OP_29(0x1C, 0x2, 0x16)
    OP_29(0x1C, 0x2, 0x17)
    OP_29(0x1C, 0x2, 0x18)
    OP_29(0x1C, 0x2, 0x19)
    OP_29(0x1C, 0x2, 0x1A)
    OP_29(0x1C, 0x2, 0x1B)
    OP_29(0x1C, 0x2, 0x1C)
    OP_29(0x1C, 0x2, 0x1D)
    OP_29(0x1C, 0x2, 0x1E)
    OP_29(0x1C, 0x2, 0x1F)

    label("loc_10876")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1088A")
    OP_29(0x1C, 0x4, 0x2)

    label("loc_1088A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_108A4")
    OP_29(0x1C, 0x4, 0x2)
    OP_29(0x1C, 0x1, 0x0)

    label("loc_108A4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_108C4")
    OP_29(0x1C, 0x4, 0x2)
    OP_29(0x1C, 0x1, 0x0)
    OP_29(0x1C, 0x1, 0x1)

    label("loc_108C4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_108EA")
    OP_29(0x1C, 0x4, 0x2)
    OP_29(0x1C, 0x1, 0x0)
    OP_29(0x1C, 0x1, 0x1)
    OP_29(0x1C, 0x1, 0x2)

    label("loc_108EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10916")
    OP_29(0x1C, 0x4, 0x2)
    OP_29(0x1C, 0x1, 0x0)
    OP_29(0x1C, 0x1, 0x1)
    OP_29(0x1C, 0x1, 0x2)
    OP_29(0x1C, 0x1, 0x3)

    label("loc_10916")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10975")
    OP_29(0x1C, 0x4, 0x2)
    OP_29(0x1C, 0x1, 0x0)
    OP_29(0x1C, 0x1, 0x1)
    OP_29(0x1C, 0x1, 0x2)
    OP_29(0x1C, 0x1, 0x3)
    SetScenarioFlags(0xBA, 3)
    SetScenarioFlags(0xBA, 4)
    SetScenarioFlags(0xBA, 5)
    SetScenarioFlags(0xBA, 6)
    SetScenarioFlags(0xBA, 7)
    SetScenarioFlags(0xBB, 0)
    SetScenarioFlags(0xBB, 1)
    SetScenarioFlags(0xBB, 2)
    SetScenarioFlags(0xBB, 3)
    SetScenarioFlags(0xBB, 4)
    SetScenarioFlags(0xBB, 5)
    SetScenarioFlags(0xBB, 6)
    SetScenarioFlags(0xBB, 7)
    SetScenarioFlags(0xBC, 0)
    SetScenarioFlags(0xBC, 1)
    SetScenarioFlags(0xBC, 2)
    SetScenarioFlags(0xBC, 3)

    label("loc_10975")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_109DD")
    OP_29(0x1C, 0x4, 0x2)
    OP_29(0x1C, 0x1, 0x0)
    OP_29(0x1C, 0x1, 0x1)
    OP_29(0x1C, 0x1, 0x2)
    OP_29(0x1C, 0x1, 0x3)
    OP_29(0x1C, 0x1, 0x4)
    SetScenarioFlags(0xBA, 2)
    SetScenarioFlags(0xBA, 3)
    SetScenarioFlags(0xBA, 4)
    SetScenarioFlags(0xBA, 5)
    SetScenarioFlags(0xBA, 6)
    SetScenarioFlags(0xBA, 7)
    SetScenarioFlags(0xBB, 0)
    SetScenarioFlags(0xBB, 1)
    SetScenarioFlags(0xBB, 2)
    SetScenarioFlags(0xBB, 3)
    SetScenarioFlags(0xBB, 4)
    SetScenarioFlags(0xBB, 5)
    SetScenarioFlags(0xBB, 6)
    SetScenarioFlags(0xBB, 7)
    SetScenarioFlags(0xBC, 0)
    SetScenarioFlags(0xBC, 1)
    SetScenarioFlags(0xBC, 2)
    SetScenarioFlags(0xBC, 3)

    label("loc_109DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10A4A")
    OP_29(0x1C, 0x4, 0x2)
    OP_29(0x1C, 0x1, 0x0)
    OP_29(0x1C, 0x1, 0x1)
    OP_29(0x1C, 0x1, 0x2)
    OP_29(0x1C, 0x1, 0x3)
    OP_29(0x1C, 0x1, 0x4)
    SetScenarioFlags(0xBA, 2)
    SetScenarioFlags(0xBA, 3)
    SetScenarioFlags(0xBA, 4)
    SetScenarioFlags(0xBA, 5)
    SetScenarioFlags(0xBA, 6)
    SetScenarioFlags(0xBA, 7)
    SetScenarioFlags(0xBB, 0)
    SetScenarioFlags(0xBB, 1)
    SetScenarioFlags(0xBB, 2)
    SetScenarioFlags(0xBB, 3)
    SetScenarioFlags(0xBB, 4)
    SetScenarioFlags(0xBB, 5)
    SetScenarioFlags(0xBB, 6)
    SetScenarioFlags(0xBB, 7)
    SetScenarioFlags(0xBC, 0)
    SetScenarioFlags(0xBC, 1)
    SetScenarioFlags(0xBC, 2)
    SetScenarioFlags(0xBC, 3)
    OP_29(0x1C, 0x4, 0x10)

    label("loc_10A4A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10ABC")
    OP_29(0x1C, 0x4, 0x2)
    OP_29(0x1C, 0x1, 0x0)
    OP_29(0x1C, 0x1, 0x1)
    OP_29(0x1C, 0x1, 0x2)
    OP_29(0x1C, 0x1, 0x3)
    OP_29(0x1C, 0x1, 0x4)
    SetScenarioFlags(0xBA, 2)
    SetScenarioFlags(0xBA, 3)
    SetScenarioFlags(0xBA, 4)
    SetScenarioFlags(0xBA, 5)
    SetScenarioFlags(0xBA, 6)
    SetScenarioFlags(0xBA, 7)
    SetScenarioFlags(0xBB, 0)
    SetScenarioFlags(0xBB, 1)
    SetScenarioFlags(0xBB, 2)
    SetScenarioFlags(0xBB, 3)
    SetScenarioFlags(0xBB, 4)
    SetScenarioFlags(0xBB, 5)
    SetScenarioFlags(0xBB, 6)
    SetScenarioFlags(0xBB, 7)
    SetScenarioFlags(0xBC, 0)
    SetScenarioFlags(0xBC, 1)
    SetScenarioFlags(0xBC, 2)
    SetScenarioFlags(0xBC, 3)
    OP_29(0x1C, 0x4, 0x10)
    OP_29(0x1C, 0x4, 0x20)

    label("loc_10ABC")

    Jump("loc_11D8F")

    label("loc_10AC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10BAE")
    OP_29(0x1D, 0x3, 0x0)
    OP_29(0x1D, 0x3, 0x1)
    OP_29(0x1D, 0x3, 0x2)
    OP_29(0x1D, 0x3, 0x10)
    OP_29(0x1D, 0x3, 0x20)
    OP_29(0x1D, 0x3, 0x40)
    OP_29(0x1D, 0x2, 0x0)
    OP_29(0x1D, 0x2, 0x1)
    OP_29(0x1D, 0x2, 0x2)
    OP_29(0x1D, 0x2, 0x3)
    OP_29(0x1D, 0x2, 0x4)
    OP_29(0x1D, 0x2, 0x5)
    OP_29(0x1D, 0x2, 0x6)
    OP_29(0x1D, 0x2, 0x7)
    OP_29(0x1D, 0x2, 0x8)
    OP_29(0x1D, 0x2, 0x9)
    OP_29(0x1D, 0x2, 0xA)
    OP_29(0x1D, 0x2, 0xB)
    OP_29(0x1D, 0x2, 0xC)
    OP_29(0x1D, 0x2, 0xD)
    OP_29(0x1D, 0x2, 0xE)
    OP_29(0x1D, 0x2, 0xF)
    OP_29(0x1D, 0x2, 0x10)
    OP_29(0x1D, 0x2, 0x11)
    OP_29(0x1D, 0x2, 0x12)
    OP_29(0x1D, 0x2, 0x13)
    OP_29(0x1D, 0x2, 0x14)
    OP_29(0x1D, 0x2, 0x15)
    OP_29(0x1D, 0x2, 0x16)
    OP_29(0x1D, 0x2, 0x17)
    OP_29(0x1D, 0x2, 0x18)
    OP_29(0x1D, 0x2, 0x19)
    OP_29(0x1D, 0x2, 0x1A)
    OP_29(0x1D, 0x2, 0x1B)
    OP_29(0x1D, 0x2, 0x1C)
    OP_29(0x1D, 0x2, 0x1D)
    OP_29(0x1D, 0x2, 0x1E)
    OP_29(0x1D, 0x2, 0x1F)

    label("loc_10BAE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10BC2")
    OP_29(0x1D, 0x4, 0x2)

    label("loc_10BC2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10BD7")
    OP_29(0x1D, 0x1, 0x0)

    label("loc_10BD7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10BEC")
    OP_29(0x1D, 0x1, 0x1)

    label("loc_10BEC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10C01")
    OP_29(0x1D, 0x1, 0x2)

    label("loc_10C01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10C16")
    OP_29(0x1D, 0x1, 0x3)

    label("loc_10C16")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10C2B")
    OP_29(0x1D, 0x1, 0x4)

    label("loc_10C2B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10C40")
    OP_29(0x1D, 0x1, 0x5)

    label("loc_10C40")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10C55")
    OP_29(0x1D, 0x1, 0x6)

    label("loc_10C55")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10C6A")
    OP_29(0x1D, 0x1, 0x7)

    label("loc_10C6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10C7F")
    OP_29(0x1D, 0x1, 0x8)

    label("loc_10C7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10C94")
    OP_29(0x1D, 0x1, 0x9)

    label("loc_10C94")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10CA9")
    OP_29(0x1D, 0x1, 0xA)

    label("loc_10CA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10CBE")
    OP_29(0x1D, 0x1, 0xB)

    label("loc_10CBE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10CD2")
    OP_29(0x1D, 0x4, 0x10)

    label("loc_10CD2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10CE6")
    OP_29(0x1D, 0x4, 0x20)

    label("loc_10CE6")

    Jump("loc_11D8F")

    label("loc_10CEB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DD8")
    OP_29(0x1E, 0x3, 0x0)
    OP_29(0x1E, 0x3, 0x1)
    OP_29(0x1E, 0x3, 0x2)
    OP_29(0x1E, 0x3, 0x10)
    OP_29(0x1E, 0x3, 0x20)
    OP_29(0x1E, 0x3, 0x40)
    OP_29(0x1E, 0x2, 0x0)
    OP_29(0x1E, 0x2, 0x1)
    OP_29(0x1E, 0x2, 0x2)
    OP_29(0x1E, 0x2, 0x3)
    OP_29(0x1E, 0x2, 0x4)
    OP_29(0x1E, 0x2, 0x5)
    OP_29(0x1E, 0x2, 0x6)
    OP_29(0x1E, 0x2, 0x7)
    OP_29(0x1E, 0x2, 0x8)
    OP_29(0x1E, 0x2, 0x9)
    OP_29(0x1E, 0x2, 0xA)
    OP_29(0x1E, 0x2, 0xB)
    OP_29(0x1E, 0x2, 0xC)
    OP_29(0x1E, 0x2, 0xD)
    OP_29(0x1E, 0x2, 0xE)
    OP_29(0x1E, 0x2, 0xF)
    OP_29(0x1E, 0x2, 0x10)
    OP_29(0x1E, 0x2, 0x11)
    OP_29(0x1E, 0x2, 0x12)
    OP_29(0x1E, 0x2, 0x13)
    OP_29(0x1E, 0x2, 0x14)
    OP_29(0x1E, 0x2, 0x15)
    OP_29(0x1E, 0x2, 0x16)
    OP_29(0x1E, 0x2, 0x17)
    OP_29(0x1E, 0x2, 0x18)
    OP_29(0x1E, 0x2, 0x19)
    OP_29(0x1E, 0x2, 0x1A)
    OP_29(0x1E, 0x2, 0x1B)
    OP_29(0x1E, 0x2, 0x1C)
    OP_29(0x1E, 0x2, 0x1D)
    OP_29(0x1E, 0x2, 0x1E)
    OP_29(0x1E, 0x2, 0x1F)

    label("loc_10DD8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10DEC")
    OP_29(0x1E, 0x4, 0x2)

    label("loc_10DEC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10E01")
    OP_29(0x1E, 0x1, 0x0)

    label("loc_10E01")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10E16")
    OP_29(0x1E, 0x1, 0x1)

    label("loc_10E16")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10E2B")
    OP_29(0x1E, 0x1, 0x2)

    label("loc_10E2B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10E40")
    OP_29(0x1E, 0x1, 0x3)

    label("loc_10E40")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10E55")
    OP_29(0x1E, 0x1, 0x4)

    label("loc_10E55")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10E6A")
    OP_29(0x1E, 0x1, 0x5)

    label("loc_10E6A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10E7F")
    OP_29(0x1E, 0x1, 0x6)

    label("loc_10E7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10E94")
    OP_29(0x1E, 0x1, 0x7)

    label("loc_10E94")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10EA9")
    OP_29(0x1E, 0x1, 0x8)

    label("loc_10EA9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10EBE")
    OP_29(0x1E, 0x1, 0x9)

    label("loc_10EBE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10ED3")
    OP_29(0x1E, 0x1, 0xA)

    label("loc_10ED3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10EE8")
    OP_29(0x1E, 0x1, 0xB)

    label("loc_10EE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10EFC")
    OP_29(0x1E, 0x4, 0x10)

    label("loc_10EFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_10F10")
    OP_29(0x1E, 0x4, 0x20)

    label("loc_10F10")

    Jump("loc_11D8F")

    label("loc_10F15")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11002")
    OP_29(0x1F, 0x3, 0x0)
    OP_29(0x1F, 0x3, 0x1)
    OP_29(0x1F, 0x3, 0x2)
    OP_29(0x1F, 0x3, 0x10)
    OP_29(0x1F, 0x3, 0x20)
    OP_29(0x1F, 0x3, 0x40)
    OP_29(0x1F, 0x2, 0x0)
    OP_29(0x1F, 0x2, 0x1)
    OP_29(0x1F, 0x2, 0x2)
    OP_29(0x1F, 0x2, 0x3)
    OP_29(0x1F, 0x2, 0x4)
    OP_29(0x1F, 0x2, 0x5)
    OP_29(0x1F, 0x2, 0x6)
    OP_29(0x1F, 0x2, 0x7)
    OP_29(0x1F, 0x2, 0x8)
    OP_29(0x1F, 0x2, 0x9)
    OP_29(0x1F, 0x2, 0xA)
    OP_29(0x1F, 0x2, 0xB)
    OP_29(0x1F, 0x2, 0xC)
    OP_29(0x1F, 0x2, 0xD)
    OP_29(0x1F, 0x2, 0xE)
    OP_29(0x1F, 0x2, 0xF)
    OP_29(0x1F, 0x2, 0x10)
    OP_29(0x1F, 0x2, 0x11)
    OP_29(0x1F, 0x2, 0x12)
    OP_29(0x1F, 0x2, 0x13)
    OP_29(0x1F, 0x2, 0x14)
    OP_29(0x1F, 0x2, 0x15)
    OP_29(0x1F, 0x2, 0x16)
    OP_29(0x1F, 0x2, 0x17)
    OP_29(0x1F, 0x2, 0x18)
    OP_29(0x1F, 0x2, 0x19)
    OP_29(0x1F, 0x2, 0x1A)
    OP_29(0x1F, 0x2, 0x1B)
    OP_29(0x1F, 0x2, 0x1C)
    OP_29(0x1F, 0x2, 0x1D)
    OP_29(0x1F, 0x2, 0x1E)
    OP_29(0x1F, 0x2, 0x1F)

    label("loc_11002")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11016")
    OP_29(0x1F, 0x4, 0x2)

    label("loc_11016")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1102B")
    OP_29(0x1F, 0x1, 0x0)

    label("loc_1102B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11040")
    OP_29(0x1F, 0x1, 0x1)

    label("loc_11040")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11055")
    OP_29(0x1F, 0x1, 0x2)

    label("loc_11055")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1106A")
    OP_29(0x1F, 0x1, 0x3)

    label("loc_1106A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1107F")
    OP_29(0x1F, 0x1, 0x4)

    label("loc_1107F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11094")
    OP_29(0x1F, 0x1, 0x5)

    label("loc_11094")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_110A9")
    OP_29(0x1F, 0x1, 0x6)

    label("loc_110A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_110BE")
    OP_29(0x1F, 0x1, 0x7)

    label("loc_110BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_110D3")
    OP_29(0x1F, 0x1, 0x8)

    label("loc_110D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_110E8")
    OP_29(0x1F, 0x1, 0x9)

    label("loc_110E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_110FD")
    OP_29(0x1F, 0x1, 0xA)

    label("loc_110FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11112")
    OP_29(0x1F, 0x1, 0xB)

    label("loc_11112")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11126")
    OP_29(0x1F, 0x4, 0x10)

    label("loc_11126")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1113A")
    OP_29(0x1F, 0x4, 0x20)

    label("loc_1113A")

    Jump("loc_11D8F")

    label("loc_1113F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1122C")
    OP_29(0x20, 0x3, 0x0)
    OP_29(0x20, 0x3, 0x1)
    OP_29(0x20, 0x3, 0x2)
    OP_29(0x20, 0x3, 0x10)
    OP_29(0x20, 0x3, 0x20)
    OP_29(0x20, 0x3, 0x40)
    OP_29(0x20, 0x2, 0x0)
    OP_29(0x20, 0x2, 0x1)
    OP_29(0x20, 0x2, 0x2)
    OP_29(0x20, 0x2, 0x3)
    OP_29(0x20, 0x2, 0x4)
    OP_29(0x20, 0x2, 0x5)
    OP_29(0x20, 0x2, 0x6)
    OP_29(0x20, 0x2, 0x7)
    OP_29(0x20, 0x2, 0x8)
    OP_29(0x20, 0x2, 0x9)
    OP_29(0x20, 0x2, 0xA)
    OP_29(0x20, 0x2, 0xB)
    OP_29(0x20, 0x2, 0xC)
    OP_29(0x20, 0x2, 0xD)
    OP_29(0x20, 0x2, 0xE)
    OP_29(0x20, 0x2, 0xF)
    OP_29(0x20, 0x2, 0x10)
    OP_29(0x20, 0x2, 0x11)
    OP_29(0x20, 0x2, 0x12)
    OP_29(0x20, 0x2, 0x13)
    OP_29(0x20, 0x2, 0x14)
    OP_29(0x20, 0x2, 0x15)
    OP_29(0x20, 0x2, 0x16)
    OP_29(0x20, 0x2, 0x17)
    OP_29(0x20, 0x2, 0x18)
    OP_29(0x20, 0x2, 0x19)
    OP_29(0x20, 0x2, 0x1A)
    OP_29(0x20, 0x2, 0x1B)
    OP_29(0x20, 0x2, 0x1C)
    OP_29(0x20, 0x2, 0x1D)
    OP_29(0x20, 0x2, 0x1E)
    OP_29(0x20, 0x2, 0x1F)

    label("loc_1122C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11240")
    OP_29(0x20, 0x4, 0x2)

    label("loc_11240")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11255")
    OP_29(0x20, 0x1, 0x0)

    label("loc_11255")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1126A")
    OP_29(0x20, 0x1, 0x1)

    label("loc_1126A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1127F")
    OP_29(0x20, 0x1, 0x2)

    label("loc_1127F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11294")
    OP_29(0x20, 0x1, 0x3)

    label("loc_11294")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_112A9")
    OP_29(0x20, 0x1, 0x4)

    label("loc_112A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_112BE")
    OP_29(0x20, 0x1, 0x5)

    label("loc_112BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_112D3")
    OP_29(0x20, 0x1, 0x6)

    label("loc_112D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_112E8")
    OP_29(0x20, 0x1, 0x7)

    label("loc_112E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_112FD")
    OP_29(0x20, 0x1, 0x8)

    label("loc_112FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11312")
    OP_29(0x20, 0x1, 0x9)

    label("loc_11312")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11327")
    OP_29(0x20, 0x1, 0xA)

    label("loc_11327")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1133C")
    OP_29(0x20, 0x1, 0xB)

    label("loc_1133C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11351")
    OP_29(0x20, 0x1, 0xC)

    label("loc_11351")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11366")
    OP_29(0x20, 0x1, 0xD)

    label("loc_11366")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1137B")
    OP_29(0x20, 0x1, 0xE)

    label("loc_1137B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11390")
    OP_29(0x20, 0x1, 0xF)

    label("loc_11390")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_113A5")
    OP_29(0x20, 0x1, 0x10)

    label("loc_113A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_113BA")
    OP_29(0x20, 0x1, 0x11)

    label("loc_113BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_113CF")
    OP_29(0x20, 0x1, 0x12)

    label("loc_113CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_113E4")
    OP_29(0x20, 0x1, 0x13)

    label("loc_113E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x17), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_113F9")
    OP_29(0x20, 0x1, 0x14)

    label("loc_113F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1140E")
    OP_29(0x20, 0x1, 0x15)

    label("loc_1140E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x19), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1142E")
    SetScenarioFlags(0x5C, 4)
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Jump("loc_114C9")

    label("loc_1142E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1144E")
    SetScenarioFlags(0x5C, 1)
    NewScene("c110C", 0, 0, 0)
    IdleLoop()
    Jump("loc_114C9")

    label("loc_1144E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1146E")
    SetScenarioFlags(0x5C, 3)
    NewScene("c040C", 0, 0, 0)
    IdleLoop()
    Jump("loc_114C9")

    label("loc_1146E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1148E")
    SetScenarioFlags(0x5C, 2)
    NewScene("c120C", 0, 0, 0)
    IdleLoop()
    Jump("loc_114C9")

    label("loc_1148E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_114AE")
    SetScenarioFlags(0x5C, 5)
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Jump("loc_114C9")

    label("loc_114AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_114C9")
    SetScenarioFlags(0x5C, 1)
    NewScene("c120C", 0, 0, 0)
    IdleLoop()

    label("loc_114C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1F), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_114E2")
    OP_29(0x20, 0x4, 0x10)
    OP_29(0x20, 0x4, 0x20)

    label("loc_114E2")

    Jump("loc_11D8F")

    label("loc_114E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_115D4")
    OP_29(0x21, 0x3, 0x0)
    OP_29(0x21, 0x3, 0x1)
    OP_29(0x21, 0x3, 0x2)
    OP_29(0x21, 0x3, 0x10)
    OP_29(0x21, 0x3, 0x20)
    OP_29(0x21, 0x3, 0x40)
    OP_29(0x21, 0x2, 0x0)
    OP_29(0x21, 0x2, 0x1)
    OP_29(0x21, 0x2, 0x2)
    OP_29(0x21, 0x2, 0x3)
    OP_29(0x21, 0x2, 0x4)
    OP_29(0x21, 0x2, 0x5)
    OP_29(0x21, 0x2, 0x6)
    OP_29(0x21, 0x2, 0x7)
    OP_29(0x21, 0x2, 0x8)
    OP_29(0x21, 0x2, 0x9)
    OP_29(0x21, 0x2, 0xA)
    OP_29(0x21, 0x2, 0xB)
    OP_29(0x21, 0x2, 0xC)
    OP_29(0x21, 0x2, 0xD)
    OP_29(0x21, 0x2, 0xE)
    OP_29(0x21, 0x2, 0xF)
    OP_29(0x21, 0x2, 0x10)
    OP_29(0x21, 0x2, 0x11)
    OP_29(0x21, 0x2, 0x12)
    OP_29(0x21, 0x2, 0x13)
    OP_29(0x21, 0x2, 0x14)
    OP_29(0x21, 0x2, 0x15)
    OP_29(0x21, 0x2, 0x16)
    OP_29(0x21, 0x2, 0x17)
    OP_29(0x21, 0x2, 0x18)
    OP_29(0x21, 0x2, 0x19)
    OP_29(0x21, 0x2, 0x1A)
    OP_29(0x21, 0x2, 0x1B)
    OP_29(0x21, 0x2, 0x1C)
    OP_29(0x21, 0x2, 0x1D)
    OP_29(0x21, 0x2, 0x1E)
    OP_29(0x21, 0x2, 0x1F)

    label("loc_115D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_115E8")
    OP_29(0x21, 0x4, 0x2)

    label("loc_115E8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_115FD")
    OP_29(0x21, 0x1, 0x0)

    label("loc_115FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11612")
    OP_29(0x21, 0x1, 0x1)

    label("loc_11612")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11627")
    OP_29(0x21, 0x1, 0x2)

    label("loc_11627")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1163C")
    OP_29(0x21, 0x1, 0x3)

    label("loc_1163C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11651")
    OP_29(0x21, 0x1, 0x4)

    label("loc_11651")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11666")
    OP_29(0x21, 0x1, 0x5)

    label("loc_11666")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1167B")
    OP_29(0x21, 0x1, 0x6)

    label("loc_1167B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11690")
    OP_29(0x21, 0x1, 0x7)

    label("loc_11690")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_116A5")
    OP_29(0x21, 0x1, 0x8)

    label("loc_116A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_116BA")
    OP_29(0x21, 0x1, 0x9)

    label("loc_116BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_116CF")
    OP_29(0x21, 0x1, 0xA)

    label("loc_116CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_116E4")
    OP_29(0x21, 0x1, 0xB)

    label("loc_116E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_116F8")
    OP_29(0x21, 0x4, 0x10)

    label("loc_116F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1170C")
    OP_29(0x21, 0x4, 0x20)

    label("loc_1170C")

    Jump("loc_11D8F")

    label("loc_11711")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_117FE")
    OP_29(0x22, 0x3, 0x0)
    OP_29(0x22, 0x3, 0x1)
    OP_29(0x22, 0x3, 0x2)
    OP_29(0x22, 0x3, 0x10)
    OP_29(0x22, 0x3, 0x20)
    OP_29(0x22, 0x3, 0x40)
    OP_29(0x22, 0x2, 0x0)
    OP_29(0x22, 0x2, 0x1)
    OP_29(0x22, 0x2, 0x2)
    OP_29(0x22, 0x2, 0x3)
    OP_29(0x22, 0x2, 0x4)
    OP_29(0x22, 0x2, 0x5)
    OP_29(0x22, 0x2, 0x6)
    OP_29(0x22, 0x2, 0x7)
    OP_29(0x22, 0x2, 0x8)
    OP_29(0x22, 0x2, 0x9)
    OP_29(0x22, 0x2, 0xA)
    OP_29(0x22, 0x2, 0xB)
    OP_29(0x22, 0x2, 0xC)
    OP_29(0x22, 0x2, 0xD)
    OP_29(0x22, 0x2, 0xE)
    OP_29(0x22, 0x2, 0xF)
    OP_29(0x22, 0x2, 0x10)
    OP_29(0x22, 0x2, 0x11)
    OP_29(0x22, 0x2, 0x12)
    OP_29(0x22, 0x2, 0x13)
    OP_29(0x22, 0x2, 0x14)
    OP_29(0x22, 0x2, 0x15)
    OP_29(0x22, 0x2, 0x16)
    OP_29(0x22, 0x2, 0x17)
    OP_29(0x22, 0x2, 0x18)
    OP_29(0x22, 0x2, 0x19)
    OP_29(0x22, 0x2, 0x1A)
    OP_29(0x22, 0x2, 0x1B)
    OP_29(0x22, 0x2, 0x1C)
    OP_29(0x22, 0x2, 0x1D)
    OP_29(0x22, 0x2, 0x1E)
    OP_29(0x22, 0x2, 0x1F)

    label("loc_117FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11812")
    OP_29(0x22, 0x4, 0x2)

    label("loc_11812")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11827")
    OP_29(0x22, 0x1, 0x0)

    label("loc_11827")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1183C")
    OP_29(0x22, 0x1, 0x1)

    label("loc_1183C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11851")
    OP_29(0x22, 0x1, 0x2)

    label("loc_11851")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11866")
    OP_29(0x22, 0x1, 0x3)

    label("loc_11866")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1187B")
    OP_29(0x22, 0x1, 0x4)

    label("loc_1187B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11890")
    OP_29(0x22, 0x1, 0x5)

    label("loc_11890")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_118A5")
    OP_29(0x22, 0x1, 0x6)

    label("loc_118A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_118BA")
    OP_29(0x22, 0x1, 0x7)

    label("loc_118BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_118CF")
    OP_29(0x22, 0x1, 0x8)

    label("loc_118CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_118E4")
    OP_29(0x22, 0x1, 0x9)

    label("loc_118E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_118F9")
    OP_29(0x22, 0x1, 0xA)

    label("loc_118F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1190E")
    OP_29(0x22, 0x1, 0xB)

    label("loc_1190E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11922")
    OP_29(0x22, 0x4, 0x10)

    label("loc_11922")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11936")
    OP_29(0x22, 0x4, 0x20)

    label("loc_11936")

    Jump("loc_11D8F")

    label("loc_1193B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A28")
    OP_29(0x23, 0x3, 0x0)
    OP_29(0x23, 0x3, 0x1)
    OP_29(0x23, 0x3, 0x2)
    OP_29(0x23, 0x3, 0x10)
    OP_29(0x23, 0x3, 0x20)
    OP_29(0x23, 0x3, 0x40)
    OP_29(0x23, 0x2, 0x0)
    OP_29(0x23, 0x2, 0x1)
    OP_29(0x23, 0x2, 0x2)
    OP_29(0x23, 0x2, 0x3)
    OP_29(0x23, 0x2, 0x4)
    OP_29(0x23, 0x2, 0x5)
    OP_29(0x23, 0x2, 0x6)
    OP_29(0x23, 0x2, 0x7)
    OP_29(0x23, 0x2, 0x8)
    OP_29(0x23, 0x2, 0x9)
    OP_29(0x23, 0x2, 0xA)
    OP_29(0x23, 0x2, 0xB)
    OP_29(0x23, 0x2, 0xC)
    OP_29(0x23, 0x2, 0xD)
    OP_29(0x23, 0x2, 0xE)
    OP_29(0x23, 0x2, 0xF)
    OP_29(0x23, 0x2, 0x10)
    OP_29(0x23, 0x2, 0x11)
    OP_29(0x23, 0x2, 0x12)
    OP_29(0x23, 0x2, 0x13)
    OP_29(0x23, 0x2, 0x14)
    OP_29(0x23, 0x2, 0x15)
    OP_29(0x23, 0x2, 0x16)
    OP_29(0x23, 0x2, 0x17)
    OP_29(0x23, 0x2, 0x18)
    OP_29(0x23, 0x2, 0x19)
    OP_29(0x23, 0x2, 0x1A)
    OP_29(0x23, 0x2, 0x1B)
    OP_29(0x23, 0x2, 0x1C)
    OP_29(0x23, 0x2, 0x1D)
    OP_29(0x23, 0x2, 0x1E)
    OP_29(0x23, 0x2, 0x1F)

    label("loc_11A28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11A3C")
    OP_29(0x23, 0x4, 0x2)

    label("loc_11A3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11A51")
    OP_29(0x23, 0x1, 0x0)

    label("loc_11A51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11A66")
    OP_29(0x23, 0x1, 0x1)

    label("loc_11A66")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11A7B")
    OP_29(0x23, 0x1, 0x2)

    label("loc_11A7B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11A90")
    OP_29(0x23, 0x1, 0x3)

    label("loc_11A90")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11AA5")
    OP_29(0x23, 0x1, 0x4)

    label("loc_11AA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11ABA")
    OP_29(0x23, 0x1, 0x5)

    label("loc_11ABA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11ACF")
    OP_29(0x23, 0x1, 0x6)

    label("loc_11ACF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11AE4")
    OP_29(0x23, 0x1, 0x7)

    label("loc_11AE4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11AF9")
    OP_29(0x23, 0x1, 0x8)

    label("loc_11AF9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11B0E")
    OP_29(0x23, 0x1, 0x9)

    label("loc_11B0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11B23")
    OP_29(0x23, 0x1, 0xA)

    label("loc_11B23")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11B38")
    OP_29(0x23, 0x1, 0xB)

    label("loc_11B38")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11B4C")
    OP_29(0x23, 0x4, 0x10)

    label("loc_11B4C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11B60")
    OP_29(0x23, 0x4, 0x20)

    label("loc_11B60")

    Jump("loc_11D8F")

    label("loc_11B65")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11C52")
    OP_29(0x24, 0x3, 0x0)
    OP_29(0x24, 0x3, 0x1)
    OP_29(0x24, 0x3, 0x2)
    OP_29(0x24, 0x3, 0x10)
    OP_29(0x24, 0x3, 0x20)
    OP_29(0x24, 0x3, 0x40)
    OP_29(0x24, 0x2, 0x0)
    OP_29(0x24, 0x2, 0x1)
    OP_29(0x24, 0x2, 0x2)
    OP_29(0x24, 0x2, 0x3)
    OP_29(0x24, 0x2, 0x4)
    OP_29(0x24, 0x2, 0x5)
    OP_29(0x24, 0x2, 0x6)
    OP_29(0x24, 0x2, 0x7)
    OP_29(0x24, 0x2, 0x8)
    OP_29(0x24, 0x2, 0x9)
    OP_29(0x24, 0x2, 0xA)
    OP_29(0x24, 0x2, 0xB)
    OP_29(0x24, 0x2, 0xC)
    OP_29(0x24, 0x2, 0xD)
    OP_29(0x24, 0x2, 0xE)
    OP_29(0x24, 0x2, 0xF)
    OP_29(0x24, 0x2, 0x10)
    OP_29(0x24, 0x2, 0x11)
    OP_29(0x24, 0x2, 0x12)
    OP_29(0x24, 0x2, 0x13)
    OP_29(0x24, 0x2, 0x14)
    OP_29(0x24, 0x2, 0x15)
    OP_29(0x24, 0x2, 0x16)
    OP_29(0x24, 0x2, 0x17)
    OP_29(0x24, 0x2, 0x18)
    OP_29(0x24, 0x2, 0x19)
    OP_29(0x24, 0x2, 0x1A)
    OP_29(0x24, 0x2, 0x1B)
    OP_29(0x24, 0x2, 0x1C)
    OP_29(0x24, 0x2, 0x1D)
    OP_29(0x24, 0x2, 0x1E)
    OP_29(0x24, 0x2, 0x1F)

    label("loc_11C52")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11C66")
    OP_29(0x24, 0x4, 0x2)

    label("loc_11C66")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11C7B")
    OP_29(0x24, 0x1, 0x0)

    label("loc_11C7B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11C90")
    OP_29(0x24, 0x1, 0x1)

    label("loc_11C90")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11CA5")
    OP_29(0x24, 0x1, 0x2)

    label("loc_11CA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11CBA")
    OP_29(0x24, 0x1, 0x3)

    label("loc_11CBA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11CCF")
    OP_29(0x24, 0x1, 0x4)

    label("loc_11CCF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11CE4")
    OP_29(0x24, 0x1, 0x5)

    label("loc_11CE4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11CF9")
    OP_29(0x24, 0x1, 0x6)

    label("loc_11CF9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11D0E")
    OP_29(0x24, 0x1, 0x7)

    label("loc_11D0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11D23")
    OP_29(0x24, 0x1, 0x8)

    label("loc_11D23")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11D38")
    OP_29(0x24, 0x1, 0x9)

    label("loc_11D38")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11D4D")
    OP_29(0x24, 0x1, 0xA)

    label("loc_11D4D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11D62")
    OP_29(0x24, 0x1, 0xB)

    label("loc_11D62")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11D76")
    OP_29(0x24, 0x4, 0x10)

    label("loc_11D76")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_11D8A")
    OP_29(0x24, 0x4, 0x20)

    label("loc_11D8A")

    Jump("loc_11D8F")

    label("loc_11D8F")

    Jump("loc_EDAE")

    label("loc_11D94")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_57_EDA4 end

    def Function_58_11DAC(): pass

    label("Function_58_11DAC")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11DB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_125A0")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "----------幕間--------------\x01",        # 0
            "QS_0401  手配魔獣⑨           \x01",      # 1
            "QS_0402  市長への差し入れ     \x01",      # 2
            "QS_0403  日曜学校の臨時講師   \x01",      # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_11E67"),
        (2, "loc_11E67"),
        (3, "loc_11E67"),
        (SWITCH_DEFAULT, "loc_11EE0"),
    )


    label("loc_11E67")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期化\x01",      # 0
            "開始\x01",        # 1
            "QF_01\x01",       # 2
            "QF_02\x01",       # 3
            "QF_03\x01",       # 4
            "QF_04\x01",       # 5
            "QF_05\x01",       # 6
            "QF_06\x01",       # 7
            "QF_07\x01",       # 8
            "QF_08\x01",       # 9
            "QF_09\x01",       # 10
            "QF_10\x01",       # 11
            "QF_11\x01",       # 12
            "QF_12\x01",       # 13
            "達成\x01",        # 14
            "報告\x01",        # 15
        )
    )

    MenuEnd(0x5)
    Jump("loc_11EEF")

    label("loc_11EE0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_11EEF")

    label("loc_11EEF")

    OP_60(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1259B")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_11F1D"),
        (2, "loc_12147"),
        (3, "loc_12371"),
        (SWITCH_DEFAULT, "loc_1259B"),
    )


    label("loc_11F1D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1200A")
    OP_29(0x25, 0x3, 0x0)
    OP_29(0x25, 0x3, 0x1)
    OP_29(0x25, 0x3, 0x2)
    OP_29(0x25, 0x3, 0x10)
    OP_29(0x25, 0x3, 0x20)
    OP_29(0x25, 0x3, 0x40)
    OP_29(0x25, 0x2, 0x0)
    OP_29(0x25, 0x2, 0x1)
    OP_29(0x25, 0x2, 0x2)
    OP_29(0x25, 0x2, 0x3)
    OP_29(0x25, 0x2, 0x4)
    OP_29(0x25, 0x2, 0x5)
    OP_29(0x25, 0x2, 0x6)
    OP_29(0x25, 0x2, 0x7)
    OP_29(0x25, 0x2, 0x8)
    OP_29(0x25, 0x2, 0x9)
    OP_29(0x25, 0x2, 0xA)
    OP_29(0x25, 0x2, 0xB)
    OP_29(0x25, 0x2, 0xC)
    OP_29(0x25, 0x2, 0xD)
    OP_29(0x25, 0x2, 0xE)
    OP_29(0x25, 0x2, 0xF)
    OP_29(0x25, 0x2, 0x10)
    OP_29(0x25, 0x2, 0x11)
    OP_29(0x25, 0x2, 0x12)
    OP_29(0x25, 0x2, 0x13)
    OP_29(0x25, 0x2, 0x14)
    OP_29(0x25, 0x2, 0x15)
    OP_29(0x25, 0x2, 0x16)
    OP_29(0x25, 0x2, 0x17)
    OP_29(0x25, 0x2, 0x18)
    OP_29(0x25, 0x2, 0x19)
    OP_29(0x25, 0x2, 0x1A)
    OP_29(0x25, 0x2, 0x1B)
    OP_29(0x25, 0x2, 0x1C)
    OP_29(0x25, 0x2, 0x1D)
    OP_29(0x25, 0x2, 0x1E)
    OP_29(0x25, 0x2, 0x1F)

    label("loc_1200A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1201E")
    OP_29(0x25, 0x4, 0x2)

    label("loc_1201E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12033")
    OP_29(0x25, 0x1, 0x0)

    label("loc_12033")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12048")
    OP_29(0x25, 0x1, 0x1)

    label("loc_12048")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1205D")
    OP_29(0x25, 0x1, 0x2)

    label("loc_1205D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12072")
    OP_29(0x25, 0x1, 0x3)

    label("loc_12072")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12087")
    OP_29(0x25, 0x1, 0x4)

    label("loc_12087")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1209C")
    OP_29(0x25, 0x1, 0x5)

    label("loc_1209C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_120B1")
    OP_29(0x25, 0x1, 0x6)

    label("loc_120B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_120C6")
    OP_29(0x25, 0x1, 0x7)

    label("loc_120C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_120DB")
    OP_29(0x25, 0x1, 0x8)

    label("loc_120DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_120F0")
    OP_29(0x25, 0x1, 0x9)

    label("loc_120F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12105")
    OP_29(0x25, 0x1, 0xA)

    label("loc_12105")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1211A")
    OP_29(0x25, 0x1, 0xB)

    label("loc_1211A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1212E")
    OP_29(0x25, 0x4, 0x10)

    label("loc_1212E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12142")
    OP_29(0x25, 0x4, 0x20)

    label("loc_12142")

    Jump("loc_1259B")

    label("loc_12147")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12234")
    OP_29(0x26, 0x3, 0x0)
    OP_29(0x26, 0x3, 0x1)
    OP_29(0x26, 0x3, 0x2)
    OP_29(0x26, 0x3, 0x10)
    OP_29(0x26, 0x3, 0x20)
    OP_29(0x26, 0x3, 0x40)
    OP_29(0x26, 0x2, 0x0)
    OP_29(0x26, 0x2, 0x1)
    OP_29(0x26, 0x2, 0x2)
    OP_29(0x26, 0x2, 0x3)
    OP_29(0x26, 0x2, 0x4)
    OP_29(0x26, 0x2, 0x5)
    OP_29(0x26, 0x2, 0x6)
    OP_29(0x26, 0x2, 0x7)
    OP_29(0x26, 0x2, 0x8)
    OP_29(0x26, 0x2, 0x9)
    OP_29(0x26, 0x2, 0xA)
    OP_29(0x26, 0x2, 0xB)
    OP_29(0x26, 0x2, 0xC)
    OP_29(0x26, 0x2, 0xD)
    OP_29(0x26, 0x2, 0xE)
    OP_29(0x26, 0x2, 0xF)
    OP_29(0x26, 0x2, 0x10)
    OP_29(0x26, 0x2, 0x11)
    OP_29(0x26, 0x2, 0x12)
    OP_29(0x26, 0x2, 0x13)
    OP_29(0x26, 0x2, 0x14)
    OP_29(0x26, 0x2, 0x15)
    OP_29(0x26, 0x2, 0x16)
    OP_29(0x26, 0x2, 0x17)
    OP_29(0x26, 0x2, 0x18)
    OP_29(0x26, 0x2, 0x19)
    OP_29(0x26, 0x2, 0x1A)
    OP_29(0x26, 0x2, 0x1B)
    OP_29(0x26, 0x2, 0x1C)
    OP_29(0x26, 0x2, 0x1D)
    OP_29(0x26, 0x2, 0x1E)
    OP_29(0x26, 0x2, 0x1F)

    label("loc_12234")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12248")
    OP_29(0x26, 0x4, 0x2)

    label("loc_12248")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1225D")
    OP_29(0x26, 0x1, 0x0)

    label("loc_1225D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12272")
    OP_29(0x26, 0x1, 0x1)

    label("loc_12272")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12287")
    OP_29(0x26, 0x1, 0x2)

    label("loc_12287")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1229C")
    OP_29(0x26, 0x1, 0x3)

    label("loc_1229C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_122B1")
    OP_29(0x26, 0x1, 0x4)

    label("loc_122B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_122C6")
    OP_29(0x26, 0x1, 0x5)

    label("loc_122C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_122DB")
    OP_29(0x26, 0x1, 0x6)

    label("loc_122DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_122F0")
    OP_29(0x26, 0x1, 0x7)

    label("loc_122F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12305")
    OP_29(0x26, 0x1, 0x8)

    label("loc_12305")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1231A")
    OP_29(0x26, 0x1, 0x9)

    label("loc_1231A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1232F")
    OP_29(0x26, 0x1, 0xA)

    label("loc_1232F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12344")
    OP_29(0x26, 0x1, 0xB)

    label("loc_12344")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12358")
    OP_29(0x26, 0x4, 0x10)

    label("loc_12358")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1236C")
    OP_29(0x26, 0x4, 0x20)

    label("loc_1236C")

    Jump("loc_1259B")

    label("loc_12371")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1245E")
    OP_29(0x27, 0x3, 0x0)
    OP_29(0x27, 0x3, 0x1)
    OP_29(0x27, 0x3, 0x2)
    OP_29(0x27, 0x3, 0x10)
    OP_29(0x27, 0x3, 0x20)
    OP_29(0x27, 0x3, 0x40)
    OP_29(0x27, 0x2, 0x0)
    OP_29(0x27, 0x2, 0x1)
    OP_29(0x27, 0x2, 0x2)
    OP_29(0x27, 0x2, 0x3)
    OP_29(0x27, 0x2, 0x4)
    OP_29(0x27, 0x2, 0x5)
    OP_29(0x27, 0x2, 0x6)
    OP_29(0x27, 0x2, 0x7)
    OP_29(0x27, 0x2, 0x8)
    OP_29(0x27, 0x2, 0x9)
    OP_29(0x27, 0x2, 0xA)
    OP_29(0x27, 0x2, 0xB)
    OP_29(0x27, 0x2, 0xC)
    OP_29(0x27, 0x2, 0xD)
    OP_29(0x27, 0x2, 0xE)
    OP_29(0x27, 0x2, 0xF)
    OP_29(0x27, 0x2, 0x10)
    OP_29(0x27, 0x2, 0x11)
    OP_29(0x27, 0x2, 0x12)
    OP_29(0x27, 0x2, 0x13)
    OP_29(0x27, 0x2, 0x14)
    OP_29(0x27, 0x2, 0x15)
    OP_29(0x27, 0x2, 0x16)
    OP_29(0x27, 0x2, 0x17)
    OP_29(0x27, 0x2, 0x18)
    OP_29(0x27, 0x2, 0x19)
    OP_29(0x27, 0x2, 0x1A)
    OP_29(0x27, 0x2, 0x1B)
    OP_29(0x27, 0x2, 0x1C)
    OP_29(0x27, 0x2, 0x1D)
    OP_29(0x27, 0x2, 0x1E)
    OP_29(0x27, 0x2, 0x1F)

    label("loc_1245E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12472")
    OP_29(0x27, 0x4, 0x2)

    label("loc_12472")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12487")
    OP_29(0x27, 0x1, 0x0)

    label("loc_12487")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1249C")
    OP_29(0x27, 0x1, 0x1)

    label("loc_1249C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_124B1")
    OP_29(0x27, 0x1, 0x2)

    label("loc_124B1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_124C6")
    OP_29(0x27, 0x1, 0x3)

    label("loc_124C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_124DB")
    OP_29(0x27, 0x1, 0x4)

    label("loc_124DB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_124F0")
    OP_29(0x27, 0x1, 0x5)

    label("loc_124F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12505")
    OP_29(0x27, 0x1, 0x6)

    label("loc_12505")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1251A")
    OP_29(0x27, 0x1, 0x7)

    label("loc_1251A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1252F")
    OP_29(0x27, 0x1, 0x8)

    label("loc_1252F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12544")
    OP_29(0x27, 0x1, 0x9)

    label("loc_12544")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12559")
    OP_29(0x27, 0x1, 0xA)

    label("loc_12559")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1256E")
    OP_29(0x27, 0x1, 0xB)

    label("loc_1256E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12582")
    OP_29(0x27, 0x4, 0x10)

    label("loc_12582")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12596")
    OP_29(0x27, 0x4, 0x20)

    label("loc_12596")

    Jump("loc_1259B")

    label("loc_1259B")

    Jump("loc_11DB6")

    label("loc_125A0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_58_11DAC end

    def Function_59_125B8(): pass

    label("Function_59_125B8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_125C2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14AD4")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "----------４章--------------\x01",        # 0
            "QS_0501  延滞本の回収２       \x01",      # 1
            "QS_0502  求む創作料理         \x01",      # 2
            "QS_0503  一目惚れのあの子     \x01",      # 3
            "QS_0504  手配魔獣⑩           \x01",      # 4
            "QS_0505  父へのプレゼント     \x01",      # 5
            "QS_0506  議員令嬢の捜索       \x01",      # 6
            "QS_0507  鎮魂の花集め         \x01",      # 7
            "QS_0508  手配魔獣?           \x01",       # 8
            "QS_0509  特注人形の受け取り   \x01",      # 9
            "QS_0510  魔導杖の新機能開発   \x01",      # 10
            "QS_0511  手配魔獣?           \x01",       # 11
            "QS_0512  手配魔獣?           \x01",       # 12
            "----------終章--------------\x01",        # 13
            "QS_0601  ジオＢの異変調査     \x01",      # 14
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_127FF"),
        (5, "loc_12929"),
        (6, "loc_12A06"),
        (7, "loc_12C28"),
        (2, "loc_12D16"),
        (3, "loc_12D16"),
        (4, "loc_12D16"),
        (8, "loc_12D16"),
        (9, "loc_12D16"),
        (10, "loc_12D16"),
        (11, "loc_12D16"),
        (12, "loc_12D16"),
        (14, "loc_12D16"),
        (SWITCH_DEFAULT, "loc_12D8F"),
    )


    label("loc_127FF")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期化\x01",                       # 0
            "開始\x01",                         # 1
            "QF_01依頼内容を聞いた\x01",        # 2
            "QF_02依頼を引き受けた\x01",        # 3
            "QF_03アルフレッドと話す\x01",      # 4
            "QF_04エルキンと話す\x01",          # 5
            "QF_05ドナルドと話す\x01",          # 6
            "QF_06アルフレッド本回収\x01",      # 7
            "QF_07ロージーと話す\x01",          # 8
            "QF_08ロージー本回収\x01",          # 9
            "QF_09フローラと話す\x01",          # 10
            "QF_10資料室に入る\x01",            # 11
            "QF_11フローラ本回収\x01",          # 12
            "全ての本を回収した\x01",           # 13
            "達成\x01",                         # 14
            "報告\x01",                         # 15
        )
    )

    MenuEnd(0x5)
    Jump("loc_12D9E")

    label("loc_12929")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期化\x01",                              # 0
            "開始（セシルorシズクと話した）\x01",      # 1
            "QF_01\x09",                               # 2
            "★01 ミハイルと話した\x01",               # 3
            "QF_02\x09",                               # 4
            "★02 メイファと話した\x01",               # 5
            "QF_03\x09",                               # 6
            "★03 アーシュラと話した\x01",             # 7
            "QF_04\x09",                               # 8
            "★04 ゲイリー教授と話した\x01",           # 9
            "QF_05\x09",                               # 10
            "★05 コンテナを調べた\x01",               # 11
            "達成\x01",                                # 12
            "報告\x01",                                # 13
        )
    )

    MenuEnd(0x5)
    Jump("loc_12D9E")

    label("loc_12A06")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期化\x01",                          # 0
            "開始\x01",                            # 1
            "QF_01 キャンベル邸にきた\x01",        # 2
            "QF_02 書き置きを確認しよう\x01",      # 3
            "QF_03 ★聞き込み\x01",                # 4
            "QF_04 ★聞き込み\x01",                # 5
            "QF_05 話を聞いてこよう\x01",          # 6
            "QF_06 IBCへ行こう！\x01",             # 7
            "QF_07 ランフィに話を聞こう\x01",      # 8
            "QF_08 総裁室に行こう\x01",            # 9
            "QF_09 空港に急ごう！\x01",            # 10
            "QF_10 駅に急げ！\x01",                # 11
            "【→次へ】\x01",                      # 12
        )
    )

    MenuEnd(0x5)
    OP_60(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C23")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "QF_13 列車内でカーラを探そう\x01",        # 0
            "QF_14 カーラを説得してみよう！\x01",      # 1
            "QF_15 説得成功！\x01",                    # 2
            "QF_16 説得は失敗したが……\x01",          # 3
            "【C0800列車に乗り込む】\x01",             # 4
            "【R0040走る列車シーン】\x01",             # 5
            "【C0800帰ってきた?成功版】\x01",          # 6
            "【C0800帰ってきた?失敗版】\x01",          # 7
            "達成\x01",                                # 8
            "報告\x01",                                # 9
        )
    )

    MenuEnd(0x5)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12C23")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_12C23")

    Jump("loc_12D9E")

    label("loc_12C28")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期化\x01",                            # 0
            "開始\x01",                              # 1
            "QF_01★01 依頼内容を聞いた\x01",        # 2
            "QF_02★02 依頼を引き受けた\x01",        # 3
            "QF_03★03 レヴァスの花を入手\x01",      # 4
            "QF_04★04 タリーズと話した\x01",        # 5
            "QF_05★05 リクエムの花を入手\x01",      # 6
            "QF_06★06 フィネルの花を入手\x01",      # 7
            "QF_07★07 花を渡した\x01",              # 8
            "達成\x01",                              # 9
            "報告\x01",                              # 10
        )
    )

    MenuEnd(0x5)
    Jump("loc_12D9E")

    label("loc_12D16")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "初期化\x01",      # 0
            "開始\x01",        # 1
            "QF_01\x01",       # 2
            "QF_02\x01",       # 3
            "QF_03\x01",       # 4
            "QF_04\x01",       # 5
            "QF_05\x01",       # 6
            "QF_06\x01",       # 7
            "QF_07\x01",       # 8
            "QF_08\x01",       # 9
            "QF_09\x01",       # 10
            "QF_10\x01",       # 11
            "QF_11\x01",       # 12
            "QF_12\x01",       # 13
            "達成\x01",        # 14
            "報告\x01",        # 15
        )
    )

    MenuEnd(0x5)
    Jump("loc_12D9E")

    label("loc_12D8F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_12D9E")

    label("loc_12D9E")

    OP_60(0x2)
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_14ACF")
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_12E08"),
        (2, "loc_1311C"),
        (3, "loc_13346"),
        (4, "loc_13570"),
        (5, "loc_1379A"),
        (6, "loc_13931"),
        (7, "loc_13C12"),
        (8, "loc_13DD3"),
        (9, "loc_13FFD"),
        (10, "loc_14227"),
        (11, "loc_14451"),
        (12, "loc_1467B"),
        (14, "loc_148A5"),
        (SWITCH_DEFAULT, "loc_14ACF"),
    )


    label("loc_12E08")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12EF5")
    OP_29(0x28, 0x3, 0x0)
    OP_29(0x28, 0x3, 0x1)
    OP_29(0x28, 0x3, 0x2)
    OP_29(0x28, 0x3, 0x10)
    OP_29(0x28, 0x3, 0x20)
    OP_29(0x28, 0x3, 0x40)
    OP_29(0x28, 0x2, 0x0)
    OP_29(0x28, 0x2, 0x1)
    OP_29(0x28, 0x2, 0x2)
    OP_29(0x28, 0x2, 0x3)
    OP_29(0x28, 0x2, 0x4)
    OP_29(0x28, 0x2, 0x5)
    OP_29(0x28, 0x2, 0x6)
    OP_29(0x28, 0x2, 0x7)
    OP_29(0x28, 0x2, 0x8)
    OP_29(0x28, 0x2, 0x9)
    OP_29(0x28, 0x2, 0xA)
    OP_29(0x28, 0x2, 0xB)
    OP_29(0x28, 0x2, 0xC)
    OP_29(0x28, 0x2, 0xD)
    OP_29(0x28, 0x2, 0xE)
    OP_29(0x28, 0x2, 0xF)
    OP_29(0x28, 0x2, 0x10)
    OP_29(0x28, 0x2, 0x11)
    OP_29(0x28, 0x2, 0x12)
    OP_29(0x28, 0x2, 0x13)
    OP_29(0x28, 0x2, 0x14)
    OP_29(0x28, 0x2, 0x15)
    OP_29(0x28, 0x2, 0x16)
    OP_29(0x28, 0x2, 0x17)
    OP_29(0x28, 0x2, 0x18)
    OP_29(0x28, 0x2, 0x19)
    OP_29(0x28, 0x2, 0x1A)
    OP_29(0x28, 0x2, 0x1B)
    OP_29(0x28, 0x2, 0x1C)
    OP_29(0x28, 0x2, 0x1D)
    OP_29(0x28, 0x2, 0x1E)
    OP_29(0x28, 0x2, 0x1F)

    label("loc_12EF5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12F09")
    OP_29(0x28, 0x4, 0x2)

    label("loc_12F09")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12F23")
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x1, 0x0)

    label("loc_12F23")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12F3D")
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x1, 0x1)

    label("loc_12F3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12F5D")
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x1, 0x1)
    OP_29(0x28, 0x1, 0x2)

    label("loc_12F5D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12F83")
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x1, 0x1)
    OP_29(0x28, 0x1, 0x2)
    OP_29(0x28, 0x1, 0x3)

    label("loc_12F83")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12FAF")
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x1, 0x1)
    OP_29(0x28, 0x1, 0x2)
    OP_29(0x28, 0x1, 0x3)
    OP_29(0x28, 0x1, 0x4)

    label("loc_12FAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_12FE1")
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x1, 0x1)
    OP_29(0x28, 0x1, 0x2)
    OP_29(0x28, 0x1, 0x3)
    OP_29(0x28, 0x1, 0x4)
    OP_29(0x28, 0x1, 0x5)

    label("loc_12FE1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13001")
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x1, 0x1)
    OP_29(0x28, 0x1, 0x6)

    label("loc_13001")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13027")
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x1, 0x1)
    OP_29(0x28, 0x1, 0x6)
    OP_29(0x28, 0x1, 0x7)

    label("loc_13027")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13047")
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x1, 0x1)
    OP_29(0x28, 0x1, 0x8)

    label("loc_13047")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1306D")
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x1, 0x1)
    OP_29(0x28, 0x1, 0x8)
    OP_29(0x28, 0x1, 0x9)

    label("loc_1306D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13099")
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x1, 0x1)
    OP_29(0x28, 0x1, 0x8)
    OP_29(0x28, 0x1, 0x9)
    OP_29(0x28, 0x1, 0xA)

    label("loc_13099")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_130E9")
    OP_29(0x28, 0x4, 0x2)
    OP_29(0x28, 0x1, 0x1)
    OP_29(0x28, 0x1, 0x2)
    OP_29(0x28, 0x1, 0x3)
    OP_29(0x28, 0x1, 0x4)
    OP_29(0x28, 0x1, 0x5)
    OP_29(0x28, 0x1, 0x6)
    OP_29(0x28, 0x1, 0x7)
    OP_29(0x28, 0x1, 0x8)
    OP_29(0x28, 0x1, 0x9)
    OP_29(0x28, 0x1, 0xA)

    label("loc_130E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13103")
    OP_29(0x28, 0x1, 0xB)
    OP_29(0x28, 0x4, 0x10)

    label("loc_13103")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13117")
    OP_29(0x28, 0x4, 0x20)

    label("loc_13117")

    Jump("loc_14ACF")

    label("loc_1311C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13209")
    OP_29(0x29, 0x3, 0x0)
    OP_29(0x29, 0x3, 0x1)
    OP_29(0x29, 0x3, 0x2)
    OP_29(0x29, 0x3, 0x10)
    OP_29(0x29, 0x3, 0x20)
    OP_29(0x29, 0x3, 0x40)
    OP_29(0x29, 0x2, 0x0)
    OP_29(0x29, 0x2, 0x1)
    OP_29(0x29, 0x2, 0x2)
    OP_29(0x29, 0x2, 0x3)
    OP_29(0x29, 0x2, 0x4)
    OP_29(0x29, 0x2, 0x5)
    OP_29(0x29, 0x2, 0x6)
    OP_29(0x29, 0x2, 0x7)
    OP_29(0x29, 0x2, 0x8)
    OP_29(0x29, 0x2, 0x9)
    OP_29(0x29, 0x2, 0xA)
    OP_29(0x29, 0x2, 0xB)
    OP_29(0x29, 0x2, 0xC)
    OP_29(0x29, 0x2, 0xD)
    OP_29(0x29, 0x2, 0xE)
    OP_29(0x29, 0x2, 0xF)
    OP_29(0x29, 0x2, 0x10)
    OP_29(0x29, 0x2, 0x11)
    OP_29(0x29, 0x2, 0x12)
    OP_29(0x29, 0x2, 0x13)
    OP_29(0x29, 0x2, 0x14)
    OP_29(0x29, 0x2, 0x15)
    OP_29(0x29, 0x2, 0x16)
    OP_29(0x29, 0x2, 0x17)
    OP_29(0x29, 0x2, 0x18)
    OP_29(0x29, 0x2, 0x19)
    OP_29(0x29, 0x2, 0x1A)
    OP_29(0x29, 0x2, 0x1B)
    OP_29(0x29, 0x2, 0x1C)
    OP_29(0x29, 0x2, 0x1D)
    OP_29(0x29, 0x2, 0x1E)
    OP_29(0x29, 0x2, 0x1F)

    label("loc_13209")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1321D")
    OP_29(0x29, 0x4, 0x2)

    label("loc_1321D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13232")
    OP_29(0x29, 0x1, 0x0)

    label("loc_13232")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13247")
    OP_29(0x29, 0x1, 0x1)

    label("loc_13247")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1325C")
    OP_29(0x29, 0x1, 0x2)

    label("loc_1325C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13271")
    OP_29(0x29, 0x1, 0x3)

    label("loc_13271")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13286")
    OP_29(0x29, 0x1, 0x4)

    label("loc_13286")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1329B")
    OP_29(0x29, 0x1, 0x5)

    label("loc_1329B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_132B0")
    OP_29(0x29, 0x1, 0x6)

    label("loc_132B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_132C5")
    OP_29(0x29, 0x1, 0x7)

    label("loc_132C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_132DA")
    OP_29(0x29, 0x1, 0x8)

    label("loc_132DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_132EF")
    OP_29(0x29, 0x1, 0x9)

    label("loc_132EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13304")
    OP_29(0x29, 0x1, 0xA)

    label("loc_13304")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13319")
    OP_29(0x29, 0x1, 0xB)

    label("loc_13319")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1332D")
    OP_29(0x29, 0x4, 0x10)

    label("loc_1332D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13341")
    OP_29(0x29, 0x4, 0x20)

    label("loc_13341")

    Jump("loc_14ACF")

    label("loc_13346")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13433")
    OP_29(0x2A, 0x3, 0x0)
    OP_29(0x2A, 0x3, 0x1)
    OP_29(0x2A, 0x3, 0x2)
    OP_29(0x2A, 0x3, 0x10)
    OP_29(0x2A, 0x3, 0x20)
    OP_29(0x2A, 0x3, 0x40)
    OP_29(0x2A, 0x2, 0x0)
    OP_29(0x2A, 0x2, 0x1)
    OP_29(0x2A, 0x2, 0x2)
    OP_29(0x2A, 0x2, 0x3)
    OP_29(0x2A, 0x2, 0x4)
    OP_29(0x2A, 0x2, 0x5)
    OP_29(0x2A, 0x2, 0x6)
    OP_29(0x2A, 0x2, 0x7)
    OP_29(0x2A, 0x2, 0x8)
    OP_29(0x2A, 0x2, 0x9)
    OP_29(0x2A, 0x2, 0xA)
    OP_29(0x2A, 0x2, 0xB)
    OP_29(0x2A, 0x2, 0xC)
    OP_29(0x2A, 0x2, 0xD)
    OP_29(0x2A, 0x2, 0xE)
    OP_29(0x2A, 0x2, 0xF)
    OP_29(0x2A, 0x2, 0x10)
    OP_29(0x2A, 0x2, 0x11)
    OP_29(0x2A, 0x2, 0x12)
    OP_29(0x2A, 0x2, 0x13)
    OP_29(0x2A, 0x2, 0x14)
    OP_29(0x2A, 0x2, 0x15)
    OP_29(0x2A, 0x2, 0x16)
    OP_29(0x2A, 0x2, 0x17)
    OP_29(0x2A, 0x2, 0x18)
    OP_29(0x2A, 0x2, 0x19)
    OP_29(0x2A, 0x2, 0x1A)
    OP_29(0x2A, 0x2, 0x1B)
    OP_29(0x2A, 0x2, 0x1C)
    OP_29(0x2A, 0x2, 0x1D)
    OP_29(0x2A, 0x2, 0x1E)
    OP_29(0x2A, 0x2, 0x1F)

    label("loc_13433")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13447")
    OP_29(0x2A, 0x4, 0x2)

    label("loc_13447")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1345C")
    OP_29(0x2A, 0x1, 0x0)

    label("loc_1345C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13471")
    OP_29(0x2A, 0x1, 0x1)

    label("loc_13471")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13486")
    OP_29(0x2A, 0x1, 0x2)

    label("loc_13486")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1349B")
    OP_29(0x2A, 0x1, 0x3)

    label("loc_1349B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_134B0")
    OP_29(0x2A, 0x1, 0x4)

    label("loc_134B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_134C5")
    OP_29(0x2A, 0x1, 0x5)

    label("loc_134C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_134DA")
    OP_29(0x2A, 0x1, 0x6)

    label("loc_134DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_134EF")
    OP_29(0x2A, 0x1, 0x7)

    label("loc_134EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13504")
    OP_29(0x2A, 0x1, 0x8)

    label("loc_13504")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13519")
    OP_29(0x2A, 0x1, 0x9)

    label("loc_13519")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1352E")
    OP_29(0x2A, 0x1, 0xA)

    label("loc_1352E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13543")
    OP_29(0x2A, 0x1, 0xB)

    label("loc_13543")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13557")
    OP_29(0x2A, 0x4, 0x10)

    label("loc_13557")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1356B")
    OP_29(0x2A, 0x4, 0x20)

    label("loc_1356B")

    Jump("loc_14ACF")

    label("loc_13570")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1365D")
    OP_29(0x2B, 0x3, 0x0)
    OP_29(0x2B, 0x3, 0x1)
    OP_29(0x2B, 0x3, 0x2)
    OP_29(0x2B, 0x3, 0x10)
    OP_29(0x2B, 0x3, 0x20)
    OP_29(0x2B, 0x3, 0x40)
    OP_29(0x2B, 0x2, 0x0)
    OP_29(0x2B, 0x2, 0x1)
    OP_29(0x2B, 0x2, 0x2)
    OP_29(0x2B, 0x2, 0x3)
    OP_29(0x2B, 0x2, 0x4)
    OP_29(0x2B, 0x2, 0x5)
    OP_29(0x2B, 0x2, 0x6)
    OP_29(0x2B, 0x2, 0x7)
    OP_29(0x2B, 0x2, 0x8)
    OP_29(0x2B, 0x2, 0x9)
    OP_29(0x2B, 0x2, 0xA)
    OP_29(0x2B, 0x2, 0xB)
    OP_29(0x2B, 0x2, 0xC)
    OP_29(0x2B, 0x2, 0xD)
    OP_29(0x2B, 0x2, 0xE)
    OP_29(0x2B, 0x2, 0xF)
    OP_29(0x2B, 0x2, 0x10)
    OP_29(0x2B, 0x2, 0x11)
    OP_29(0x2B, 0x2, 0x12)
    OP_29(0x2B, 0x2, 0x13)
    OP_29(0x2B, 0x2, 0x14)
    OP_29(0x2B, 0x2, 0x15)
    OP_29(0x2B, 0x2, 0x16)
    OP_29(0x2B, 0x2, 0x17)
    OP_29(0x2B, 0x2, 0x18)
    OP_29(0x2B, 0x2, 0x19)
    OP_29(0x2B, 0x2, 0x1A)
    OP_29(0x2B, 0x2, 0x1B)
    OP_29(0x2B, 0x2, 0x1C)
    OP_29(0x2B, 0x2, 0x1D)
    OP_29(0x2B, 0x2, 0x1E)
    OP_29(0x2B, 0x2, 0x1F)

    label("loc_1365D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13671")
    OP_29(0x2B, 0x4, 0x2)

    label("loc_13671")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13686")
    OP_29(0x2B, 0x1, 0x0)

    label("loc_13686")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1369B")
    OP_29(0x2B, 0x1, 0x1)

    label("loc_1369B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_136B0")
    OP_29(0x2B, 0x1, 0x2)

    label("loc_136B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_136C5")
    OP_29(0x2B, 0x1, 0x3)

    label("loc_136C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_136DA")
    OP_29(0x2B, 0x1, 0x4)

    label("loc_136DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_136EF")
    OP_29(0x2B, 0x1, 0x5)

    label("loc_136EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13704")
    OP_29(0x2B, 0x1, 0x6)

    label("loc_13704")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13719")
    OP_29(0x2B, 0x1, 0x7)

    label("loc_13719")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1372E")
    OP_29(0x2B, 0x1, 0x8)

    label("loc_1372E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13743")
    OP_29(0x2B, 0x1, 0x9)

    label("loc_13743")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13758")
    OP_29(0x2B, 0x1, 0xA)

    label("loc_13758")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1376D")
    OP_29(0x2B, 0x1, 0xB)

    label("loc_1376D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13781")
    OP_29(0x2B, 0x4, 0x10)

    label("loc_13781")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13795")
    OP_29(0x2B, 0x4, 0x20)

    label("loc_13795")

    Jump("loc_14ACF")

    label("loc_1379A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13887")
    OP_29(0x2C, 0x3, 0x0)
    OP_29(0x2C, 0x3, 0x1)
    OP_29(0x2C, 0x3, 0x2)
    OP_29(0x2C, 0x3, 0x10)
    OP_29(0x2C, 0x3, 0x20)
    OP_29(0x2C, 0x3, 0x40)
    OP_29(0x2C, 0x2, 0x0)
    OP_29(0x2C, 0x2, 0x1)
    OP_29(0x2C, 0x2, 0x2)
    OP_29(0x2C, 0x2, 0x3)
    OP_29(0x2C, 0x2, 0x4)
    OP_29(0x2C, 0x2, 0x5)
    OP_29(0x2C, 0x2, 0x6)
    OP_29(0x2C, 0x2, 0x7)
    OP_29(0x2C, 0x2, 0x8)
    OP_29(0x2C, 0x2, 0x9)
    OP_29(0x2C, 0x2, 0xA)
    OP_29(0x2C, 0x2, 0xB)
    OP_29(0x2C, 0x2, 0xC)
    OP_29(0x2C, 0x2, 0xD)
    OP_29(0x2C, 0x2, 0xE)
    OP_29(0x2C, 0x2, 0xF)
    OP_29(0x2C, 0x2, 0x10)
    OP_29(0x2C, 0x2, 0x11)
    OP_29(0x2C, 0x2, 0x12)
    OP_29(0x2C, 0x2, 0x13)
    OP_29(0x2C, 0x2, 0x14)
    OP_29(0x2C, 0x2, 0x15)
    OP_29(0x2C, 0x2, 0x16)
    OP_29(0x2C, 0x2, 0x17)
    OP_29(0x2C, 0x2, 0x18)
    OP_29(0x2C, 0x2, 0x19)
    OP_29(0x2C, 0x2, 0x1A)
    OP_29(0x2C, 0x2, 0x1B)
    OP_29(0x2C, 0x2, 0x1C)
    OP_29(0x2C, 0x2, 0x1D)
    OP_29(0x2C, 0x2, 0x1E)
    OP_29(0x2C, 0x2, 0x1F)

    label("loc_13887")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1389B")
    OP_29(0x2C, 0x4, 0x2)

    label("loc_1389B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_138B0")
    OP_29(0x2C, 0x1, 0x0)

    label("loc_138B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_138C5")
    OP_29(0x2C, 0x1, 0x1)

    label("loc_138C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_138DA")
    OP_29(0x2C, 0x1, 0x2)

    label("loc_138DA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_138EF")
    OP_29(0x2C, 0x1, 0x3)

    label("loc_138EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13904")
    OP_29(0x2C, 0x1, 0x4)

    label("loc_13904")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13918")
    OP_29(0x2C, 0x4, 0x10)

    label("loc_13918")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1392C")
    OP_29(0x2C, 0x4, 0x20)

    label("loc_1392C")

    Jump("loc_14ACF")

    label("loc_13931")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13A1E")
    OP_29(0x2D, 0x3, 0x0)
    OP_29(0x2D, 0x3, 0x1)
    OP_29(0x2D, 0x3, 0x2)
    OP_29(0x2D, 0x3, 0x10)
    OP_29(0x2D, 0x3, 0x20)
    OP_29(0x2D, 0x3, 0x40)
    OP_29(0x2D, 0x2, 0x0)
    OP_29(0x2D, 0x2, 0x1)
    OP_29(0x2D, 0x2, 0x2)
    OP_29(0x2D, 0x2, 0x3)
    OP_29(0x2D, 0x2, 0x4)
    OP_29(0x2D, 0x2, 0x5)
    OP_29(0x2D, 0x2, 0x6)
    OP_29(0x2D, 0x2, 0x7)
    OP_29(0x2D, 0x2, 0x8)
    OP_29(0x2D, 0x2, 0x9)
    OP_29(0x2D, 0x2, 0xA)
    OP_29(0x2D, 0x2, 0xB)
    OP_29(0x2D, 0x2, 0xC)
    OP_29(0x2D, 0x2, 0xD)
    OP_29(0x2D, 0x2, 0xE)
    OP_29(0x2D, 0x2, 0xF)
    OP_29(0x2D, 0x2, 0x10)
    OP_29(0x2D, 0x2, 0x11)
    OP_29(0x2D, 0x2, 0x12)
    OP_29(0x2D, 0x2, 0x13)
    OP_29(0x2D, 0x2, 0x14)
    OP_29(0x2D, 0x2, 0x15)
    OP_29(0x2D, 0x2, 0x16)
    OP_29(0x2D, 0x2, 0x17)
    OP_29(0x2D, 0x2, 0x18)
    OP_29(0x2D, 0x2, 0x19)
    OP_29(0x2D, 0x2, 0x1A)
    OP_29(0x2D, 0x2, 0x1B)
    OP_29(0x2D, 0x2, 0x1C)
    OP_29(0x2D, 0x2, 0x1D)
    OP_29(0x2D, 0x2, 0x1E)
    OP_29(0x2D, 0x2, 0x1F)

    label("loc_13A1E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13A32")
    OP_29(0x2D, 0x4, 0x2)

    label("loc_13A32")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13A47")
    OP_29(0x2D, 0x1, 0x0)

    label("loc_13A47")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13A5C")
    OP_29(0x2D, 0x1, 0x1)

    label("loc_13A5C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13A71")
    OP_29(0x2D, 0x1, 0x2)

    label("loc_13A71")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13A86")
    OP_29(0x2D, 0x1, 0x3)

    label("loc_13A86")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13A9B")
    OP_29(0x2D, 0x1, 0x4)

    label("loc_13A9B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13AB0")
    OP_29(0x2D, 0x1, 0x5)

    label("loc_13AB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13AC5")
    OP_29(0x2D, 0x1, 0x6)

    label("loc_13AC5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13ADA")
    OP_29(0x2D, 0x1, 0x7)

    label("loc_13ADA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13AEF")
    OP_29(0x2D, 0x1, 0x8)

    label("loc_13AEF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13B04")
    OP_29(0x2D, 0x1, 0x9)

    label("loc_13B04")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13B19")
    OP_29(0x2D, 0x1, 0xC)

    label("loc_13B19")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13B2E")
    OP_29(0x2D, 0x1, 0xD)

    label("loc_13B2E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13B43")
    OP_29(0x2D, 0x1, 0xE)

    label("loc_13B43")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13B58")
    OP_29(0x2D, 0x1, 0xF)

    label("loc_13B58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B7A")
    OP_29(0x2D, 0x3, 0x10)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Jump("loc_13BE5")

    label("loc_13B7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B9F")
    SetScenarioFlags(0x5C, 0)
    OP_29(0x2D, 0x3, 0x10)
    NewScene("r0040", 0, 0, 0)
    IdleLoop()
    Jump("loc_13BE5")

    label("loc_13B9F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x13), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13BC4")
    SetScenarioFlags(0x5C, 3)
    OP_29(0x2D, 0x3, 0x10)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()
    Jump("loc_13BE5")

    label("loc_13BC4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13BE5")
    SetScenarioFlags(0x5C, 3)
    OP_29(0x2D, 0x2, 0xE)
    NewScene("c0800", 0, 0, 0)
    IdleLoop()

    label("loc_13BE5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x15), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13BF9")
    OP_29(0x2D, 0x4, 0x10)

    label("loc_13BF9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13C0D")
    OP_29(0x2D, 0x4, 0x20)

    label("loc_13C0D")

    Jump("loc_14ACF")

    label("loc_13C12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13CFF")
    OP_29(0x2E, 0x3, 0x0)
    OP_29(0x2E, 0x3, 0x1)
    OP_29(0x2E, 0x3, 0x2)
    OP_29(0x2E, 0x3, 0x10)
    OP_29(0x2E, 0x3, 0x20)
    OP_29(0x2E, 0x3, 0x40)
    OP_29(0x2E, 0x2, 0x0)
    OP_29(0x2E, 0x2, 0x1)
    OP_29(0x2E, 0x2, 0x2)
    OP_29(0x2E, 0x2, 0x3)
    OP_29(0x2E, 0x2, 0x4)
    OP_29(0x2E, 0x2, 0x5)
    OP_29(0x2E, 0x2, 0x6)
    OP_29(0x2E, 0x2, 0x7)
    OP_29(0x2E, 0x2, 0x8)
    OP_29(0x2E, 0x2, 0x9)
    OP_29(0x2E, 0x2, 0xA)
    OP_29(0x2E, 0x2, 0xB)
    OP_29(0x2E, 0x2, 0xC)
    OP_29(0x2E, 0x2, 0xD)
    OP_29(0x2E, 0x2, 0xE)
    OP_29(0x2E, 0x2, 0xF)
    OP_29(0x2E, 0x2, 0x10)
    OP_29(0x2E, 0x2, 0x11)
    OP_29(0x2E, 0x2, 0x12)
    OP_29(0x2E, 0x2, 0x13)
    OP_29(0x2E, 0x2, 0x14)
    OP_29(0x2E, 0x2, 0x15)
    OP_29(0x2E, 0x2, 0x16)
    OP_29(0x2E, 0x2, 0x17)
    OP_29(0x2E, 0x2, 0x18)
    OP_29(0x2E, 0x2, 0x19)
    OP_29(0x2E, 0x2, 0x1A)
    OP_29(0x2E, 0x2, 0x1B)
    OP_29(0x2E, 0x2, 0x1C)
    OP_29(0x2E, 0x2, 0x1D)
    OP_29(0x2E, 0x2, 0x1E)
    OP_29(0x2E, 0x2, 0x1F)

    label("loc_13CFF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13D13")
    OP_29(0x2E, 0x4, 0x2)

    label("loc_13D13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13D28")
    OP_29(0x2E, 0x1, 0x0)

    label("loc_13D28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13D3D")
    OP_29(0x2E, 0x1, 0x1)

    label("loc_13D3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13D52")
    OP_29(0x2E, 0x1, 0x2)

    label("loc_13D52")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13D67")
    OP_29(0x2E, 0x1, 0x3)

    label("loc_13D67")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13D7C")
    OP_29(0x2E, 0x1, 0x4)

    label("loc_13D7C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13D91")
    OP_29(0x2E, 0x1, 0x5)

    label("loc_13D91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13DA6")
    OP_29(0x2E, 0x1, 0x6)

    label("loc_13DA6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13DBA")
    OP_29(0x2E, 0x4, 0x10)

    label("loc_13DBA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13DCE")
    OP_29(0x2E, 0x4, 0x20)

    label("loc_13DCE")

    Jump("loc_14ACF")

    label("loc_13DD3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13EC0")
    OP_29(0x2F, 0x3, 0x0)
    OP_29(0x2F, 0x3, 0x1)
    OP_29(0x2F, 0x3, 0x2)
    OP_29(0x2F, 0x3, 0x10)
    OP_29(0x2F, 0x3, 0x20)
    OP_29(0x2F, 0x3, 0x40)
    OP_29(0x2F, 0x2, 0x0)
    OP_29(0x2F, 0x2, 0x1)
    OP_29(0x2F, 0x2, 0x2)
    OP_29(0x2F, 0x2, 0x3)
    OP_29(0x2F, 0x2, 0x4)
    OP_29(0x2F, 0x2, 0x5)
    OP_29(0x2F, 0x2, 0x6)
    OP_29(0x2F, 0x2, 0x7)
    OP_29(0x2F, 0x2, 0x8)
    OP_29(0x2F, 0x2, 0x9)
    OP_29(0x2F, 0x2, 0xA)
    OP_29(0x2F, 0x2, 0xB)
    OP_29(0x2F, 0x2, 0xC)
    OP_29(0x2F, 0x2, 0xD)
    OP_29(0x2F, 0x2, 0xE)
    OP_29(0x2F, 0x2, 0xF)
    OP_29(0x2F, 0x2, 0x10)
    OP_29(0x2F, 0x2, 0x11)
    OP_29(0x2F, 0x2, 0x12)
    OP_29(0x2F, 0x2, 0x13)
    OP_29(0x2F, 0x2, 0x14)
    OP_29(0x2F, 0x2, 0x15)
    OP_29(0x2F, 0x2, 0x16)
    OP_29(0x2F, 0x2, 0x17)
    OP_29(0x2F, 0x2, 0x18)
    OP_29(0x2F, 0x2, 0x19)
    OP_29(0x2F, 0x2, 0x1A)
    OP_29(0x2F, 0x2, 0x1B)
    OP_29(0x2F, 0x2, 0x1C)
    OP_29(0x2F, 0x2, 0x1D)
    OP_29(0x2F, 0x2, 0x1E)
    OP_29(0x2F, 0x2, 0x1F)

    label("loc_13EC0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13ED4")
    OP_29(0x2F, 0x4, 0x2)

    label("loc_13ED4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13EE9")
    OP_29(0x2F, 0x1, 0x0)

    label("loc_13EE9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13EFE")
    OP_29(0x2F, 0x1, 0x1)

    label("loc_13EFE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13F13")
    OP_29(0x2F, 0x1, 0x2)

    label("loc_13F13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13F28")
    OP_29(0x2F, 0x1, 0x3)

    label("loc_13F28")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13F3D")
    OP_29(0x2F, 0x1, 0x4)

    label("loc_13F3D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13F52")
    OP_29(0x2F, 0x1, 0x5)

    label("loc_13F52")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13F67")
    OP_29(0x2F, 0x1, 0x6)

    label("loc_13F67")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13F7C")
    OP_29(0x2F, 0x1, 0x7)

    label("loc_13F7C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13F91")
    OP_29(0x2F, 0x1, 0x8)

    label("loc_13F91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13FA6")
    OP_29(0x2F, 0x1, 0x9)

    label("loc_13FA6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13FBB")
    OP_29(0x2F, 0x1, 0xA)

    label("loc_13FBB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13FD0")
    OP_29(0x2F, 0x1, 0xB)

    label("loc_13FD0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13FE4")
    OP_29(0x2F, 0x4, 0x10)

    label("loc_13FE4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_13FF8")
    OP_29(0x2F, 0x4, 0x20)

    label("loc_13FF8")

    Jump("loc_14ACF")

    label("loc_13FFD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_140EA")
    OP_29(0x30, 0x3, 0x0)
    OP_29(0x30, 0x3, 0x1)
    OP_29(0x30, 0x3, 0x2)
    OP_29(0x30, 0x3, 0x10)
    OP_29(0x30, 0x3, 0x20)
    OP_29(0x30, 0x3, 0x40)
    OP_29(0x30, 0x2, 0x0)
    OP_29(0x30, 0x2, 0x1)
    OP_29(0x30, 0x2, 0x2)
    OP_29(0x30, 0x2, 0x3)
    OP_29(0x30, 0x2, 0x4)
    OP_29(0x30, 0x2, 0x5)
    OP_29(0x30, 0x2, 0x6)
    OP_29(0x30, 0x2, 0x7)
    OP_29(0x30, 0x2, 0x8)
    OP_29(0x30, 0x2, 0x9)
    OP_29(0x30, 0x2, 0xA)
    OP_29(0x30, 0x2, 0xB)
    OP_29(0x30, 0x2, 0xC)
    OP_29(0x30, 0x2, 0xD)
    OP_29(0x30, 0x2, 0xE)
    OP_29(0x30, 0x2, 0xF)
    OP_29(0x30, 0x2, 0x10)
    OP_29(0x30, 0x2, 0x11)
    OP_29(0x30, 0x2, 0x12)
    OP_29(0x30, 0x2, 0x13)
    OP_29(0x30, 0x2, 0x14)
    OP_29(0x30, 0x2, 0x15)
    OP_29(0x30, 0x2, 0x16)
    OP_29(0x30, 0x2, 0x17)
    OP_29(0x30, 0x2, 0x18)
    OP_29(0x30, 0x2, 0x19)
    OP_29(0x30, 0x2, 0x1A)
    OP_29(0x30, 0x2, 0x1B)
    OP_29(0x30, 0x2, 0x1C)
    OP_29(0x30, 0x2, 0x1D)
    OP_29(0x30, 0x2, 0x1E)
    OP_29(0x30, 0x2, 0x1F)

    label("loc_140EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_140FE")
    OP_29(0x30, 0x4, 0x2)

    label("loc_140FE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14113")
    OP_29(0x30, 0x1, 0x0)

    label("loc_14113")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14128")
    OP_29(0x30, 0x1, 0x1)

    label("loc_14128")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1413D")
    OP_29(0x30, 0x1, 0x2)

    label("loc_1413D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14152")
    OP_29(0x30, 0x1, 0x3)

    label("loc_14152")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14167")
    OP_29(0x30, 0x1, 0x4)

    label("loc_14167")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1417C")
    OP_29(0x30, 0x1, 0x5)

    label("loc_1417C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14191")
    OP_29(0x30, 0x1, 0x6)

    label("loc_14191")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_141A6")
    OP_29(0x30, 0x1, 0x7)

    label("loc_141A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_141BB")
    OP_29(0x30, 0x1, 0x8)

    label("loc_141BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_141D0")
    OP_29(0x30, 0x1, 0x9)

    label("loc_141D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_141E5")
    OP_29(0x30, 0x1, 0xA)

    label("loc_141E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_141FA")
    OP_29(0x30, 0x1, 0xB)

    label("loc_141FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1420E")
    OP_29(0x30, 0x4, 0x10)

    label("loc_1420E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14222")
    OP_29(0x30, 0x4, 0x20)

    label("loc_14222")

    Jump("loc_14ACF")

    label("loc_14227")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14314")
    OP_29(0x31, 0x3, 0x0)
    OP_29(0x31, 0x3, 0x1)
    OP_29(0x31, 0x3, 0x2)
    OP_29(0x31, 0x3, 0x10)
    OP_29(0x31, 0x3, 0x20)
    OP_29(0x31, 0x3, 0x40)
    OP_29(0x31, 0x2, 0x0)
    OP_29(0x31, 0x2, 0x1)
    OP_29(0x31, 0x2, 0x2)
    OP_29(0x31, 0x2, 0x3)
    OP_29(0x31, 0x2, 0x4)
    OP_29(0x31, 0x2, 0x5)
    OP_29(0x31, 0x2, 0x6)
    OP_29(0x31, 0x2, 0x7)
    OP_29(0x31, 0x2, 0x8)
    OP_29(0x31, 0x2, 0x9)
    OP_29(0x31, 0x2, 0xA)
    OP_29(0x31, 0x2, 0xB)
    OP_29(0x31, 0x2, 0xC)
    OP_29(0x31, 0x2, 0xD)
    OP_29(0x31, 0x2, 0xE)
    OP_29(0x31, 0x2, 0xF)
    OP_29(0x31, 0x2, 0x10)
    OP_29(0x31, 0x2, 0x11)
    OP_29(0x31, 0x2, 0x12)
    OP_29(0x31, 0x2, 0x13)
    OP_29(0x31, 0x2, 0x14)
    OP_29(0x31, 0x2, 0x15)
    OP_29(0x31, 0x2, 0x16)
    OP_29(0x31, 0x2, 0x17)
    OP_29(0x31, 0x2, 0x18)
    OP_29(0x31, 0x2, 0x19)
    OP_29(0x31, 0x2, 0x1A)
    OP_29(0x31, 0x2, 0x1B)
    OP_29(0x31, 0x2, 0x1C)
    OP_29(0x31, 0x2, 0x1D)
    OP_29(0x31, 0x2, 0x1E)
    OP_29(0x31, 0x2, 0x1F)

    label("loc_14314")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14328")
    OP_29(0x31, 0x4, 0x2)

    label("loc_14328")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1433D")
    OP_29(0x31, 0x1, 0x0)

    label("loc_1433D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14352")
    OP_29(0x31, 0x1, 0x1)

    label("loc_14352")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14367")
    OP_29(0x31, 0x1, 0x2)

    label("loc_14367")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1437C")
    OP_29(0x31, 0x1, 0x3)

    label("loc_1437C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14391")
    OP_29(0x31, 0x1, 0x4)

    label("loc_14391")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_143A6")
    OP_29(0x31, 0x1, 0x5)

    label("loc_143A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_143BB")
    OP_29(0x31, 0x1, 0x6)

    label("loc_143BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_143D0")
    OP_29(0x31, 0x1, 0x7)

    label("loc_143D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_143E5")
    OP_29(0x31, 0x1, 0x8)

    label("loc_143E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_143FA")
    OP_29(0x31, 0x1, 0x9)

    label("loc_143FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1440F")
    OP_29(0x31, 0x1, 0xA)

    label("loc_1440F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14424")
    OP_29(0x31, 0x1, 0xB)

    label("loc_14424")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14438")
    OP_29(0x31, 0x4, 0x10)

    label("loc_14438")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1444C")
    OP_29(0x31, 0x4, 0x20)

    label("loc_1444C")

    Jump("loc_14ACF")

    label("loc_14451")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1453E")
    OP_29(0x32, 0x3, 0x0)
    OP_29(0x32, 0x3, 0x1)
    OP_29(0x32, 0x3, 0x2)
    OP_29(0x32, 0x3, 0x10)
    OP_29(0x32, 0x3, 0x20)
    OP_29(0x32, 0x3, 0x40)
    OP_29(0x32, 0x2, 0x0)
    OP_29(0x32, 0x2, 0x1)
    OP_29(0x32, 0x2, 0x2)
    OP_29(0x32, 0x2, 0x3)
    OP_29(0x32, 0x2, 0x4)
    OP_29(0x32, 0x2, 0x5)
    OP_29(0x32, 0x2, 0x6)
    OP_29(0x32, 0x2, 0x7)
    OP_29(0x32, 0x2, 0x8)
    OP_29(0x32, 0x2, 0x9)
    OP_29(0x32, 0x2, 0xA)
    OP_29(0x32, 0x2, 0xB)
    OP_29(0x32, 0x2, 0xC)
    OP_29(0x32, 0x2, 0xD)
    OP_29(0x32, 0x2, 0xE)
    OP_29(0x32, 0x2, 0xF)
    OP_29(0x32, 0x2, 0x10)
    OP_29(0x32, 0x2, 0x11)
    OP_29(0x32, 0x2, 0x12)
    OP_29(0x32, 0x2, 0x13)
    OP_29(0x32, 0x2, 0x14)
    OP_29(0x32, 0x2, 0x15)
    OP_29(0x32, 0x2, 0x16)
    OP_29(0x32, 0x2, 0x17)
    OP_29(0x32, 0x2, 0x18)
    OP_29(0x32, 0x2, 0x19)
    OP_29(0x32, 0x2, 0x1A)
    OP_29(0x32, 0x2, 0x1B)
    OP_29(0x32, 0x2, 0x1C)
    OP_29(0x32, 0x2, 0x1D)
    OP_29(0x32, 0x2, 0x1E)
    OP_29(0x32, 0x2, 0x1F)

    label("loc_1453E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14552")
    OP_29(0x32, 0x4, 0x2)

    label("loc_14552")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14567")
    OP_29(0x32, 0x1, 0x0)

    label("loc_14567")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1457C")
    OP_29(0x32, 0x1, 0x1)

    label("loc_1457C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14591")
    OP_29(0x32, 0x1, 0x2)

    label("loc_14591")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_145A6")
    OP_29(0x32, 0x1, 0x3)

    label("loc_145A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_145BB")
    OP_29(0x32, 0x1, 0x4)

    label("loc_145BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_145D0")
    OP_29(0x32, 0x1, 0x5)

    label("loc_145D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_145E5")
    OP_29(0x32, 0x1, 0x6)

    label("loc_145E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_145FA")
    OP_29(0x32, 0x1, 0x7)

    label("loc_145FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1460F")
    OP_29(0x32, 0x1, 0x8)

    label("loc_1460F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14624")
    OP_29(0x32, 0x1, 0x9)

    label("loc_14624")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14639")
    OP_29(0x32, 0x1, 0xA)

    label("loc_14639")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1464E")
    OP_29(0x32, 0x1, 0xB)

    label("loc_1464E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14662")
    OP_29(0x32, 0x4, 0x10)

    label("loc_14662")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14676")
    OP_29(0x32, 0x4, 0x20)

    label("loc_14676")

    Jump("loc_14ACF")

    label("loc_1467B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14768")
    OP_29(0x33, 0x3, 0x0)
    OP_29(0x33, 0x3, 0x1)
    OP_29(0x33, 0x3, 0x2)
    OP_29(0x33, 0x3, 0x10)
    OP_29(0x33, 0x3, 0x20)
    OP_29(0x33, 0x3, 0x40)
    OP_29(0x33, 0x2, 0x0)
    OP_29(0x33, 0x2, 0x1)
    OP_29(0x33, 0x2, 0x2)
    OP_29(0x33, 0x2, 0x3)
    OP_29(0x33, 0x2, 0x4)
    OP_29(0x33, 0x2, 0x5)
    OP_29(0x33, 0x2, 0x6)
    OP_29(0x33, 0x2, 0x7)
    OP_29(0x33, 0x2, 0x8)
    OP_29(0x33, 0x2, 0x9)
    OP_29(0x33, 0x2, 0xA)
    OP_29(0x33, 0x2, 0xB)
    OP_29(0x33, 0x2, 0xC)
    OP_29(0x33, 0x2, 0xD)
    OP_29(0x33, 0x2, 0xE)
    OP_29(0x33, 0x2, 0xF)
    OP_29(0x33, 0x2, 0x10)
    OP_29(0x33, 0x2, 0x11)
    OP_29(0x33, 0x2, 0x12)
    OP_29(0x33, 0x2, 0x13)
    OP_29(0x33, 0x2, 0x14)
    OP_29(0x33, 0x2, 0x15)
    OP_29(0x33, 0x2, 0x16)
    OP_29(0x33, 0x2, 0x17)
    OP_29(0x33, 0x2, 0x18)
    OP_29(0x33, 0x2, 0x19)
    OP_29(0x33, 0x2, 0x1A)
    OP_29(0x33, 0x2, 0x1B)
    OP_29(0x33, 0x2, 0x1C)
    OP_29(0x33, 0x2, 0x1D)
    OP_29(0x33, 0x2, 0x1E)
    OP_29(0x33, 0x2, 0x1F)

    label("loc_14768")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1477C")
    OP_29(0x33, 0x4, 0x2)

    label("loc_1477C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14791")
    OP_29(0x33, 0x1, 0x0)

    label("loc_14791")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_147A6")
    OP_29(0x33, 0x1, 0x1)

    label("loc_147A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_147BB")
    OP_29(0x33, 0x1, 0x2)

    label("loc_147BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_147D0")
    OP_29(0x33, 0x1, 0x3)

    label("loc_147D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_147E5")
    OP_29(0x33, 0x1, 0x4)

    label("loc_147E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_147FA")
    OP_29(0x33, 0x1, 0x5)

    label("loc_147FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1480F")
    OP_29(0x33, 0x1, 0x6)

    label("loc_1480F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14824")
    OP_29(0x33, 0x1, 0x7)

    label("loc_14824")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14839")
    OP_29(0x33, 0x1, 0x8)

    label("loc_14839")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1484E")
    OP_29(0x33, 0x1, 0x9)

    label("loc_1484E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14863")
    OP_29(0x33, 0x1, 0xA)

    label("loc_14863")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14878")
    OP_29(0x33, 0x1, 0xB)

    label("loc_14878")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1488C")
    OP_29(0x33, 0x4, 0x10)

    label("loc_1488C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_148A0")
    OP_29(0x33, 0x4, 0x20)

    label("loc_148A0")

    Jump("loc_14ACF")

    label("loc_148A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14992")
    OP_29(0x34, 0x3, 0x0)
    OP_29(0x34, 0x3, 0x1)
    OP_29(0x34, 0x3, 0x2)
    OP_29(0x34, 0x3, 0x10)
    OP_29(0x34, 0x3, 0x20)
    OP_29(0x34, 0x3, 0x40)
    OP_29(0x34, 0x2, 0x0)
    OP_29(0x34, 0x2, 0x1)
    OP_29(0x34, 0x2, 0x2)
    OP_29(0x34, 0x2, 0x3)
    OP_29(0x34, 0x2, 0x4)
    OP_29(0x34, 0x2, 0x5)
    OP_29(0x34, 0x2, 0x6)
    OP_29(0x34, 0x2, 0x7)
    OP_29(0x34, 0x2, 0x8)
    OP_29(0x34, 0x2, 0x9)
    OP_29(0x34, 0x2, 0xA)
    OP_29(0x34, 0x2, 0xB)
    OP_29(0x34, 0x2, 0xC)
    OP_29(0x34, 0x2, 0xD)
    OP_29(0x34, 0x2, 0xE)
    OP_29(0x34, 0x2, 0xF)
    OP_29(0x34, 0x2, 0x10)
    OP_29(0x34, 0x2, 0x11)
    OP_29(0x34, 0x2, 0x12)
    OP_29(0x34, 0x2, 0x13)
    OP_29(0x34, 0x2, 0x14)
    OP_29(0x34, 0x2, 0x15)
    OP_29(0x34, 0x2, 0x16)
    OP_29(0x34, 0x2, 0x17)
    OP_29(0x34, 0x2, 0x18)
    OP_29(0x34, 0x2, 0x19)
    OP_29(0x34, 0x2, 0x1A)
    OP_29(0x34, 0x2, 0x1B)
    OP_29(0x34, 0x2, 0x1C)
    OP_29(0x34, 0x2, 0x1D)
    OP_29(0x34, 0x2, 0x1E)
    OP_29(0x34, 0x2, 0x1F)

    label("loc_14992")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_149A6")
    OP_29(0x34, 0x4, 0x2)

    label("loc_149A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_149BB")
    OP_29(0x34, 0x1, 0x0)

    label("loc_149BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_149D0")
    OP_29(0x34, 0x1, 0x1)

    label("loc_149D0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_149E5")
    OP_29(0x34, 0x1, 0x2)

    label("loc_149E5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_149FA")
    OP_29(0x34, 0x1, 0x3)

    label("loc_149FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14A0F")
    OP_29(0x34, 0x1, 0x4)

    label("loc_14A0F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14A24")
    OP_29(0x34, 0x1, 0x5)

    label("loc_14A24")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14A39")
    OP_29(0x34, 0x1, 0x6)

    label("loc_14A39")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14A4E")
    OP_29(0x34, 0x1, 0x7)

    label("loc_14A4E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14A63")
    OP_29(0x34, 0x1, 0x8)

    label("loc_14A63")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14A78")
    OP_29(0x34, 0x1, 0x9)

    label("loc_14A78")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14A8D")
    OP_29(0x34, 0x1, 0xA)

    label("loc_14A8D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14AA2")
    OP_29(0x34, 0x1, 0xB)

    label("loc_14AA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14AB6")
    OP_29(0x34, 0x4, 0x10)

    label("loc_14AB6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_14ACA")
    OP_29(0x34, 0x4, 0x20)

    label("loc_14ACA")

    Jump("loc_14ACF")

    label("loc_14ACF")

    Jump("loc_125C2")

    label("loc_14AD4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_59_125B8 end

    SaveToFile()

Try(main)
