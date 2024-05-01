# Input Expression = 2 + 3 * 4


           
           Expression
            /   |   \
         Term AddOp Expression
          |     |        \
       Factor  +         Term
         |               /   |   \
      Primary        Factor MulOp Term
         |            |        |     \
      Number         Primary   *   Factor
         |            |              |
         2          Number         Primary
                      |              |     
                      3            Number
                                     |
                                     4

