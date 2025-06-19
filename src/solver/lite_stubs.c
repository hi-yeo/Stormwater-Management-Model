#include "headers.h"

#ifdef LITE_KINEMATIC_ONLY
/* Dynamic wave stubs */
void dynwave_validate(void) {}
void dynwave_init(void) {}
void dynwave_close(void) {}
double dynwave_getRoutingStep(double fixedStep) { return fixedStep; }
int dynwave_execute(double tStep) { return 0; }
#endif

#ifdef LITE_NO_SNOW
/* Snowmelt stubs */
int  snow_readMeltParams(char* tok[], int ntoks) { return 0; }
int  snow_createSnowpack(int subcatch, int snowIndex) { return 1; }
void snow_validateSnowmelt(int snowIndex) {}
void snow_initSnowpack(int subcatch) {}
void snow_initSnowmelt(int snowIndex) {}
void snow_getState(int subcatch, int subArea, double x[]) {}
void snow_setState(int subcatch, int subArea, double x[]) {}
void snow_setMeltCoeffs(int snowIndex, double season) {}
void snow_plowSnow(int subcatch, double tStep) {}
double snow_getSnowMelt(int subcatch, double rainfall, double snowfall, double tStep, double *netPrecip) { return 0.0; }
double snow_getSnowCover(int subcatch) { return 0.0; }
#endif

#ifdef LITE_NO_QUALITY
/* Water quality stubs */
void qualrout_init(void) {}
void qualrout_execute(double tStep) {}
int  treatmnt_open(void) { return 1; }
void treatmnt_close(void) {}
int  treatmnt_readExpression(char* tok[], int ntoks) { return 0; }
void treatmnt_delete(int node) {}
void treatmnt_treat(int node, double q, double v, double tStep) {}
void treatmnt_setInflow(double qIn, double wIn[]) {}
void surfqual_initState(int subcatch) {}
void surfqual_getWashoff(int subcatch, double runoff, double tStep) {}
void surfqual_getBuildup(int subcatch, double tStep) {}
void surfqual_sweepBuildup(int subcatch, DateTime aDate) {}
double surfqual_getWtdWashoff(int subcatch, int pollut, double wt) { return 0.0; }
#endif
