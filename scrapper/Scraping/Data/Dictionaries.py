SECTION_1 = {"PRODUCT_NAME": ["Product name", "Additional identification"],
             "Chemical_name": ["Chemical name:", "Chemical formula:"],
             "Chemical_formula": ["Chemical formula:", "INDEX No."],
             "INDEX_No": ["INDEX No.", "CAS-No."],
             "CAS_No": ["CAS-No.", "EC No."],
             "EC_No": ["EC No.", "REACH Registration No."],
             "REACH_Registration_No": ["REACH Registration No.",
                                       "1.2 Relevant identified uses of the substance or mixture and uses advised against"],
             "Identified_uses": ["Identified uses:", "Uses advised against:"],
             "Uses_advised_against": ["Uses advised against:", "1.3 Details of the supplier of the safety data sheet"],
             "Company Name": ["Company Name", "1.4 Emergency telephone number:"],
             "24-Hour Health Emergency": ["24-Hour Health Emergency", "SECTION 2. Hazard(s) identification"]
             }
SECTION_2 = {"2.1 Classification of the substance or mixture":["2.1 Classification of the substance or mixture",
                                                               "Classification according to Regulation <l.bracket>EC<r.bracket> No 1272/2008 as amended."],
    "Health Hazards":["Health Hazards","2.2 Label Elements"],
    "Signal Words:":["Signal Words:","Hazard Statement<l.bracket>s<r.bracket>:"],
    "Hazard Statement(s):":["Hazard Statement<l.bracket>s<r.bracket>","Supplemental label information"],
    "Supplemental label information":["Supplemental label information","Precautionary Statements"],
    "Prevention:":["Prevention:","Response:"],
    "Response:":["Response","Disposal:"],
    "Disposal:":["Disposal:","2.3 Other hazards"],
    "2.3 Other hazards":["2.3 Other hazards","SECTION 3: Composition/information on ingredients"],
}
SECTIONS = {"SECTION 1: Identification of the substance/mixture and of the company/undertaking": ["SECTION", "1", ":",
                                                                                                  "Identification",
                                                                                                  "of",
                                                                                                  "the",
                                                                                                  "substance/mixture",
                                                                                                  "and", "of", "the",
                                                                                                  "company/undertaking"],
            "SECTION 2: Hazards identification": ["SECTION", "2", ":", "Hazards", "identification"],
            "SECTION 3: Composition/information on ingredients": ["SECTION", "3", ":", "Composition/information", "on",
                                                                  "ingredients"],
            "SECTION 4: First aid measures": ["SECTION", "4", ":", "First", "aid", "measures"],
            "SECTION 5:Firefighting measures": ["SECTION", "5", ":", "Firefighting", "measures"],
            "SECTION 6: Handling and storage": ["SECTION", "6", ":", "Handling", "and", "storage"],
            "SECTION 7: Exposure controls/personal protection": ["SECTION", "7%", ":",
                                                                 "Exposure", "controls/personal", "protection"],
            "SECTION 8: Exposure controls": ["SECTION", "8", ":", "Exposure", "controls"],
            "SECTION 9: Physical and chemical properties": ["SECTION", "9", ":",
                                                            "Physical", "and", "chemical", "properties"],
            "SECTION 10: Stability and reactivity": ["SECTION", "10", ":", "Stability", "and", "reactivity"],
            "SECTION 11: Toxicological information": ["SECTION", "11", ":", "Toxicological", "information"],
            "SECTION 12: Ecological information": ["SECTION", "12", ":", "Ecological", "information"],
            "SECTION 13: Disposal considerations": ["SECTION", "13", ":", "Disposal", "considerations"],
            "SECTION 14: Transport information": ["SECTION", "14", ":", "Transport", "information"],
            "SECTION 15: Regulatory information": ["SECTION", "15", ":", "Regulatory", "information"],
            "SECTION 16: Other information": ["SECTION", "16", ":", "Other", "information"]}
SECTION_KEY = ['SECTION 1: Identification of the substance/mixture and of the company/undertaking', 'SECTION 2: '
                                                                                                    'Hazards '
                                                                                                    'identification',
               'SECTION 3: Composition/information on ingredients', "SECTION 4: First aid measures",
               'SECTION 5: Firefighting measures', 'SECTION 6: Accidental release measures', 'SECTION 7: Handling and storage',
               'SECTION 8: Exposure controls', 'SECTION 9: Physical and chemical properties', 'SECTION 10: Stability '
                                                                                              'and reactivity',
               'SECTION 11: Toxicological information', 'SECTION 12: Ecological information', 'SECTION 13: Disposal '
                                                                                              'considerations',
               'SECTION 14: Transport information', 'SECTION 15: Regulatory information', 'SECTION 16: Other '
                                                                                          'information']

Section_two = {}
Prodlist_of_bold_item = ["Product identifier", "Chemical name", "Other means of identification",
                         "Recommended restrictions", "Recommended use", "Manufacturer/Importer/Distributor Information",
                         "Emergency telephone number", "24 - Hour Health"]
list_of_bold_item1 = ["Product identifier", "Chemical name", "Other means of identification",
                      "Recommended restrictions",
                      "Recommended restrictions", "Manufacturer/Importer/Distributor Information",
                      "Emergency telephone number"]
Puct_identifier = {"Product identifier": "Product identifier"}
Chemical_name = {"Chemical name": "Chemical name"}
Other_means_of_identification = {"Other means of identification": ["CAS Number"]}
Recommended_restrictions = {"Recommended restrictions": ["Recommended use", "Restrictions on use"]}
Manufacturer_Importer_Distributor_Information = {
    "Manufacturer/Importer/Distributor Information": ["Company Name", "Telephone", "Fax", "E-mail"]}
Emergency_telephone_number = {"Emergency telephone number": ["24-Hour Health", "Emergency"]}

# Product Identifier
Identification = {
    "Product_identifier": ["Product", "identifier"],

    "Chemical_name": ["Chemical", "name"],

    "Other_means_of_identification": ["Other", "means", "of", "identification"],
    "CAS_Number": ["CAS", "Number"],

    "Recommended_restrictions": ["Recommended", "restrictions"],
    "Recommended_use": ["Recommended", "use"],
    "Restrictions_on_use": ["Restrictions", "on", "use"],

    "Manufacturer_Importer_Distributor_Information": ["Manufacturer/Importer/Distributor", "Information"],
    "Company_Name": ["Company", "Name"],
    "Telephone": ["Telephone"],
    "Fax": ["Fax"],
    "E_mail": ["E-mail"],

    "Emergency_telephone_number": ["Emergency", "telephone", "number"],
    "Hour_Health": ["24", "-", "Hour", "Health"],
    "Emergency": ["Emergency"]
}


