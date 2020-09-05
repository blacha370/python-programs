from tkinter import ttk

class GuiCreator:
    @staticmethod
    def createGuiElement(data, widget_type, parent, element_name, position=(0, 0), text=None):
        element = widget_type(parent, text=text)
        element.grid(column=position[0], row=position[1])
        data['elements'][element_name] = element

    @staticmethod
    def createButton(data, parent, button_name, command, text=str(), position=(0, 0)):
        element = ttk.Button(parent, command=command, text=text)
        element.grid(column=position[0], row=position[1])
        data['elements'][button_name] = element

    @staticmethod
    def destroyFrame(elements):
        list_to_delete = []
        for item in elements.items():
            if not item[0] == 'root':
                list_to_delete.append(item[1])
        for widget in list_to_delete:
            widget.destroy()
