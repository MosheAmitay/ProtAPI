# YNpdb
A Python Rest_API for the RCSB Protein Data Bank

YNpdb includs two functions:
1. search_pdb()- askes for pdb ids and columns(records) of interest 
                 and prints the information about them arranged.
2. print_all()- askes for pdb ids and columns(records) of interest 
                and prints the full records as a dictionary.
## Install
For using my library you must install the libraries: requests, xmltodict, urllib2, json, os
## Examples
1.
Enter the ids that you are interested in (separated by commas): 6R9M
Enter the columns that you are interested in (separated by commas):
 choose them from this link - https://www.rcsb.org/pdb/results/reportField.do: ligandName,sequence

{
    "6R9M: ligandName in chain A": "null",
    "6R9M: ligandName in chain B": "null",
    "6R9M: sequence in chain A": "MHHHHHHHHLEVLFQGPTSDIQTYTSINKYEVPPAYSRLPLTSGRFGTDNFDFTPFNNTEYSGLDPDVDNHYTNAIIQLYRFIPEMFNFVVGCLKDENFETTLLTDLGYLFDMMERSHGKICSSSNFQASLKSLTDKRQLENGEPQEHLEEYLESLCIRESIEDFNSSESIKRNMPQKFNRFLLSQLIKEEAQTVNHNITLNQCFGLETEIRTECSCDHYDTTVKLLPSLSISGINKTVIKQLNKKSNGQNILPYIEYAMKNVTQKNSICPTCGKTETITQECTVKNLPSVLSLELSLLDTEFSNIRSSKNWLTSEFYGSIIKNKAVLRSTASELKGTSHIFKYELNGYVAKITDNNNETRLVTYVKKYNPKENCFKWLMFNDYLVVEITEEEALKMTYPWKTPEIIIYCDAEELRKPFFSVDTYSINYDILFRDYFANGIRDTARREYKLLTHDEAPKSGTLVAIDAAFVSLQSELCEIDHQGIRSIIRPKRTALARISIIRGEEGELYGVPFVDDYVVNTNHIEDYLTRYSGILPGDLDPEKSTKRLVRRNVVYRKVWLLMQLGCVFVGHGLNNDFKHININVPRNQIRDTAIYFLQGKRYLSLRYLAYVLLGMNIQEGNHDSIEDAHTALILYKKYLHLKEKAIFEKVLNSVYEEGRAHNFKVPETSKG",
    "6R9M: sequence in chain B": "AAGGAA"
}


the results are also saved in output.txt

2.
