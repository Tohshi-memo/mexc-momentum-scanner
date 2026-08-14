# Decision Report

- generated_at: 2026-08-14T13:06:28.183489+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11553**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11553, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_4PCT | 14/20 | 70.0% | +0.86% | **+0.60%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.62% | **+0.47%** |
| LIMIT_5PCT | 7/20 | 35.0% | +1.25% | **+0.44%** |
| LIMIT_2PCT | 18/20 | 90.0% | +0.47% | **+0.42%** |
| LIMIT_ATR | 13/20 | 65.0% | +0.59% | **+0.38%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 19/20 | 95.0% | +1.40% | **+1.33%** |
| LIMIT_ATR_LONG | 9/20 | 45.0% | +2.79% | **+1.26%** |
| LIMIT_BB3S_LONG | 3/4 | 75.0% | +1.61% | **+1.21%** |
| LIMIT_5PCT_LONG | 8/20 | 40.0% | +2.11% | **+0.84%** |
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.20% | **+0.84%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$631.69** / 初期 $100.00 (+531.69%)
- 確定: 4021件 (Win 1262 / Loss 1321 / Flat 1438) / skip 4093件
- 成長率目線: 平均log +0.000458 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: APR/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.50% 残高後 $631.69

## 4. Robust Adaptive DryRun ($100)

- 残高: **$149.41** / 初期 $100.00 (+49.41%)
- 確定: 1651件 (Win 471 / Loss 398 / Flat 782) / skip 3313件
- 成長率目線: 平均log +0.000243 / 幾何平均 +0.024% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0615 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $149.41

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.72** / 初期 $100.00 (+17.72%)
- 確定: 1513件 (Win 457 / Loss 575 / Flat 481) / pending 3件 / skip 1508件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET_LONG` (selected_by_causal_log_growth) / causal_score +0.000210 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: APR/USDT:USDT `MARKET_LONG` SL_HIT account -0.17% 残高後 $117.72

## 6. Latest Market Context

- 更新: 2026-08-14T13:06:21.399160+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.00% price=62703.7
- Funnel: target 985 → liquid 179 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ACE/USDT:USDT | +134.76% | $32,099,846.27 |
| AKE/USDT:USDT | +80.36% | $67,688,119.66 |
| VELVET/USDT:USDT | +53.79% | $34,639,151.63 |
| CROSS/USDT:USDT | +32.09% | $1,292,344.17 |
| CAP/USDT:USDT | +24.76% | $4,710,652.56 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| AVAAI/USDT:USDT | below_1h_threshold | +2.85% | +2.86% |
| AKE/USDT:USDT | below_1h_threshold | +2.55% | +2.55% |
| ACE/USDT:USDT | below_1h_threshold | +1.77% | +1.77% |
| VELVET/USDT:USDT | below_1h_threshold | +1.18% | +1.18% |
| 2Z/USDT:USDT | below_1h_threshold | +1.02% | +1.02% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
