environment = "development"

if environment != "production":
    raise ValueError("Production environment required")