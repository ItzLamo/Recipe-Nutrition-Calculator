import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import json
import os

# Constants and Configuration
PADDING = {"small": 5, "medium": 10, "large": 15}
COLORS = {
    "primary": "#2196F3",
    "secondary": "#FFC107",
    "success": "#4CAF50",
    "error": "#F44336",
    "background": "#F5F5F5",
    "text": "#212121"
}

NUTRITION_DATA = {
    # Meat
    "chicken breast": {
        "calories": 165, "protein": 31, "carbs": 0, "fat": 3.6,
        "fiber": 0, "sugar": 0, "unit": "g", "serving_size": 100,
        "category": "meat"
    },
    "beef steak": {
        "calories": 250, "protein": 26, "carbs": 0, "fat": 17,
        "fiber": 0, "sugar": 0, "unit": "g", "serving_size": 100,
        "category": "meat"
    },
    "pork loin": {
        "calories": 242, "protein": 27, "carbs": 0, "fat": 14,
        "fiber": 0, "sugar": 0, "unit": "g", "serving_size": 100,
        "category": "meat"
    },
    "turkey breast": {
        "calories": 135, "protein": 30, "carbs": 0, "fat": 1,
        "fiber": 0, "sugar": 0, "unit": "g", "serving_size": 100,
        "category": "meat"
    },
    "lamb chop": {
        "calories": 294, "protein": 25, "carbs": 0, "fat": 21,
        "fiber": 0, "sugar": 0, "unit": "g", "serving_size": 100,
        "category": "meat"
    },
    
    # Vegetables
    "spinach": {
        "calories": 23, "protein": 2.9, "carbs": 3.6, "fat": 0.4,
        "fiber": 2.2, "sugar": 0.4, "unit": "g", "serving_size": 100,
        "category": "vegetables"
    },
    "broccoli": {
        "calories": 55, "protein": 3.7, "carbs": 11, "fat": 0.6,
        "fiber": 2.4, "sugar": 1.7, "unit": "g", "serving_size": 100,
        "category": "vegetables"
    },
    "carrot": {
        "calories": 41, "protein": 0.9, "carbs": 9.6, "fat": 0.2,
        "fiber": 2.8, "sugar": 4.7, "unit": "g", "serving_size": 100,
        "category": "vegetables"
    },
    "cucumber": {
        "calories": 16, "protein": 0.7, "carbs": 3.6, "fat": 0.1,
        "fiber": 0.5, "sugar": 1.7, "unit": "g", "serving_size": 100,
        "category": "vegetables"
    },
    "bell pepper": {
        "calories": 31, "protein": 1, "carbs": 6, "fat": 0.3,
        "fiber": 2.1, "sugar": 4.2, "unit": "g", "serving_size": 100,
        "category": "vegetables"
    },
    
    # Fruits
    "apple": {
        "calories": 52, "protein": 0.3, "carbs": 14, "fat": 0.2,
        "fiber": 2.4, "sugar": 10.4, "unit": "piece", "serving_size": 1,
        "category": "fruits"
    },
    "banana": {
        "calories": 89, "protein": 1.1, "carbs": 23, "fat": 0.3,
        "fiber": 2.6, "sugar": 12, "unit": "piece", "serving_size": 1,
        "category": "fruits"
    },
    "orange": {
        "calories": 43, "protein": 1, "carbs": 11, "fat": 0.1,
        "fiber": 2.2, "sugar": 9, "unit": "piece", "serving_size": 1,
        "category": "fruits"
    },
    "grapes": {
        "calories": 69, "protein": 0.7, "carbs": 18, "fat": 0.2,
        "fiber": 0.9, "sugar": 16, "unit": "g", "serving_size": 100,
        "category": "fruits"
    },
    "avocado": {
        "calories": 160, "protein": 2, "carbs": 9, "fat": 15,
        "fiber": 7, "sugar": 0.7, "unit": "g", "serving_size": 100,
        "category": "fruits"
    },
    
    # Dairy
    "milk": {
        "calories": 42, "protein": 3.4, "carbs": 5, "fat": 1,
        "fiber": 0, "sugar": 5, "unit": "ml", "serving_size": 100,
        "category": "dairy"
    },
    "cheese": {
        "calories": 402, "protein": 25, "carbs": 1.3, "fat": 33,
        "fiber": 0, "sugar": 0.4, "unit": "g", "serving_size": 100,
        "category": "dairy"
    },
    "yogurt": {
        "calories": 59, "protein": 3.5, "carbs": 4.7, "fat": 3.3,
        "fiber": 0, "sugar": 4.7, "unit": "ml", "serving_size": 100,
        "category": "dairy"
    },
    "butter": {
        "calories": 717, "protein": 0.9, "carbs": 0.1, "fat": 81,
        "fiber": 0, "sugar": 0.1, "unit": "g", "serving_size": 100,
        "category": "dairy"
    },
    "egg": {
        "calories": 155, "protein": 13, "carbs": 1.1, "fat": 11,
        "fiber": 0, "sugar": 0.4, "unit": "piece", "serving_size": 1,
        "category": "dairy"
    },
    
    # Grains
    "rice": {
        "calories": 130, "protein": 2.7, "carbs": 28, "fat": 0.3,
        "fiber": 0.4, "sugar": 0.1, "unit": "g", "serving_size": 100,
        "category": "grains"
    },
    "oats": {
        "calories": 389, "protein": 16.9, "carbs": 66, "fat": 6.9,
        "fiber": 10.6, "sugar": 0, "unit": "g", "serving_size": 100,
        "category": "grains"
    },
    "quinoa": {
        "calories": 120, "protein": 4.1, "carbs": 21.3, "fat": 1.9,
        "fiber": 2.8, "sugar": 0.9, "unit": "g", "serving_size": 100,
        "category": "grains"
    },
    "barley": {
        "calories": 354, "protein": 12.5, "carbs": 73.5, "fat": 2.3,
        "fiber": 17.3, "sugar": 0.8, "unit": "g", "serving_size": 100,
        "category": "grains"
    },
    "bread": {
        "calories": 265, "protein": 9, "carbs": 49, "fat": 3.2,
        "fiber": 2.7, "sugar": 5, "unit": "slice", "serving_size": 1,
        "category": "grains"
    }
}

RECIPES_DIR = "saved_recipes"

class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = {}
        self.total_nutrition = {
            "calories": 0, "protein": 0, "carbs": 0,
            "fat": 0, "fiber": 0, "sugar": 0
        }
        self.servings = 1
    
    def add_ingredient(self, ingredient, amount):
        if ingredient in NUTRITION_DATA:
            self.ingredients[ingredient] = amount
            self._calculate_nutrition(ingredient, amount)
    
    def remove_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            amount = self.ingredients[ingredient]
            self._subtract_nutrition(ingredient, amount)
            del self.ingredients[ingredient]
    
    def _calculate_nutrition(self, ingredient, amount):
        data = NUTRITION_DATA[ingredient]
        multiplier = amount / data["serving_size"]
        
        for nutrient in self.total_nutrition:
            if nutrient in data:
                self.total_nutrition[nutrient] += data[nutrient] * multiplier
    
    def _subtract_nutrition(self, ingredient, amount):
        data = NUTRITION_DATA[ingredient]
        multiplier = amount / data["serving_size"]
        
        for nutrient in self.total_nutrition:
            if nutrient in data:
                self.total_nutrition[nutrient] -= data[nutrient] * multiplier
    
    def set_servings(self, servings):
        self.servings = max(1, servings)
    
    def get_nutrition_info(self, per_serving=False):
        nutrition = {}
        divider = self.servings if per_serving else 1
        
        for nutrient, value in self.total_nutrition.items():
            nutrition[nutrient] = round(value / divider, 1)
        
        return nutrition
    
    def get_ingredients_by_category(self):
        categorized = {}
        for ingredient, amount in self.ingredients.items():
            category = NUTRITION_DATA[ingredient]["category"]
            if category not in categorized:
                categorized[category] = []
            categorized[category].append((ingredient, amount))
        return categorized
    
    def clear(self):
        self.ingredients.clear()
        for key in self.total_nutrition:
            self.total_nutrition[key] = 0
        self.servings = 1

class RecipeCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Recipe Nutrition Calculator")
        self.root.geometry("700x700")
        self.root.configure(bg=COLORS["background"])
        
        self.configure_styles()
        self.recipe = Recipe("New Recipe")
        self.setup_gui()
    
    def configure_styles(self):
        style = ttk.Style()
        style.configure("Main.TFrame", background=COLORS["background"])
        style.configure("Card.TFrame", background="white", relief="raised")
        style.configure("Title.TLabel", 
                       font=("Helvetica", 16, "bold"),
                       foreground=COLORS["primary"])
        style.configure("Subtitle.TLabel",
                       font=("Helvetica", 12),
                       foreground=COLORS["text"])
        style.configure("Primary.TButton",
                       background=COLORS["primary"],
                       foreground="Black")
        style.configure("Success.TButton",
                       background=COLORS["success"],
                       foreground="Black")
    
    def setup_gui(self):
        # Main container
        main_container = ttk.Frame(self.root, style="Main.TFrame", padding=PADDING["medium"])
        main_container.pack(fill="both", expand=True)
        
        # Title
        title_label = ttk.Label(main_container, 
                              text="Recipe Nutrition Calculator",
                              style="Title.TLabel")
        title_label.pack(pady=PADDING["medium"])
        
        # Recipe Name Frame
        name_frame = ttk.Frame(main_container, style="Card.TFrame", padding=PADDING["medium"])
        name_frame.pack(fill="x", pady=PADDING["small"])
        
        ttk.Label(name_frame, text="Recipe Name:", style="Subtitle.TLabel").pack(side="left")
        self.recipe_name = ttk.Entry(name_frame, width=40)
        self.recipe_name.pack(side="left", padx=PADDING["small"])
        
        # Servings Frame
        servings_frame = ttk.Frame(main_container, style="Card.TFrame", padding=PADDING["medium"])
        servings_frame.pack(fill="x", pady=PADDING["small"])
        
        ttk.Label(servings_frame, text="Servings:", style="Subtitle.TLabel").pack(side="left")
        self.servings_var = tk.StringVar(value="1")
        servings_spinbox = ttk.Spinbox(servings_frame, from_=1, to=50, width=5,
                                     textvariable=self.servings_var,
                                     command=self.update_servings)
        servings_spinbox.pack(side="left", padx=PADDING["small"])
        
        # Ingredient Input Frame
        input_frame = ttk.LabelFrame(main_container, text="Add Ingredient", padding=PADDING["medium"])
        input_frame.pack(fill="x", pady=PADDING["small"])
        
        # Category filter
        ttk.Label(input_frame, text="Category:").grid(row=0, column=0)
        self.category_var = tk.StringVar()
        categories = sorted(set(data["category"] for data in NUTRITION_DATA.values()))
        category_cb = ttk.Combobox(input_frame, textvariable=self.category_var, values=["All"] + categories)
        category_cb.grid(row=0, column=1, padx=PADDING["small"])
        category_cb.bind("<<ComboboxSelected>>", self.filter_ingredients)
        
        # Ingredient selection
        ttk.Label(input_frame, text="Ingredient:").grid(row=0, column=2)
        self.ingredient_var = tk.StringVar()
        self.ingredient_cb = ttk.Combobox(input_frame, textvariable=self.ingredient_var)
        self.ingredient_cb['values'] = sorted(NUTRITION_DATA.keys())
        self.ingredient_cb.grid(row=0, column=3, padx=PADDING["small"])
        
        # Amount input
        ttk.Label(input_frame, text="Amount:").grid(row=0, column=4)
        self.amount_var = tk.StringVar()
        amount_entry = ttk.Entry(input_frame, textvariable=self.amount_var, width=10)
        amount_entry.grid(row=0, column=5, padx=PADDING["small"])
        
        # Add button
        ttk.Button(input_frame, text="Add", style="Primary.TButton",
                  command=self.add_ingredient).grid(row=0, column=6, padx=PADDING["small"])
        
        # Ingredients List
        list_frame = ttk.LabelFrame(main_container, text="Ingredients", padding=PADDING["medium"])
        list_frame.pack(fill="both", expand=True, pady=PADDING["small"])
        
        ingredients_frame = ttk.Frame(list_frame)
        ingredients_frame.pack(fill="both", expand=True)
        
        self.ingredients_text = tk.Text(ingredients_frame, height=10, width=50)
        scrollbar = ttk.Scrollbar(ingredients_frame, orient="vertical", command=self.ingredients_text.yview)
        self.ingredients_text.configure(yscrollcommand=scrollbar.set)
        
        self.ingredients_text.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Nutrition Display
        nutrition_frame = ttk.LabelFrame(main_container, text="Nutrition Information", padding=PADDING["medium"])
        nutrition_frame.pack(fill="x", pady=PADDING["small"])
        
        self.nutrition_labels = {}
        nutrients = ["calories", "protein", "carbs", "fat", "fiber", "sugar"]
        for i, nutrient in enumerate(nutrients):
            row = i // 3
            col = i % 3
            ttk.Label(nutrition_frame, text=f"{nutrient.title()}:").grid(row=row, column=col*2, sticky="w", padx=PADDING["small"])
            self.nutrition_labels[nutrient] = ttk.Label(nutrition_frame, text="0")
            self.nutrition_labels[nutrient].grid(row=row, column=col*2+1, sticky="w", padx=PADDING["small"])
        
        # Buttons Frame
        button_frame = ttk.Frame(main_container, padding=PADDING["medium"])
        button_frame.pack(fill="x")
        
        ttk.Button(button_frame, text="Clear Recipe", command=self.clear_recipe).pack(side="left", padx=PADDING["small"])
        ttk.Button(button_frame, text="Save Recipe", style="Success.TButton",
                  command=self.save_recipe).pack(side="left", padx=PADDING["small"])
        ttk.Button(button_frame, text="Load Recipe", command=self.load_recipe).pack(side="left", padx=PADDING["small"])
    
    def filter_ingredients(self, event=None):
        category = self.category_var.get()
        if category == "All":
            self.ingredient_cb['values'] = sorted(NUTRITION_DATA.keys())
        else:
            filtered = [ing for ing, data in NUTRITION_DATA.items() if data["category"] == category]
            self.ingredient_cb['values'] = sorted(filtered)
    
    def update_servings(self):
        try:
            servings = int(self.servings_var.get())
            self.recipe.set_servings(servings)
            self.update_display()
        except ValueError:
            self.servings_var.set("1")
    
    def add_ingredient(self):
        ingredient = self.ingredient_var.get()
        try:
            amount = float(self.amount_var.get())
            if amount <= 0:
                raise ValueError("Amount must be greater than 0")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return
        
        if ingredient not in NUTRITION_DATA:
            messagebox.showerror("Error", "Please select a valid ingredient")
            return
        
        self.recipe.add_ingredient(ingredient, amount)
        self.update_display()
        self.amount_var.set("")
    
    def update_display(self):
        # Update ingredients list
        self.ingredients_text.delete(1.0, tk.END)
        categorized = self.recipe.get_ingredients_by_category()
        
        for category, ingredients in sorted(categorized.items()):
            self.ingredients_text.insert(tk.END, f"\n{category.title()}:\n")
            for ingredient, amount in sorted(ingredients):
                unit = NUTRITION_DATA[ingredient]["unit"]
                self.ingredients_text.insert(tk.END, f"  • {ingredient}: {amount} {unit}\n")
        
        # Update nutrition info
        nutrition = self.recipe.get_nutrition_info(per_serving=True)
        for nutrient, value in nutrition.items():
            unit = "g" if nutrient != "calories" else "kcal"
            self.nutrition_labels[nutrient].config(text=f"{value} {unit}")
    
    def clear_recipe(self):
        if messagebox.askyesno("Clear Recipe", "Are you sure you want to clear the current recipe?"):
            self.recipe.clear()
            self.recipe_name.delete(0, tk.END)
            self.ingredients_text.delete(1.0, tk.END)
            self.servings_var.set("1")
            self.update_display()
    
    def save_recipe(self):
        name = self.recipe_name.get()
        if not name:
            messagebox.showerror("Error", "Please enter a recipe name")
            return
        
        if not os.path.exists(RECIPES_DIR):
            os.makedirs(RECIPES_DIR)
        
        try:
            recipe_data = {
                "name": name,
                "ingredients": self.recipe.ingredients,
                "nutrition": self.recipe.get_nutrition_info()
            }
            filename = f"{RECIPES_DIR}/{name.lower().replace(' ', '_')}.json"
            with open(filename, 'w') as f:
                json.dump(recipe_data, f, indent=2)
            messagebox.showinfo("Success", f"Recipe saved to {filename}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save recipe: {str(e)}")
    
    def load_recipe(self):
        if not os.path.exists(RECIPES_DIR):
            os.makedirs(RECIPES_DIR)
            
        filename = filedialog.askopenfilename(
            initialdir=RECIPES_DIR,
            title="Select Recipe",
            filetypes=(("JSON files", "*.json"), ("All files", "*.*"))
        )
        
        if filename:
            try:
                with open(filename, 'r') as f:
                    recipe_data = json.load(f)
                
                self.recipe_name.delete(0, tk.END)
                self.recipe_name.insert(0, recipe_data["name"])
                
                self.recipe.clear()
                for ingredient, amount in recipe_data["ingredients"].items():
                    self.recipe.add_ingredient(ingredient, amount)
                
                self.update_display()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load recipe: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeCalculatorApp(root)
    root.mainloop()