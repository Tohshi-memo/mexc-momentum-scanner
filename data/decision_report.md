# Decision Report

- generated_at: 2026-10-20T13:51:15.922419+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **17065**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=17065, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.57%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.57% | **-0.57%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +4.10% | **+0.82%** |
| LIMIT_6PCT | 5/20 | 25.0% | +1.93% | **+0.48%** |
| LIMIT_9PCT | 2/20 | 10.0% | +4.59% | **+0.46%** |
| LIMIT_8PCT | 2/20 | 10.0% | +3.70% | **+0.37%** |
| LIMIT_5PCT | 9/20 | 45.0% | +0.63% | **+0.29%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 11/11 | 100.0% | +2.74% | **+2.74%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +2.52% | **+1.77%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +2.05% | **+1.74%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.87% | **+1.21%** |
| MARKET_LONG | 20/20 | 100.0% | +0.82% | **+0.82%** |

## 2. $100 Live Portfolio

- 残高: **$121.36** / 初期 $100.00 (+21.36%)
- 確定トレード: 247件 (TP 91 / SL 149 / EXP 7)
- 最新: BAT/USDT:USDT SL_HIT PnL -3.97% 残高後 $121.36
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,330.85** / 初期 $100.00 (+1230.85%)
- 確定: 6485件 (Win 1887 / Loss 2070 / Flat 2528) / skip 7141件
- 成長率目線: 平均log +0.000399 / 幾何平均 +0.040% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APR/USDT:USDT `LIMIT_BB3S_LONG` SL_HIT account -0.50% 残高後 $1,330.85

## 4. Robust Adaptive DryRun ($100)

- 残高: **$283.06** / 初期 $100.00 (+183.06%)
- 確定: 3813件 (Win 1050 / Loss 889 / Flat 1874) / skip 6663件
- 成長率目線: 平均log +0.000273 / 幾何平均 +0.027% per trade / maxDD +4.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0806 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: APR/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.35% 残高後 $283.06

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.61** / 初期 $100.00 (+17.61%)
- 確定: 3310件 (Win 959 / Loss 1303 / Flat 1048) / pending 0件 / skip 5224件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000346 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: MARSCOIN/USDT:USDT `MARKET` EXPIRED account +0.03% 残高後 $117.61

## 6. Latest Market Context

- 更新: 2026-10-20T13:51:06.336991+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.38% price=81888.9
- Funnel: target 1084 → liquid 162 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 92.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JCT/USDT:USDT | +130.91% | $19,485,653.39 |
| ALT/USDT:USDT | +24.79% | $2,444,997.20 |
| APR/USDT:USDT | +17.75% | $1,392,732.18 |
| PHA/USDT:USDT | +14.76% | $20,106,733.80 |
| SOXS/USDT:USDT | +12.22% | $4,019,336.09 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| USELESS/USDT:USDT | below_1h_threshold | +3.50% | +3.11% |
| GRASS/USDT:USDT | below_1h_threshold | +2.27% | +1.88% |
| CHIP/USDT:USDT | below_1h_threshold | +1.89% | +1.51% |
| INJ/USDT:USDT | below_1h_threshold | +1.80% | +1.42% |
| AERO/USDT:USDT | below_1h_threshold | +1.63% | +1.25% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
