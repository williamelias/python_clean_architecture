#!/usr/bin/env python3
from clean_project.database import models as md
from sqlalchemy_data_model_visualizer import (
    generate_data_model_diagram,
    add_web_font_and_interactivity,
)


if __name__ == "__main__":
    # List of models to create visual data
    # models = [Item, TodoList, Owner]
    models = [md.Item, md.TodoList, md.Owner]

    base_path_file = "./assets/diagram/model_diagram"

    generate_data_model_diagram(models, base_path_file)
    add_web_font_and_interactivity(base_path_file, f"{base_path_file}.svg")
