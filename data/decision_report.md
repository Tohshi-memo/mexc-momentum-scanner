# Decision Report

- generated_at: 2026-06-13T20:20:02.481551+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6609**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6609, expectancy=-0.06%
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
| LIMIT_6PCT_LONG | 11/20 | 55.0% | +1.79% | **+0.99%** |
| LIMIT_7PCT_LONG | 10/20 | 50.0% | +1.97% | **+0.98%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +1.26% | **+0.82%** |
| LIMIT_8PCT_LONG | 8/20 | 40.0% | +1.00% | **+0.40%** |
| LIMIT_5PCT_LONG | 11/20 | 55.0% | +0.44% | **+0.24%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$168.15** / 初期 $100.00 (+68.15%)
- 確定: 1482件 (Win 399 / Loss 472 / Flat 611) / skip 1688件
- 成長率目線: 平均log +0.000351 / 幾何平均 +0.035% per trade / maxDD +7.25%
- 次の候補: `LIMIT_ATR_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: COAI/USDT:USDT `LIMIT_ATR_LONG` SL_HIT account -0.50% 残高後 $168.15

## 4. Robust Adaptive DryRun ($100)

- 残高: **$99.06** / 初期 $100.00 (-0.94%)
- 確定: 20件 (Win 6 / Loss 9 / Flat 5) / skip 0件
- 成長率目線: 平均log -0.000473 / 幾何平均 -0.047% per trade / maxDD +1.59%
- 次の候補: `LIMIT_5PCT` (selected_by_robust_growth_score) / robust_score +0.0190 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: COAI/USDT:USDT `LIMIT_1PCT_LONG` SL_HIT account -0.35% 残高後 $99.06

## 5. Latest Market Context

- 更新: 2026-06-13T20:19:58.293409+00:00 / 保存件数 288/288
- BTC: STAGNANT 1h -0.03% price=64241.9
- Funnel: target 770 → liquid 132 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| RIF/USDT:USDT | +19.76% | $8,472,711.45 |
| AT/USDT:USDT | +12.72% | $1,058,920.15 |
| COAI/USDT:USDT | +11.77% | $28,950,802.92 |
| VELVET/USDT:USDT | +9.48% | $62,824,462.73 |
| H/USDT:USDT | +8.29% | $15,106,019.42 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| RIF/USDT:USDT | below_1h_threshold | +3.78% | +3.81% |
| BSB/USDT:USDT | below_1h_threshold | +1.50% | +1.53% |
| AIOT/USDT:USDT | below_1h_threshold | +1.38% | +1.41% |
| VELVET/USDT:USDT | below_1h_threshold | +1.12% | +1.14% |
| RIVER/USDT:USDT | below_1h_threshold | +0.86% | +0.89% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
