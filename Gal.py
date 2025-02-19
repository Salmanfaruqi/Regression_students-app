import streamlit as st

# Function to pair keywords and ads using a greedy algorithm
def pair_keywords_ads(keywords, ads):
    pairs = []
    for k, k_rev in keywords.items():
        for a, a_rev in ads.items():
            if k_rev > 0 and a_rev > 0:
                # Allocate the minimum of the remaining revenues
                revenue = min(k_rev, a_rev)
                pairs.append({"Keyword": k, "Ad": a, "Revenue": revenue})
                # Subtract the allocated revenue from both keyword and ad
                keywords[k] -= revenue
                ads[a] -= revenue
    return pairs

# Main function for the Streamlit app
def main():
    st.title("Gal's Challenge")

    # Input for Ads Revenue
    st.write("Enter Revenue for Ads:")
    Ad1 = st.number_input("A1", min_value=1, max_value=1000, value=20)
    Ad2 = st.number_input("A2", min_value=1, max_value=1000, value=20)
    Ad3 = st.number_input("A3", min_value=1, max_value=1000, value=20)

    # Input for Keywords Revenue
    st.write("Enter Revenue for Keywords:")
    KW1 = st.number_input("K1", min_value=1, max_value=1000, value=20)
    KW2 = st.number_input("K2", min_value=1, max_value=1000, value=20)
    KW3 = st.number_input("K3", min_value=1, max_value=1000, value=20)

    # Create dictionaries for keywords and ads
    keywords = {"K1": KW1, "K2": KW2, "K3": KW3}
    ads = {"A1": Ad1, "A2": Ad2, "A3": Ad3}

    if st.button("Generate Pairs"):
        # Generate pairs using the greedy algorithm
        pairs = pair_keywords_ads(keywords, ads)

        # Display the pairs in a table
        st.header("Keyword-Ad Pairs")
        st.table(pairs)

        # Display the remaining revenues (optional)
        #st.header("Remaining Revenues")
        #st.write("Keywords:", keywords)
        #st.write("Ads:", ads)

# Run the Streamlit app
if __name__ == "__main__":
    main()
