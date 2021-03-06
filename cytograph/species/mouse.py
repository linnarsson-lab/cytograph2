import numpy as np
# Cell cycle gene sets from Tirosh et al. doi:10.1126/science.aad0501, plus histones for S phase from own analyses
# Removed BIRC5 because it's expressed in certain non-cycling heart cells
g1_mouse = ['Mcm5', 'Pcna', 'Tyms', 'Fen1', 'Mcm2', 'Mcm4', 'Rrm1', 'Ung', 'Gins2', 'Mcm6', 'Cdca7', 'Dtl', 'Prim1', 'Uhrf1', 'Cenpu', 'Hells', 'Rfc2', 'Rpa2', 'Nasp', 'Rad51ap1', 'Gmnn', 'Wdr76', 'Slbp', 'Ccne2', 'Ubr7', 'Pold3', 'Msh2', 'Atad2', 'Rad51', 'Rrm2', 'Cdc45', 'Cdc6', 'Exo1', 'Tipin', 'Dscc1', 'Blm', 'Casp8ap2', 'Usp1', 'Clspn', 'Pola1', 'Chaf1b', 'Brip1', 'E2f8']
s_mouse = ["Hist1h2aj", "Hist1h2am", "Hist1h1d", "Hist1h4c"]
g2m_mouse = ['Hmgb2', 'Cdk1', 'Nusap1', 'Ube2c', 'Tpx2', 'Top2a', 'Ndc80', 'Cks2', 'Nuf2', 'Cks1b', 'Mki67', 'Tmpo', 'Cenpf', 'Tacc3', 'Fam64a', 'Smc4', 'Ccnb2', 'Ckap2l', 'Ckap2', 'Aurkb', 'Bub1', 'Kif11', 'Anp32e', 'Tubb4b', 'Gtse1', 'Kif20b', 'Hjurp', 'Hjurp', 'Cdca3', 'Hn1', 'Cdc20', 'Ttk', 'Cdc25c', 'Kif2c', 'Rangap1', 'Ncapd2', 'Dlgap5', 'Cdca2', 'Cdca8', 'Ect2', 'Kif23', 'Hmmr', 'Aurka', 'Psrc1', 'Anln', 'Lbr', 'Ckap5', 'Cenpe', 'Ctcf', 'Nek2', 'G2e3', 'Gas2l3', 'Cbx5', 'Cenpa']

cc_genes_mouse = np.array([
	'Abhd3', 'Ac016205.1', 'Ac073529.1', 'Ac084033.3', 'Ac087632.1',
	'Ac091057.6', 'Ac097534.2', 'Ac099850.2', 'Ac135586.2', 'Acaa2',
	'Acadm', 'Acp1', 'Actl6a', 'Acyp1', 'Adcy3', 'Add3', 'Adk', 'Ahcy',
	'Akirin2', 'Akr7a2', 'Al359513.1', 'Al449266.1', 'Al513165.2',
	'Anapc11', 'Anln', 'Anp32a', 'Anp32b', 'Anp32e', 'Ap001347.1',
	'Apold1', 'Arhgap11a', 'Arhgef39', 'Arid1a', 'Arl6ip1', 'Arl6ip6',
	'Armc1', 'Asf1b', 'Aspm', 'Asrgl1', 'Atad2', 'Atad5',
	'Atp1b3', 'Aurka', 'Aurkb', 'Banf1', 'Bard1', 'Baz1a', 'Baz1b',
	'Birc5', 'Blm', 'Bora', 'Brca1', 'Brca2', 'Brd8', 'Brip1', 'Btg3',
	'Bub1', 'Bub1b', 'Bub3', 'C11orf58', 'C19orf48', 'C1orf112',
	'C1orf35', 'C21orf58', 'C5orf34', 'Cacybp', 'Camta1',
	'Carhsp1', 'Cbx1', 'Cbx3', 'Cbx5', 'Ccar1', 'Ccdc14', 'Ccdc167',
	'Ccdc18', 'Ccdc34', 'Ccdc77', 'Ccna1', 'Ccna2', 'Ccnb1', 'Ccnb2',
	'Ccne2', 'Ccnf', 'Cct4', 'Cct5', 'Cdc20', 'Cdc25b', 'Cdc25c',
	'Cdc27', 'Cdc45', 'Cdc6', 'Cdc7', 'Cdca2', 'Cdca3', 'Cdca4',
	'Cdca7l', 'Cdca8', 'Cdk1', 'Cdk19', 'Cdk2', 'Cdk4', 'Cdk5rap2',
	'Cdkal1', 'Cdkn1b', 'Cdkn2c', 'Cdkn3', 'Cdt1', 'Cenpa', 'Cenpc',
	'Cenpe', 'Cenpf', 'Cenph', 'Cenpi', 'Cenpj', 'Cenpk', 'Cenpl',
	'Cenpm', 'Cenpn', 'Cenpo', 'Cenpp', 'Cenpq', 'Cenpu', 'Cenpw',
	'Cenpx', 'Cep112', 'Cep128', 'Cep135', 'Cep192', 'Cep295', 'Cep55',
	'Cep57', 'Cep57l1', 'Cep70', 'Cetn3', 'Cfap20', 'Cfl2', 'Cggbp1',
	'Chaf1a', 'Chchd2', 'Chek1', 'Chek2', 'Chrac1', 'Cip2a', 'Cit',
	'Ckap2', 'Ckap2l', 'Ckap5', 'Cklf', 'Cks1b', 'Cks2', 'Clspn',
	'Cmc2', 'Cmss1', 'Cnih4', 'Cnn3', 'Cntln', 'Cntrl', 'Coa1',
	'Commd4', 'Cox8a', 'Cse1l', 'Ctcf', 'Ctdspl2', 'Cwf19l2', 'Cyb5b',
	'Cycs', 'Dach1', 'Dbf4', 'Dbf4b', 'Dbi', 'Dcaf7', 'Dcp2', 'Dcxr',
	'Ddah2', 'Ddx39a', 'Ddx46', 'Dek', 'Depdc1', 'Depdc1b', 'Desi2',
	'Dhfr', 'Diaph3', 'Dkc1', 'Dleu2', 'Dlgap5', 'Dna2', 'Dnajb1',
	'Dnajc9', 'Dnmt1', 'Dpm1', 'Dr1', 'Dscc1', 'Dsn1', 'Dtl', 'Dtymk',
	'Dusp16', 'Dut', 'Dynll1', 'Dyrk1a', 'E2f3', 'E2f7', 'E2f8',
	'Ect2', 'Eed', 'Eef1d', 'Eid1', 'Eif1ax', 'Eif2s2', 'Eif4a3',
	'Eif4e', 'Eif5', 'Emc9', 'Enah', 'Eno1', 'Eny2', 'Erh', 'Esco2',
	'Ewsr1', 'Exosc8', 'Ezh2', 'Fam111b', 'Fam122b', 'Fam72c',
	'Fam72d', 'Fam83d', 'Fancb', 'Fancd2', 'Fanci', 'Fancl', 'Fbl',
	'Fbxl5', 'Fbxo5', 'Fdps', 'Fdx1', 'Fen1', 'Fgfr1op', 'Filip1l',
	'Foxm1', 'Fus', 'Fuz', 'Fxr1', 'Fzr1', 'G2e3', 'G3bp1', 'Gabpb1',
	'Gas2l3', 'Gemin2', 'Gen1', 'Ggct', 'Ggh', 'Gins2',
	'Glo1', 'Gmnn', 'Gmps', 'Gng5', 'Gpbp1', 'Gpsm2', 'Gtse1', 'H1fx',
	'H2afv', 'H2afx', 'H2afy', 'H2afz', 'Hacd3', 'Hadh', 'Hat1',
	'Haus1', 'Haus6', 'Haus8', 'Hdac2', 'Hdgf', 'Hells', 'Hes1',
	'Hint1', 'Hirip3', 'Hist1h1a', 'Hist1h1c', 'Hist1h1d', 'Hist1h2bh',
	'Hist1h4c', 'Hist2h2ac', 'Hjurp', 'Hmg20b', 'Hmga1', 'Hmga2',
	'Hmgb1', 'Hmgb2', 'Hmgb3', 'Hmgn1', 'Hmgn2', 'Hmgn3', 'Hmgn5',
	'Hmgxb4', 'Hmmr', 'Hnrnpa0', 'Hnrnpa1', 'Hnrnpa2b1', 'Hnrnpa3',
	'Hnrnpab', 'Hnrnpc', 'Hnrnpd', 'Hnrnpdl', 'Hnrnpf', 'Hnrnph3',
	'Hnrnpk', 'Hnrnpll', 'Hnrnpm', 'Hnrnpu', 'Hnrnpul1', 'Hp1bp3',
	'Hpf1', 'Hsd17b11', 'Hsp90b1', 'Hspa13', 'Hspa1b',
	'Hspb11', 'Hspd1', 'Hspe1', 'Hyls1', 'Idh2', 'Ift122', 'Igf2bp3',
	'Ikbip', 'Ilf2', 'Ilf3', 'Ilvbl', 'Immp1l', 'Incenp', 'Ipo5',
	'Iqgap3', 'Isca2', 'Isoc1', 'Itgae', 'Itgb3bp', 'Jade1', 'Jpt1',
	'Katnbl1', 'Kctd9', 'Kiaa0586', 'Kif11', 'Kif14', 'Kif15',
	'Kif18a', 'Kif18b', 'Kif20a', 'Kif20b', 'Kif22', 'Kif23', 'Kif2c',
	'Kif4a', 'Kif5b', 'Kifc1', 'Kmt5a', 'Knl1', 'Knstrn', 'Kpna2',
	'Kpnb1', 'Larp7', 'Lbr', 'Lcorl', 'Lig1', 'Lin52',
	'Linc01224', 'Linc01572', 'Lmnb1', 'Lmnb2', 'Lrr1', 'Lsm14a',
	'Lsm2', 'Lsm3', 'Lsm4', 'Lsm5', 'Lsm6', 'Lsm7', 'Lsm8', 'Luc7l2',
	'Mad2l1', 'Magi1', 'Magoh', 'Magohb', 'Mapk1ip1l', 'Mapre1',
	'Marcks', 'Mastl', 'Mbnl2', 'Mcm10', 'Mcm2', 'Mcm3', 'Mcm4',
	'Mcm5', 'Mcm7', 'Med30', 'Melk', 'Mgme1', 'Mis18a',
	'Mis18bp1', 'Mki67', 'Mms22l', 'Mnd1', 'Mns1', 'Morf4l2',
	'Mphosph9', 'Mre11', 'Mrpl18', 'Mrpl23', 'Mrpl47', 'Mrpl51',
	'Mrpl57', 'Mrps34', 'Mtfr2', 'Mybl2', 'Myef2', 'Mzt1', 'Mzt2b',
	'Naa38', 'Naa50', 'Nae1', 'Nap1l1', 'Nap1l4', 'Nasp', 'Ncapd2',
	'Ncapd3', 'Ncapg', 'Ncapg2', 'Ncaph', 'Ncl', 'Ndc1', 'Ndc80',
	'Nde1', 'Ndufa6', 'Ndufaf3', 'Ndufs6', 'Nedd1', 'Neil3', 'Nek2',
	'Nelfe', 'Nenf', 'Nfatc3', 'Nfyb', 'Nipbl', 'Nmu', 'Nono', 'Nop56',
	'Nop58', 'Nrdc', 'Nsd2', 'Nsmce2', 'Nsmce4a', 'Nucks1', 'Nudc',
	'Nudcd2', 'Nudt1', 'Nudt15', 'Nudt21', 'Nudt5', 'Nuf2', 'Nup107',
	'Nup35', 'Nup37', 'Nup50', 'Nup54', 'Nusap1', 'Odc1', 'Odf2',
	'Oip5', 'Orc6', 'Pa2g4', 'Paics', 'Paip2', 'Pak4', 'Papola',
	'Parp1', 'Parpbp', 'Paxx', 'Pbk', 'Pcbd2', 'Pcbp2', 'Pcm1', 'Pcna',
	'Pcnp', 'Pds5b', 'Phf19', 'Phf5a', 'Phgdh', 'Phip', 'Pif1',
	'Pimreg', 'Pin1', 'Plcb1', 'Plgrkt', 'Plin3', 'Plk1',
	'Plk4', 'Pmaip1', 'Pnisr', 'Pnn', 'Pnrc2', 'Poc1a', 'Pold2',
	'Pold3', 'Pole2', 'Polq', 'Polr2c', 'Polr2d', 'Polr2g', 'Polr2j',
	'Polr2k', 'Polr3k', 'Ppia', 'Ppig', 'Ppih', 'Ppp1cc', 'Ppp2r3c',
	'Ppp2r5c', 'Ppp6r3', 'Prc1', 'Prdx3', 'Prim1', 'Prim2',
	'Prpf38b', 'Prpsap1', 'Prr11', 'Psip1', 'Psma3', 'Psma4', 'Psmb2',
	'Psmb3', 'Psmc3', 'Psmc3ip', 'Psmd10', 'Psmd14', 'Psmg2', 'Psrc1',
	'Ptbp1', 'Ptges3', 'Ptma', 'Ptms', 'Pttg1', 'Puf60', 'Rab8a',
	'Racgap1', 'Rad21', 'Rad51ap1', 'Rad51b', 'Rad51c', 'Ran',
	'Ranbp1', 'Rangap1', 'Rassf1', 'Rbbp4', 'Rbbp8', 'Rbl1', 'Rbm17',
	'Rbm39', 'Rbm8a', 'Rbmx', 'Rcc1', 'Rdx', 'Reep4', 'Rfc1', 'Rfc2',
	'Rfc3', 'Rfc4', 'Rfwd3', 'Rheb', 'Rmi2', 'Rnaseh2b', 'Rnaseh2c',
	'Rnf138', 'Rnf168', 'Rnf26', 'Rnps1', 'Rpa1', 'Rpa3', 'Rpl35',
	'Rpl39l', 'Rplp0', 'Rplp1', 'Rplp2', 'Rpn2', 'Rpp30', 'Rps15',
	'Rps16', 'Rps20', 'Rps21', 'Rpsa', 'Rrm1', 'Rsrc1', 'Rsrc2',
	'Rtkn2', 'Ruvbl2', 'Sac3d1', 'Sae1', 'Sap18', 'Sapcd2', 'Scaf11',
	'Sclt1', 'Sdhaf3', 'Selenok', 'Sem1', 'Sephs1',
	'Serbp1', 'Set', 'Sf1', 'Sf3b2', 'Sfpq', 'Sgo1', 'Sgo2',
	'Shcbp1', 'Sinhcaf', 'Siva1', 'Ska1', 'Ska2', 'Ska3', 'Slbp',
	'Slc20a1', 'Slc25a3', 'Sltm', 'Smc1a', 'Smc2', 'Smc3', 'Smc4',
	'Smc5', 'Smchd1', 'Snapc1', 'Snrnp25', 'Snrnp40', 'Snrnp70',
	'Snrpa', 'Snrpa1', 'Snrpb', 'Snrpc', 'Snrpd1', 'Snrpd2', 'Snrpd3',
	'Snrpe', 'Snrpf', 'Snrpg', 'Son', 'Spag5', 'Spata5', 'Spc25',
	'Spcs2', 'Spdl1', 'Srek1', 'Sri', 'Srp9', 'Srrm1', 'Srsf1',
	'Srsf10', 'Srsf11', 'Srsf2', 'Srsf3', 'Srsf4', 'Srsf7', 'Ssb',
	'Ssbp1', 'Ssna1', 'Ssrp1', 'St13', 'Stag1', 'Stil', 'Stip1',
	'Stk17b', 'Stk3', 'Stoml2', 'Sugp2', 'Sumo1', 'Sumo3', 'Supt16h',
	'Suv39h2', 'Suz12', 'Syne2', 'Tacc3', 'Tbc1d31', 'Tbc1d5', 'Tdp1',
	'Tead1', 'Tex30', 'Tfdp1', 'Thrap3', 'Ticrr', 'Timeless', 'Timm10',
	'Tk1', 'Tmed5', 'Tmem106c', 'Tmem237', 'Tmem60', 'Tmem97', 'Tmpo',
	'Tmsb15a', 'Top1', 'Top2a', 'Tpi1', 'Tpr', 'Tprkb', 'Tpx2',
	'Tra2b', 'Traip', 'Troap', 'Ttc28', 'Ttf2', 'Ttk', 'Txndc12', 'Tyms',
	'Uba2', 'Ubb', 'Ube2c', 'Ube2d2', 'Ube2d3', 'Ube2i', 'Ube2n',
	'Ube2s', 'Ube2t', 'Uhrf1', 'Ung', 'Uqcc2', 'Uqcc3', 'Uqcrc1',
	'Uqcrfs1', 'Usp1', 'Vbp1', 'Vdac3', 'Vezf1', 'Vrk1', 'Wapl',
	'Wdhd1', 'Wdpcp', 'Wdr34', 'Wdr76', 'Xpo1', 'Xrcc4', 'Xrcc5',
	'Xrcc6', 'Yap1', 'Ybx1', 'Yeats4', 'Z94721.1', 'Zfp36l1', 'Zgrf1',
	'Zmym1', 'Znf22', 'Znf367', 'Znf43', 'Znf704', 'Znf83', 'Zranb3',
	'Zscan16-as1', 'Zwint'], dtype=object)

# RIKEN FANTOM5 curated mouse TFs (http://fantom.gsc.riken.jp/5/sstar/Data_source)
TFs_mouse = [
	"Atf3",
	"Mynn",
	"Arid3a",
	"Crebbp",
	"Nfe2l2",
	"Khsrp",
	"Tbx3",
	"Hic1",
	"Zfp148",
	"Zfp651",
	"Smad6",
	"Zfp438",
	"Zfp597",
	"Hsfy2",
	"Foxj1",
	"Lhx3",
	"Stat3",
	"Zc3h12a",
	"Nr2c1",
	"Hoxc13",
	"Kdm5d",
	"Sox2",
	"Zbtb7a",
	"Neurod6",
	"Atf5",
	"Hoxb2",
	"Lhx1",
	"Nr3c2",
	"Egr1",
	"Smarca5",
	"Zfp382",
	"Xbp1",
	"Foxa3",
	"Uncx",
	"Creb3l1",
	"Zfp280c",
	"Skil",
	"Zfat",
	"Zfp609",
	"Zfp560",
	"Helt",
	"Hoxa5",
	"Zfp503",
	"Hhex",
	"Klf10",
	"Nfrkb",
	"Ezh2",
	"Satb1",
	"Alx1",
	"Hivep1",
	"Zfp217",
	"Zfp280d",
	"Foxh1",
	"Zfp385b",
	"Zfp37",
	"Ankzf1",
	"Zfp366",
	"Csda",
	"Ncoa7",
	"Nrl",
	"Nfil3",
	"Zfp82",
	"Tcf20",
	"Rax",
	"Mtf1",
	"Pax7",
	"Zfp69",
	"Rcor1",
	"Gata6",
	"Tbr1",
	"Nr1d2",
	"Hmx2",
	"Hoxd8",
	"Stat1",
	"Mllt10",
	"Atf6",
	"Ascl2",
	"Hmbox1",
	"Zc3h13",
	"Foxn2",
	"Tfap2d",
	"Irx3",
	"Foxl1",
	"L3mbtl3",
	"Etv4",
	"Myst4",
	"Erg",
	"Ets1",
	"Sox21",
	"Zbtb48",
	"Foxk1",
	"Barx2",
	"Gm608",
	"Osr1",
	"Klf9",
	"Egr3",
	"Zfp324",
	"Ezh1",
	"Atrx",
	"Zfp764",
	"Rfx3",
	"Zbtb1",
	"Zfp161",
	"Prdm11",
	"Purb",
	"Six3",
	"Zic3",
	"Pou2af1",
	"Zfp319",
	"Spib",
	"Zfp238",
	"Hic2",
	"Tead2",
	"Ctcf",
	"Dmrt1",
	"Zfp42",
	"Zfp787",
	"Sox12",
	"Foxp2",
	"Tfdp1",
	"Zfp622",
	"Eomes",
	"Tgif1",
	"Tbp",
	"Tbx4",
	"C330006K01Rik",
	"Cenpt",
	"Pou3f4",
	"Hdx",
	"Zbtb38",
	"Zfp768",
	"Zkscan16",
	"Zfp488",
	"Arx",
	"Rhox10",
	"Ascl3",
	"Hoxc6",
	"Ncoa2",
	"Sp100",
	"Ash1l",
	"Zfp872",
	"Sp140",
	"Usf1",
	"Ikzf1",
	"Zfp335",
	"Gsc",
	"Zfp691",
	"Zim2",
	"Ikzf2",
	"Dbx2",
	"Zfp784",
	"Csrnp2",
	"Zfp444",
	"Hnrnpk",
	"Bsx",
	"Smarca2",
	"Mbd4",
	"Hes6",
	"Nfkbia",
	"Barhl2",
	"Adnp2",
	"Bcl11a",
	"Foxc1",
	"Pou4f1",
	"Zic4",
	"Rhox13",
	"Foxf2",
	"Matr3",
	"Myb",
	"Hoxc12",
	"Yeats2",
	"Zfp105",
	"Zbp1",
	"Zfp618",
	"Myt1",
	"Msx1",
	"Spic",
	"Klf6",
	"Prrx1",
	"Tead3",
	"Dmrtb1",
	"Zc3h8",
	"Zfp354a",
	"Zfp598",
	"Lrrfip2",
	"Msc",
	"Zim1",
	"Jazf1",
	"Irx1",
	"Esx1",
	"Hes1",
	"Mycl1",
	"Mga",
	"Hesx1",
	"Sox1",
	"Dlx6",
	"Nkx6-2",
	"Sall4",
	"Mycn",
	"Zfp523",
	"Nfe2l1",
	"Nono",
	"Runx1",
	"Vdr",
	"Neurod1",
	"Zfp36l2",
	"Kat5",
	"Rc3h2",
	"E4f1",
	"Zfp867",
	"Npas3",
	"Prdm2",
	"Mesp1",
	"Zfp365",
	"Myc",
	"Zfp58",
	"Hoxb13",
	"Zfp167",
	"Dnajc21",
	"Zfp454",
	"Arnt",
	"Nanog",
	"Pbx3",
	"Tcf3",
	"Dmrtc2",
	"Foxj2",
	"Zfpm2",
	"Unk",
	"Tlx1",
	"Prkrir",
	"Zfp71-rs1",
	"Nkx2-9",
	"Ebf2",
	"Rorc",
	"Foxb1",
	"Nr1h4",
	"Fosl2",
	"Batf",
	"Nkx2-3",
	"Ubp1",
	"Bhlhe22",
	"Rfx7",
	"Neurog2",
	"Creb1",
	"Tada2a",
	"Thrb",
	"Zfp180",
	"Gsx2",
	"Hmgxb4",
	"Dpf3",
	"Six5",
	"Etv2",
	"Bhlha9",
	"Trp63",
	"Zbtb11",
	"Zfp786",
	"Gcfc1",
	"Rfx5",
	"Mll5",
	"Tsc22d4",
	"Zfp704",
	"Snapc4",
	"Hmgxb3",
	"Hkr1",
	"Maz",
	"Npas2",
	"Zfp827",
	"Tshz1",
	"Sp8",
	"Meis2",
	"Kdm5a",
	"Fos",
	"Lhx4",
	"Nfib",
	"Pcbp1",
	"Snai1",
	"Zfp160",
	"Kcnip3",
	"Phf20",
	"Utf1",
	"Mta2",
	"Zfp940",
	"Scaper",
	"Arid1a",
	"Phox2a",
	"Preb",
	"Zfp386",
	"Ehf",
	"Ciz1",
	"Zfp608",
	"Zfp830",
	"Epas1",
	"Bola2",
	"Irf6",
	"Zfp653",
	"Ttf1",
	"Skor1",
	"Runx2",
	"Rsl1",
	"Nr5a1",
	"Pknox1",
	"Zmat1",
	"Trp73",
	"Runx1t1",
	"Tax1bp3",
	"Pou5f1",
	"Rfx4",
	"Zcchc11",
	"Zfp449",
	"Rlf",
	"Lrrfip1",
	"Klf5",
	"Zbtb6",
	"Tfap2e",
	"Ppp1r13l",
	"Tfb1m",
	"Aire",
	"Prdm4",
	"Zbtb25",
	"Myog",
	"Aff3",
	"Pcgf6",
	"Hoxb7",
	"Nfatc4",
	"Foxd1",
	"Nfix",
	"Rbpj",
	"Zfp697",
	"Hoxa6",
	"Ncoa4",
	"Bclaf1",
	"Zfp800",
	"Cxxc1",
	"Irf2",
	"Zfp874b",
	"Zfp282",
	"Zhx3",
	"Aebp2",
	"Fezf2",
	"Zfp248",
	"Atf7",
	"Dlx5",
	"Noc4l",
	"Snai3",
	"Dmtf1",
	"Thap8",
	"Zmat3",
	"Hsf4",
	"Foxe1",
	"Zfp420",
	"Bhlhe41",
	"Ski",
	"Atoh1",
	"Tcf4",
	"Zbtb42",
	"Jarid2",
	"Tsc22d2",
	"Cpxcr1",
	"Sp5",
	"Mybl2",
	"Zic5",
	"Nfatc2",
	"Isl2",
	"Mllt11",
	"Nr0b2",
	"Zfp574",
	"Zfp354c",
	"Tal2",
	"Hmga2",
	"Crebl2",
	"Hoxa11",
	"Mbd1",
	"Nkrf",
	"Zbtb39",
	"Ybx1",
	"Vax2",
	"Spdef",
	"Zfp414",
	"Rfx8",
	"Tal1",
	"Tbx22",
	"Dbx1",
	"Tada2b",
	"Zfp142",
	"Nkx2-6",
	"Klf3",
	"Sp4",
	"Emx1",
	"Zfp821",
	"Zfp341",
	"Smarcc2",
	"Rcor2",
	"Jdp2",
	"Zfp644",
	"Mysm1",
	"Nkx6-1",
	"Dmap1",
	"L3mbtl2",
	"Hlf",
	"Hopx",
	"Relb",
	"Bmyc",
	"Dach1",
	"Tlx3",
	"Zfp273",
	"Zfp703",
	"Pax2",
	"Mta1",
	"Nr1h5",
	"Zfp759",
	"Trp53",
	"Ttf2",
	"Tbx15",
	"Rcor3",
	"Zfp607",
	"Zfp398",
	"Patz1",
	"Glis1",
	"Dpf1",
	"Zkscan3",
	"Pitx3",
	"Hes3",
	"Nfat5",
	"Rorb",
	"Dmbx1",
	"Cebpz",
	"Zfp174",
	"Nr2c2",
	"Osr2",
	"Crem",
	"Gmeb2",
	"Alx4",
	"Zfp111",
	"Zfp639",
	"Sox8",
	"Zbtb20",
	"Zkscan5",
	"Hoxc5",
	"Creb3",
	"Foxr1",
	"Yy1",
	"Rest",
	"Sp1",
	"Zfp791",
	"Zfp746",
	"Tgif2",
	"Terf1",
	"Npas4",
	"Isx",
	"Zfp583",
	"Zfp106",
	"Arid4b",
	"Id1",
	"Bach2",
	"Zfp750",
	"Meis3",
	"Nfya",
	"Akna",
	"Zfp655",
	"Zfp592",
	"Hoxb4",
	"Zfp11",
	"Gm4944",
	"Grlf1",
	"Ovol2",
	"Hoxc8",
	"Pawr",
	"Wiz",
	"Sox18",
	"Zfp14",
	"Phb2",
	"Hinfp",
	"Zfp219",
	"Tfap2c",
	"Zfp202",
	"Zfp275",
	"Klf12",
	"Zfp92",
	"Grhl3",
	"Rfx1",
	"Zfp738",
	"Mllt4",
	"Parp12",
	"Hoxa10",
	"Lcorl",
	"En1",
	"Ebf1",
	"Homez",
	"Elk1",
	"E2f6",
	"Eno1",
	"Erf",
	"Zfp281",
	"Mier1",
	"Zfp629",
	"Ptf1a",
	"Hoxa1",
	"Zfp719",
	"Nfic",
	"Bcl11b",
	"Foxn3",
	"Tcf15",
	"Nfkbid",
	"Atf1",
	"Klf1",
	"Zfp286",
	"Zbtb10",
	"Mef2a",
	"L3mbtl1",
	"Zc3h4",
	"Phtf1",
	"Cux2",
	"Zcchc6",
	"Zbtb46",
	"Foxn4",
	"Zfp623",
	"Klf17",
	"Pax1",
	"Zfp74",
	"E2f8",
	"Sox9",
	"Pou5f2",
	"Glis2",
	"Ncoa6",
	"Olig2",
	"Hoxb9",
	"Smad3",
	"Klf15",
	"Zfp407",
	"Zfp113",
	"Hoxd12",
	"Six2",
	"Stat6",
	"Foxo3",
	"Gtf2i",
	"Gabpa",
	"Phf5a",
	"Cebpe",
	"Rarb",
	"Ebf3",
	"Hoxa3",
	"Ebf4",
	"Zfp110",
	"Msx3",
	"Dlx2",
	"Rxra",
	"Dnmt3b",
	"Lyar",
	"Yeats4",
	"Gli2",
	"Zfp668",
	"Zscan30",
	"Foxp4",
	"Pdx1",
	"Zfp30",
	"Foxa2",
	"Wt1",
	"Zscan22",
	"Rfxank",
	"Foxo1",
	"Dlx1",
	"Nrf1",
	"Ddit3",
	"Gfi1b",
	"Fubp3",
	"Ncoa3",
	"Nr1i3",
	"Grhl2",
	"Hbp1",
	"Foxn1",
	"Rfx6",
	"Hif3a",
	"Scrt2",
	"Lhx2",
	"Setbp1",
	"Zbtb37",
	"Ikzf4",
	"Rbm22",
	"Zic2",
	"Zfp367",
	"Nkx2-1",
	"Zfp13",
	"Pknox2",
	"Taf1",
	"Zfp207",
	"Zfp187",
	"Dnmt1",
	"Hoxd10",
	"Sebox",
	"Zfp507",
	"Klf13",
	"Casz1",
	"Rora",
	"Nr4a2",
	"Lhx6",
	"Smarca1",
	"Nhlh1",
	"Zfp524",
	"Nfkbiz",
	"Foxs1",
	"Pou2f2",
	"Atoh8",
	"Stat4",
	"Mllt3",
	"Tcf7",
	"Atoh7",
	"Zbtb32",
	"Thap4",
	"Zfp526",
	"Etv5",
	"Zfp346",
	"Zfp251",
	"Ascl1",
	"Gzf1",
	"Thap1",
	"Batf2",
	"Maff",
	"Camta1",
	"Nr1h2",
	"Elk3",
	"Phtf2",
	"Arid5b",
	"Zbtb41",
	"Hey1",
	"Zkscan1",
	"Msx2",
	"Zfp362",
	"Ash2l",
	"Esrrg",
	"Mtf2",
	"D630045J12Rik",
	"Arntl2",
	"Zfp64",
	"Egr2",
	"Cux1",
	"Tsc22d3",
	"Csrnp3",
	"Hmga1",
	"Zfp326",
	"Hnf1b",
	"Carhsp1",
	"Bach1",
	"Zik1",
	"Irf7",
	"Ikzf3",
	"Zfp953",
	"Zscan29",
	"Zfp292",
	"Zc3h7b",
	"Mef2c",
	"Terf2",
	"Myst1",
	"Zfp108",
	"Sox30",
	"Dr1",
	"Nfxl1",
	"Zfp516",
	"Fam170a",
	"Irf5",
	"Otp",
	"Zfp27",
	"Mnx1",
	"Zfp9",
	"Zkscan17",
	"Zfp667",
	"Sox5",
	"Mesp2",
	"Ncor2",
	"Zic1",
	"Otx1",
	"Tbx1",
	"Nfatc3",
	"Zxdc",
	"Prdm1",
	"Nkx2-4",
	"Smarcb1",
	"Zfp580",
	"Tox",
	"Zeb2",
	"Zfp296",
	"Tead1",
	"Creb3l2",
	"Zfp874a",
	"Zfp804a",
	"Irf8",
	"Zc3h11a",
	"Irx4",
	"Whsc1",
	"Zfp532",
	"Rel",
	"Zzz",
	"Pax3",
	"Zfp518b",
	"Gmeb1",
	"Zfp146",
	"Sox14",
	"Bola1",
	"Prop1",
	"Junb",
	"Cdc5l",
	"Tbx21",
	"Zfp46",
	"Zfp91",
	"Zfp513",
	"Foxi3",
	"Rhox6",
	"Pitx2",
	"Tcf25",
	"Smarcd1",
	"Zbtb8b",
	"Peg3",
	"Zfp263",
	"E2f1",
	"Cramp1l",
	"Hnf1a",
	"Foxd2",
	"Pbx1",
	"Etv3",
	"Zfp775",
	"Deaf1",
	"Zfp84",
	"Noc3l",
	"Mafa",
	"Smarcd2",
	"Fezf1",
	"Rhox8",
	"Hmg20b",
	"Klf11",
	"Snai2",
	"Zfp189",
	"Atf4",
	"Barhl1",
	"Zfp462",
	"Hivep2",
	"Arid4a",
	"Zufsp",
	"Usf2",
	"Pax5",
	"Zfp790",
	"AW146020",
	"Zfp94",
	"Zkscan14",
	"Kcmf1",
	"Zfp1",
	"Zfp354b",
	"Zbtb49",
	"Zbtb24",
	"Pcbp2",
	"Rxrb",
	"Zfp689",
	"Elk4",
	"Mll2",
	"Elf1",
	"Hoxb6",
	"Zfp637",
	"Arntl",
	"Zfp677",
	"Cbfb",
	"Onecut3",
	"Zfp810",
	"Trerf1",
	"Smarcal1",
	"Zfp280b",
	"Zfp770",
	"Cebpd",
	"Pogz",
	"Sp6",
	"Sp110",
	"Tfam",
	"Zkscan6",
	"Myod1",
	"Zfp658",
	"Smarcd3",
	"Nr4a1",
	"Zfp711",
	"Zfp182",
	"Zbtb44",
	"Sim1",
	"Twist2",
	"Vsx1",
	"Gm98",
	"Zfp945",
	"Creb3l4",
	"Slc30a9",
	"Nhlh2",
	"Nr3c1",
	"Irx2",
	"Phox2b",
	"Pou3f3",
	"Nfkb2",
	"Ctcfl",
	"Smad2",
	"Zfp715",
	"Ybx2",
	"Pitx1",
	"Zeb1",
	"Neurog1",
	"Zfp612",
	"Nkx2-5",
	"Foxk2",
	"Zfp446",
	"Scrt1",
	"E2f7",
	"Etv6",
	"Foxf1a",
	"Pbrm1",
	"Zfp706",
	"Pou1f1",
	"Sox4",
	"Zbtb22",
	"Hoxb3",
	"Dnajc1",
	"Gabpb1",
	"Cebpa",
	"Nr1h3",
	"Atf2",
	"Zfp60",
	"Tet1",
	"Npas1",
	"Hoxc4",
	"Mbd5",
	"Rela",
	"Plek",
	"Phb",
	"Zfp143",
	"Pou4f3",
	"Nfx1",
	"Zc3h6",
	"Rbak",
	"Rreb1",
	"Mbd6",
	"Zfp579",
	"Zfpm1",
	"Atf6b",
	"Six6",
	"Mnt",
	"Gbx2",
	"Rere",
	"Myst2",
	"Dpf2",
	"Dmrt3",
	"Nkx3-2",
	"Ets2",
	"Myf5",
	"Ncor1",
	"Cebpg",
	"Zfp334",
	"Nfe2l3",
	"Aebp1",
	"Zbtb2",
	"Zfp287",
	"Zfp828",
	"Neurod2",
	"Zfp740",
	"Bbx",
	"Zfp652",
	"Tet2",
	"Zfp28",
	"Nkx2-2",
	"Foxa1",
	"Thra",
	"Zfp12",
	"Mlxipl",
	"Isl1",
	"Zfp536",
	"Foxi1",
	"Hmx1",
	"Nr2f2",
	"Kdm2a",
	"Mef2d",
	"Klf7",
	"Nr2f1",
	"Zbtb8a",
	"Rhox12",
	"Nfatc1",
	"Prrxl1",
	"Zfp87",
	"Srf",
	"Zfp606",
	"Topors",
	"Figla",
	"Sall2",
	"Thap6",
	"Rfxap",
	"Foxm1",
	"Etv1",
	"Zfp595",
	"Sohlh2",
	"Rarg",
	"Zfp708",
	"Zbtb3",
	"Ppard",
	"Nfyb",
	"Sox15",
	"Prox2",
	"Mecom",
	"Thap3",
	"Max",
	"Dach2",
	"Znfx1",
	"Gbx1",
	"Zbed3",
	"Grhl1",
	"Foxl2",
	"Evx2",
	"Zmat4",
	"Zfp329",
	"Pcbp3",
	"Thap11",
	"Insm1",
	"Prdm15",
	"Klf14",
	"Zfp647",
	"Zfp59",
	"Jun",
	"Alx3",
	"Dmrta1",
	"Sfpq",
	"Prdm16",
	"Ncoa5",
	"Hoxc10",
	"Satb2",
	"Clock",
	"Vax1",
	"Olig3",
	"Hsf1",
	"Foxo4",
	"Srebf2",
	"Zfp397",
	"Irf1",
	"Mier3",
	"Tcf23",
	"Zfp395",
	"Zfp3",
	"Zfp39",
	"Egr4",
	"Zbtb33",
	"Mybl1",
	"Sfpi1",
	"Hmg20a",
	"Sox6",
	"Mef2b",
	"Zfp788",
	"Onecut1",
	"Dbp",
	"Zfp322a",
	"Irf4",
	"Gabpb2",
	"Zbtb7c",
	"Onecut2",
	"Meis1",
	"Zfp641",
	"Parp1",
	"Gatad2b",
	"Zfp128",
	"Zfp474",
	"Scx",
	"Prdm13",
	"Hltf",
	"Hsf2",
	"Mbd3l1",
	"Nr2f6",
	"Tax1bp1",
	"Zfp429",
	"Zfhx4",
	"Zmat5",
	"Zfp628",
	"Yy2",
	"Mitf",
	"Zbtb26",
	"Zfp68",
	"Zfp661",
	"Mier2",
	"Nfkbil1",
	"E2f4",
	"Glis3",
	"Ddb2",
	"Bmp2",
	"Meox1",
	"Neurog3",
	"Tfdp2",
	"Tbx19",
	"Zzz3",
	"L3mbtl4",
	"Zfp664",
	"Smad1",
	"Emx2",
	"Mkx",
	"Zfp369",
	"Zfp672",
	"Gata1",
	"Zfy2",
	"Zfp423",
	"Smad9",
	"Mll3",
	"Zbtb4",
	"Lyl1",
	"Vsx2",
	"Plagl1",
	"Zc3h15",
	"Hoxd9",
	"Myst3",
	"Zgpat",
	"Zfp239",
	"Zfp26",
	"Skor2",
	"Zhx1",
	"Zfp191",
	"Zfp213",
	"Zfp51",
	"Nr2e3",
	"Six1",
	"Wdhd1",
	"Foxp1",
	"Mlxip",
	"Atxn7",
	"Thap7",
	"Bhlha15",
	"Arnt2",
	"Zfp410",
	"Bola3",
	"Zbtb7b",
	"Zfp521",
	"Sox11",
	"Zfp687",
	"Stat2",
	"Zfp184",
	"Rxrg",
	"Klf4",
	"Tfeb",
	"Mxd4",
	"Tbx2",
	"Kdm5b",
	"Lhx9",
	"Zfp780b",
	"Fosb",
	"Zfp563",
	"Arid3c",
	"Ferd3l",
	"Mllt1",
	"Pou6f1",
	"Rfx2",
	"Runx3",
	"Zfp418",
	"Zfp317",
	"Barx1",
	"Hivep3",
	"Zfp558",
	"Zfp53",
	"Myt1l",
	"Bnc1",
	"Zfp498",
	"Elf5",
	"Pax8",
	"Srebf1",
	"Pparg",
	"Nr4a3",
	"Lef1",
	"Lmx1b",
	"Pou2f1",
	"Tshz2",
	"Hoxd3",
	"Zfp777",
	"Prdm8",
	"Zfp456",
	"Tox2",
	"Dmrt2",
	"Tlx2",
	"Prdm10",
	"Cic",
	"Tfe3",
	"Zbtb17",
	"Zbtb9",
	"Smarcc1",
	"Zfp712",
	"Bhlhe40",
	"Pou3f2",
	"Hsf5",
	"Ovol1",
	"Zfyve26",
	"Sall1",
	"Ar",
	"Gtf3a",
	"Smarce1",
	"Sp3",
	"Nfia",
	"Mafk",
	"Zfp276",
	"Zfp619",
	"Tfap2a",
	"Zfp688",
	"Kdm5c",
	"Tcf21",
	"Zfp458",
	"Znf512b",
	"Hoxa4",
	"Arid1b",
	"Zfp707",
	"Prdm6",
	"Maf1",
	"Nr1i2",
	"Zfp260",
	"Zbtb12",
	"Irx5",
	"Bptf",
	"Ssrp1",
	"Gli3",
	"Zfp518a",
	"Mllt6",
	"Foxc2",
	"Prdm12",
	"Ubtf",
	"Ppara",
	"Tbx18",
	"Tet3",
	"Sox13",
	"Creb3l3",
	"Prox1",
	"Zfp748",
	"Id3",
	"Dnmt3a",
	"Hey2",
	"Zbed6",
	"Zfp426",
	"Dnmt3l",
	"Hand2",
	"Otx2",
	"Hoxa13",
	"Gcm1",
	"Sp2",
	"Hoxd13",
	"Trps1",
	"Heyl",
	"Gm8008",
	"Brca1",
	"Zfp78",
	"Drap1",
	"Esrrb",
	"Gata4",
	"Prrx2",
	"Zc3h3",
	"Bcl6b",
	"Dnajc2",
	"Nr2e1",
	"Nr6a1",
	"Zfp41",
	"Zfp747",
	"Tfcp2l1",
	"Insm2",
	"Tbx20",
	"Dmrta2",
	"Cebpb",
	"Foxo6",
	"Lmx1a",
	"9130023H24Rik",
	"Tox4",
	"Meox2",
	"Pspc1",
	"Zfp941",
	"Zfp7",
	"Id2",
	"Zfp277",
	"Mafb",
	"Mxi1",
	"Zfp358",
	"Bcl6",
	"Maf",
	"Nr0b1",
	"Zfp422",
	"Zfp646",
	"Prdm5",
	"Dlx3",
	"Nfyc",
	"Hoxb5",
	"Zbed4",
	"Zfp467",
	"Aff4",
	"Tead4",
	"Tsc22d1",
	"Fubp1",
	"Zhx2",
	"Mlx",
	"Mafg",
	"Zscan21",
	"Gfi1",
	"Zfp846",
	"Zfp511",
	"Sp9",
	"Id4",
	"Zfp295",
	"Pgr",
	"Mbd3",
	"Gsx1",
	"Fosl1",
	"Sox17",
	"Mta3",
	"Gata2",
	"Twist1",
	"Cnot4",
	"Zfp57",
	"Tub",
	"Zfp192",
	"C130039O16Rik",
	"Smad7",
	"Irf9",
	"Zfp710",
	"Pax9",
	"Hnf4g",
	"Zmat2",
	"Zbtb16",
	"Zfp455",
	"Tfec",
	"Gata5",
	"Cdx2",
	"Tfap2b",
	"Tef",
	"Nfkb1",
	"Zfp593",
	"Zfp385c",
	"Zfp235",
	"Foxq1",
	"Cdx1",
	"St18",
	"Foxg1",
	"Purg",
	"Bnc2",
	"Hoxa9",
	"E2f3",
	"Smarcad1",
	"Zfp451",
	"Tfap4",
	"Elf4",
	"En2",
	"Pura",
	"Elf2",
	"Unkl",
	"Zfp428",
	"Pbx2",
	"Tcf12",
	"Zbtb5",
	"Zfhx2",
	"Hnf4a",
	"Arid3b",
	"Zkscan2",
	"Hes5",
	"Sohlh1",
	"Rc3h1",
	"Pou2f3",
	"Creb5",
	"Hif1a",
	"Sp7",
	"Zbtb43",
	"Plagl2",
	"Zfp799",
	"Six4",
	"Tcf7l1",
	"E2f5",
	"Hlx",
	"Pax6",
	"Lcor",
	"Stat5a",
	"Zfp408",
	"Zc3h10",
	"Fiz1",
	"Zfp445",
	"Mbd2",
	"Sim2",
	"Pbx4",
	"Plag1",
	"Gatad2a",
	"Sall3",
	"Camta2",
	"Ahctf1",
	"Toe1",
	"Zfp709",
	"Zscan12",
	"Foxe3",
	"Arid2",
	"Zscan2",
	"Olig1",
	"Pcbp4",
	"Zfp212",
	"Nfkbib",
	"Hoxa2",
	"Zfp553",
	"Irf3",
	"Tshz3",
	"Mxd3",
	"Tcf19",
	"Hoxb8",
	"Hoxd11",
	"Tfcp2",
	"Elf3",
	"Esr2",
	"Zc3h14",
	"Klf2",
	"Zc3h12b",
	"Nr5a2",
	"Zfp771",
	"Fli1",
	"Zfhx3",
	"Klf16",
	"Zfp2",
	"Mxd1",
	"Tfb2m",
	"Myf6",
	"Zfp36l1",
	"Rara",
	"Stat5b",
	"Neurod4",
	"Ikzf5",
	"Spz1",
	"Zfp90",
	"Ccdc79",
	"Sox3",
	"Zfp385a",
	"Zc3h18",
	"Zfp318",
	"Hoxd4",
	"Mecp2",
	"Smad4",
	"Foxd3",
	"Ncoa1",
	"Aff1",
	"Smarca4",
	"Arid5a",
	"Gli1",
	"Foxj3",
	"Zfp605",
	"Adnp",
	"Zfp512",
	"Sox7",
	"Tcf7l2",
	"Sox10",
	"Zfp958",
	"Zc3h7a",
	"Smad5",
	"Lhx5",
	"Mael",
	"Gatad1",
	"Mll1",
	"Nfe2",
	"Aff2",
	"Nfkbie",
	"Esr1",
	"Ahr",
	"Vezf1",
	"Zfp384",
	"Csrnp1",
	"Zfp236",
	"Pou3f1",
	"Hes2",
	"Lhx8",
	"Nr1d1",
	"Shox2",
	"Hoxa7",
	"Crebzf",
	"Gata3",
	"Zfp566",
	"Tbpl1",
	"Mbnl3",
	"Zbtb40",
	"Zfp839",
	"Bcl3",
	"Tox3",
	"Prdm9",
	"Hand1",
	"E2f2",
	"Zfp961",
	"Nkx3-1",
	"Crx",
	"Zfp62",
	"Esrra",
	"Rbpjl",
	"Foxp3",
	"Zbtb45",
	"Bhlhb9",
	"Zfx",
	"Tcfl5",
	"Pou4f2",
	"Jund",
	"Tbx5",
	"Zfp141",
	"Thap2",
	"Zfp575"
]
