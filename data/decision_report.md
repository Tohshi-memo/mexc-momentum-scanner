# Decision Report

- generated_at: 2026-06-16T02:17:46.427385+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6831**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6831, expectancy=-0.05%
- 直近20件 MARKET基準: n=20, expectancy=-2.31%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -2.31% | **-2.31%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_FIB1618 | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_6PCT | 7/20 | 35.0% | +1.15% | **+0.40%** |
| LIMIT_7PCT | 5/20 | 25.0% | +1.23% | **+0.31%** |
| LIMIT_FIB1272 | 9/20 | 45.0% | +0.60% | **+0.27%** |
| LIMIT_10PCT | 2/20 | 10.0% | +2.00% | **+0.20%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET_LONG | 20/20 | 100.0% | +2.34% | **+2.34%** |
| ASK_LONG | 20/20 | 100.0% | +2.21% | **+2.21%** |
| LIMIT_1PCT_LONG | 14/20 | 70.0% | +2.24% | **+1.57%** |
| LIMIT_2PCT_LONG | 10/20 | 50.0% | +2.45% | **+1.22%** |
| LIMIT_4PCT_LONG | 6/20 | 30.0% | +2.44% | **+0.73%** |

## 2. $100 Live Portfolio

- 残高: **$103.01** / 初期 $100.00 (+3.01%)
- 確定トレード: 9件 (TP 5 / SL 4 / EXP 0)
- 最新: ASTEROID/USDT:USDT SL_HIT PnL -4.00% 残高後 $103.01
- 最新戦略メタ: tier=A, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$184.73** / 初期 $100.00 (+84.73%)
- 確定: 1704件 (Win 446 / Loss 530 / Flat 728) / skip 1688件
- 成長率目線: 平均log +0.000360 / 幾何平均 +0.036% per trade / maxDD +7.25%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: SPACE/USDT:USDT `LIMIT_2PCT_LONG` EXPIRED account +0.00% 残高後 $184.73

## 4. Robust Adaptive DryRun ($100)

- 残高: **$97.60** / 初期 $100.00 (-2.40%)
- 確定: 155件 (Win 28 / Loss 30 / Flat 97) / skip 87件
- 成長率目線: 平均log -0.000156 / 幾何平均 -0.016% per trade / maxDD +3.03%
- 次の候補: `LIMIT_2PCT_LONG` (selected_by_robust_growth_score) / robust_score +0.0744 / risk 0.35% / cost 0.15% / daily stop 1.5% / DD stop 8.0%
- 最新: MEGA/USDT:USDT `LIMIT_ATR_LONG` EXPIRED account -0.22% 残高後 $97.60

## 5. Latest Market Context

- 更新: 2026-06-16T02:17:42.113782+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.30% price=66109.5
- Funnel: target 772 → liquid 157 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| ASTEROID/USDT:USDT | +35.41% | $7,181,273.00 |
| ROAM/USDT:USDT | +28.86% | $2,721,279.08 |
| PUFFER/USDT:USDT | +26.89% | $1,347,717.48 |
| SPCXSTOCK/USDT:USDT | +23.14% | $402,637,195.31 |
| VELVET/USDT:USDT | +22.74% | $11,747,896.72 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| PUFFER/USDT:USDT | below_1h_threshold | +3.53% | +3.83% |
| VELVET/USDT:USDT | below_1h_threshold | +2.44% | +2.74% |
| EVAA/USDT:USDT | below_1h_threshold | +2.30% | +2.60% |
| ASTEROID/USDT:USDT | below_1h_threshold | +1.97% | +2.27% |
| BSB/USDT:USDT | below_1h_threshold | +1.82% | +2.12% |

## 6. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
