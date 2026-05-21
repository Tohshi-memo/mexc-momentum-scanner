# Decision Report

- generated_at: 2026-05-21T13:53:58.727094+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4631**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4631, expectancy=-0.10%
- 直近20件 MARKET基準: n=20, expectancy=-0.23%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.23% | **-0.23%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 4/17 | 23.5% | +2.69% | **+0.63%** |
| LIMIT_5PCT | 5/20 | 25.0% | +2.36% | **+0.59%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |
| LIMIT_6PCT | 3/20 | 15.0% | +1.89% | **+0.28%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +0.98% | **+0.44%** |
| LIMIT_2PCT_LONG | 13/20 | 65.0% | +0.51% | **+0.33%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +0.49% | **+0.25%** |
| MARKET_LONG | 20/20 | 100.0% | +0.11% | **+0.11%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +0.18% | **+0.09%** |

## 2. $100 Live Portfolio

- 残高: **$95.73** / 初期 $100.00 (-4.27%)
- 確定トレード: 59件 (TP 15 / SL 41 / EXP 3)
- 最新: BSB/USDT:USDT SL_HIT PnL -4.00% 残高後 $95.73
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$121.41** / 初期 $100.00 (+21.41%)
- 確定: 546件 (Win 138 / Loss 185 / Flat 223) / skip 646件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.036% per trade / maxDD +4.21%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PROVE/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $121.41

## 4. Latest Market Context

- 更新: 2026-05-21T13:53:53.283720+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.36% price=76965.8
- Funnel: target 766 → liquid 138 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 66.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| NEX/USDT:USDT | +43.32% | $1,366,490.66 |
| EDEN/USDT:USDT | +42.31% | $33,602,356.52 |
| ROAM/USDT:USDT | +39.08% | $2,309,428.62 |
| PROVE/USDT:USDT | +38.12% | $6,416,417.99 |
| FIDA/USDT:USDT | +36.47% | $14,489,059.33 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BEAT/USDT:USDT | below_1h_threshold | +4.82% | +5.18% |
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +4.07% | +4.43% |
| LIT/USDT:USDT | below_1h_threshold | +3.13% | +3.49% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +3.04% | +3.40% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +2.86% | +3.22% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
