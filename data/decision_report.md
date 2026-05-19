# Decision Report

- generated_at: 2026-05-19T14:23:41.949439+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **4471**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=4471, expectancy=-0.09%
- 直近20件 MARKET基準: n=20, expectancy=-0.69%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.69% | **-0.69%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_3PCT | 14/20 | 70.0% | +0.46% | **+0.32%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.95% | **+0.29%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +0.33% | **+0.16%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +1.45% | **+0.14%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 4/6 | 66.7% | +3.17% | **+2.11%** |
| LIMIT_ATR_LONG | 15/20 | 75.0% | +1.54% | **+1.16%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +5.53% | **+0.83%** |
| MARKET_LONG | 20/20 | 100.0% | +0.65% | **+0.65%** |
| LIMIT_7PCT_LONG | 6/20 | 30.0% | +1.92% | **+0.58%** |

## 2. $100 Live Portfolio

- 残高: **$96.21** / 初期 $100.00 (-3.79%)
- 確定トレード: 55件 (TP 14 / SL 38 / EXP 3)
- 最新: EDEN/USDT:USDT SL_HIT PnL -4.00% 残高後 $96.21
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$123.33** / 初期 $100.00 (+23.33%)
- 確定: 468件 (Win 124 / Loss 161 / Flat 183) / skip 564件
- 成長率目線: 平均log +0.000448 / 幾何平均 +0.045% per trade / maxDD +4.21%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RON/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $123.33

## 4. Latest Market Context

- 更新: 2026-05-19T14:23:37.407299+00:00 / 保存件数 288/288
- BTC: BEARISH 1h -0.58% price=76393.6
- Funnel: target 764 → liquid 137 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RON/USDT:USDT | +33.68% | $14,160,918.74 |
| PLAY/USDT:USDT | +28.87% | $5,600,317.46 |
| EDEN/USDT:USDT | +22.29% | $3,685,799.31 |
| ONT/USDT:USDT | +11.95% | $2,247,495.89 |
| ONDO/USDT:USDT | +7.79% | $69,498,008.82 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LIT/USDT:USDT | below_1h_threshold | +0.55% | +1.13% |
| AXS/USDT:USDT | below_1h_threshold | +0.34% | +0.92% |
| EDEN/USDT:USDT | below_1h_threshold | +0.27% | +0.86% |
| BRKBSTOCK/USDT:USDT | below_1h_threshold | +0.12% | +0.70% |
| RON/USDT:USDT | below_1h_threshold | +0.09% | +0.67% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
