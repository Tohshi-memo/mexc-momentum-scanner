# Decision Report

- generated_at: 2026-06-12T02:16:16.365865+00:00
- source: `data/experiments.json` + archive=True
- closed shadow trades: **6445**

## 1. 今日の判断

- 結論: **実行可能なMARKET SHORTは安全条件未達。LIMIT/LONGはシャドウで測り、実行側対応まではlive portfolioへ流さない。**
- 全期間 MARKET基準: n=6445, expectancy=-0.06%
- 直近20件 MARKET基準: n=20, expectancy=-0.68%
- live採用条件: `MARKET`のみ / EV >= +0.20% / filled >= 10

### 実行可能ランキング (現executorで正確に測れるもの)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| MARKET | 20/20 | 100.0% | -0.68% | **-0.68%** |

### シャドウ上位 SHORT (まだ実行に直結しない候補を含む)

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_10PCT | 2/20 | 10.0% | +8.00% | **+0.80%** |
| LIMIT_FIB1618 | 2/20 | 10.0% | +6.46% | **+0.65%** |
| LIMIT_9PCT | 2/20 | 10.0% | +6.29% | **+0.63%** |
| LIMIT_ATR | 14/20 | 70.0% | +0.28% | **+0.20%** |
| LIMIT_4PCT | 12/20 | 60.0% | +0.06% | **+0.04%** |

### シャドウ上位 LONG

| strategy | filled/total | fill率 | avg PnL | 実質EV |
|---|---:|---:|---:|---:|
| LIMIT_2PCT_LONG | 15/20 | 75.0% | +1.59% | **+1.19%** |
| LIMIT_FIB1618_LONG | 3/20 | 15.0% | +4.69% | **+0.70%** |
| LIMIT_1PCT_LONG | 16/20 | 80.0% | +0.66% | **+0.53%** |
| LIMIT_ATR_LONG | 13/20 | 65.0% | +0.80% | **+0.52%** |
| LIMIT_3PCT_LONG | 11/20 | 55.0% | +0.64% | **+0.35%** |

## 2. $100 Live Portfolio

- 残高: **$95.65** / 初期 $100.00 (-4.35%)
- 確定トレード: 16件 (TP 2 / SL 13 / EXP 1)
- 最新: UB/USDT:USDT TP_HIT PnL +8.00% 残高後 $95.65
- 最新戦略メタ: tier=B, direction=short, entry=MARKET

## 3. Safe Adaptive DryRun ($100)

- 残高: **$151.41** / 初期 $100.00 (+51.41%)
- 確定: 1327件 (Win 344 / Loss 427 / Flat 556) / skip 1679件
- 成長率目線: 平均log +0.000313 / 幾何平均 +0.031% per trade / maxDD +7.25%
- 次の候補: `MARKET_LONG` (selected_by_recent_avg_log_return) / risk 0.50% / daily stop 2.0% / DD stop 10.0%
- 最新: ID/USDT:USDT `MARKET_LONG` EXPIRED account -0.04% 残高後 $151.41

## 4. Latest Market Context

- 更新: 2026-06-12T02:16:10.600803+00:00 / 保存件数 288/288
- BTC: BULLISH 1h +0.37% price=63636.3
- Funnel: target 782 → liquid 158 → pre 50 → checked 50 → surge 1 → strict 1
- Surge前reject: below_1h_threshold=49, below_relative_strength=0, invalid_ohlcv=0, errors=0
- データ欠損注意: open_interest_usd 0%, oi_change_pct 0%, long_short_ratio 0%

### 24h上昇上位

| symbol | 24h | volume |
|---|---:|---:|
| VELVET/USDT:USDT | +117.51% | $131,517,199.65 |
| ESPORTS/USDT:USDT | +32.62% | $27,747,115.80 |
| XPL/USDT:USDT | +22.86% | $3,710,603.25 |
| SKYAI/USDT:USDT | +19.94% | $13,456,251.67 |
| NAORIS/USDT:USDT | +19.79% | $1,463,979.26 |

### Near Miss

| symbol | reason | 1h | RS |
|---|---|---:|---:|
| VELVET/USDT:USDT | below_1h_threshold | +4.74% | +4.37% |
| CLO/USDT:USDT | below_1h_threshold | +3.99% | +3.62% |
| PYTH/USDT:USDT | below_1h_threshold | +3.07% | +2.70% |
| XPL/USDT:USDT | below_1h_threshold | +2.73% | +2.36% |
| MAGMA/USDT:USDT | below_1h_threshold | +1.47% | +1.10% |

## 5. 次に見るべき不足

- LIMIT戦略は期待値が高く出やすいので、実行するならpending注文/約定待ち/未約定失効をlive側で実装してから昇格。
- near miss銘柄の1h/4h後リターンを保存すると、閾値を5%固定にするべきか判断しやすい。
- funding/OI/long_short_ratioの欠損率が高い場合、取れない銘柄群を別扱いにする。
