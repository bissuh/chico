import {AbsoluteFill, Img, useCurrentFrame, staticFile} from 'remotion';
import {loadFont as loadAnton} from '@remotion/google-fonts/Anton';
import {loadFont as loadPlayfair} from '@remotion/google-fonts/PlayfairDisplay';

const {fontFamily: ANTON} = loadAnton();
const {fontFamily: PLAYFAIR} = loadPlayfair('normal', {weights: ['900'], subsets: ['latin']});

const TEAL = '#2A7A6D';
const TEAL_BRIGHT = '#3FA08F';
const SANS = '"Helvetica Neue", Helvetica, Arial, sans-serif';

export type SlideProps = {
  bg?: string;
  slideNo?: number;
  slideTotal?: number;
  kicker?: string; // small format/topic label, top-left under wordmark
  accentTop?: string; // teal italic line above the headline
  headline?: string; // the big Anton line(s)
  body?: string; // optional supporting paragraph
  footnote?: string; // bottom line: CTA or source
  handle?: string;
};

const resolveSrc = (raw?: string) => {
  if (!raw) return undefined;
  if (raw.startsWith('http')) return raw;
  return staticFile(raw);
};

const Grain: React.FC = () => {
  const frame = useCurrentFrame();
  return (
    <AbsoluteFill
      style={{
        opacity: 0.05,
        mixBlendMode: 'overlay',
        backgroundImage: `radial-gradient(circle at ${20 + (frame % 30)}% ${30 + (frame % 25)}%, white 1px, transparent 2px)`,
        backgroundSize: '6px 6px',
        pointerEvents: 'none',
      }}
    />
  );
};

export const CarouselSlide: React.FC<SlideProps> = ({
  bg,
  slideNo,
  slideTotal,
  kicker,
  accentTop,
  headline,
  body,
  footnote,
  handle = '@thebillionperson',
}) => {
  const src = resolveSrc(bg);

  return (
    <AbsoluteFill style={{backgroundColor: '#0c1413'}}>
      {/* Doré background */}
      {src ? (
        <AbsoluteFill style={{overflow: 'hidden'}}>
          <Img src={src} style={{width: '100%', height: '100%', objectFit: 'cover', transform: 'scale(1.04)'}} />
        </AbsoluteFill>
      ) : (
        <AbsoluteFill style={{background: `linear-gradient(180deg, ${TEAL} 0%, #16332e 100%)`}} />
      )}

      {/* teal wash + legibility scrim */}
      <AbsoluteFill style={{backgroundColor: TEAL, mixBlendMode: 'multiply', opacity: 0.5}} />
      <AbsoluteFill
        style={{
          background:
            'linear-gradient(180deg, rgba(0,0,0,0.55) 0%, rgba(0,0,0,0.15) 32%, rgba(0,0,0,0.35) 62%, rgba(0,0,0,0.82) 100%)',
        }}
      />

      {/* content */}
      <AbsoluteFill style={{padding: 84, display: 'flex', flexDirection: 'column', justifyContent: 'space-between'}}>
        {/* top row */}
        <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start'}}>
          <div>
            <div
              style={{
                fontFamily: ANTON,
                fontSize: 30,
                letterSpacing: '0.18em',
                color: 'white',
                textTransform: 'uppercase',
                textShadow: '0 2px 10px rgba(0,0,0,0.7)',
              }}
            >
              The Billion Person
            </div>
            {kicker ? (
              <div
                style={{
                  fontFamily: SANS,
                  fontSize: 24,
                  letterSpacing: '0.22em',
                  color: TEAL_BRIGHT,
                  textTransform: 'uppercase',
                  fontWeight: 700,
                  marginTop: 12,
                  textShadow: '0 2px 8px rgba(0,0,0,0.8)',
                }}
              >
                {kicker}
              </div>
            ) : null}
          </div>
          {slideNo ? (
            <div
              style={{
                fontFamily: PLAYFAIR,
                fontStyle: 'italic',
                fontWeight: 900,
                fontSize: 44,
                color: 'white',
                textShadow: '0 2px 12px rgba(0,0,0,0.8)',
              }}
            >
              {String(slideNo).padStart(2, '0')}
              <span style={{color: TEAL_BRIGHT, fontSize: 30}}>/{String(slideTotal ?? 8).padStart(2, '0')}</span>
            </div>
          ) : null}
        </div>

        {/* headline block, weighted to lower third */}
        <div style={{marginTop: 'auto', marginBottom: 24}}>
          {accentTop ? (
            <div
              style={{
                fontFamily: PLAYFAIR,
                fontStyle: 'italic',
                fontWeight: 900,
                fontSize: 52,
                color: TEAL_BRIGHT,
                marginBottom: 22,
                textShadow: '0 4px 18px rgba(0,0,0,0.8)',
              }}
            >
              {accentTop}
            </div>
          ) : null}
          {headline ? (
            <div
              style={{
                fontFamily: ANTON,
                fontWeight: 400,
                fontSize: 104,
                lineHeight: 0.98,
                color: 'white',
                textTransform: 'uppercase',
                letterSpacing: '0.005em',
                textShadow: '0 6px 30px rgba(0,0,0,0.65), 0 2px 8px rgba(0,0,0,0.9)',
                maxWidth: 880,
              }}
            >
              {headline}
            </div>
          ) : null}
          {body ? (
            <div
              style={{
                fontFamily: SANS,
                fontWeight: 500,
                fontSize: 40,
                lineHeight: 1.3,
                color: 'rgba(255,255,255,0.94)',
                marginTop: 30,
                maxWidth: 840,
                textShadow: '0 3px 16px rgba(0,0,0,0.8)',
              }}
            >
              {body}
            </div>
          ) : null}
        </div>

        {/* bottom row */}
        <div style={{display: 'flex', flexDirection: 'column', gap: 18}}>
          <div style={{height: 6, width: 130, background: TEAL_BRIGHT, borderRadius: 3}} />
          <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center'}}>
            <div
              style={{
                fontFamily: SANS,
                fontWeight: 700,
                fontSize: 32,
                color: 'white',
                letterSpacing: '0.02em',
                textShadow: '0 2px 10px rgba(0,0,0,0.8)',
              }}
            >
              {handle}
            </div>
            {footnote ? (
              <div
                style={{
                  fontFamily: SANS,
                  fontWeight: 600,
                  fontSize: 28,
                  color: TEAL_BRIGHT,
                  letterSpacing: '0.04em',
                  textTransform: 'uppercase',
                  textShadow: '0 2px 10px rgba(0,0,0,0.8)',
                }}
              >
                {footnote}
              </div>
            ) : null}
          </div>
        </div>
      </AbsoluteFill>

      <Grain />
      <AbsoluteFill
        style={{
          background: 'radial-gradient(circle at center, transparent 52%, rgba(0,0,0,0.4) 100%)',
          pointerEvents: 'none',
        }}
      />
    </AbsoluteFill>
  );
};
