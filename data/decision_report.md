# Decision Report

- generated_at: 2026-06-12T01:57:55.845975+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6443**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6443, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.10%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.10% | **-0.10%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +6.46% | **+0.65%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| ASK | 20/20 | 100.0% | +0.53% | **+0.53%** |
| LIMIT_1PCT | 18/20 | 90.0% | +0.41% | **+0.37%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +0.79% | **+0.59%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.66% | **+0.53%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.52% | **+0.50%** |
| MARKET_LONG | 20/20 | 100.0% | +0.26% | **+0.26%** |
| ASK_LONG | 20/20 | 100.0% | +0.20% | **+0.20%** |

## 2. $100 Live Portfolio

- 残高: **$95.65** / 初期 $100.00 (-4.35%)
- 確定トレード: 16件 (TP 2 / SL 13 / EXP 1)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $95.65
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.41** / 初期 $100.00 (+51.41%)
- 確定: 1327件 (Win 344 / Loss 427 / Flat 556) / skip 1677件
- 成長率目線: 平均log +0.000313 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `MARKET_LONG` EXPIRED account -0.04% 残高後 $151.41

## 4. Latest Market Context

- 更新: 2026-06-12T01:57:50.340580+00:00 / 保存件数 288/288
- BTC: BULLISH 1h -0.41% price=63353.6
- Funnel: target 782 → liquid 157 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=48, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 83.1 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +110.10% | $132,187,750.60 |
| ESPORTS/USDT:USDT | +29.60% | $27,147,045.00 |
| H/USDT:USDT | +20.81% | $37,740,263.43 |
| XPL/USDT:USDT | +19.32% | $3,092,817.70 |
| SKYAI/USDT:USDT | +19.15% | $13,482,814.54 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +4.97% | +5.38% |
| SKYAI/USDT:USDT | below_1h_threshold | +4.21% | +4.62% |
| NAORIS/USDT:USDT | below_1h_threshold | +3.81% | +4.23% |
| STG/USDT:USDT | below_1h_threshold | +3.68% | +4.09% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.65% | +2.06% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
