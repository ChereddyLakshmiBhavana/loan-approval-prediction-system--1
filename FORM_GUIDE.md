# 📋 Loan Application Form - Field Guide

## Complete Field Explanations

This guide explains each field in the loan application form on http://localhost:3000

---

## 👨‍👩‍👧‍👦 **Number of Dependents**
- **What it means**: How many family members depend on you financially
- **Accepted values**: 0, 1, 2, 3, 4, 5+ 
- **Example**: If you have a spouse and 2 children = 3 dependents
- **Why it matters**: More dependents = higher expenses, may affect loan approval
- **Default**: Leave empty or enter your actual number

---

## 🎓 **Education**
- **What it means**: Your highest level of education
- **Options**: 
  - ✅ **Graduate** - Bachelor's degree or higher
  - ✅ **Not Graduate** - High School or below
- **Why it matters**: Education level indicates financial literacy and earning potential
- **Select**: Click dropdown to choose one option

---

## 💼 **Self Employed**
- **What it means**: Are you running your own business or working as an employee?
- **Options**:
  - ✅ **Yes** - You own a business or freelance
  - ✅ **No** - You work for a company/organization
- **Why it matters**: Self-employed applicants have variable income, may be riskier
- **Select**: Click dropdown to choose one option

---

## 💰 **Annual Income**
- **What it means**: How much money you earn in a year (in ₹ Rupees)
- **Accepted values**: Any positive number (e.g., 300000, 500000, 1000000)
- **Format**: Enter as plain numbers (no commas or special characters)
- **Example**: 
  - 300000 = ₹3 Lakhs per year
  - 1000000 = ₹10 Lakhs per year
  - 5000000 = ₹50 Lakhs per year
- **Why it matters**: More income = better ability to repay loan
- **Tip**: If you earn ₹60,000/month, enter: 60000 × 12 = 720,000

---

## 🏦 **Loan Amount**
- **What it means**: How much money you want to borrow (in ₹ Rupees)
- **Accepted values**: Any positive number
- **Format**: Enter as plain numbers
- **Example**:
  - 100000 = ₹1 Lakh loan
  - 500000 = ₹5 Lakhs loan
  - 2000000 = ₹20 Lakhs loan
- **Why it matters**: Loan amount compared to income affects approval chances
- **Ratio**: Banks usually approve if loan ≤ 5× your annual income

---

## ⏱️ **Loan Term (Duration)**
- **What it means**: How long you want to repay the loan (in months)
- **Accepted values**: 12 to 360 months (must be multiple of 12)
- **Common values**:
  - 60 months = 5 years
  - 120 months = 10 years
  - 180 months = 15 years
  - 240 months = 20 years
  - 360 months = 30 years
- **Why it matters**: Longer term = lower monthly payment but more interest
- **Default**: 360 months (30-year mortgage)

---

## 📊 **CIBIL Score**
- **What it means**: Your credit score (financial reliability rating)
- **Accepted values**: 300 to 900
- **What it indicates**:
  - **300-550**: Poor credit (high default history)
  - **550-650**: Average credit (some payment delays)
  - **650-750**: Good credit (mostly on-time payments)
  - **750-900**: Excellent credit (perfect payment history)
- **Why it matters**: Higher CIBIL score = MUCH higher approval chances
- **Impact**: A 100-point difference can change approval status completely
- **Default**: Enter your actual CIBIL score from bank records

**How to check your CIBIL score:**
- Visit www.cibil.com
- Contact your bank (usually free)
- Register and pull your credit report

---

## 🏠 **Residential Assets Value**
- **What it means**: Total value of property you own (house, apartment) in ₹
- **Accepted values**: Any non-negative number
- **Example**:
  - 1000000 = ₹10 Lakhs (house value)
  - 5000000 = ₹50 Lakhs (house value)
- **If you don't own property**: Enter 0
- **Why it matters**: Assets can be collateral; banks feel safer with mortgageable property
- **Note**: Enter market value, not purchase price

---

## 🏢 **Commercial Assets Value**
- **What it means**: Value of business property or commercial real estate you own in ₹
- **Accepted values**: Any non-negative number
- **Example**:
  - 2000000 = ₹20 Lakhs (office/shop value)
  - 10000000 = ₹1 Crore (commercial building)
- **If you don't own commercial property**: Enter 0
- **Why it matters**: Business assets increase loan approval chances, show business success

---

## 💎 **Luxury Assets Value**
- **What it means**: Value of expensive items you own (car, jewelry, jewelry, electronics) in ₹
- **Accepted values**: Any non-negative number
- **Example**:
  - 500000 = Car worth ₹5 Lakhs
  - 200000 = Jewelry worth ₹2 Lakhs
  - 150000 = High-end electronics
- **If you don't own luxury items**: Enter 0
- **Why it matters**: Shows you have disposable income and financial stability
- **Note**: Banks can repossess these items if loan defaults

---

## 🏧 **Bank Assets Value**
- **What it means**: Money in your bank accounts (savings, current, fixed deposits) in ₹
- **Accepted values**: Any non-negative number
- **Example**:
  - 500000 = ₹5 Lakhs in savings account
  - 1000000 = ₹10 Lakhs in FDs + savings
- **Where to find**: Check your bank account statements total
- **Why it matters**: **Most important!** Liquid money shows you can pay EMI immediately
- **Impact**: High bank assets = much higher approval chance

---

## ✅ **How to Use the Form**

1. **Fill in all fields** - Each field is required
2. **Use realistic numbers** - Based on your actual financial situation
3. **For dropdowns** - Click and select one option (Graduate/Not Graduate, Yes/No)
4. **For numbers** - Just type the value, no special characters needed
5. **Click "🚀 Predict Loan Approval"** - Button at the bottom
6. **See results** - Approval status + probability + confidence level

---

## 📝 **Example: Real-Life Scenario**

Let's say you're filling this form with realistic data:

```
Number of Dependents:        2      (You support 2 people)
Education:                   Graduate
Self Employed:               No     (You have a job)
Annual Income:               720000 (₹60,000 × 12 months)
Loan Amount:                 500000 (You want ₹5 Lakh loan)
Loan Term:                   180    (15 years to repay)
CIBIL Score:                 750    (Good credit score)
Residential Assets:          2000000 (Your house worth ₹20 Lakh)
Commercial Assets:           0      (No business property)
Luxury Assets:               400000 (Car + electronics worth ₹4 Lakh)
Bank Assets:                 300000 (₹3 Lakh in savings)
```

**Expected Result**: ✅ **APPROVED** (High probability like 0.85 or higher)

---

## 💡 **Tips for Loan Approval**

1. **Strongest factors** (in order of importance):
   - Bank Assets (liquid money available)
   - CIBIL Score (credit history)
   - Annual Income (earning capacity)
   - Residential Assets (collateral)

2. **To increase approval chances**:
   - ✅ Improve CIBIL score (pay bills on time)
   - ✅ Increase savings/bank balance
   - ✅ Reduce loan amount
   - ✅ Extend loan term (lower EMI)
   - ✅ Reduce number of dependents (on paper for loan)
   - ✅ Increase income (job promotion, side business)

3. **What reduces approval**:
   - ❌ Very low CIBIL score (< 600)
   - ❌ Loan amount > 5× annual income
   - ❌ No bank assets/savings
   - ❌ No residential assets
   - ❌ High number of dependents

---

## 🎯 **After Submission**

You'll see:
- **Approval Status**: APPROVED ✅ or REJECTED ❌
- **Approval Probability**: 0-100% (e.g., 85% = likely to be approved)
- **Confidence Level**: Low/Medium/High (how sure the AI is)

---

## ❓ **Frequently Asked Questions**

**Q: Can I test with different values?**  
✅ YES! Try multiple scenarios to see how each field affects the prediction.

**Q: Does this affect my real credit?**  
✅ NO! This is just a prediction tool. Your actual CIBIL score/credit unaffected.

**Q: Why do I need all this information?**  
✅ Banks look at everything: income, assets, credit score, dependents, loan amount.

**Q: Can I change values and resubmit?**  
✅ YES! The form resets after each prediction. You can enter different data anytime.

**Q: What's CIBIL?**  
✅ CIBIL = Credit Information Bureau India Limited (India's main credit rating agency)

---

**Enjoy using the Loan Approval Prediction System!** 🎯💰
