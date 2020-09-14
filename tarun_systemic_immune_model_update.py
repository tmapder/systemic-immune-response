
# coding: utf-8

# In[17]:


import tellurium as te

model_string = '''
/////////////////////// Reactions //////////////////////////////

//Tissue infection

J1: D -> E; dE*E0; // E0 => initial number of E-cells
J2: E -> D; dE*E;
J3: E -> Ev; bE*V*E;
J4: Ev -> E; aE*Ev;
J5: Ev -> D; dEv*Ev;
J6: Ev -> D; kE*Tct*Ev/(KEv + Ev + Tct);

J7: -> Tct; g*Tc;
J8: Tct ->; dC*Tct;
J9: Tct ->; dT1*Tct*Da/(Da+dT2);

J10: -> V; pV*Ev;
J11: V ->; cV*V;
J12: -> Da; bD*V*(D0-Da); // D0 => initial number of inactive D-cells
J13: Da ->; dD*Da;

// Systemic reactions in Lymph

J14: -> Dm; kD*Da;
J15: Dm ->; dDm*Dm;
J16: -> Tc; dC*Tc0; // Tc0 => initial number of naive Tc-cells
J17: Tc ->; dC*Tc;
J18:  -> Tc; rT1*Dm*Tc/(Dm+rT2); 
J19: Tc ->; dT1*Tc*Dm/(Dm+dT2);

J20: -> Th1; sTh1*Th1/(1+Th2)^2;
J21:  -> Th1; pTh1*Dm*(Th1^2)/(1+Th2)^2;
J22: Th1 ->; dTh1*Dm*(Th1^3)/(1+Th2);
J23: Th1 ->; mTh*Th1;
J24: -> Th2; sTh2*Th2/(1+Th2);
J25:  -> Th2; pTh2*(ro+Th1)*Dm*(Th2^2)/((1+Th2)*(1+Th1+Th2)) 
J26: Th2 ->; mTh*Th2;

// Antibody production

J27: -> B; dB*B0; // B0 => initial number of inactive B-cells
J28: B ->; dB*B;
J29:  -> B; rB1*B*(Dm+h*Th2)/(Dm+h*Th2+rB2);
J30: B -> Pss; pS*B;
J31: B -> Psn; pS*B;
J32: B -> Pls; pL*B*Th2;
J33: B -> Pln; pL*B*Th2;
J34: Pss ->; dS*Pss;
J35: Psn ->; dS*Psn;
J36: Pls ->; dL*Pls;
J37: Pln ->; dL*Pln;
J38: Pss -> Pls; d*(1-v)*Pss;
J39: Psn -> Pln; d*(1-v)*Psn;
J40:  -> Pss; b*v*Pss;
J41:  -> Pls; b*v*Pls;
J42:  -> Psn; b*v*Psn;
J43:  -> Pln; b*v*Pln;
J44: Pls -> Pss; d*(1-v)*Pls;
J45: Pln -> Psn; d*(1-v)*Pln; 

J46:  -> sIgM; pAS*Pss;
J47:  -> nIgM; pAS*Psn;
J48:  -> sIgG; pAS*Pls;
J49:  -> nIgG; pAS*Pln;
J50: sIgM ->; dM*sIgM;
J51: sIgG ->; dG*sIgG;
J52: nIgM ->; dM*nIgM;
J53: nIgG ->; dG*nIgG;

// Antibody feedback to tissue

J54: Ev + nIgM -> D; eE*Ev*nIgM; 
J55: Ev + nIgG -> D; eE*Ev*nIgG;
J56: V + sIgM ->; eV*V*sIgM;
J57: V + sIgG ->; eV*V*sIgG;


/////////////////// Parameters ///////////////////////

// Epithelial infection

dE=10^-3;
E0 = 5.0*10^5;
bE=7.0*10^-6;
dEv=0.12;
aE=5.0*10^-1;
pV=1.9;
cV=1.0;

// Dendritic cell infection, activation, migration

D0=10^4;
bD=10^-6;
dD=2.9;
kD = 0.5;
dDm = 0.5;

// Cytotoxic T-cell activation, proliferation

dC=2.0*10^-3;
Tc0=2.0*10^3;
rT1=3.5;
rT2=2.0*10^3;
dT1=1.0;
dT2=1.0;

// T-cell mediated Cytotoxicity

kE=1.19*10^-2;
g=0.15;
KEv = 500.0;

// Helper T-cell activation, proliferation

sTh1=1.0;
pTh1=0.012;
dTh1=0.001;
KTh1 =500.0;
mTh=0.0225;
sTh2=0.04;
pTh2=0.003;
ro=1.0;

// B-cell activation, proliferation, differentiation

dB=0.02;
B0=2.0*10^1;
rB1=4.5;
rB2=1*10^4;
h=1.0;

// Plasma cell proliferation, differentiation and antibody production

pS=3.0*10^-1;
pL=1.5*10^-4;
dS=0.2;
dL=0.02;
b=2.4*10^-2;
d=2.4*10^-2;
pAS=0.8*10^2;
pAL=1.2*10^2;
dG=0.5;
dM=2.0;

// Switching functions of the Plasma Cells

u =  0.5;
v =  0.5;

// Antibody activity: virus and cell killing

eE=0.0001;
eV=0.00018;

////////////////// Initial Conditions /////////////////////

E = 5.0*10^5; // Uninfected epithelial cells
Ev = 10.0; // Virus-infected epithelial cells
V = 1000.0; // 
Da = 0.0; // Infected-activated dendtritic cells in Tissue

Dm = 0.0; // Migrated dendritic cells in Lymph
Tc = 1.0; // Effector cytotoxic T-cells in Lymph
Tct = 0.0; // Effector cytotoxic T-cells in Tissue
Th1 = 1.0; // Type I helper T-cells
Th2 = 1.0; // Type II helper T-cells

B = 1.0; // Activated B-cells
pSs = 0.0; // SP-RBD-specific Short-living plasma cells
pLs = 0.0; // SP-RBD-specific Long-living plasma cells
pSn = 0.0; // NP-specific Short-living plasma cells
pLn = 0.0; // NP-specific Long-living plasma cells

sIgM = 0.0; // SP-RBD-specific IgM
sIgG = 0.0; // SP-RBD-specific IgG
nIgM = 0.0; // NP-specific IgM
nIgG = 0.0; // NP-specific IgG

'''
rr = te.loadAntimonyModel(model_string)
n = rr.simulate(0,30,10000,['time','Tc','Tct','Da','Dm'])
rr.plot()

