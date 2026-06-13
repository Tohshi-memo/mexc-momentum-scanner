# Decision Report

- generated_at: 2026-06-13T21:46:26.318378+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6611**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6611, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| ASK | 20/20 | 100.0% | +0.43% | **+0.43%** |
| LIMIT_3PCT | 15/20 | 75.0% | +0.42% | **+0.31%** |
| LIMIT_9PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +2.26% | **+1.13%** |
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.97% | **+1.08%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.26% | **+0.82%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.50% | **+0.60%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +1.55% | **+0.31%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$166.47** / 初期 $100.00 (+66.47%)
- 確定: 1484件 (Win 399 / Loss 474 / Flat 611) / skip 1688件
- 成長率目線: 平均log +0.000343 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $166.47

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.71** / 初期 $100.00 (-1.29%)
- 確定: 22件 (Win 6 / Loss 10 / Flat 6) / skip 0件
- 成長率目線: 平均log -0.000589 / 幾何平均 -0.059% per trade / maxDD +1.93%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $98.71

## 5. Latest Market Context

- 更新: 2026-06-13T21:46:22.372453+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.35% price=64475.1
- Funnel: target 770 → liquid 131 → pre 50 → checked 50 → surge 0 → strict 0
- Surge前reject: below_1h_threshold=50, below_relative_strength=0, invalid_ohlcv=0, errors=0

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIF/USDT:USDT | +21.41% | $9,923,066.38 |
| MEGA/USDT:USDT | +10.81% | $2,253,868.57 |
| BTW/USDT:USDT | +9.08% | $1,856,555.13 |
| COAI/USDT:USDT | +6.18% | $32,240,775.22 |
| BRETT/USDT:USDT | +5.16% | $1,137,672.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| COAI/USDT:USDT | below_1h_threshold | +4.40% | +4.06% |
| H/USDT:USDT | below_1h_threshold | +4.03% | +3.69% |
| ZEC/USDT:USDT | below_1h_threshold | +3.26% | +2.91% |
| MEGA/USDT:USDT | below_1h_threshold | +3.03% | +2.68% |
| RIF/USDT:USDT | below_1h_threshold | +2.40% | +2.05% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
