# Decision Report

- generated_at: 2026-06-13T18:44:50.125808+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6600**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6600, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-1.60%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.60% | **-1.60%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_5PCT | 7/20 | 35.0% | +0.24% | **+0.09%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.05% | **+0.01%** |
| LIMIT_3PCT | 18/20 | 90.0% | -0.14% | **-0.13%** |
| LIMIT_4PCT | 16/20 | 80.0% | -0.25% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 13/20 | 65.0% | +2.72% | **+1.77%** |
| LIMIT_2PCT_LONG | 11/20 | 55.0% | +2.78% | **+1.53%** |
| MARKET_LONG | 20/20 | 100.0% | +1.40% | **+1.40%** |
| LIMIT_ATR_LONG | 8/20 | 40.0% | +3.24% | **+1.30%** |
| LIMIT_4PCT_LONG | 7/20 | 35.0% | +2.86% | **+1.00%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$169.68** / 初期 $100.00 (+69.68%)
- 確定: 1473件 (Win 396 / Loss 466 / Flat 611) / skip 1688件
- 成長率目線: 平均log +0.000359 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $169.68

## 4. Robust Adaptive DryRun ($100)

- 残高: **$100.65** / 初期 $100.00 (+0.65%)
- 確定: 11件 (Win 4 / Loss 2 / Flat 5) / skip 0件
- 成長率目線: 平均log +0.000593 / 幾何平均 +0.059% per trade / maxDD +0.35%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0605 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: VELVET/USDT:USDT `LIMIT_1PCT_LONG` EXPIRED account +0.00% 残高後 $100.65

## 5. Latest Market Context

- 更新: 2026-06-13T18:44:44.621064+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.44% price=64219.9
- Funnel: target 770 → liquid 136 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.8 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +35.62% | $66,766,651.20 |
| AT/USDT:USDT | +11.64% | $1,033,424.31 |
| RIF/USDT:USDT | +10.10% | $6,639,586.21 |
| H/USDT:USDT | +7.99% | $16,087,802.15 |
| BTW/USDT:USDT | +3.86% | $1,525,279.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| JCT/USDT:USDT | below_1h_threshold | +1.86% | +1.42% |
| SPACE/USDT:USDT | below_1h_threshold | +1.86% | +1.42% |
| NAORIS/USDT:USDT | below_1h_threshold | +1.79% | +1.35% |
| LIT/USDT:USDT | below_1h_threshold | +1.76% | +1.32% |
| BRETT/USDT:USDT | below_1h_threshold | +1.67% | +1.24% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
