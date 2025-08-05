from tensorflow.keras.models import load_model
model = load_model('/home/pritham/Desktop/SmartBridge/Code/fresh_vs_rotten.h5')
model.save('/home/pritham/Desktop/SmartBridge/Code/fresh_vs_rotten.keras')