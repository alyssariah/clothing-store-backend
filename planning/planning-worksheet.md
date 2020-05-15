# Project Overview

## Project Schedule
|  Day | Deliverable | Status
|---|---| ---|
|Day 1| Project Worsheet & Django Authentication | Complete
|Day 2|	Django Api and Deployment | Complete
|Day 3| React Header, LogIn, SignUp, and Home | Complete
|Day 4| React Clothing List, Full Details, Shopping Cart| Complete
|Day 5| React Shopping Cart, Confirmation Page, and My Orders| Complete
|Day 6| React Profile, Search Bar, and Touch Ups | Complete
|Day 7| Present | Incomplete


## Project Description

This project is a mock up of a clothing store. It has a navigation bar with a drop down menu for items in the store and a search bar. It also has a login option and a shopping cart above the navigation bar. The welcome page features popular items and a user can click on a category in the navbar to be redirected to that page. When a user clicks on an item, they are redirected to a page that displays full item details and an option to add it to their cart. The shopping cart displays all the added items and provides the option to checkout. When a user logs in, they can see their previous orders and the items they saved in their cart. This project is made with a react frontend and a django backend with postgresql.
Inspirations:

https://www.downeastbasics.com/
https://www.rei.com/
https://www.nike.com/w/womens-pants-tights-2kq19z5e1x6

## Project Links
frontend: https://github.com/alyssariah/clothing-store-frontend/

backend: https://github.com/alyssariah/clothing-store-backend/

## Wireframes

This link includes all my wireframes for home page, login page, profile page, past orders page, item full detail page, and checkout page

https://www.figma.com/file/EfU7YZmkxe52rxeQ8mBHpF/Clothing-Store?node-id=0%3A1



## React Architecture
https://docs.google.com/drawings/d/1qn8AAY4Hh9_uGAHRzQ76rZyzVBdHQJY96QbUxbzr_eo/edit

## Database Models
```
class Product(models.Model):
	name = models.CharField(max_length=100)
	pictureUrl = models.CharField(max_length=255)
	price = models.IntegerField()
	qty = models.IntegerField()
	size = models.CharField(max_length=100, choices=[('XS', 'XS'), ('S', 'S'),('M', 'M'), ('L', 'L'), ('XL', 'XL'),])
	description = models.TextField(blank=True)
	category = models.CharField(max_length=100, choices=[('Dresses', 'Dresses'), ('Tops', 'Tops'),('Bottoms', 'Bottoms'), ('Accessories', 'Accessories'), ('Sale', 'Sale'),])
class Order(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ManyToManyField(Product, related_name='products')
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name + ' ' + self.price

```


## MVP/PostMVP

The functionality will then be divided into two separate lists: MPV and PostMVP.
 com
#### MVP

MVP List:
- [x] Set up Django Project with correct structure
- [x] Set up authentication for users
- [x] Make models, serializers, views, urls for api
- [x] Seed postgres with clothing data
- [x] Deploy to heroku and syncdb
- [x] Set up React app
- [x] App Routes
- [x] Header
- [x] Login and Sign up
- [x] Home Page
- [x] Clothing List
- [x] Full Detail Page
- [x] Shopping Cart
- [x] Checkout Item
- [x] Confirmation Page
- [x] My Orders



#### PostMVP
PostMVP List:
- [x] Profile
- [x] Search bar
- [x] Hover effect over items
- [ ] Responsive
- [ ] PayPal



## Time/Priority Matrix

Based on the initial logic defined in the previous sections try and breakdown the logic further into functional components, and by that we mean functions.  Try and capture what logic would need to be defined if the game was broken down into the following categories.

Time frames are also key in the development cycle.  You have limited time to code all phases of the game.  Your estimates can then be used to evalute game possibilities based on time needed and the actual time you have before game must be submitted. It's always best to pad the time by a few hours so that you account for the unknown so add and additional hour or two to each component to play it safe.

| Task | Priority | Estimated Time | Time Invetsted | Actual Time |
| --- | :---: |  :---: | :---: | :---: |
| Set up Django | H | 1hr | .5hr | hr|
| Authentication | H | 2hr | 1hr | hr|
| API | H | 4hr | 12hr | hr|
| Seed | H | 3hr| 2hr | hr |
| Deploy to Heroku | H | 2hr | 2hr | hr|
| Set up React App | H | 1hr| 1hr | hr |
| App Routes | H | 1hr | 1hr | hr|
| Header | H | 3hr | 2hr | hr|
| Log In | H | 1hr | 1hr | hr|
| Sign Up | H | 1hr | 1hr | hr|
| Home Page | H | 2hr | 2hr | hr|
| Clothing List | H | 4hr | 2hr | hr|
| Full Detail Page | H | 4hr | 3hr | hr|
| Shopping Cart | H | 4hr | 6hr | hr|
| Checkout Item | H | 1hr | 1hr | hr|
| Confirmation Page | H | 1hr | 1hr | hr|
| My Orders | H | 4hr | 3hr | hr|
| Profile | L | 1hr | 2hr | hr|
| Bugs | H | 4hr | 1hr | hr|
| Search bar | L | 4hr | 2hr | hr|
| Extra CSS | L | 5hr | 4hr | hr|
| Hover effect | L | 1hr | 1hr | hr|
| PayPal | L | 6hr | 2hr | hr|
| Responsive | L | 3hr | 6hr | hr|
| Total |  | 50hrs| 60hrs | 60hrs |

## Additional Libraries
    MDBootstrap
    

## Code Snippet
Table used in the shopping cart
```
           {
            'img': <img src={item.product.pictureUrl} alt="" className="img-fluid z-depth-0" style={{height: '80px', width: '100px'}}/>,
            'product': [<h5 className="mt-3" key={new Date().getDate + 1}><strong>{item.product.name}</strong></h5>, <p key={new
              Date().getDate} className="text-muted"></p>],
            'size': <h5 className="mt-3" >{item.product.category === 'Dresses' || item.product.category === 'Tops' || item.product.category === 'Sale'? item.size: '--'}</h5>,
            'price': <h5 className="mt-3" >${item.product.price * item.qty}.00</h5>,
            'qty': <h5 className="mt-3" ><input style={{width: '2.5vw', textAlign: 'center'}}class="quantity" value={item.qty}  min='1' onChange={handleQty} type="number"/></h5>,
            'button':
            <MDBTooltip placement="top">
                <MDBBtn className='mt-3' color="white" size="sm" onClick={()=>{removeItem(item.id)}}>
                    X
                </MDBBtn>
                <div>Remove item</div>
            </MDBTooltip> 
          }

```

## Issues and Resolutions
 Use this section to list of all major issues encountered and their resolution.

#### SAMPLE.....
**ERROR**: app.js:34 Uncaught SyntaxError: Unexpected identifier
**RESOLUTION**: Missing comma after first object in sources {} object
