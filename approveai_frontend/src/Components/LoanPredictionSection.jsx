import React, { useRef, useState } from "react";
import "../Style/LoanPredictionSectionDesign.css"
import {ResponsiveContainer, BarChart, Bar, XAxis, YAxis, Tooltip, Legend} from "recharts"
import axios from "axios";

const LoanPredictionSection = () => {

    const name = useRef("Null")
    const address = useRef("Null")
    const gender = useRef("Null")
    const married = useRef("Null")
    const dependence = useRef("Null")
    const education = useRef("Null")
    const selfEmployee = useRef("Null")
    const appillicantIncome = useRef("Null")
    const coapplicant = useRef("Null")
    const loanamount = useRef("Null")
    const loanamountterm = useRef("Null")
    const credithistory = useRef("Null")
    const propertyarea = useRef("Null")

    const loanResult=useRef()

    const [aprovedPercentage,setAprovedPercentage]=useState(0)
    const [rejectedPercentage,setRegectedPercentage]=useState(0)
    const [status,setStatus]=useState("Null")

    const arrayData = [
        {
            xaxisData : "Approved",
            yaxisData : "70%",
            Approved : aprovedPercentage,
        },

        {
            xaxisData : "Rejected",
            yaxisData : "30%",
            Rejected : rejectedPercentage,
        },
    ]

    const PredictBTNClicked = async() =>{

        const sendedData={
            FullName:name.current.value,
            Address:address.current.value,
            Gender:gender.current.value,
            Married:married.current.value,
            Dependents:dependence.current.value,
            Education:education.current.value,
            SelfEmployed:selfEmployee.current.value,
            ApplicantIncome:appillicantIncome.current.value,
            CoapplicantIncome:coapplicant.current.value,
            LoanAmount:loanamount.current.value,
            LoanAmountTerm:loanamountterm.current.value,
            CreditHistory:credithistory.current.value,
            PropertyArea:propertyarea.current.value,
        }

        if(name.current.value !== "" && address.current.value !== "" && gender.current.value !== "" && married.current.value !== "" && dependence.current.value !== "" && education.current.value !== "" && selfEmployee.current.value !== "" && loanamountterm.current.value !== "" && credithistory.current.value !== "" && propertyarea.current.value !== "" && appillicantIncome.current.value !== "" && coapplicant.current.value !== "" && loanamount.current.value !== ""){
            
            const response = await axios.post("http://127.0.0.1:8000/loan", sendedData);
        
            if (response.data.message === "ok") {

                loanResult.current.style.display="flex"
                
                setAprovedPercentage(parseInt(response.data.Approved_Percentage))
                setRegectedPercentage(parseInt(response.data.Rejected_Percentage))
                if (response.data.Status === "Approved") {
                    setStatus("🎉 Congratulations! Your Loan is Approved!<br/><br/>Dear Sir, your loan application has been approved! 🚀<br/>You're just a step away from achieving your dreams.<br/>Thank you for trusting us to make it possible! 💼✨")
                }
                else{
                    setStatus("😔 Oops! Your Loan Application Wasn't Approved.<br/><br/>Dear Sir, unfortunately, your loan application didn’t meet the criteria this time.<br/>Don’t lose heart – every setback is a setup for a comeback! 🌟<br/>You can always reach out for assistance or reapply when ready.")
                }
            }
            else {
                alert("Something is going to wrong, Please try again !!");
            }
        }
        else{
            alert("Some fields are empty")
        }

    }


    return (
        <div className="loanprediction-main-section">
            <div className="loanprediction-section">
                <h1>Loan Prediction</h1>

                <div className="agileits-top">
                    <form>
                        <input className="text" type="text" name="Username" ref={name} placeholder="Full Name" required />
                        <input className="text" type="text" name="Username" ref={address} placeholder="Address" required />
                        
                        <label className="fieldLabel">Gender</label>
                        <select className="selectField" ref={gender} defaultValue="Male">
                            <option value="Male">Male</option>
                            <option value="Female">Female</option>
                        </select>

                        <label className="fieldLabel">Married</label>
                        <select className="selectField" ref={married} defaultValue="Yes">
                            <option value="Yes">Yes</option>
                            <option value="No">No</option>
                        </select>

                        <label className="fieldLabel">Dependents</label>
                        <select className="selectField" ref={dependence} defaultValue="0">
                            <option value="0">0</option>
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3+">3+</option>
                        </select>

                        <label className="fieldLabel">Education</label>
                        <select className="selectField" ref={education} defaultValue="Graduate">
                            <option value="Graduate">Graduate</option>
                            <option value="Not Graduate">Not Graduate</option>
                        </select>

                        <label className="fieldLabel">Self Employed</label>
                        <select className="selectField" ref={selfEmployee} defaultValue="No">
                            <option value="No">No</option>
                            <option value="Yes">Yes</option>
                        </select>

                        <input className="text" type="text" ref={appillicantIncome} name="ApplicantIncome" placeholder="Applicant Income" required />
                        <input className="text" type="text" ref={coapplicant} name="CoapplicantIncome" placeholder="Coapplicant Income" required />
                        <input className="text" type="text" ref={loanamount} name="LoanAmount" placeholder="LoanAmount" required />

                        <label className="fieldLabel">Loan Amount Term</label>
                        <select className="selectField" ref={loanamountterm} defaultValue="No">
                            <option value="360">360</option>
                            <option value="180">180</option>
                        </select>

                        <label className="fieldLabel">Credit History</label>
                        <select className="selectField" ref={credithistory} defaultValue="1">
                            <option value="1">1</option>
                            <option value="0">0</option>
                        </select>

                        <label className="fieldLabel">Property Area</label>
                        <select className="selectField" ref={propertyarea} defaultValue="Urban">
                            <option value="Urban">Urban</option>
                            <option value="Rural">Rural</option>
                            <option value="Semiurban">Semiurban</option>
                        </select>

                        <input type="button" defaultValue="Predict" onClick={PredictBTNClicked} />
                    </form>
                </div>

            </div>

            <div className="prediction-result" ref={loanResult}>
                <h2>Loan Approval Status</h2>

                <p className="prediction" dangerouslySetInnerHTML={{ __html: status }}></p>

                <ResponsiveContainer width="90%" aspect={2}>
                    <BarChart data={arrayData} width={400} height={400}>
                        <XAxis dataKey="xaxisData"/>
                        <YAxis />
                        <Tooltip />
                        <Legend />
                        <Bar dataKey="Approved" fill="#04e762" stackId="a"/>
                        <Bar dataKey="Rejected" fill="#ff0000" stackId="a"/>
                    </BarChart>
                </ResponsiveContainer>
            </div>
        </div>
    )
}

export default LoanPredictionSection