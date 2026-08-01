import { useEffect, useRef, useState } from "react";
import { CheckCircle2, Loader2, Circle } from "lucide-react";
import "./PipelineProgress.css";

const STEPS = [
  "Cloning repository",
  "Analyzing project structure",
  "Running AI analysis",
  "Generating documentation",
];

const formatElapsed = (seconds) => {
  const m = Math.floor(seconds / 60).toString().padStart(2, "0");
  const s = Math.floor(seconds % 60).toString().padStart(2, "0");
  return `${m}:${s}`;
};


function PipelineProgress({ active = true }) {

  const [stepIndex, setStepIndex] = useState(0);
  const [elapsed, setElapsed] = useState(0);

  const stepIntervalRef = useRef(null);
  const timerIntervalRef = useRef(null);


  useEffect(() => {

    if (!active) return;


    stepIntervalRef.current = setInterval(() => {

      setStepIndex(prev =>
        prev < STEPS.length - 1
          ? prev + 1
          : prev
      );

    }, 2000);



    timerIntervalRef.current = setInterval(() => {

      setElapsed(prev => prev + 1);

    },1000);



    return () => {

      clearInterval(stepIntervalRef.current);
      clearInterval(timerIntervalRef.current);

    };


  },[active]);



  const progressPercent =
    Math.min(
      Math.round(
        ((stepIndex + 1) / STEPS.length) * 100
      ),
      95
    );



  return (

    <div className="pipeline-progress">


      <div className="pipeline-progress-header">

        <div>

          <h3>
            Analyzing Repository
          </h3>

          <p>
            Processing your repository...
          </p>

        </div>


        <div className="elapsed-time">
          Elapsed: {formatElapsed(elapsed)}
        </div>

      </div>



      <div className="progress-bar-track">

        <div
          className="progress-bar-fill"
          style={{
            width:`${progressPercent}%`
          }}
        />

      </div>



      <div className="progress-percent">
        {progressPercent}%
      </div>





      <ol className="pipeline-steps">


        {STEPS.map((label,index)=>{


          const state =
            index < stepIndex
            ? "done"
            : index === stepIndex
            ? "active"
            : "pending";


          return (

            <li
              key={label}
              className={`pipeline-step ${state}`}
            >

              <span className="step-marker">

                {
                  state==="done" &&
                  <CheckCircle2 size={16}/>
                }


                {
                  state==="active" &&
                  <Loader2
                    size={16}
                    className="spin-icon"
                  />
                }


                {
                  state==="pending" &&
                  <Circle size={14}/>
                }


              </span>


              <span className="step-label">
                {label}
              </span>


            </li>

          );


        })}


      </ol>


    </div>

  );

}


export default PipelineProgress;