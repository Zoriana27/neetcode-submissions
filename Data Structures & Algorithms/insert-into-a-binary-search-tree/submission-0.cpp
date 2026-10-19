/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        TreeNode* temp = root;
        if(temp == nullptr){
            temp = new TreeNode();
            temp->val = val;
            temp->right = nullptr;
            temp->left = nullptr;
            return temp;
        }
        if(val < temp->val){
            temp->left = insertIntoBST(temp->left, val);
        }
        else if(val > temp->val){
            temp->right = insertIntoBST(temp->right, val);
        }
        return root;
        
    }
};