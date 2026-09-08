# Decision Report

- generated_at: 2026-09-08T14:11:29.715732+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13999**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.35% / filled 20/20。**
- 全期間 MARKET基準: n=13999, expectancy=-0.01%
- 直近20件 MARKET基準: n=20, expectancy=+1.35%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.35% | **+1.35%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.35% | **+1.35%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_1PCT | 17/20 | 85.0% | +0.42% | **+0.36%** |
| LIMIT_7PCT | 3/20 | 15.0% | +2.27% | **+0.34%** |
| LIMIT_ATR | 10/20 | 50.0% | +0.68% | **+0.34%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT_LONG | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_9PCT_LONG | 8/20 | 40.0% | +0.69% | **+0.27%** |
| LIMIT_8PCT_LONG | 10/20 | 50.0% | -0.76% | **-0.38%** |
| LIMIT_FIB1618_LONG | 6/20 | 30.0% | -1.45% | **-0.44%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | -0.69% | **-0.55%** |

## 2. $100 Live Portfolio

- 残高: **$120.92** / 初期 $100.00 (+20.92%)
- 確定トレード: 206件 (TP 77 / SL 124 / EXP 5)
- 最新: BONER/USDT:USDT SL_HIT PnL -4.00% 残高後 $120.92
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,007.04** / 初期 $100.00 (+907.04%)
- 確定: 5263件 (Win 1584 / Loss 1707 / Flat 1972) / skip 5297件
- 成長率目線: 平均log +0.000439 / 幾何平均 +0.044% per trade / maxDD +8.46%
- 次の候補: `LIMIT_6PCT` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: USELESS/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $1,007.04

## 4. Robust Adaptive DryRun ($100)

- 残高: **$190.03** / 初期 $100.00 (+90.03%)
- 確定: 2602件 (Win 722 / Loss 622 / Flat 1258) / skip 4808件
- 成長率目線: 平均log +0.000247 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0642 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $190.03

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.57** / 初期 $100.00 (+20.57%)
- 確定: 2588件 (Win 759 / Loss 978 / Flat 851) / pending 1件 / skip 2878件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000210 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: USELESS/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $120.57

## 6. Latest Market Context

- 更新: 2026-09-08T14:11:17.764577+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.18% price=78074.9
- Funnel: target 1070 → liquid 158 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SOPH/USDT:USDT | +58.89% | $30,662,977.32 |
| USELESS/USDT:USDT | +26.37% | $14,643,389.32 |
| BNCSTOCK/USDT:USDT | +24.93% | $2,293,451.01 |
| FORM/USDT:USDT | +19.19% | $4,956,475.35 |
| AKE/USDT:USDT | +17.16% | $10,059,896.22 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NBISSTOCK/USDT:USDT | below_1h_threshold | +3.24% | +3.07% |
| SKHYSTOCK/USDT:USDT | below_1h_threshold | +3.01% | +2.83% |
| USELESS/USDT:USDT | below_1h_threshold | +2.66% | +2.48% |
| SOXS/USDT:USDT | below_1h_threshold | +1.98% | +1.80% |
| VVV/USDT:USDT | below_1h_threshold | +1.82% | +1.65% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
