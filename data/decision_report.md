# Decision Report

- generated_at: 2026-09-24T23:51:24.210144+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **15504**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.71% / filled 20/20。**
- 全期間 MARKET基準: n=15504, expectancy=+0.01%
- 直近20件 MARKET基準: n=20, expectancy=+0.71%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.71% | **+0.71%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT | 4/20 | 20.0% | +4.15% | **+0.83%** |
| MARKET | 20/20 | 100.0% | +0.71% | **+0.71%** |
| LIMIT_10PCT | 3/20 | 15.0% | +4.00% | **+0.60%** |
| LIMIT_8PCT | 5/20 | 25.0% | +2.34% | **+0.59%** |
| LIMIT_FIB1272 | 8/20 | 40.0% | +0.97% | **+0.39%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_BB3S_LONG | 7/12 | 58.3% | +3.15% | **+1.84%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.62% | **+1.30%** |
| MARKET_LONG | 20/20 | 100.0% | +1.08% | **+1.08%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.76% | **+0.69%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +5.14% | **+0.51%** |

## 2. $100 Live Portfolio

- 残高: **$120.08** / 初期 $100.00 (+20.08%)
- 確定トレード: 219件 (TP 79 / SL 135 / EXP 5)
- 最新: XPL/USDT:USDT SL_HIT PnL -3.85% 残高後 $120.08
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$1,197.79** / 初期 $100.00 (+1097.79%)
- 確定: 5900件 (Win 1739 / Loss 1890 / Flat 2271) / skip 6165件
- 成長率目線: 平均log +0.000421 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_BB3S_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SAGA/USDT:USDT `LIMIT_BB3S_LONG` EXPIRED account +0.00% 残高後 $1,197.79

## 4. Robust Adaptive DryRun ($100)

- 残高: **$253.55** / 初期 $100.00 (+153.55%)
- 確定: 3441件 (Win 949 / Loss 792 / Flat 1700) / skip 5474件
- 成長率目線: 平均log +0.000270 / 幾何平均 +0.027% per trade / maxDD +3.96%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score -0.0034 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MYX/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $253.55

## 5. Causal Adaptive DryRun ($100)

- 残高: **$120.20** / 初期 $100.00 (+20.20%)
- 確定: 3169件 (Win 933 / Loss 1253 / Flat 983) / pending 1件 / skip 3804件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000113 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: SAGA/USDT:USDT `LIMIT_8PCT` EXPIRED account +0.00% 残高後 $120.20

## 6. Latest Market Context

- 更新: 2026-09-24T23:51:12.974518+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.19% price=84398.3
- Funnel: target 1069 → liquid 176 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| SAGA/USDT:USDT | +66.82% | $7,983,883.23 |
| QNT/USDT:USDT | +9.47% | $3,416,713.41 |
| XAI/USDT:USDT | +9.41% | $11,182,453.53 |
| XPL/USDT:USDT | +9.26% | $14,837,646.23 |
| CHIP/USDT:USDT | +8.04% | $1,421,308.15 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| SAGA/USDT:USDT | below_1h_threshold | +4.63% | +4.44% |
| SYN/USDT:USDT | below_1h_threshold | +3.20% | +3.01% |
| XPL/USDT:USDT | below_1h_threshold | +2.00% | +1.81% |
| 1000BONK/USDT:USDT | below_1h_threshold | +1.78% | +1.58% |
| ONDO/USDT:USDT | below_1h_threshold | +1.43% | +1.23% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
