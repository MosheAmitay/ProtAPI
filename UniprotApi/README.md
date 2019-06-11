# Prot API

## Uniprot

UniProt is a freely accessible database of protein sequence and functional information, many entries being derived from genome sequencing projects. It contains a large amount of information about the biological function of proteins derived from the research literature.  
https://en.wikipedia.org/wiki/UniProt.

Since this is a very large data base, access of information can be a burden especially when information of more than one accession number is wanted.

## Description
This is a class meant to help users retrieve specific data for 1 or more accession numbers.
This class is made up of 8 definitions:

1.	GeneName: finds gene name/s of given accession number/s.
2.	Title: finds title of accession number/s.
3.	ProteinName: finds the protein name/s of given accession number/s.
4.	Organism: finds name/s of organism/s of given accession number/s.
5.	ProteinSeq: finds the protein sequence/s of given accession number/s.
6.	Modified: finds modified genes in given accession number/s.
7.	Variations: finds variations for given accession number/s.
8.	PrintAll: prints all the data at once for all the accession numbers given.

## How To Use
1.	Create a youreName.py file
2.	Include the following import:
from UniprotApi import *
3.	Create a variable for the UniprotApi class:
youreName = UniprotApi()
4.	Use the variable to call one or all of the functions mentioned in the description:
youreName.GeneName()
youreName.Title()
youreName.ProteinName()
youreName.Organism()
youreName.ProteinSeq()
youreName.Modified()
youreName.Variations()
youreName.PrintAll()

## Code Examples:
Once you have youreName.py file created (mentioned in the 'how to use section')

1. To extract gene names:

youreName.py file will include:

from UniprotApi import *

VarName = UniprotApi()

VarName.GeneName()

you will run youreName.py in the linux window:

python youreName.py

Please Enter Accession Numbers (seperated by spaces): Q14533 Q3TTY5 P08069 Q60751 P69892

(the results you will get:)

Gene Name Of Q14533: KRT81

Gene Name Of Q3TTY5: Krt2

Gene Name of P08069: IGF1R

Gene Name of Q60751: Igf1r

Gene Name of P69892: HBG2

2. To extract protein names for all the accession numbers:

youreName.py will include:

from UniprotApi import *

VarName = UniprotApi()

VarName.ProteinName()

you will run youreName.py in the linux window:

python youreName.py

Please Enter Accession Numbers (seperated by spaces): Q14533 Q3TTY5 P08069 Q60751 P69892

(the results you will get:)

Protein Name Of Q14533: Keratin, type II cuticular Hb1

Protein Name Of Q3TTY5: Keratin, type II cytoskeletal 2 epidermal

Protein Name Of P08069: Insulin-like growth factor 1 receptor

Protein Name Of Q60751: Insulin-like growth factor 1 receptor

Protein Name Of P69892: Hemoglobin subunit gamma-2

3. To extract all the information for all of the accession numbers:

youreName.py will include:

from UniprotApi import *

VarName = UniprotApi()

VarName.PrintAll()

you will run youreName.py in the linux window:

python youreName.py

Please Enter Accession Numbers (seperated by spaces): Q14533 Q3TTY5 P08069 Q60751 P69892

(the results you will get:)

Information for accession number: Q14533

Gene Name: KRT81

Title: Characterization and chromosomal localization of human hair-specific keratin genes and comparative expression during the hair growth cycle.

Protein Name: Keratin, type II cuticular Hb1

Organism: Homo sapiens

Protein Sequence:
MTCGSGFGGRAFSCISACGPRPGRCCITAAPYRGISCYRGLTGGFGSHSVCGGFRAGSCG
RSFGYRSGGVCGPSPPCITTVSVNESLLTPLNLEIDPNAQCVKQEEKEQIKSLNSRFAAF
IDKVRFLEQQNKLLETKLQFYQNRECCQSNLEPLFEGYIETLRREAECVEADSGRLASEL
NHVQEVLEGYKKKYEEEVSLRATAENEFVALKKDVDCAYLRKSDLEANVEALIQEIDFLR
RLYEEEILILQSHISDTSVVVKLDNSRDLNMDCIIAEIKAQYDDIVTRSRAEAESWYRSK
CEEMKATVIRHGETLRRTKEEINELNRMIQRLTAEVENAKCQNSKLEAAVAQSEQQGEAA
LSDARCKLAELEGALQKAKQDMACLIREYQEVMNSKLGLDIEIATYRRLLEGEEQRLCEG
IGAVNVCVSSSRGGVVCGDLCVSGSRPVTGSVCSAPCNGNVAVSTGLCAPCGQLNTTCGG
GSCGVGSCGISSLGVGSCGSSCRKC

Modified Genes:


There are no modified genes

Variations:

{
    "Sequence Varient 1": "G Turns to Rat position: 52",
    "Sequence Varient 2": "L Turns to Rat position: 248",
    "Sequence Varient 3": "R Turns to Cat position: 316",
    "Sequence Varient 4": "E Turns to Kat position: 402",
    "Sequence Varient 5": "R Turns to Cat position: 408",
    "Sequence Varient 6": "E Turns to Kat position: 413"
}

Information for accession number: Q3TTY5

Gene Name: Krt2

Title: An unusual type-II 70-kilodalton keratin protein of mouse epidermis exhibiting postnatal body-site specificity and sensitivity to hyperproliferation.

Protein Name: Keratin, type II cytoskeletal 2 epidermal

Organism: Mus musculus

Protein Sequence:
MSCQISCRSRRGGGGGGGGGFRGFSSGSAVVSGGSRRSNTSFSCISRHGGGRGGSGGGGF
GSQSLVGLGGYKSISSSVAGNSGGYGGSSFGGSSGFGGGRGFGGGQGFGGSGGFGGGSGF
GGGQGFGGGSRFGGGSGFGGGGFGGGSFGGGRFGGGPGGFGGPGGFPGGGIHEVSVNQSL
LQPLDVKVDPEIQNVKSQEREQIKTLNNKFASFIDKVRFLEQQNQVLRTKWELLQQLDVG
SRTTNLDPIFQAYIGMLKKQVDRLSAERTSQESELNNMQDLVEDFKKKYEDEINKRTSAE
NDFVTIKKDVDSCYMDKTELQARLDILAQEVNFLRTLYDAELSQLQQDVTDTNVILSMDN
NRNLDLDSIIAEVQNQYEMIAHKSKAESEELYHSKYEELQVTAVKHGDSLKEIKMEISEL
NRTIQRLQGEISHVKKQCKGVQDSIADAEQRGEHAIKDARGKLTDLEEALQQCREDLARL
LRDYQELMNTKLSLDVEIATYRKLLEGEECRMSGDFSDNVSVSITSSTISSSVASKTGFG
SGGQSSGGRGSYGGRGGGGGGGSTYGSGGRSSGSRGSGSGSGGGGYSSGGGSRGGSGGGY
GSGGGSRGGSGGGYGSGGGSGSGGGYSSGGGSRGGSGGGGVSSGGGSRGGSSSGGGSRGG
SSSGGGGYSSGGGSRGGSSSGGAGSSSEKGGSGSGEGCGSGVTFSFR

Modified Genes:

{
    "Modification number 1": "Description= Asymmetric dimethylarginine",
    "Modification number 2": "Description= Phosphoserine",
    "Modification number 3": "Description= Phosphoserine",
    "Modification number 4": "Description= Omega-N-methylarginine",
    "Modification number 5": "Description= Phosphoserine",
    "Modification number 6": "Description= Omega-N-methylarginine",
    "Modification number 7": "Description= Omega-N-methylarginine",
    "Modification number 8": "Description= Omega-N-methylarginine",
    "Modification number 9": "Description= Omega-N-methylarginine"
}

Variations:

{
    "Sequence Varient 1": "T Turns to Pat position: 500"
}

Information for accession number: P08069

Gene Name: IGF1R

Title: Insulin-like growth factor I receptor primary structure: comparison with insulin receptor suggests structural determinants that define functional specificity.

Protein Name: Insulin-like growth factor 1 receptor

Organism: Homo sapiens

Protein Sequence:
MKSGSGGGSPTSLWGLLFLSAALSLWPTSGEICGPGIDIRNDYQQLKRLENCTVIEGYLH
ILLISKAEDYRSYRFPKLTVITEYLLLFRVAGLESLGDLFPNLTVIRGWKLFYNYALVIF
EMTNLKDIGLYNLRNITRGAIRIEKNADLCYLSTVDWSLILDAVSNNYIVGNKPPKECGD
LCPGTMEEKPMCEKTTINNEYNYRCWTTNRCQKMCPSTCGKRACTENNECCHPECLGSCS
APDNDTACVACRHYYYAGVCVPACPPNTYRFEGWRCVDRDFCANILSAESSDSEGFVIHD
GECMQECPSGFIRNGSQSMYCIPCEGPCPKVCEEEKKTKTIDSVTSAQMLQGCTIFKGNL
LINIRRGNNIASELENFMGLIEVVTGYVKIRHSHALVSLSFLKNLRLILGEEQLEGNYSF
YVLDNQNLQQLWDWDHRNLTIKAGKMYFAFNPKLCVSEIYRMEEVTGTKGRQSKGDINTR
NNGERASCESDVLHFTSTTTSKNRIIITWHRYRPPDYRDLISFTVYYKEAPFKNVTEYDG
QDACGSNSWNMVDVDLPPNKDVEPGILLHGLKPWTQYAVYVKAVTLTMVENDHIRGAKSE
ILYIRTNASVPSIPLDVLSASNSSSQLIVKWNPPSLPNGNLSYYIVRWQRQPQDGYLYRH
NYCSKDKIPIRKYADGTIDIEEVTENPKTEVCGGEKGPCCACPKTEAEKQAEKEEAEYRK
VFENFLHNSIFVPRPERKRRDVMQVANTTMSSRSRNTTAADTYNITDPEELETEYPFFES
RVDNKERTVISNLRPFTLYRIDIHSCNHEAEKLGCSASNFVFARTMPAEGADDIPGPVTW
EPRPENSIFLKWPEPENPNGLILMYEIKYGSQVEDQRECVSRQEYRKYGGAKLNRLNPGN
YTARIQATSLSGNGSWTDPVFFYVQAKTGYENFIHLIIALPVAVLLIVGGLVIMLYVFHR
KRNNSRLGNGVLYASVNPEYFSAADVYVPDEWEVAREKITMSRELGQGSFGMVYEGVAKG
VVKDEPETRVAIKTVNEAASMRERIEFLNEASVMKEFNCHHVVRLLGVVSQGQPTLVIME
LMTRGDLKSYLRSLRPEMENNPVLAPPSLSKMIQMAGEIADGMAYLNANKFVHRDLAARN
CMVAEDFTVKIGDFGMTRDIYETDYYRKGGKGLLPVRWMSPESLKDGVFTTYSDVWSFGV
VLWEIATLAEQPYQGLSNEQVLRFVMEGGLLDKPDNCPDMLFELMRMCWQYNPKMRPSFL
EIISSIKEEMEPGFREVSFYYSEENKLPEPEELDLEPENMESVPLDPSASSSSLPLPDRH
SGHKAENGPGPGVLVLRASFDERQPYAHMNGGRKNERALPLPQSSTC

Modified Genes:

{
    "Modification number 1": "Description= Phosphotyrosine",
    "Modification number 2": "Description= Phosphotyrosine; by autocatalysis",
    "Modification number 3": "Description= Phosphotyrosine; by autocatalysis",
    "Modification number 4": "Description= Phosphotyrosine; by autocatalysis",
    "Modification number 5": "Description= Phosphoserine; by GSK3-beta",
    "Modification number 6": "Description= Phosphoserine"
}

Variations:

{
    "Sequence Varient 1": "V Turns to Lat position: 105",
    "Sequence Varient 10": "R Turns to Qat position: 739",
    "Sequence Varient 11": "H Turns to Rat position: 808",
    "Sequence Varient 12": "A Turns to Tat position: 828",
    "Sequence Varient 13": "N Turns to Sat position: 857",
    "Sequence Varient 14": "Y Turns to Cat position: 865",
    "Sequence Varient 15": "R Turns to Sat position: 1256",
    "Sequence Varient 16": "R Turns to Cat position: 1337",
    "Sequence Varient 17": "A Turns to Tat position: 1338",
    "Sequence Varient 18": "A Turns to Vat position: 1347",
    "Sequence Varient 2": "R Turns to Qat position: 138",
    "Sequence Varient 3": "K Turns to Nat position: 145",
    "Sequence Varient 4": "N Turns to Yat position: 359",
    "Sequence Varient 5": "V Turns to Mat position: 388",
    "Sequence Varient 6": "R Turns to Hat position: 437",
    "Sequence Varient 7": "R Turns to Qat position: 511",
    "Sequence Varient 8": "R Turns to Hat position: 595",
    "Sequence Varient 9": "R Turns to Hat position: 605"
}

Information for accession number: Q60751

Gene Name: Igf1r

Title: Cloning of cDNA for the mouse insulin-like growth factor I receptor.

Protein Name: Insulin-like growth factor 1 receptor

Organism: Mus musculus

Protein Sequence:
MKSGSGGGSPTSLWGLVFLSAALSLWPTSGEICGPGIDIRNDYQQLKRLENCTVIEGFLH
ILLISKAEDYRSYRFPKLTVITEYLLLFRVAGLESLGDLFPNLTVIRGWKLFYNYALVIF
EMTNLKDIGLYNLRNITRGAIRIEKNADLCYLSTIDWSLILDAVSNNYIVGNKPPKECGD
LCPGTLEEKPMCEKTTINNEYNYRCWTTNRCQKMCPSVCGKRACTENNECCHPECLGSCH
TPDDNTTCVACRHYYYKGVCVPACPPGTYRFEGWRCVDRDFCANIPNAESSDSDGFVIHD
DECMQECPSGFIRNSTQSMYCIPCEGPCPKVCGDEEKKTKTIDSVTSAQMLQGCTILKGN
LLINIRRGNNIASELENFMGLIEVVTGYVKIRHSHALVSLSFLKNLRLILGEEQLEGNYS
FYVLDNQNLQQLWDWNHRNLTVRSGKMYFAFNPKLCVSEIYRMEEVTGTKGRQSKGDINT
RNNGERASCESDVLRFTSTTTWKNRIIITWHRYRPPDYRDLISFTVYYKEAPFKNVTEYD
GQDACGSNSWNMVDVDLPPNKEGEPGILLHGLKPWTQYAVYVKAVTLTMVENDHIRGAKS
EILYIRTNASVPSIPLDVLSASNSSSQLIVKWNPPTLPNGNLSYYIVRWQRQPQDGYLYR
HNYCSKDKIPIRKYADGTIDVEEVTENPKTEVCGGDKGPCCACPKTEAEKQAEKEEAEYR
KVFENFLHNSIFVPRPERRRRDVMQVANTTMSSRSRNTTVADTYNITDPEEFETEYPFFE
SRVDNKERTVISNLRPFTLYRIDIHSCNHEAEKLGCSASNFVFARTMPAEGADDIPGPVT
WEPRPENSIFLKWPEPENPNGLILMYEIKYGSQVEDQRECVSRQEYRKYGGAKLNRLNPG
NYTARIQATSLSGNGSWTDPVFFYVPAKTTYENFMHLIIALPVAILLIVGGLVIMLYVFH
RKRNNSRLGNGVLYASVNPEYFSAADVYVPDEWEVAREKITMNRELGQGSFGMVYEGVAK
GVVKDEPETRVAIKTVNEAASMRERIEFLNEASVMKEFNCHHVVRLLGVVSQGQPTLVIM
ELMTRGDLKSYLRSLRPEVEQNNLVLIPPSLSKMIQMAGEIADGMAYLNANKFVHRDLAA
RNCMVAEDFTVKIGDFGMTRDIYETDYYRKGGKGLLPVRWMSPESLKDGVFTTHSDVWSF
GVVLWEIATLAEQPYQGLSNEQVLRFVMEGGLLDKPDNCPDMLFELMRMCWQYNPKMRPS
FLEIIGSIKDEMEPSFQEVSFYYSEENKPPEPEELEMELEMEPENMESVPLDPSASSASL
PLPERHSGHKAENGPGPGVLVLRASFDERQPYAHMNGGRANERALPLPQSSTC

Modified Genes:

{
    "Modification number 1": "Description= Phosphotyrosine",
    "Modification number 2": "Description= Phosphotyrosine; by autocatalysis",
    "Modification number 3": "Description= Phosphotyrosine; by autocatalysis",
    "Modification number 4": "Description= Phosphotyrosine; by autocatalysis",
    "Modification number 5": "Description= Phosphoserine; by GSK3-beta",
    "Modification number 6": "Description= Phosphoserine"
}

Variations:

{}

Information for accession number: P69892

Gene Name: HBG2

Title: Human fetal G gamma- and A gamma-globin genes: complete nucleotide sequences suggest that DNA can be exchanged between these duplicated genes.

Protein Name: Hemoglobin subunit gamma-2

Organism: Homo sapiens

Protein Sequence:
MGHFTEEDKATITSLWGKVNVEDAGGETLGRLLVVYPWTQRFFDSFGNLSSASAIMGNPK
VKAHGKKVLTSLGDAIKHLDDLKGTFAQLSELHCDKLHVDPENFKLLGNVLVTVLAIHFG
KEFTPEVQASWQKMVTGVASALSSRYH

Modified Genes:

{
    "Modification number 1": "Description= N-acetylglycine; in form Hb F1",
    "Modification number 10": "Description= Phosphoserine",
    "Modification number 11": "Description= Phosphoserine",
    "Modification number 2": "Description= Phosphothreonine",
    "Modification number 3": "Description= Phosphoserine",
    "Modification number 4": "Description= Phosphoserine",
    "Modification number 5": "Description= Phosphoserine",
    "Modification number 6": "Description= N6-acetyllysine",
    "Modification number 7": "Description= N6-acetyllysine",
    "Modification number 8": "Description= S-nitrosocysteine",
    "Modification number 9": "Description= Phosphoserine"
}

Variations:

{
    "Sequence Varient 1": "G Turns to Cat position: 2",
    "Sequence Varient 10": "N Turns to Kat position: 20",
    "Sequence Varient 11": "V Turns to Aat position: 21",
    "Sequence Varient 12": "E Turns to Kat position: 22",
    "Sequence Varient 13": "E Turns to Qat position: 22",
    "Sequence Varient 14": "D Turns to Gat position: 23",
    "Sequence Varient 15": "D Turns to Vat position: 23",
    "Sequence Varient 16": "G Turns to Eat position: 26",
    "Sequence Varient 17": "E Turns to Kat position: 27",
    "Sequence Varient 18": "V Turns to Iat position: 35",
    "Sequence Varient 19": "T Turns to Pat position: 39",
    "Sequence Varient 2": "E Turns to Gat position: 6",
    "Sequence Varient 20": "R Turns to Gat position: 41",
    "Sequence Varient 21": "R Turns to Kat position: 41",
    "Sequence Varient 22": "F Turns to Sat position: 42",
    "Sequence Varient 23": "S Turns to Rat position: 45",
    "Sequence Varient 24": "M Turns to Rat position: 56",
    "Sequence Varient 25": "K Turns to Eat position: 60",
    "Sequence Varient 26": "K Turns to Qat position: 60",
    "Sequence Varient 27": "H Turns to Lat position: 64",
    "Sequence Varient 28": "H Turns to Yat position: 64",
    "Sequence Varient 29": "K Turns to Nat position: 66",
    "Sequence Varient 3": "D Turns to Nat position: 8",
    "Sequence Varient 30": "K Turns to Qat position: 67",
    "Sequence Varient 31": "K Turns to Rat position: 67",
    "Sequence Varient 32": "V Turns to Mat position: 68",
    "Sequence Varient 33": "G Turns to Rat position: 73",
    "Sequence Varient 34": "I Turns to Tat position: 76",
    "Sequence Varient 35": "I Turns to Vat position: 76",
    "Sequence Varient 36": "H Turns to Rat position: 78",
    "Sequence Varient 37": "D Turns to Nat position: 81",
    "Sequence Varient 38": "H Turns to Yat position: 93",
    "Sequence Varient 39": "D Turns to Nat position: 95",
    "Sequence Varient 4": "K Turns to Eat position: 9",
    "Sequence Varient 40": "E Turns to Kat position: 102",
    "Sequence Varient 41": "K Turns to Nat position: 105",
    "Sequence Varient 42": "L Turns to Hat position: 106",
    "Sequence Varient 43": "H Turns to Rat position: 118",
    "Sequence Varient 44": "F Turns to Lat position: 119",
    "Sequence Varient 45": "K Turns to Qat position: 121",
    "Sequence Varient 46": "E Turns to Kat position: 122",
    "Sequence Varient 47": "E Turns to Aat position: 126",
    "Sequence Varient 48": "W Turns to Gat position: 131",
    "Sequence Varient 49": "H Turns to Yat position: 147",
    "Sequence Varient 5": "K Turns to Qat position: 9",
    "Sequence Varient 6": "T Turns to Rat position: 13",
    "Sequence Varient 7": "W Turns to Rat position: 16",
    "Sequence Varient 8": "G Turns to Rat position: 17",
    "Sequence Varient 9": "K Turns to Nat position: 18"
}














