# BioMarkQA2

## Overview
BioMarkQA2 is a scientific literature query tool built on top of PaperQA2. It specializes in retrieving biomarker-related information from academic papers.

## Installation
```bash
git clone https://github.com/your-repo/BioMarkQA2.git
cd BioMarkQA2
pip install -r requirements.txt

```
BioMarkQA2
├─ .DS_Store
├─ LICENSE
├─ README.md
├─ __init__.py
├─ biomarkqa2_model
│  ├─ __init__.py
│  ├─ config.py
│  ├─ data_processing.py
│  ├─ interface.py
│  └─ retrieval.py
├─ config.py
├─ data
│  ├─ .DS_Store
│  ├─ exported_tables.csv
│  └─ papers
│     ├─ .DS_Store
│     ├─ 10.1002@mabi.201800407.pdf
│     ├─ 10.1021@acsnano.0c08430.pdf
│     ├─ 10.1177_1535370216647123.pdf
│     ├─ 10.1177_1535370217719222.pdf
│     ├─ 10867_2013_Article_9314.pdf
│     ├─ 12195_2015_Article_388.pdf
│     ├─ 262_2024_Article_3636.pdf
│     ├─ 41578_2021_Article_399.pdf
│     ├─ 42003_2024_Article_6982.pdf
│     ├─ 978-1-0716-3222-2.pdf
│     ├─ 978-1-4939-7808-3.pdf
│     ├─ 978-3-540-69379-6.pdf
│     ├─ ADHM-11-2200163.pdf
│     ├─ ADVS-11-2308237.pdf
│     ├─ ADVS-5-1700991.pdf
│     ├─ ADVS-6-1802281.pdf
│     ├─ ADVS-8-2101796.pdf
│     ├─ Advanced Materials - 2024 - He - Peptide‐Driven Proton Sponge Nano‐Assembly for Imaging and Triggering Lysosome‐Regulated.pdf
│     ├─ BTM2-9-e10693.pdf
│     ├─ IEDD_0_1922387.pdf
│     ├─ IMM-159-183.pdf
│     ├─ JVI.00129-19.pdf
│     ├─ RA-011-D1RA03166J.pdf
│     ├─ Small - 2009 - Steinmetz - Virus‐Templated Silica Nanoparticles.pdf
│     ├─ ao2c05539.pdf
│     ├─ ao8b00227.pdf
│     ├─ cancers-11-00515.pdf
│     ├─ cancers-13-00627.pdf
│     ├─ cancers-13-02909.pdf
│     ├─ cells-12-02241.pdf
│     ├─ cells-13-01478.pdf
│     ├─ chariou2021.pdf
│     ├─ chung-et-al-2020-covid-19-vaccine-frontrunners-and-their-nanotechnology-design.pdf
│     ├─ d3ma00820g.pdf
│     ├─ eScholarship UC item 0cw4z8hz.pdf
│     ├─ eScholarship UC item 20j8t23n.pdf
│     ├─ fmicb-14-1117494.pdf
│     ├─ fonc-10-594614.pdf
│     ├─ franke2017.pdf
│     ├─ ijms-22-09733.pdf
│     ├─ ijms-24-14034.pdf
│     ├─ jitc-2021-004044.pdf
│     ├─ jitc-2022-005834.pdf
│     ├─ lam2017.pdf
│     ├─ lu-et-al-2018-new-directions-for-drug-delivery-in-cancer-therapy.pdf
│     ├─ main.pdf
│     ├─ nihms-1018974.pdf
│     ├─ nihms-1023880.pdf
│     ├─ nihms-1023887.pdf
│     ├─ nihms-1028555.pdf
│     ├─ nihms-1039289.pdf
│     ├─ nihms-1066839.pdf
│     ├─ nihms-1066972.pdf
│     ├─ nihms-1066974.pdf
│     ├─ nihms-1066975.pdf
│     ├─ nihms-1066978.pdf
│     ├─ nihms-1066981.pdf
│     ├─ nihms-1593977.pdf
│     ├─ nihms-1593989.pdf
│     ├─ nihms-1621210.pdf
│     ├─ nihms-1632071.pdf
│     ├─ nihms-1658883.pdf
│     ├─ nihms-1669605.pdf
│     ├─ nihms-1679614.pdf
│     ├─ nihms-1679739.pdf
│     ├─ nihms-1684434.pdf
│     ├─ nihms-1693116.pdf
│     ├─ nihms-1693120.pdf
│     ├─ nihms-1693130.pdf
│     ├─ nihms-1693176.pdf
│     ├─ nihms-1693190.pdf
│     ├─ nihms-1693191.pdf
│     ├─ nihms-1693193.pdf
│     ├─ nihms-1693247.pdf
│     ├─ nihms-1693250.pdf
│     ├─ nihms-1693252.pdf
│     ├─ nihms-1746556.pdf
│     ├─ nihms-1746662.pdf
│     ├─ nihms-1764798.pdf
│     ├─ nihms-1778227.pdf
│     ├─ nihms-1814940.pdf
│     ├─ nihms-1817095.pdf
│     ├─ nihms-1825298.pdf
│     ├─ nihms-1837790.pdf
│     ├─ nihms-1846484.pdf
│     ├─ nihms-1846486.pdf
│     ├─ nihms-1847836.pdf
│     ├─ nihms-1847839.pdf
│     ├─ nihms-1847846.pdf
│     ├─ nihms-1848149.pdf
│     ├─ nihms-1851535.pdf
│     ├─ nihms-1852501.pdf
│     ├─ nihms-1860381.pdf
│     ├─ nihms-1860384.pdf
│     ├─ nihms-1860385.pdf
│     ├─ nihms-1860386.pdf
│     ├─ nihms-1860387.pdf
│     ├─ nihms-1860388.pdf
│     ├─ nihms-1862762.pdf
│     ├─ nihms-1882735.pdf
│     ├─ nihms-1888235.pdf
│     ├─ nihms-1915476.pdf
│     ├─ nihms-1927871.pdf
│     ├─ nihms-1929071.pdf
│     ├─ nihms-1929076.pdf
│     ├─ nihms-1929079.pdf
│     ├─ nihms-1929080.pdf
│     ├─ nihms-1958247.pdf
│     ├─ nihms-2004569.pdf
│     ├─ nihms-2004570.pdf
│     ├─ nihms-2040021.pdf
│     ├─ nihms-2040496.pdf
│     ├─ nihms-2040497.pdf
│     ├─ nihms-2040498.pdf
│     ├─ nihms-226040.pdf
│     ├─ nihms-397065.pdf
│     ├─ nihms-421065.pdf
│     ├─ nihms-546179.pdf
│     ├─ nihms-703879.pdf
│     ├─ nihms-780278.pdf
│     ├─ nihms-780393.pdf
│     ├─ nihms-785326.pdf
│     ├─ nihms-986373.pdf
│     ├─ nihms-986533.pdf
│     ├─ nihms-987847.pdf
│     ├─ nihms-995452.pdf
│     ├─ nihms-995454.pdf
│     ├─ nihms-995958.pdf
│     ├─ nihms159006.pdf
│     ├─ nihms159007.pdf
│     ├─ nihms269325.pdf
│     ├─ nihms297244.pdf
│     ├─ nihms297480.pdf
│     ├─ nihms315518.pdf
│     ├─ nihms315521.pdf
│     ├─ nihms315522.pdf
│     ├─ nihms392359.pdf
│     ├─ nihms437598.pdf
│     ├─ nihms472440.pdf
│     ├─ nihms626551.pdf
│     ├─ nihms677905.pdf
│     ├─ nihms696211.pdf
│     ├─ nihms738066.pdf
│     ├─ nihms739980.pdf
│     ├─ nihms765684.pdf
│     ├─ nihms766064.pdf
│     ├─ nihms766315.pdf
│     ├─ nihms833077.pdf
│     ├─ nihms833923.pdf
│     ├─ nihms833930.pdf
│     ├─ nihms833941.pdf
│     ├─ nihms833972.pdf
│     ├─ nihms833976.pdf
│     ├─ nihms834145.pdf
│     ├─ nihms834146.pdf
│     ├─ nihms834271.pdf
│     ├─ nihms834299.pdf
│     ├─ nihms845028.pdf
│     ├─ nihms848682.pdf
│     ├─ nihms864355.pdf
│     ├─ nihms895714.pdf
│     ├─ nihms900799.pdf
│     ├─ nihms900811.pdf
│     ├─ nihms921493.pdf
│     ├─ nihms926552.pdf
│     ├─ nihms954033.pdf
│     ├─ nihms959931.pdf
│     ├─ pnas.202221859.pdf
│     ├─ pt3c00285.pdf
│     ├─ qt5004v69h.pdf
│     ├─ s41565-020-0737-y.pdf
│     ├─ s41565-024-01667-5.pdf
│     ├─ steinmetz-2013-viral-nanoparticles-in-drug-delivery-and-imaging.pdf
│     ├─ uhde-holzem2015.pdf
│     └─ zhou-et-al-2023-molecularly-stimuli-responsive-self-assembled-peptide-nanoparticles-for-targeted-imaging-and-therapy (1).pdf
├─ data_processing.py
├─ generation.py
├─ interface.py
├─ logo_dark.png
├─ logo_light.png
├─ requirements.txt
├─ retrieval.py
├─ scripts
│  └─ run_biomarkqa2.py
├─ streamlit_app
│  └─ app.py
└─ tests
   ├─ test_data_processing.py
   ├─ test_generation.py
   ├─ test_interface.py
   └─ test_retrieval.py

```