var insertIntoBST = function(root, val) {
    let current_node = root
    if (current_node == null){
        return new TreeNode(val)
    }
    while (current_node != null){
        if (val < current_node.val){
            if (current_node.left != null) {
                current_node = current_node.left
            }else {
                current_node.left = new TreeNode(val)
                return root
            }
        } else {
            if (current_node.right != null) {
                current_node = current_node.right
            } else {
                current_node.right = new TreeNode(val)
                return root
            }
        }
    }
};