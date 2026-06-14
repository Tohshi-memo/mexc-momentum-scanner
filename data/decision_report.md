# Decision Report

- generated_at: 2026-06-14T05:29:35.452511+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6641**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6641, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=+0.20%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | +0.20% | **+0.20%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| ASK | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.50% | **+0.37%** |
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_7PCT_LONG | 9/20 | 45.0% | +1.30% | **+0.58%** |
| LIMIT_9PCT_LONG | 4/20 | 20.0% | +2.82% | **+0.56%** |
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.42% | **+0.32%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.48% | **+0.31%** |
| LIMIT_10PCT_LONG | 2/20 | 10.0% | +2.22% | **+0.22%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$168.14** / 初期 $100.00 (+68.14%)
- 確定: 1514件 (Win 406 / Loss 485 / Flat 623) / skip 1688件
- 成長率目線: 平均log +0.000343 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account +0.00% 残高後 $168.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.71** / 初期 $100.00 (-1.29%)
- 確定: 46件 (Win 16 / Loss 12 / Flat 18) / skip 6件
- 成長率目線: 平均log -0.000282 / 幾何平均 -0.028% per trade / maxDD +2.00%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0316 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: TRADOOR/USDT:USDT `LIMIT_5PCT` SL_HIT account +0.07% 残高後 $98.71

## 5. Latest Market Context

- 更新: 2026-06-14T05:29:30.950498+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=64282.4
- Funnel: target 770 → liquid 125 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 73.2 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +71.86% | $27,074,377.24 |
| TRADOOR/USDT:USDT | +42.02% | $5,678,293.68 |
| BTW/USDT:USDT | +25.89% | $2,639,862.71 |
| VELVET/USDT:USDT | +15.62% | $55,501,195.91 |
| JCT/USDT:USDT | +9.83% | $10,442,588.78 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| LAB/USDT:USDT | below_1h_threshold | +2.97% | +3.00% |
| PLAY/USDT:USDT | below_1h_threshold | +2.94% | +2.96% |
| BTW/USDT:USDT | below_1h_threshold | +2.24% | +2.27% |
| HOME/USDT:USDT | below_1h_threshold | +2.14% | +2.17% |
| FOLKS/USDT:USDT | below_1h_threshold | +1.69% | +1.72% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
