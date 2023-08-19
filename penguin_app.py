@st.cache()
def prediction(model, island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex):
  species = model.predict([[island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex]])
  species = species[0]
  if species == 0:
    return "Adelie"
  elif species == 1:
    return "Chinstrap"
  else:
    return "Gentoo"