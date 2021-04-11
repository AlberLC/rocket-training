using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using UnityEngine;

public class Nave : CuerpoCeleste
{
    [SerializeField]
    private float combustible;
    private bool contacto;
    private ConectorExterno conectorExterno;
    private EsferaCeleste[] esferasCelestes;

    public float Combustible { get { return combustible; } set { combustible = value; } }

    protected override void Awake()
    {
        base.Awake();
        esferasCelestes = FindObjectsOfType<EsferaCeleste>().ToArray();
    }

    private void Start()
    {
        contacto = false;
        conectorExterno = new ConectorExterno(@"C:\Users\FlanaPC\Documents\Unity\Pruebas\Assets\ScriptsExternos\main.py");
        StartCoroutine(CorFixedUpdate());
    }

    private void FixedUpdate()
    {
        Vector3 fuerzaTotal = esferasCelestes.Select(c => c.GetFuerzaAtraccion(this)).Aggregate((a, b) => a + b);
        RigidBody.AddForce(fuerzaTotal);
    }

    private void OnCollisionStay(Collision collision)
    {
        contacto = true;
    }

    private void OnCollisionExit(Collision collision)
    {
        contacto = false;
    }

    IEnumerator CorFixedUpdate()
    {
        float angulo, potencia;
        Datos datos;

        while (true)
        {
            datos = new Datos() {
                g = g,
                datosNave = new DatosNave() {
                    nombre = "FlanaNave",
                    posicion = Posicion,
                    velocidad = RigidBody.velocity,
                    masa = Masa,
                    altura = 2.1f,
                    ancho = 1.5f,
                    angulo = Rotacion.z,
                    combustible = Combustible
                },
                datosEsferasCelestes = esferasCelestes.Select(c => new DatosEsferaCeleste()
                {
                    nombre = c.name,
                    posicion = c.Posicion,
                    velocidad = c.RigidBody.velocity,
                    masa = c.Masa,
                    radio = c.Radio
                }).ToArray()
            };

            conectorExterno.EnviarDatos(datos);
            yield return new WaitUntil(conectorExterno.HayDatos);            
            (angulo, potencia) = conectorExterno.RecibirDatos();

            if (!contacto)
            {
                //RigidBody.rotation = Quaternion.Euler(0, 0, angulo);
                RigidBody.MoveRotation(Quaternion.Lerp(transform.rotation, Quaternion.Euler(0, 0, angulo), Time.fixedDeltaTime * 1));
            }

            if (potencia > 0)
            {
                potencia *= 3.2f;
                potencia -= 3.1f;
                RigidBody.AddForce(transform.right * potencia);
            }
        }
    }
}
