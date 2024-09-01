Redis which is a popular fast in-memory database uses many optimization techniques to speed up the retrievals, one of them is the concept of using skip lists, in simple terms skip lists are augmented linked lists for faster search, as you can skip through portions of the list which don't contain the data you're looking for.

The data is stored in the form of linked lists with an additional information pertaining to an abstract concept of `lanes`, each node contains 3 data members: `value`, `next` and `down` and the data has a layer of abstraction called lanes, there are 2 types of lanes: normal lane, which is the original linked list and express lanes which are the abstractions, here is a representation:

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/sxdg5wofgsjy6avygfzc.png)
// Image courtesy: https://www.geeksforgeeks.org/skip-list/

The code for searching in a linked list is really neat:
```
SkipNode* search(int key) [
    curr = head;
    while(curr != nullptr) {
        while(curr -> right != nullptr && curr -> right -> value <= key) {
            curr = curr -> right;
        }
        if(curr -> val == key) break;
        curr = curr -> down;
    }
]
```