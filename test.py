import bpy

scene = bpy.context.scene
for obj in scene.objects:
    
    if obj.type == 'MESH':
        obj.location.x += 1.0
        print("object : " + obj.name + " type : " + obj.type)