# Decision Report

- generated_at: 2026-08-14T20:46:39.347834+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **11603**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=11603, expectancy=-0.02%
- 直近20件 MARKET基準: n=20, expectancy=-1.48%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.48% | **-1.48%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 8/20 | 40.0% | +1.60% | **+0.64%** |
| LIMIT_3PCT | 16/20 | 80.0% | +0.70% | **+0.56%** |
| LIMIT_2PCT | 17/20 | 85.0% | +0.61% | **+0.52%** |
| LIMIT_5PCT | 6/20 | 30.0% | +1.65% | **+0.50%** |
| LIMIT_7PCT | 4/20 | 20.0% | +2.00% | **+0.40%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_ATR_LONG | 10/20 | 50.0% | +3.84% | **+1.92%** |
| LIMIT_6PCT_LONG | 7/20 | 35.0% | +3.66% | **+1.28%** |
| LIMIT_3PCT_LONG | 9/20 | 45.0% | +2.49% | **+1.12%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +1.22% | **+1.10%** |
| MARKET_LONG | 20/20 | 100.0% | +0.92% | **+0.92%** |

## 2. $100 Live Portfolio

- 残高: **$121.65** / 初期 $100.00 (+21.65%)
- 確定トレード: 182件 (TP 71 / SL 106 / EXP 5)
- 最新: GUA/USDT:USDT TP_HIT PnL +8.00% 残高後 $121.65
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$644.98** / 初期 $100.00 (+544.98%)
- 確定: 4071件 (Win 1277 / Loss 1339 / Flat 1455) / skip 4093件
- 成長率目線: 平均log +0.000458 / 幾何平均 +0.046% per trade / maxDD +8.13%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: CYS/USDT:USDT `LIMIT_FIB1272_LONG` EXPIRED account +0.00% 残高後 $644.98

## 4. Robust Adaptive DryRun ($100)

- 残高: **$151.92** / 初期 $100.00 (+51.92%)
- 確定: 1669件 (Win 478 / Loss 404 / Flat 787) / skip 3345件
- 成長率目線: 平均log +0.000251 / 幾何平均 +0.025% per trade / maxDD +3.96%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0762 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_5PCT` EXPIRED account +0.00% 残高後 $151.92

## 5. Causal Adaptive DryRun ($100)

- 残高: **$117.62** / 初期 $100.00 (+17.62%)
- 確定: 1552件 (Win 472 / Loss 594 / Flat 486) / pending 6件 / skip 1522件
- 検証方式: 検出時点より前にクローズ済みの結果だけで選択し、active中に戦略を固定
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_causal_log_growth) / causal_score +0.000243 / risk 0.175% / cost 0.15% / batch最大 2件 / open risk上限 1.05% / DD stop 8.0%
- 最新: CYS/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $117.62

## 6. Latest Market Context

- 更新: 2026-08-14T20:46:29.209243+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.07% price=62893.1
- Funnel: target 985 → liquid 173 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| DOLO/USDT:USDT | +23.18% | $1,464,402.63 |
| US/USDT:USDT | +23.04% | $6,735,296.62 |
| CYS/USDT:USDT | +14.90% | $13,763,414.76 |
| ACE/USDT:USDT | +13.44% | $61,819,051.39 |
| ACU/USDT:USDT | +9.04% | $2,121,167.05 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| WLFI/USDT:USDT | below_1h_threshold | +3.71% | +3.78% |
| SOXL/USDT:USDT | below_1h_threshold | +2.73% | +2.80% |
| MUU/USDT:USDT | below_1h_threshold | +1.79% | +1.86% |
| SKYAI/USDT:USDT | below_1h_threshold | +1.74% | +1.81% |
| TRUMPOFFICIAL/USDT:USDT | below_1h_threshold | +1.68% | +1.76% |

## 7. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
