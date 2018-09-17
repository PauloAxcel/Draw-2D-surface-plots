# Draw-2D-surface-plots
  Updated 7 minutes ago In this work I have a function y = f(x1,x2) where the dependence is unknown. However there is a hidden dependece. This work is based on results obtained from COMSOL Multiphysics 5.2(R). Where we want to identify the optical field enhancement of different surface patterns. The data obtained is related to the surface patterns and correspondent enhancement obtained. In this case we want to check how different roughness sizes influence the enhancement. The roughness is characterized by 2 dimensions x1 and x2 and the enhancement is given by y. After the combination of multiple values for x1 and x2 we built a matrix with dimension x1.size and x2.size with values corresponding to the enhacement. This matrix is afterwards converted into a 2d surface map plot. The enhancement value goes from 1 &lt; Enh ~&lt; 10^12 so a convinient way to present the data is through log10 of the enhancement.