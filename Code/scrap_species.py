#   Scrap : https://www.mushroom.world/mushrooms/namelist

# Path to save the data
path = 'C:/Users/mbrei/OneDrive/Bureau/M2/ChampIA/Data/mushroom_data.csv'

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

species = ["Agaricus-arvensis", "Agaricus-augustus", "Agaricus-campestris", "Agaricus-sylvicola",
    "Agrocybe-pediades", "Agrocybe-praecox", "Albatrellus-confluens", "Albatrellus-ovinus",
    "Aleuria-aurantia", "Amanita-battarrae", "Amanita-bisporigera", "Amanita-cokeri",
    "Amanita-fulva", "Amanita-jacksonii", "Amanita-muscaria", "Amanita-pantherina",
    "Amanita-phalloides", "Amanita-porphyria", "Amanita-regalis", "Amanita-rubescens",
    "Amanita-submembranacea", "Amanita-vaginata", "Amanita-virosa", "Ampulloclitocybe-clavipes",
    "Armillaria-borealis", "Armillaria-gallica", "Armillaria-mellea", "Auriscalpium-vulgare",
    "Bankera-fuligineoalba", "Boletus-edulis", "Boletus-pinophilus", "Bondarzewia-berkeleyi",
    "Bovista-nigrescens", "Bovista-plumbea", "Calocera-viscosa", "Calocybe-gambosa",
    "Calocybe-persicolor", "Calvatia-gigantea", "Candolleomyces-candolleanus", "Cantharellula-umbonata",
    "Cantharellus-cibarius", "Cantharellus-cinnabarinus", "Chalciporus-piperatus", "Chlorophyllum-molybdites",
    "Chlorophyllum-rhacodes", "Chroogomphus-britannicus", "Clathrus-ruber", "Clitocybe-fragrans",
    "Clitocybe-gibba", "Clitocybe-metachroa", "Clitocybe-nebularis", "Clitocybe-nuda", "Clitopilus-prunulus",
    "Coltricia-perennis", "Conocybe-apala", "Coprinellus-disseminatus", "Coprinellus-xanthothrix",
    "Coprinopsis-atramentaria", "Coprinopsis-variegata", "Coprinus-comatus", "Coprinus-plicatilis",
    "Cortinarius-alboviolaceus", "Cortinarius-armillatus", "Cortinarius-camphoratus", "Cortinarius-caperatus",
    "Cortinarius-collinitus", "Cortinarius-croceus", "Cortinarius-flexipes", "Cortinarius-laniger",
    "Cortinarius-malicorius", "Cortinarius-mucosus", "Cortinarius-orellanus", "Cortinarius-rubellus",
    "Cortinarius-semisanguineus", "Cortinarius-talus", "Cortinarius-traganus", "Cortinarius-violaceus",
    "Craterellus-tubaeformis", "Cystoderma-amianthinum", "Cystodermella-cinnabarina", "Entoloma-sericeum",
    "Entoloma-vernum", "Galerina-marginata", "Galerina-pumila", "Geastrum-rufescens", "Gomphidius-glutinosus",
    "Gymnopilus-penetrans", "Gymnopilus-picreus", "Gymnopus-dryophilus", "Gymnopus-peronatus",
    "Gyromitra-esculenta", "Gyromitra-infula", "Hebeloma-crustuliniforme", "Hebeloma-mesophaeum",
    "Helvella-elastica", "Helvella-lacunosa", "Hericium-americanum", "Hericium-cirrhatum", "Hericium-erinaceus",
    "Hortiboletus-rubellus", "Hydnellum-scabrosum", "Hydnum-repandum", "Hydnum-rufescens", "Hygrophoropsis-aurantiaca",
    "Hygrophorus-camarophyllus", "Hygrophorus-hypothejus", "Hygrophorus-olivaceoalbus", "Hygrophorus-pustulatus",
    "Hypholoma-capnoides", "Hypholoma-fasciculare", "Hypholoma-lateritium", "Hypholoma-marginatum", "Imleria-badia",
    "Inocybe-geophylla", "Inocybe-lacera", "Kuehneromyces-lignicola", "Kuehneromyces-mutabilis", "Laccaria-laccata",
    "Lacrymaria-lacrymabunda", "Lactarius-camphoratus", "Lactarius-deliciosus", "Lactarius-deterrimus", "Lactarius-helvus",
    "Lactarius-indigo", "Lactarius-lignyotus", "Lactarius-mammosus", "Lactarius-musteus", "Lactarius-rufus",
    "Lactarius-tabidus", "Lactarius-torminosus", "Lactarius-trivialis", "Lactarius-turpis", "Lactarius-utilis",
    "Lactarius-volemus", "Lactifluus-piperatus", "Laetiporus-sulphureus", "Leccinum-aurantiacum", "Leccinum-scabrum",
    "Leccinum-versipelle", "Lepiota-clypeolaria", "Leratiomyces-magnivelaris", "Leucocoprinus-birnbaumii",
    "Leucocybe-connata", "Lycoperdon-excipuliforme", "Lycoperdon-nigrescens", "Lycoperdon-perlatum",
    "Lycoperdon-pratense", "Lycoperdon-pyriforme", "Macrolepiota-procera", "Marasmiellus-perforans",
    "Marasmius-oreades", "Marasmius-rotula", "Megacollybia-platyphylla", "Melanoleuca-cognata", "Morchella-elata",
    "Morchella-esculenta", "Mycena-epipterygia", "Mycena-galericulata", "Mycena-laevigata", "Mycena-metata",
    "Mycena-pura", "Mycena-urania", "Neolentinus-lepideus", "Omphalotus-illudens", "Omphalotus-olearius",
    "Otidea-onotica", "Panaeolus-foenisecii", "Paxillus-involutus", "Peziza-badia", "Peziza-repanda",
    "Phallus-impudicus", "Phallus-rubicundus", "Pholiota-alnicola", "Pholiota-aurivella", "Pholiota-lenta",
    "Pholiota-limonella", "Pholiota-squarrosa", "Phyllotopsis-nidulans", "Pleurotus-citrinopileatus",
    "Pleurotus-ostreatus", "Pleurotus-pulmonarius", "Pluteus-cervinus", "Pluteus-pellitus", "Polyporus-ciliatus",
    "Polyporus-squamosus", "Psathyrella-microrrhiza", "Pseudohydnum-gelatinosum", "Psilocybe-semilanceata",
    "Ramaria-lutea", "Ramaria-pallida", "Rhizina-undulata", "Rickenella-swartzii", "Rubroboletus-satanas",
    "Russula-acrifolia", "Russula-adusta", "Russula-aeruginea", "Russula-claroflava", "Russula-clavipes",
    "Russula-decolorans", "Russula-emetica", "Russula-mustelina", "Russula-paludosa", "Russula-velenovskyi",
    "Russula-vesca", "Russula-vinosa", "Russula-xerampelina", "Sarcodon-squamosus", "Strobilomyces-strobilaceus",
    "Strobilurus-esculentus", "Strobilurus-stephanocystis", "Stropharia-aeruginosa", "Stropharia-hornemannii",
    "Stropharia-rugosoannulata", "Suillus-americanus", "Suillus-bovinus", "Suillus-grevillei", "Suillus-luteus",
    "Suillus-variegatus", "Tapinella-atrotomentosa", "Tapinella-panuoides", "Tricholoma-aestuans", "Tricholoma-arvernense",
    "Tricholoma-equestre", "Tricholoma-focale", "Tricholoma-fulvum", "Tricholoma-inamoenum", "Tricholoma-saponaceum",
    "Tricholoma-sejunctum", "Tricholoma-stiparophyllum", "Tricholoma-virgatum", "Tricholomopsis-decora",
    "Tricholomopsis-rutilans", "Turbinellus-floccosus", "Tylopilus-felleus", "Xerocomellus-chrysenteron",
    "Xerocomus-subtomentosus", "Xeromphalina-campanella"
]

site = 'https://www.mushroom.world/show?n='
urls = [site + specie for specie in species]

def scrape_mushroom_page(url):
    try:
        # is the url working ?
        response = requests.get(url, timeout=2)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error URL {url} : {e}")
        return {'url': url, 'scientific_name': np.nan, 'common_name': np.nan, 'family': np.nan,
                'location': np.nan, 'dimension': np.nan, 'edibility': np.nan,
                'description': np.nan, 'image': np.nan}

    soup = BeautifulSoup(response.text, 'html.parser')

    try:
        # name
        name_section = soup.find('div', class_='mush-caption')
        scientific_name = name_section.b.text.strip() if name_section and name_section.b else np.nan
        common_name = name_section.find('span', class_='mush-commonname').text.strip("()") if name_section and name_section.find('span', class_='mush-commonname') else np.nan
    except (AttributeError, KeyError):
        scientific_name, common_name = np.nan, np.nan

    # family, location
    info_dict = {}
    try:
        for div in soup.find_all('div', class_='mush-info'):
            label = div.find('div', class_='mush-labelus').text.strip()
            value = div.find('div', class_='mush-textus').text.strip()
            info_dict[label] = value
    except AttributeError:
        pass

    # Description
    try:
        description = soup.find('div', class_='mush-longtextus').text.strip()
    except AttributeError:
        description = np.nan

    # Images
    try:
        image_links = [img['href'] for img in soup.select('.mush-image a')]
        image_paths = ", ".join(image_links) if image_links else np.nan
    except AttributeError:
        image_paths = np.nan

    return {
        'url': url,
        'scientific_name': scientific_name,
        'common_name': common_name,
        'family': info_dict.get('Family', np.nan),
        'location': info_dict.get('Location', np.nan),
        'dimension': info_dict.get('Dimensions', np.nan),
        'edibility': info_dict.get('Edibility', np.nan),
        'description': description,
        'image': image_paths
    }
    
data = pd.DataFrame([scrape_mushroom_page(url) for url in urls])

data.to_csv(path, index=False)