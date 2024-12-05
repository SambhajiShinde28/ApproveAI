import React from "react";
import '../Style/ApprovedAIDesign.css'
import HeaderComp from './HeaderComp.jsx'
import LoanPredictionSection from "./LoanPredictionSection.jsx"

const ApprovedAI=()=>{
    return(
        <>
            <div className="main-container">
                <HeaderComp></HeaderComp>
                <LoanPredictionSection></LoanPredictionSection>
            </div>
        </>
    )
}

export default ApprovedAI