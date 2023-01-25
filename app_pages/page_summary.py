'''
This file and the contents have been taken from the 
 Churnometer walk through Project 2 and customized for
 this project
'''
import streamlit as st

def page_summary_body():

    st.write("### Quick Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Dataset**\n"
        f"* The dataset is sourced from **[Kaggle](https://www.kaggle.com/codeinstitute/housing-prices-data)**.\n"
        f"* The dataset has 1.461 thousand rows and represents housing records from Ames, Iowa. "
        f"**Ames, Iowa**\n"
        f"* Ames has a robust, stable economy and a flourish cultural environment, with a population\n "
        f"of 89.540 people. \n\n"
        f"* The dataset typically contains a house profile, "
        f"ie. Floor Area, Basement, Garage, Kitchen, Lot, Porch, Wood Deck, Year Built "
        f"and the respective sale price, for houses built between 1872 and 2010.\n\n"
        f"**SalePrice** is the price a house sold for and is our target variable.\n")

    # "Business Requirements" section
    st.write(
        f"The project has 2 business requirements:\n"
        f"* 1 - My niece is interested in discovering how house attributes correlate with the sale price.\n"
        f"  * My niece expects data visualizations of the correlated variables against the sale price.\n"
        f"* 2 - My niece is interested in predicting the house sales price from her new 6 refurbished houses, "
        f"and any other house in Ames, Iowa, that she will consider to buy or sell in the future."
        )

    # Link to README file, so the users can have access to full project documentation
    st.info(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/Vasi012/PP5-Predictive-Analysis#readme)"
        )

    st.info(
        f"**Dataset Content Guidelines**\n\n"
        f"|Variable|Meaning|Units|\n"
        f"|:----|:----|:----|\n"
        f"|1stFlrSF|First Floor square feet|(Min - Max > Sq. ft.) 334 - 4692|\n"
        f"|2ndFlrSF|Second floor square feet|(Min - Max > Sq. ft.) 0 - 2065|\n"
        f"|BedroomAbvGr|Bedrooms above grade (does NOT include basement bedrooms)|(Min - Max > Bedrooms) 0 - 8|\n"
        f"|BsmtExposure|Refers to walkout or garden level walls|Gd: Good Exposure; Av: Average Exposure; Mn: Mimimum Exposure; No: No Exposure; None: No Basement|\n"
        f"|BsmtFinType1|Rating of basement finished area|GLQ: Good Living Quarters; ALQ: Average Living Quarters; BLQ: Below Average Living Quarters; Rec: Average Rec Room; LwQ: Low Quality; Unf: Unfinshed; None: No Basement|\n"
        f"|BsmtFinSF1|Type 1 finished square feet|(Min - Max > Sq. ft.) 0 - 5644|\n"
        f"|BsmtUnfSF|Unfinished square feet of basement area|(Min - Max > Sq. ft.) 0 - 2336|\n"
        f"|TotalBsmtSF|Total square feet of basement area|(Min - Max > Sq. ft.) 0 - 6110|\n"
        f"|GarageArea|Size of garage in square feet|(Min - Max > Sq. ft.) 0 - 1418|\n"
        f"|GarageFinish|Interior finish of the garage|Fin: Finished; RFn: Rough Finished; Unf: Unfinished; None: No Garage|\n"
        f"|GarageYrBlt|Year garage was built|(Min - Max > Year) 1900 - 2010|\n"
        f"|GrLivArea|Above grade (ground) living area square feet|(Min - Max > Sq. ft.) 334 - 5642|\n"
        f"|KitchenQual|Kitchen quality|Ex: Excellent; Gd: Good; TA: Typical/Average; Fa: Fair; Po: Poor|\n"
        f"|LotArea| Lot size in square feet|(Min - Max > Sq. ft.) 1300 - 215245|\n"
        f"|LotFrontage| Linear feet of street connected to property|(Min - Max > Lin. ft.) 21 - 313|\n"
        f"|MasVnrArea|Masonry veneer area in square feet|(Min - Max > Sq. ft.) 0 - 1600|\n"
        f"|EnclosedPorch|Enclosed porch area in square feet|(Min - Max > Sq. ft.) 0 - 286|\n"
        f"|OpenPorchSF|Open porch area in square feet|(Min - Max > Sq. ft.) 0 - 547|\n"
        f"|OverallCond|Rates the overall condition of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|\n"
        f"|OverallQual|Rates the overall material and finish of the house|10: Very Excellent; 9: Excellent; 8: Very Good; 7: Good; 6: Above Average; 5: Average; 4: Below Average; 3: Fair; 2: Poor; 1: Very Poor|\n"
        f"|WoodDeckSF|Wood deck area in square feet|(Min - Max > Sq. ft.) 0 - 736|\n"
        f"|YearBuilt|Original construction date|(Min - Max > Year) 1872 - 2010|\n"
        f"|YearRemodAdd|Remodel date (same as construction date if no remodeling or additions)|(Min - Max > Year) 1950 - 2010|\n"
        f"|SalePrice|Sale Price|(Min - Max > Price in $) 34900 - 755000|\n"
        )