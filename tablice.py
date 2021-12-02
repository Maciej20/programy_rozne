#Program, który sprawdza, czy tablica rejestracyjna jest prawidłowa


LETTERS = list("ABCDEFGHIJKLMNOPRSTUVWXYZ")
FORBIDDEN_LETTERS = list("BDIOZ")
DIGITS = [str(x) for x in range(10)]
WYR_1 = ["B", "C", "D", "E", "F", "G", "K", "L", "N", "O", "P", "R", "S", "T", "W", "Z"]
IND = [str(letter + digit) for letter in WYR_1 for digit in DIGITS]
WYR_2 = ['DJ', 'DL', 'DB', 'DW', 'CB', 'CG', 'CT', 'CW', 'LB', 'LC', 'LU', 'LZ', 'FG', 'FZ', 
'EL', 'EP', 'ES', 'KR', 'KN', 'KT', 'WO', 'WP', 'WR', 'WS', 'WG', 'WL', 'WM', 'WA', 'WB', 'WD', 'WE', 'WF', 
'WH', 'WI', 'WJ', 'WK', 'WN', 'WT', 'WU', 'WW', 'WX', 'WY', 'WZ', 'OP', 'OB', 'OK', 'RK', 'RP', 'RZ', 'RT', 
'BI', 'BL', 'BS', 'GD', 'GA', 'GS', 'SB', 'SY', 'SH', 'SC', 'SD', 'SG', 'SJ', 'SK', 'SM', 'SL', 'SR', 'SI', 
'SO', 'SW', 'ST', 'SZ', 'TK', 'NE', 'NO', 'PK', 'PN', 'PL', 'PO', 'PP', 'PZ', 'ZK', 'ZS'] 
WYR_3 = ['DBL', 'DDZ', 'DGL', 'DGR', 'DJA', 'DJE', 'DKA', 'DKL', 'DLE', 'DLB', 'DLU', 'DLW', 'DMI', 
'DOL', 'DOA', 'DPL', 'DST', 'DSR', 'DSW', 'DTR', 'DBA', 'DWL', 'DWR', 'DZA', 'DZG', 'DZL', 'CAL', 'CBR', 
'CBY', 'CCH', 'CGD', 'CGR', 'CIN', 'CLI', 'CMG', 'CNA', 'CRA', 'CRY', 'CSE', 'CSW', 'CTR', 'CTU', 'CWA', 
'CWL', 'CZN', 'LBI', 'LBL', 'LCH', 'LHR', 'LJA', 'LKS', 'LKR', 'LLB', 'LUB', 'LLE', 'LLU', 'LOP', 'LPA', 
'LPU', 'LRA', 'LRY', 'LSW', 'LTM', 'LWL', 'LZA', 'FGW', 'FKR', 'FMI', 'FNW', 'FSL', 'FSD', 'FSU', 'FSW', 
'FWS', 'FZI', 'FZG', 'FZA', 'EBR', 'EBE', 'EKU', 'ELA', 'ELE', 'ELC', 'ELW', 'EOP', 'EPA', 'EPJ', 'EPI', 
'EPD', 'ERA', 'ERW', 'ESI', 'ESK', 'ETM', 'EWI', 'EWE', 'EZD', 'EZG', 'KBC', 'KBR', 'KCH', 'KDA', 'KGR', 
'KRA', 'KLI', 'KMI', 'KMY', 'KNS', 'KNT', 'KOL', 'KOS', 'KPR', 'KSU', 'KTA', 'KTT', 'KWA', 'KWI', 'WBR', 
'WCI', 'WGS', 'WGM', 'WGR', 'WKZ', 'WLI', 'WLS', 'WMA', 'WML', 'WND', 'WOS', 'WOR', 'WOT', 'WPI', 'WPL', 
'WPN', 'WPR', 'WPZ', 'WPY', 'WPU', 'WRA', 'WSI', 'WSE', 'WSC', 'WSK', 'WSZ', 'WWE', 'WWL', 'WWY', 'WZW', 
'WZU', 'WZY', 'OGL', 'OKL', 'OKR', 'ONA', 'ONY', 'OOL', 'OPO', 'OPR', 'OST', 'RBI', 'RBR', 'RDE', 'RJA', 
'RJS', 'RKL', 'RKR', 'RLS', 'RLE', 'RLU', 'RLA', 'RMI', 'RNI', 'RPR', 'RPZ', 'RRS', 'RZE', 'RSA', 'RST', 
'RSR', 'RTA', 'BAU', 'BIA', 'BBI', 'BGR', 'BHA', 'BKL', 'BLM', 'BMN', 'BSE', 'BSI', 'BSK', 'BSU', 'BWM', 
'BZA', 'GSP', 'GBY', 'GCH', 'GCZ', 'GDA', 'GKA', 'GKS', 'GKW', 'GLE', 'GMB', 'GND', 'GPU', 'GSL', 'GST',
'GSZ', 'GTC', 'GWE', 'SJZ', 'SPI', 'SRS', 'SZO', 'SBE', 'SBI', 'SCI', 'SCZ', 'SGL', 'SKL', 'SLU', 'SMI',
'SMY', 'SPS', 'SRC', 'SRB', 'STA', 'SBL', 'SWD', 'SZA', 'SZY', 'TBU', 'TJE', 'TKA', 'TKI', 'TKN', 'TOP',
'TOS', 'TPI', 'TSA', 'TSK', 'TST', 'TSZ', 'TLW', 'NBA', 'NBR', 'NDZ', 'NEB', 'NEL', 'NGI', 'NIL', 'NKE',
'NLI', 'NMR', 'NNI', 'NNM', 'NOE', 'NGO', 'NOL', 'NOS', 'NPI', 'NSZ', 'NWE', 'PKO', 'PCH', 'PCT', 'PGN',
'PGS', 'PGO', 'PJA', 'PKA', 'PKE', 'PKL', 'PKN', 'PKS', 'PKR', 'PLE', 'PMI', 'PNT', 'POB', 'POS', 'POT',
'PPL', 'POZ', 'PRA', 'PSL', 'PSZ', 'PSR', 'PSE', 'PTU', 'PWA', 'PWL', 'PWR', 'PZL', 'ZSW', 'ZBI', 'ZCH',
'ZDR', 'ZGL', 'ZGY', 'ZGR', 'ZKA', 'ZKL', 'ZKO', 'ZLO', 'ZMY', 'ZPL', 'ZPY', 'ZSL', 'ZST', 'ZSZ', 'ZSD',
'ZWA']

LEN_4 = {"ddd": ["000"], "ddl": ["00"], "dld": ["00", "10", "20", "30", "40", "50", "60", "70", "80", "90",
"01", "02", '03', '04', '05', '06', '07', '08', '09'], "ldd": ["00"], "dll": ["0"], "lld": ["0"], "ldl": ["0"]}
LEN_5_6_IND = ["lll", "lld", "ldl", "ldd", "llll", "llld", "lldl", "lldd"]
LEN_7_IND = ["lllll", "lllld", "llldl", "llldd"]
LEN_7_WYR_2 = {"ddddd": ["00000"], "ddddl": ["0000"], "dddll": ["000"], "dlddd": [f"{a}{b}{c}{d}" for a in range(10) for b in range(10) for c in range(10) for d in range(10) if int(f"{b}{c}{d}") == 0 or a == 0],
"dlldd": [f"{a}{b}{c}" for a in range(10) for b in range(10) for c in range(10) if int(f"{b}{c}") == 0 or a == 0]}
LEN_7_WYR_3 = {"lddd": ["000"], "ddll": ["00"], "dldd": [f"{a}{b}{c}" for a in range(10) for b in range(10) for c in range(10) if int(f"{b}{c}") == 0 or a == 0],
"ddld": [f"{a}{b}{c}" for a in range(10) for b in range(10) for c in range(10) if int(f"{a}{b}") == 0 or c == 0], "dlld": ["00", "10", "20", "30", "40", "50", "60", "70", "80", "90",
"01", "02", '03', '04', '05', '06', '07', '08', '09'], "lldd": ["00"]}
LEN_8 = {"ddddd": ["00000"], "ddddl": ["0000"], "dddll": ["000"]}


def plate_validation(plate):
    if type(plate) != str:
        return False
    length = len(plate)
    if length == 4:
        if plate[0] not in WYR_1:
            return False
        else:
            car = plate[1:]
        for char in car:
            if char in FORBIDDEN_LETTERS:
                return False
        if classify_str(car) in LEN_4.keys() and dropletters(car) not in LEN_4[classify_str(car)]:
            return True
        else:
            return False

    elif length == 5 or length == 6:
        if plate[0:2] not in IND:
            return False
        else:
            car = plate[2:]
        if classify_str(car) in LEN_5_6_IND:
            return True
        else:
            return False

    elif length == 7:
        if plate [0:2] in IND:
            car = plate[2:]
            if classify_str(car) in LEN_7_IND:
                return True
            else:
                return False
        elif plate[0:3] in WYR_3: ## ważne aby najpierw sprawdzić wyróżniki 3-literowe, dopiero potem te 2-literowe
            car = plate[3:]
            for char in car:
                if char in FORBIDDEN_LETTERS:
                    return False
            if classify_str(car) in LEN_7_WYR_3.keys() and dropletters(car) not in LEN_7_WYR_3[classify_str(car)]:
                return True
            else:
                return False

        elif plate [0:2] in WYR_2:
            car = plate [2:]
            for char in car:
                if char in FORBIDDEN_LETTERS:
                    return False
            if classify_str(car) in LEN_7_WYR_2.keys() and dropletters(car) not in LEN_7_WYR_2[classify_str(car)]:
                return True
            else:
                return False
        else:
            return False
    
    elif length == 8:
        if plate[0:3] in WYR_3:
            car = plate[3:]
            for char in car:
                if char in FORBIDDEN_LETTERS:
                    return False
            if classify_str(car) in LEN_8.keys() and dropletters(car) not in LEN_8[classify_str(car)]:
                return True
            else:
                return False
            
        else:
            return False
    else:
        return False
              
def classify_str(str):
    '''Funkcja iteruje przez napis i jeśli znak jest cyfrą, to odpowiadającemu indeksowi w napisie x przyporządkowuje 'd',
    a jeśli znak jest wielką literą, to 'l', a następnie zwraca x
    Jeśli którykolwiek znak nie jest dużą literą lub cyfrą, to funkcja zwraca fałsz'''
    x = ""
    for char in str:
        if char in DIGITS:
            x += "d"
        elif char in LETTERS:
            x += "l"
        else: 
            return False
    return x

def dropletters(str):
    '''Funkcja tworzy nowy napis x, w taki sposób, że dodaje do niego tylko znaki będące cyframi'''
    x = ""
    for char in str:
        if char in DIGITS:
            x += char
    return x

def show_c(data):
    plates = data["plate"].unique()
    c = {plate: plate_validation(plate) for plate in plates}
    print("Tablica | Czy poprawna?")
    for k, v in c.items():
        print(k, v)
        