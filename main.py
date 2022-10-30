import os
from colorthief import ColorThief
from get_section import get_sections


def get_trigger(rule): # This hurts but custom rules gotta custom rule
    match rule:
        case "democratic" | "democracy":
            return "coa_def_democracy_flag_trigger"
        case "absolute_monarchy":
            return "coa_def_absolute_monarchy_flag_trigger"
        case "republic":
            return "coa_def_republic_flag_trigger"
        case "communism" | "communist" | "council_republic":
            return "coa_def_communist_flag_trigger"
        case "monarchy":
            return "coa_def_monarchy_flag_trigger"
        case "monarchy_democratic" | "democratic_monarchy":
            return "coa_def_democratic_monarchy_flag_trigger"
        case "dictatorship" | "dictorship": # typo, blame TBW
            return "coa_def_dictatorship_flag_trigger"
        case "socialist":
            return "coa_def_socialism_flag_trigger"
        case "fascist":
            return "coa_def_fascist_flag_trigger"
        case "council_republic_democratic":
            return "coa_def_council_republic_democratic_flag_trigger"
        case "socialist_dictatorship":
            return "coa_def_socialist_dictatorship_flag_trigger"
        case "LUC":
            return "coa_def_started_LUC_flag_trigger"
        case "PAP" | "theocracy" | 'Theocracy':
            return "coa_def_theocracy_flag_trigger"
        case "MOD":
            return "coa_def_started_MOD_flag_trigger"
        case "PAR":
            return "coa_def_started_PAR_flag_trigger"
        case "SIC":
            return "coa_def_started_SIC_flag_trigger"
        case "TUS":
            return "coa_def_started_TUS_flag_trigger"
        case "bavaria":
            return "coa_def_started_BAV_flag_trigger"
        case "hannover":
            return "coa_def_started_HAN_flag_trigger"
        case "austria":
            return "coa_def_started_AUS_flag_trigger"
        case "subject":
            return "coa_def_ensign_trigger"
        case "subject_britain" | "subject_GBR":
            return "coa_def_british_ensign_trigger"
        case "subject_spain":
            return "coa_def_spanish_ensign_trigger"
        case "subject_sweden":
            return "coa_def_swedish_ensign_trigger"
        case "subject_denmark":
            return "coa_def_danish_ensign_trigger"
        case "subject_ukraine":
            return "coa_def_ukrainian_ensign_trigger"
        case "subject_austria":
            return "coa_def_austrian_ensign_trigger"
        case "subject_notNET":
            return "coa_def_no_NET_overlord_flag_trigger"
        case "subject_bolivia":
            return "coa_def_bolivia_ensign_trigger"
        case "perubolivia_socialist":
            return "coa_def_peru_bolivia_socialist_flag_trigger"
        case "perubolivia_fascist":
            return "coa_def_peru_bolivia_fascist_flag_trigger"
        case "perubolivia_monarchy":
            return "coa_def_peru_bolivia_monarchy_flag_trigger"
        case "perubolivia_republic_democratic":
            return "coa_def_peru_bolivia_republic_democratic_flag_trigger"
        case "perubolivia_dictatorship":
            return "coa_def_peru_bolivia_dictatorship_flag_trigger"
        case "overlord_norway":
            return "coa_SWE_use_norway_canton_trigger"
        case "textime":
            return "coa_def_time_tex_flag_trigger"
        case "subject_FRA_GBR":
            return "coa_def_french_british_ensign_trigger"
        case "subject_USA":
            return "coa_def_american_ensign_trigger"
        case "independent":
            return "coa_def_independent_flag_trigger"
        case _:
            raise Exception("You are bad and should feel bad: " + rule)


def create_definition(TAG, rule):
    if rule is None:
        return "\tflag_definition = {\n\t\tcoa = " + TAG + "\n\t\tsubject_canton = " + TAG + "\n\t\tpriority = 100\n\t}"
    elif rule.startswith("subject"):
        if "GBR" in rule or "britain" in rule or "notNET" in rule: #only britain (and DEI) should have a canton because i say so
            return "\tflag_definition = {\n\t\tcoa = " + TAG + "_" + rule + "\n\t\tsubject_canton = " + TAG + "_" + rule + "\n\t\tallow_overlord_canton = yes\n\t\tpriority = 600\n\t\ttrigger = {\n\t\t\t" + get_trigger(rule) + " = yes\n\t\t}\n\t}"
        else:
            return "\tflag_definition = {\n\t\tcoa = " + TAG + "_" + rule + "\n\t\tsubject_canton = " + TAG + "_" + rule + "\n\t\tallow_overlord_canton = no\n\t\tpriority = 600\n\t\ttrigger = {\n\t\t\t" + get_trigger(rule) + " = yes\n\t\t}\n\t}"
    elif rule.startswith("perubolivia"): #make sure Peru-Bolivia overrules its other custom flags
        return "\tflag_definition = {\n\t\tcoa = " + TAG + "_" + rule + "\n\t\tsubject_canton = " + TAG + "_" + rule + "\n\t\tpriority = 550\n\t\ttrigger = {\n\t\t\t" + get_trigger(rule) + " = yes\n\t\t}\n\t}"
    else:
        return "\tflag_definition = {\n\t\tcoa = " + TAG + "_" + rule + "\n\t\tsubject_canton = " + TAG + "_" + rule + "\n\t\tpriority = 500\n\t\ttrigger = {\n\t\t\t" + get_trigger(rule) + " = yes\n\t\t}\n\t}"


mod_path = r"C:\Users\marti\OneDrive\Documenten\Paradox Interactive\Victoria 3\mod\Better Flags Mod!"
flag_path = os.path.join(mod_path, r"gfx\coat_of_arms\textured_emblems")
game_path = r"C:\Program Files (x86)\Steam\steamapps\common\Victoria 3\game"

coa_file = open(os.path.join(mod_path, r"common\coat_of_arms\coat_of_arms\04_MoreFlags.txt"), 'w', encoding='utf-8-sig')
def_file = open(os.path.join(mod_path, r"common\flag_definitions\02_flag_definitions.txt"), 'w', encoding='utf-8-sig')

sections = get_sections(r"C:\Program Files (x86)\Steam\steamapps\common\Victoria 3\game\common\flag_definitions\00_flag_definitions.txt")

# TAG : [def1, (coa, rule))]
TAGS = {}

for file in os.listdir(flag_path):
    filename = os.path.join(flag_path, file)
    if "charge" in filename:
        continue

    color_thief = ColorThief(filename)
    rgb = color_thief.get_color(quality=1)

    COA = file.split(".")[0]
    print(COA)

    if "_" in COA:
        entry = (COA.split("_")[0], "_".join(COA.split("_")[1:]))
    else:
        entry = (COA, None)

    TAG, _ = entry

    if TAG in TAGS:
        coa = TAGS[TAG]
        coa.append(entry)
        TAGS[TAG] = coa
    else:
        TAGS[TAG] = [entry]

    template_coa = COA + " = {\n\tpattern = \"pattern_solid.tga\"\n\tcolor1 = rgb {" + " ".join([str(v) for v in rgb]) + "}\n\t\n\ttextured_emblem = {\n\t\ttexture = \"" + file + "\"\n\t\tinstance = { scale = { 1 1 } position = { 0.5 0.5 } }\n\t}\n}\n\n"

    coa_file.write(template_coa)


def_file.write("# common variables\n@coa_width = 768\n@coa_height = 512\n@canton_scale_cross_x = @[ ( 333 / coa_width ) + 0.001 ]\n@canton_scale_cross_y = @[ ( 205 / coa_height ) + 0.001 ]\n@canton_scale_sweden_x = @[ ( 255 / coa_width ) + 0.001 ]\n@canton_scale_sweden_y = @[ ( 204 / coa_height ) + 0.001 ]\n@canton_scale_norway_x = @[ ( 192 / coa_width ) + 0.001 ]\n@canton_scale_norway_y = @[ ( 192 / coa_height ) + 0.001 ]\n@canton_scale_denmark_x = @[ ( 220 / coa_width ) + 0.001 ]\n@canton_scale_denmark_y = @[ ( 220 / coa_height ) + 0.001 ]\n@third = @[1/3]\n")

for TAG, rules in TAGS.items():

    definitions = [create_definition(tag, rule) for tag, rule in rules]

    if TAG in sections:
        template_def = sections[TAG]
        template_def[-1] = "\n".join(definitions)
        template_def.append('}')
        template_def = "\n".join(template_def) + "\n\n"
    else:
        template_def = TAG + " = {\n" + "\n".join(definitions) + "\n}\n\n"

    def_file.write(template_def)


coa_file.close()
def_file.close()
