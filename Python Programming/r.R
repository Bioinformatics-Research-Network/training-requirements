```{r}
# Load the reticulate package
library(reticulate)

# Check if reticulate is loaded
if ("reticulate" %in% loadedNamespaces()) {
  print("reticulate is loaded correctly")
} else {
  print("reticulate is not loaded correctly")
}


# Set the Python path with escaped backslashes or use forward slashes
use_python("C:\\Users\\abdoj\\AppData\\Local\\Programs\\Python\\Python312\\python.exe", required = TRUE)


# Run the Python script using source_python
source_python("C:/Users/abdoj/OneDrive - UGent/Desktop/summer/skill-assessments/Python Programming/tic_tac_toe.py")
```

