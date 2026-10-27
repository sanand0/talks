#!/usr/bin/env python3
"""
Glucofix Phase 3 Trial - Patient Eligibility Analysis
A systematic evaluation of patient records against stringent inclusion/exclusion criteria
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class GlucofixEligibilityChecker:
    """
    Analyzes patient eligibility for the Glucofix Phase 3 clinical trial
    """
    
    def __init__(self, excel_file_path):
        """Load all patient data sheets"""
        self.file_path = excel_file_path
        self.demographics = pd.read_excel(excel_file_path, sheet_name='Demographics')
        self.diagnoses = pd.read_excel(excel_file_path, sheet_name='Diagnoses')
        self.medications = pd.read_excel(excel_file_path, sheet_name='Medications')
        self.lab_results = pd.read_excel(excel_file_path, sheet_name='Lab_Results')
        self.visits = pd.read_excel(excel_file_path, sheet_name='Visits')
        
        # Reference date for the analysis (today)
        self.reference_date = datetime.now()
        
        # Initialize results storage
        self.results = []
        
    def check_patient_eligibility(self, patient_id):
        """
        Check all inclusion and exclusion criteria for a single patient
        Returns: dict with eligibility status and detailed reasons
        """
        result = {
            'Patient_ID': patient_id,
            'Eligible': True,
            'Failed_Criteria': [],
            'Warnings': [],
            'Details': {}
        }
        
        # Get patient data
        demo = self.demographics[self.demographics['Patient_ID'] == patient_id].iloc[0]
        pt_diagnoses = self.diagnoses[self.diagnoses['Patient_ID'] == patient_id]
        pt_meds = self.medications[self.medications['Patient_ID'] == patient_id]
        pt_labs = self.lab_results[self.lab_results['Patient_ID'] == patient_id]
        
        # ============ INCLUSION CRITERIA ============
        
        # 1. Age: 30-75 years (inclusive)
        age = demo['Age']
        if age < 30 or age > 75:
            result['Eligible'] = False
            result['Failed_Criteria'].append(f"Age {age} outside 30-75 range")
        result['Details']['Age'] = age
        
        # 2. Diagnosis of T2DM for ≥ 6 months
        t2dm_diagnoses = pt_diagnoses[pt_diagnoses['ICD10_Code'].str.startswith('E11', na=False)]
        if len(t2dm_diagnoses) == 0:
            result['Eligible'] = False
            result['Failed_Criteria'].append("No Type 2 Diabetes diagnosis found")
        else:
            t2dm_diagnoses['Date_First_Diagnosed'] = pd.to_datetime(t2dm_diagnoses['Date_First_Diagnosed'])
            earliest_t2dm = t2dm_diagnoses['Date_First_Diagnosed'].min()
            months_since_diagnosis = (self.reference_date - earliest_t2dm).days / 30.44
            
            if months_since_diagnosis < 6:
                result['Eligible'] = False
                result['Failed_Criteria'].append(f"T2DM diagnosed only {months_since_diagnosis:.1f} months ago (need ≥6)")
            
            result['Details']['T2DM_Diagnosis_Date'] = earliest_t2dm.strftime('%Y-%m-%d')
            result['Details']['Months_Since_T2DM_Diagnosis'] = f"{months_since_diagnosis:.1f}"
            
        # 3. HbA1c between 7.5% and 10.5% (inclusive)
        hba1c_tests = pt_labs[pt_labs['Test_Name'] == 'HbA1c']
        if len(hba1c_tests) > 0:
            # Get most recent HbA1c within 30 days
            hba1c_tests['Test_Date'] = pd.to_datetime(hba1c_tests['Test_Date'])
            recent_hba1c = hba1c_tests.sort_values('Test_Date', ascending=False).iloc[0]
            hba1c_value = recent_hba1c['Value']
            
            if hba1c_value < 7.5 or hba1c_value > 10.5:
                result['Eligible'] = False
                result['Failed_Criteria'].append(f"HbA1c {hba1c_value}% outside 7.5-10.5% range")
            
            result['Details']['HbA1c'] = f"{hba1c_value}%"
            result['Details']['HbA1c_Date'] = recent_hba1c['Test_Date'].strftime('%Y-%m-%d')
        else:
            result['Eligible'] = False
            result['Failed_Criteria'].append("No HbA1c measurement found")
            
        # 4. BMI between 23.0 and 40.0 kg/m²
        bmi = demo['BMI']
        if pd.notna(bmi):
            if bmi < 23.0 or bmi > 40.0:
                result['Eligible'] = False
                result['Failed_Criteria'].append(f"BMI {bmi:.1f} outside 23.0-40.0 range")
            result['Details']['BMI'] = f"{bmi:.1f}"
        else:
            result['Eligible'] = False
            result['Failed_Criteria'].append("BMI not recorded")
            
        # 5. Background therapy: Metformin ≥ 1000 mg/day for ≥ 3 months
        metformin_meds = pt_meds[pt_meds['Generic_Name'].str.lower().str.contains('metformin', na=False)]
        
        if len(metformin_meds) > 0:
            # Check for active metformin prescription
            active_metformin = metformin_meds[pd.isna(metformin_meds['End_Date'])]
            
            if len(active_metformin) > 0:
                metformin_dose = active_metformin.iloc[0]['Dose']
                result['Details']['Metformin_Dose'] = metformin_dose
                
                # Check duration (≥ 3 months)
                metformin_start = pd.to_datetime(active_metformin.iloc[0]['Start_Date'])
                months_on_metformin = (self.reference_date - metformin_start).days / 30.44
                
                if months_on_metformin < 3:
                    result['Eligible'] = False
                    result['Failed_Criteria'].append(f"Metformin only for {months_on_metformin:.1f} months (need ≥3)")
                
                result['Details']['Months_on_Metformin'] = f"{months_on_metformin:.1f}"
            else:
                result['Eligible'] = False
                result['Failed_Criteria'].append("No currently active metformin prescription")
        else:
            result['Eligible'] = False
            result['Failed_Criteria'].append("No metformin prescription found")
            
        # 6. Fasting Plasma Glucose: 130-260 mg/dL
        fpg_tests = pt_labs[pt_labs['Test_Name'] == 'Fasting Plasma Glucose']
        if len(fpg_tests) > 0:
            recent_fpg = fpg_tests.sort_values('Test_Date', ascending=False).iloc[0]
            fpg_value = recent_fpg['Value']
            
            if fpg_value < 130 or fpg_value > 260:
                result['Eligible'] = False
                result['Failed_Criteria'].append(f"FPG {fpg_value} mg/dL outside 130-260 range")
            
            result['Details']['FPG'] = f"{fpg_value} mg/dL"
        else:
            result['Warnings'].append("No fasting glucose measurement found")
            
        # 7. Renal Function: eGFR ≥ 60 mL/min/1.73 m²
        egfr_tests = pt_labs[pt_labs['Test_Name'] == 'eGFR']
        creatinine_tests = pt_labs[pt_labs['Test_Name'] == 'Serum Creatinine']
        
        if len(egfr_tests) > 0:
            recent_egfr = egfr_tests.sort_values('Test_Date', ascending=False).iloc[0]
            egfr_value = recent_egfr['Value']
            
            if egfr_value < 60:
                result['Eligible'] = False
                result['Failed_Criteria'].append(f"eGFR {egfr_value} mL/min/1.73m² below 60")
            
            result['Details']['eGFR'] = f"{egfr_value} mL/min/1.73m²"
        elif len(creatinine_tests) > 0:
            result['Warnings'].append("eGFR not directly measured, creatinine available")
        else:
            result['Eligible'] = False
            result['Failed_Criteria'].append("No renal function tests found")
            
        # 8. Blood Pressure: SBP ≤ 160 mmHg and DBP ≤ 95 mmHg
        bp_tests = pt_labs[pt_labs['Test_Name'].isin(['Systolic BP', 'Diastolic BP'])]
        
        if len(bp_tests) > 0:
            sbp_tests = bp_tests[bp_tests['Test_Name'] == 'Systolic BP']
            dbp_tests = bp_tests[bp_tests['Test_Name'] == 'Diastolic BP']
            
            if len(sbp_tests) > 0:
                recent_sbp = sbp_tests.sort_values('Test_Date', ascending=False).iloc[0]['Value']
                if recent_sbp > 160:
                    result['Eligible'] = False
                    result['Failed_Criteria'].append(f"Systolic BP {recent_sbp} mmHg exceeds 160")
                result['Details']['Systolic_BP'] = f"{recent_sbp} mmHg"
                
            if len(dbp_tests) > 0:
                recent_dbp = dbp_tests.sort_values('Test_Date', ascending=False).iloc[0]['Value']
                if recent_dbp > 95:
                    result['Eligible'] = False
                    result['Failed_Criteria'].append(f"Diastolic BP {recent_dbp} mmHg exceeds 95")
                result['Details']['Diastolic_BP'] = f"{recent_dbp} mmHg"
        else:
            result['Warnings'].append("No blood pressure measurements found")
            
        # 9. Contraception/Pregnancy (for women of childbearing potential)
        # Assuming we don't have pregnancy test data, but we note the requirement
        if demo['Gender'] == 'Female' and age >= 18 and age <= 50:
            result['Warnings'].append("Pregnancy test required at screening and randomization")
            
        # 10. Informed Consent
        if demo['Phone_Consent'] == 'Y':
            result['Details']['Phone_Consent'] = 'Yes'
        else:
            result['Warnings'].append("Phone consent not obtained - full informed consent needed")
            
        # ============ EXCLUSION CRITERIA ============
        
        # 1. Type 1 Diabetes
        t1dm_diagnoses = pt_diagnoses[pt_diagnoses['ICD10_Code'].str.startswith('E10', na=False)]
        if len(t1dm_diagnoses) > 0:
            result['Eligible'] = False
            result['Failed_Criteria'].append("Type 1 Diabetes diagnosis found (EXCLUSION)")
            
        # 2. Recent DKA or HHS (within 6 months)
        dka_codes = pt_diagnoses[pt_diagnoses['ICD10_Code'].str.contains('E10.1|E11.1|E13.1|E14.1', na=False)]
        if len(dka_codes) > 0:
            dka_codes['Date_First_Diagnosed'] = pd.to_datetime(dka_codes['Date_First_Diagnosed'])
            recent_dka = dka_codes[dka_codes['Date_First_Diagnosed'] > (self.reference_date - timedelta(days=180))]
            if len(recent_dka) > 0:
                result['Eligible'] = False
                result['Failed_Criteria'].append("Recent diabetic ketoacidosis/HHS (EXCLUSION)")
                
        # 3. Significant Insulin Therapy (>14 days in last 3 months)
        insulin_meds = pt_meds[pt_meds['Generic_Name'].str.lower().str.contains('insulin', na=False)]
        if len(insulin_meds) > 0:
            insulin_meds['Start_Date'] = pd.to_datetime(insulin_meds['Start_Date'])
            recent_insulin = insulin_meds[insulin_meds['Start_Date'] > (self.reference_date - timedelta(days=90))]
            
            if len(recent_insulin) > 0:
                result['Eligible'] = False
                result['Failed_Criteria'].append("Recent insulin use in last 3 months (EXCLUSION)")
                
        # 4. Use of GLP-1, SGLT2, or TZDs (within 3 months)
        excluded_meds = pt_meds[
            pt_meds['Generic_Name'].str.lower().str.contains(
                'semaglutide|liraglutide|dulaglutide|empagliflozin|dapagliflozin|canagliflozin|pioglitazone|rosiglitazone',
                na=False
            )
        ]
        
        if len(excluded_meds) > 0:
            excluded_meds['Start_Date'] = pd.to_datetime(excluded_meds['Start_Date'])
            recent_excluded = excluded_meds[
                (excluded_meds['Start_Date'] > (self.reference_date - timedelta(days=90))) |
                (pd.isna(excluded_meds['End_Date']))
            ]
            
            if len(recent_excluded) > 0:
                med_names = recent_excluded['Generic_Name'].unique()
                result['Eligible'] = False
                result['Failed_Criteria'].append(f"Use of excluded medication class: {', '.join(med_names)} (EXCLUSION)")
                
        # 5. Inadequate/Excessive Glycemic Control
        # Already checked in inclusion criteria - HbA1c outside 7.5-10.5% is exclusion
        
        # 6. Impaired Renal Function (eGFR < 60)
        # Already checked in inclusion criteria
        
        # 7. Significant Hepatic Impairment
        alt_tests = pt_labs[pt_labs['Test_Name'] == 'ALT']
        ast_tests = pt_labs[pt_labs['Test_Name'] == 'AST']
        
        if len(alt_tests) > 0:
            recent_alt = alt_tests.sort_values('Test_Date', ascending=False).iloc[0]['Value']
            if recent_alt > 120:  # Assuming ULN is 40, so 3x ULN = 120
                result['Eligible'] = False
                result['Failed_Criteria'].append(f"ALT {recent_alt} > 3x ULN (EXCLUSION)")
                
        if len(ast_tests) > 0:
            recent_ast = ast_tests.sort_values('Test_Date', ascending=False).iloc[0]['Value']
            if recent_ast > 120:  # Assuming ULN is 40, so 3x ULN = 120
                result['Eligible'] = False
                result['Failed_Criteria'].append(f"AST {recent_ast} > 3x ULN (EXCLUSION)")
                
        # 8. Recent Major Cardiovascular Events (within 6 months)
        cv_codes = pt_diagnoses[
            pt_diagnoses['ICD10_Code'].str.contains('I21|I63|I64|I50', na=False)
        ]
        
        if len(cv_codes) > 0:
            cv_codes['Date_First_Diagnosed'] = pd.to_datetime(cv_codes['Date_First_Diagnosed'])
            recent_cv = cv_codes[cv_codes['Date_First_Diagnosed'] > (self.reference_date - timedelta(days=180))]
            if len(recent_cv) > 0:
                result['Eligible'] = False
                result['Failed_Criteria'].append("Recent major cardiovascular event (EXCLUSION)")
                
        # 9. Uncontrolled Hypertension (SBP ≥ 170 or DBP ≥ 100)
        # Enhanced check beyond inclusion criteria
        if len(bp_tests) > 0:
            sbp_tests = bp_tests[bp_tests['Test_Name'] == 'Systolic BP']
            dbp_tests = bp_tests[bp_tests['Test_Name'] == 'Diastolic BP']
            
            if len(sbp_tests) > 0:
                recent_sbp = sbp_tests.sort_values('Test_Date', ascending=False).iloc[0]['Value']
                if recent_sbp >= 170:
                    result['Eligible'] = False
                    result['Failed_Criteria'].append(f"Uncontrolled hypertension: SBP {recent_sbp} ≥ 170 (EXCLUSION)")
                    
            if len(dbp_tests) > 0:
                recent_dbp = dbp_tests.sort_values('Test_Date', ascending=False).iloc[0]['Value']
                if recent_dbp >= 100:
                    result['Eligible'] = False
                    result['Failed_Criteria'].append(f"Uncontrolled hypertension: DBP {recent_dbp} ≥ 100 (EXCLUSION)")
                    
        # 10. Active Malignancy
        cancer_codes = pt_diagnoses[
            pt_diagnoses['ICD10_Code'].str.contains('C[0-9]|D0[0-9]', na=False) &
            ~pt_diagnoses['ICD10_Code'].str.contains('C44|D04', na=False)  # Exclude basal cell carcinoma
        ]
        
        if len(cancer_codes) > 0:
            cancer_codes['Date_First_Diagnosed'] = pd.to_datetime(cancer_codes['Date_First_Diagnosed'])
            recent_cancer = cancer_codes[
                (cancer_codes['Date_First_Diagnosed'] > (self.reference_date - timedelta(days=1825))) &  # 5 years
                (cancer_codes['Currently_Active'] == 'Y')
            ]
            if len(recent_cancer) > 0:
                result['Eligible'] = False
                result['Failed_Criteria'].append("Active malignancy within 5 years (EXCLUSION)")
                
        # 11. History of Pancreatitis
        pancreatitis_codes = pt_diagnoses[
            pt_diagnoses['ICD10_Code'].str.contains('K85|K86.1', na=False)
        ]
        
        if len(pancreatitis_codes) > 0:
            result['Eligible'] = False
            result['Failed_Criteria'].append("History of pancreatitis (EXCLUSION)")
            
        # 12. Significant Hematologic Abnormalities
        hemoglobin_tests = pt_labs[pt_labs['Test_Name'] == 'Hemoglobin']
        
        if len(hemoglobin_tests) > 0:
            recent_hgb = hemoglobin_tests.sort_values('Test_Date', ascending=False).iloc[0]['Value']
            if recent_hgb < 9.0:
                result['Eligible'] = False
                result['Failed_Criteria'].append(f"Hemoglobin {recent_hgb} g/dL < 9.0 (EXCLUSION)")
                
        return result
    
    def analyze_all_patients(self):
        """Analyze all patients in the database"""
        print("Analyzing patient eligibility for Glucofix Phase 3 Trial...")
        print("="*80)
        
        patient_ids = self.demographics['Patient_ID'].unique()
        
        for patient_id in patient_ids:
            try:
                result = self.check_patient_eligibility(patient_id)
                self.results.append(result)
            except Exception as e:
                print(f"Error analyzing patient {patient_id}: {str(e)}")
                
        return self.results
    
    def generate_summary_report(self):
        """Generate comprehensive summary statistics"""
        df_results = pd.DataFrame(self.results)
        
        eligible_count = df_results['Eligible'].sum()
        total_count = len(df_results)
        
        print(f"\n{'='*80}")
        print(f"GLUCOFIX TRIAL ELIGIBILITY SUMMARY")
        print(f"{'='*80}\n")
        
        print(f"Total Patients Screened: {total_count}")
        print(f"Eligible Patients: {eligible_count} ({eligible_count/total_count*100:.1f}%)")
        print(f"Ineligible Patients: {total_count - eligible_count} ({(total_count-eligible_count)/total_count*100:.1f}%)")
        
        # Top reasons for exclusion
        print(f"\n{'='*80}")
        print("TOP REASONS FOR INELIGIBILITY:")
        print(f"{'='*80}\n")
        
        all_failures = []
        for result in self.results:
            all_failures.extend(result['Failed_Criteria'])
            
        from collections import Counter
        failure_counts = Counter(all_failures)
        
        for reason, count in failure_counts.most_common(15):
            print(f"  {count:3d} patients: {reason}")
            
        return df_results
    
    def rank_patients_by_enrollment_likelihood(self, df_results):
        """
        Rank patients by likelihood of successful enrollment
        Based on number of warnings and complexity of follow-up required
        """
        
        # Calculate enrollment likelihood score
        def calculate_score(row):
            if not row['Eligible']:
                return 0
            
            # Base score for eligible patients
            score = 100
            
            # Deduct points for warnings
            score -= len(row['Warnings']) * 10
            
            # Bonus for having phone consent
            if 'Phone_Consent' in row['Details'] and row['Details']['Phone_Consent'] == 'Yes':
                score += 5
                
            # Bonus for optimal HbA1c (middle of range)
            if 'HbA1c' in row['Details']:
                hba1c = float(row['Details']['HbA1c'].replace('%', ''))
                if 8.5 <= hba1c <= 9.5:  # Sweet spot in middle of range
                    score += 5
                    
            # Bonus for good renal function (well above cutoff)
            if 'eGFR' in row['Details']:
                egfr = float(row['Details']['eGFR'].split()[0])
                if egfr >= 80:
                    score += 5
                    
            return score
        
        df_results['Enrollment_Score'] = df_results.apply(calculate_score, axis=1)
        df_ranked = df_results[df_results['Eligible']].sort_values('Enrollment_Score', ascending=False)
        
        return df_ranked
    
    def export_results(self, output_path):
        """Export detailed results to Excel"""
        df_results = pd.DataFrame(self.results)
        
        # Prepare detailed export
        export_data = []
        for result in self.results:
            row = {
                'Patient_ID': result['Patient_ID'],
                'Eligible': result['Eligible'],
                'Failed_Criteria': '; '.join(result['Failed_Criteria']) if result['Failed_Criteria'] else 'None',
                'Warnings': '; '.join(result['Warnings']) if result['Warnings'] else 'None',
            }
            row.update(result['Details'])
            export_data.append(row)
            
        df_export = pd.DataFrame(export_data)
        
        # Rank eligible patients
        eligible_df = df_export[df_export['Eligible'] == True].copy()
        
        # Calculate enrollment score
        eligible_df['Warning_Count'] = df_export[df_export['Eligible'] == True]['Warnings'].apply(
            lambda x: 0 if x == 'None' else len(x.split(';'))
        )
        eligible_df['Enrollment_Priority'] = eligible_df['Warning_Count'].apply(
            lambda x: 'High' if x == 0 else ('Medium' if x <= 2 else 'Low')
        )
        
        # Sort by priority
        eligible_df = eligible_df.sort_values(['Warning_Count', 'HbA1c'], 
                                              ascending=[True, True])
        
        # Write to Excel with multiple sheets
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            # All results
            df_export.to_excel(writer, sheet_name='All_Patients', index=False)
            
            # Eligible patients only (ranked)
            eligible_df.to_excel(writer, sheet_name='Eligible_Ranked', index=False)
            
            # Ineligible patients with reasons
            ineligible_df = df_export[df_export['Eligible'] == False]
            ineligible_df.to_excel(writer, sheet_name='Ineligible', index=False)
            
        print(f"\n✓ Detailed results exported to: {output_path}")


def main():
    """Main execution function"""
    
    # File path
    file_path = '/mnt/user-data/uploads/Glucofix_Patient_Records.xlsx'
    
    # Initialize checker
    checker = GlucofixEligibilityChecker(file_path)
    
    # Run analysis
    results = checker.analyze_all_patients()
    
    # Generate summary
    df_results = checker.generate_summary_report()
    
    # Rank eligible patients
    df_ranked = checker.rank_patients_by_enrollment_likelihood(df_results)
    
    print(f"\n{'='*80}")
    print("TOP 20 CANDIDATES FOR ENROLLMENT (Ranked by Likelihood):")
    print(f"{'='*80}\n")
    
    for idx, (_, row) in enumerate(df_ranked.head(20).iterrows(), 1):
        print(f"{idx:2d}. {row['Patient_ID']} (Score: {row['Enrollment_Score']:.0f})")
        
        # Show key details
        if 'HbA1c' in row['Details']:
            print(f"    HbA1c: {row['Details']['HbA1c']}", end="")
        if 'BMI' in row['Details']:
            print(f" | BMI: {row['Details']['BMI']}", end="")
        if 'eGFR' in row['Details']:
            print(f" | eGFR: {row['Details']['eGFR']}", end="")
        if 'Age' in row['Details']:
            print(f" | Age: {row['Details']['Age']}")
        else:
            print()
            
        if len(row['Warnings']) > 0:
            print(f"    Warnings: {', '.join(row['Warnings'])}")
        print()
    
    # Export results
    output_path = '/mnt/user-data/outputs/Glucofix_Eligibility_Analysis.xlsx'
    checker.export_results(output_path)
    
    print(f"\n{'='*80}")
    print("Analysis complete!")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    main()
