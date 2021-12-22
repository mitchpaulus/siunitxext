#!/usr/bin/python3
import json

# read units.json file
with open('units.json', encoding='utf-8') as json_file:
    data = json.load(json_file)

def to_tex_file(file_name, spacing_option):
    first_group = True
    with open(file_name, 'w', encoding='utf-8') as f:
        for group in data["groups"]:
            if not first_group:
                f.write("\n")
            f.write(f"% {group['name']}\n")
            first_definition = True
            for definition in group["definitions"]:
                if not first_definition:
                    f.write("\n")
                for name in definition["names"]:
                    tex = definition["tex"]
                    if "spacing" in definition and definition["spacing"] == False:
                        f.write(f"\\DeclareSIUnit[{spacing_option}]\\{name}{{{tex}}}\n")
                    else:
                        f.write(f"\\DeclareSIUnit\\{name}{{{tex}}}\n")
                first_definition = False
            first_group = False


def to_markdown_table():
    with open('table.md', 'w', encoding='utf-8') as f:
        f.write(" Unit Macro | Tex Output \n")
        f.write("----|----\n")

        for group in data["groups"]:
            for definition in group["definitions"]:
                names = ', '.join([ '\\' + n for n in definition["names"] ])

                # Write names comma separated
                f.write(f"{names} | {definition['tex']} \n")


to_tex_file("siunitx-local-units-v2.tex", "number-unit-product={}")
to_tex_file("siunitx-local-units-v3.tex", "quantity-product={}")
to_markdown_table()
