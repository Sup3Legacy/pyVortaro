


tokens = ("EK", "FOR", "DIS", "MAL", "NE", "MEZ", "EKSTER", "GE", "INTER", "LE",
          "ON", "OP", "OBL", "UL", "EM", "EJ", "EG", "ET", "IN", "ID", "AR",
          "ER", "IL", "AJX", "IG", "IGX", "IND", "AD", "IST", "AN", "EC", "EBL",
          "UJ", "ING",
          "O", "I", "AS", "IS", "OS", "A", "E", "U", "US", "N", "J",
          "PRED", "RAD"
          )

t_EK = r'ek'
t_FOR = r'for'
t_DIS = r'dis'
t_MAL = r'mal'
t_NE = r'ne'
t_MEZ = r'mez'
t_EKSTER = r'ekster'
t_GE = r'ge'
t_INTER = r'inter'
t_LE = r'le'
t_ON = r'on'
t_OP = r'op'
t_OBL = r'obl'
t_UL = r'ul'
t_EM = r'em'
t_EJ = r'ej'
t_EG = r'eg'
t_ET = r'et'
t_IN = r'in'
t_ID = r'id'
t_AR = r'ar'
t_ER = r'er'
t_IL = r'il'
t_AJX = r'aĵ'
t_IG = r'ig'
t_IGX = r'iĝ'
t_IND = r'ind'
t_AD = r'ad'
t_IST = r'ist'
t_AN = r'an'
t_EC = r'ec'
t_EBL = r'ebl'
t_UJ = r'uj'
t_ING = r'ing'
t_O = r'o'
t_A = r'a'
t_E = r'e'
t_I = r'i'
t_IS = r'is'
t_OS = r'os'
t_AS = r'as'
t_U = r'u'
t_US = r'us'
t_J = r'j'
t_N = r'n'
t_PRED = r'\'[0-9]+'
t_RAD = r'\_'

def t_error(t):
    print(f"Illegal character {t.value[0]!r}")
    t.lexer.skip(1)

import ply.lex as lex
lex.lex()
