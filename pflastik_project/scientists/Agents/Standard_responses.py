# you should see some thing like this 
Anonymous_response = """{
        "identification_report": {
            "disease_name": "Fire Blight",
            "plant_name": "Apple (Malus domestica)",
            "description": "Fire blight is a contagious disease caused by the bacterium Erwinia amylovora. It affects apple and pear trees, as well as other members of the family Rosaceae.",
            "diagnosis": "The disease is diagnosed by observing characteristic symptoms such as the browning and blackening of leaves, which appear scorched, and the oozing of bacterial exudate from infected plant parts. Laboratory tests can confirm the presence of Erwinia amylovora.",
            "symptoms": [
                "Browning and blackening of leaves",
                "Leaves appear scorched",
                "Water-soaked lesions on stems",
                "Oozing of bacterial exudate",
                "Blossoms turn brown and wilt",
                "Twigs and branches die back"
            ],
            "management_tips": [
                "Prune out infected branches during dormant season",
                "Disinfect pruning tools between cuts",
                "Avoid excessive nitrogen fertilization",
                "Apply appropriate bactericides or antibiotics",
                "Plant resistant varieties if available",
                "Ensure proper spacing for air circulation"
            ],
            "notes": "Fire blight can spread rapidly in warm, wet conditions. Monitoring and early intervention are crucial for managing the disease."
        }
    }
"""
Farmer_response = """
    {
  "PlantDiseaseAnalysis": {
    "DiseaseName": {
      "ScientificName": "Venturia inaequalis",
      "CommonName": "Apple Scab"
    },
    "AffectedPlant": "Apple (Malus domestica)",
    "Description": "Apple Scab is a fungal disease caused by Venturia inaequalis. It primarily affects apple trees, causing dark, scabby lesions on leaves, fruit, and sometimes young shoots.",
    "DiagnosisMethod": {
      "Step1": "Visual Inspection: Look for dark, olive-green to black, velvety spots on the leaves and fruits.",
      "Step2": "Microscopic Examination: Confirm the presence of fungal spores using a microscope.",
      "Step3": "Lab Testing: In some cases, laboratory analysis may be necessary to confirm the fungal species."
    },
    "Symptoms": {
      "Leaves": "Olive-green to black spots that enlarge and merge, leading to yellowing and premature leaf drop.",
      "Fruits": "Similar dark lesions on the surface, which can cause deformation and cracking.",
      "Shoots": "Young shoots may exhibit dark lesions and stunted growth."
    },
    "ManagementTips": {
      "CulturalPractices": "Remove and destroy fallen leaves and infected fruit. Prune trees to improve air circulation.",
      "ChemicalTreatments": "Apply fungicides such as captan, myclobutanil, or sulfur during the growing season, especially after wet conditions.",
      "OrganicSolutions": "Use neem oil or potassium bicarbonate sprays as organic alternatives."
    },
    "PreventionStrategies": {
      "CropRotation": "Avoid planting apple trees in areas where apple scab was previously a problem.",
      "ResistantVarieties": "Choose scab-resistant apple varieties.",
      "SanitationPractices": "Maintain cleanliness in the orchard by removing debris and fallen leaves regularly."
    },
    "AdditionalNotes": "Apple scab is more prevalent in regions with cool, wet springs. The disease can significantly impact yield if not managed properly."
  },
  "SoilAndFieldConditions": {
    "SoilType": "Loamy soil (typical for apple orchards, though not visible in the image)",
    "SoilHealth": "No direct signs of soil health issues in the image, but leaf symptoms indicate possible fungal infection",
    "MoistureLevels": "The presence of fungal disease suggests periods of high moisture or poor drainage conditions.",
    "SoilpH": "Apple trees prefer slightly acidic to neutral soil pH (around 6.0-7.0). No direct indication from the image.",
    "NutrientStatus": "No visible signs of nutrient deficiencies such as chlorosis or stunting in the image.",
    "FieldConditions": "No visible signs of erosion or significant compaction. However, fungal infections suggest the need for better air circulation and moisture management.",
    "RecommendationsForImprovement": {
      "SoilAmendments": "Add organic matter to improve soil structure and drainage.",
      "IrrigationPractices": "Ensure proper irrigation practices to avoid waterlogging and maintain optimal soil moisture.",
      "FieldManagementTechniques": "Implement regular pruning, sanitation, and monitoring for early signs of disease."
    }
  },
  "ReferenceImage": "/mnt/data/Crop-Diseases-The-Nightmare-of-Every-Farmer-.jpeg"
  }
    """
Scientist_response = """
            {
        "PlantDiseaseAnalysis": {
            "DiseaseName": {
            "ScientificName": "Venturia inaequalis",
            "CommonName": "Apple Scab"
            },
            "AffectedPlant": {
            "Species": "Malus domestica",
            "CommonName": "Apple"
            },
            "PathogenInformation": {
            "PathogenType": "Fungal",
            "ScientificClassification": {
                "Kingdom": "Fungi",
                "Phylum": "Ascomycota",
                "Class": "Dothideomycetes",
                "Order": "Venturiales",
                "Family": "Venturiaceae",
                "Genus": "Venturia",
                "Species": "V. inaequalis"
            },
            "LifeCycle": "The pathogen overwinters in fallen leaves and infects new leaves in the spring. It produces ascospores and conidia that spread via wind and rain."
            },
            "Description": {
            "Etiology": "Venturia inaequalis causes scab lesions primarily on leaves, fruit, and occasionally on young twigs.",
            "Epidemiology": "Disease development is favored by wet, cool conditions in the spring. Spores germinate and infect plant tissues, leading to the characteristic scab lesions."
            },
            "DiagnosisMethod": {
            "VisualInspection": "Identify dark, velvety lesions on leaves and fruit.",
            "LaboratoryTests": "PCR to detect fungal DNA, microscopic examination of spores.",
            "RequiredEquipment": "Microscope, PCR machine, DNA extraction kits."
            },
            "Symptoms": {
            "MorphologicalIndicators": "Olive-green to black, velvety spots on leaves, which can lead to leaf curling and deformation.",
            "PhysiologicalIndicators": "Reduced photosynthesis, premature leaf drop.",
            "MolecularIndicators": "Presence of specific fungal DNA markers detectable by PCR."
            },
            "ManagementStrategies": {
            "IntegratedPestManagement": "Regular monitoring, use of resistant varieties, proper sanitation (removal of fallen leaves).",
            "ChemicalTreatments": "Fungicides such as captan, mancozeb, or myclobutanil applied according to a schedule.",
            "BiologicalControls": "Introduction of beneficial fungi or bacteria that inhibit Venturia inaequalis.",
            "GeneticResistance": "Cultivation of apple varieties that are genetically resistant to apple scab."
            },
            "PreventionStrategies": {
            "CulturalPractices": "Prune trees to improve air circulation, remove and destroy fallen leaves.",
            "ResistantCultivars": "Planting scab-resistant apple varieties such as 'Liberty' or 'Enterprise'.",
            "BiosecurityMeasures": "Regular inspection and quarantine of new plant materials."
            },
            "AdditionalNotes": {
            "EnvironmentalConditions": "High humidity and cool temperatures promote disease spread.",
            "ImpactOnYield": "Severe infections can lead to significant yield loss and reduced fruit quality."
            }
        },
        "PlantInformation": {
            "PlantBiology": {
            "GrowthStages": "Seed germination, vegetative growth, flowering, fruiting, senescence.",
            "PhysiologicalProcesses": "Photosynthesis, respiration, transpiration, nutrient uptake.",
            "GeneticInformation": "Apple genome contains genes for disease resistance, including those coding for resistance proteins against fungal pathogens."
            },
            "ChemicalComposition": {
            "KeyMetabolites": "Sugars, organic acids, phenolic compounds.",
            "Nutrients": "Vitamins (e.g., vitamin C), minerals (e.g., potassium, calcium).",
            "PotentialToxins": "Cyanogenic glycosides in seeds (e.g., amygdalin)."
            },
            "Proteins": {
            "Functions": "Enzymes for metabolic processes, structural proteins, resistance proteins.",
            "RelevanceToPlantHealth": "Pathogenesis-related proteins (PR proteins) are crucial for defense against pathogens."
            },
            "GeneticMarkers": {
            "DiseaseResistanceMarkers": "Markers for resistance genes such as Vf (scab resistance gene).",
            "SusceptibilityMarkers": "Markers for genes that may increase susceptibility to scab."
            }
        },
        "SoilAndFieldConditions": {
            "SoilType": {
            "Description": "Based on the image, likely a well-drained loamy soil which is typical for apple orchards."
            },
            "SoilHealthIndicators": {
            "ErosionSigns": "Not visually evident from the image.",
            "Compaction": "Not visually evident, but soil testing can confirm.",
            "OrganicMatterContent": "Requires soil testing; recommended to maintain high organic matter for healthy apple trees.",
            "MicrobialActivity": "High microbial activity is crucial for nutrient cycling; soil testing can measure microbial biomass."
            },
            "MoistureLevels": {
            "Assessment": "Soil should be kept consistently moist but not waterlogged. Moisture sensors can be used for accurate measurement.",
            "MeasurementTechniques": "Tensiometers, moisture probes, and regular soil moisture checks."
            },
            "SoilpH": {
            "Estimation": "Optimal pH for apple trees is 6.0-6.5. Soil testing is necessary for accurate measurement.",
            "ImpactOnPlantHealth": "Incorrect pH can affect nutrient availability and disease susceptibility."
            },
            "NutrientStatus": {
            "Observations": "Leaf discoloration might indicate nutrient deficiencies or toxicities. Soil and tissue tests are recommended.",
            "RecommendedTests": "Soil tests for macronutrients (N, P, K) and micronutrients (Fe, Mn, Zn, etc.)."
            },
            "FieldConditions": {
            "DrainagePatterns": "Good drainage is crucial; avoid waterlogged conditions.",
            "Topography": "Slightly sloped fields are ideal for drainage.",
            "PestInfestations": "Regular scouting for pests like codling moth and aphids.",
            "WeedGrowth": "Maintain a weed-free zone around trees to reduce competition for nutrients."
            },
            "ChemicalAnalysis": {
            "PresenceOfChemicals": "Test for residual pesticides and pollutants to avoid phytotoxicity.",
            "Concentration": "Regular soil testing to monitor and manage chemical levels."
            },
            "RecommendationsForImprovement": {
            "SoilAmendments": "Incorporate organic matter such as compost to improve soil structure and fertility.",
            "IrrigationPractices": "Use drip irrigation to maintain optimal moisture levels.",
            "CoverCropping": "Use cover crops to improve soil health and reduce erosion.",
            "FieldManagementTechniques": "Regular soil testing, proper pruning, and pest management practices."
            },
            "ResearchInsights": {
            "RecentStudies": "Recent studies highlight the effectiveness of integrated pest management and the use of biocontrol agents in managing apple scab.",
            "InnovativeSolutions": "CRISPR-Cas9 technology for developing resistant apple varieties, advanced soil health monitoring tools."
            }
        }
        }
    """