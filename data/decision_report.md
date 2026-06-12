# Decision Report

- generated_at: 2026-06-12T02:45:52.230019+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6447**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6447, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.70%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.70% | **-0.70%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +6.46% | **+0.65%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.50% | **+0.35%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.03% | **+0.02%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.52% | **+1.14%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +4.69% | **+0.70%** |
| MARKET_LONG | 20/20 | 100.0% | +0.62% | **+0.62%** |
| ASK_LONG | 20/20 | 100.0% | +0.54% | **+0.54%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.53% | **+0.42%** |

## 2. $100 Live Portfolio

- 残高: **$95.65** / 初期 $100.00 (-4.35%)
- 確定トレード: 16件 (TP 2 / SL 13 / EXP 1)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $95.65
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.41** / 初期 $100.00 (+51.41%)
- 確定: 1327件 (Win 344 / Loss 427 / Flat 556) / skip 1681件
- 成長率目線: 平均log +0.000313 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `MARKET_LONG` EXPIRED account -0.04% 残高後 $151.41

## 4. Latest Market Context

- 更新: 2026-06-12T02:45:47.034151+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.28% price=63576.8
- Funnel: target 782 → liquid 158 → pre 50 → checked 50 → surge 2 → strict 1
- Surge前reject: below_1h_threshold=47, below_relative_strength=1, invalid_ohlcv=0, errors=0
- Strict後reject: 4h RSI 69.0 >= 65=1
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +111.26% | $133,768,570.89 |
| XPL/USDT:USDT | +23.31% | $3,909,748.06 |
| SKYAI/USDT:USDT | +20.00% | $13,661,438.89 |
| CLO/USDT:USDT | +17.13% | $1,264,182.78 |
| NAORIS/USDT:USDT | +16.95% | $1,504,648.06 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| MAGMA/USDT:USDT | below_relative_strength | +5.00% | +4.72% |
| PYTH/USDT:USDT | below_1h_threshold | +4.55% | +4.27% |
| INJ/USDT:USDT | below_1h_threshold | +3.32% | +3.05% |
| XPL/USDT:USDT | below_1h_threshold | +3.04% | +2.76% |
| UB/USDT:USDT | below_1h_threshold | +2.66% | +2.38% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
