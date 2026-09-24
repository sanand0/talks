# Decision Tree Builder

URL: https://prudhvi1709.github.io/decisiontreegen/

Decision Tree Builder

-

Light

-

Dark

-

Auto

#

Decision Tree Builder

##

OpenAI API Key

Enter your OpenAI API Key:

Your API key is stored locally in your browser and never sent to our servers.

##

Base URL

Enter your OpenAI API Base URL:

Your API key is stored locally in your browser and never sent to our servers.

##

Model

Model:

gpt-4.1-nano
gpt-4.1-mini
gpt-4o-mini
o3-mini

###

Sample Datasets

##### Heart Disease

Predict heart disease risk based on medical indicators

Target: target

##### Housing Prices

Predict housing prices based on location and features

Target: price

##### Iris Classification

Classify iris flowers based on petal and sepal measurements

Target: species

##### Wine Quality

Predict wine quality based on chemical properties

Target: quality

##### Student Performance

Predict student performance in secondary education (high school)

Target: G3

###

Step 1: Upload Dataset

Choose CSV or XLSX file:

##### Data Preview

schoolsexageaddressfamsizePstatusMeduFeduMjobFjobreasonguardiantraveltimestudytimefailuresschoolsupfamsuppaidactivitiesnurseryhigherinternetromanticfamrelfreetimegooutDalcWalchealthabsencesG1G2G3

GPF18UGT3A44at_hometeachercoursemother220yesnononoyesyesnono4341136566

GPF17UGT3T11at_homeothercoursefather120noyesnononoyesyesno5331134556

GPF15ULE3T11at_homeotherothermother123yesnoyesnoyesyesyesno432233107810

GPF15UGT3T42healthserviceshomemother130noyesyesyesyesyesyesyes3221152151415

GPF16UGT3T33otherotherhomefather120noyesyesnoyesyesnono432125461010

GPM16ULE3T43servicesotherreputationmother120noyesyesyesyesyesyesno54212510151515

GPM16ULE3T22otherotherhomemother120nonononoyesyesyesno4441130121211

GPF17UGT3A44otherteacherhomemother220yesyesnonoyesyesnono4141116656

GPM15ULE3A32servicesotherhomemother120noyesyesnoyesyesyesno4221110161819

GPM15UGT3T34otherotherhomemother120noyesyesyesyesyesyesno5511150141515

GPF15UGT3T44teacherhealthreputationmother120noyesyesnoyesyesyesno33312201089

GPF15UGT3T21servicesotherreputationfather330noyesnoyesyesyesyesno5221144101212

GPM15ULE3T44healthservicescoursefather110noyesyesyesyesyesyesno4331352141414

GPM15UGT3T43teacherothercoursemother220noyesyesnoyesyesyesno5431232101011

GPM15UGT3A22otherotherhomeother130noyesnonoyesyesyesyes4521130141616

GPF16UGT3T44healthotherhomemother110noyesnonoyesyesyesno4441224141414

GPF16UGT3T44servicesservicesreputationmother130noyesyesyesyesyesyesno3231226131414

GPF16UGT3T33otherotherreputationmother320yesyesnoyesyesyesnono532114481010

GPM17UGT3T32servicesservicescoursemother113noyesnoyesyesyesyesno55524516655

GPM16ULE3T43healthotherhomefather110nonoyesyesyesyesyesno313135481010

###

Step 2: Generate Derived Metrics (Optional)

Generate AI-powered derived metrics

Select columns for derived metrics:

school

sex

age

address

famsize

Pstatus

Medu

Fedu

Mjob

Fjob

reason

guardian

traveltime

studytime

failures

schoolsup

famsup

paid

activities

nursery

higher

internet

romantic

famrel

freetime

goout

Dalc

Walc

health

absences

G1

G2

G3

Custom derived metrics (optional):

Include derived metrics in decision tree

Generate Derived Metrics

Skip to Analysis

###

Derived Metrics Preview

##### Enhanced Dataset with Derived Metrics

schoolsexageaddressfamsizePstatusMeduFeduMjobFjobreasonguardiantraveltimestudytimefailuresschoolsupfamsuppaidactivitiesnurseryhigherinternetromanticfamrelfreetimegooutDalcWalchealthabsencesG1G2G3parent_edu_avgabsences_per_agetotal_alcoholalc_ratio_wknd_to_workavg_gradegrade_improvementhas_failurestraveltime_to_studytimeany_supportstudy_efficiencysocial_activity_scorefamrel_romantic_interactionhealth_per_absencescombined_social_timeMjob_scoreFjob_scoreparent_job_stabilitytraveltime_sqPstatus_binfamsize_binfamsize_Pstatus_interaction

181444122111434113656640.333333333333333320.99999000009999895.66666666666666710.99999500002499992.83331916673749970.4285714285714285574

171111212111533113455610.2352941176470588220.99999000009999895.33333333333333310.499997500012499932.66665333339999930.661

15111112211231111143223310781010.666666666666666651.49999250003749988.333333333333334310.499997500012499934.1666458334374990.272727272727272751

1511421311131111111322115215141530.1333333333333333320.999990000099998914.6666666666666660.33333222222592594.8888725926469131.666666666666666741

16113322112111143212546101030.2531.99998000019999798.66666666666666640.499997500012499934.333311666774999151

11611143323112111111542125101515153.50.62531.9999800001999979150.499997500012499937.49996250018749850.4545454545454545361

11611122221112111444113121211220.999990000099998911.666666666666666-10.499997500012499935.833304166812499381

171442411221111414111665640.3529411764705882620.99999000009999895.6666666666666670.99999500002499992.83331916673749970.1428571428571428554

1151132321112111114221111618192.520.999990000099998917.66666666666666830.499997500012499938.8332891668875141

11511342211121111115511151415153.520.999990000099998914.66666666666666610.499997500012499937.333296666849998561

###### Select derived metrics for decision tree:

parent_edu_avg

absences_per_age

total_alcohol

alc_ratio_wknd_to_work

avg_grade

grade_improvement

has_failures

traveltime_to_studytime

any_support

study_efficiency

social_activity_score

famrel_romantic_interaction

health_per_absences

combined_social_time

Mjob_score

Fjob_score

parent_job_stability

traveltime_sq

Pstatus_bin

famsize_bin

famsize_Pstatus_interaction

Select All
Select None

Proceed to Analysis

###

Step 3: Configure Analysis

Target Column:
schoolsexageaddressfamsizePstatusMeduFeduMjobFjobreasonguardiantraveltimestudytimefailuresschoolsupfamsuppaidactivitiesnurseryhigherinternetromanticfamrelfreetimegooutDalcWalchealthabsencesG1G2G3parent_edu_avgabsences_per_agetotal_alcoholalc_ratio_wknd_to_workavg_gradegrade_improvementhas_failurestraveltime_to_studytimeany_supportstudy_efficiencysocial_activity_scorefamrel_romantic_interactionhealth_per_absencescombined_social_timeMjob_scoreFjob_scoreparent_job_stabilitytraveltime_sqPstatus_binfamsize_binfamsize_Pstatus_interaction

Analysis Prompt:

Analyze

###

Step 4: AI Analysis

##

View Generated Code

```
# Handle missing values
df.fillna(df.median(numeric_only=True), inplace=True)

# Select target and features (exclude grade columns: G1, G2, avg_grade, grade_improvement)
exclude_cols = ['G3', 'G1', 'G2', 'avg_grade', 'grade_improvement']
feature_cols = [col for col in df.columns if col not in exclude_cols]

# Prepare data
X = df[feature_cols]
y = df['G3']

# Create and train model
model = DecisionTreeRegressor(max_depth=3)
model.fit(X, y)

```

###

Step 5: Decision Tree

######

Ask Questions About Your Decision Tree

Analyze Tree

Ask about feature importance, decision paths, or specific outcomes to highlight relevant tree sections.

######

Analysis Result

Clear Highlights

Expand All

Is study_efficiency < 3.667?

Is absences_per_age < 0.028?

Is traveltime_to_studytime < 0.417?

YES

Prediction: 6.153846153846154

NO

Prediction: 0.6875

Is studytime < 2.500?

YES

Prediction: 6.142857142857143

NO

Prediction: 10.1

Is studytime < 2.500?

Is study_efficiency < 5.667?

YES

Prediction: 9.151162790697674

NO

Prediction: 12.698224852071005

Is study_efficiency < 4.806?

YES

Prediction: 13.642857142857142

NO

Prediction: 16.5625

##### Model Performance

0.673

Accuracy

0.673

Precision

0.673

Recall

0.673

F1 Score

0

False Positives

0

False Negatives

###

Step 6: Revise Analysis

Revision Instructions:

Revise Analysis

Loading...

Processing...

This is Demo. contains no confidential data/IP

Info

Python environment initialized successfully!

Success

Sample dataset loaded successfully! Found 395 rows with 33 columns.

Info

Skipped derived metrics generation. Proceeding with original dataset.

Success

Decision tree model created successfully! Accuracy: 86.0%

Success

Decision tree model created successfully! Accuracy: 31.8%

Success

Successfully generated 21 derived metrics!

Success

Decision tree model created successfully! Accuracy: 67.3%
