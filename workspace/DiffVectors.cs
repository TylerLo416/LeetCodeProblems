using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DiffVectors : MonoBehaviour
{
    ////The two robots 
    //[SerializeField] private GameObject refRobot;
    //[SerializeField] private GameObject userRobot;

    //The vector arrows 
    [SerializeField] private GameObject[] diffArrows;
    private Vector3[] diffOgScales; 

    //The array of joints to be compared 
    [SerializeField] private GameObject[] userJoints;
    [SerializeField] private GameObject[] refJoints;

    //transform.rotation = Quaternion.LookRotation(directionVector);

    // Start is called before the first frame update
    void Start()
    {
        diffOgScales = new Vector3[diffArrows.Length]; 
        for (int index = 0; index < userJoints.Length; index++)
        {
            //Get original scales of arrows 
            diffOgScales[index] = diffArrows[index].transform.localScale;
        }
    }

    // Update is called once per frame
    void Update()
    {
        for (int index = 0; index < userJoints.Length; index++)
        {
            //Set diff arrow to position of the user's joints 
            diffArrows[index].transform.position = userJoints[index].transform.position;

            //Calculate the difference vector 
            Vector3 direction = refJoints[index].transform.position - userJoints[index].transform.position;

            //Set color based on diff vector magnitude 
            float mag = direction.magnitude;

            //Set rotation of the arrow if vector is not (0,0,0)
            if(mag > Mathf.Epsilon) 
            {
                diffArrows[index].transform.rotation = Quaternion.LookRotation(direction, Vector3.up);
            }
            //Debug.Log(mag); 
                if (mag > .3)
                {
                    setColor(diffArrows[index], Color.red); 
                }
                else if (mag < .1)
                {
                    //setColor(diffArrows[index], Color.green);
                    setColor(diffArrows[index], new Color(0.0f, 1.0f, 0.0f, 0.0f));
                }
                else
                {
                    setColor(diffArrows[index], Color.yellow);
                }
            //Reveal Red arrows, then Yellow arrows; Do not reveal green arrows
            /*int redArrowCount = 0;

            for (int i = 0; i < diffArrows.Length; i++)
            {
                if (diffArrows[i].color == Color.red)
                {
                    redArrowCount++;
                }
            }*/

            //diffArrows[index].transform.localScale = new Vector3(mag * diffOgScales[index].x, diffArrows[index].transform.localScale .y, diffArrows[index].transform.localScale .z); 
        }
    }

    void setColor(GameObject arrow, Color arrowColor)
    {
        Transform arrowMesh = arrow.transform.GetChild(0); 
        arrowMesh.GetComponent<Renderer>().material.color = arrowColor;
        arrowMesh.GetChild(0).GetComponent<Renderer>().material.color = arrowColor; 
    }
}