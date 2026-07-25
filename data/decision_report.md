# Decision Report

- generated_at: 2026-07-25T23:41:17.426521+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **9546**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.48% / filled 20/20。**
- 全期間 MARKET基準: n=9546, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=+0.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.48% | **+0.48%** |
| LIMIT_2PCT | 16/20 | 80.0% | +0.52% | **+0.42%** |
| LIMIT_3PCT | 13/20 | 65.0% | +0.41% | **+0.27%** |
| LIMIT_ATR | 9/20 | 45.0% | +0.56% | **+0.25%** |
| LIMIT_FIB1272 | 6/20 | 30.0% | +0.84% | **+0.25%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.03% | **+0.93%** |
| MARKET_LONG | 20/20 | 100.0% | +0.70% | **+0.70%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.91% | **+0.68%** |
| LIMIT_FIB1272_LONG | 10/20 | 50.0% | +1.32% | **+0.66%** |
| LIMIT_8PCT_LONG | 5/20 | 25.0% | +1.60% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$104.82** / 初期 $100.00 (+4.82%)
- 確定トレード: 140件 (TP 47 / SL 88 / EXP 5)
- 最新: B2/USDT:USDT TP_HIT PnL +8.00% 残高後 $104.82
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$452.01** / 初期 $100.00 (+352.01%)
- 確定: 3374件 (Win 1071 / Loss 1095 / Flat 1208) / skip 2733件
- 成長率目線: 平均log +0.000447 / 幾何平均 +0.045% per trade / maxDD +8.13%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $452.01

## 4. Robust Adaptive DryRun ($100)

- 残高: **$136.75** / 初期 $100.00 (+36.75%)
- 確定: 1199件 (Win 331 / Loss 265 / Flat 603) / skip 1758件
- 成長率目線: 平均log +0.000261 / 幾何平均 +0.026% per trade / maxDD +3.89%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0846 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $136.75

## 5. Causal Adaptive DryRun ($100)

- 残高: **$107.70** / 初期 $100.00 (+7.70%)
- 確定: 590件 (Win 199 / Loss 228 / Flat 163) / pending 2件 / skip 424件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000461 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: DEXE/USDT:USDT `LIMIT_2PCT_LONG` SL_HIT account -0.17% 残高後 $107.70

## 6. Latest Market Context

- 更新: 2026-07-25T23:41:08.574258+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=64358.8
- Funnel: target 898 → liquid 118 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ESPORTS/USDT:USDT | +24.89% | $26,580,022.50 |
| EUL/USDT:USDT | +23.96% | $19,738,085.89 |
| BANK/USDT:USDT | +15.87% | $88,024,655.17 |
| ALLO/USDT:USDT | +13.02% | $18,138,308.18 |
| DEXE/USDT:USDT | +9.68% | $129,201,584.18 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| ESPORTS/USDT:USDT | below_1h_threshold | +4.17% | +4.20% |
| LAB/USDT:USDT | below_1h_threshold | +2.15% | +2.18% |
| EUL/USDT:USDT | below_1h_threshold | +1.47% | +1.50% |
| BANK/USDT:USDT | below_1h_threshold | +1.13% | +1.16% |
| EVAA/USDT:USDT | below_1h_threshold | +0.95% | +0.98% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
