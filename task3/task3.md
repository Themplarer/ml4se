Я использовал обученную модель из [репозитория](https://github.com/tech-srl/code2vec).
Для проверки нужны фрагменты кода на Java.

# Фрагмент 1
```java
int f(int n) {
    if (n == 0) {
        return 1; 
    } else {
        return n * f(n-1);
    }
}
```

Результирующий вектор - 
`[
0.258571
0.159237
0.102514
0.082340
0.060176
0.059877
0.042954
0.041031
0.033209
0.029109
]`

<details>
    <summary>Полный вывод</summary>

    Original name:  f
        (0.472304) predicted: ['m']                                                                         
        (0.174314) predicted: ['fact']                                                                      
        (0.101179) predicted: ['factorial']                                                                 
        (0.095780) predicted: ['faculty']                                                                   
        (0.067391) predicted: ['get', 'n']                                                                  
        (0.038753) predicted: ['get', 'result', 'score']                                                    
        (0.013598) predicted: ['is', 'power', 'of']                                                         
        (0.013113) predicted: ['digit', 'count']                                                            
        (0.012808) predicted: ['comb']                                                                      
        (0.010760) predicted: ['get', 'in']                                                                 
    Attention:                                                                                                  
    0.258571        context: n,(NameExpr0)^(BinaryExpr:times)_(MethodCallExpr1)_(BinaryExpr:minus)_(NameExpr0),n
    0.159237        context: 1,(IntegerLiteralExpr1)^(BinaryExpr:minus1)^(MethodCallExpr)_(NameExpr2),f         
    0.102514        context: int,(PrimitiveType0)^(MethodDeclaration)_(NameExpr1),METHOD_NAME
    0.082340        context: 0,(IntegerLiteralExpr1)^(BinaryExpr:equals)^(IfStmt)_(BlockStmt)_(ReturnStmt)_(IntegerLiteralExpr0),1
    0.060176        context: METHOD_NAME,(NameExpr1)^(MethodDeclaration)_(BlockStmt)_(IfStmt)_(BlockStmt)_(ReturnStmt)_(BinaryExpr:times)_(NameExpr0),n
    0.059877        context: int,(PrimitiveType1)^(Parameter)^(MethodDeclaration)_(BlockStmt)_(IfStmt)_(BlockStmt)_(ReturnStmt)_(IntegerLiteralExpr0),1
    0.042954        context: int,(PrimitiveType0)^(MethodDeclaration)_(Parameter)_(VariableDeclaratorId0),n
    0.041031        context: n,(VariableDeclaratorId0)^(Parameter)^(MethodDeclaration)_(BlockStmt)_(IfStmt)_(BlockStmt)_(ReturnStmt)_(BinaryExpr:times)_(NameExpr0),n
    0.033209        context: int,(PrimitiveType0)^(MethodDeclaration)_(Parameter)_(PrimitiveType1),int
    0.029109        context: n,(VariableDeclaratorId0)^(Parameter)_(PrimitiveType1),int
</details>

# Фрагмент 2
```java
int f(int n) {
    if (n == 0) {
        return 1; 
    }
    
    return f(n-1) * n;
}
```

Результирующий вектор - 
`[
0.185362
0.162145
0.114916
0.073981
0.071805
0.059422
0.054705
0.048954
0.043211
0.030999
]`

<details>
    <summary>Полный вывод</summary>

    Original name:  f
        (0.709648) predicted: ['m']                                                                                                                           
        (0.153206) predicted: ['get', 'f']                                                                                                                    
        (0.029845) predicted: ['faculty']                                                                                                                     
        (0.025613) predicted: ['n']                                                                                                                           
        (0.021773) predicted: ['neg']                                                                                                                         
        (0.017769) predicted: ['factorial']                                                                                                                   
        (0.013131) predicted: ['method']                                                                                                                      
        (0.009915) predicted: ['goo']                                                                                                                         
        (0.009796) predicted: ['compute']                                                                                                                     
        (0.009304) predicted: ['foo']

    Attention:                                                                                                                                                    
    0.185362        context: int,(PrimitiveType1)^(Parameter)^(MethodDeclaration)_(BlockStmt)_(ReturnStmt)_(BinaryExpr:times)_(MethodCallExpr0)_(NameExpr2),f     
    0.162145        context: int,(PrimitiveType1)^(Parameter)^(MethodDeclaration)_(BlockStmt)_(ReturnStmt)_(BinaryExpr:times)_(NameExpr1),n                       
    0.114916        context: 1,(IntegerLiteralExpr1)^(BinaryExpr:minus1)^(MethodCallExpr)_(NameExpr2),f                                                           
    0.073981        context: int,(PrimitiveType0)^(MethodDeclaration)_(NameExpr1),METHOD_NAME                                                                     
    0.071805        context: n,(VariableDeclaratorId0)^(Parameter)^(MethodDeclaration)_(BlockStmt)_(ReturnStmt)_(BinaryExpr:times)_(MethodCallExpr0)_(NameExpr2),f
    0.059422        context: 0,(IntegerLiteralExpr1)^(BinaryExpr:equals)^(IfStmt)_(BlockStmt)_(ReturnStmt)_(IntegerLiteralExpr0),1                                
    0.054705        context: n,(VariableDeclaratorId0)^(Parameter)^(MethodDeclaration)_(BlockStmt)_(ReturnStmt)_(BinaryExpr:times)_(NameExpr1),n                  
    0.048954        context: METHOD_NAME,(NameExpr1)^(MethodDeclaration)_(BlockStmt)_(ReturnStmt)_(BinaryExpr:times)_(MethodCallExpr0)_(NameExpr2),f              
    0.043211        context: int,(PrimitiveType1)^(Parameter)^(MethodDeclaration)_(BlockStmt)_(IfStmt)_(BlockStmt)_(ReturnStmt)_(IntegerLiteralExpr0),1           
    0.030999        context: int,(PrimitiveType0)^(MethodDeclaration)_(Parameter)_(VariableDeclaratorId0),n
</details>