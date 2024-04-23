import { Card, CardTitle } from '@/components/ui/card'
import { useSelections } from '@baml/playground-common'
import { useAtom } from 'jotai'
import Joyride, { Placement, TooltipProps } from 'react-joyride'
import { productTourDoneAtom } from '../_atoms/atoms'

export const Tour = () => {
  const steps = [
    {
      target: '.tour-editor',
      content:
        'Welcome! PromptFiddle is a playground to share and test prompt templates. Prompts here are modeled like functions',
      disableBeacon: true,
      placement: 'auto' as Placement,
    },
    // {
    //   // ..that can convert these definitions into actual Python or TS functions
    //   target: '.tour-editor',
    //   content: 'LLM functions are written using BAML, a superset of the Jinja language.',
    //   placement: 'right' as Placement,
    // },
    {
      target: '.tour-prompt-preview',
      content: (
        <div>
          <p>See a realtime preview of the exact prompt, including ifs, loops, and inputs.</p>
          <br />
          <p className="font-semibold"> No guessing what the prompt is!</p>
        </div>
      ),
      placement: 'left' as Placement,
    },
    {
      target: '.tour-test-panel',
      content: "Click 'Run all' to test this LLM function!",
      placement: 'left-start' as Placement,
    },

    // {
    //   target: '.tour-templates',
    //   content: 'Check out other templates to learn different prompting strategies',
    // },
  ]
  const [productTourDone, setProductTourDone] = useAtom(productTourDoneAtom)
  if (productTourDone) {
    return null
  }

  return (
    <div className="">
      <Joyride
        steps={steps}
        continuous={true}
        disableOverlayClose={true}
        spotlightClicks={true}
        showProgress={true}
        hideCloseButton={true}
        disableCloseOnEsc={true}
        showSkipButton={false}
        callback={(data) => {
          if (data.status === 'finished') {
            setProductTourDone(true)
          }
        }}
        styles={{
          options: {
            overlayColor: 'rgba(0, 0, 0, 0.7)',
          },
        }}
      />
    </div>
  )
}