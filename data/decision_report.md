# Decision Report

- generated_at: 2026-10-01T10:31:32.980099+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15891**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=15891, expectancy=-0.00%
- 直近20件 MARKET基準: n=20, expectancy=-1.59%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.59% | **-1.59%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT | 9/20 | 45.0% | +0.95% | **+0.43%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_4PCT | 15/20 | 75.0% | +0.05% | **+0.04%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +0.12% | **+0.02%** |
| LIMIT_ATR | 17/20 | 85.0% | -0.45% | **-0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/7 | 71.4% | +4.01% | **+2.86%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +2.62% | **+2.36%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.68% | **+1.87%** |
| MARKET_LONG | 20/20 | 100.0% | +1.22% | **+1.22%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.33% | **+1.05%** |

## 2. $100 Live Portfolio

- 残高: **$120.75** / 初期 $100.00 (+20.75%)
- 確定トレード: 225件 (TP 82 / SL 136 / EXP 7)
- 最新: XLM/USDT:USDT SL_HIT PnL -2.52% 残高後 $120.75
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,291.04** / 初期 $100.00 (+1191.04%)
- 確定: 6010件 (Win 1779 / Loss 1932 / Flat 2299) / skip 6442件
- 成長率目線: 平均log +0.000426 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,291.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$267.83** / 初期 $100.00 (+167.83%)
- 確定: 3544件 (Win 979 / Loss 813 / Flat 1752) / skip 5758件
- 成長率目線: 平均log +0.000278 / 幾何平均 +0.028% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1375 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: LONGXIA/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $267.83

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 4052件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000270 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-01T10:31:16.789565+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.06% price=83692.0
- Funnel: target 1097 → liquid 176 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI n/a=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| MOVR/USDT:USDT | +65.74% | $17,042,659.22 |
| CT/USDT:USDT | +28.25% | $5,757,905.58 |
| NOM/USDT:USDT | +25.71% | $2,485,889.98 |
| LONGXIA/USDT:USDT | +24.03% | $2,630,195.55 |
| NIGHT/USDT:USDT | +21.15% | $8,571,920.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MOVR/USDT:USDT | below_1h_threshold | +2.82% | +2.89% |
| NIGHT/USDT:USDT | below_1h_threshold | +2.25% | +2.31% |
| MARSCOIN/USDT:USDT | below_1h_threshold | +1.55% | +1.61% |
| NOM/USDT:USDT | below_1h_threshold | +1.22% | +1.29% |
| PHA/USDT:USDT | below_1h_threshold | +0.80% | +0.86% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
