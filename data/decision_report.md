# Decision Report

- generated_at: 2026-06-14T03:21:56.136715+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6630**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.77% / filled 20/20。**
- 全期間 MARKET基準: n=6630, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.77%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +1.38% | **+1.38%** |
| MARKET | 20/20 | 100.0% | +0.77% | **+0.77%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.67% | **+0.40%** |
| LIMIT_5PCT | 8/20 | 40.0% | +0.95% | **+0.38%** |
| LIMIT_6PCT | 2/20 | 10.0% | +1.89% | **+0.19%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 5/20 | 25.0% | +2.48% | **+0.62%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.88% | **+0.62%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +0.36% | **+0.16%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$169.85** / 初期 $100.00 (+69.85%)
- 確定: 1503件 (Win 405 / Loss 481 / Flat 617) / skip 1688件
- 成長率目線: 平均log +0.000352 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_ATR_LONG` TP_HIT account +1.00% 残高後 $169.85

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.92** / 初期 $100.00 (-1.08%)
- 確定: 41件 (Win 14 / Loss 11 / Flat 16) / skip 0件
- 成長率目線: 平均log -0.000265 / 幾何平均 -0.026% per trade / maxDD +1.93%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0226 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $98.92

## 5. Latest Market Context

- 更新: 2026-06-14T03:21:50.851897+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.06% price=64490.0
- Funnel: target 770 → liquid 126 → pre 50 → checked 50 → surge 2 → strict 0
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.1 >= 65=1, 4h RSI 88.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| TRADOOR/USDT:USDT | +44.12% | $3,857,660.30 |
| H/USDT:USDT | +37.90% | $20,176,204.92 |
| BTW/USDT:USDT | +21.36% | $2,077,802.78 |
| BRETT/USDT:USDT | +10.41% | $1,555,853.14 |
| MEGA/USDT:USDT | +9.12% | $3,932,800.69 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| H/USDT:USDT | below_1h_threshold | +4.73% | +4.67% |
| NOT/USDT:USDT | below_1h_threshold | +3.46% | +3.40% |
| SIREN/USDT:USDT | below_1h_threshold | +1.83% | +1.78% |
| DASH/USDT:USDT | below_1h_threshold | +1.47% | +1.42% |
| ALGO/USDT:USDT | below_1h_threshold | +0.88% | +0.82% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
