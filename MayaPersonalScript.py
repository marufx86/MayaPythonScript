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
