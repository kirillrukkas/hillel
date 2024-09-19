XPath локатори:
1. 
//button[text()='Login']
2. 
//input[@name='email']
3. 
//input[@name='password']
4. 
//a[@href='/register']
5. 
//div[@class='header']
6. 
//span[text()='Welcome']
7. 
//form[@id='loginForm']
8. 
//input[@type='submit']
9. 
//label[@for='email']
10. 
//label[@for='password']
11. 
//footer//a[text()='Contact']
12. 
//nav//ul//li//a[@href='/home']
13. 
//section[@id='features']//h2
14. 
//div[@class='container']//p
15. 
//header//img[@alt='Logo']
16. 
//aside//ul//li//a[text()='Profile']
17. 
//main//h1
18. 
//article//h3
19. 
//div[@class='content']//a[@href='/about']
20. 
//form[@id='searchForm']//input[@type='text']
21. 
//table[@id='dataTable']//tr[1]//td[2]
22. 
//div[@class='sidebar']//ul//li[3]
23. 
//button[@class='btn-primary']
24. 
//input[@placeholder='Search']
25. 
//div[@class='footer']//p[text()='© 2024']

--------------------------------------------

CSS локатори:
1. 
button:contains('Login')
2. 
input[name='email']
3. 
input[name='password']
4. 
a[href='/register']
5. 
div.header
6. 
span:contains('Welcome')
7. 
form#loginForm
8. 
input[type='submit']
9. 
label[for='email']
10. 
label[for='password']
11. 
footer a:contains('Contact')
12. 
nav ul li a[href='/home']
13. 
section#features h2
14. 
div.container p
15. 
header img[alt='Logo']
16. 
aside ul li a:contains('Profile')
17. 
main h1
18. 
article h3
19. 
div.content a[href='/about']
20. 
form#searchForm input[type='text']
21. 
table#dataTable tr:first-child td:nth-child(2)
22. 
div.sidebar ul li:nth-child(3)
23. 
button.btn-primary
24. 
input[placeholder='Search']
25. 
div.footer p:contains('© 2024')