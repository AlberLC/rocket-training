using System.Collections;
using System.Collections.Generic;
using System.Linq;

using UnityEngine;

public class Satelite : EsferaCeleste
{
    [SerializeField]
    private CuerpoCeleste planeta = null;
    
    private void Start()
    {
        Vector3 direccionPlaneta = planeta.Posicion - transform.position;
        Vector3 direccionInicial = Quaternion.Euler(0, 0, -90) * direccionPlaneta.normalized;
        float velocidadInicial = Mathf.Sqrt((float)(g * planeta.Masa / direccionPlaneta.magnitude));

        RigidBody.AddForce(direccionInicial * velocidadInicial, ForceMode.VelocityChange);
    }

    private void FixedUpdate()
    {
        RigidBody.AddForce(planeta.GetFuerzaAtraccion(this));
    }

}
