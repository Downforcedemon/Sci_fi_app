package scifimuseum.com.exoplanetsearch;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class LightCurve {
    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private Long id;

    private String ticId; // TESS Input Catalog ID
    private Double ra; // Right Ascension
    private Double dec; // Declination
    private Double pmRA; // Proper Motion in RA
    private Double pmDEC; // Proper Motion in DEC
    private Double tessMag; // TESS Magnitude
    private String objType; // Object Type
    private String typeSrc; // Source of Type
    private String version; // Data Version
    private String hip; // HIP Catalog ID
    private String tyc; // TYC Catalog ID
    private String ucac; // UCAC Catalog ID
    private String twoMass; // 2MASS ID
    private String sdss; // SDSS ID
    private String allwise; // ALLWISE ID
    private String gaia; // GAIA ID
    private String apass; // APASS ID
    private String kic; // KIC ID
    private Double ePmRA; // Error in Proper Motion RA
    private Double ePmDEC; // Error in Proper Motion DEC
    private Double plx; // Parallax
    private Double ePlx; // Error in Parallax
    // ... additional fields for magnitude and errors in various bands
    private Double teff; // Effective Temperature
    private Double eTeff; // Error in Effective Temperature
    private Double logg; // Surface Gravity
    private Double eLogg; // Error in Surface Gravity
    private Double mh; // Metallicity
    private Double eMh; // Error in Metallicity
    private Double rad; // Stellar Radius
    private Double eRad; // Error in Stellar Radius
    private Double mass; // Stellar Mass
    private Double eMass; // Error in Stellar Mass
    private String lumClass; // Luminosity Class
    private Double lum; // Stellar Luminosity
    private Double eLum; // Error in Stellar Luminosity
    private Double distance; // Distance
    private Double eDistance; // Error in Distance
    private Double ebv; // E(B-V) Reddening
    private Double eEbv; // Error in E(B-V)
    private Integer numCont; // Number of Sources in Aperture
    private Double contRatio; // Contamination Ratio
    

    // constructor
    public LightCurve(String ticId, Double ra, Double dec, Double pmRA /*, other parameters */) {
        this.ticId = ticId;
        this.ra = ra;
        this.dec = dec;
        this.pmRA = pmRA;
        // Initialize other fields
    }

    // Example getters and setters
    public String getTicId() {
        return ticId;
    }

    public void setTicId(String ticId) {
        this.ticId = ticId;
    }

    public Double getRa() {
        return ra;
    }

    public void setRa(Double ra) {
        this.ra = ra;
    }

    public Double getDec() {
        return dec;
    }

    public void setDec(Double dec) {
        this.dec = dec;
    }

    public Double getPmRA() {
        return pmRA;
    }

    public void setPmRA(Double pmRA) {
        this.pmRA = pmRA;
    }

    
}
