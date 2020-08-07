# systemic-immune-response

Integrate immune response (ODE) with PhysiCell

For now, just compile with `make` and run `COVID19` to see the dummy `lymphatic_main_model` being invoked. Files of interest are `custom_modules/lymphatic_submodel.{h,cpp}` and `main.cpp`.

## Changes from original 3.2 code
* added `custom_modules/lymphatic_submodel.{h,cpp}`

Not yet using, but also:
* added `beta/setup_libroadrunner.py`
* added `intracellular/PhysiCell_intracellular.h`
* added `std::string sbml_filename;` into `class Cell_Definition` (in `core/PhysiCell_cell.h`)
* incorporate intracellular (SBML, libRoadrunner) info into `custom.{h,cpp}`
  * see `assign_SBML_model( Cell* pC )` in `custom.cpp`
  * see extra code in `create_cell_types( void )` where we obtain the desired SBML species' indices.
* added `Make-sbml`