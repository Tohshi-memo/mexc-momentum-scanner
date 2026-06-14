# Decision Report

- generated_at: 2026-06-14T05:48:59.097269+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6643**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6643, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-0.40%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.40% | **-0.40%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1272 | 5/20 | 25.0% | +1.50% | **+0.37%** |
| LIMIT_9PCT | 3/20 | 15.0% | +1.72% | **+0.26%** |
| LIMIT_7PCT | 4/20 | 20.0% | +1.10% | **+0.22%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |
| LIMIT_8PCT | 3/20 | 15.0% | +1.14% | **+0.17%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 14/20 | 70.0% | +1.60% | **+1.12%** |
| MARKET_LONG | 20/20 | 100.0% | +0.80% | **+0.80%** |
| LIMIT_1PCT_LONG | 15/20 | 75.0% | +0.62% | **+0.46%** |
| ASK_LONG | 20/20 | 100.0% | +0.42% | **+0.42%** |
| LIMIT_7PCT_LONG | 7/20 | 35.0% | +0.68% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$168.14** / 初期 $100.00 (+68.14%)
- 確定: 1516件 (Win 406 / Loss 485 / Flat 625) / skip 1688件
- 成長率目線: 平均log +0.000343 / 幾何平均 +0.034% per trade / maxDD +7.25%
- 次の候補: `LIMIT_9PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: H/USDT:USDT `LIMIT_9PCT_LONG` EXPIRED account +0.00% 残高後 $168.14

## 4. Robust Adaptive DryRun ($100)

- 残高: **$98.86** / 初期 $100.00 (-1.14%)
- 確定: 48件 (Win 17 / Loss 12 / Flat 19) / skip 6件
- 成長率目線: 平均log -0.000238 / 幾何平均 -0.024% per trade / maxDD +2.00%
- 次の候補: `LIMIT_6PCT` (selected_by_robust_growth_score) / robust_score +0.0331 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: H/USDT:USDT `LIMIT_6PCT` EXPIRED account +0.00% 残高後 $98.86

## 5. Latest Market Context

- 更新: 2026-06-14T05:48:51.130881+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h +0.04% price=64328.4
- Funnel: target 770 → liquid 125 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=46, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 74.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| H/USDT:USDT | +79.55% | $27,923,394.97 |
| TRADOOR/USDT:USDT | +43.72% | $5,790,600.23 |
| BTW/USDT:USDT | +24.07% | $2,693,426.64 |
| VELVET/USDT:USDT | +22.73% | $56,666,643.56 |
| MEGA/USDT:USDT | +12.36% | $4,192,907.52 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MEGA/USDT:USDT | below_relative_strength | +5.01% | +4.97% |
| PLAY/USDT:USDT | below_1h_threshold | +3.20% | +3.16% |
| TRADOOR/USDT:USDT | below_1h_threshold | +2.76% | +2.72% |
| FOLKS/USDT:USDT | below_1h_threshold | +2.42% | +2.38% |
| JASMY/USDT:USDT | below_1h_threshold | +2.36% | +2.32% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
