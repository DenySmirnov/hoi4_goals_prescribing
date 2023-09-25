def modify_goals_gfx(icon_name):
    # Write icon name
    IconName = icon_name

    # Open file goals.gfx
    with open('goals.gfx', 'r') as goals_file:
        data = goals_file.read()

    # Find last '}' and delete it
    data = data.rsplit('}', 1)[0]

    # Write new goal
    data += f'''
    SpriteType = {{ 
        name = "GFX_{IconName}"
        texturefile = "gfx/interface/goals/{IconName}.dds"
    }}
    }}
    '''

    # Save
    with open('goals.gfx', 'w') as goals_file:
        goals_file.write(data)

def modify_goals_shine_gfx(icon_name):
    # Open file goals_shine.gfx
    with open('goals_shine.gfx', 'r') as goals_shine_file:
        data = goals_shine_file.read()

    # Find last '}' and delete it
    data = data.rsplit('}', 1)[0]

    # Write new goal
    data += f'''
    SpriteType = {{
        name = "GFX_{icon_name}_shine"
        texturefile = "gfx/interface/goals/{icon_name}.dds"
        effectFile = "gfx/FX/buttonstate.lua"
        animation = {{
            animationmaskfile = "gfx/interface/goals/{icon_name}.dds"
            animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
            animationrotation = -90.0
            animationlooping = no
            animationtime = 0.75
            animationdelay = 0
            animationblendmode = "add"
            animationtype = "scrolling"
            animationrotationoffset = {{ x = 0.0 y = 0.0 }}
            animationtexturescale = {{ x = 2.0 y = 1.0 }} 
        }}
        animation = {{
            animationmaskfile = "gfx/interface/goals/{icon_name}.dds"
            animationtexturefile = "gfx/interface/goals/shine_overlay.dds"
            animationrotation = 90.0
            animationlooping = no
            animationtime = 0.75
            animationdelay = 0
            animationblendmode = "add"
            animationtype = "scrolling" 
            animationrotationoffset = {{ x = 0.0 y = 0.0 }}
            animationtexturescale = {{ x = 1.0 y = 1.0 }} 
        }}
        legacy_lazy_load = no
    }}
    }}
    '''

    # Save
    with open('goals_shine.gfx', 'w') as goals_shine_file:
        goals_shine_file.write(data)

def main():
    while True:
        icon_name = input("Write icon name\nWrite 0 to exit: ")
        if icon_name == '0':
            break
        modify_goals_gfx(icon_name)
        modify_goals_shine_gfx(icon_name)

if __name__ == "__main__":
    main()
