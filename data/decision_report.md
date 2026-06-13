# Decision Report

- generated_at: 2026-06-13T18:31:57.852939+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6598**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6598, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-1.00%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -1.00% | **-1.00%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_6PCT | 5/20 | 25.0% | +0.71% | **+0.18%** |
| LIMIT_5PCT | 6/20 | 30.0% | +0.13% | **+0.04%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +0.05% | **+0.01%** |
| LIMIT_3PCT | 17/20 | 85.0% | -0.09% | **-0.08%** |
| LIMIT_4PCT | 15/20 | 75.0% | -0.27% | **-0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.24% | **+1.57%** |
| LIMIT_ATR_LONG | 10/20 | 50.0% | +2.89% | **+1.45%** |
| LIMIT_2PCT_LONG | 12/20 | 60.0% | +2.22% | **+1.33%** |
| MARKET_LONG | 20/20 | 100.0% | +1.00% | **+1.00%** |
| LIMIT_4PCT_LONG | 8/20 | 40.0% | +2.00% | **+0.80%** |

## 2. $100 Live Portfolio

- 残高: **$100.00** / 初期 $100.00 (+0.00%)
- 確定トレード: 0件 (TP 0 / SL 0 / EXP 0)

## 3. Safe Adaptive DryRun ($100)

- 残高: **$168.62** / 初期 $100.00 (+68.62%)
- 確定: 1471件 (Win 395 / Loss 466 / Flat 610) / skip 1688件
- 成長率目線: 平均log +0.000355 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: RIF/USDT:USDT `LIMIT_1PCT_LONG` TP_HIT account +1.00% 残高後 $168.62

## 4. Robust Adaptive DryRun ($100)

- 残高: **$100.22** / 初期 $100.00 (+0.22%)
- 確定: 9件 (Win 3 / Loss 2 / Flat 4) / skip 0件
- 成長率目線: 平均log +0.000250 / 幾何平均 +0.025% per trade / maxDD +0.35%
- 次の候補: `LIMIT_1PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0677 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: RIF/USDT:USDT `LIMIT_5PCT` SL_HIT account -0.35% 残高後 $100.22

## 5. Latest Market Context

- 更新: 2026-06-13T18:31:53.284850+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.36% price=64170.6
- Funnel: target 770 → liquid 136 → pre 50 → checked 50 → surge 3 → strict 2
- Surge前reject: below_1h_threshold=47, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 87.4 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +21.68% | $64,526,234.15 |
| AT/USDT:USDT | +12.79% | $1,021,246.00 |
| RIF/USDT:USDT | +8.65% | $6,508,008.79 |
| H/USDT:USDT | +6.38% | $15,810,807.58 |
| NOT/USDT:USDT | +4.19% | $2,724,648.03 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| NAORIS/USDT:USDT | below_1h_threshold | +1.98% | +1.62% |
| JCT/USDT:USDT | below_1h_threshold | +1.61% | +1.25% |
| SPACE/USDT:USDT | below_1h_threshold | +1.55% | +1.19% |
| CHZ/USDT:USDT | below_1h_threshold | +1.50% | +1.14% |
| EDGE/USDT:USDT | below_1h_threshold | +1.37% | +1.01% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
