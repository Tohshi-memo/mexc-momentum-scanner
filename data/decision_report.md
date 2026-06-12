# Decision Report

- generated_at: 2026-06-12T02:10:07.560094+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6444**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6444, expectancy=-0.06%
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
| LIMIT_2PCT_LONG | 16/20 | 80.0% | +1.24% | **+0.99%** |
| LIMIT_FIB1618_LONG | 4/20 | 20.0% | +2.52% | **+0.50%** |
| LIMIT_1PCT_LONG | 17/20 | 85.0% | +0.39% | **+0.33%** |
| LIMIT_ATR_LONG | 14/20 | 70.0% | +0.46% | **+0.32%** |
| LIMIT_3PCT_LONG | 12/20 | 60.0% | +0.26% | **+0.15%** |

## 2. $100 Live Portfolio

- 残高: **$95.65** / 初期 $100.00 (-4.35%)
- 確定トレード: 16件 (TP 2 / SL 13 / EXP 1)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $95.65
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.41** / 初期 $100.00 (+51.41%)
- 確定: 1327件 (Win 344 / Loss 427 / Flat 556) / skip 1678件
- 成長率目線: 平均log +0.000313 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `MARKET_LONG` EXPIRED account -0.04% 残高後 $151.41

## 4. Latest Market Context

- 更新: 2026-06-12T02:10:04.286494+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.25% price=63560.1
- Funnel: target 782 → liquid 156 → pre 50 → checked 50 → surge 1 → strict 0
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 65.5 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +107.23% | $130,635,200.50 |
| ESPORTS/USDT:USDT | +31.10% | $27,630,863.89 |
| XPL/USDT:USDT | +21.91% | $3,612,089.21 |
| SKYAI/USDT:USDT | +19.86% | $13,433,051.60 |
| XMR/USDT:USDT | +19.75% | $9,070,510.00 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| CLO/USDT:USDT | below_1h_threshold | +4.10% | +3.85% |
| PYTH/USDT:USDT | below_1h_threshold | +2.86% | +2.60% |
| XPL/USDT:USDT | below_1h_threshold | +1.80% | +1.55% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.74% | +1.49% |
| UAI/USDT:USDT | below_1h_threshold | +1.19% | +0.94% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
