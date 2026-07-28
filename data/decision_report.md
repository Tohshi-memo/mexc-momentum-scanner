# Decision Report

- generated_at: 2026-07-28T20:36:18.672290+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9726**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=9726, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.62%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.62% | **-0.62%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT | 4/20 | 20.0% | +5.40% | **+1.08%** |
| LIMIT_6PCT | 6/20 | 30.0% | +2.91% | **+0.87%** |
| LIMIT_5PCT | 9/20 | 45.0% | +1.74% | **+0.78%** |
| LIMIT_BB3S | 11/18 | 61.1% | +1.22% | **+0.75%** |
| LIMIT_FIB1272 | 7/20 | 35.0% | +0.64% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.93% | **+1.83%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.89% | **+1.33%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +3.30% | **+0.99%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +1.61% | **+0.89%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +1.02% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$107.44** / 初期 $100.00 (+7.44%)
- 確定トレード: 150件 (TP 52 / SL 93 / EXP 5)
- 最新: DEXE/USDT:USDT TP_HIT PnL +8.00% 残高後 $107.44
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$503.02** / 初期 $100.00 (+403.02%)
- 確定: 3496件 (Win 1107 / Loss 1134 / Flat 1255) / skip 2791件
- 成長率目線: 平均log +0.000462 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BEAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.77% 残高後 $503.02

## 4. Robust Adaptive DryRun ($100)

- 残高: **$137.24** / 初期 $100.00 (+37.24%)
- 確定: 1226件 (Win 338 / Loss 275 / Flat 613) / skip 1911件
- 成長率目線: 平均log +0.000258 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.1223 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: SPCXSTOCK/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $137.24

## 5. Causal Adaptive DryRun ($100)

- 残高: **$110.41** / 初期 $100.00 (+10.41%)
- 確定: 744件 (Win 242 / Loss 283 / Flat 219) / pending 3件 / skip 450件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000512 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BEAT/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.26% 残高後 $110.41

## 6. Latest Market Context

- 更新: 2026-07-28T20:36:11.655440+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.05% price=63916.8
- Funnel: target 904 → liquid 173 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| JIMOTHY/USDT:USDT | +21.82% | $1,401,482.48 |
| ON/USDT:USDT | +19.50% | $37,873,246.70 |
| BTW/USDT:USDT | +16.20% | $5,834,086.75 |
| RIF/USDT:USDT | +15.52% | $4,625,454.85 |
| BEAT/USDT:USDT | +11.06% | $59,771,738.25 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ZIL/USDT:USDT | below_1h_threshold | +3.33% | +3.27% |
| CAP/USDT:USDT | below_1h_threshold | +2.93% | +2.88% |
| INFQSTOCK/USDT:USDT | below_1h_threshold | +1.91% | +1.86% |
| SNXX/USDT:USDT | below_1h_threshold | +1.65% | +1.60% |
| ON/USDT:USDT | below_1h_threshold | +1.59% | +1.54% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
