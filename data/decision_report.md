# Decision Report

- generated_at: 2026-11-10T10:21:16.869322+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18593**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18593, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-0.03%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.03% | **-0.03%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +2.20% | **+0.88%** |
| LIMIT_5PCT | 8/20 | 40.0% | +1.83% | **+0.73%** |
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.42% | **+0.31%** |
| LIMIT_7PCT | 2/20 | 10.0% | +2.80% | **+0.28%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.51% | **+1.06%** |
| LIMIT_ATR_LONG | 11/20 | 55.0% | +1.65% | **+0.91%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +1.23% | **+0.74%** |
| LIMIT_BB3S_LONG | 4/5 | 80.0% | +0.72% | **+0.58%** |
| LIMIT_9PCT_LONG | 3/20 | 15.0% | +3.40% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$121.13** / 初期 $100.00 (+21.13%)
- 確定トレード: 268件 (TP 97 / SL 163 / EXP 8)
- 最新: CRWVSTOCK/USDT:USDT SL_HIT PnL -2.78% 残高後 $121.13
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,665.33** / 初期 $100.00 (+1565.33%)
- 確定: 7190件 (Win 2067 / Loss 2295 / Flat 2828) / skip 7964件
- 成長率目線: 平均log +0.000391 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ONE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $1,665.33

## 4. Robust Adaptive DryRun ($100)

- 残高: **$391.91** / 初期 $100.00 (+291.91%)
- 確定: 4760件 (Win 1279 / Loss 1048 / Flat 2433) / skip 7244件
- 成長率目線: 平均log +0.000287 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0774 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: AIN/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.52% 残高後 $391.91

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6751件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000384 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-10T10:21:04.822567+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.28% price=74273.4
- Funnel: target 1094 → liquid 149 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| INIT/USDT:USDT | +65.16% | $13,690,223.78 |
| ONE/USDT:USDT | +20.95% | $6,685,048.12 |
| NIUBI/USDT:USDT | +20.12% | $2,371,082.99 |
| ARIA/USDT:USDT | +11.25% | $1,279,471.06 |
| ZHIPUSTOCK/USDT:USDT | +9.86% | $1,537,134.76 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ONE/USDT:USDT | below_1h_threshold | +2.10% | +2.39% |
| NBISSTOCK/USDT:USDT | below_1h_threshold | +1.70% | +1.98% |
| SPCXSTOCK/USDT:USDT | below_1h_threshold | +0.76% | +1.04% |
| INIT/USDT:USDT | below_1h_threshold | +0.71% | +0.99% |
| AIOT/USDT:USDT | below_1h_threshold | +0.70% | +0.98% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
