# Select Children Object on outliner

import maya.cmds as cmds

def select_children_with_partial_name(parent_name, partial_name):
    # Check if the parent object exists
    if cmds.objExists(parent_name):
        # List all children of the specified parent
        children = cmds.listRelatives(parent_name, children=True, fullPath=True) or []

        # Filter children with the specified partial name
        matching_children = [child for child in children if partial_name in cmds.listRelatives(child, parent=False, fullPath=True)[0]]

        # Select the matching children
        if matching_children:
            cmds.select(matching_children, replace=True)
            print(f"Selected {len(matching_children)} objects with name containing '{partial_name}' under '{parent_name}'.")
        else:
            print(f"No objects with name containing '{partial_name}' found under '{parent_name}'.")
    else:
        print(f"Object '{parent_name}' does not exist.")

# Replace '_Outline' with the actual name of your parent object and '_PartialName' with the partial name to match
parent_name = "_Outline"
partial_name = "_Outline"
select_children_with_partial_name(parent_name, partial_name)

############################################################################################################################################################

# Ungroup all and unparent all

import maya.cmds as cmds

def ungroup_unparent_and_delete_history():
    # Get a list of all groups in the scene
    groups = cmds.ls(type='transform', long=True)

    # Iterate through the list and ungroup each group
    for group in groups:
        children = cmds.listRelatives(group, children=True, fullPath=True)
        if children and cmds.objectType(children[0]) == 'transform':
            cmds.parent(children, world=True)

    print("Ungrouped all objects.")

    # Unparent all objects
    all_objects = cmds.ls(dag=True, long=True)
    cmds.parent(all_objects, world=True)

    print("Unparented all objects.")

    # Delete construction history for all objects in the scene
    cmds.delete(all_objects, constructionHistory=True)

    print("Deleted construction history for all objects.")

# Call the function to ungroup, unparent, and delete history
ungroup_unparent_and_delete_history()

###############################################################################################
import maya.cmds as cmds

def delete_empty_groups():
    """Deletes all empty groups in the scene."""

    # Get a list of all transform nodes (potential groups)
    all_transforms = cmds.ls(type='transform')

    # Iterate through each transform node
    for transform in all_transforms:
        # Check if it's a group (has children)
        children = cmds.listRelatives(transform, children=True)
        if not children:
            # If no children, it's an empty group, so delete it
            cmds.delete(transform)

    print("Deleted all empty groups.")

# Call the function to delete empty groups
delete_empty_groups()
###############################################################################################

#############################################################################################

# remove prefix from name

import maya.cmds as cmds

def remove_pasted_prefix():
    # Specify the prefix to remove
    prefix_to_remove = "pasted__"

    # Get selected objects
    selected_objects = cmds.ls(selection=True, long=True)

    if not selected_objects:
        print("No objects selected.")
        return

    for obj in selected_objects:
        # Check if the object name contains the specified prefix
        if prefix_to_remove in obj:
            # Remove the specified prefix
            new_name = obj.replace(prefix_to_remove, "")
            # Rename the object
            cmds.rename(obj, new_name)
            print(f"Removed '{prefix_to_remove}' prefix from: {new_name}")

# Call the function to remove the prefix from selected objects
remove_pasted_prefix()

###############################################################################################

# Make objects as parent and child
# c1 & c1_child will give result as

#  c1
#    -c1_child

import maya.cmds as cmds

def create_parent_child_sets():
    # Get all objects in the scene
    all_objects = cmds.ls(dag=True, long=True)

    # Iterate through the objects and find parent-child pairs
    for obj in all_objects:
        if obj.endswith("_child"):
            # Extract the parent name
            parent_name = obj.rsplit("_", 1)[0]

            # Check if the parent exists
            if cmds.objExists(parent_name):
                # Parent the child under the parent
                cmds.parent(obj, parent_name)
                print(f"Parented '{obj}' under '{parent_name}'.")

# Call the function to create parent-child relationships
create_parent_child_sets()

##############################################################################################################################################################################

#group everything with same name

import maya.cmds as cmds

def group_pcube_objects():
    # Create the group (if it doesn't exist)
    group_name = "pSphere_group"
    if not cmds.objExists(group_name):
        cmds.group(empty=True, name=group_name)

    # Iterate through objects and group those starting with "pCube"
    for obj in cmds.ls(type='transform'):
        if obj.startswith("pSphere"):
            cmds.parent(obj, group_name)

    print(f"Grouped objects starting with 'pCube' under '{group_name}'")

# Call the function
group_pcube_objects()

#####################################################################################################################################################################

#group everything with same middle name

import maya.cmds as cmds

def group_solid_concrete_objects():
    group_name = "Solid_Concrete"  # Name for the group

    # Create group if it doesn't exist
    if not cmds.objExists(group_name):
        cmds.group(empty=True, name=group_name)

    # Find and group objects with "Solid_Concrete" in their name
    for obj in cmds.ls(type='transform'): 
        if "Solid_Concrete" in obj:
            cmds.parent(obj, group_name)

    print(f"Grouped objects containing 'Solid_Concrete' under '{group_name}'")

# Call the function
group_solid_concrete_objects()

#####################################################################################################################################################################

#assign materials based on the object name on outliner

import maya.cmds as cmds

def create_materials_from_names():
    for obj in cmds.ls(type='transform'):
        if obj.startswith("pool_Umbrella"):  # Adjust prefix as needed
            # Extract base name (e.g., "pCube1")
            base_name = obj.split("|")[-1] 
            # Create new material name
            material_name = base_name + "_m"
            
            # Create new Lambert material if it doesn't exist
            if not cmds.objExists(material_name):
                cmds.shadingNode('lambert', asShader=True, name=material_name)
            
            # Assign the new material to the object
            cmds.select(obj)
            cmds.hyperShade(assign=material_name)

# Call the function
create_materials_from_names()

#####################################################################################################################################################################

#create materials from names with random color

import maya.cmds as cmds
import random

def create_materials_from_names_with_random_color():
    for obj in cmds.ls(type='transform'):
        if obj.startswith("generic"):  # Adjust prefix as needed
            base_name = obj.split("|")[-1]
            material_name = base_name + "_m"
            
            if not cmds.objExists(material_name):
                cmds.shadingNode('lambert', asShader=True, name=material_name)
                
                # Generate random color
                random_color = (random.random(), random.random(), random.random())
                
                # Set the color of the material
                cmds.setAttr(material_name + ".color", *random_color) 
            
            cmds.select(obj)
            cmds.hyperShade(assign=material_name)

# Call the function
create_materials_from_names_with_random_color()

############################################################################################################################################################################

#replace the object name with material name(material should be lambert)
import maya.cmds as cmds

def rename_object_with_material():
    """
    Renames the selected object to the name of its assigned material.
    """

    selected_objects = cmds.ls(selection=True)

    if selected_objects:
        obj = selected_objects[0]  # Get the first selected object

        # Find the Shading Group connected to the object's shape node
        shape_node = cmds.listRelatives(obj, shapes=True)[0]
        shading_group = cmds.listConnections(shape_node, type="shadingEngine")

        if shading_group:
            # Get the material connected to the Shading Group
            material = cmds.listConnections(shading_group[0], source=True, destination=False)

            if material:
                material_name = material[0]  # Get the first assigned material
                cmds.rename(obj, material_name)  # Rename the object
            else:
                print(f"No material connected to Shading Group of {obj}")
        else:
            print(f"No Shading Group found for {obj}")

rename_object_with_material()
#############################################################################################################################################################################

#(batch select objects)replace the object name with material name(material should be lambert)

import maya.cmds as cmds

def rename_objects_with_material():
    """
    Renames selected objects to the names of their assigned materials.
    """

    selected_objects = cmds.ls(selection=True)

    for obj in selected_objects:
        # Find the Shading Group connected to the object's shape node
        shape_node = cmds.listRelatives(obj, shapes=True)[0]
        shading_group = cmds.listConnections(shape_node, type="shadingEngine")

        if shading_group:
            # Get the material connected to the Shading Group
            material = cmds.listConnections(shading_group[0], source=True, destination=False)

            if material:
                material_name = material[0]  # Get the first assigned material
                cmds.rename(obj, material_name)  # Rename the object
            else:
                print(f"No material connected to Shading Group of {obj}")
        else:
            print(f"No Shading Group found for {obj}")

rename_objects_with_material()

#####################################################################################################################################################################
import maya.cmds as cmds

def remove_prefix_from_names():
    """
    Removes the "pasted__" prefix from the names of selected objects.
    """

    selected_objects = cmds.ls(selection=True)

    for obj in selected_objects:
        if obj.startswith("pasted__"):
            new_name = obj.replace("pasted__", "")
            cmds.rename(obj, new_name)

remove_prefix_from_names()

########################################################################################################################################################################
import maya.cmds as cmds

def remove_double_prefix_from_materials():
    """
    Removes the "pasted__pasted__" prefix from the names of all materials in the scene.
    """

    all_materials = cmds.ls(materials=True)

    for material in all_materials:
        if material.startswith("pasted__pasted__"):
            new_name = material.replace("pasted__pasted__", "")
            cmds.rename(material, new_name)

remove_double_prefix_from_materials()