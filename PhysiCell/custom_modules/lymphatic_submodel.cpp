#include "./lymphatic_submodel.h" 

using namespace PhysiCell; 

std::string lymphatic_model_version = "0.1.0"; 

Submodel_Information lymphatic_submodel_info; 

void lymphatic_submodel_setup( void )
{
		// set version 
	lymphatic_submodel_info.name = "lymphatic model"; 
	lymphatic_submodel_info.version = lymphatic_model_version; 

		// set functions 
	lymphatic_submodel_info.main_function = lymphatic_main_model;
	lymphatic_submodel_info.phenotype_function = NULL; // pushed into the "main" model  
	lymphatic_submodel_info.mechanics_function = NULL;

		// what microenvironment variables do you need 
	lymphatic_submodel_info.microenvironment_variables.push_back( "virion" );

		// what cell variables and parameters do you need? 
	lymphatic_submodel_info.cell_variables.push_back( "unbound_external_ACE2" ); 
	
	lymphatic_submodel_info.register_model(); 
	
	return; 
}

void lymphatic_model( Cell* pCell, Phenotype& phenotype, double dt )
{
	static int lung_epithelial_type = get_cell_definition( "lung epithelium" ).type; 
	
	// bookkeeping -- find microenvironment variables we need

	static int nV_external = microenvironment.find_density_index( "virion" ); 
	
	static int nV_internal = pCell->custom_data.find_variable_index( "virion" ); 

	// bookkeeping -- find custom data we need 
	
	static int nR_EU = pCell->custom_data.find_variable_index( "unbound_external_ACE2" ); 
	
	// do nothing if dead 
	if( phenotype.death.dead == true )
	{ return; } 

	// if not lung epithelium, do nothing 
	// if( pCell->type != lung_epithelial_type )
	// { return; } 
	
	// actual model goes here 
	
	
	return; 
}

void lymphatic_main_model( double dt )
{
	std::cout << "---------- lymphatic_main_model: " << PhysiCell_globals.current_time << std::endl;
	#pragma omp parallel for 
	for( int n=0; n < (*all_cells).size() ; n++ )
	{
		Cell* pC = (*all_cells)[n]; 
		if( pC->phenotype.death.dead == false )
		{ lymphatic_model( pC, pC->phenotype , dt ); }
	}
	
	return; 
}
	
