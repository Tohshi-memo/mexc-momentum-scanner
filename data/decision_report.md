# Decision Report

- generated_at: 2026-05-01T12:32:12.123502+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **2796**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=2796, expectancy=-0.12%
- 直近20件 MARKET基準: n=20, expectancy=-1.61%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.61% | **-1.61%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 9/20 | 45.0% | +1.94% | **+0.87%** |
| LIMIT_7PCT | 7/20 | 35.0% | +2.34% | **+0.82%** |
| LIMIT_9PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 5/20 | 25.0% | +1.48% | **+0.37%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +3.13% | **+2.97%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +3.26% | **+2.44%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +2.81% | **+1.69%** |
| MARKET_LONG | 20/20 | 100.0% | +1.61% | **+1.61%** |
| ASK_LONG | 20/20 | 100.0% | +0.85% | **+0.85%** |

## 2. $100 Live Portfolio

- 残高: **$102.51** / 初期 $100.00 (+2.51%)
- 確定トレード: 4件 (TP 3 / SL 1 / EXP 0)
- 最新: PLAY/USDT:USDT TP_HIT PnL +7.74% 残高後 $102.51
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Latest Market Context

- 更新: 2026-05-01T12:32:09.798210+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.45% price=77781.7
- Funnel: target 760 → liquid 198 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 80.9 >= 65=1, 4h RSI 75.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| B/USDT:USDT | +66.23% | $13,538,225.68 |
| UB/USDT:USDT | +60.30% | $19,117,227.09 |
| BR/USDT:USDT | +39.09% | $25,361,607.73 |
| NFP/USDT:USDT | +35.80% | $1,265,307.80 |
| ORCA/USDT:USDT | +34.32% | $11,178,558.77 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NFP/USDT:USDT | below_relative_strength | +5.30% | +4.85% |
| ORCA/USDT:USDT | below_1h_threshold | +2.84% | +2.39% |
| ENSO/USDT:USDT | below_1h_threshold | +1.39% | +0.93% |
| B/USDT:USDT | below_1h_threshold | +1.19% | +0.74% |
| LAB/USDT:USDT | below_1h_threshold | +1.07% | +0.62% |

## 4. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
