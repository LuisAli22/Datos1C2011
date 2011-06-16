/*#include "view_manager.h"
#include "drawing_board.h"
#include "drawing_toolbar.h"
#include "network_toolbar.h"
#include "main_menu.h"
#include "about_dialog.h"
#include "save_as_dialog.h"
#include "open_dialog.h"
#include "confirmation_dialog.h"
#include "open_error_dialog.h"*/
#include "circuit_manager.h"
#include "model_view_interface.h"
#include "view.h"
#include "settings.h"
#include <gtkmm.h>
#include <iostream>
#include <libglademm/xml.h>

//void on_window_destroy (GtkObject *object, gpointer user_data)
//{
//        gtk_main_quit();
//}

int main (int argc, char **argv){

	//Gtk::Window* window = 0;

	Gtk::Main kit(argc, argv);

	Glib::RefPtr<Gnome::Glade::Xml> refXml;

	try {
		refXml = Gnome::Glade::Xml::create("vista_1tab_test_super_asd5.glade");
	}

	catch(const Gnome::Glade::XmlError& ex) {
		std::cerr << "FileError: " << ex.what() << std::endl;
		return 1;
	}

	CircuitManager circuitManager;
	Settings settings;
	ModelViewInterface interface(circuitManager, settings);

	View view(kit, refXml, interface);

	//AboutDialog aboutDialog(refXml);
	//SaveAsDialog saveAsDialog(refXml, interface);
	//OpenDialog openDialog(refXml, interface);
	//ConfirmationDialog confirmationDialog;
	//OpenErrorDialog openErrorDialog;
	//MenuEmergente menuEmergente(refXml);

	//MainMenu mainMenu(refXml);

	//ViewManager viewManager(refXml, aboutDialog, saveAsDialog, openDialog, confirmationDialog, mainMenu, interface, menuEmergente, openErrorDialog);
	//mainMenu.set_view_manager(&viewManager);
	interface.set_view_manager(view.get_view_manager());

	//DrawingToolbar drawingToolbar(refXml, viewManager);
	//NetworkToolbar networkToolbar(refXml);

	//window->show_all_children();

	//kit.run(*window);

	//delete window;

	view.start();

	return 0;

}

