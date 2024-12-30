# Maya Python Scripts Repository

This repository contains a collection of Python scripts for automating and optimizing various tasks in Autodesk Maya. These scripts are designed to enhance workflow efficiency, especially in scenes involving multiple objects, groups, materials, and transformations.

---

## Scripts Overview

### 1. **Select Children Objects by Partial Name**
   - **Functionality:** Selects child objects under a specified parent object based on a partial name match.
   - **Usage:** Replace `_Outline` with the parent object name and the desired partial name.

### 2. **Parent Outlines to Base Objects**
   - **Functionality:** Parents objects ending with `_Outline` to their corresponding base objects.
   - **Example:** `object_Outline` becomes a child of `object`.

### 3. **Ungroup, Unparent, and Clear History**
   - **Functionality:** Ungroups all objects, unparents them, and deletes their construction history.

### 4. **Delete Empty Groups**
   - **Functionality:** Deletes all empty groups in the scene.

### 5. **Group Individual Objects**
   - **Functionality:** Creates individual groups for each top-level object in the scene.

### 6. **Separate Objects Inside Groups**
   - **Functionality:** Separates geometry within groups using Maya's `Separate` operation.

### 7. **Remove Prefix from Names**
   - **Functionality:** Removes a specified prefix (e.g., `pasted__`) from selected object names.

### 8. **Create Parent-Child Relationships**
   - **Functionality:** Automatically parents objects with names ending in `_child` to their corresponding parent objects.

### 9. **Group Objects with Similar Names**
   - **Functionality:** Groups objects based on shared naming conventions or patterns (e.g., same prefix or middle name).

### 10. **Assign Materials Based on Object Names**
   - **Functionality:** Creates and assigns materials to objects based on their names.

### 11. **Assign Materials with Random Colors**
   - **Functionality:** Generates and assigns materials with random colors to objects with specific naming patterns.

### 12. **Rename Objects with Material Names**
   - **Functionality:** Renames objects based on their assigned materials (supports Lambert and Phong).

### 13. **Add Suffix to Object Names**
   - **Functionality:** Adds a specified suffix (e.g., `_1`) to all object names in the scene.

### 14. **Retain Camera Settings While Clearing Scene**
   - **Functionality:** Deletes all objects, groups, and materials while retaining active camera settings.

### 15. **Remove Double Prefixes from Materials**
   - **Functionality:** Cleans up material names by removing redundant prefixes like `pasted__pasted__`.

---

## How to Use
1. Copy the desired script(s) into Maya's Script Editor.
2. Execute the script using the `Run` button or assign it to a shelf button for quick access.
3. Modify the parameters (e.g., object names, prefixes, suffixes) as needed.

---

## Examples
### Example 1: Select Children Objects
```python
parent_name = "ParentObjectName"
partial_name = "_ChildPartialName"
select_children_with_partial_name(parent_name, partial_name)
```

### Example 2: Group Objects by Name
```python
group_name = "GroupName"
group_solid_concrete_objects()
```

---

## Contributions
Feel free to contribute additional scripts or improvements by creating a pull request.

---

## License
This repository is licensed under the MIT License. See the `LICENSE` file for details.
