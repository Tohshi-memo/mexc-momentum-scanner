# Decision Report

- generated_at: 2026-06-15T12:02:33.108844+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6777**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6777, expectancy=-0.04%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT | 17/20 | 85.0% | +1.31% | **+1.12%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.62% | **+0.47%** |
| LIMIT_FIB1272 | 3/20 | 15.0% | +2.58% | **+0.39%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |
| LIMIT_1PCT | 19/20 | 95.0% | +0.11% | **+0.11%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 17/20 | 85.0% | +0.87% | **+0.74%** |
| LIMIT_1PCT_LONG | 18/20 | 90.0% | +0.69% | **+0.62%** |
| LIMIT_FIB1272_LONG | 6/20 | 30.0% | +1.04% | **+0.31%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.62% | **+0.28%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.68% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RIF/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.02
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$173.62** / 初期 $100.00 (+73.62%)
- 確定: 1650件 (Win 430 / Loss 513 / Flat 707) / skip 1688件
- 成長率目線: 平均log +0.000334 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_3PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ASTEROID/USDT:USDT `LIMIT_3PCT_LONG` SL_HIT account -0.50% 残高後 $173.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.27** / 初期 $100.00 (-1.73%)
- 確定: 143件 (Win 28 / Loss 27 / Flat 88) / skip 45件
- 成長率目線: 平均log -0.000122 / 幾何平均 -0.012% per trade / maxDD +2.37%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.35% 残高後 $98.27

## 5. Latest Market Context

- 更新: 2026-06-15T12:02:28.725194+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.05% price=66156.5
- Funnel: target 771 → liquid 146 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 85.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +79.72% | $4,901,076.48 |
| EVAA/USDT:USDT | +77.44% | $30,458,650.20 |
| CLO/USDT:USDT | +39.75% | $2,315,815.67 |
| ZEC/USDT:USDT | +27.16% | $255,031,545.34 |
| UAI/USDT:USDT | +26.16% | $3,225,944.40 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| BSB/USDT:USDT | below_1h_threshold | +1.25% | +1.31% |
| ASTEROID/USDT:USDT | below_1h_threshold | +0.98% | +1.04% |
| FHE/USDT:USDT | below_1h_threshold | +0.91% | +0.97% |
| ZEN/USDT:USDT | below_1h_threshold | +0.86% | +0.92% |
| JTO/USDT:USDT | below_1h_threshold | +0.76% | +0.81% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
