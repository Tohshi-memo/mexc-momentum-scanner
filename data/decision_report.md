# Decision Report

- generated_at: 2026-11-11T10:21:38.087394+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **18668**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=18668, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 6/20 | 30.0% | +2.27% | **+0.68%** |
| LIMIT_3PCT | 17/20 | 85.0% | +0.78% | **+0.66%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.27% | **+0.38%** |
| LIMIT_9PCT | 4/20 | 20.0% | +1.15% | **+0.23%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.25% | **+0.21%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 5/14 | 35.7% | +7.53% | **+2.69%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.51% | **+1.36%** |
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +2.76% | **+1.24%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +4.00% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$121.01** / 初期 $100.00 (+21.01%)
- 確定トレード: 269件 (TP 97 / SL 164 / EXP 8)
- 最新: JCT/USDT:USDT SL_HIT PnL -4.00% 残高後 $121.01
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,656.10** / 初期 $100.00 (+1556.10%)
- 確定: 7211件 (Win 2073 / Loss 2306 / Flat 2832) / skip 8018件
- 成長率目線: 平均log +0.000389 / 幾何平均 +0.039% per trade / maxDD +8.46%
- 次の候補: `LIMIT_7PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ARIA/USDT:USDT `LIMIT_FIB1272` SL_HIT account -0.10% 残高後 $1,656.10

## 4. Robust Adaptive DryRun ($100)

- 残高: **$391.65** / 初期 $100.00 (+291.65%)
- 確定: 4778件 (Win 1283 / Loss 1056 / Flat 2439) / skip 7301件
- 成長率目線: 平均log +0.000286 / 幾何平均 +0.029% per trade / maxDD +4.29%
- 次の候補: `LIMIT_FIB1272` (selected_by_robust_growth_score) / robust_score -0.0164 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: JCT/USDT:USDT `LIMIT_FIB1272` EXPIRED account +0.00% 残高後 $391.65

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 6827件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_7PCT` (selected_by_causal_log_growth) / causal_score +0.000131 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-11-11T10:21:18.937795+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=73786.0
- Funnel: target 1099 → liquid 149 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 90.7 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| AGT/USDT:USDT | +126.30% | $6,156,937.35 |
| ARIA/USDT:USDT | +46.74% | $5,390,933.32 |
| SNXX/USDT:USDT | +20.50% | $27,614,862.40 |
| MUU/USDT:USDT | +17.34% | $13,374,937.39 |
| SOXL/USDT:USDT | +16.89% | $655,750,922.31 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SNDKSTOCK/USDT:USDT | below_1h_threshold | +2.88% | +2.85% |
| MUU/USDT:USDT | below_1h_threshold | +2.63% | +2.59% |
| GRAM/USDT:USDT | below_1h_threshold | +2.19% | +2.16% |
| JCT/USDT:USDT | below_1h_threshold | +2.08% | +2.05% |
| MUSTOCK/USDT:USDT | below_1h_threshold | +1.45% | +1.42% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
