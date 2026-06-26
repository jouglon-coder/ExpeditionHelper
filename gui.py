from dataclasses import fields
import tkinter as tk
from tkinter import ttk

from manager import Manager
from data.weapons import weapons
from data.pictos import pictos
from data.skills import skills


EFFECTS = (
    "rush",
    "shell",
    "powerful",
    "powerless",
    "slow",
    "defenceless",
    "base attack",
    "shot",
    "burn",
    "mark",
)


class ExpeditionHelperApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Expedition Helper")
        self.root.geometry("1200x700")

        self.manager = Manager()

        self.manager.weapons.extend(weapons)
        self.manager.pictos.extend(pictos)
        self.manager.skills.extend(skills)

        self.manager.weapons.sort(
            key=lambda item: (item.owner, item.name)
        )
        self.manager.pictos.sort(
            key=lambda item: item.name
        )
        self.manager.skills.sort(
            key=lambda item: (item.owner, item.name)
        )

        self.create_tabs()

    def create_tabs(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True)

        weapons_tab = ttk.Frame(notebook)
        pictos_tab = ttk.Frame(notebook)
        skills_tab = ttk.Frame(notebook)

        notebook.add(weapons_tab, text="Weapons")
        notebook.add(pictos_tab, text="Pictos")
        notebook.add(skills_tab, text="Skills")

        self.create_effects_page(
            parent=weapons_tab,
            items=self.manager.weapons,
            search_fields=("lvl4", "lvl10", "lvl20"),
        )

        self.create_effects_page(
            parent=pictos_tab,
            items=self.manager.pictos,
            search_fields=("description",),
        )

        self.create_effects_page(
            parent=skills_tab,
            items=self.manager.skills,
            search_fields=("description", "special"),
        )

    def create_effects_page(
        self,
        parent: ttk.Frame,
        items: list,
        search_fields: tuple[str, ...],
    ):
        filters_frame = ttk.Frame(parent)
        filters_frame.pack(fill="x", padx=10, pady=10)

        ttk.Label(
            filters_frame,
            text="Effects:",
        ).pack(
            side="left",
            padx=(0, 10),
        )

        effect_variables = {
            effect: tk.BooleanVar()
            for effect in EFFECTS
        }

        table, details = self.create_table(parent, items)

        for effect_name, variable in effect_variables.items():
            checkbutton = ttk.Checkbutton(
                filters_frame,
                text=effect_name.title(),
                variable=variable,
                command=lambda: self.filter_by_effects(
                    table=table,
                    items=items,
                    search_fields=search_fields,
                    effect_variables=effect_variables,
                    details=details,
                ),
            )

            checkbutton.pack(side="left", padx=5)

        table.bind(
            "<<TreeviewSelect>>",
            lambda event: self.show_details(
                table,
                details,
            ),
        )

    def create_table(
        self,
        parent: ttk.Frame,
        items: list,
    ):
        column_names = [
            field.name
            for field in fields(items[0])
        ]

        content_frame = ttk.Panedwindow(
            parent,
            orient="vertical",
        )
        content_frame.pack(fill="both", expand=True)

        table_frame = ttk.Frame(content_frame)
        details_frame = ttk.Frame(content_frame)

        content_frame.add(table_frame, weight=3)
        content_frame.add(details_frame, weight=1)

        table = ttk.Treeview(
            table_frame,
            columns=column_names,
            show="headings",
        )

        vertical_scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=table.yview,
        )

        horizontal_scrollbar = ttk.Scrollbar(
            table_frame,
            orient="horizontal",
            command=table.xview,
        )

        table.configure(
            yscrollcommand=vertical_scrollbar.set,
            xscrollcommand=horizontal_scrollbar.set,
        )

        table.grid(
            row=0,
            column=0,
            sticky="nsew",
        )

        vertical_scrollbar.grid(
            row=0,
            column=1,
            sticky="ns",
        )

        horizontal_scrollbar.grid(
            row=1,
            column=0,
            sticky="ew",
        )

        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)

        for column_name in column_names:
            table.heading(
                column_name,
                text=column_name.replace("_", " ").title(),
            )

            table.column(
                column_name,
                width=self.get_column_width(column_name),
                minwidth=80,
                anchor="w",
            )

        details = tk.Text(
            details_frame,
            wrap="word",
            height=10,
            padx=10,
            pady=10,
            state="disabled",
        )

        details_scrollbar = ttk.Scrollbar(
            details_frame,
            orient="vertical",
            command=details.yview,
        )

        details.configure(
            yscrollcommand=details_scrollbar.set,
        )

        details.grid(
            row=0,
            column=0,
            sticky="nsew",
        )

        details_scrollbar.grid(
            row=0,
            column=1,
            sticky="ns",
        )

        details_frame.rowconfigure(0, weight=1)
        details_frame.columnconfigure(0, weight=1)

        self.fill_table(table, items)

        return table, details

    def filter_by_effects(
        self,
        table: ttk.Treeview,
        items: list,
        search_fields: tuple[str, ...],
        effect_variables: dict[str, tk.BooleanVar],
        details: tk.Text,
    ):
        selected_effects = [
            effect_name
            for effect_name, variable in effect_variables.items()
            if variable.get()
        ]

        if not selected_effects:
            filtered_items = items
        else:
            filtered_items = []

            for item in items:
                searchable_text = " ".join(
                    str(getattr(item, field_name))
                    for field_name in search_fields
                ).lower()

                if all(
                    effect in searchable_text
                    for effect in selected_effects
                ):
                    filtered_items.append(item)

        self.fill_table(table, filtered_items)
        self.clear_details(details)

    def fill_table(
        self,
        table: ttk.Treeview,
        items: list,
    ):
        table.delete(*table.get_children())
        table.item_objects = {}

        column_names = table["columns"]

        for item in items:
            values = [
                self.format_value(
                    getattr(item, column_name)
                )
                for column_name in column_names
            ]

            row_id = table.insert(
                "",
                "end",
                values=values,
            )

            table.item_objects[row_id] = item

    def show_details(
        self,
        table: ttk.Treeview,
        details: tk.Text,
    ):
        selected_rows = table.selection()

        if not selected_rows:
            self.clear_details(details)
            return

        row_id = selected_rows[0]
        item = table.item_objects.get(row_id)

        if item is None:
            self.clear_details(details)
            return

        lines = []

        for field in fields(item):
            title = field.name.replace("_", " ").title()
            value = self.format_value(
                getattr(item, field.name)
            )

            lines.append(
                f"{title}:\n{value}"
            )

        details.configure(state="normal")
        details.delete("1.0", "end")
        details.insert(
            "1.0",
            "\n\n".join(lines),
        )
        details.configure(state="disabled")

    @staticmethod
    def clear_details(details: tk.Text):
        details.configure(state="normal")
        details.delete("1.0", "end")
        details.configure(state="disabled")

    @staticmethod
    def format_value(value):
        if isinstance(value, dict):
            return " | ".join(
                f"{location}: {description}"
                for location, description in value.items()
            )

        return str(value)

    @staticmethod
    def get_column_width(column_name: str):
        widths = {
            "name": 160,
            "owner": 90,
            "elem": 90,
            "cost": 60,
            "description": 500,
            "special": 400,
            "location": 600,
            "lvl4": 400,
            "lvl10": 400,
            "lvl20": 400,
        }

        return widths.get(column_name, 150)
