# Eatery --- Knowledge Base

**Dataset type:** Fictional demonstration data for a Retrieval-Augmented
Generation (RAG) mini project\
**Version:** 1.0\
**Primary use:** Restaurant customer-support assistant\
**Currency:** Pakistani Rupees (PKR)

> IMPORTANT: Eatery and all facts in this document are
> fictional sample data created for software testing. The founding
> story, people, branches, addresses/areas, menu, prices, timings, and
> policies are not verified real-world claims. Replace them with
> verified information before using this assistant with real customers.

## 1. Restaurant Overview

**Restaurant name:** Eatery\
**Short name:** Eatery\
**Business type:** Casual dining restaurant and takeaway\
**Cuisine:** Pakistani comfort food, pasta, burgers, sandwiches, and
fast food\
**Founded:** 2018\
**Founder:** Salman Ahmed (fictional)\
**Head office:** Gulshan-e-Iqbal, Karachi, Pakistan (fictional)\
**Brand promise:** Familiar comfort food, generous portions, consistent
preparation, and friendly service.

Eatery is a fictional Karachi-based casual dining
brand. It began as a small pasta and takeaway counter and gradually
expanded into a multi-branch restaurant. The concept combines pasta
dishes with popular Pakistani and fast-food favourites so that customers
can choose from both local comfort food and casual international-style
meals.

The restaurant's sample customer-support assistant should answer
questions using this knowledge base and the live menu tool where
appropriate. It must not invent missing facts. If a detail is not stated
in the knowledge base, it should say that the information is currently
unavailable and offer to confirm it with the restaurant.

## 2. Founding Story and History

Eatery was founded in **2018** by **Salman Ahmed**, a
fictional food entrepreneur from Karachi.

The idea began when Salman noticed that many nearby takeaway restaurants
focused on only one category of food. He wanted to create a small,
approachable place where customers could order pasta as well as familiar
local favourites such as chicken dishes, burgers, and sandwiches.

The first outlet was a compact takeaway counter in **Gulshan-e-Iqbal,
Karachi**. Its early menu focused on a few pasta recipes, a chicken
burger, and sandwiches. The restaurant gradually gained repeat customers
through word of mouth. As demand increased, the business expanded its
menu and opened additional outlets in other Karachi neighbourhoods.

### Milestones

-   **2018 --- First outlet opened:** The first Eatery counter
    opened in Gulshan-e-Iqbal, Karachi.
-   **2019 --- Menu expansion:** Burgers, sandwiches, and selected
    Pakistani meals were added.
-   **2021 --- Second outlet:** A branch opened in North Nazimabad to
    serve customers in the northern part of Karachi.
-   **2022 --- Delivery-focused expansion:** The PECHS outlet opened
    with a focus on takeaway and delivery orders.
-   **2024 --- Further growth:** The DHA and Bahria Town outlets were
    added to the fictional branch network.
-   **2025 --- Standardized customer support:** The restaurant
    introduced a centralized support process for menu questions, order
    validation, and complaints.

These dates and milestones are fictional and are included to provide
useful historical facts for RAG retrieval.

## 3. Branch Directory

The fictional restaurant has five branches, all located in Karachi,
Pakistan.

  --------------------------------------------------------------------------------------
  Branch ID      Branch name       Area              Address description  Main service
                                                                          focus
  -------------- ----------------- ----------------- -------------------- --------------
  ET-GUL         Gulshan-e-Iqbal   Gulshan-e-Iqbal   Main commercial area Dine-in,
                 Branch                              near University      takeaway,
                                                     Road,                delivery
                                                     Gulshan-e-Iqbal,     
                                                     Karachi              

  ET-NNZ         North Nazimabad   North Nazimabad   Block H commercial   Dine-in,
                 Branch                              area, North          takeaway,
                                                     Nazimabad, Karachi   delivery

  ET-PECHS       PECHS Branch      PECHS             Shahrah-e-Quaideen   Takeaway and
                                                     vicinity, PECHS,     delivery
                                                     Karachi              

  ET-DHA         DHA Branch        DHA Phase 6       Commercial area near Dine-in,
                                                     Bukhari Commercial,  takeaway,
                                                     Karachi              delivery

  ET-BT          Bahria Town       Bahria Town       Main commercial      Dine-in,
                 Branch            Karachi           zone, Bahria Town    takeaway
                                                     Karachi              
  --------------------------------------------------------------------------------------

**Branch-count answer:** Eatery has five fictional
branches in this dataset.

### Branch lookup facts

-   The original branch is **Gulshan-e-Iqbal (ET-GUL)**.
-   The North Nazimabad branch is **ET-NNZ**.
-   The PECHS branch is **ET-PECHS**.
-   The DHA branch is **ET-DHA**.
-   The Bahria Town branch is **ET-BT**.
-   All five branches are in Karachi.
-   The head office is associated with Gulshan-e-Iqbal.
-   The first branch opened in 2018 in Gulshan-e-Iqbal.

## 4. Branch-Specific Signature Dishes

The following dishes are **exclusive to the named branch** in this
sample dataset. They are not part of the regular menu at the other
branches. If a customer asks for one of these dishes at another branch,
the assistant must explain that it is only available at its designated
branch.

  ---------------------------------------------------------------------------
  Dish             Exclusive branch  Description                 Sample price
  ---------------- ----------------- ------------------ ---------------------
  Karachi Creamy   Gulshan-e-Iqbal   Creamy pasta with              PKR 1,050
  Chicken Pasta    (ET-GUL)          seasoned chicken,  
                                     mushrooms, and a   
                                     mild pepper sauce. 

  North Nazimabad  North Nazimabad   Pasta tossed with              PKR 1,150
  Spicy Malai Boti (ET-NNZ)          spicy              
  Pasta                              malai-boti-style   
                                     chicken, herbs,    
                                     and a light creamy 
                                     sauce.             

  PECHS Smoky      PECHS (ET-PECHS)  Alfredo-style                  PKR 1,200
  Tikka Alfredo                      pasta with smoky   
                                     tikka chicken and  
                                     a mild cheese      
                                     sauce.             

  DHA Dynamite     DHA (ET-DHA)      Creamy spicy pasta             PKR 1,250
  Zinger Pasta                       topped with        
                                     chopped crispy     
                                     zinger chicken and 
                                     dynamite sauce.    

  Bahria Town      Bahria Town       Baked pasta with a             PKR 1,300
  Loaded Cheese    (ET-BT)           three-cheese       
  Pasta                              topping, chicken,  
                                     and seasoned       
                                     crumbs.            
  ---------------------------------------------------------------------------

### Strict availability rules

1.  Karachi Creamy Chicken Pasta is available only at Gulshan-e-Iqbal.
2.  North Nazimabad Spicy Malai Boti Pasta is available only at North
    Nazimabad.
3.  PECHS Smoky Tikka Alfredo is available only at PECHS.
4.  DHA Dynamite Zinger Pasta is available only at DHA.
5.  Bahria Town Loaded Cheese Pasta is available only at Bahria Town.
6.  Do not tell a customer that an exclusive dish is available at
    another branch.
7.  If the customer asks whether an exclusive dish can be delivered from
    its home branch to another neighbourhood, do not assume that
    cross-branch delivery is possible. Say that this needs confirmation.
8.  The prices above are sample dataset prices, not live prices. If a
    live menu tool returns a different price, use the live tool result
    for the current menu price and clarify that branch-exclusive
    availability is still governed by this document.

## 5. Regular Menu --- Sample Data

These three menu entries are carried over from the starter menu in the
supplied mini-project notebook.

  ------------------------------------------------------------------------
  Menu item                             Sample price Availability
  --------------------- ---------------------------- ---------------------
  Zinger Burger                              PKR 850 Regular menu; branch
                                                     availability should
                                                     be confirmed

  Chicken Biryani                            PKR 450 Regular menu; branch
                                                     availability should
                                                     be confirmed

  Club Sandwich                              PKR 700 Regular menu; branch
                                                     availability should
                                                     be confirmed
  ------------------------------------------------------------------------

**Important:** The notebook's `fetch_menu()` function currently returns
these three items and prices. This knowledge-base document does not
change that Python list. The branch-exclusive dishes above are
additional sample knowledge for RAG testing and will not appear in
`fetch_menu()` unless you add them to the code.

## 6. Branch Details

### 6.1 Gulshan-e-Iqbal Branch --- ET-GUL

-   **Area:** Gulshan-e-Iqbal, Karachi
-   **Role in the brand:** Original and first-ever outlet.
-   **Opened:** 2018
-   **Services:** Dine-in, takeaway, delivery.
-   **Exclusive signature dish:** Karachi Creamy Chicken Pasta.
-   **Dish description:** Creamy chicken pasta with mushrooms and mild
    pepper sauce.
-   **Sample price:** PKR 1,050.
-   **Key fact:** The restaurant's founding story and first outlet are
    linked to this branch.

### 6.2 North Nazimabad Branch --- ET-NNZ

-   **Area:** North Nazimabad, Karachi
-   **Opened:** 2021
-   **Services:** Dine-in, takeaway, delivery.
-   **Exclusive signature dish:** North Nazimabad Spicy Malai Boti
    Pasta.
-   **Dish description:** Pasta with spicy malai-boti-style chicken,
    herbs, and a light creamy sauce.
-   **Sample price:** PKR 1,150.
-   **Key fact:** This was the second branch in the fictional expansion
    timeline.

### 6.3 PECHS Branch --- ET-PECHS

-   **Area:** PECHS, Karachi
-   **Opened:** 2022
-   **Services:** Takeaway and delivery.
-   **Exclusive signature dish:** PECHS Smoky Tikka Alfredo.
-   **Dish description:** Alfredo-style pasta with smoky tikka chicken
    and a mild cheese sauce.
-   **Sample price:** PKR 1,200.
-   **Key fact:** This branch was designed around takeaway and delivery
    orders.

### 6.4 DHA Branch --- ET-DHA

-   **Area:** DHA Phase 6, Karachi
-   **Opened:** 2024
-   **Services:** Dine-in, takeaway, delivery.
-   **Exclusive signature dish:** DHA Dynamite Zinger Pasta.
-   **Dish description:** Spicy creamy pasta topped with crispy zinger
    chicken and dynamite sauce.
-   **Sample price:** PKR 1,250.
-   **Key fact:** Its signature dish combines pasta with the
    restaurant's zinger-style flavour profile.

### 6.5 Bahria Town Branch --- ET-BT

-   **Area:** Bahria Town Karachi
-   **Opened:** 2024
-   **Services:** Dine-in and takeaway.
-   **Exclusive signature dish:** Bahria Town Loaded Cheese Pasta.
-   **Dish description:** Baked pasta with three cheeses, chicken, and
    seasoned crumbs.
-   **Sample price:** PKR 1,300.
-   **Key fact:** This branch's signature item is a baked,
    cheese-focused pasta dish.

## 7. Customer Support Facts and Boundaries

The restaurant's customer-support assistant may use this document to
answer questions about:

-   Restaurant name, cuisine, founding year, and founder.
-   The founding story and historical milestones.
-   Number of branches and their neighbourhoods.
-   Which branch is the original branch.
-   Branch IDs and each branch's service focus.
-   Which signature dish belongs to which branch.
-   Whether a branch-exclusive dish is available at another branch.
-   The sample regular menu and the sample prices listed in the
    notebook.

The assistant must follow these boundaries:

-   Do not invent a phone number, email address, exact street address,
    opening hours, delivery radius, reservation policy, refund policy,
    or allergen statement. This dataset does not define those facts.
-   Do not claim that a branch is currently open. No live
    operating-hours data is provided.
-   Do not claim that an item is in stock right now. No live inventory
    data is provided.
-   Do not treat a sample price as a guaranteed current price.
-   Do not claim that a branch-exclusive dish can be ordered from
    another branch.
-   If a requested fact is missing, say that the knowledge base does not
    contain it and offer to confirm it.

## 8. RAG Retrieval Quick Reference

This section provides concise, independently retrievable facts for
common customer questions.

**Q: What is the restaurant's name?**\
A: Eatery.

**Q: When was Eatery founded?**\
A: It was founded in 2018 in this fictional dataset.

**Q: Who founded Eatery?**\
A: Salman Ahmed is listed as the founder in this fictional dataset.

**Q: Where did the first branch open?**\
A: The first branch opened in Gulshan-e-Iqbal, Karachi, in 2018.

**Q: How many branches does the restaurant have?**\
A: Five sample branches: Gulshan-e-Iqbal, North Nazimabad, PECHS, DHA
Phase 6, and Bahria Town Karachi.

**Q: Which branch is the original branch?**\
A: Gulshan-e-Iqbal (ET-GUL).

**Q: Which branch serves Karachi Creamy Chicken Pasta?**\
A: Only the Gulshan-e-Iqbal branch (ET-GUL).

**Q: Can I get North Nazimabad Spicy Malai Boti Pasta at DHA?**\
A: No. It is listed as exclusive to North Nazimabad (ET-NNZ).

**Q: Which branch has PECHS Smoky Tikka Alfredo?**\
A: PECHS (ET-PECHS) only.

**Q: Which branch has DHA Dynamite Zinger Pasta?**\
A: DHA Phase 6 (ET-DHA) only.

**Q: Which branch has Bahria Town Loaded Cheese Pasta?**\
A: Bahria Town (ET-BT) only.

**Q: What is the sample price of a Zinger Burger?**\
A: PKR 850 in the notebook's starter menu.

**Q: What is the sample price of Chicken Biryani?**\
A: PKR 450 in the notebook's starter menu.

**Q: What is the sample price of a Club Sandwich?**\
A: PKR 700 in the notebook's starter menu.

**Q: Does the knowledge base provide exact opening hours?**\
A: No. Opening hours are not specified.

**Q: Does the knowledge base provide a contact number?**\
A: No. A contact number is not specified.

## 9. Suggested RAG Test Questions

Use these questions to test retrieval accuracy, branch matching, and
whether the model avoids unsupported claims.

1.  What year was Eatery founded?
2.  Who founded the restaurant?
3.  Tell me the story behind the restaurant's name and founding.
4.  Where was the first outlet opened?
5.  How many branches are there, and what are their areas?
6.  Which branch is the oldest?
7.  I am in DHA. Can I order Karachi Creamy Chicken Pasta there?
8.  Which branch serves the Spicy Malai Boti Pasta?
9.  Is PECHS Smoky Tikka Alfredo available in North Nazimabad?
10. What is special about the Bahria Town branch?
11. Which branch focuses mainly on takeaway and delivery?
12. What are the three items in the notebook's regular menu and their
    prices?
13. What is the sample price of DHA Dynamite Zinger Pasta?
14. Does the restaurant have a branch in Clifton?
15. What time does the PECHS branch close?
16. Give me the restaurant's phone number.
17. Can you guarantee that the DHA branch has the signature pasta in
    stock today?

Questions 14--17 are deliberate negative tests. The correct response is
that the provided knowledge base does not contain enough information to
answer them. The assistant should not guess.

## 10. Data Consistency Note

There are two information sources in the mini project:

1.  **Python menu tool:** The `menu` list in the notebook currently
    contains Zinger Burger (PKR 850), Chicken Biryani (PKR 450), and
    Club Sandwich (PKR 700). Use the tool for menu-price questions when
    it is available.
2.  **RAG knowledge base:** This document contains the fictional
    restaurant profile, founding story, branch directory,
    branch-specific signature dishes, and test questions.

If the tool and document disagree about a live menu price, prefer the
current tool result for the price. For branch-exclusive dish ownership,
use the branch rules in this document. Do not infer current stock or
opening status from either source.
