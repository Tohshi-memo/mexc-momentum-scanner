# Decision Report

- generated_at: 2026-09-01T01:41:20.331423+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **13216**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +1.08% / filled 20/20。**
- 全期間 MARKET基準: n=13216, expectancy=+0.02%
- 直近20件 MARKET基準: n=20, expectancy=+1.08%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +1.08% | **+1.08%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT | 19/20 | 95.0% | +1.51% | **+1.43%** |
| MARKET | 20/20 | 100.0% | +1.08% | **+1.08%** |
| LIMIT_2PCT | 16/20 | 80.0% | +1.02% | **+0.82%** |
| LIMIT_FIB1272 | 10/20 | 50.0% | +1.22% | **+0.61%** |
| LIMIT_5PCT | 10/20 | 50.0% | +1.16% | **+0.58%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 8/20 | 40.0% | +3.46% | **+1.38%** |
| LIMIT_8PCT_LONG | 7/20 | 35.0% | +2.29% | **+0.80%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +1.55% | **+0.70%** |
| LIMIT_FIB1272_LONG | 12/20 | 60.0% | +0.90% | **+0.54%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.44% | **+0.40%** |

## 2. $100 Live Portfolio

- 残高: **$120.80** / 初期 $100.00 (+20.80%)
- 確定トレード: 195件 (TP 73 / SL 117 / EXP 5)
- 最新: ARB/USDT:USDT SL_HIT PnL -2.46% 残高後 $120.80
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$792.74** / 初期 $100.00 (+692.74%)
- 確定: 4878件 (Win 1485 / Loss 1609 / Flat 1784) / skip 4899件
- 成長率目線: 平均log +0.000424 / 幾何平均 +0.042% per trade / maxDD +8.46%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BTR/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $792.74

## 4. Robust Adaptive DryRun ($100)

- 残高: **$174.13** / 初期 $100.00 (+74.13%)
- 確定: 2198件 (Win 609 / Loss 529 / Flat 1060) / skip 4429件
- 成長率目線: 平均log +0.000252 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0551 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: BTR/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $174.13

## 5. Causal Adaptive DryRun ($100)

- 残高: **$115.69** / 初期 $100.00 (+15.69%)
- 確定: 2085件 (Win 610 / Loss 813 / Flat 662) / pending 0件 / skip 2607件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `MARKET` (selected_by_causal_log_growth) / causal_score +0.000128 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: BASECAT/USDT:USDT `MARKET` SL_HIT account -0.17% 残高後 $115.69

## 6. Latest Market Context

- 更新: 2026-09-01T01:41:12.447675+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.12% price=78523.4
- Funnel: target 1031 → liquid 148 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 77.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ARB/USDT:USDT | +36.55% | $43,705,035.52 |
| BTR/USDT:USDT | +27.04% | $6,532,203.36 |
| USELESS/USDT:USDT | +21.44% | $17,358,112.67 |
| 0G/USDT:USDT | +19.44% | $22,624,730.87 |
| CRV/USDT:USDT | +11.45% | $3,718,042.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CRV/USDT:USDT | below_1h_threshold | +2.26% | +2.38% |
| BTR/USDT:USDT | below_1h_threshold | +2.25% | +2.37% |
| KORU/USDT:USDT | below_1h_threshold | +2.15% | +2.27% |
| ARB/USDT:USDT | below_1h_threshold | +2.01% | +2.13% |
| SKHYNIXSTOCK/USDT:USDT | below_1h_threshold | +1.39% | +1.51% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
