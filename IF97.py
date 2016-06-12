
N = [0.14632971213167, -0.84548187169114, -3.7563603672040, 3.3855169168385, -0.95791963387872, 0.15772038513228, -0.016616417199501, 0.00081214629983568, 0.00028319080123804, -0.00060706301565874, -0.018990068218419, -0.032529748770505, -0.021841717175414, -0.000052838357969930, -0.00047184321073267, -0.00030001780793026, 0.000047661393906987, -0.0000044141845330846, -0.00000000000000072694996297594, -0.000031679644845054, -
     0.0000028270797985312, -0.00000000085205128120103, -0.0000022425281908000, -0.00000065171222895601, -0.00000000000014341729937924, -0.00000040516996860117, -0.0000000012734301741641, -0.00000000017424871230634, -0.00000000000000000068762131295531, 0.000000000000000000014478307828521, 0.000000000000000000000026335781662795, -0.000000000000000000000011947622640071, 0.0000000000000000000000018228094581404, -0.000000000000000000000000093537087292458]
I = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2,
     2, 3, 3, 3, 4, 4, 4, 5, 8, 8, 21, 23, 29, 30, 31, 32]
J = [-2, -1, 0, 1, 2, 3, 4, 5, -9, -7, -1, 0, 1, 3, -3, 0, 1, 3, 17, -
     4, 0, 6, -5, -2, 10, -8, -11, -6, -29, -31, -38, -39, -40, -41]
Na = [-0.000000133645667811215, 0.00000455912656802978, -0.0000146294640700979, 0.00639341312970080, 372.783927268847, -7186.54377460447, 573494.752103400, -2675693.29111439, -0.0000334066283302614, -0.245479214069597e-1, 0.478087847764996e2, 0.764664131818904e-5, 0.128350627676972e-2, 0.171219081377331e-1, -0.851007304583213e1, -
      0.136513461629781e-1, -0.384460997596657e-5, 0.337423807911655e-2, -0.551624873066791, 0.729202277107470, -0.992522757376041e-2, -0.119308831407288, 0.793929190615421, 0.454270731799386, 0.209998591259910, -0.00642109823904738, -0.0235155868604540, 0.00252233108341612, -0.00764885133368119, 0.0136176427574291, -0.0133027883575669]
Ia = [-12, -12, -12, -12, -12, -12, -12, -12, -10, -10, -10, -8, -
      8, -8, -8, -5, -3, -2, -2, -2, -1, -1, 0, 0, 1, 3, 3, 4, 4, 10, 12]
Ja = [0, 1, 2, 6, 14, 16, 20, 22, 1, 5, 12, 0, 2, 4,
      10, 2, 0, 1, 3, 4, 0, 2, 0, 1, 1, 0, 1, 0, 3, 4, 5]
NB = [0.0000323254573644920, -0.000127575556587181, -0.000475851877356068, 0.00156183014181602, 0.105724860113781, -85.8514221132534, 724.140095480911, 0.00296475810273257, -0.00592721983365988, -0.0126305422818666, -0.115716196364853, 84.9000969739595, -0.0108602260086615, 0.0154304475328851, 0.0750455441524466, 0.0252520973612982, -
      0.0602507901232996, -3.07622221350501, -0.0574011959864879, 5.03471360939849, -0.925081888584834, 3.91733882917546, -77.3146007130190, 9493.08762098587, -1410437.19679409, 8491662.30819026, 0.861095729446704, 0.323346442811720, 0.873281936020439, -0.436653048526683, 0.286596714529479, -0.131778331276228, 0.00676682064330275]
IB = [-12, -12, -10, -10, -10, -10, -10, -8, -8, -8, -8, -8, -6, -6, -
      6, -4, -4, -3, -2, -2, -1, -1, -1, -1, -1, -1, 0, 0, 1, 3, 5, 6, 8]
JB = [0, 1, 0, 1, 5, 10, 12, 0, 1, 2, 4, 10, 0, 1, 2, 0,
      1, 5, 0, 4, 2, 4, 6, 10, 14, 16, 0, 2, 1, 1, 1, 1, 1]

PP = 16.53
TT = 1386
RR = 0.461526


def gama(p, t):
    pi = p / PP
    tao = TT / t
    gm = 0
    for i in range(1, 35):
        gm += N[i - 1] * (7.1 - pi)**I[i - 1] * (tao - 1.222)**J[i - 1]
    return gm


def gamapai(p, t):
    pi = p / PP
    tao = TT / t
    gmp = 0
    for i in range(1, 35):
        gmp -= N[i - 1] * I[i - 1] * (7.1 - pi)**(I[i - 1] - 1) * (tao - 1.222)**J[i - 1]
    return gmp


def gamapaipai(p, t):
    pi = p / PP
    tao = TT / t
    gmpp = 0
    for i in range(1, 35):
        gmpp += N[i - 1] * I[i - 1] * (I[i - 1] - 1) * \
            (7.1 - pi)**(I[i - 1] - 2) * (tao - 1.222)**J[i - 1]
    return gmpp


def gamatao(p, t):
    pi = p / PP
    tao = TT / t
    gmt = 0
    for i in range(1, 35):
        gmt += N[i - 1] * (7.1 - pi)**I[i - 1] * J[i - 1] * (tao - 1.222)**(J[i - 1] - 1)
    return gmt


def gamataotao(p, t):
    pi = p / PP
    tao = TT / t
    gmtt = 0
    for i in range(1, 35):
        gmtt += N[i - 1] * (7.1 - pi)**I[i - 1] * J[i - 1] * \
            (J[i - 1] - 1) * (tao - 1.222)**(J[i - 1] - 2)
    return gmtt


def gamapaitao(p, t):
    pi = p / PP
    tao = TT / t
    gmpt = 0
    for i in range(1, 35):
        gmpt -= N[i - 1] * I[i - 1] * (7.1 - pi)**(I[i - 1] - 1) * \
            J[i - 1] * (tao - 1.222)**(J[i - 1] - 1)
    return gmpt


def Volume(p, t):
    pi = p / PP
    vol = pi * gamapai(p, t) * RR * t / (p * 1000)
    return vol


def InternalEnergy(p, t):
    pi = p / PP
    tao = TT / t
    eng = (tao * gamatao(p, t) - pi * gamapai(p, t)) * RR * t
    return eng


def Entropy(p, t):
    tao = TT / t
    ent = (tao * gamatao(p, t) - gama(p, t)) * RR
    return ent


def Enthalpy(p, t):
    tao = TT / t
    ent = tao * gamatao(p, t) * RR * t
    return ent


def IHCapacity(p, t):
    tao = TT / t
    cap = 0 - tao**2 * gamataotao(p, t) * RR
    return cap


def Sound(p, t):
    tao = TT / t
    s1 = gamapai(p, t)**2
    s2 = gamapai(p, t) - tao * gamapaitao(p, t)
    s3 = s2**2
    s4 = tao**2 * gamataotao(p, t)
    s5 = s3 / s4
    sou = (s1 * RR * t * 1000 / (s5 - gamapaipai(p, t)))**0.5
    return sou


def Buchong_BE3a(p, h):
    jieguo = 0
    TX = 760
    H = h / 2300
    pi = p / 100
    for i in range(1, 31):
        jieguo += Na[i - 1] * (pi + 0.240)**Ia[i - 1] * (H - 0.615)**Ja[i - 1]
    return jieguo * TX


def buchong_BE3b(p, h):
    jieguo = 0
    Tc = 860
    pc = 100
    pi = p / pc
    eta = h / 2800
    for i in range(0, 33):
        jieguo += NB[i] * (pi + 0.298)**IB[i] * (eta - 0.720)**JB[i]
    zzjieguo = Tc * jieguo
    return zzjieguo
