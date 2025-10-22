from infrastructure.apis.product import ProductAPIs

class Product:

    def product_category_count_avgrating(self):
        """Counts the type the product"""
        try:
            category_dict={}
            product_list = ProductAPIs().get_products_list()
            for product in product_list.get("products"):
                category = product.get("category")
                rating = product.get("rating")
                # Initialize the category if it doesn't exist
                if category not in category_dict:
                    category_dict[category] = {"count": 0, "total_rating": 0.0}
                category_dict[category]["count"]+=1
                category_dict[category]["total_rating"]+=rating
            result=[]
            print("category_dict")
            print(category_dict)
            for key, value in category_dict.items():
                category_dict[key]["avg_rating"] = value["total_rating"]/value["count"]
                result.append({"Category":key, 
                               "count":value["count"], 
                               "avg_rating":value["avg_rating"]})
            return result
        except Exception as e:
            return None


