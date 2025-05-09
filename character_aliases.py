import pickle
from pathlib import Path

UNCLE_TOM_CABIN_CHARACTER_ALIASES = {
    # 1. Uncle Tom
    "Uncle Tom": [
        "Uncle Tom",
        "Tom",
        "UNCLE TOM",    # All-caps variant
        "Uncle Tom’s"   # Possessive form
    ],

    # 2. Aunt Chloe
    "Aunt Chloe": [
        "Aunt Chloe",
        "Chloe",
        # Variants that appear with punctuation/line breaks:
        "Aunt\nChloe", 
        "Aunt Chloe,—“I"
    ],

    # 3. Eliza Harris
    "Eliza Harris": [
        "Eliza Harris",
        "Eliza",
        "Mrs. Harris",
        # Common dialect/spelling variants:
        "Liza",
        "Lizzy",
        "Lizy",
        # The text sometimes shows her name with punctuation/line breaks:
        "Eliza\n",             
        "Eliza trembled",      
        "Eliza glided\nforward",
        "Eliza tremulously",  
        # You may want to strip punctuation/line breaks depending on your approach
    ],

    # 4. George Harris
    "George Harris": [
        "George Harris",
        "George",
        "Mr. Harris",
        # Occasionally split across lines in the text:
        "George\nHarris"
    ],

    # 5. Evangeline "Eva" St. Clare
    "Evangeline \"Eva\" St. Clare": [
        "Eva",
        "Little Eva",
        "Miss Eva",
        "Evangeline St. Clare",
        "Evangeline \"Eva\" St. Clare",
        "Eva."  # sometimes appears with punctuation
    ],

    # 6. Augustine St. Clare
    "Augustine St. Clare": [
        "Augustine",
        "Mr. St. Clare",
        "Master St. Clare",
        "Augustine St. Clare",
        # Variants/punctuation from text:
        "St. Clare",
        "Augustine St.\nClare",
        "Augustine St."
    ],

    # 7. Marie St. Clare
    "Marie St. Clare": [
        "Marie",
        "Mrs. St. Clare",
        "Marie St. Clare",
        "Miss\nMarie",       # appears with a line break
        "Marie St. Clare’s"  # possessive form
    ],

    # 8. Miss Ophelia (Ophelia St. Clare)
    "Miss Ophelia": [
        "Miss Ophelia",
        "Ophelia",
        "Cousin Ophelia",
        # Sometimes referred to with last name or line breaks:
        "Ophelia St. Clare",
        "Miss\nOphelia",
        # Topsy’s nickname for her:
        "Feely",
        "Feeley",
        "Phelia"
    ],

    # 9. Topsy
    "Topsy": [
        "Topsy"
        # No major variants found for Topsy in the extracted text
    ],

    # 10. Simon Legree
    "Simon Legree": [
        "Simon Legree",
        "Legree",
        "Master Legree",
        "Simon"
    ],

    # 11. Cassy
    "Cassy": [
        "Cassy",
        "Cass"
    ],

    # 12. Emmeline
    "Emmeline": [
        "Emmeline"
        # Sometimes with punctuation: "Emmeline."
    ],

    # 13. George Shelby
    "George Shelby": [
        "George Shelby",
        "Mas’r George",
        "Master George",
        "Georgey"  # Dialect form in text
    ],

    # 14. Mr. Shelby (Arthur Shelby)
    "Mr. Shelby": [
        "Mr. Shelby",
        "Arthur Shelby",
        "Arthur",
        "Shelby"  # sometimes just last name in the text
    ],

    # 15. Mrs. Shelby (Emily Shelby)
    "Mrs. Shelby": [
        "Mrs. Shelby",
        "Emily Shelby",
        "Emily"
    ],

    # 16. Sam
    "Sam": [
        "Sam",
        "Black Sam"  # frequently called “Black Sam” in dialect passages
    ],

    # 17. Quimbo
    "Quimbo": [
        "Quimbo"
        # no additional variants found in extracted list
    ],

    # 18. Phineas Fletcher
    "Phineas Fletcher": [
        "Phineas Fletcher",
        "Phineas"
    ],

    # 19. Tom Loker
    "Tom Loker": [
        "Tom Loker",
        "Loker"
    ],

    # 20. Mr. Haley
    "Mr. Haley": [
        "Mr. Haley",
        "Haley",
        "Dan Haley"  # occasionally appears as “Dan Haley” in some editions/contexts
    ]
}

UNCLE_TOM_CABIN_MINOR_CHARACTER_ALIASES = {
    # Eliza’s young son:
    "Harry Harris": [
        "Harry",
        "Little Harry",
        "Harry Harris"
    ],

    # Frequently just “Andy” in the Shelby household:
    "Andy": [
        "Andy"
    ],

    # Other slaves or servants on the Shelby plantation:
    "Black Jake": [
        "Jake",
        "Black Jake"
    ],
    "Mose": [
        "Mose"
    ],
    "Pete": [
        "Pete"
    ],
    "Polly": [
        "Polly"
    ],
    "Jinny": [
        "Jinny"
    ],
    "Aunt Sally": [
        "Sally",
        "Aunt Sally"
    ],
    
    # Occasional references:
    "Tom Lincon": [
        "Tom Lincon"
    ],

    # Another servant name that pops up occasionally:
    "Mandy": [
        "Mandy"
    ],

    # The Birds (Senator Bird & Mrs. Bird), who help Eliza:
    "Senator Bird": [
        "Mr. Bird",
        "Senator Bird",
        "John Bird",
        "Bird"
    ],
    "Mrs. Bird": [
        "Mrs. Bird",
        "Mary Bird",
        "Mary"
    ],
    
    # House servants at the Bird home:
    "Cudjoe": [
        "Cudjoe",
        "Uncle Cudjoe"
    ],
    "Aunt Dinah": [
        "Aunt Dinah",
        "Dinah"
    ],

    # Minor characters associated with Quaker settlement:
    "Rachel Halliday": [
        "Rachel Halliday",
        "Rachel"
    ],
    "Simeon Halliday": [
        "Simeon Halliday",
        "Simeon"
    ],
    "Ruth Stedman": [
        "Ruth Stedman",
        "Ruth"
    ],

    # Another Quaker or friend in the novel:
    "John Van Trompe": [
        "John Van Trompe"
        # occasionally just "John," but there are MANY “John” references, so be cautious
    ],

    # Another escaping slave or contact:
    "Lucy": [
        "Lucy"
    ],

    # On Legree’s plantation:
    "Sambo": [
        "Sambo"
    ],
    # We already had Quimbo in top 20.

    # Servants in St. Clare’s household:
    "Adolph": [
        "Adolph",
        "Dolph"
    ],
    "Mammy": [
        "Mammy"
    ],
    # Some editions also mention "Mammy" by an actual name, but in text she’s usually just “Mammy.”

    # Alfred St. Clare (Augustine’s brother):
    "Alfred St. Clare": [
        "Alfred St. Clare",
        "Alfred",
        "Uncle Alfred"
    ],
    # His son, cousin to Eva:
    "Henrique St. Clare": [
        "Henrique",
        "Cousin Henrique"
    ],

    # Prue, the enslaved woman in New Orleans (meets tragic end):
    "Prue": [
        "Prue"
    ],

    # Another enslaved woman purchased by Legree alongside Emmeline:
    "Susan": [
        "Susan",
        "Susan."
    ],

    # Madame de Thoux (George Harris’s sister in some later chapters):
    "Madame de Thoux": [
        "Madame de Thoux",
        "De Thoux"
    ],

    # Old Bruno is the Shelby family’s dog, occasionally mentioned by name:
    "Bruno": [
        "Bruno",
        "Old Bruno"
    ]
}

# Add minor characters to character aliases
UNCLE_TOM_CABIN_CHARACTER_ALIASES.update(UNCLE_TOM_CABIN_MINOR_CHARACTER_ALIASES)



AUNT_PHILLIS_CABIN_CHARACTER_ALIASES = {
    # 1. Aunt Phillis
    "Aunt Phillis": [
        "Aunt Phillis",
        "Phillis",
        "Phillis b'lieve",
        "AUNT PHILLIS'S"      # All-caps / possessive title
    ],

    # 2. Uncle Bacchus
    "Uncle Bacchus": [
        "Uncle Bacchus",
        "Bacchus",
        "Uncle Bacchus's"     # Possessive
    ],

    # 3. Mr. Weston
    "Mr. Weston": [
        "Mr. Weston",
        "Weston",             # Surname only
        "Cousin Weston"       # Northern speakers’ form
    ],

    # 4. Alice Weston
    "Alice Weston": [
        "Alice Weston",
        "Alice",              # First name only
        "Miss Alice",
        "Miss Weston"
    ],

    # 5. Arthur Weston
    "Arthur Weston": [
        "Arthur Weston",
        "Arthur"
    ],

    # 6. Cousin Janet (a.k.a. Miss Janet)
    "Cousin Janet": [
        "Cousin Janet",
        "Miss Janet",
        "Janet",
        "Cousin Janet's",     # Possessive
        "JANET"               # All-caps
    ],

    # 7. Aunt Peggy
    "Aunt Peggy": [
        "Aunt Peggy",
        "Peggy",
        "Aunt Peggy's",
        "Peggy al'ars"
    ],

    # 8. Aunt Polly
    "Aunt Polly": [
        "Aunt Polly",
        "Polly",
        "Aunt Polly's"
    ],

    # 9. Uncle Toby
    "Uncle Toby": [
        "Uncle Toby",
        "UNCLE TOBY"
    ],

    # 10. Uncle Geoffrey
    "Uncle Geoffrey": [
        "Uncle Geoffrey"
    ],

    # 11. Uncle Jack
    "Uncle Jack": [
        "Uncle Jack"
    ],

    # 12. Abel Johnson
    "Abel Johnson": [
        "Abel Johnson",
        "Abel"
    ],

    # 13. Captain William Moore
    "Captain William Moore": [
        "Captain William Moore",
        "Captain Moore",
        "Captain Moore's",
        "Captain",            # Generic title—context-dependent
        "Moore"
    ],

    # 14. Walter Lee
    "Walter Lee": [
        "Walter Lee",
        "Walter Lee's",
        "Walter"
    ],

    # 15. Mr. Barbour
    "Mr. Barbour": [
        "Mr. Barbour",
        "Barbour"
    ],

    # 16. Mr. Kent
    "Mr. Kent": [
        "Mr. Kent",
        "Kent"
    ],

    # 17. Mr. Chapman
    "Mr. Chapman": [
        "Mr. Chapman",
        "Chapman"
    ],

    # 18. Mark (slave boy on Weston place)
    "Mark": [
        "Mark"
    ],

    # 19. John (slave on Weston place)
    "John": [
        "John",
        "Johns"               # Plural form occasionally used
    ],

    # 20. Nancy (slave on Weston place)
    "Nancy": [
        "Nancy"
    ],

    # 21. Moses (overseer/slave)
    "Moses": [
        "Moses"
    ],

    # 22. Aunt Lucy
    "Aunt Lucy": [
        "Aunt Lucy",
        "Lucy"
    ],

    # 23. Susan (maid to the Moores)
    "Susan": [
        "Susan"
    ]
}


TWELVE_YEARS_SLAVE_CHARACTER_ALIASES = {
    # 1. Solomon Northup (narrator; enslaved name “Platt”)
    "Solomon Northup": [
        "Solomon Northup",
        "Solomon",
        "Northup",
        "Platt",
        "Solomon Northup Staunton",
        "Platt Epps",
        "did'nt Platt",
        "Solomon Northup’s"
    ],

    # "Platt": [
    #     "Platt",
    #     "Platt Epps",
    #     "did'nt Platt",
    # ],

    # 2. Anne Northup (wife)
    "Anne Northup": [
        "Anne Northup",
        "Ann Northup",
        "Anne",
        "Anne Hampton",
        "Anne Hampton Northup",
        "Anne."
    ],

    # 3. Elizabeth Northup (daughter)
    "Elizabeth Northup": [
        "Elizabeth",
        "ELIZABETH",
        "Elizabeth Northup"
    ],

    # 4. Margaret Northup (daughter)
    "Margaret Northup": [
        "Margaret"
    ],

    # 5. Alonzo Northup (son)
    "Alonzo Northup": [
        "Alonzo",
        "Alonzo Northup"
    ],

    # 6. William Ford (first owner)
    "William Ford": [
        "William Ford",
        "Ford",
        "Ford's",
        "William Ford's",
        "Master Ford",
        "Franklin Ford"   # contextual variant in the list
    ],

    # 7. John M. Tibeats (carpenter)
    "John M. Tibeats": [
        "John M. Tibeats",
        "JOHN M. TIBEATS",
        "Tibeats"
    ],

    # 8. Edwin Epps (second owner)
    "Edwin Epps": [
        "Edwin Epps",
        "Epps",
        "Edwin",
        "Master Epps",
        "Massa Epps",
        "Epps.",
        "Master Epps!",
        "Epps farewell",
        "Epps'"
    ],

    # 9. Mistress Epps (Mary/Thérezine Epps)
    "Mistress Epps": [
        "Mistress Epps"
    ],

    # 10. Patsey
    "Patsey": [
        "Patsey",
        "Pats"
    ],

    # 11. Eliza (enslaved mother sold with her children)
    "Eliza": [
        "Eliza",
        "d. Eliza",
        "Eliza heard Freeman"
    ],

    # 12. Randall (Eliza’s son)
    "Randall": [
        "Randall"
    ],

    # 13. Emily (Eliza’s daughter)
    "Emily": [
        "Emily"
    ],

    # 14. Samuel Bass (Canadian carpenter who aids Solomon)
    "Samuel Bass": [
        "Bass"
    ],

    # 15. Armsby (overseer who betrays Solomon’s letter attempt)
    "Armsby": [
        "Armsby"
    ],

    # 16. Chapin (Ford’s just overseer)
    "Chapin": [
        "Chapin"
    ],

    # 17. Ebenezer Radburn (Washington jailer)
    "Ebenezer Radburn": [
        "Ebenezer Radburn",
        "Radburn"
    ],

    # 18. James H. Burch (slave dealer)
    "James H. Burch": [
        "James H. Burch",
        "JAMES H. BURCH",
        "Burch",
        "--James H. Burch",
        "BURCH ARRESTED--"
    ],

    # 19. Theophilus Freeman (New-Orleans broker)
    "Theophilus Freeman": [
        "Theophilus Freeman",
        "Theophilus",
        "--Theophilus Freeman",
        "Freeman"
    ],

    # 20. Henry B. Northup (cousin & rescuer)
    "Henry B. Northup": [
        "Henry B. Northup",
        "H. B. Northup",
        "B. NORTHUP"
    ],

    # 21. John P. Waddill (Louisiana attorney)
    "John P. Waddill": [
        "John P. Waddill",
        "JOHN P. WADDILL",
        "Waddill",
        "  P. Waddill"
    ],

    # 22. David Wilson (editor/ghost-writer)
    "David Wilson": [
        "David Wilson",
        "DAVID WILSON"
    ],

    # 23. Joseph B. Roberts (friend in Saratoga)
    "Joseph B. Roberts": [
        "Joseph B. Roberts",
        "JOSEPH B. ROBERTS",
        "B. Roberts"
    ],

    # 24. Uncle Abram (elder field hand)
    "Uncle Abram": [
        "Uncle Abram",
        "UNCLE ABRAM",
        "Abram",
        "Uncle Abram's"
    ],

    # 25. Abram Hamilton (kidnapper)
    "Abram Hamilton": [
        "Abram Hamilton",
        "HAMILTON"
    ],

    # 26. Peter Tanner (planter who shelters Solomon during rescue)
    "Peter Tanner": [
        "Peter Tanner",
        "Peter Tanner's",
        "Tanner"
    ],

    # 27. Lew Cheney (driver who betrays runaways)
    "Lew Cheney": [
        "Lew Cheney",
        "Cheney",
        "--Lew Cheney",
        "David Cheney"
    ],

    # 28. Timothy Eddy (New-York magistrate)
    "Timothy Eddy": [
        "Timothy Eddy",
        "TIMOTHY EDDY"
    ],

    # 29. Clemens Ray (free Black man seized with Solomon)
    "Clemens Ray": [
        "Clemens Ray",
        "Clem Ray",
        "Clem"
    ],

    # 30. Elisha Berry (slave owner in the New-Orleans pen)
    "Elisha Berry": [
        "Elisha Berry",
        "Berry"
    ]
}


# If main file, save to results directory
if __name__ == "__main__":

    # Define root directory
    root_dir = Path(__file__).parent

    results_dir = Path(root_dir) / "results"
    character_aliases_dir = results_dir / "character_aliases"

    character_aliases_dir.mkdir(parents=True, exist_ok=True)

    pickle.dump(UNCLE_TOM_CABIN_CHARACTER_ALIASES, open(character_aliases_dir / "uncle_toms_cabin.pkl", "wb"))
    pickle.dump(AUNT_PHILLIS_CABIN_CHARACTER_ALIASES, open(character_aliases_dir / "aunt_phillis_cabin.pkl", "wb"))
    pickle.dump(TWELVE_YEARS_SLAVE_CHARACTER_ALIASES, open(character_aliases_dir / "twelve_years_slave.pkl", "wb"))