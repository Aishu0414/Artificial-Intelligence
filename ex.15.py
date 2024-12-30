class DecisionTree:
    def __init__(self, max_depth=None):
        self.max_depth = max_depth
        self.tree = None

    def gini_index(self, labels):
        """Calculate the Gini index for a list of labels."""
        unique_labels = set(labels)
        gini = 1.0
        for label in unique_labels:
            p = labels.count(label) / len(labels)
            gini -= p ** 2
        return gini

    def best_split(self, data):
        """Find the best feature to split on based on Gini index."""
        best_gini = float('inf')
        best_split = None
        best_left = None
        best_right = None
        n_features = len(data[0]) - 1  # Last column is the label

        # Try splitting on each feature
        for feature in range(n_features):
            # Sort the data by the feature value
            sorted_data = sorted(data, key=lambda x: x[feature])

            left_labels = []
            right_labels = [row[-1] for row in sorted_data]  # Initialize with all labels on the right

            for i in range(1, len(sorted_data)):  # Avoid splitting at the same point
                left_labels.append(sorted_data[i-1][-1])
                right_labels.remove(sorted_data[i-1][-1])

                # Calculate the Gini index for the split
                if sorted_data[i][feature] != sorted_data[i-1][feature]:  # Check for a change in feature value
                    gini = (len(left_labels) / len(sorted_data)) * self.gini_index(left_labels) + \
                           (len(right_labels) / len(sorted_data)) * self.gini_index(right_labels)
                    if gini < best_gini:
                        best_gini = gini
                        best_split = (feature, sorted_data[i][feature])
                        best_left = left_labels
                        best_right = right_labels
        return best_split, best_left, best_right

    def build_tree(self, data, depth=0):
        """Recursively build the decision tree."""
        labels = [row[-1] for row in data]
        
        # If all labels are the same or max depth is reached, return a leaf
        if len(set(labels)) == 1 or (self.max_depth and depth >= self.max_depth):
            return labels[0]

        # Find the best split
        split, left_labels, right_labels = self.best_split(data)
        if split is None:  # If no valid split, return majority class
            return max(set(labels), key=labels.count)

        # Ensure both left and right datasets are non-empty
        left_data = [row for row in data if row[split[0]] <= split[1]]
        right_data = [row for row in data if row[split[0]] > split[1]]

        # Check if any of the split sides are empty
        if not left_data or not right_data:
            return max(set(labels), key=labels.count)  # Return majority class if no valid split

        left_tree = self.build_tree(left_data, depth + 1)
        right_tree = self.build_tree(right_data, depth + 1)

        return {"split": split, "left": left_tree, "right": right_tree}

    def fit(self, data):
        """Train the decision tree."""
        self.tree = self.build_tree(data)

    def predict(self, row, node=None):
        """Make a prediction using the trained decision tree."""
        if node is None:
            node = self.tree
        
        if isinstance(node, dict):  # Not a leaf node
            if row[node['split'][0]] <= node['split'][1]:
                return self.predict(row, node['left'])
            else:
                return self.predict(row, node['right'])
        else:
            return node  # Leaf node, return the label

# Sample dataset (fruit classification)
# Format: [weight, color, label] where label: 0 for apple, 1 for orange
data = [
    [150, 'red', 0],  # apple
    [130, 'red', 0],  # apple
    [180, 'orange', 1],  # orange
    [160, 'orange', 1],  # orange
    [170, 'red', 0],  # apple
    [140, 'orange', 1],  # orange
]

# Train decision tree
tree = DecisionTree(max_depth=3)
tree.fit(data)

# Test prediction
test_row = [160, 'red']  # A red fruit weighing 160g
prediction = tree.predict(test_row)
print(f"Prediction for {test_row}: {'Apple' if prediction == 0 else 'Orange'}")
