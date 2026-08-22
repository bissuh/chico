/**
 * Font loading. Swap these two imports to change the typeface across every
 * slide and reel at once, then update THEME.fonts in theme.ts so the names
 * match what is actually loaded.
 *
 * Any family in @remotion/google-fonts works. The import path is the family
 * name with no spaces: PlayfairDisplay, SpaceGrotesk, Anton, Lora.
 *
 * Load only the weights the components actually use. Loading a whole family
 * fires ~100 network requests per render and slows every frame.
 */
import {loadFont as loadSans} from '@remotion/google-fonts/Inter';
import {loadFont as loadMono} from '@remotion/google-fonts/JetBrainsMono';

export const {fontFamily: SANS} = loadSans('normal', {
  weights: ['400', '500', '600', '700', '800'],
  subsets: ['latin', 'latin-ext'],
});

export const {fontFamily: MONO} = loadMono('normal', {
  weights: ['400', '700'],
  subsets: ['latin', 'latin-ext'],
});
