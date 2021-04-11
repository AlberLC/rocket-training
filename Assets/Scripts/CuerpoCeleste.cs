using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(Rigidbody))]
public class CuerpoCeleste : MonoBehaviour
{
    //private const float realG = 6.674e-11;
    protected const float g = 1e-6f;
    private Rigidbody rigidBody;
    

    public float Masa => RigidBody.mass;    
    public Rigidbody RigidBody { get { return rigidBody; } private set { rigidBody = value; } }
    public Vector3 Posicion => transform.position;
    public Vector3 Rotacion => transform.rotation.eulerAngles;

    protected virtual void Awake()
    {
        RigidBody = GetComponent<Rigidbody>();
    }

    // --------------------------------------------------------------------------------
    public Vector3 GetFuerzaAtraccion(CuerpoCeleste cc)
    {
        float moduloAtraccion = cc.Masa * rigidBody.mass / Mathf.Pow(Vector3.Distance(cc.Posicion, rigidBody.position), 2) * g;
        Vector3 direccionPlaneta = rigidBody.position - cc.Posicion;
        return direccionPlaneta.normalized * moduloAtraccion;
    }
}
