# Decision Report

- generated_at: 2026-06-15T12:43:27.144618+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6780**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6780, expectancy=-0.04%
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
| LIMIT_6PCT | 4/20 | 20.0% | +1.89% | **+0.38%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.95% | **+0.33%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272_LONG | 7/20 | 35.0% | +1.77% | **+0.62%** |
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +0.43% | **+0.34%** |
| LIMIT_6PCT_LONG | 9/20 | 45.0% | +0.62% | **+0.28%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.68% | **+0.24%** |
| MARKET_LONG | 20/20 | 100.0% | -0.00% | **-0.00%** |

## 2. $100 Live Portfolio

- 残高: **$103.02** / 初期 $100.00 (+3.02%)
- 確定トレード: 6件 (TP 4 / SL 2 / EXP 0)
- 最新: RIF/USDT:USDT TP_HIT PnL +8.00% 残高後 $103.02
- 最新戦略メタ: tier=S, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$173.62** / 初期 $100.00 (+73.62%)
- 確定: 1653件 (Win 430 / Loss 513 / Flat 710) / skip 1688件
- 成長率目線: 平均log +0.000334 / 幾何平均 +0.033% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: BABY/USDT:USDT `LIMIT_3PCT_LONG` EXPIRED account +0.00% 残高後 $173.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.27** / 初期 $100.00 (-1.73%)
- 確定: 143件 (Win 28 / Loss 27 / Flat 88) / skip 48件
- 成長率目線: 平均log -0.000122 / 幾何平均 -0.012% per trade / maxDD +2.37%
- 次の候補: `LIMIT_FIB1272_LONG` (selected_by_robust_growth_score) / robust_score +0.0109 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: EVAA/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.35% 残高後 $98.27

## 5. Latest Market Context

- 更新: 2026-06-15T12:43:22.540068+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.32% price=66404.7
- Funnel: target 771 → liquid 147 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 86.0 >= 65=1, 4h RSI 70.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| EVAA/USDT:USDT | +83.59% | $32,121,903.41 |
| ASTEROID/USDT:USDT | +72.72% | $5,143,320.95 |
| CLO/USDT:USDT | +42.37% | $2,373,869.66 |
| UAI/USDT:USDT | +28.12% | $3,607,866.27 |
| ZEC/USDT:USDT | +25.35% | $268,745,832.62 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| XLM/USDT:USDT | below_1h_threshold | +3.05% | +2.72% |
| BABY/USDT:USDT | below_1h_threshold | +2.98% | +2.66% |
| FLOKI/USDT:USDT | below_1h_threshold | +2.13% | +1.81% |
| ZRO/USDT:USDT | below_1h_threshold | +1.92% | +1.60% |
| ADA/USDT:USDT | below_1h_threshold | +1.62% | +1.30% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
