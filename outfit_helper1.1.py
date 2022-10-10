import os
from tkinter import*
from tkinter import ttk
import time
from tkinter import filedialog



mod_name_get = ''
head_get = 0
skin_get = ''
mask = 0
root = Tk() 
root.title('outfit helper')


width = 354
height = 250
my_notebook=ttk.Notebook(root)
my_notebook.grid(row=0, column=0, padx = 5, pady=5)

#root.configure(background="grey")


bg_color = "#dbdbdb"
frame_color = 'white'


mpath = os.getcwd()
options = Frame(my_notebook, width=width, height=height)#tab for seting up options like head on/off
options.pack(fill="both", expand=1)
my_notebook.add(options, text="setup")

mat = Frame(my_notebook, width=width, height=height)
mat.pack(fill='both', expand=1)
my_notebook.add(mat, text="texture")

#loc = Frame(my_notebook, width = width, height = height)
#loc.pack(fill="both", expand=1)
#my_notebook.add(loc, text='localization')

#obj = Frame(my_notebook, width=width, height=height)
#obj.pack(fill="both", expand=1)
#my_notebook.add(obj, text="object")
root.geometry(str(width)+"x"+str(height))
export = Frame(my_notebook, width=width, height=height)
export.pack(fill="both", expand=1)
my_notebook.add(export, text="create files")
def main():#options tab
        
    
    
    

    #loc = Frame(my_notebook, width=width, height=height)
    #loc.pack(fill='both', expand=1)
   # my_notebook.add(loc, text='localization')




    def options_ender():#this runs and creates glboal variables for things like
        global mod_name_get#the mod name
        global mask
        global head_get
        global skin_get
        mask = mask_toggle.get()
        head_get = head_toggle.get()
        skin_get = skin_name_val.get()
        mod_name_get=mod_name_val.get()
        make_file()

    #loads save files
    def loader():
        load_data = ''
        try:
            root.load_file_path = filedialog.askopenfilename(initialdir=mpath, title="select save file", filetypes=(("save files", "*.save_file"),('all files', "*.*")))
            load_file = open(root.load_file_path, 'r')
        except FileNotFoundError:
            print('window dialog closed')
            return()
        x=0
        for line in load_file:
            load_data+=line
            x+=1
        load_data.split('|')
        load_split = load_data.split('|')
        print(load_split,'  <---save contents')
        mod_name.delete(0, END)
        mod_name.insert(0, load_split[0])
        skin_name.delete(0, END)
        skin_name.insert(0, load_split[1])
        if head_toggle.get() != int(load_split[2]):
            print('head toggled')
            head_toggle_box.toggle()
        if mask_toggle.get() != int(load_split[3]):
            print('mask toggled')
            mask_toggle_box.toggle()
            
        global mat_list
        mat_list= load_split[4].split('TEXTURESPLIT')
        global mat_temp
        mat_temp = load_split[5].split('TEXTURESPLIT')
        global mat_nm
        mat_nm = load_split[6].split('TEXTURESPLIT')
        global obj_list
        obj_list = load_split[7].split('OBJECTSPLIT')      
        obj_list.pop()
        obj_listbox.delete(0, END)
        for stuff in obj_list:
            obj_listbox.insert(0, stuff)
        
        mat_listbox.delete(0, END)
        mat_list.pop()
        mat_nm.pop()
        mat_temp.pop()
        print('''
material name list
---------------------------------------
''',mat_list)
        print('''
material template/type
---------------------------------------
''',mat_temp)
        for stuff in mat_list:
            mat_listbox.insert(0, stuff)
        
        load_file.close()
        print ('''
normals on/off
---------------------------------------
''',mat_nm)
        print('''
object list
---------------------------------------
''',obj_list)
    #saves files
    def saver():
        save_file_path = os.path.join(mpath, (mod_name_val.get()+'.save_file'))#path to the save file
        save_file = open(save_file_path, 'w')
        save_file.write(mod_name_val.get()+'|')#0 saves mod name
        save_file.write(skin_name_val.get()+'|')#1 saves skin name
        save_file.write(str(head_toggle.get())+'|')#2 saves head toggle
        save_file.write(str(mask_toggle.get())+'|')#3 saves mask toggle
        x=0
        for i in mat_list:
            save_file.write(mat_list[x]+'TEXTURESPLIT') #4 material list
            x+=1
        save_file.write('|')
        x=0
        for i in mat_temp:
            save_file.write(mat_temp[x]+"TEXTURESPLIT") #5 material template
            x+=1
        save_file.write('|')
        x=0
        for i in mat_nm:
            save_file.write(str(mat_nm[x])+'TEXTURESPLIT')
            x+=1
        save_file.write('|')
        x=0
        for i in obj_list:            
            save_file.write(str(obj_list[x])+'OBJECTSPLIT')
            x+=1
        
        save_file.write('|')
        x=0
        

        save_file.close()


    #load save button
    label =Label(options, text='')
    label.grid(row=4, column=0)
    save_button = Button(options, relief=RIDGE, text='load options', command=loader, bg=bg_color)
    save_button.grid(row=10, column=0, columnspan=5, sticky=EW)
    #save button
    save_button = Button(export, text='save options', command=saver, bg=bg_color)
    save_button.grid(row=4, column=0)

    
        
    #increase the size of the tab
    label = Label(options, text="                                                 ")
    label.grid(row=0, column=0, columnspan=2)
    #name of the mod
    global mod_name_val
    mod_name_val = StringVar()
    mod_name = Entry(options, bg=bg_color, textvariable=mod_name_val, bd=1)
    label = Label(options, text="mod name")
    label.grid(row=0, column=0, sticky=S,)
    mod_name.grid(row=1, column=0, sticky=N)

    #name of the skin
    global skin_name_va
    skin_name_val = StringVar()
    skin_name = Entry(options, bg=bg_color, textvariable=skin_name_val,  bd=1)
    label = Label(options, text="skin name")
    label.grid(row=2, column=0, sticky=S,)
    skin_name.grid(row=3, column=0, sticky=N)



    #generate file button
    label = Label(export, text="                                                 ")
    label.grid(row=1, column=1)
    generate = Button(export, text="generate files", bg=bg_color, command=options_ender)
    generate.grid(row=1, column=0, sticky=EW, columnspan=2)

    #head replacement
    label.grid(row=0, column=1)
    head_toggle= IntVar()
    head_toggle_box = Checkbutton(options, text="replace head", variable=head_toggle, onvalue=True, offvalue=False)
    head_toggle_box.grid(row=1, column=2, sticky=N)

    #mask replacment
    mask_toggle = IntVar()
    mask_toggle_box = Checkbutton(options, text="hide mask", variable=mask_toggle, onvalue = True, offvalue=False)
    mask_toggle_box.grid(row=2, column=2, sticky=SW)    




    #textures
    #######################################################################
    label = Label(mat,  bg=frame_color, text="material name")
    label.grid(row=0, column=0, sticky=S)
    mat_name = Entry(mat, bg=bg_color)
    mat_name.grid(row=1, column=0, sticky=N)

    label = Label(mat,  bg=frame_color, text="render template/material type")
    label.grid(row=0, column=1)

    global template_list
    
    template_list =[
        'basic',
        'illumination',
        'opacity'
        ]
    template_act = StringVar(mat)
    template_picker = OptionMenu(mat, template_act, *template_list)
    template_picker.config(bg=bg_color,width=15)
    template_picker.grid(row=1, column=1, sticky=N)
    template_act.set(template_list[0])

    
    def add_material():
        if template_act.get() == "":
            print('no render template chosen')
        else:
            mat_list.append(mat_name.get())
            mat_temp.append(template_act.get())
            mat_nm.append(nm_check.get())
            mat_listbox.insert(END, mat_name.get())
            print('''
list of materials
-----------------------------------------------------------''')
        t = 0
        for i in mat_list:
            print(str(t+1)+":", mat_list[t]+"| type:", mat_temp[t]+'| normals:', mat_nm[t])
            t+=1
            #print("1:", mat_list[i], mat_temp[i])
    global mat_list
    global mat_temp
    global mat_nm
    mat_list = []
    mat_temp =[]
    mat_nm = []
    label = Label(mat,  bg=frame_color, text="")
    label.grid(row=4, column=0)
    add_mat = Button(mat, text="add material", command = add_material, bg = bg_color)
    add_mat.grid(row=3, column = 0, columnspan=4, sticky=EW)
    nm_check = IntVar()
    nm_box = Checkbutton(mat, text="""no normal texture""", variable=nm_check, onvalue=1, offvalue=0)
    nm_box.grid(row=2, column=0, sticky=NW)

    def mat_delete_func():
        mat_index = mat_list.index(mat_listbox.get(ANCHOR))
        mat_list.remove(mat_listbox.get(ANCHOR))
        del mat_nm[mat_index]
        del mat_temp[mat_index]
        mat_listbox.delete(ANCHOR)
    def mat_edit_func():
        mat_index= mat_list.index(mat_listbox.get(ANCHOR))
        mat_temp[mat_index]=template_act.get()
        mat_nm[mat_index]=nm_check.get()
        print('''
list of materials
-----------------------------------------------------------''')
        t = 0
        for i in mat_list:
            print(str(t+1)+":", mat_list[t]+"| type:", mat_temp[t]+'| normals:', mat_nm[t])
            t+=1
    
    mat_scroll = Scrollbar(mat, orient=VERTICAL)
    mat_listbox = Listbox(mat, width = 36, height=4, bg=bg_color, yscrollcommand=mat_scroll.set)
    mat_scroll.config(command=mat_listbox.yview, bg='blue')
    mat_scroll.grid(row=6, column=1, sticky=E)
    mat_listbox.grid(row=6, column=0, rowspan=10, columnspan=6, sticky=N)
    mat_delete = Button(mat, text="delete material", command=mat_delete_func, bg=bg_color)
    mat_delete.grid(row=5, column=0,  sticky=EW, padx=0)
    mat_edit = Button(mat, text="edit material", command=mat_edit_func, bg=bg_color)
    mat_edit.grid(row=5, column=1, sticky=EW, padx=15)
    



    #this handels the object stuff
    label = Label(options, text="insert object name")
    label.grid(row=4, column =0)
    obj_name = Entry(options, bg=bg_color)
    obj_name.grid(row=5, column=0)
    global obj_list
    obj_list = []
    def obj_adder():
        obj_list.append(obj_name.get())
        print("""----------------------
added""", obj_name.get(),'''
''',obj_list)
        obj_listbox.insert(END,obj_name.get())
    obj_add = Button(options, text="add object", command=obj_adder, bg=bg_color, relief=GROOVE)
    obj_add.grid(row=5, column=1, columnspan=2, sticky=EW)
    label = Label(options, text='')
    label.grid(row=6, column=0)

    #object list
    def deleter():
        obj_list.remove(obj_listbox.get(ANCHOR))
        obj_listbox.delete(ANCHOR)
    obj_listbox = Listbox(options, width = 15, height=5, bg=bg_color)
    obj_listbox.grid(row=1, column=4, rowspan=10, sticky=N)
    delete_obj = Button(options, text='delete object', command=deleter, bg=bg_color)
    delete_obj.grid(row=5, column=4)
    label = Label(options, text='objects list')
    label.grid(row=0, column=4)
    
    


#put important stuff here like file location, paths, and whatever gets shared between functions
def setup():
    global mpath #the filepath to the .py
    mpath= os.getcwd()


def make_file(): #this is what will generate the actual files
    mod_folder = os.path.join(mpath, mod_name_get)
    print(mat_list,'  <---mat_list')
    print(mat_temp, '  <==mat_temp')
    print(mod_name_get, "  <-------mod name")
    print(mod_folder, "  <----mod folder")
    os.mkdir(mod_folder)

    #makes all the main files for moding
    os.mkdir(mod_folder+'/assets')
    os.mkdir(mod_folder+'/assets/units')
    os.mkdir(mod_folder+'/assets/units/wardrobe_mod/')
    os.mkdir(mod_folder+'/assets/units/wardrobe_mod/armor_skins')
    os.mkdir(mod_folder+'/assets/units/wardrobe_mod/armor_skins/'+skin_get)
    os.mkdir(mod_folder+'/assets/units/wardrobe_mod/armor_skins/'+skin_get+'_fps')
    os.mkdir(mod_folder+'/assets/guis')
    os.mkdir(mod_folder+'/assets/guis/dlcs')
    os.mkdir(mod_folder+'/assets/guis/dlcs/wardrobe_mod')
    os.mkdir(mod_folder+'/assets/guis/dlcs/wardrobe_mod/textures')
    os.mkdir(mod_folder+'/assets/guis/dlcs/wardrobe_mod/textures/pd2')
    os.mkdir(mod_folder+'/assets/guis/dlcs/wardrobe_mod/textures/pd2/blackmarket')
    os.mkdir(mod_folder+'/assets/guis/dlcs/wardrobe_mod/textures/pd2/blackmarket/icons')
    os.mkdir(mod_folder+'/assets/guis/dlcs/wardrobe_mod/textures/pd2/blackmarket/icons/player_styles')

    default_fps_path = (mod_folder+'/assets/units/wardrobe_mod/armor_skins/'+skin_get+'_fps')
    default_path = (mod_folder+'/assets/units/wardrobe_mod/armor_skins/'+skin_get)

    #generate the files
    #the model

    gui_path = os.path.join((mod_folder+'/assets/guis/dlcs/wardrobe_mod/textures/pd2/blackmarket/icons/player_styles'), (skin_get+'.texture'))
    gui_main = open(gui_path, 'w')
    
    model = os.path.join(default_path, (skin_get+".model"))
    model_file = open(model, "w")

    model_fps = os.path.join(default_fps_path, (skin_get+"_fps.model"))
    model_fps_file = open(model_fps, "w")
    
    unit_path = os.path.join(default_path, (skin_get+".unit"))
    unit_file = open(unit_path, "w")

    unit_fps_path = os.path.join(default_fps_path, (skin_get+"_fps.unit"))
    unit_fps_file = open(unit_fps_path, "w")

    object_path = os.path.join(default_path, (skin_get+".object"))
    object_file = open(object_path, 'w')

    object_fps_path = os.path.join(default_fps_path, (skin_get+"_fps.object"))
    object_fps_file = open(object_fps_path, 'w')

    material_path = os.path.join(default_path, (skin_get+".material_config"))
    material_file = open(material_path, "w")

    material_fps_path = os.path.join(default_fps_path, (skin_get+"_fps.material_config"))
    material_fps_file = open(material_fps_path, "w")

  #generates the placeholder textures 
    x=0
    main_mat = []
    print(mat_nm)
    for i in mat_list:
        textures = os.path.join(default_path, (mat_list[x]+'_df.texture'))
        texture = open(textures, "w")
        main_mat.append(mat_list[x]+'_df')
        print(mat_nm[x])
        if mat_nm[x] =='0' or mat_nm[x] ==0 :
            textures = os.path.join(default_path, (mat_list[x]+'_nm.texture'))
            texture = open(textures, "w")
            main_mat.append(mat_list[x]+'_nm')
        if mat_temp[x] == 'opacity':
            textures = os.path.join(default_path, (mat_list[x]+'_op.texture'))
            texture = open(textures, "w")
            main_mat.append(mat_list[x]+'_op')
        if mat_temp[x] == 'illumination':
            textures = os.path.join(default_path, (mat_list[x]+'_il.texture'))
            texture = open(textures, "w")
            main_mat.append(mat_list[x]+'_il')

            
        x+=1
    print(main_mat,'  <---main_mat')
            




    #unit file
    unit_file.write('''<?xml version="1.0"?>
<unit type="dah" slot="1">
	<object file="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+skin_get+'''" />

	<extensions>
		<extension name="unit_data" class="ScriptUnitData" />
		<extension name="contour" class="ContourExt"/>
	</extensions>
</unit>''')
    unit_fps_file.write('''<?xml version="1.0"?>
<unit type="dah" slot="1">
	<object file="units/wardrobe_mod/armor_skins/'''+skin_get+'''_fps/'''+skin_get+'''_fps" />

	<extensions>
		<extension name="unit_data" class="ScriptUnitData" />
		<extension name="contour" class="ContourExt"/>
	</extensions>
</unit>''')

    

    #objectf file writer
    object_file.write('''<?xml version="1.0"?>
<dynamic_object>
	<diesel materials="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+skin_get+'''" orientation_object="root_point" />

	<graphics>
		<graphic_group name="character" enabled="true" culling_object="co_box">
''')
    object_fps_file.write('''<?xml version="1.0"?>
<dynamic_object>
	<diesel materials="units/wardrobe_mod/armor_skins/'''+skin_get+'''_fps/'''+skin_get+'''_fps" orientation_object="root_point" />

	<graphics>
		<graphic_group name="character" enabled="true" culling_object="co_box">
''')
    x=0
    for i in obj_list:
        object_file.write('''    			<object name="'''+obj_list[x]+'''" enabled="true"/>
''')
        object_fps_file.write('''    			<object name="'''+obj_list[x]+'''" enabled="true"/>
''')
        x+=1
    object_file.write('''
		</graphic_group>
	</graphics>

</dynamic_object>''')
    object_fps_file.write('''
		</graphic_group>
	</graphics>

</dynamic_object>''')
    


    #material config writer
    material_file.write('''<?xml version="1.0" ?>
<materials group="clown" version="3">
''')
    material_fps_file.write('''<?xml version="1.0" ?>
<materials group="clown" version="3">
''')
    x =0
    for i in mat_list:
        print(mat_temp[x])
        if mat_temp[x] == 'basic':#basic render template
            material_file.write('''    <material name="'''+mat_list[x]+'''" render_template="generic:CONTOUR:DIFFUSE_TEXTURE:NORMALMAP:RL_PLAYERS:SKINNED_3WEIGHTS" unique="true" version="2">
''')
        if mat_temp[x] =='illumination':#illumination render template
            print("glow")
            material_file.write('''    <material unique="true" render_template="generic:CONTOUR:DIFFUSE_TEXTURE:NORMALMAP:SELF_ILLUMINATION:SELF_ILLUMINATION_BLOOM:SKINNED_3WEIGHTS" name="'''+mat_list[x]+'''" version="2">
        <variable type="scalar" name="il_multiplier" value="reddot"/>
        <self_illumination_texture    file="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+mat_list[x]+'''_il"/>
        <variable type="scalar" name="il_bloom" value="1"/>
        <variable name="contour_distance"  value="0" type="scalar"/>
''')
        if mat_temp[x] == 'opacity': #opacity render template
            material_file.write('''	<material render_template="opacity:DIFFUSE_TEXTURE:NORMALMAP:OPACITY_CONTROLLER:SKINNED_3WEIGHTS" unique="true" version="2" name="'''+mat_list[x]+'''">
		<opacity_texture file="units/payday2/characters/'''+skin_get+'''/'''+mat_list[x]+'''_op"/>
''')
        material_file.write('''        <diffuse_texture file="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+mat_list[x]+'''_df"/>
''')
        if mat_nm[x] ==0:
            material_file.write('''        <bump_normal_texture file="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+mat_list[x]+'''_nm"/>''')
        else:
            material_file.write('''        <bump_normal_texture file="units/dev_tools/tangent_test/blank_nm"/>''')
        material_file.write('''
        <variable type="vector3" name="contour_color" value="1 1 1"/>
        <variable type="scalar" name="contour_opacity" value="0"/>
            
        </material>
''')
        if mat_temp[x]=="basic":
            material_fps_file.write('''    <material name="'''+mat_list[x]+'''" render_template="generic:DEPTH_SCALING:DIFFUSE_TEXTURE:NORMALMAP:SKINNED_3WEIGHTS" unique="true" version="2">''')
        if mat_temp[x] == 'illumination':
            material_fps_file.write('''    <material render_template="generic:DEPTH_SCALING:DIFFUSE_TEXTURE:NORMALMAP:SELF_ILLUMINATION:SELF_ILLUMINATION_BLOOM:SKINNED_3WEIGHTS" name="'''+mat_list[x]+'''" version="2">
        <variable type="scalar" name="il_multiplier" value="reddot"/>
        <self_illumination_texture    file="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+mat_list[x]+'''_il"/>
        <variable type="scalar" name="il_bloom" value="1"/>''')
        if mat_temp[x] == 'opacity':
            material_fps_file.write('''    <material render_template="opacity:DIFFUSE_TEXTURE:NORMALMAP:OPACITY_CONTROLLER:SKINNED_3WEIGHTS" unique="true" version="2" name="'''+mat_list[x]+'''" version="2">
		<opacity_texture file="units/payday2/characters/'''+skin_get+'''/'''+mat_list[x]+'''_op"/>''')
        material_fps_file.write('''
        <diffuse_texture file="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+mat_list[x]+'''_df"/>
''')
        if mat_nm[x] ==0:
            material_fps_file.write('''        <bump_normal_texture file="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+mat_list[x]+'''_nm"/>
''')
        else:
            material_fps_file.write('''        <bump_normal_texture file="units/dev_tools/tangent_test/blank_nm"/>
''')
        material_fps_file.write('''
    </material>
''')
        x+=1
    material_file.write("""
</material>""")
    material_fps_file.write('''
</material>''')
        
    

    
    
    
    #handels the generation of the localization file
    os.mkdir(mod_folder+"/localization")
    loc_text_loc = os.path.join((mod_folder+"/localization"),'english.txt')
    loc_text = open(loc_text_loc, "w")
    loc_text.write('''{
"bm_suit_'''+skin_get+'''" : "'''+skin_get+'''"
"menu_l_global_value_'''+skin_get+'''_g" : "'"
"bm_suit_'''+skin_get+'''_desc" : " "
}''')
    

    #chandels the generation of the main.xml file
    ##############################################################################
    main_xml_path = os.path.join(mod_folder, "main.xml")
    main_xml = open(main_xml_path, "w") #prints the main.xml
    main_xml.write('''<table name="'''+mod_name_get+'''" image="guis/dlcs/wardrobe_mod/textures/pd2/blackmarket/icons/player_styles/'''+mod_name_get+'''">
	<Localization directory="localization" default="english.txt"/>
	<GlobalValue id="'''+skin_get+'''_g" color="Color(10, 114, 177)"/>
	<PlayerStyle id="'''+skin_get+'''" unit="units/wardrobe_mod/armor_skins/'''+skin_get+'''_fps/'''+skin_get+'''_fps" third_unit="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+skin_get+'''" default_gloves="false" exclude_glove_adapter="true" texture_bundle_folder="wardrobe_mod" global_value="'''+skin_get+'''_g">
		<third_body_replacement	mask="''')
    if mask == 0:
        main_xml.write('false')
    else:
        main_xml.write('true')
    main_xml.write('''" head="''')
    if head_get==1:
        main_xml.write('true')
    else:
        main_xml.write('false')
    main_xml.write('''" armor="true" body="true" hands="true" vest="true" arms="true" glove_adapter="false"/>
		<body_replacement		mask="true" head="''')
    if head_get == 0: #for if the head is on/off 
        main_xml.write('false')
    else:
        main_xml.write('true')
    main_xml.write('''" armor="true" body="true" hands="true" vest="true" arms="true" glove_adapter="false"/>
		<characters>
			<bodhi		third_unit="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+skin_get+'''"/>
			<chains		third_unit="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+skin_get+'''"/>
			<dragon		third_unit="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+skin_get+'''"/>
			<joy		third_unit="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+skin_get+'''"/>
			<ecp_male	third_unit="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+skin_get+'''"/>
			<max		third_unit="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+skin_get+'''"/>
			<wild		third_unit="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+skin_get+'''"/>
			<jacket		third_unit="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+skin_get+'''"/>
			<jowi		third_unit="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+skin_get+'''"/>
			<chico		third_unit="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+skin_get+'''"/>
			<jimmy		third_unit="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+skin_get+'''"/>
			<sokol		third_unit="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+skin_get+'''"/>
			<myh		third_unit="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+skin_get+'''"/>
			<sydney		third_unit="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+skin_get+'''"/>
			<ecp_female	third_unit="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+skin_get+'''"/>
			<female_1	third_unit="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+skin_get+'''"/>
			<bonnie		third_unit="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+skin_get+'''"/>
		</characters>
	</PlayerStyle>

    <AddFiles directory="assets">	
	<texture path="guis/dlcs/wardrobe_mod/textures/pd2/blackmarket/icons/player_styles/'''+skin_get+'''"/>
''')
    x = 0
    for i in main_mat:
        main_xml.write('''	<texture path="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+main_mat[x]+'''"/>
''')
        x+=1

    main_xml.write('''	<unit_mat path="units/wardrobe_mod/armor_skins/'''+skin_get+'''/'''+skin_get+'''"/>
	<unit_mat path="units/wardrobe_mod/armor_skins/'''+skin_get+'''_fps/'''+skin_get+'''_fps"/>
</AddFiles>
</table>''')

    
    

main()
#input()
root.mainloop()
