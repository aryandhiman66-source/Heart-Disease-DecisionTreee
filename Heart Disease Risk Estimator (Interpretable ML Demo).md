

**Heart Disease Risk Estimation – Interpretable ML Pipeline**

**1. Overview**

**This project implements an interpretable machine learning pipeline for estimating heart disease risk from clinical features. The goal is risk estimation, not medical diagnosis.**



**The system produces:**

**A probability score for heart disease risk**

**A human-readable risk category**

**The design emphasizes interpretability, transparency, and ethical use.**



**Disclaimer**

**This tool is for educational and demonstrational purposes only and does not provide medical advice. It must not be used for clinical decision-making. Always consult a qualified healthcare professional.**



**2. Problem Statement**

**Early screening for heart disease can benefit from models that are:**

**Transparent**

**Auditable**

**Easy to reason about for clinicians and stakeholders**

**In medical contexts, missing a true positive case (false negative) is often more harmful than flagging a false positive. For this reason, the project prioritizes sensitivity (recall) and interpretability over raw accuracy.**



**3. Data Description**

**Dataset**

**Heart Disease dataset (commonly used benchmark in machine learning).**



**Target variable:**



**1 → Presence of heart disease**

**0 → Absence of heart disease**



**Input features (13)**

**age – Age of the patient**

**sex – Sex (1 = male, 0 = female)**

**cp – Chest pain type**

**trestbps – Resting blood pressure**

**chol – Serum cholesterol**

**fbs – Fasting blood sugar**

**restecg – Resting ECG results**

**thalach – Maximum heart rate achieved**

**exang – Exercise-induced angina**

**oldpeak – ST depression induced by exercise**

**slope – Slope of peak exercise ST segment**

**ca – Number of major vessels**

**thal – Thalassemia**



**All features are used consistently during training and inference to avoid data leakage.**



**4. Modeling Approach**

**4.1 Choice of Model: Decision Tree**

**A Decision Tree classifier is used because it provides:**

**Interpretability – The decision logic can be visualized and explained.**

**Rule-based reasoning – Input–output relationships are explicit.**

**Fast inference – Suitable for real-time or near real-time estimation.**

**These properties are especially important in healthcare-adjacent applications where explainability is critical.**



**4.2 Regularization via Pruning**

**A fully grown, unpruned Decision Tree is prone to overfitting.**

**To address this, cost-complexity pruning (ccp\_alpha) is applied to:**

**Reduce model variance**

**Improve generalization to unseen data**

**Control model complexity**

**Pruning involves exploring the trade-off between model simplicity and predictive performance and selecting an appropriate ccp\_alpha value.**



**5. Evaluation Strategy**

**Model evaluation does not rely solely on accuracy. Instead, it focuses on metrics that are more meaningful in a screening context:**

**Recall (Sensitivity) – Minimize false negatives**

**Precision – Control false positives**

**F1-score – Balance between precision and recall**

**This metric choice reflects the higher cost of missed positive cases in medical screening scenarios.**



**6. Risk Estimation Output**

**The deployed model returns:**

**Risk score – Estimated probability of heart disease**

**Risk level – One of:**

**Low risk**

**Medium risk**

**High risk**

**Risk categories are derived from probability thresholds chosen to prioritize sensitivity.**

**This system does not diagnose disease; it provides a risk estimate that is intended for educational illustration only.**



**7. System Architecture**

**Training (offline)**

**Data preprocessing**

**Feature selection / preparation**

**Training a pruned Decision Tree classifier**

**Model serialization using joblib**



**Inference (online)**

**A Flask API loads the serialized model**

**Incoming input data are validated**



**The API returns:**

**Risk score (probability)**

**Risk level (categorical label)**

**End-to-end pipeline**

**User Input → Validation → Model → Risk Score → Risk Level**



**8. API Usage**

**Endpoint**

**POST /predict**



**Example request body:**

**json**

**{**

  **"age": 55,**

  **"sex": 1,**

  **"cp": 0,**

  **"trestbps": 140,**

  **"chol": 240,**

  **"fbs": 0,**

  **"restecg": 1,**

  **"thalach": 150,**

  **"exang": 0,**

  **"oldpeak": 1.2,**

  **"slope": 1,**

  **"ca": 0,**

  **"thal": 2**

**}**



**Example response:**

**json**

**{**

  **"risk\_score": 0.42,**

  **"risk\_level": "Medium risk",**

  **"disclaimer": "Educational use only. Not medical advice."**

**}**



**9. Limitations**

**Trained on a benchmark dataset, not on real clinical population data.**

**Does not incorporate temporal or longitudinal patient information.**

**Risk thresholds are heuristic and context-dependent, not clinically validated.**

**These limitations are explicitly acknowledged to help avoid misuse and over-interpretation of the results.**



**10. Future Work**

**Planned or potential improvements include:**

**Per-prediction decision-path explanations (e.g., feature-based rules).**

**Probability calibration and ROC-based threshold tuning.**

**A simple web UI for non-technical users.**

**Validation on external datasets or more realistic clinical data.**



**11. Tech Stack**

**Python**

**scikit-learn**

**Flask**

**NumPy**

**joblib**

