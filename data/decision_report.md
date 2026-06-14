# Decision Report

- generated_at: 2026-06-14T05:16:12.202482+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6640**

## 1. 今日の判断

- 結論: **MARKET SHORTは実行候補。直近EV +0.77% / filled 20/20。**
- 全期間 MARKET基準: n=6640, expectancy=-0.05%
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
| LIMIT_FIB1272 | 4/20 | 20.0% | +1.33% | **+0.27%** |
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.13% | **+0.56%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +0.50% | **+0.20%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.16% | **+0.11%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$168.14** / 初期 $100.00 (+68.14%)
- 確定: 1513件 (Win 406 / Loss 485 / Flat 622) / skip 1688件
- 成長率目線: 平均log +0.000343 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $168.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.71** / 初期 $100.00 (-1.29%)
- 確定: 46件 (Win 16 / Loss 12 / Flat 18) / skip 5件
- 成長率目線: 平均log -0.000282 / 幾何平均 -0.028% per trade / maxDD +2.00%
- 次の候補: `見送り` (no_strategy_passed_robust_filters) / robust_score n/a / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TRADOOR/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $98.71

## 5. Latest Market Context

- 更新: 2026-06-14T05:16:07.126497+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.03% price=64321.8
- Funnel: target 770 → liquid 125 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 72.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +70.54% | $26,076,378.82 |
| TRADOOR/USDT:USDT | +38.10% | $5,545,531.47 |
| BTW/USDT:USDT | +23.91% | $2,611,309.31 |
| VELVET/USDT:USDT | +10.49% | $54,655,003.94 |
| BRETT/USDT:USDT | +9.44% | $1,607,845.64 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +2.68% | +2.64% |
| FOLKS/USDT:USDT | below_1h_threshold | +2.03% | +2.00% |
| PLAY/USDT:USDT | below_1h_threshold | +1.80% | +1.76% |
| HOME/USDT:USDT | below_1h_threshold | +1.07% | +1.04% |
| JCT/USDT:USDT | below_1h_threshold | +0.95% | +0.91% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
