# Decision Report

- generated_at: 2026-08-30T05:21:13.847609+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13022**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=13022, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=-1.75%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.75% | **-1.75%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S | 11/17 | 64.7% | +0.85% | **+0.55%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +1.60% | **+0.48%** |
| LIMIT_6PCT | 8/20 | 40.0% | +1.18% | **+0.47%** |
| LIMIT_ATR | 15/20 | 75.0% | +0.38% | **+0.28%** |
| LIMIT_4PCT | 16/20 | 80.0% | +0.25% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_5PCT_LONG | 9/20 | 45.0% | +4.45% | **+2.00%** |
| LIMIT_4PCT_LONG | 10/20 | 50.0% | +3.50% | **+1.75%** |
| LIMIT_3PCT_LONG | 10/20 | 50.0% | +3.12% | **+1.56%** |
| LIMIT_BB3S_LONG | 2/3 | 66.7% | +2.00% | **+1.33%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +2.27% | **+0.91%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 194件 (TP 73 / SL 116 / EXP 5)
- 最新: SKR/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$788.13** / 初期 $100.00 (+688.13%)
- 確定: 4792件 (Win 1460 / Loss 1576 / Flat 1756) / skip 4791件
- 成長率目線: 平均log +0.000431 / 幾何平均 +0.043% per trade / maxDD +8.46%
- 次の候補: `LIMIT_4PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: PONS/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $788.13

## 4. Robust Adaptive DryRun ($100)

- 残高: **$173.29** / 初期 $100.00 (+73.29%)
- 確定: 2106件 (Win 589 / Loss 514 / Flat 1003) / skip 4327件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.96%
- 次の候補: `LIMIT_7PCT` (selected_by_robust_growth_score) / robust_score +0.0609 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $173.29

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.13** / 初期 $100.00 (+17.13%)
- 確定: 2065件 (Win 607 / Loss 801 / Flat 657) / pending 2件 / skip 2425件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000358 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: PONS/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $117.13

## 6. Latest Market Context

- 更新: 2026-08-30T05:21:04.639476+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=78108.2
- Funnel: target 1023 → liquid 116 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| HNT/USDT:USDT | +84.01% | $31,843,510.85 |
| NIULAI/USDT:USDT | +56.44% | $2,561,959.05 |
| FONE/USDT:USDT | +55.62% | $1,396,511.79 |
| PONS/USDT:USDT | +42.38% | $1,520,764.72 |
| PROM/USDT:USDT | +33.81% | $14,687,668.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| UAI/USDT:USDT | below_1h_threshold | +4.70% | +4.66% |
| BTR/USDT:USDT | below_1h_threshold | +3.77% | +3.74% |
| SKR/USDT:USDT | below_1h_threshold | +3.72% | +3.68% |
| HNT/USDT:USDT | below_1h_threshold | +2.58% | +2.55% |
| TUT/USDT:USDT | below_1h_threshold | +2.55% | +2.52% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
